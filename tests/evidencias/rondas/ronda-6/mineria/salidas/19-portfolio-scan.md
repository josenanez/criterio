# /criterio-portfolio:portfolio-scan 

## Barrido terminado — 2026-10-16

Leí 52 de los 78 documentos y escribí 10 fichas nuevas. Quedaron sin tocar las de PRY-202, PRY-205 y PRY-208, que tienen 26 documentos sin cambio.

- **Términos:** ya estaban vigentes (v1.1, familia 0.3.12, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.
- **Fichas nuevas:** PRY-199, 200, 201, 203, 204, 206, 207, 209, 210 y 211. Las sellé una por una y todas aceptaron el sello.
- **Ilegibles y movidos:** ninguno ilegible. No movimos nada porque no existe carpeta `entrada/`.
- **Datos sin encontrar:** la autoridad y la fase no aparecen en ninguna acta. PRY-206, 209 y 211 no tienen cronograma ni contratos en la carpeta.

**Lo que más conviene mirar** (las fichas guardan la declaración y la evidencia por separado, no son dictamen):
- **Cronograma sin motivo (PRY-203):** el cronograma v2 movió la licencia del 2026-01-21 al 2026-05-21 sin motivo ni aprobación. Además hay un cambio de alcance (CC-01, +120 días) pendiente de comité y un compromiso vencido.
- **Facturas contra actas (PRY-201, 207 y 210):**
  - PRY-201 tiene facturado el CT-600 con sus entregables sin acta de recibo.
  - PRY-207 tiene facturado más de lo aceptado.
  - PRY-210 también, y además recibió un entregable sin acta.
- **Hitos cerrados sin acta:** hay 20 hitos declarados cerrados sin acta que lo pruebe, contando todo el portafolio.
- **Cambios pendientes:** PRY-209 y PRY-211 tienen solicitudes de cambio pendientes (+93 y +102 días).
- **Citas de PRY-205:** las de su ficha no resuelven porque no incluyen la carpeta del proyecto. No lo corregí porque no se leyó en esta corrida.

La corrida registró 60 hallazgos en total y la salida completa quedó en `estado/corridas/salida-portfolio-scan.md`.

**Tres cosas a tener en cuenta:**
- **Error mío corregido:** en las fichas sin cronograma dejé `milestones` con un formato inválido y el cierre falló. Lo corregí a una lista vacía, regeneré la instantánea y registré la corrida sin problema. Los sellos no se tocaron.
- **Tiempo no medido:** la corrida salió con `segundos: null`. Ya había marcado el arranque, pero el sistema no registró la duración.
- **Carpeta ajena:** existe `estado/PRY-205-…/` con un estado propio que este barrido no usa y que no toqué.

Si hay más de un proyecto con ficha, puedo generar el informe consolidado con `/portfolio-report`.

*Pie: criterio-portfolio 0.3.12 · términos v1.1 (https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.12) · fichas tocadas: 10 · campos en `not_found` por ficha: autoridad y fase en todas; producto en 201, 206, 209, 210 y 211; cronograma y contratos en 206, 209 y 211.*