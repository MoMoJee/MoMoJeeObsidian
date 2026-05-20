---
name: homework-note-packaging
description: Use when:packaging Obsidian homework notes by finding linked Excalidraw handwritten notes, exporting them to PNG, generating a watermarked XeLaTeX document, and compiling a PDF for examples, exercises, or chapter homework.
---

# Homework Note Packaging

Package selected Obsidian notes into a watermarked PDF.

## Fixed Paths

- Vault root: `D:\PROJECTS\MoMoJeeObsidian\MoMoJeeOsidian`
- Excalidraw folder: `D:\PROJECTS\MoMoJeeObsidian\MoMoJeeOsidian\Excalidraw`
- Exporter script: `D:\PROJECTS\ExcalidrawExporter\export.js`
- Default watermark: `叶哲昊　24012561`
- Compiler: XeLaTeX

## Required Inputs

Confirm these before starting if missing:

- Note directory containing the selected Markdown files.
- File list, such as `例 3.1.3`, `习题 3.1.2`, or `本章习题 3.1`.
- Output directory.
- PDF file name.
- Optional watermark text and chapter title.

## Workflow

1. Read only the explicitly selected Markdown notes.
2. Extract embedded Excalidraw links such as `![[Drawing ...excalidraw]]`.
3. Build a mapping: Markdown note -> Excalidraw file -> PNG output path.
4. Export with `node D:\PROJECTS\ExcalidrawExporter\export.js` using paired input syntax `source.excalidraw.md=output.png` and `-v` set to the vault root.
5. If more than 10 drawings are involved, split export into batches.
6. Generate a XeLaTeX file in the output directory with foreground watermark using `\AddToShipoutPictureFG`.
7. Compile with XeLaTeX. If the target PDF is locked, use a new job name.
8. Report exported PNG files, PDF path, page count if available, and failures.

## Constraints

- Do not scan the whole vault; process only the user-selected notes.
- Do not modify source Markdown notes or Excalidraw files.
- Keep generated PNG, `.tex`, auxiliary files, and PDF inside the selected output directory.
- Use UTF-8-safe file creation/editing for `.tex` content.
