# /criterio-portfolio:portfolio-report html

El informe HTML del portafolio está generado: 24 páginas en `/home/claude/banco/ronda-1/mineria/espacio/reportes/`. La corrida quedó registrada como `2026-10-14-portfolio-report-1`.

- **Cargado:** 13 fichas (PRY-199 a PRY-211), todas con barrido del 2026-10-14. Los términos v1.0 ya estaban aceptados en la configuración.
- **Qué cambió:** nada. La única instantánea es la de hoy, así que esta corrida es el punto de partida y no hay delta.
- **Hallazgos:** 39 señales en 9 proyectos. Es lo que el script `compute` calculó, y yo no recalculé nada.
- **Verdes sin sustento:** PRY-202, PRY-208 y PRY-211 declaran verde y la evidencia no lo sostiene.
- **Sobrefacturación:** PRY-206 facturó 65,9 M COP por encima de lo aceptado, y PRY-211 186,9 M COP por encima.
- **Costo:** la proyección de PRY-207 supera lo aprobado en 24,1 %.
- **Tiempo:** PRY-210 lleva 91 días de atraso contra la línea base original (17,2 %).
- **Contradicción:** PRY-208 tiene dos fechas de fin distintas, 2026-06-19 en el cronograma y 2026-07-21 en el acta, de la misma fecha y sin forma de saber cuál es más nueva.

**Qué vista va a quién:**
- **`index.html`:** vista por campo con la cadena de evidencia completa. Es para quien va a actuar.
- **`decisiones.html`:** vista por decisión, para el patrocinador y el comité del 2026-10-28. No es la anterior recortada.
- **PDF:** sale de imprimir el HTML.

- **Formato:** la configuración dice `pptx`, pero usé `html` porque se pidió en la invocación.
- **Confirmación mensual:** toca este mes (5 campos), pero no se formularon las preguntas porque la sesión no tiene interfaz.
- **Carpeta de fichas:** la skill habla de `estado/fichas/`, pero en este estado están en `estado/portafolio/records/`; usé esa.

Lo que mostré, entero, está en `estado/portafolio/corridas/salida-portfolio-report.md`.