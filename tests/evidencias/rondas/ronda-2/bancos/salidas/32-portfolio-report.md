# /criterio-portfolio:portfolio-report html

El informe de portafolio está generado: 13 proyectos, 11 con hallazgos y 67 señales en total. Seis proyectos reportados en verde están contradichos por la evidencia: PRY-202, 203, 207, 208, 209 y 210.

Se usaron las 13 fichas de `estado/records/`, todas barridas hoy (2026-10-15). Los términos ya estaban vigentes (v0.3.8, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo.

- **Qué cambió:** nada que reportar. La única instantánea es la de hoy, así que este es el punto de partida y no hay delta contra el que medir.
- **Contradicción de fechas:** PRY-206 tiene dos fechas de fin, 2026-09-25 en el cronograma y 2026-11-11 en el acta. Las dos fuentes son del mismo día (2025-06-02), así que no se puede decir cuál prevalece.
- **Facturado sobre lo aceptado:** en PRY-206, Redes del Norte facturó 1.317,8 M y lo aceptado suma 920,1 M, una diferencia de 397,8 M.
- **Otros desvíos grandes:**
  - Costo de PRY-204: +27,6 %.
  - Costo de PRY-208: +25,9 %.
  - Atraso de PRY-207: 143 días.
  - Atraso de PRY-200: 98 días sin autorización.
- **Vacías:** no hay proyectos en silencio (el máximo es PRY-201, 11 días) ni dependencias en riesgo marcadas por el script.
- **Pendiente:** no generé las cinco preguntas de confirmación del mes porque nadie puede responder en esta sesión.
- **Columna "Declarado":** en la tabla de estado general, para los proyectos sin estado verde dice "no consta en el cómputo". No verifiqué qué estado declaran en sus fichas.

La corrida quedó registrada como `2026-10-15-portfolio-report-1` (75 documentos, 41 segundos, ninguno releído). Lo que se muestra aquí está en `estado/corridas/salida-portfolio-report.md`.

Los archivos están en `/home/claude/banco/ronda-2/bancos/espacio/reportes/` (26 páginas):
- **`index.html`:** vista por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- **`decisiones.html`:** vista por decisión, solo lo que excede la facultad de quien gerencia. Es para el patrocinador y el comité del 2026-10-22.
- **Páginas de apoyo:** una por proyecto, una por producto, más `proyectos.html` y `productos.html`.

El PDF sale de imprimir el HTML desde el navegador.

Criterio-portfolio 0.3.8 · fichas aplicadas: 13 (2026-10-15) · campos inciertos: la fecha de fin de PRY-206, 13 autoridades sin identificar y 4 proyectos sin producto · términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.8