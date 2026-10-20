# How the terms are accepted

A disclaimer in a repository is read by no one. Criterio ships no professional sign-off, so the warning has to reach the person who runs it and the person who later receives the document. Four layers do that. Every skill in every plugin implements all four.

## Layer 1 — Gate in the local configuration, one acceptance per version

**Every version of the family is accepted again**, even when the terms did not change. Installing Criterio or updating it to a new version requires a new acceptance; earlier ones are kept. The succession of dated acceptances —who, which version, which text— is the trail.

The setup command of each agent shows the short form (the "In short" / "En corto" section of the terms file that ships inside the plugin), asks for an explicit yes and the person's name, and records it with one script call, the same in the three agents:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" aceptar --config .criterio/portafolio/config.json --por "Nombre Apellido"
```

That call writes, deterministically and without the model:

1. **A receipt in Markdown and in PDF** in `.criterio/terminos/aceptacion-<plugin>-<version>-<date>.md` and `.pdf`: name, date, family version, terms version and file, the terms' SHA-256, the version-register entry, the link to the legal notice, an integrity note, and the full text accepted.
2. **A `.sha256` file** next to them, in the standard format: `shasum -a 256 -c aceptacion-….sha256` checks both without the plugin (Windows: `certutil -hashfile <file> SHA256`).
3. **An entry in `.criterio/terminos/aceptaciones.json`**, the local acceptance log. Every entry carries the SHA-256 of the previous one: an altered or removed acceptance breaks the chain.
4. **The record in the configuration:**

```json
"terms_accepted": {
  "version": "1.2",
  "date": "2026-10-15",
  "by": "Nombre Apellido",
  "family_version": "0.3.8",
  "plugin": "criterio-portfolio",
  "terms_file": "TERMS.es.md",
  "terms_sha256": "<SHA-256 of the terms file shown>",
  "register_sha256": "<SHA-256 of the version-register entry>",
  "receipt_md": ".criterio/terminos/aceptacion-criterio-portfolio-0.3.8-2026-10-15.md",
  "receipt_md_sha256": "<SHA-256 of the Markdown receipt>",
  "receipt_pdf": ".criterio/terminos/aceptacion-criterio-portfolio-0.3.8-2026-10-15.pdf",
  "receipt_pdf_sha256": "<SHA-256 of the PDF receipt>",
  "legal_notice": "https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.8"
}
```

**The gate is code, not a promise.** `config` and `corrida-inicio` —which every command calls before it starts— check that the acceptance is for the installed family version, that the terms fingerprint is that of the terms file shipped in the plugin, and that both receipts are there with the fingerprint recorded. If any of the three fails, the command stops and says why: answer questions, show the short form, ask for an explicit yes, record it with `aceptar`, start again. Acceptance is never assumed, never inferred from the user continuing, and never written without the user saying yes.

**Integrity.** A receipt keeps its integrity and may not be modified: any change, however small, produces another SHA-256 and voids it as a record. The same holds for the terms and for the version register: their fingerprints are published with each version in the legal notice of the family, at https://www.josenanez.com/es/agents/criterio-pmo/legal, which the maintainer controls.

**The version register.** `registro/versiones.json` (copied byte for byte into every plugin as `REGISTRO.json`) records each version like a patent register: date, commit, what changed, which terms govern it with their SHA-256, the fingerprint of what each agent does, and the SHA-256 of the previous entry. `scripts/registro.py verificar` is a gate: a modified entry, a broken chain, a released version with no entry, or terms changed without a new version all fail it. From 0.3.9 every entry also carries its git tag, and `registro.py liberar <version> --etiquetar` makes the release commit and creates the tag on it, so the entry and the tag point to the same commit; the gate fails if a tag points to a commit that does not contain its entry. Earlier entries record the commit where each version was born: the `v0.3.6` tag, created by hand, marks a later commit of the same version, and `v0.3.8` marks the commit that registered it.

**Short form shown at the gate** (Spanish, from `TERMS.es.md`; the English one is in `TERMS.md`):

> Criterio produce borradores de trabajo, no decisiones ni asesoría. Procesa los documentos que usted le indique y dice lo que muestran; no sabe lo que se habló fuera de ellos. Puede equivocarse, y por eso cada dato viene con la cita del documento de donde salió: la verificación es suya. Sus documentos se procesan en la infraestructura de la plataforma de IA, no solo en su equipo. Cada versión se prueba antes de publicarse; garantía y responsabilidad: licencia Apache 2.0. Cada versión se acepta de nuevo y deja un comprobante en Markdown y PDF con su huella SHA-256. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

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
