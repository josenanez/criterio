# /criterio-portfolio:portfolio-report html

Generé el informe de portafolio en HTML: 13 proyectos, 12 con hallazgos y 69 señales. Los términos ya estaban vigentes (versión 0.3.13), aceptados por José Francisco Ñáñez el 2026-10-17.

**Qué cambió:** nada. La única instantánea es la de hoy, así que este es el punto de partida y no hay delta. Las 13 fichas (PRY-199 a PRY-211) son del barrido de hoy.

**Hallazgos principales:**
- **Verdes sin sustento (4):** PRY-200, 202, 205 y 207 se declaran en verde, pero los documentos no lo respaldan.
  - PRY-205 proyecta 23,5 % de sobrecosto.
  - PRY-207 tiene el piloto vencido hace 8 días.
- **PRY-211 (rojo):** el proveedor Datos para Cooperativas facturó COP 376.332.909 sin ningún entregable aceptado, y tiene 2 entregables atrasados.
- **PRY-208:** va 117 días (29,6 %) atrasado frente a la línea base original.
- **Control de cambios:** el cambio CC-01 de PRY-203 aprobó 112 días sin que se moviera la línea base.
- **Hitos vencidos:** hay 4 (PRY-206, 207, 208 y 211).
- **Hitos "cumplidos" sin evidencia:** hay 25.
- **Silencio:** PRY-204 lleva 22 días sin documentos.
- **Vacíos:** ningún proyecto tiene autoridad ni fase identificadas, y cinco no tienen producto asociado.

**Dónde quedó el informe:** en `reportes/`, que es la carpeta que sirve Rostrum, con 25 páginas.
- `reportes/index.html` es la vista por campo, con la cadena de evidencia, para quien va a actuar.
- `reportes/decisiones.html` es la vista por decisión, para el patrocinador.
- Hay además una página por proyecto y por producto. El PDF sale de imprimir el HTML.

La configuración dice `pptx`; usé `html` porque lo pediste.

**Pendiente:** la confirmación mensual de cinco campos no se formuló, porque esta sesión no tiene quien responda. Queda para la próxima corrida con interlocutor.

**Corrida registrada:** `2026-10-17-portfolio-report-1`, con el texto completo en `estado/corridas/salida-portfolio-report.md`. Después de registrarla corregí en ese archivo un conteo (25 hitos sin evidencia, no 28). Si la corrida guardó su propia copia del texto, esa copia puede seguir con el 28.

Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

¿Quieres que arme el material de comité para el 2026-10-24, o que entre al detalle de PRY-200 y PRY-211?