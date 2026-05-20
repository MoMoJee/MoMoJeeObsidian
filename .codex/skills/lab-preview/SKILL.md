---
name: lab-preview
description: Use when:preparing for a physics, optics, or electronics experiment by reading local materials and generating an experiment interpretation document, an operation guide, and a blank XeLaTeX data-record PDF.
---

# Lab Preview

Use this skill before a lab session.

## Required Inputs

- Experiment name.
- Work directory. All generated files must stay inside this directory.

## Workflow

1. Explore only the work directory.
2. Locate manuals, PPTs, Markdown notes, PDFs, DOCX files, images, and other reference materials.
3. If no manual is found, list the files and ask for confirmation before writing.
4. Read the manual fully, including linked images when needed.
5. Extract experiment purpose, principle, formulas, instruments, operation steps, data-record requirements, data-processing methods, safety notes, and common error sources.
6. Generate `[实验名称]_实验解读.md`.
7. Generate `[实验名称]_操作指导.md`.
8. Generate `[实验名称]_数据记录单.tex` and compile it to PDF with XeLaTeX.

## Document Requirements

The interpretation document should explain:

- 实验目的与意义
- 实验原理详解
- 实验仪器解析
- 实验装置与光路
- 数据处理方法
- 常见问题与注意事项

The operation guide should be directly actionable:

- 实验前准备
- Step-by-step operations
- Expected phenomena
- Notes at each step
- Data recording reminders
- Shutdown and cleanup

The data record sheet should:

- Leave all data cells blank.
- Use three-line tables.
- Include units in headers.
- Reserve calculation space for uncertainty or derived quantities when needed.
- Use `adjustbox`, `makecell`, or landscape pages for wide tables.

## Constraints

- Do not write outside the work directory.
- Do not start writing before reading the manual.
- Do not guess missing experiment content.
- Use relative image paths.
