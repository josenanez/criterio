# /criterio-portfolio:portfolio-scan 

Terminé el barrido: leí 48 de los 72 documentos y dejé 24 sin tocar porque no habían cambiado. La corrida quedó registrada como `2026-10-16-portfolio-scan-1`.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los volví a registrar.

**Qué hay ahora**
- **Documentos:** 72 en la carpeta, ninguno ilegible.
- **Proyectos:** 13 con ficha. Creé 10 fichas nuevas (PRY-199, 200, 201, 202, 204, 205, 206, 207, 210 y 211) y las sellé. PRY-203, 208 y 209 no cambiaron y las dejé como estaban.
- **Entrada:** no existe la carpeta `entrada/`, así que no moví ni dejé pendiente ningún archivo.
- **Campos sin dato:** 24 en las 10 fichas nuevas. Faltan la autoridad del gerente y la fase en las 10, y el producto en 4 (las actas de PRY-202, 206, 210 y 211 dicen «No aplica»). La autoridad del gerente tampoco aparece en las actas de PRY-203, 208 y 209.
- **Alertas:** el script calculó 54 en 11 proyectos.

**Lo que más pide mirada**
- **Verde contradicho por la evidencia en 7 proyectos** (200, 206, 207, 208, 209, 210 y 211). Por ejemplo, PRY-211 reporta verde con 30 % de avance y una proyección de 22.675 M sobre 18.000 M aprobados.
- **13 hitos declarados cerrados sin acta de recibo.** PRY-202 tiene los cuatro así. Lo que corresponde pedir es el acta.
- **PRY-200:** el cronograma v2 (2026-10-13) mueve un hito 27 días antes de que el comité vea el cambio CC-01, que sigue pendiente.
- **PRY-207:** el cronograma v2 que ya trae el corrimiento de 72 días es del 2026-09-26, doce días antes de la solicitud CC-01 (2026-10-08). Además el despliegue queda después del cierre que fija el acta.
- **Compromisos vencidos sin evidencia:** 8, 6 de ellos en PRY-209. Los otros dos son de PRY-202 y PRY-204.
- **PRY-210:** lleva 20 días sin documentos nuevos. Su factura FV-1941 coincide con el monto del entregable ya recibido, pero dice «Entregables del contrato CT-941», en plural. Conviene confirmar a qué entregable se imputó.
- **PRY-201:** su cierre comprometido (2026-09-10) ya pasó y reporta 81 % en verde. El script no lo marca porque la carpeta no trae cronograma.

**Una anomalía en PRY-209:** el índice reporta 35 citas que no resuelven. Son del bloque `pm_record`, cuyas rutas son relativas a la carpeta del proyecto y no a la raíz de documentos. Los documentos existen y no toqué esa ficha porque es del gerente.

Sí me quedó un asunto pendiente: el informe consolidado que ofrece el comando. Puedo armarlo, y el comité semanal es el 2026-10-23.

Archivos en `/home/claude/banco/ronda-5/retail/espacio/estado`:
- corridas/salida-portfolio-scan.md
- records/

criterio-portfolio 0.3.11 · términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.11