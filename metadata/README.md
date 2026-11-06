# Catalogue metadata

`analyses.json` provides the factual identification layer used by the landing-page catalogue, report-page descriptions, and machine-readable project index.

The catalogue contains one record per report. Each record identifies its own report and points to its exact Markdown and PDF source files. Descriptions and graph-method notes were written after inspection of the corresponding report.

## Field meanings

- `id`: stable internal slug.
- `model`: producing system label as stated in the report; no unverified model-version claim is added.
- `title`: report's own title, taken from the document metadata or title block.
- `observation_snapshot`: the observation date or interval stated by the report. This is not automatically treated as the document publication date.
- `description`: a short report-specific account of its actual focus.
- `graph_approach`: the graph representation, units, relation types, and/or observation boundary as described by that report. These descriptions are intentionally not normalized to a common schema.
- `prompt_arrangement`: a factual description of the prompt arrangement documented in the report appendix. It does not infer the number of separate user turns.
- `markdown`, `pdf`: paths to the unchanged source documents.
- `html`: output path of the generated HTML representation.

## Editorial boundary

Catalogue metadata is not part of the source report. It may identify and describe the report, but it must not replace the report's analysis, add editorial findings, or imply a shared conclusion across models.

The project-level research question describes the common object of inquiry. It does not serve as a mandatory report-level question and does not override any model-specific framing.

No ranking, scoring, shared finding taxonomy, or automatic meta-analysis is generated from these records.

## Shared structured data

`structured-data.json` is the single source of truth for the website-level identity graph used by the static-site builder.

- The canonical person identifier is `https://danielberanek.cz/#person`.
- The person's ORCID is linked through `sameAs`: `https://orcid.org/0009-0004-0050-0264`.
- The portfolio is represented as a `ResearchProject`, with the person identified as its founder. The person is also identified as publisher of the website and report pages.
- The website and each report page reuse the same Person, WebSite, and ResearchProject identifiers.
- Author-led reports produced using LLMs are represented as `CreativeWork` records. The person is identified as founder and publisher/curator of the portfolio; report-level authorship statements and the documented role of each model remain in the original report.
- Observation snapshots are not converted into publication dates.

Update this file when the canonical author identity, ORCID, project identity, or website-level description changes. Generated JSON-LD is emitted by `scripts/build.py`; do not maintain separate hand-written graphs in the HTML templates.

## Dataset and distribution metadata

`structured-data.json` is the shared source of truth for the canonical Person, website, project, and Dataset identity.

- The Dataset is a curated collection of author-led research reports produced using LLMs. Project-level creator/curator metadata does not replace the report-specific authorship and AI-use statements preserved in each source.
- Dataset subjects use the exact canonical SKOS concept URIs for DIO and ODI from the DIO/ODI Reference Vocabulary. No local or duplicate concept identifiers are minted.
- The build emits Schema.org `Dataset` and `DataDownload` nodes on the landing page and report pages.
- The build also emits a DCAT 3 catalogue in `dataset.jsonld` and `dataset.ttl`. Each report has Markdown, PDF, and HTML distributions with explicit media types and stable access URLs.
- SHA-256 checksums are attached to the original Markdown and PDF distributions and are also listed in `source-integrity.json`. HTML is a generated representation and is not assigned a checksum in the Dataset metadata.
- Observation snapshots remain distinct from publication dates. No publication date or licence is inferred where it has not been established.

The DCAT files are generated outputs. Do not edit them by hand; update the metadata and build logic instead.
