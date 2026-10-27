---
name: meeting-record
description: "Cómo se lleva a la ficha lo que dice una sesión de un órgano: el orden del día, los acuerdos con su responsable y su fecha, los compromisos con su historia y las decisiones pendientes, cada dato con su cita. Úsalo al procesar una convocatoria, unas notas, una transcripción o un acta firmada. Meeting record, board minutes, agreements, commitments."
---

# La ficha de una sesión

Una ficha por sesión de un órgano, en `<estado>/reuniones/<órgano>-<AAAA-MM-DD>.json`. El órgano es el nombre de su carpeta en `organos/`; la fecha, la de la carpeta de la sesión. **Lo que el documento no dice se deja vacío**: un responsable o una fecha que nadie escribió no se completa por contexto. El motor valida la ficha y dice qué le falta (`record_issues`).

## Los campos

```json
{
  "organ": "junta",
  "date": "2026-09-24",
  "source": "organos/junta/2026-09-24/40-acta/acta.pdf",
  "agenda": [{"item": "Aprobación de los estados financieros", "source": "…/10-convocatoria/orden-del-dia.md, punto 2"}],
  "agreements": [
    {"id": "A-1", "what": "Aprobar los estados financieros de agosto", "who": "Vicepresidencia financiera",
     "due": "2026-10-15", "source": "…/40-acta/acta.pdf, punto 2"}
  ],
  "commitments": [
    {"id": "C-1", "who": "Gerencia de riesgos", "what": "Presentar el informe de cartera",
     "due_date": "2026-10-20", "original_due_date": "2026-10-06",
     "reschedules": [{"due_date": "2026-10-13", "source": "…/2026-10-01/40-acta/acta.pdf, punto 4"},
                     {"due_date": "2026-10-20", "source": "…/2026-10-08/40-acta/acta.pdf, punto 3"}],
     "state": "open", "evidence": null, "source": "…/40-acta/acta.pdf, punto 5"}
  ],
  "decisions": [ "…con decision-brief…" ]
}
```

## Acuerdos y compromisos

- **Cada cita va relativa a la carpeta de la oficina** —`organos/junta/2026-09-24/40-acta/acta.md`, sin la carpeta de la oficina delante— y **señala un renglón**: `<archivo>, línea N`, o `<archivo>, punto N` si el documento numera la lista. Puedes agregar el texto citado entre « » después, pero no la reemplaza: «Compromisos, primer punto» no dice qué renglón es.
- **Un acuerdo** es lo que el órgano resolvió. Lleva `who` y `due` si el acta los dice; si no, quedan vacíos y el motor levanta `agreement_without_owner` o `agreement_without_date`. **No los completes.**
- **Un compromiso** es lo que alguien prometió entregar. **Es del acta donde nació**: si una sesión posterior lo mueve, no se crea otro; se agrega la nueva fecha a `reschedules` del original, con la cita del acta que lo movió, y `due_date` pasa a ser la vigente. Aplica **commitment-tracking**.
- **Cumplido** (`state: met`) solo con un documento que lo sostenga, citado en `evidence`. Que alguien diga en la sesión que ya lo hizo no lo cumple. **Antes de dejar abierto un compromiso cuya fecha ya pasó, busca su evidencia** en el material de las sesiones del mismo órgano (`20-material/`) y en la carpeta de la sesión donde nació: un documento que diga que se entregó, y cuándo, lo cumple; cítalo en `evidence`. Si no hay ninguno, queda abierto y el motor lo dice.
- **Los compromisos de proyecto son de Samuel.** Si el acta menciona uno, no lo copies: el motor los cita de su ficha.

## El acta, solo la firmada

Los acuerdos y compromisos de la ficha salen del acta firmada de `40-acta/`. De las notas o la transcripción sale el borrador (**minutes-draft**), no la ficha. Si solo hay notas, la ficha lleva el orden del día y las decisiones, y los acuerdos esperan el acta.
