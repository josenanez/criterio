# /criterio-portfolio:portfolio-scan 

El barrido terminó: leí 51 de 75 documentos y dejé 10 fichas nuevas, cada una sellada al cerrar su proyecto.

- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no volví a registrarlos.
- **Qué leí y qué no:** los 24 documentos de PRY-202, 204 y 206 no habían cambiado y no los releí. Ninguno de los 75 fue ilegible. Todo cupo en un solo lote.
- **Fichas nuevas:** PRY-199, 200, 201, 203, 205, 207, 208, 209, 210 y 211. En `entrada/` no había nada que mover.
- **Corrida registrada:** quedó como `2026-10-15-portfolio-scan-1`, con 67 hallazgos entre los 13 proyectos. El registro marca `relectura: sin_cambio 75, releidos 0` porque lo calculó después de sellar.

Lo que más pesa, según las señales que calculó el script:
- **Verde que no se sostiene:** PRY-203, 207, 208, 209 y 210 reportan verde, pero tienen hitos cerrados sin acta, avance fuera de lo que sostiene el plan, sobrecosto o compromisos vencidos.
- **Hitos cerrados sin acta:** son 24 en la cartera; solo tres tienen acta de recibo (diseño funcional de PRY-199 y PRY-209, ambiente de pruebas de PRY-203).
- **Cambios autorizados sin línea base nueva:** PRY-203 (CC-01), PRY-205 (CC-01) y PRY-207 (CC-01 y CC-02). En PRY-200 y PRY-210 el cronograma v2 ya movió las fechas mientras el cambio sigue pendiente de comité.
- **Presupuesto:** la proyección supera lo aprobado en PRY-208 (+25,9 %) y PRY-203 (+13,7 %). En PRY-205 lo ejecutado supera lo comprometido y ningún documento lo explica.
- **Compromisos vencidos:** Diana Molina en PRY-200 y PRY-203, y María Restrepo en PRY-208. Otros dos compromisos (PRY-201 y PRY-210) no tienen fecha.
- **Campos sin dato:** ninguna acta nombra la facultad del gerente ni la fase. Son 28 campos en `not_found`.

El índice sigue marcando como fuente sin resolver los campos del gerente en PRY-206 (la ficha del gerente, que este barrido no reescribe).

Puedo preparar el informe consolidado con `/criterio-portfolio:portfolio-report`.

Archivos en `/home/claude/banco/ronda-2/bancos/espacio/estado`:
- `corridas/salida-portfolio-scan.md`
- `records/`
- `snapshots/2026-10-15.json`

Criterio Portfolio 0.3.8 · Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal