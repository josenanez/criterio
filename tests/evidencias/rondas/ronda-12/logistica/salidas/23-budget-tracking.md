# /criterio-portfolio:budget-tracking portafolio

## Presupuesto — Portafolio Logística al 2026-10-28

Revisé los 13 proyectos (PRY-199 a PRY-211). Todo está en COP y no convertí nada. El aprobado sale del acta de cada proyecto. Comprometido, ejecutado y proyección salen del último informe de avance, y son declaraciones del gerente. Ninguna alerta de presupuesto cruza un umbral.

- **Comprometido sobre el umbral de 90%:** ningún proyecto lo pasa. El más alto es PRY-211, con 75.2% comprometido y 198350098 de disponible real.
- **Proyección sobre el aprobado:** PRY-202 (+4.5%), PRY-207 (+4.2%) y PRY-206 (+0.6%). Ninguna llega al umbral de 10%, pero las tres exceden lo aprobado.
- **Ejecutado mayor que comprometido:** pasa en PRY-200, PRY-202 y PRY-208. El informe no define "comprometido". Si incluye lo ya ejecutado, las cifras están mal. Si es lo que falta por causar, el disponible real de esos tres está sobrestimado. No lo puedo resolver desde los documentos.
- **Avance declarado frente a ejecución:**
  - PRY-207 declara 24% de avance con 3 de 3 hitos cumplidos y 38.3% ejecutado.
  - PRY-208 lleva 57.6% ejecutado frente a 43% declarado.
  - PRY-204 lleva 17.2% ejecutado frente a 53% declarado.
  - PRY-200, PRY-201 y PRY-206 declaran entre 69% y 77% con 28.6% a 47.3% ejecutado, y tienen hitos cumplidos sin evidencia.
- **Aprobado viejo:** PRY-202, PRY-207 y PRY-204 tienen un aprobado de 12 a 16 meses, sin ningún movimiento de presupuesto declarado.
- **Sin dato:**
  - No hay línea base de presupuesto en ninguna ficha. No pude dar original, vigente ni desviación de costo.
  - Las replanificaciones de presupuesto están en `not_found`. Las que aparecen en `compute` son de cronograma.
  - No sumé el portafolio, porque el script no entrega totales de dinero.

**Siguiente paso:** puedo preparar la solicitud de cambio de PRY-202, PRY-207 o PRY-206, que exceden el aprobado. También puedo armar el detalle por proveedor de PRY-211, que es el que más cerca está del tope.

Los términos estaban vigentes (v1.3, aceptados por José Francisco Ñáñez el 2026-10-28), así que no hubo que registrarlos de nuevo. La corrida quedó registrada como `2026-10-28-budget-tracking-1`.

Archivos en `/home/claude/r12/logistica/espacio/estado/corridas/`:
- salida-budget-tracking.md