# How the terms are accepted

A disclaimer in a repository is read by no one. Criterio ships no professional sign-off, so the warning has to reach the person who runs it and the person who later receives the document. Four layers do that. Every skill in every plugin implements all four.

## Layer 1 — Gate in the local configuration

The company's private local file carries the acceptance record:

```yaml
---
terms_accepted:
  version: "1.0"
  date: 2026-09-18
  by: "Nombre Apellido"
---
```

Skill behaviour:

1. Read `terms_accepted` from the local file.
2. **Missing, or `version` older than the current `TERMS.md`** → show the short form of the disclaimer, ask for explicit acceptance, and offer to write the block with today's date and the name the user gives.
3. Until it is recorded, the skill answers questions and explains itself, but **does not produce a full analysis or a report**.
4. Acceptance is never assumed, never inferred from the user continuing, and never written without the user saying yes.

This is the closest thing to real consent available here, and it lives on the disk of whoever runs it.

**Short form shown at the gate:**

> Criterio produces working drafts, not legal or accounting advice. No professional has certified its content. Every output must be verified by someone qualified before you act on it. The law changes and these packages may be out of date. Your documents are processed on the AI platform's infrastructure. Provided as is, with no warranty. Full terms: TERMS.md.

## Layer 2 — Footer on every generated report

Every report, spreadsheet or document the plugin produces carries, at the end:

```
Generado con Criterio <versión> · borrador de trabajo, según los documentos leídos
Fichas aplicadas: 14 proyectos · último barrido 2026-09-18
Campos sin dato en este análisis: 6 · contradicciones abiertas: 2
Verificar contra la fuente antes de decidir. Términos: <enlace al repositorio>
```

The document circulates by email and lands in a board pack. The warning travels with it or it does not exist.

The footer is written in the language of the report, not in English.

## Layer 3 — Banner at the start of the run

Before the first finding, the analysis states which records it loaded, when they were last refreshed, and that the output is a working draft. If a record is stale, or a project has no record at all, it says so here rather than at the end.

Cheap, visible, and lost in a long thread — which is why it is not the only layer.

## Layer 4 — TERMS.md and a notice in the README

The standard open-source minimum: a terms file, linked from the README, from the installation instructions and from every package scope page. Necessary, and on its own read by nobody.

## What this does not do

It does not make the output reliable, it does not transfer responsibility away from the person who runs it, and it is not a substitute for a lawyer or an accountant reading the result. It makes the limits impossible to miss. That is all it does, and it is worth doing well.
