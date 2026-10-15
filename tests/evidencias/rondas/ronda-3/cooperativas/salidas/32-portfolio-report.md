# /criterio-portfolio:portfolio-report html

# Portafolio — 2026-10-15

Generé el informe HTML y registré la corrida (`2026-10-15-portfolio-report-1`). Cargué 13 fichas, todas con fecha 2026-10-15. Hay 13 proyectos, 10 con hallazgos y 64 señales en total.

**Términos:** ya estaban vigentes, versión 0.3.9, aceptados por José Francisco Ñáñez el 2026-10-15. No los registré de nuevo. Texto completo: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Dónde quedó el informe**, en `/home/claude/banco/ronda-3/cooperativas/espacio/reportes/` (25 páginas):
- **`index.html`:** vista por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- **`decisiones.html`:** vista por decisión, para el patrocinador y el comité del 2026-10-22.
- **Una página por proyecto.** El PDF sale de imprimir el HTML.

**Qué cambió:** nada. La instantánea anterior tiene la misma fecha que el barrido, así que el diff dio 0 cambios. Esto es el punto de partida.

**Lo principal:**
- **Verdes contradichos:** 5 proyectos declaran verde y la evidencia no lo sostiene (PRY-202, 203, 204, 205 y 208).
- **Hitos sin evidencia:** hay 22 hitos declarados cumplidos sin evidencia. PRY-205 tiene 5, PRY-203 tiene 4, y el más viejo lleva 363 días en PRY-202.
- **Corrimientos sin autorización:** PRY-204 se corrió 112 días y PRY-208 se corrió 33, sin cambio aprobado.
- **PRY-203:** concentra 18 de las 64 señales. Tiene 7 compromisos vencidos, y dos de ellos se reprogramaron 5 y 6 veces.
- **PRY-206:** la proyección de costo está 26,4 % sobre lo aprobado, y el cambio CC-01 no tiene línea base.
- **PRY-209:** el proveedor Soluciones Solidarias tiene 3 entregables atrasados y $1.882.339.743 facturados sin entrega.
- **Silencio:** ningún proyecto pasa de 15 días sin movimiento.

**Notas y límites:**
- Las fichas están en `estado/records/`, no en `estado/fichas/` como dice el comando.
- No desglosé las contradicciones campo por campo, ni las dependencias; el informe remite al detalle en `index.html`.
- La confirmación del mes (5 campos) quedó pendiente, porque la sesión era sin interfaz. Las 5 preguntas están en el informe.
- Los 13 proyectos no tienen patrocinador identificado en la ficha.

Lo que te mostré aquí está guardado entero en `estado/corridas/salida-portfolio-report.md`.

Si quieres, el siguiente paso es preparar el material del comité del 2026-10-22 (`/criterio-portfolio:steering-pack`). También puedo entrar al detalle de PRY-203 o PRY-209.