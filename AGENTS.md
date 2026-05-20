# MoMoJeeObsidian Codex Rules

This repository is an Obsidian vault. Treat it as the user's long-term learning workspace, not as a normal source-code repo.

## Default Behavior

- Reply in Chinese unless the user explicitly asks for another language.
- Prefer calm, detailed, concrete explanations for physics, optics, electronics, mathematics, and experiment work.
- Preserve the user's note style: plain language, enough derivation detail, Obsidian wikilinks, Markdown math, and careful image references.
- Search with `rg` first. Constrain searches to the subject folder or files named by the user whenever possible.
- Never print secrets, tokens, API keys, cookies, or private identifiers unless the user explicitly asks to inspect a local secret value.

## File Safety

- Do not delete, empty, rename, or move files without explicit permission.
- Do not edit `.github`, `.obsidian`, `.trash`, `copilot`, image assets, or `*.excalidraw.md` files unless the user explicitly asks for that exact file type.
- Standard Markdown notes are the main editable surface.
- Files under `Scripts/` may be read and edited only when the user asks for script work.
- For experiment-report or experiment-preview tasks, all generated files must stay inside the user-provided work directory.

## Skill Routing

- Use `$obsidian-learning` for vault Q&A, preview notes, note cleanup, wikilinks, and learning explanations.
- Use `$academic-writing` for STEM academic prose, abstracts, paper sections, and literature-style writing.
- Use `$latex-writing` for LaTeX authoring, Chinese XeLaTeX documents, formulas, tables, figures, and compile fixes.
- Use `$excalidraw-export` when exporting `.excalidraw.md` drawings to PNG or SVG.
- Use `$homework-note-packaging` for exporting linked Excalidraw homework notes and packaging them into watermarked PDFs.
- Use `$lab-preview` for experiment preview documents, operation guides, and blank data-record PDFs.
- Use `$lab-report-writing` for full Chinese lab reports in LaTeX.

## Subagent Routing

When the user asks for a specialized workflow, prefer the matching Codex subagent:

- `obsidian_learning_assistant`: learning Q&A, preview notes, vault organization.
- `academic_writer`: STEM academic writing and polishing.
- `homework_note_packager`: Excalidraw homework export and PDF packaging.
- `lab_preview_assistant`: experiment preview package generation.
- `lab_report_writer`: complete experiment report generation.

Use subagents for large reading/writing jobs or parallel extraction, but keep final integration and file-safety judgment in the main thread.
