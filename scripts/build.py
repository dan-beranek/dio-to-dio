#!/usr/bin/env python3
"""Build the DIO to DIO static portfolio from unchanged Markdown/PDF sources."""
from __future__ import annotations
import hashlib, html, json, re, shutil, subprocess, sys
from pathlib import Path
from urllib.parse import urljoin

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

def render_markdown(source: Path, filter_path: Path) -> str:
    command = [
        "pandoc", f"--from={PANDOC_FROM}", "--to=html5", "--wrap=none",
        "--mathjax", f"--lua-filter={filter_path}", str(source)
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, encoding="utf-8", capture_output=True)
    if result.returncode != 0:
        fail(f"Pandoc failed for {source.relative_to(ROOT)}:\n{result.stderr}")
    if not result.stdout.strip():
        fail(f"Pandoc produced empty HTML for {source.relative_to(ROOT)}")
    return result.stdout


def validate_structured_data(config: dict) -> None:
    person = config.get("person", {})
    project = config.get("project", {})
    website = config.get("website", {})
    required_person_fields = ("@id", "@type", "name", "url", "sameAs")
    if any(not person.get(key) for key in required_person_fields):
        fail("metadata/structured-data.json has incomplete person identity metadata.")
    if person["@type"] != "Person":
        fail("The canonical author entity must use @type Person.")
    if person["@id"] != "https://danielberanek.cz/#person":
        fail("The canonical person @id must remain https://danielberanek.cz/#person.")
    if "https://orcid.org/0009-0004-0050-0264" not in person["sameAs"]:
        fail("The canonical person sameAs list must include the ORCID URI.")
    if not project.get("name") or not project.get("description") or not project.get("sameAs"):
        fail("metadata/structured-data.json has incomplete project metadata.")
    if not website.get("name") or not website.get("description") or not website.get("inLanguage"):
        fail("metadata/structured-data.json has incomplete website metadata.")

def report_schema_nodes(record: dict, site_url: str, config: dict) -> tuple[dict, dict]:
    page_url = urljoin(site_url, record["html"])
    page_id = page_url + "#webpage"
    work_id = page_url + "#report"
    website_id = site_url + "#website"
    project_id = site_url + "#project"
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
    work = {
        "@type": "CreativeWork",
        "@id": work_id,
        "name": record["title"],
        "description": record["description"],
        "url": page_url,
        "inLanguage": config["website"]["inLanguage"],
        "isPartOf": {"@id": website_id},
        "about": {"@id": project_id},
        "publisher": person_ref,
        "mainEntityOfPage": {"@id": page_id}
    }
    return page, work

def build_jsonld(config: dict, site_url: str, records: list, current_record: dict | None = None) -> dict:
    person = dict(config["person"])
    website_id = site_url + "#website"
    project_id = site_url + "#project"
    person_ref = {"@id": person["@id"]}
    website_ref = {"@id": website_id}
    project_ref = {"@id": project_id}

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
            "maintainer": person_ref
        }
    ]

    if current_record is None:
        report_pages = []
        for record in records:
            page, work = report_schema_nodes(record, site_url, config)
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
    else:
        page, work = report_schema_nodes(current_record, site_url, config)
        graph.extend([page, work])

    payload = {"@context": "https://schema.org", "@graph": graph}
    # Validate serialization and graph identity before writing it into HTML.
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
    return parsed

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
    pdf_href = html.escape(f"sources/pdf/{Path(record['pdf']).name}", quote=True)
    return f'''<article class="analysis-card">
  <div class="analysis-card-meta"><span>{index:02d} / {total:02d}</span><span>{model}</span><time>{snapshot}</time></div>
  <h3><a href="{href}">{title}</a></h3>
  <p>{description}</p>
  <div class="analysis-card-links"><a href="{href}">Read HTML report</a><a href="{pdf_href}" download>Original PDF</a></div>
</article>'''

