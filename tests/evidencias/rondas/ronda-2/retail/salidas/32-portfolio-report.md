# /criterio-portfolio:portfolio-report html

**Informe de portafolio generado y corrida registrada (2026-10-15-portfolio-report-1).**

Cargué 13 fichas, todas del 2026-10-15, desde `estado/records/` (no existe `estado/fichas/`). Los términos v1.1 ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-15, así que no los volví a registrar.

**Qué cambió:** nada. La instantánea previa es de hoy, así que el diff dio 0 cambios y este informe es el punto de partida.

**Hallazgos:** 60 señales en 12 de 13 proyectos. Solo PRY-199 sale limpio.
- **Verdes contradichos (5):** PRY-202, 203, 205, 206 y 211 declaran verde contra su propia evidencia.
- **Hitos cumplidos sin evidencia:** 29 señales en 12 proyectos. El más viejo es PRY-203, con 444 días.
- **Tiempo:** PRY-201 va +91 días, PRY-211 +77 y PRY-208 +41. PRY-208 y PRY-211 tienen replanificación no autorizada.
- **Costo:** PRY-205 proyecta +25,6% sobre lo aprobado y PRY-204 +22,4%.
- **Compromisos:** 4 vencidos (PRY-204, 207, 208, 211) y 2 sin fecha (PRY-205, 209).
- **Proveedor de PRY-206:** dos entregables vencidos (233 y 128 días) y uno entregado sin evidencia de aceptación.
- **Gobierno:** los 13 proyectos salen sin autoridad de aprobación identificada.
- **Silencio y dependencias:** ningún proyecto supera el umbral de 15 días y `compute` no devolvió dependencias en riesgo.

**Dónde quedó:** `/home/claude/banco/ronda-2/retail/espacio/reportes/` (24 páginas).
- `index.html` va a quien actúa (gerente de PMO y líderes de proyecto). Es por campo, con la cadena de evidencia.
- `decisiones.html` va al patrocinador y al comité del 2026-10-22. Es por decisión, solo lo que excede la facultad del gerente.
- Hay además una página por proyecto. El PDF sale de imprimir el HTML.

**Confirmación mensual:** no la apliqué; la sesión es sin interfaz y no hay nadie que responda.

Lo que le mostré a la persona quedó en `estado/corridas/salida-portfolio-report.md`. El pie con versión 0.3.8, fichas aplicadas y términos está al final de ese archivo: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.8

Si quiere seguir, puedo armar el material del comité del 2026-10-22 o entrar al detalle de los cinco verdes contradichos.