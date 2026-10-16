# /criterio-portfolio:portfolio-scan 

Barrido terminado y registrado como `2026-10-15-portfolio-scan-1`.

Los términos ya estaban vigentes (v0.3.10, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré otra vez. Sin carpeta `entrada/` ni archivos ilegibles, no hubo nada que mover ni omitir.

- **Documentos:** 66 en la carpeta, 38 leídos y 28 sin cambio.
- **Proyectos:** 13 con ficha. Escribí y sellé 10 fichas nuevas: PRY-199, 200, 201, 202, 203, 206, 207, 208, 210 y 211. PRY-204, 205 y 209 no cambiaron y no las toqué.
- **Ejecución:** un solo lote, uno tras otro y sin subagentes.
- **Tiempo:** 122 segundos medidos por la corrida.

El código calculó 56 hallazgos sobre los 13 proyectos, incluidos los de PRY-204, 205 y 209. Lo que más pesa:
- **Hitos cerrados sin acta de recibo (18):** en PRY-200, 202, 203, 207 y 208, más 1 en PRY-204.
- **Factura sin entrega (PRY-203):** la factura FV-1345 por 459.463.652 COP no tiene acta de recibo. Los 4 entregables del contrato CT-345 aparecen «en curso» y también quedaron marcados como atrasados.
- **Cierres vencidos con avance incompleto:** PRY-200, 201, 202 y 203. PRY-200 y PRY-203 declaran verde pese a eso, y PRY-211 también declara verde.
- **Compromisos vencidos:** 9, entre ellos los puntos 7 y 22 de PRY-202 y el punto 39 de PRY-211. El punto 37 de PRY-207 no tiene fecha.
- **Cambio sin decidir:** la solicitud CC-01 de PRY-201 (+59 días, +118.000.000 COP) sigue pendiente de comité, y el proyecto ya reporta rojo.
- **PRY-209:** el índice marcó como fuente faltante las citas de la ficha del gerente (`ficha-pm.json`), aunque los documentos están en disco. No la modifiqué. Conviene revisarla con `document-index`.

Ninguna de las 10 actas declara la autoridad del gerente; la fase tampoco aparece en ningún documento.

El informe consolidado queda disponible con `portfolio-report`, porque ya hay más de un proyecto.

Archivos en `/home/claude/banco/ronda-4/retail/espacio/estado/`:
- `corridas/salida-portfolio-scan.md`
- `snapshots/2026-10-15.json`
- `records/`

Criterio-portfolio 0.3.10 · Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.10