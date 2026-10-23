# /criterio-portfolio:portfolio-report html

Generé el informe HTML del portafolio con las fichas de hoy (2026-10-23). No hay diff porque es el punto de partida: la instantánea de hoy es la primera y dio 0 cambios.

Los términos v1.2 ya estaban aceptados a nombre de José Francisco Ñáñez para esta prueba. Las 13 fichas están frescas, así que no hizo falta un barrido previo.

**Lo que muestra el informe**
- **Hallazgos:** 13 proyectos, 9 con hallazgos y 54 señales en total.
- **Verdes sin sustento:** 5 proyectos se declaran en verde y la evidencia los contradice: PRY-200, 204, 205, 208 y 210.
- **Sobrecosto proyectado:** PRY-202 (+14,4 %) y PRY-204 (+20,5 %) pasan el umbral del 10 %.
- **En silencio:** PRY-210 lleva 21 días sin documentos nuevos.
- **Hito vencido:** PRY-209 tiene "Pozos perforados" vencido hace 10 días.
- **Compromisos:** PRY-200 tiene 8 vencidos y 2 reprogramados 5 o 6 veces.
- **Vacíos:** ninguna de las 13 fichas tiene autoridad aprobadora registrada, y 9 proyectos no tienen producto asignado.

La confirmación mensual de cinco campos queda vacía en esta corrida. El script no generó los campos y la sesión no tiene interfaz para preguntar.

**Archivos**, en `/tmp/claude-0/-home-claude/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/r11/oil-gas/espacio/reportes/`:
- `index.html` va para quien va a actuar. Va por campo y trae la cadena de evidencia completa.
- `decisiones.html` va para el patrocinador. Va por decisión, con pregunta cerrada y consecuencia de no decidir.
- También quedaron las páginas por proyecto (`PRY-199.html` a `PRY-211.html`), las de producto, `productos.html` y `proyectos.html`.
- El PDF sale de imprimir el HTML.

La corrida quedó registrada como `2026-10-23-portfolio-report-1`, con lo que te mostré guardado en `estado/corridas/salida-portfolio-report.md`.

Pie: criterio-portfolio 0.8.0, 13 fichas del 2026-10-23, sin campos en conflicto. Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal

Si hay comité próximo (29 de octubre), puedo preparar el material con `steering-pack`, o entrar al detalle de PRY-200.