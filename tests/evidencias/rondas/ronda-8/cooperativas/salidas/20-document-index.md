# /criterio-portfolio:document-index 

## Carpeta al 2026-10-17

**Documentos:** 76 · **Sin cambio:** 76 · **Hay que releer:** 0

No hay documentos nuevos, cambiados, reguardados, renombrados ni borrados. El único hallazgo son 37 citas de PRY-200 que el índice marca como "ya no resuelven".

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré otra vez.

### Citas que dejaron de resolver
Las 37 son de PRY-200. Los archivos citados sí existen en `PRY-200-crédito-de-libranza-digital/`, así que no se borraron ni se movieron. Mi lectura es que el índice no resuelve las rutas citadas sin el prefijo de la carpeta del proyecto. No lo confirmé en el código del índice.

| Campo | Documento citado |
|---|---|
| identity: code, name, business_area, product, sponsor, manager, committee (7) | 00-gobierno/2025-12-18-acta-constitucion.md |
| declared: status, progress_pct, as_of (3) | 20-seguimiento/2026-10-07-informe-avance.md |
| plan.start_date; money.currency, money.approved (3) | 00-gobierno/2025-12-18-acta-constitucion.md |
| plan.end_date y los 5 hitos (name, baseline_date, current_date, state) (21) | 10-plan/2025-12-18-cronograma-v1.xlsx |
| plan.milestones[2].evidence (1) | 20-seguimiento/2026-10-07-acta-recibo-integración-con-el-core-cooperativo.md |
| money.committed, executed, projection (3) | 20-seguimiento/2026-10-07-informe-avance.md |

### Formatos que no se pudieron leer
El índice no reportó ninguno.

### Qué sigue
No hace falta `/portfolio-scan`, porque `projects_to_recompute` está vacío. Antes de tocar la ficha de PRY-200, hay que confirmar si el problema es de resolución de rutas. No corregí ninguna cita.

Un detalle sin resolver: en la carpeta de PRY-200 está `2026-10-17-notas-reunion.txt`, pero el índice no lo reporta como nuevo. No averigüé si ya estaba indexado o si el índice no lee `.txt`.

La corrida quedó registrada como `2026-10-17-document-index-1`. Tardó 15 segundos y la salida completa está en `estado/corridas/salida-document-index.md`. El número de documentos de la corrida quedó sin medir.