# /criterio-portfolio:portfolio-scan 

## Barrido terminado — 2026-10-17

Generé 10 fichas nuevas, una por proyecto: PRY-199, 201, 202, 203 y 206 a 211. Leí 66 de los 89 documentos. Los otros 23 no habían cambiado, y de ellos salen las fichas de PRY-200, 204 y 205, que no toqué. No hubo archivos ilegibles. No existe la carpeta `entrada/`, así que no moví nada. Terminé en unos 5 minutos (301 s medidos por la corrida), con un solo lote y sin subagentes.

Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-17 (v0.3.13), así que no los registré de nuevo.

**Lo que ya se ve en los documentos** (las cifras definitivas las calcula el informe consolidado):
- **Hitos cerrados sin acta de recibo:** PRY-203 (3), PRY-206 (3), PRY-211 (3), PRY-208 (2), PRY-210 (2) y PRY-201 (1). Los registré como cerrados, que es lo que declaran, y anoté la falta de prueba.
- **Facturas sin recibo o por encima de lo recibido:**
  - PRY-209 cobró 148,3 M COP sin acta de recibo de ningún entregable del contrato.
  - PRY-210 cobró 487,9 M COP y solo hay recibido un entregable de 339,9 M.
  - PRY-211 cobró 345,8 M COP y solo hay recibido un entregable de 246,8 M.
- **Verde con cifras que no cuadran:** PRY-202 y PRY-208 proyectan más que su presupuesto aprobado. En PRY-202 y PRY-211 el ejecutado supera lo comprometido.
- **PRY-207:** la solicitud de cambio CC-01 sigue pendiente de comité, pero el cronograma v2 ya mueve el piloto lo que ella pide.
- **Compromisos vencidos:**
  - PRY-207: Diana Molina, vencía el 2026-10-10.
  - PRY-211: Sandra Gil, vencía el 2026-09-29.
  - En ambos la fecha es anterior a la reunión que los registra. Conviene confirmarlo con quien levantó la minuta.
- **Estado rojo:** PRY-206 y PRY-207.

**Dos avisos:**
- La ficha de PRY-200 tiene 51 citas que el índice no resuelve, porque las rutas están escritas sin el prefijo de carpeta. No la releí. Hay que corregirla o decidir si se relee.
- «Hallazgo de seguridad en los medios de pago» aparece en el informe de la iluminación LED (PRY-199) y en los de PRY-202, 203, 209 y 211. Parece plantilla. Lo registré como incidencia de cada uno.

La corrida registró 73 hallazgos en total, y en los diez proyectos nuevos no hubo ningún error de lectura.

Si quiere el informe consolidado, el comando es `/criterio-portfolio:portfolio-report`. El comité semanal es el 2026-10-22.

Archivos en `estado/`:
- `corridas/salida-portfolio-scan.md`
- `snapshots/2026-10-17.json`
- `records/PRY-199.json` y las otras nueve fichas

Para armar las fichas escribí un script auxiliar en la carpeta temporal de la sesión. No forma parte del plugin.

criterio-portfolio 0.3.13 · términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.13