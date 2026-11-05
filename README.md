# DIO to DIO

**A reflexive research portfolio on the reconstruction of Digital Identity Optimization (DIO) and the Ontology of Digital Identity (ODI) by large language models.**

The public portfolio brings together nine independent model-generated research reports. DIO/ODI is both the subject of inquiry and the conceptual perspective through which each model examines the distributed ecosystem.

## Research design

The common research assignment establishes the object of inquiry and broad analytical directions: DIO/ODI-native exploration and graph-theoretical examination. It does not prescribe a single interpretation, graph schema, node/edge taxonomy, observation boundary, metric set, or conclusion.

Each report retains its own analytical framing, methodological choices, evidence boundary, graph model, appendices, and conclusions. Eight reports document staged prompt components in their appendices; Leo AI documents one author-designed integrated prompt. The reports are not ranked or harmonized.

The project-level research question is:

> How do large language models reconstruct and examine Digital Identity Optimization (DIO) when the framework is applied to itself, and what do their independently developed interpretations and graph-theoretical analyses reveal about the DIO/ODI ecosystem?

## Publication principles

- The original Markdown files in `reports/markdown/` are the authoritative text sources.
- Individual HTML report pages are generated from those Markdown files using Pandoc. The conversion is a presentation transformation; it does not rewrite, shorten, or editorially normalize report prose.
- Original PDFs in `reports/pdf/` are copied to the published site unchanged.
- Factual descriptions and report metadata are maintained separately in `metadata/analyses.json`.
- The portfolio provides a common publishing format, not a common interpretation.
- Any future meta-analysis would have its own research question, method, and standalone publication.

## Repository structure

```text
.
├── .github/workflows/pages.yml
├── assets/
│   ├── brand/                 # Canonical DIO/ODI SVG files
│   └── css/site.css
├── metadata/
│   └── analyses.json          # Factual catalogue metadata
├── reports/
│   ├── markdown/              # Nine original LLM reports
│   └── pdf/                   # Nine original PDFs
├── scripts/
│   ├── build.py               # Static site generator
│   └── filters/preserve-title.lua
├── index.html                 # Project landing-page template
└── README.md
```

The generated `site/` directory contains the deployable static website, individual HTML pages, and unchanged source downloads. It is a build output and is not maintained by hand.

## Build locally

Requirements: Python 3 and [Pandoc](https://pandoc.org/).

From the repository root:

```bash
python3 scripts/build.py
```

The build verifies the nine Markdown/PDF pairs and their exact filename matching, checks that the catalogue and source inventory agree, copies source files without modifying them, calculates SHA-256 hashes for the published source-integrity manifest, and generates the static pages, sitemap, robots.txt, and `llms.txt`.

## GitHub Pages

The workflow in `.github/workflows/pages.yml` builds and deploys the site after relevant changes are pushed to `main`. In repository settings, configure **Settings → Pages → Build and deployment → Source → GitHub Actions**.

Expected project URL: <https://dan-beranek.github.io/dio-to-dio/>.

## Visual identity

The logo assets in `assets/brand/` are exact copies of the canonical DIO/ODI SVG files from the author's [DIO/ODI concept repository](https://github.com/dan-beranek/dio-odi-autorsky-koncept). They are not redrawn or approximated.
