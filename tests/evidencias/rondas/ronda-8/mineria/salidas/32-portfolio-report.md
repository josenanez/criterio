# /criterio-portfolio:portfolio-report html

Generé el informe en HTML con las dos vistas más una página por proyecto y por producto: 23 páginas en total.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo. Resumen: Criterio produce borradores de trabajo, no asesoría, y la verificación es de usted. Texto completo: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Dónde quedó.** Todo está en `/home/claude/banco/ronda-8/mineria/espacio/reportes/`.
- **`index.html`:** vista por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- **`decisiones.html`:** vista por decisión, solo lo que excede la facultad de quien gerencia. Es para el patrocinador.
- **PDF:** sale de imprimir el HTML.

**Fichas.** Cargué 13 proyectos con datos al 2026-10-17. El diff no encontró cambios, porque la instantánea anterior es de hoy.

**Hallazgos.**
- **Alertas:** 11 de los 13 proyectos tienen alertas, 52 en total.
- **Verdes contradichos:** 7 proyectos declarados en verde no los sostiene la evidencia.
- **Concentración:** PRY-201 concentra 15 alertas, PRY-204 tiene 7 y PRY-200 tiene 6.
- **Sin alertas:** PRY-199 y PRY-208.
- **Autoridad:** los 13 proyectos están sin autoridad nombrada.
- **Sin producto asociado:** 7 proyectos.

**Corrección mía.** La primera corrida registrada (`2026-10-17-portfolio-report-1`) tenía una nota que omitía PRY-201. Corregí la salida y registré una segunda corrida (`2026-10-17-portfolio-report-2`) con la nota correcta. La segunda no midió el tiempo de ejecución, así que la medida de 25 segundos está en la corrida 1.

**Confirmación mensual.** No la hice, porque en esta sesión no hay nadie a quien preguntar. Queda para la próxima.

La salida completa está en `estado/corridas/salida-portfolio-report.md`. Si hay comité cerca (el próximo es el 2026-10-21), puedo armar el material con `/steering-pack`, o entrar al detalle de PRY-201.