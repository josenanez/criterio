# /criterio-portfolio:portfolio-report html

El informe de portafolio quedó generado en HTML y la corrida quedó registrada. Falta solo que lo revises.

**Fichas y términos**
- Las fichas están en `estado/records/`, de PRY-199 a PRY-211, todas del 2026-10-16. No hay carpeta `estado/fichas/`.
- Los términos ya estaban vigentes (v1.1, familia 0.3.11), aceptados por José Francisco Ñáñez el 2026-10-16. No hizo falta volver a registrarlos.
- No existía una instantánea anterior: el diff dio 0 cambios, así que esta corrida es el punto de partida.

**Hallazgos**
- 13 proyectos, 11 con hallazgos y 66 señales en total.
- 7 proyectos declaran verde y la evidencia lo contradice: PRY-200, 202, 204, 205, 206, 207 y 209.
- PRY-200 acumula 14 señales: 25 % declarado frente al 100 % que sostiene el plan, 5 entregables de proveedor vencidos y 207,6 M COP facturados sin entrega. También lleva 20 días en silencio.
- PRY-211 tiene 6 compromisos vencidos y 2 reprogramados 5 o 6 veces. Además, el cronograma y el acta dan fechas de fin distintas (2027-05-31 y 2027-07-23), y no hay forma de saber cuál manda.
- PRY-207 también está en silencio, con 18 días.
- PRY-208 movió su línea base 38 días sin autorización.
- Ningún proyecto tiene autoridad de aprobación identificada (13 de 13).

**Dónde quedó**
- `reportes/index.html`: vista por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- `reportes/decisiones.html`: vista por decisión. Es para el patrocinador o el comité.
- Hay 25 páginas en total, una por proyecto más las dos vistas. El PDF sale de imprimir el HTML.
- Lo que muestro aquí está guardado en `estado/corridas/salida-portfolio-report.md`. La corrida es `2026-10-16-portfolio-report-1`, de 57 segundos. Se leyeron 75 documentos, todos sin cambios.

**Preguntas de confirmación:** el informe incluye cinco preguntas cerradas, pero nadie las respondió en esta sesión de prueba. Quedan para la próxima corrida.

Si hay comité próximo (el 2026-10-23), puedo preparar el material con `/steering-pack`, o entrar al detalle de PRY-200 o PRY-211.