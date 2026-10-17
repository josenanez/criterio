# /criterio-portfolio:document-index 

## Carpeta al 2026-10-17

**Documentos:** 89 · **Sin cambio:** 89 · **Hay que releer:** 0

No cambió el contenido de ningún documento. Tampoco hay documentos solo reguardados, renombrados, movidos ni borrados. No hace falta correr `/portfolio-scan`.

**Citas que no resuelven:** el índice marca 15 citas de PRY-200 como `source_missing`. Los tres archivos citados sí están en la carpeta del proyecto:
- `00-gobierno/2025-06-26-acta-constitucion.docx`: 11 campos.
- `10-plan/2025-06-26-cronograma-v1.csv`: `plan.end_date`.
- `20-seguimiento/2026-10-13-informe-avance.md`: `money.committed`, `executed` y `projection`.

Es probable que sea un fallo de rutas, no una cita rota. La ficha cita con el prefijo del proyecto (`PRY-200-crédito-de-libranza-digital/00-gobierno/…`) y el índice reporta la ruta sin ese prefijo. No lo verifiqué en el código del script. Lo dejé escrito como una señal por confirmar.

No hubo formatos ilegibles, porque este comando no lee documentos.

**Términos:** ya estaban vigentes para la versión 0.3.13, aceptados por José Francisco Ñáñez el 2026-10-17, así que no registré una aceptación nueva.

**Corrida:** quedó registrada como `2026-10-17-document-index-1` (26 segundos, 13 proyectos). La salida está en `estado/corridas/salida-document-index.md`.

La corrida también devolvió 66 hallazgos abiertos de corridas anteriores, entre ellos 23 de `milestone_met_without_evidence`. No salen de este índice.