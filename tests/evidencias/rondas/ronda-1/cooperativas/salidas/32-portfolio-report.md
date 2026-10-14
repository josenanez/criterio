# /criterio-portfolio:portfolio-report html

Generé el informe del portafolio en HTML y dejé la corrida registrada (`2026-10-14-portfolio-report-1`). El script midió 27 segundos y 72 documentos, ninguno releído.

Los términos ya estaban aceptados: la versión 1.0 de la configuración coincide con `TERMS.md`, a nombre de José Francisco Ñáñez el 2026-10-14. Las fichas están en `estado/records/`, no en `estado/fichas/`. Usé las 13 que hay, de la instantánea del 2026-10-14.

**Qué cambió:** nada. La instantánea comparada es de la misma fecha, así que es un punto de partida y no hay diferencia contra una corrida anterior.

**Resultado:** 13 proyectos, 12 con hallazgos y 60 señales en total.
- **Verdes contradichos (5):** PRY-201, 204, 208, 209 y 210 se declaran en verde, pero la evidencia los contradice.
- **Silencio (3):** PRY-200 y 201 llevan 24 días sin movimiento, y PRY-211 lleva 17.
- **Desvío contra la línea base original:**
  - PRY-209: +114 días (60 %).
  - PRY-205: +112 días (34,6 %).
  - PRY-208: +100 días y +16,1 % en costo.
  - PRY-210: +69 días.
  - PRY-203: +23 días.
  - Replanificaciones sin autorización: PRY-203, 205 y 208.
- **Hitos sin evidencia:** hay 26 hitos declarados cumplidos sin documento que lo respalde. PRY-211 tiene 5.
- **Compromisos vencidos (3):** PRY-204 (Gustavo Neira, 17 días), PRY-205 (Óscar Ramírez, 15 días) y PRY-210 (Beatriz Cuéllar, 11 días).
- **Vacíos:** los 13 proyectos no tienen autoridad registrada, y 5 no tienen producto asociado (PRY-202, 205, 208, 209 y 210).

La confirmación mensual de cinco campos no se corrió porque nadie podía responder en esta sesión de prueba. En esta corrida el script no devolvió dependencias en riesgo entre proyectos.

**Archivos:** están en `/home/claude/banco/ronda-1/cooperativas/espacio/reportes/` (25 páginas, una por proyecto más las dos vistas).
- `index.html` es la vista por campo, con la cadena de evidencia completa, para quien va a actuar.
- `decisiones.html` es la vista por decisión, para el patrocinador y el comité del 2026-10-21.
- El PDF sale de imprimir el HTML.
- El texto de este resumen quedó en `estado/corridas/salida-portfolio-report.md`.