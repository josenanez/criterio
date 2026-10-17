# /criterio-portfolio:portfolio-report html

El informe HTML está generado y la corrida quedó registrada como `2026-10-17-portfolio-report-1`. Tardó 28 segundos y leyó 89 documentos, todos sin cambios.

**Términos:** ya estaban vigentes (versión 1.1, familia 0.3.13) y constan a nombre de José Francisco Ñáñez, 2026-10-17. Por eso no registré una aceptación nueva.

**Fichas:** cargué las 13 de `estado/records/` (PRY-199 a PRY-211), todas del barrido de hoy, así que ninguna está vieja.

**Qué cambió:** nada. La única instantánea es la de hoy, así que el diff da 0 cambios y esta corrida es el punto de partida.

**Hallazgos (73 señales, 12 de 13 proyectos):**
- **Verdes contradichos:** 7 proyectos se declaran en verde y la evidencia no lo sostiene. Por ejemplo, PRY-202 lleva 52 días de atraso y 21,8 % de sobrecosto proyectado.
- **Atrasos mayores al 10 %:** PRY-205 (107 días, 51,7 %), PRY-210 (76 días), PRY-211 (75 días) y PRY-202 (52 días).
- **Hitos cumplidos sin evidencia:** 21 señales de este tipo.
- **Compromisos vencidos:** 11, nueve de ellos en PRY-200.
- **Proveedor y presupuesto:** PRY-209 tiene 95,2 % del presupuesto comprometido y facturación sin entrega.
- **Vacíos:** ninguno de los 13 proyectos tiene identificada la autoridad que aprueba cambios. Seis proyectos no están asociados a ningún producto: PRY-202, 203, 206, 209, 210 y 211.
- **Sin hallazgos:** PRY-199 no tiene señales. No hay proyectos en silencio.

**Dónde quedó el informe:** en `/home/claude/banco/ronda-8/retail/espacio/reportes/`, 24 páginas.
- `index.html` es la vista por campo, con la cadena de evidencia completa. Va para quien va a actuar.
- `decisiones.html` es la vista por decisión, con pregunta cerrada y consecuencia de no decidir. Va para el patrocinador y el comité del 2026-10-22.
- El resto son una página por proyecto, una por producto, `productos.html` y `proyectos.html`.
- Para el PDF se imprime el HTML desde el navegador.

**Pendiente:** la confirmación mensual de cinco campos queda sin hacer, porque nadie responde en esta sesión y no inventé las preguntas.

La configuración pide `pptx`, pero usé `html` porque lo indicó el argumento del comando.

La salida de la corrida está en `/home/claude/banco/ronda-8/retail/espacio/estado/corridas/salida-portfolio-report.md`.