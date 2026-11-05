# Catalogue metadata

`analyses.json` is reserved for factual catalogue records used to build the index and individual report pages.

It is intentionally empty at scaffold stage. Records will be added only after the original source reports have been read. Descriptions will be specific to each report and will not force all analyses into the same research question, method, graph model, finding categories, or conclusion.

Potential factual fields include:

- stable report identifier / URL slug;
- exact title as it appears in the report;
- producing LLM/system name and model version, only where stated or verifiable;
- report language;
- observation snapshot or analysis date, distinguishing them where necessary;
- a concise factual description of what that particular report examines;
- a factual note on its prompt arrangement, based on the appendix or other source evidence;
- exact relative paths to the unchanged Markdown and PDF source files.

No field should be populated by guessing. Report-specific method descriptions remain free-form; the catalogue must not impose a common graph schema or analytical taxonomy.
