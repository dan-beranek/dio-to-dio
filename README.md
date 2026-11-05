# DIO to DIO

**A reflexive research project on the reconstruction of Digital Identity Optimization (DIO) and the Ontology of Digital Identity (ODI) by large language models.**

This repository is the source of truth for the project. Original model-generated reports are stored as Markdown and PDF files. The website is a separate presentation layer built around those source documents.

## Repository structure

```text
.
├── README.md
├── UPLOAD-GUIDE.md
├── index.html
├── .nojekyll
├── assets/
│   ├── brand/                 # Canonical DIO/ODI SVG assets, copied unchanged
│   └── css/                   # Website styles
├── metadata/
│   ├── README.md
│   └── analyses.json          # Factual catalogue; populated after source review
└── reports/
    ├── markdown/              # Original LLM reports (.md), unchanged
    └── pdf/                   # Corresponding original PDFs, unchanged
```

## Adding the nine analyses

For each analysis, place the original Markdown file in `reports/markdown/` and its corresponding original PDF in `reports/pdf/`. Use the same lowercase filename stem for both files. For example:

```text
reports/markdown/chatgpt.md
reports/pdf/chatgpt.pdf
```

The stem should identify the producing system or report unambiguously. Do not add front matter, rewrite titles, edit appendices, normalize terminology, or otherwise modify the source Markdown or PDF. Keep the prompt appendices inside the reports where they originally appear.

See [UPLOAD-GUIDE.md](UPLOAD-GUIDE.md) for the upload procedure.

## Publication principles

- Each report remains an independent analytical output of its producing LLM.
- The HTML report page is a faithful rendering of its original Markdown, not an edited or summarized edition.
- The original PDF is made available unchanged.
- Report-specific descriptions and catalogue metadata are written only after the source files have been reviewed. They identify each report; they do not impose a shared interpretation or taxonomy.
- The project website may explain the common research purpose and publication method, but it does not synthesize or harmonize the nine interpretations.
- Any future meta-analysis would be a separately designed and separately published research output.

## Research question

How do large language models reconstruct and examine Digital Identity Optimization (DIO) when the framework is applied to itself, and what do their independently developed interpretations and graph-theoretical analyses reveal about the DIO/ODI ecosystem?

The reports may differ in their analytical framing, choice of concepts, graph boundaries, methods, and conclusions. Such differences are preserved rather than flattened into a common result.

## Website

`index.html` is an initial project landing page. Individual report pages and the final catalogue will be generated after the original Markdown and PDF files have been added and reviewed. The source reports remain authoritative.

## Visual identity

The brand assets in `assets/brand/` are copies of the canonical DIO/ODI SVG assets from the author's [DIO/ODI concept repository](https://github.com/dan-beranek/dio-odi-autorsky-koncept). They are not redrawn or approximated. See `assets/brand/README.md` for usage notes.
