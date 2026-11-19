#!/usr/bin/env python3
"""Build the DIO to DIO static portfolio from unchanged Markdown/PDF sources."""
from __future__ import annotations
import hashlib, html, json, re, shutil, subprocess, sys, urllib.request
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import quote, urljoin

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site"
CATALOGUE_START = "<!-- ANALYSIS_CATALOGUE:START -->"
CATALOGUE_END = "<!-- ANALYSIS_CATALOGUE:END -->"
PANDOC_FROM = (
    "markdown+yaml_metadata_block+raw_tex+raw_html+pipe_tables+"
    "fenced_code_attributes+tex_math_dollars+footnotes+task_lists"
)

def fail(message: str) -> None:
    print(f"BUILD ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

def safe_relative(raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts:
        fail(f"Unsafe repository path in metadata: {raw}")
    return path

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()



CHUNK_ORDER = [
    "C0_identity_invariant",
    "C1_reconstruction_environments",
    "C2_work_positioning",
    "C3_reconstruction_mechanics",
    "C4_k6",
    "C5_failures_robustness",
    "C6_machine_readable_representation",
]
REGISTRY_MINIMUM = (2, 10, 0)
REPOSITORY = "dan-beranek/dio-to-dio"
MANIFEST_FILENAME = "resolved-artifact-metadata.json"
REGISTRY_SNAPSHOT_FILENAME = "keyword-registry.resolved.json"


def parse_semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", value or "")
    if not match:
        fail(f"Invalid canonical keyword registry version: {value!r}")
    return tuple(map(int, match.groups()))


def load_canonical_keyword_registry(source: dict) -> tuple[dict, str, str]:
    raw_url = (
        "https://raw.githubusercontent.com/"
        f"{source['repository']}/{source['ref']}/{source['file']}"
    )
    fetched_from = raw_url
    try:
        request = urllib.request.Request(
            raw_url,
            headers={"Accept": "application/json", "User-Agent": "DIO-to-DIO-metadata-builder"}
        )
        with urllib.request.urlopen(request, timeout=20) as response:
            registry_text = response.read().decode("utf-8")
    except Exception as exc:
        snapshot = ROOT / safe_relative(source["snapshot_path"])
        if not snapshot.is_file():
            fail(
                "Unable to fetch the canonical DIO/ODI keyword registry and no "
                f"committed snapshot is available: {exc}"
            )
        registry_text = snapshot.read_text(encoding="utf-8")
        fetched_from = source["snapshot_path"]

    try:
        registry = json.loads(registry_text)
    except json.JSONDecodeError as exc:
        fail(f"Canonical keyword registry is not valid JSON: {exc}")

    version = parse_semver(registry.get("registry_version", ""))
    if (
        registry.get("status") != source.get("status_required")
        or version[0] != int(source.get("compatible_major", -1))
        or version < REGISTRY_MINIMUM
    ):
        fail(
            "Expected canonical-approved keyword registry >= 2.10.0 "
            f"within compatible major 2; received {registry.get('registry_version')!r} "
            f"with status {registry.get('status')!r}."
        )
    return registry, registry_text, fetched_from


def resolve_surface_profile(registry: dict, profile_id: str, profile: dict) -> dict:
    if profile.get("status") != "canonical-approved":
        fail(f"{profile_id}: surface profile is not canonical-approved.")
    if profile.get("scope") != "derived-public-webpage":
        fail(f"{profile_id}: expected scope derived-public-webpage.")

    selectors = profile.get("chunks", {})
    chunks = registry.get("chunks", {})
    if set(selectors) != set(CHUNK_ORDER):
        fail(f"{profile_id}: selectors must provide exactly the canonical C0–C6 chunks.")
    if selectors.get("C0_identity_invariant") != "all":
        fail(f"{profile_id}: C0 must be exported in full.")
    if not isinstance(selectors.get("C1_reconstruction_environments"), list):
        fail(f"{profile_id}: C1 must be an explicit ordered selection.")
    if selectors.get("C4_k6") not in ("all", "none"):
        fail(f"{profile_id}: K6 must be complete or absent.")

    resolved = []
    resolved_chunks = {}
    seen = set()
    for chunk_name in CHUNK_ORDER:
        source_terms = chunks.get(chunk_name, {}).get("terms")
        if not isinstance(source_terms, list):
            fail(f"{profile_id}: canonical chunk {chunk_name} is missing.")
        selector = selectors[chunk_name]
        if selector == "all":
            selected = list(source_terms)
        elif selector == "none":
            selected = []
        elif isinstance(selector, list):
            selected = selector
            if chunk_name != "C2_work_positioning":
                positions = [
                    source_terms.index(term) if term in source_terms else -1
                    for term in selected
                ]
                if (
                    -1 in positions
                    or positions != sorted(positions)
                    or len(set(selected)) != len(selected)
                ):
                    fail(
                        f"{profile_id}: {chunk_name} must preserve canonical order "
                        "and contain unique canonical terms."
                    )
            elif len({term.casefold() for term in selected}) != len(selected):
                fail(f"{profile_id}: C2 contains duplicate terms.")
        else:
            fail(f"{profile_id}: invalid selector for {chunk_name}.")

        resolved_chunks[chunk_name] = selected
        for term in selected:
            folded = term.casefold()
            if folded not in seen:
                seen.add(folded)
                resolved.append(term)

    if "resolved_keywords" in profile:
        fail(f"{profile_id}: derived profiles must resolve from selectors, not stored keyword copies.")
    c0 = set(chunks["C0_identity_invariant"]["terms"])
    required_rationales = set(resolved) - c0
    rationales = profile.get("term_rationales", {})
    if (
        set(rationales) != required_rationales
        or any(not str(rationales.get(term, "")).strip() for term in required_rationales)
    ):
        missing = sorted(required_rationales - set(rationales))
        extra = sorted(set(rationales) - required_rationales)
        fail(f"{profile_id}: rationale coverage mismatch; missing={missing}; extra={extra}.")
    if len(resolved) != len({term.casefold() for term in resolved}):
        fail(f"{profile_id}: resolved keyword sequence contains duplicates.")

    return {
        "profile": profile,
        "keywords": resolved,
        "chunks": resolved_chunks,
    }


def load_page_surface_profiles(site_url: str, records: list) -> tuple[dict, dict, str, str, dict]:
    config_path = ROOT / "metadata" / "artifact-metadata.json"
    if not config_path.is_file():
        fail("Missing metadata/artifact-metadata.json.")
    artifact_config = json.loads(config_path.read_text(encoding="utf-8"))
    registry_source = artifact_config.get("registry_source", {})
    registry, registry_text, fetched_from = load_canonical_keyword_registry(registry_source)

    artifacts = artifact_config.get("artifacts", [])
    if len(artifacts) != len(records) + 1:
        fail(
            f"Expected one homepage profile plus {len(records)} report profiles; "
            f"found {len(artifacts)}."
        )
    by_page_key = {}
    resolved_artifacts = []
    expected = {
        "dio-to-dio-home": {
            "path": "index.html",
            "url": site_url,
            "role": "homepage",
        }
    }
    for record in records:
        expected[record["id"]] = {
            "path": record["html"],
            "url": urljoin(site_url, record["html"]),
            "role": "report",
        }

    for artifact in artifacts:
        page_key = artifact.get("page_key")
        if not page_key or page_key in by_page_key:
            fail(f"Missing or duplicate page_key in artifact metadata: {page_key!r}.")
        if page_key not in expected:
            fail(f"Unknown DIO to DIO page_key in artifact metadata: {page_key!r}.")
        expected_page = expected[page_key]
        paths = artifact.get("paths")
        urls = artifact.get("urls")
        if paths != [expected_page["path"]] or urls != [expected_page["url"]]:
            fail(f"{artifact.get('id')}: page path/URL does not match the source catalogue.")
        if not artifact.get("keyword_profile_id"):
            fail(f"{artifact.get('id')}: missing keyword_profile_id.")

        profile_id = artifact["keyword_profile_id"]
        profile = registry.get("surface_profiles", {}).get(profile_id)
        projection = resolve_surface_profile(registry, profile_id, profile)
        surface = profile.get("surface", {})
        if (
            surface.get("repository") != REPOSITORY
            or surface.get("page_key") != page_key
            or surface.get("paths") != paths
            or surface.get("urls") != urls
        ):
            fail(f"{profile_id}: canonical surface identity does not match local page metadata.")

        page_entity_id = expected_page["url"] + (
            "#webpage" if expected_page["role"] == "report" else "#webpage"
        )
        item = {
            **artifact,
            "status": profile["status"],
            "scope": profile["scope"],
            "purpose": profile.get("purpose", ""),
            "keyword_chunks": projection["chunks"],
            "keywords": projection["keywords"],
            "keyword_rationales": profile.get("term_rationales", {}),
            "schema_entity_id": page_entity_id,
            "in_language": "en",
        }
        by_page_key[page_key] = item
        resolved_artifacts.append(item)

    if set(by_page_key) != set(expected):
        missing = sorted(set(expected) - set(by_page_key))
        extra = sorted(set(by_page_key) - set(expected))
        fail(f"Page profile inventory mismatch; missing={missing}; extra={extra}.")

    registry_sha256 = hashlib.sha256(registry_text.encode("utf-8")).hexdigest()
    registry_info = {
        "repository": registry_source["repository"],
        "file": registry_source["file"],
        "ref": registry_source["ref"],
        "registry_version": registry["registry_version"],
        "status": registry["status"],
        "sha256": registry_sha256,
        "fetched_from": fetched_from,
        "canonical_discovery": registry_source.get("registry_discovery"),
        "resolved_snapshot_path": REGISTRY_SNAPSHOT_FILENAME,
    }
    manifest = {
        "schema_version": "1.0.0",
        "site": artifact_config.get("site", {}),
        "author": artifact_config.get("author", {}),
        "keyword_registry": registry_info,
        "artifacts": resolved_artifacts,
    }
    return by_page_key, manifest, registry_text, REGISTRY_SNAPSHOT_FILENAME, registry_info


def upsert_head_metadata(
    html_text: str,
    keywords: list[str],
    profile_id: str,
    registry_version: str,
    manifest_url: str,
) -> str:
    def upsert_meta(source: str, name: str, value: str) -> str:
        escaped_name = re.escape(name)
        pattern = re.compile(
            rf"<meta\b(?=[^>]*\bname\s*=\s*(['\"]){escaped_name}\1)[^>]*>",
            re.IGNORECASE,
        )
        tag = (
            f'<meta name="{html.escape(name, quote=True)}" '
            f'content="{html.escape(value, quote=True)}">'
        )
        matches = list(pattern.finditer(source))
        if len(matches) > 1:
            fail(f"Duplicate meta name={name!r} in generated page head.")
        if matches:
            match = matches[0]
            return source[:match.start()] + tag + source[match.end():]
        description = re.search(
            r"<meta\b(?=[^>]*\bname\s*=\s*(['\"])description\1)[^>]*>",
            source,
            re.IGNORECASE,
        )
        if not description:
            fail(f"Cannot add {name!r}: page has no unique meta description.")
        return source[:description.end()] + "\n  " + tag + source[description.end():]

    html_text = upsert_meta(html_text, "keywords", ", ".join(keywords))
    html_text = upsert_meta(html_text, "dio-odi:keyword-profile", profile_id)
    html_text = upsert_meta(html_text, "dio-odi:keyword-registry-version", registry_version)

    href = html.escape(manifest_url, quote=True)
    link_pattern = re.compile(
        r"<link\b(?=[^>]*\brel\s*=\s*(['\"])describedby\1)[^>]*>",
        re.IGNORECASE,
    )
    describedby = list(link_pattern.finditer(html_text))
    link_tag = (
        '<link rel="describedby" type="application/json" '
        f'href="{href}" title="Resolved page metadata and keyword profiles">'
    )
    if len(describedby) > 1:
        fail("Duplicate rel=describedby links in generated page head.")
    if describedby:
        match = describedby[0]
        html_text = html_text[:match.start()] + link_tag + html_text[match.end():]
    else:
        head_end = re.search(r"</head\s*>", html_text, re.IGNORECASE)
        if not head_end:
            fail("Cannot add resolved metadata link: no closing </head>.")
        html_text = html_text[:head_end.start()] + link_tag + "\n  " + html_text[head_end.start():]
    return html_text


class JsonLdCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.payloads = []
        self.capture = False
        self.buffer = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag.lower() == "script" and dict(attrs).get("type", "").lower() == "application/ld+json":
            self.capture = True
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self.capture:
            self.payloads.append("".join(self.buffer).strip())
            self.capture = False
            self.buffer = []


def validate_published_page_metadata(
    page_html: str,
    page_key: str,
    profile: dict,
    registry_version: str,
    manifest_url: str,
    dataset_keywords: list,
) -> None:
    def meta_values(name: str) -> list[str]:
        result = []
        for match in re.finditer(r"<meta\b[^>]*>", page_html, re.IGNORECASE):
            tag = match.group(0)
            name_match = re.search(r"\bname\s*=\s*(['\"])(.*?)\1", tag, re.IGNORECASE)
            content_match = re.search(r"\bcontent\s*=\s*(['\"])(.*?)\1", tag, re.IGNORECASE)
            if name_match and content_match and name_match.group(2).lower() == name.lower():
                result.append(html.unescape(content_match.group(2)))
        return result

    expected_keywords = profile["keywords"]
    if meta_values("keywords") != [", ".join(expected_keywords)]:
        fail(f"{page_key}: HTML meta keywords differ from the resolved canonical profile.")
    if meta_values("dio-odi:keyword-profile") != [profile["keyword_profile_id"]]:
        fail(f"{page_key}: HTML keyword profile identifier is missing or incorrect.")
    if meta_values("dio-odi:keyword-registry-version") != [registry_version]:
        fail(f"{page_key}: HTML keyword registry version is missing or incorrect.")
    if manifest_url not in page_html or 'rel="describedby"' not in page_html:
        fail(f"{page_key}: page does not link to the resolved keyword metadata manifest.")

    parser = JsonLdCollector()
    parser.feed(page_html)
    parser.close()
    graphs = []
    for payload in parser.payloads:
        try:
            document = json.loads(payload)
        except json.JSONDecodeError as exc:
            fail(f"{page_key}: malformed embedded JSON-LD: {exc}")
        if isinstance(document, dict):
            graphs.extend(document.get("@graph", []))
            if "@graph" not in document:
                graphs.append(document)

    matching = [
        node for node in graphs
        if isinstance(node, dict) and node.get("@id") == profile["schema_entity_id"]
    ]
    if len(matching) != 1:
        fail(f"{page_key}: expected exactly one primary Schema.org page entity in JSON-LD.")
    if matching[0].get("keywords") != expected_keywords:
        fail(f"{page_key}: Schema.org page keywords differ from the canonical profile.")

    datasets = [node for node in graphs if isinstance(node, dict) and node.get("@type") == "Dataset"]
    if len(datasets) != 1 or datasets[0].get("keywords") != dataset_keywords:
        fail(f"{page_key}: page-surface metadata changed the independent Dataset keyword profile.")
    report_works = [
        node for node in graphs
        if isinstance(node, dict) and isinstance(node.get("@id"), str) and node["@id"].endswith("#report")
    ]
    if any("keywords" in node for node in report_works):
        fail(f"{page_key}: page-surface keywords leaked into a report CreativeWork entity.")


def render_markdown(source: Path, filter_path: Path) -> str:
    filters = [filter_path]
    if source.name == "Claude-DIO-ODI-Reflexive-Analysis-Reconstruction-Resilience.md":
        table_filter = ROOT / "scripts" / "filters" / "claude-table-cards.lua"
        if not table_filter.is_file():
            fail("Missing Claude Chapter 8 table-presentation filter.")
        filters.append(table_filter)
    command = [
        "pandoc", f"--from={PANDOC_FROM}", "--to=html5", "--wrap=none",
        "--mathjax", *[f"--lua-filter={item}" for item in filters], str(source)
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, encoding="utf-8", capture_output=True)
    if result.returncode != 0:
        fail(f"Pandoc failed for {source.relative_to(ROOT)}:\n{result.stderr}")
    if not result.stdout.strip():
        fail(f"Pandoc produced empty HTML for {source.relative_to(ROOT)}")
    return result.stdout



class ReportHeadingCollector(HTMLParser):
    """Collect all linkable H1–H6 headings from the rendered report body."""
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.headings = []
        self.current = None

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self.current is None:
            attributes = dict(attrs)
            self.current = {
                "level": int(tag[1]),
                "id": attributes.get("id"),
                "text": []
            }

    def handle_data(self, data: str) -> None:
        if self.current is not None:
            self.current["text"].append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.current is not None and tag == f"h{self.current['level']}":
            heading = self.current
            title = " ".join("".join(heading["text"]).split())
            if title:
                self.headings.append({
                    "level": heading["level"],
                    "id": heading["id"],
                    "title": title
                })
            self.current = None


def report_toc_markup(html_fragment: str, page_url: str) -> str:
    """Build a nested, absolute-URL table of contents for one report page."""
    parser = ReportHeadingCollector()
    parser.feed(html_fragment)
    parser.close()

    if not parser.headings:
        return ""

    roots = []
    stack = [(0, roots)]
    for heading in parser.headings:
        if not heading["id"]:
            fail(f"Report heading has no anchor id: {heading['title']}")
        node = {**heading, "children": []}
        while stack[-1][0] >= node["level"]:
            stack.pop()
        stack[-1][1].append(node)
        stack.append((node["level"], node["children"]))

    def render_items(items: list) -> str:
        rendered = []
        for item in items:
            fragment = quote(item["id"], safe="-._~")
            href = html.escape(f"{page_url}#{fragment}", quote=True)
            label = html.escape(item["title"])
            children = render_items(item["children"])
            nested = f'<ol class="report-toc-list">{children}</ol>' if children else ""
            rendered.append(
                f'<li class="report-toc-item report-toc-level-{item["level"]}">'
                f'<a href="{href}">{label}</a>{nested}</li>'
            )
        return "\n".join(rendered)

    return f"""<aside class="report-toc" data-report-toc>
  <button class="report-toc-toggle" type="button" aria-expanded="false" aria-controls="report-toc-panel">
    <span class="report-toc-toggle-label">Contents</span>
    <span class="report-toc-toggle-chevron" aria-hidden="true"></span>
  </button>
  <nav class="report-toc-panel" id="report-toc-panel" aria-label="Report contents" aria-hidden="true">
    <div class="report-toc-panel-header">
      <p>On this page</p>
      <button class="report-toc-close" type="button" aria-label="Close contents">×</button>
    </div>
    <ol class="report-toc-list">{render_items(roots)}</ol>
  </nav>
</aside>"""



def validate_structured_data(config: dict) -> None:
    person = config.get("person", {})
    project = config.get("project", {})
    website = config.get("website", {})
    required_person_fields = ("@id", "@type", "name", "url", "sameAs")
    if any(not person.get(key) for key in required_person_fields):
        fail("metadata/structured-data.json has incomplete person identity metadata.")
    if person["@type"] != "Person":
        fail("The canonical person node must use @type Person.")
    if person["@id"] != "https://danielberanek.cz/#person":
        fail("The canonical person @id must remain https://danielberanek.cz/#person.")
    if "https://orcid.org/0009-0004-0050-0264" not in person["sameAs"]:
        fail("The canonical person sameAs list must include the ORCID URI.")
    if not project.get("name") or not project.get("description") or not project.get("sameAs"):
        fail("metadata/structured-data.json has incomplete project metadata.")
    if not website.get("name") or not website.get("description") or not website.get("inLanguage"):
        fail("metadata/structured-data.json has incomplete website metadata.")
    dataset = config.get("dataset", {})
    if not dataset.get("@id") or not dataset.get("name") or not dataset.get("description"):
        fail("metadata/structured-data.json has incomplete dataset metadata.")
    expected_about = {
        "https://vocab.danielberanek.cz/dio-odi/#DIO",
        "https://vocab.danielberanek.cz/dio-odi/#ODI"
    }
    if set(dataset.get("about", [])) != expected_about:
        fail("Dataset about links must identify the canonical DIO and ODI SKOS concepts.")

def distribution_records(records: list, site_url: str, integrity_records: list) -> list:
    hashes = {item["id"]: item for item in integrity_records}
    distributions = []
    for record in records:
        integrity = hashes[record["id"]]
        items = [
            ("markdown", "Markdown", "sources/markdown/" + Path(record["markdown"]).name, "text/markdown", "https://www.iana.org/assignments/media-types/text/markdown", integrity["markdown_sha256"]),
            ("pdf", "PDF", "sources/pdf/" + Path(record["pdf"]).name, "application/pdf", "https://www.iana.org/assignments/media-types/application/pdf", integrity["pdf_sha256"]),
            ("html", "HTML", record["html"], "text/html", "https://www.iana.org/assignments/media-types/text/html", None)
        ]
        for key, label, path, media_type, media_type_uri, digest in items:
            distributions.append({
                "id": f"{record['id']}-{key}",
                "record_id": record["id"],
                "format": key,
                "label": label,
                "title": f"{record['model']} — {label}",
                "url": urljoin(site_url, path),
                "media_type": media_type,
                "media_type_uri": media_type_uri,
                "sha256": digest
            })
    distributions.append({
        "id": "source-integrity",
        "record_id": None,
        "format": "json",
        "label": "Source integrity manifest",
        "title": "Source integrity manifest — SHA-256",
        "url": urljoin(site_url, "source-integrity.json"),
        "media_type": "application/json",
        "media_type_uri": "https://www.iana.org/assignments/media-types/application/json",
        "sha256": None
    })
    return distributions


def report_schema_nodes(record: dict, site_url: str, config: dict, keyword_profiles: dict | None = None) -> tuple[dict, dict]:
    page_url = urljoin(site_url, record["html"])
    page_id = page_url + "#webpage"
    work_id = page_url + "#report"
    website_id = site_url + "#website"
    dataset_id = config["dataset"]["@id"]
    person_ref = {"@id": config["person"]["@id"]}
    page = {
        "@type": "WebPage",
        "@id": page_id,
        "url": page_url,
        "name": record["title"],
        "description": record["description"],
        "inLanguage": config["website"]["inLanguage"],
        "isPartOf": {"@id": website_id},
        "mainEntity": {"@id": work_id}
    }
    if keyword_profiles is not None:
        page_profile = keyword_profiles.get(record["id"])
        if page_profile is None:
            fail(f"Missing page keyword profile for report: {record['id']}")
        page["keywords"] = page_profile["keywords"]
    work = {
        "@type": "CreativeWork",
        "@id": work_id,
        "name": record["title"],
        "description": record["description"],
        "url": page_url,
        "inLanguage": config["website"]["inLanguage"],
        "isPartOf": [{"@id": website_id}, {"@id": dataset_id}],
        "about": [{"@id": uri} for uri in config["dataset"]["about"]],
        "publisher": person_ref,
        "mainEntityOfPage": {"@id": page_id}
    }
    return page, work


def build_jsonld(config: dict, site_url: str, records: list, integrity_records: list, current_record: dict | None = None, keyword_profiles: dict | None = None) -> dict:
    person = dict(config["person"])
    website_id = site_url + "#website"
    project_id = site_url + "#project"
    dataset_config = config["dataset"]
    dataset_id = dataset_config["@id"]
    person_ref = {"@id": person["@id"]}
    website_ref = {"@id": website_id}
    project_ref = {"@id": project_id}
    dataset_ref = {"@id": dataset_id}
    distributions = distribution_records(records, site_url, integrity_records)

    graph = [
        person,
        {
            "@type": "WebSite",
            "@id": website_id,
            "url": site_url,
            "name": config["website"]["name"],
            "description": config["website"]["description"],
            "inLanguage": config["website"]["inLanguage"],
            "publisher": person_ref
        },
        {
            "@type": "ResearchProject",
            "@id": project_id,
            "name": config["project"]["name"],
            "description": config["project"]["description"],
            "url": site_url,
            "sameAs": config["project"]["sameAs"],
            "founder": person_ref,
            "subjectOf": dataset_ref
        },
        {
            "@type": "Dataset",
            "@id": dataset_id,
            "name": dataset_config["name"],
            "description": dataset_config["description"],
            "url": site_url,
            "inLanguage": config["website"]["inLanguage"],
            "creator": person_ref,
            "publisher": person_ref,
            "about": [{"@id": uri} for uri in dataset_config["about"]],
            "keywords": dataset_config["keywords"],
            "hasPart": [
                {"@id": urljoin(site_url, record["html"]) + "#report"}
                for record in records
            ],
            "distribution": [
                {"@id": dataset_id + "-distribution-" + item["id"]}
                for item in distributions
            ]
        }
    ]

    if current_record is None:
        report_pages = []
        for record in records:
            page, work = report_schema_nodes(record, site_url, config, keyword_profiles)
            graph.extend([page, work])
            report_pages.append({"@id": page["@id"]})
        graph.append({
            "@type": "CollectionPage",
            "@id": site_url + "#webpage",
            "url": site_url,
            "name": config["website"]["name"],
            "description": config["website"]["description"],
            "inLanguage": config["website"]["inLanguage"],
            "isPartOf": website_ref,
            "mainEntity": project_ref,
            "hasPart": report_pages,
            "author": person_ref,
            "publisher": person_ref
        })
        if keyword_profiles is not None:
            home_profile = keyword_profiles.get("dio-to-dio-home")
            if home_profile is None:
                fail("Missing page keyword profile for the DIO to DIO homepage.")
            graph[-1]["keywords"] = home_profile["keywords"]
    else:
        page, work = report_schema_nodes(current_record, site_url, config, keyword_profiles)
        graph.extend([page, work])

    for item in distributions:
        node = {
            "@type": "DataDownload",
            "@id": dataset_id + "-distribution-" + item["id"],
            "name": item["title"],
            "contentUrl": item["url"],
            "encodingFormat": item["media_type"],
            "isPartOf": dataset_ref
        }
        if item["sha256"]:
            node["sha256"] = item["sha256"]
        graph.append(node)

    payload = {"@context": "https://schema.org", "@graph": graph}
    serialized = json.dumps(payload, ensure_ascii=False)
    parsed = json.loads(serialized)
    ids = [node["@id"] for node in parsed["@graph"] if isinstance(node, dict) and node.get("@id")]
    if len(ids) != len(set(ids)):
        fail("Generated JSON-LD contains duplicate @id values in one graph.")
    people = [node for node in parsed["@graph"] if node.get("@type") == "Person"]
    if len(people) != 1 or people[0].get("@id") != config["person"]["@id"]:
        fail("Generated JSON-LD does not contain exactly one canonical Person node.")
    if "https://orcid.org/0009-0004-0050-0264" not in people[0].get("sameAs", []):
        fail("Generated JSON-LD lost the canonical ORCID sameAs link.")
    datasets = [node for node in parsed["@graph"] if node.get("@type") == "Dataset"]
    if len(datasets) != 1 or datasets[0].get("@id") != dataset_id:
        fail("Generated JSON-LD does not contain exactly one canonical Dataset node.")
    return parsed


def build_dcat_exports(config: dict, site_url: str, records: list, integrity_records: list) -> tuple[str, str]:
    dataset = config["dataset"]
    dataset_id = dataset["@id"]
    person_id = config["person"]["@id"]
    distributions = distribution_records(records, site_url, integrity_records)
    graph = [{
        "@id": dataset_id,
        "@type": "dcat:Dataset",
        "dcterms:title": {"@value": dataset["name"], "@language": "en"},
        "dcterms:description": {"@value": dataset["description"], "@language": "en"},
        "dcterms:creator": {"@id": person_id},
        "dcterms:publisher": {"@id": person_id},
        "dcterms:isPartOf": {"@id": site_url + "#project"},
        "dcterms:language": {"@id": "http://id.loc.gov/vocabulary/iso639-1/en"},
        "dcat:landingPage": {"@id": site_url},
        "dcat:keyword": [{"@value": keyword, "@language": "en"} for keyword in dataset["keywords"]],
        "dcat:theme": [{"@id": uri} for uri in dataset["about"]],
        "dcat:distribution": [
            {"@id": dataset_id + "-distribution-" + item["id"]}
            for item in distributions
        ]
    }]
    for item in distributions:
        node = {
            "@id": dataset_id + "-distribution-" + item["id"],
            "@type": "dcat:Distribution",
            "dcterms:title": {"@value": item["title"], "@language": "en"},
            "dcat:accessURL": {"@id": item["url"]},
            "dcat:mediaType": {"@id": item["media_type_uri"]}
        }
        if item["sha256"]:
            node["spdx:checksum"] = {
                "@type": "spdx:Checksum",
                "spdx:algorithm": {"@id": "spdx:checksumAlgorithm_sha256"},
                "spdx:checksumValue": item["sha256"]
            }
        graph.append(node)
    jsonld = {
        "@context": {
            "dcat": "http://www.w3.org/ns/dcat#",
            "dcterms": "http://purl.org/dc/terms/",
            "spdx": "http://spdx.org/rdf/terms#"
        },
        "@graph": graph
    }

    def ttl_literal(value: str) -> str:
        return json.dumps(value, ensure_ascii=False) + "@en"

    lines = [
        "@prefix dcat: <http://www.w3.org/ns/dcat#> .",
        "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "@prefix spdx: <http://spdx.org/rdf/terms#> .",
        "",
        f"<{dataset_id}> a dcat:Dataset ;",
        f"  dcterms:title {ttl_literal(dataset['name'])} ;",
        f"  dcterms:description {ttl_literal(dataset['description'])} ;",
        f"  dcterms:creator <{person_id}> ;",
        f"  dcterms:publisher <{person_id}> ;",
        f"  dcterms:isPartOf <{site_url}#project> ;",
        "  dcterms:language <http://id.loc.gov/vocabulary/iso639-1/en> ;",
        f"  dcat:landingPage <{site_url}> ;",
        "  dcat:keyword " + ", ".join(ttl_literal(keyword) for keyword in dataset["keywords"]) + " ;",
        "  dcat:theme " + ", ".join(f"<{uri}>" for uri in dataset["about"]) + " ;",
        "  dcat:distribution " + ",\n    ".join(
            f"<{dataset_id}-distribution-{item['id']}>" for item in distributions
        ) + " .",
        ""
    ]
    for index, item in enumerate(distributions):
        lines.extend([
            f"<{dataset_id}-distribution-{item['id']}> a dcat:Distribution ;",
            f"  dcterms:title {ttl_literal(item['title'])} ;",
            f"  dcat:accessURL <{item['url']}> ;",
            f"  dcat:mediaType <{item['media_type_uri']}>"
        ])
        if item["sha256"]:
            lines[-1] += " ;"
            lines.extend([
                "  spdx:checksum [",
                "    a spdx:Checksum ;",
                "    spdx:algorithm spdx:checksumAlgorithm_sha256 ;",
                f"    spdx:checksumValue {json.dumps(item['sha256'])}",
                "  ]"
            ])
        lines[-1] += " ."
        lines.append("")
    return json.dumps(jsonld, ensure_ascii=False, indent=2) + "\n", "\n".join(lines)

def jsonld_script(payload: dict) -> str:
    serialized = json.dumps(payload, ensure_ascii=False, indent=2)
    # Prevent a metadata string from prematurely closing the script element.
    serialized = serialized.replace("</", "<\\/")
    return '  <script type="application/ld+json">\n' + serialized + '\n  </script>\n'

def card(record: dict, index: int, total: int) -> str:
    model = html.escape(record["model"])
    title = html.escape(record["title"])
    description = html.escape(record["description"])
    snapshot = html.escape(record["observation_snapshot"])
    href = html.escape(record["html"], quote=True)
    md_href = html.escape(f"sources/markdown/{Path(record['markdown']).name}", quote=True)
    pdf_href = html.escape(f"sources/pdf/{Path(record['pdf']).name}", quote=True)
    return f'''<article class="analysis-card">
  <div class="analysis-card-meta"><span>{index:02d} / {total:02d}</span><span>{model}</span><time>{snapshot}</time></div>
  <h3><a href="{href}">{title}</a></h3>
  <p>{description}</p>
  <div class="analysis-card-links"><a href="{md_href}">Markdown</a><a href="{pdf_href}">PDF</a><a href="{href}">HTML</a></div>
</article>'''

EXTERNAL_RESOURCES = [
    ("https://danielberanek.cz/manifest-dio/", "DIO/ODI Hub"),
    ("https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Ber%C3%A1nek%2C%20Daniel%22&l=list&p=1&s=10&sort=bestmatch", "Zenodo"),
    ("https://orcid.org/0009-0004-0050-0264", "Author profile (ORCID)"),
    ("https://vocab.danielberanek.cz/dio-odi/", "Reference Vocabulary & Model"),
    ("https://github.com/dan-beranek/dio-to-dio", "Website repository (GitHub)"),
    ("https://dan-beranek.github.io/dio-odi-autorsky-koncept/en/partnerships/", "Partnership Proposal", "partnership-link"),
]


def resource_menu(mobile: bool = False) -> str:
    links_class = "mobile-resource-links" if mobile else "resource-links"
    panel_id = "mobile-external-resources" if mobile else "desktop-external-resources"
    links = "\n            ".join(
        (
            f'<a class="{item[2]}" href="{html.escape(item[0], quote=True)}" target="_blank" rel="noopener noreferrer">{html.escape(item[1])}<span aria-hidden="true">↗</span></a>'
            if len(item) > 2
            else f'<a href="{html.escape(item[0], quote=True)}" target="_blank" rel="noopener noreferrer">{html.escape(item[1])}<span aria-hidden="true">↗</span></a>'
        )
        for item in EXTERNAL_RESOURCES
    )
    if mobile:
        return f'''<details class="mobile-resource-nav">
          <summary aria-controls="{panel_id}">External resources <span class="resource-chevron" aria-hidden="true"></span></summary>
          <div class="{links_class}" id="{panel_id}">
            {links}
          </div>
        </details>'''
    return f'''<div class="resource-nav">
          <button class="resource-trigger" type="button" aria-haspopup="true" aria-expanded="false" aria-controls="{panel_id}">
            External resources <span class="resource-chevron" aria-hidden="true"></span>
          </button>
          <div class="{links_class}" id="{panel_id}">
            {links}
          </div>
        </div>'''


def report_header_navigation() -> str:
    desktop = f'''<nav class="primary-nav" aria-label="Report navigation">
        <a href="../">All analyses</a>
        <a href="https://github.com/dan-beranek/dio-to-dio" target="_blank" rel="noopener noreferrer">Website repository (GitHub)</a>
        {resource_menu()}
      </nav>'''
    mobile = f'''<details class="mobile-menu">
        <summary class="mobile-menu-toggle" aria-label="Toggle navigation"><span class="menu-icon" aria-hidden="true"></span></summary>
        <div class="mobile-menu-panel">
          <nav aria-label="Mobile navigation">
            <a href="../">All analyses</a>
            <a href="https://github.com/dan-beranek/dio-to-dio">Source repository</a>
            {resource_menu(True)}
          </nav>
        </div>
      </details>'''
    return desktop + "\n      " + mobile


def report_page(record: dict, index: int, total: int, html_fragment: str, site_url: str, structured_data: dict, integrity_records: list, all_records: list, keyword_profiles: dict, registry_version: str, manifest_url: str) -> str:
    model = html.escape(record["model"])
    title = html.escape(record["title"])
    description = html.escape(record["description"])
    graph = html.escape(record["graph_approach"])
    prompt = html.escape(record["prompt_arrangement"])
    snapshot = html.escape(record["observation_snapshot"])
    page_url = urljoin(site_url, record["html"])
    toc_markup = report_toc_markup(html_fragment, page_url)
    canonical = html.escape(page_url, quote=True)
    page_profile = keyword_profiles.get(record["id"])
    if page_profile is None:
        fail(f"Missing keyword surface profile for report {record['id']}.")
    schema_markup = jsonld_script(
        build_jsonld(
            structured_data, site_url, all_records, integrity_records,
            current_record=record, keyword_profiles=keyword_profiles
        )
    )
    pdf_link = html.escape(f"../sources/pdf/{Path(record['pdf']).name}", quote=True)
    md_link = html.escape(f"../sources/markdown/{Path(record['markdown']).name}", quote=True)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <meta name="description" content="{description}">
  <meta name="keywords" content="{html.escape(", ".join(page_profile["keywords"]), quote=True)}">
  <meta name="dio-odi:keyword-profile" content="{html.escape(page_profile["keyword_profile_id"], quote=True)}">
  <meta name="dio-odi:keyword-registry-version" content="{html.escape(registry_version, quote=True)}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="DIO to DIO">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <link rel="describedby" type="application/json" href="{html.escape(manifest_url, quote=True)}" title="Resolved page metadata and keyword profiles">
  <link rel="icon" type="image/svg+xml" href="../favicon.svg">
  <link rel="stylesheet" href="../assets/css/site.css">
  <script src="../assets/js/site.js" defer></script>
  <title>{title} · DIO to DIO</title>
{schema_markup}  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body class="report-page">
  <a class="skip-link" href="#report-content">Skip to report</a>
  <header class="site-header">
    <div class="shell header-inner">
      <a class="brand" href="../" aria-label="DIO to DIO home">
        <img src="../assets/brand/logo-dio-odi.svg" alt="DIO/ODI" width="148" height="40">
        <span class="brand-divider" aria-hidden="true"></span>
        <span class="brand-project">DIO to DIO</span>
      </a>
      {report_header_navigation()}
    </div>
  </header>
  {toc_markup}
  <main id="report-content">
    <section class="report-intro shell">
      <p class="eyebrow">Author-led research report · {index:02d} / {total:02d}</p>
      <h1>{model}</h1>
      <p class="report-title-meta">{title}</p>
      <div class="report-source-links"><a href="{md_link}">Markdown</a><a href="{pdf_link}">PDF</a><a href="../{html.escape(record["html"], quote=True)}">HTML</a></div>
    </section>
    <section class="report-description shell" aria-labelledby="description-heading">
      <div class="report-description-main">
        <p class="eyebrow">Catalogue record</p>
        <h2 id="description-heading">Report description</h2>
        <p>{description}</p>
      </div>
      <dl class="report-facts">
        <div><dt>Producing system</dt><dd>{model}</dd></div>
        <div><dt>Observation snapshot</dt><dd>{snapshot}</dd></div>
        <div><dt>Prompt arrangement</dt><dd>{prompt}</dd></div>
        <div><dt>Graph approach in this report</dt><dd>{graph}</dd></div>
      </dl>
    </section>
    <section class="report-rendered shell">
      <div class="report-rendered-heading">
        <p class="eyebrow">Original report</p>
        <p>The report below is rendered from the unchanged Markdown source. The original PDF and Markdown files are available above.</p>
      </div>
      <article class="report-body">{html_fragment}</article>
    </section>
  </main>
  <footer class="site-footer"><div class="shell footer-inner"><a href="https://danielberanek.cz/" class="footer-author">Daniel Beránek</a><span>DIO to DIO · {index:02d} / {total:02d}</span><a href="../">Back to all analyses</a></div></footer>
</body>
</html>
'''

def main() -> None:
    metadata = json.loads((ROOT / "metadata" / "analyses.json").read_text(encoding="utf-8"))
    records = metadata.get("analyses", [])
    structured_data = json.loads((ROOT / "metadata" / "structured-data.json").read_text(encoding="utf-8"))
    validate_structured_data(structured_data)
    if not records:
        fail("The report catalogue must contain at least one analysis.")
    record_ids = [record.get("id") for record in records]
    if any(not record_id for record_id in record_ids) or len(record_ids) != len(set(record_ids)):
        fail("Every report must have a non-empty, unique catalogue id.")

    source_md_dir = ROOT / "reports" / "markdown"
    source_pdf_dir = ROOT / "reports" / "pdf"
    expected_md, expected_pdf, integrity_records = set(), set(), []
    for record in records:
        md_rel, pdf_rel = safe_relative(record["markdown"]), safe_relative(record["pdf"])
        md_path, pdf_path = ROOT / md_rel, ROOT / pdf_rel
        if not md_path.is_file():
            fail(f"Missing Markdown source: {md_rel}")
        if not pdf_path.is_file():
            fail(f"Missing PDF source: {pdf_rel}")
        if md_path.stem != pdf_path.stem:
            fail(f"Markdown/PDF filename stems do not match: {md_rel} / {pdf_rel}")
        expected_md.add(md_path.name)
        expected_pdf.add(pdf_path.name)
        integrity_records.append({
            "id": record["id"], "markdown": record["markdown"],
            "markdown_sha256": sha256(md_path), "pdf": record["pdf"],
            "pdf_sha256": sha256(pdf_path)
        })

    actual_md = {p.name for p in source_md_dir.glob("*.md") if p.name != "README.md"}
    actual_pdf = {p.name for p in source_pdf_dir.glob("*.pdf")}
    if actual_md != expected_md:
        fail(f"Markdown inventory differs from catalogue. Unlisted: {sorted(actual_md - expected_md)}; missing: {sorted(expected_md - actual_md)}")
    if actual_pdf != expected_pdf:
        fail(f"PDF inventory differs from catalogue. Unlisted: {sorted(actual_pdf - expected_pdf)}; missing: {sorted(expected_pdf - actual_pdf)}")
    if not shutil.which("pandoc"):
        fail("Pandoc is required. Install Pandoc before running the build.")
    filter_path = ROOT / "scripts" / "filters" / "preserve-title.lua"
    if not filter_path.is_file():
        fail("Missing title-preservation Lua filter.")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(ROOT / "assets", OUT / "assets")
    shutil.copy2(ROOT / "favicon.svg", OUT / "favicon.svg")
    shutil.copytree(source_md_dir, OUT / "sources" / "markdown", ignore=shutil.ignore_patterns("README.md"))
    shutil.copytree(source_pdf_dir, OUT / "sources" / "pdf")
    (OUT / "analyses").mkdir(parents=True)

    site_url = metadata.get("project", {}).get("site_url", "https://dan-beranek.github.io/dio-to-dio/")
    keyword_profiles, surface_manifest, registry_text, registry_snapshot_filename, registry_info = (
        load_page_surface_profiles(site_url, records)
    )
    manifest_url = urljoin(site_url, MANIFEST_FILENAME)
    for index, record in enumerate(records, start=1):
        source = ROOT / safe_relative(record["markdown"])
        fragment = render_markdown(source, filter_path)
        output_rel = safe_relative(record["html"])
        if output_rel.suffix.lower() != ".html":
            fail(f"Rendered page path must end in .html: {output_rel}")
        output_path = OUT / output_rel
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            report_page(
                record, index, len(records), fragment, site_url, structured_data,
                integrity_records, records, keyword_profiles,
                registry_info["registry_version"], manifest_url
            ),
            encoding="utf-8"
        )

    index_html = (ROOT / "index.html").read_text(encoding="utf-8")
    if CATALOGUE_START not in index_html or CATALOGUE_END not in index_html:
        fail("index.html must contain analysis catalogue markers.")
    cards = "\n".join(card(record, index, len(records)) for index, record in enumerate(records, start=1))
    replacement = f"{CATALOGUE_START}\n<div class=\"analysis-grid\">\n{cards}\n</div>\n{CATALOGUE_END}"
    index_html = re.sub(re.escape(CATALOGUE_START) + r".*?" + re.escape(CATALOGUE_END), lambda _: replacement, index_html, flags=re.S)
    home_profile = keyword_profiles.get("dio-to-dio-home")
    if home_profile is None:
        fail("Missing DIO to DIO homepage surface profile.")
    index_html = upsert_head_metadata(
        index_html, home_profile["keywords"], home_profile["keyword_profile_id"],
        registry_info["registry_version"], manifest_url
    )
    home_schema = jsonld_script(
        build_jsonld(
            structured_data, site_url, records, integrity_records,
            keyword_profiles=keyword_profiles
        )
    )
    if "</head>" not in index_html:
        fail("index.html is missing its closing head element.")
    index_html = index_html.replace("</head>", home_schema + "</head>", 1)
    (OUT / "index.html").write_text(index_html, encoding="utf-8")

    # Keep the shared navigation present and complete on the landing page and every report.
    published_pages = [OUT / "index.html", *sorted((OUT / "analyses").glob("*.html"))]
    css_text = (OUT / "assets" / "css" / "site.css").read_text(encoding="utf-8")
    if "position: sticky;" not in css_text or "top: 0;" not in css_text:
        fail("The shared site header must be sticky at the top of the viewport.")
    for page_path in published_pages:
        page_html = page_path.read_text(encoding="utf-8")
        if 'class="primary-nav"' not in page_html or 'class="mobile-menu"' not in page_html:
            fail(f"Missing desktop or mobile navigation in {page_path.relative_to(OUT)}")
        if 'class="resource-trigger"' not in page_html or 'aria-haspopup="true"' not in page_html:
            fail(f"Missing accessible desktop external-resources trigger in {page_path.relative_to(OUT)}")
        if "assets/js/site.js" not in page_html:
            fail(f"Missing navigation behaviour script in {page_path.relative_to(OUT)}")
        for resource_url, *_ in EXTERNAL_RESOURCES:
            escaped_url = html.escape(resource_url, quote=True)
            if escaped_url not in page_html:
                fail(f"Missing external resource in {page_path.relative_to(OUT)}: {resource_url}")
        project_repository = "https://github.com/dan-beranek/dio-to-dio"
        if page_path == OUT / "index.html":
            if project_repository not in page_html or "Website repository (GitHub)" not in page_html:
                fail("The landing page must link to the repository that publishes this website.")
        else:
            repository_link = f'<a href="{project_repository}" target="_blank" rel="noopener noreferrer">Website repository (GitHub)</a>'
            if repository_link not in page_html:
                fail(f"Missing website repository link in {page_path.relative_to(OUT)}")


    (OUT / "source-integrity.json").write_text(json.dumps({
        "algorithm": "SHA-256",
        "note": "Hashes are calculated from the original repository files before the website build.",
        "sources": integrity_records
    }, indent=2) + "\n", encoding="utf-8")

    # Preserve the exact registry bytes used for this build; the manifest points to
    # that immutable build input and records its SHA-256 digest.
    (OUT / MANIFEST_FILENAME).write_text(
        json.dumps(surface_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    (OUT / REGISTRY_SNAPSHOT_FILENAME).write_text(registry_text, encoding="utf-8")

    dataset_keywords = structured_data["dataset"]["keywords"]
    for artifact in surface_manifest["artifacts"]:
        page_path = OUT / safe_relative(artifact["paths"][0])
        if not page_path.is_file():
            fail(f"Expected generated page is missing: {artifact['paths'][0]}")
        validate_published_page_metadata(
            page_path.read_text(encoding="utf-8"),
            artifact["page_key"],
            artifact,
            registry_info["registry_version"],
            manifest_url,
            dataset_keywords,
        )

    dcat_jsonld, dcat_turtle = build_dcat_exports(structured_data, site_url, records, integrity_records)
    (OUT / "dataset.jsonld").write_text(dcat_jsonld, encoding="utf-8")
    (OUT / "dataset.ttl").write_text(dcat_turtle, encoding="utf-8")

    sitemap_urls = [site_url] + [urljoin(site_url, r["html"]) for r in records]
    sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
    sitemap += "\n".join(f"  <url><loc>{html.escape(url)}</loc></url>" for url in sitemap_urls)
    sitemap += "\n</urlset>\n"
    (OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {urljoin(site_url, 'sitemap.xml')}\n", encoding="utf-8")

    llms_lines = [
        "# DIO to DIO", "",
        "A reflexive research portfolio examining how large language models reconstruct Digital Identity Optimization (DIO) and the Ontology of Digital Identity (ODI) when the framework is applied to its own distributed ecosystem.", "",
        "The portfolio presents eleven author-led research reports using large language models. All eleven share one author-designed research and prompt framework. Ten models received the prompt in three sequential phases, with a model-specific clarification in phase two; the local label for this component varies by report. Leo AI received one integrated prompt consolidating the substantive content of all three phases. These differences concern prompt delivery, not the research design. The reports retain distinct analytical approaches and are not ranked, harmonized, or synthesized. Each is available as unchanged Markdown and PDF sources plus a faithful HTML representation.", "",
        "## Project", f"- Home: {site_url}", "- Repository: https://github.com/dan-beranek/dio-to-dio", "",
        "## Machine-readable dataset metadata",
        f"- DCAT JSON-LD: {urljoin(site_url, 'dataset.jsonld')}",
        f"- DCAT Turtle: {urljoin(site_url, 'dataset.ttl')}",
        f"- Source integrity manifest: {urljoin(site_url, 'source-integrity.json')}",
        f"- Resolved page metadata manifest: {manifest_url}",
        f"- Canonical keyword registry snapshot used by this build: {urljoin(site_url, REGISTRY_SNAPSHOT_FILENAME)}", "",
        "## Reports"
    ]
    for record in records:
        llms_lines.extend([
            f"### {record['model']}: {record['title']}",
            f"- Markdown: {urljoin(site_url, 'sources/markdown/' + Path(record['markdown']).name)}",
            f"- PDF: {urljoin(site_url, 'sources/pdf/' + Path(record['pdf']).name)}",
            f"- HTML: {urljoin(site_url, record['html'])}",
            f"- Description: {record['description']}", ""
        ])
    (OUT / "llms.txt").write_text("\n".join(llms_lines), encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {len(records)} report pages and copied {len(expected_md)} Markdown / {len(expected_pdf)} PDF source pairs into {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