def report_page(record: dict, index: int, total: int, html_fragment: str, site_url: str, structured_data: dict) -> str:
    model = html.escape(record["model"])
    title = html.escape(record["title"])
    description = html.escape(record["description"])
    graph = html.escape(record["graph_approach"])
    prompt = html.escape(record["prompt_arrangement"])
    snapshot = html.escape(record["observation_snapshot"])
    page_url = urljoin(site_url, record["html"])
    canonical = html.escape(page_url, quote=True)
    schema_markup = jsonld_script(build_jsonld(structured_data, site_url, [record], current_record=record))
    pdf_link = html.escape(f"../sources/pdf/{Path(record['pdf']).name}", quote=True)
    md_link = html.escape(f"../sources/markdown/{Path(record['markdown']).name}", quote=True)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <meta name="description" content="{description}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="DIO to DIO">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/svg+xml" href="../favicon.svg">
  <link rel="stylesheet" href="../assets/css/site.css">
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
      <nav aria-label="Report navigation"><a href="../">All analyses</a><a href="https://github.com/dan-beranek/dio-to-dio">Repository</a></nav>
    </div>
  </header>
  <main id="report-content">
    <section class="report-intro shell">
      <p class="eyebrow">Independent model analysis · {index:02d} / {total:02d}</p>
      <h1>{model}</h1>
      <p class="report-title-meta">{title}</p>
      <div class="report-source-links"><a href="{pdf_link}" download>Download original PDF</a><a href="{md_link}" download>Download original Markdown</a></div>
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
    if len(records) != 9:
        fail(f"Expected 9 analyses in metadata, found {len(records)}")

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
    for index, record in enumerate(records, start=1):
        source = ROOT / safe_relative(record["markdown"])
        fragment = render_markdown(source, filter_path)
        output_rel = safe_relative(record["html"])
        if output_rel.suffix.lower() != ".html":
            fail(f"Rendered page path must end in .html: {output_rel}")
        output_path = OUT / output_rel
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report_page(record, index, len(records), fragment, site_url, structured_data), encoding="utf-8")

    index_html = (ROOT / "index.html").read_text(encoding="utf-8")
    if CATALOGUE_START not in index_html or CATALOGUE_END not in index_html:
        fail("index.html must contain analysis catalogue markers.")
    cards = "\n".join(card(record, index, len(records)) for index, record in enumerate(records, start=1))
    replacement = f"{CATALOGUE_START}\n<div class=\"analysis-grid\">\n{cards}\n</div>\n{CATALOGUE_END}"
    index_html = re.sub(re.escape(CATALOGUE_START) + r".*?" + re.escape(CATALOGUE_END), lambda _: replacement, index_html, flags=re.S)
    home_schema = jsonld_script(build_jsonld(structured_data, site_url, records))
    if "</head>" not in index_html:
        fail("index.html is missing its closing head element.")
    index_html = index_html.replace("</head>", home_schema + "</head>", 1)
    (OUT / "index.html").write_text(index_html, encoding="utf-8")

    (OUT / "source-integrity.json").write_text(json.dumps({
        "algorithm": "SHA-256",
        "note": "Hashes are calculated from the original repository files before the website build.",
        "sources": integrity_records
    }, indent=2) + "\n", encoding="utf-8")

    sitemap_urls = [site_url] + [urljoin(site_url, r["html"]) for r in records]
    sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
    sitemap += "\n".join(f"  <url><loc>{html.escape(url)}</loc></url>" for url in sitemap_urls)
    sitemap += "\n</urlset>\n"
    (OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {urljoin(site_url, 'sitemap.xml')}\n", encoding="utf-8")

    llms_lines = [
        "# DIO to DIO", "",
        "A reflexive research portfolio examining how large language models reconstruct Digital Identity Optimization (DIO) and the Ontology of Digital Identity (ODI) when the framework is applied to its own distributed ecosystem.", "",
        "The portfolio preserves nine independent reports. It does not rank, harmonize, or synthesize their interpretations. Report descriptions are factual catalogue metadata; each full report is rendered from its unchanged Markdown source, with original Markdown and PDF files available.", "",
        "## Project", f"- Home: {site_url}", "- Repository: https://github.com/dan-beranek/dio-to-dio", "", "## Independent reports"
    ]
    for record in records:
        llms_lines.extend([
            f"### {record['model']}: {record['title']}",
            f"- HTML: {urljoin(site_url, record['html'])}",
            f"- Markdown: {urljoin(site_url, 'sources/markdown/' + Path(record['markdown']).name)}",
            f"- PDF: {urljoin(site_url, 'sources/pdf/' + Path(record['pdf']).name)}",
            f"- Description: {record['description']}", ""
        ])
    (OUT / "llms.txt").write_text("\n".join(llms_lines), encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {len(records)} report pages and copied {len(expected_md)} Markdown / {len(expected_pdf)} PDF source pairs into {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
