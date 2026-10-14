# /criterio-portfolio:document-index 

Terminé el índice. No hay documentos por releer, pero 24 citas de PRY-208 no resuelven.

## Carpeta al 2026-10-14

**Documentos:** 72 · **Sin cambio:** 72 · **Hay que releer:** 0

No hay contenido cambiado, reguardados, renombrados ni borrados. Por eso no hace falta `/portfolio-scan`.

**Citas rotas:** las 24 son de PRY-208 y salen de `00-gobierno/ficha-pm.json`. Citan estos documentos:
- el acta de constitución (6 campos de identidad)
- las notas del 2026-10-14 (los compromisos 0, 2 y 3, y el riesgo 0)
- el comité del 2026-10-11 (el compromiso 1)

Los tres documentos existen y no cambiaron. La ficha del gerente cita la ruta relativa a la carpeta del proyecto, y el índice busca desde `documentos/proyectos/`. En cambio, `estado/records/PRY-208.json` sí cita con el prefijo `PRY-208-motor-de-crédito/`. Esto es una hipótesis por la forma de las rutas y no la comprobé en el código del índice. No corregí ninguna cita.

Los términos 1.0 ya constaban en la configuración, a nombre de José Francisco Ñáñez con fecha 2026-10-14, así que no pedí aceptación de nuevo.

**Formatos no legibles:** ninguno. Este comando solo cuenta y compara.

La salida está en `estado/corridas/salida-document-index.md` y la corrida quedó registrada como `2026-10-14-document-index-1`. Tardó 22 segundos. El registro dejó el número de documentos sin medir (`documentos: null`).

Hay además una carpeta `estado/PRY-208-motor-de-crédito/` con su propio estado anidado que no esperaba. No la toqué.