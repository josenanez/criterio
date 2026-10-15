# /criterio-portfolio:portfolio-scan 

Barrido terminado: leí 52 de los 71 documentos, escribí y sellé 10 fichas nuevas y registré la corrida. Los 19 documentos restantes son de PRY-201, PRY-203 y PRY-210. No habían cambiado, así que no los releí.

Los términos (versión 1.1) ya estaban aceptados por José Francisco Ñáñez el 2026-10-15, con comprobante vigente. No los registré otra vez.

**Qué se leyó**
- **Inventario:** había 71 documentos en 13 carpetas de proyecto y todos eran legibles.
- **Lote:** el plan traía un solo lote de 10 proyectos. Los leí uno tras otro en esta conversación, sin subagentes, y sellé cada ficha al terminar su proyecto.
- **`entrada/`:** no existe esa carpeta, así que no moví ni clasifiqué nada.

**Qué hay que mirar**
- **Hitos cerrados sin acta:** hay 21 en el portafolio.
  - PRY-200: 3 hitos.
  - PRY-204: 3 hitos.
  - PRY-211: 2 hitos.
- **PRY-200, cierre ambiguo:** el acta fija el cierre en 2026-07-16, pero el cronograma v2 mueve «Salida a producción» al 2026-10-18 (CC-01, +118 días). Además reporta 53 % de avance con los 5 hitos cerrados. Sus 3 entregables del contrato CT-992 llevan entre 157 y 287 días vencidos.
- **PRY-202 y PRY-206, recibos y facturas:**
  - PRY-202: el licenciamiento de CT-665 figura «recibido» y está facturado, sin acta de recibo.
  - PRY-206: el licenciamiento figura «recibido» en dos contratos, sin acta en ninguno. FV-1319 factura 73,5 M, unos 18 M más de lo que vale el entregable.
- **Costo:** la proyección supera el presupuesto aprobado en PRY-204 (17,2 %), PRY-207 (28,9 %) y PRY-209 (28,4 %).
- **PRY-205 y PRY-208:** lo ejecutado supera lo comprometido. El script no lo marca; lo dejé anotado en la salida.
- **PRY-208, CC-01:** la solicitud de cambio (+113 días) quedó sin línea base nueva, porque ese proyecto no tiene cronograma.
- **Verde con señales en contra:** PRY-202, PRY-207, PRY-209 y PRY-211 declaran verde.
- **Compromiso vencido:** María Restrepo, en PRY-206, para el 2026-09-27.
- **Compromiso sin fecha:** María Restrepo, en PRY-205 («por definir»).
- **PRY-203, fuera de mi alcance:** 13 campos de la ficha del gerente apuntan a una cita sin el prefijo de carpeta, y por eso no cruzan. No es una ficha mía y no la toqué.

**Decisiones tomadas sin preguntar**
- «Producto asociado: No aplica» quedó como `not_found`, no como un producto con ese nombre.
- «Autorizada por el comité» quedó como quien decidió, sin nombre, porque el documento no lo da.
- No inventé dependencias entre proyectos. Las actas dicen «Ninguna declarada».

El pie del informe cita la versión 0.3.8, las 10 fichas tocadas, los campos en `not_found` y el enlace a los términos. Como el barrido cubrió más de un proyecto, puedo generar el informe consolidado.

Archivos están en `/home/claude/banco/ronda-2/cooperativas/espacio/estado/`:
- `corridas/salida-portfolio-scan.md`
- `records/` (las 10 fichas nuevas)
- `snapshots/2026-10-15.json`