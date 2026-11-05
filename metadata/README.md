# Catalogue metadata

`analyses.json` provides the factual identification layer used by the landing-page catalogue, report-page descriptions, and machine-readable project index.

The catalogue has nine records. Each record identifies its own report and points to its exact Markdown and PDF source files. Descriptions and graph-method notes were written after inspection of the corresponding report.

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
