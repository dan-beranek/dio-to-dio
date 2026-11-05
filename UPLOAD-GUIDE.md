# Repository guide — source reports and publishing

This repository already contains the nine original Markdown reports and their nine matching PDFs. It is the source of truth for the public DIO to DIO research portfolio.

## Source locations

- Original Markdown: `reports/markdown/`
- Original PDF: `reports/pdf/`
- Factual report metadata: `metadata/analyses.json`
- Canonical author, website, and project identity for JSON-LD: `metadata/structured-data.json`
- Project landing-page template: `index.html`
- Build script: `scripts/build.py`

For every report, keep the Markdown and PDF basenames matched exactly.

## Source-file rules

- Preserve original Markdown and PDF files byte-for-byte unless a new source version is intentionally supplied.
- Do not add YAML front matter to the Markdown.
- Do not remove or split prompt appendices, references, tables, diagrams, or other report sections.
- Do not edit a report to make its structure match another report.
- Do not treat the catalogue description as a replacement for the report.
- Record a new or revised source pair and update its factual metadata deliberately; keep the original publication state recoverable through Git history.

## Build and validation

Requirements: Python 3 and Pandoc.

From the repository root, run:

```bash
python3 scripts/build.py
```

The build stops if:
- the catalogue does not contain exactly nine reports;
- a listed Markdown or PDF source is missing;
- a Markdown/PDF filename pair does not match;
- the files in the source folders do not match the catalogue inventory;
- Pandoc or the source-preservation filter is unavailable.

Before rendering, the build validates the canonical Person identifier and ORCID `sameAs` link in `metadata/structured-data.json`. It emits a consistent Schema.org graph on the landing page and each report page; do not hand-edit JSON-LD in generated HTML.

The build then:
- renders the Markdown source to HTML using Pandoc;
- keeps the report body separate from factual catalogue metadata;
- copies the original Markdown and PDF sources into the deployable output unchanged;
- records SHA-256 digests for all 18 source documents;
- generates the landing-page cards, individual report pages, sitemap, robots.txt, and llms.txt.

LaTeX used only for the original title-page typography is represented with equivalent HTML typography. A print-only page-break command does not create an empty web page. Unrecognized raw TeX is retained visibly rather than silently discarded.

## GitHub Pages

The GitHub Actions workflow builds the static output after relevant changes are pushed to `main`. Set the Pages deployment source to **GitHub Actions** in repository settings if this has not already been done.

Expected URL:

<https://dan-beranek.github.io/dio-to-dio/>
