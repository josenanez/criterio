# /criterio-portfolio:portfolio-report html

Generé el informe HTML del portafolio y registré la corrida como `2026-10-15-portfolio-report-1`. Los términos ya estaban vigentes (aceptados por José Francisco Ñáñez el 2026-10-15, versión 0.3.9), así que no hubo que registrarlos de nuevo.

Cargué las 13 fichas, todas con barrido del 2026-10-15. Ninguna pasa de 7 días en silencio. El diff dio 0 cambios, porque la instantánea anterior es del mismo día, así que no hay delta real.

Resultado: 10 de los 13 proyectos tienen hallazgos, con 61 señales en total.
- **Verdes contradichos:** 7 proyectos declaran verde y la evidencia no lo sostiene: PRY-200, 201, 205, 207, 208, 209 y 210.
- **Más señales:** PRY-201 con 17 y PRY-205 con 11. PRY-205 tiene 4 entregables de proveedor atrasados y una factura sin entrega.
- **Hitos:** hay 18 hitos dados por cumplidos sin evidencia y 2 vencidos (PRY-206 y PRY-209).
- **Costo:** PRY-208 y PRY-209 pasan el umbral del 10 %.
- **Sin hallazgos:** PRY-199, 203 y 211.
- **Silencio y dependencias:** ningún proyecto está en silencio ni tiene dependencias declaradas.
- **Vacíos de información:** ningún proyecto tiene autoridad registrada y 6 no tienen producto asociado.

No hice la confirmación mensual de cinco preguntas, porque nadie podía responder en esta prueba. Queda para la próxima corrida con interfaz.

Archivos en `/home/claude/banco/ronda-3/retail/espacio/reportes/2026-10-15-portafolio/` (24 páginas):
- **`index.html`:** vista por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- **`decisiones.html`:** vista por decisión, solo lo que excede la facultad de quien gerencia. Es para el patrocinador.
- **Otras páginas:** una por proyecto, una por producto, más `proyectos.html` y `productos.html`.
- **PDF:** sale de imprimir el HTML.

Lo que mostré en esta respuesta, entero, está en `/home/claude/banco/ronda-3/retail/espacio/estado/corridas/salida-portfolio-report.md`.

Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal