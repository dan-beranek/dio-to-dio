# Upload guide — source reports

This repository is prepared to receive all nine original Markdown reports and their nine matching PDF files. You do **not** need to upload the reports into ChatGPT one by one. Put the files directly into this GitHub repository; once they are there, the repository can be used as the source for the next analysis and publication steps.

## 1. Create the repository

Create an empty public GitHub repository named:

```text
dan-beranek/dio-to-dio
```

Do not initialize it with an additional README, licence, or `.gitignore`, because this starter package already contains the initial files.

## 2. Add the starter structure

Download and extract `dio-to-dio-starter.zip`. The folder inside the archive is `dio-to-dio-starter/`.

The recommended method is GitHub Desktop:

1. Clone the empty `dan-beranek/dio-to-dio` repository to your computer.
2. Copy the **contents** of the extracted `dio-to-dio-starter/` folder into the cloned repository folder. Do not replace or delete the hidden `.git` directory created by GitHub Desktop.
3. Commit the files and push the commit to GitHub.

The same can be done with Git on the command line after cloning the empty repository:

```bash
git clone https://github.com/dan-beranek/dio-to-dio.git
# Copy the contents of dio-to-dio-starter/ into the cloned dio-to-dio/ folder.
cd dio-to-dio
git add .
git commit -m "Add DIO to DIO project scaffold"
git push origin main
```

If GitHub creates a default branch with a name other than `main`, use that branch name in the final command.

## 3. Add the source files

Put the nine original `.md` files here:

```text
reports/markdown/
```

Put the nine matching original `.pdf` files here:

```text
reports/pdf/
```

Use the same filename stem for each pair. Example:

| Original Markdown | Matching PDF |
|---|---|
| `reports/markdown/chatgpt.md` | `reports/pdf/chatgpt.pdf` |
| `reports/markdown/deepseek.md` | `reports/pdf/deepseek.pdf` |
| `reports/markdown/leo-ai.md` | `reports/pdf/leo-ai.pdf` |

These are examples of filename conventions, not a prescribed list of the nine systems. Use names that accurately identify the actual source system/report.

### Source-file rules

- Upload the original files, not rewritten or re-exported substitutes.
- Do not add YAML front matter or metadata to the source Markdown.
- Do not remove or split prompt appendices, references, tables, diagrams, or other report sections.
- Do not edit a report to make its structure match another report.
- Keep the PDF exactly as originally produced.
- If an original file has a meaningful version marker in its filename, preserve that information consistently in the matching pair.

## 4. Push the reports

After copying all 18 source files into the two directories, commit and push them together. This avoids any need to submit the documents to ChatGPT as separate daily inputs.

## 5. Tell ChatGPT the repository is ready

Send the repository URL:

```text
https://github.com/dan-beranek/dio-to-dio
```

The next step will be to inspect all nine Markdown/PDF pairs from GitHub, verify their pairing and source integrity, and prepare factual report-specific catalogue descriptions. The HTML pages will then be generated from the Markdown sources without editorial changes.

## Folder map

```text
reports/
├── markdown/
│   ├── <report-slug-01>.md
│   ├── <report-slug-02>.md
│   └── ...
└── pdf/
    ├── <report-slug-01>.pdf
    ├── <report-slug-02>.pdf
    └── ...
```
