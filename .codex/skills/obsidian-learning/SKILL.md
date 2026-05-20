---
name: obsidian-learning
description: Use when working in the MoMoJeeObsidian vault to answer learning questions, generate preview notes, optimize Obsidian Markdown notes, connect notes with wikilinks, or explain physics, optics, electronics, and mathematics from local notes and textbooks.
---

# Obsidian Learning

Use this skill for learning support inside the MoMoJeeObsidian vault.

## Core Rules

- Work mainly with standard `.md` notes.
- Do not edit `.obsidian`, `.trash`, `copilot`, image assets, or `*.excalidraw.md` unless explicitly requested.
- Never delete, empty, move, or rename notes without explicit permission.
- If a Markdown note refers to an image that is needed to understand the text, view the image before explaining or rewriting.
- Use Obsidian wikilinks for internal connections: `[[Note]]`, `[[Note|Alias]]`, `![[image.png]]` when appropriate.

## Note Style

- Use plain, detailed, concrete Chinese. Avoid vague or ornamental writing.
- Preserve the user's habit of using `==highlight==` for core terms and states.
- Use `$...$` for inline math and `$$...$$` for block math.
- Use `\vec{}` for physical vectors, such as `\vec{E}` and `\vec{B}`.
- Prefer numbered Chinese outlines plus Markdown headings, for example `### 三、...` and `#### 1. ...`.
- Use bold lead-ins such as `**物理意义**：` and blockquote conclusions such as `> **结论**：...`.

## Preview Note Workflow

1. Identify the subject folder specified by the user. If it is missing, ask for the subject or folder.
2. If no chapter is specified, inspect the latest existing notes in that subject, infer the next section from the textbook, and confirm before writing.
3. Read the relevant textbook or lecture content fully for the target section.
4. Search nearby existing notes for related knowledge and link them with wikilinks.
5. Write one section or one note at a time. Do not batch-write many notes unless the user explicitly asks.
6. Keep all formulas from the source material, but explain them in concrete language.
7. Include important images when they materially help understanding, using correct Obsidian paths.

## Q&A Workflow

- Base answers on user-provided excerpts, screenshots, or local notes first.
- If updating notes, summarize exactly which file changed.
- If the answer depends on an image, inspect it rather than guessing.
