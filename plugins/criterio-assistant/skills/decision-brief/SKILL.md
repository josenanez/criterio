---
name: decision-brief
description: "Cómo se arma la ficha de una decisión pendiente de un órgano: la decisión como la escribe el material, las opciones que traen los documentos con su evidencia citada, lo que falta saber y la fecha que fija el plazo, sin ordenarlas ni recomendar. Úsalo al preparar una sesión o al encontrar en el material un punto que pide una decisión. Decision brief, board pack, options."
---

# La ficha de una decisión

Va en la ficha de la sesión donde se planteó, en `decisions`:

```json
{
  "id": "D-1",
  "decision": "Proveedor del centro de datos alterno",
  "source": "organos/comite/2026-10-01/20-material/propuesta.pdf",
  "options": [
    {"option": "Renovar con el proveedor actual", "evidence": [{"archivo": "…/20-material/propuesta.pdf", "pagina": 3}]},
    {"option": "Licitar", "evidence": [{"archivo": "…/20-material/comparativo.xlsx", "fila": 4}]}
  ],
  "missing": ["La oferta económica del segundo proveedor no está en la carpeta"],
  "deadline": "2026-11-02",
  "deadline_source": "…/20-material/propuesta.pdf, página 1: «la oferta vence el 2 de noviembre»",
  "status": "pending"
}
```

## Las reglas

1. **Las opciones son las que traen los documentos**, en el orden en que aparecen. No inventes una que nadie planteó.
2. **Cada opción con su evidencia citada.** Una opción sin documento que la sostenga lleva `evidence` vacío, y se ve así en el paquete.
3. **No las ordenes ni digas cuál conviene.** Nada de `rank`, `recommended`, «la mejor», «la más conveniente»: el motor rechaza la ficha que lo trae. Hay cuatro razones (ADR 0012): Ofelia solo sabe lo escrito; que una opción sea la mejor no se puede calificar contra una clave; si propusiera qué acordar, después mediría su propia propuesta; y en una entidad vigilada una recomendación necesita un dueño que responda por ella.
4. **Lo que falta saber** es lo que el material no responde y la decisión necesita. Se dice, no se supone. Lo que los documentos ya dicen —cuándo se decide, quién decide, que el acta la aplazó— no va en `missing`: va en su campo o en la cita.
5. **El plazo es la fecha que un documento fija**, con su cita. Si ninguno la fija, `deadline` queda vacío. El motor calcula cuántos días faltan.
6. **Una decisión tomada** (`status: decided`) lo está porque el acta firmada lo dice, con su cita.
7. **La decisión se cita donde la escribe el material**, en `source`; el acta que la aplaza o la toma se cita aparte. **Cada cita va relativa a la carpeta de la oficina y señala un renglón**: `<archivo>, línea N`, o `<archivo>, punto N` si el documento numera la lista. Puedes agregar el texto citado entre « » después, pero no la reemplaza: «Compromisos, primer punto» no dice qué renglón es.
