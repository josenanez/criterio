# /criterio-portfolio:portfolio-report html

El informe en HTML está generado: 25 páginas en `/home/claude/banco/ronda-2/cooperativas/espacio/reportes/`. Usé las 13 fichas del barrido de hoy (2026-10-15), sin ninguna con más de una semana. Los términos ya estaban aceptados por José Francisco Ñáñez (2026-10-15, versión 0.3.8), así que no los registré de nuevo.

**Qué cambió:** nada. La única instantánea es la de hoy, así que este informe es el punto de partida y no tiene delta.

**Qué encontró el cálculo:** 59 señales en 12 de los 13 proyectos. El proyecto sin señales es PRY-199.
- **Verdes sin respaldo:** cinco proyectos declaran verde y la evidencia lo contradice: PRY-201, 202, 207, 209 y 211.
- **Hitos "cumplidos" sin evidencia:** 21 en total. PRY-201 tiene 5 de 5 y PRY-203 tiene 4 de 4.
- **Retrasos fuertes:** PRY-200 va +118 días y PRY-210 va +177 días contra la línea base original.
- **Sobrecosto:** PRY-204 +17,2 %, PRY-207 +28,9 % y PRY-209 +28,4 %.
- **Proveedores:** PRY-201 facturó 121.861.832 COP sin entrega. PRY-206 facturó 17.974.024 COP por encima de lo aceptado.
- **Contradicción de fechas:** en PRY-203, la fecha de fin es 2026-09-03 en el cronograma de la PMO y 2026-10-15 según el gerente del proyecto.
- **Silencio y vencidos:** PRY-202 lleva 18 días en silencio y tiene un hito vencido.
- **Vacíos:** ninguno de los 13 proyectos tiene autoridad identificada, y 5 no tienen producto asignado.

**Qué vista va a quién:**
- `index.html` es la vista por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- `decisiones.html` es la vista por decisión, para el patrocinador y el comité.
- El PDF sale de imprimir el HTML.

**Cosas por saber:**
- Las fichas están en `estado/records/`, no en `estado/fichas/` como dice el comando, y las usé desde ahí.
- La confirmación mensual de cinco campos no se hizo, porque en esta sesión nadie podía responder.
- Dejé la dependencia de PRY-202 con los proyectos que integran con el core solo como pregunta, porque ninguna ficha la declara por código.

La corrida quedó registrada como `2026-10-15-portfolio-report-1`, con la salida en `estado/corridas/salida-portfolio-report.md`.

Si hay comité el 22 de octubre, el siguiente paso sería preparar el material con `/criterio-portfolio:steering-pack`, o entrar al detalle de PRY-201, 202 y 207.

Pie: criterio-portfolio 0.3.8 · 13 fichas del 2026-10-15 · campo incierto: PRY-203 `plan.end_date` · términos: https://www.josenanez.com/es/agents/criterio-pmo/legal