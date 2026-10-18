# /criterio-portfolio:health-check PRY-200

El diagnóstico de PRY-200 (Tienda en línea) está hecho. La carpeta no sostiene que el proyecto esté en verde ni que su avance sea 57%.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo.

**Dictamen:** de 17 afirmaciones, 3 están sostenidas, 12 sin sustento y 2 contradichas. Leí los 6 documentos de la carpeta, fechados entre 2025-08-14 y 2026-10-09. Ningún otro proyecto menciona a PRY-200.

- **Contradichas:**
  - El estado verde choca con dos entregables del contrato CT-497 vencidos y pendientes, uno hace 294 días y otro hace 43.
  - El avance de 57% choca con el cronograma: 4 de 5 hitos cerrados soportan entre 80% y 100%.
- **Hitos sin evidencia:** los cuatro hitos del cronograma marcados como cerrados no tienen ningún documento de cierre. Llevan 328, 237, 146 y 54 días de vencidos.
- **Dinero:** salvo el presupuesto aprobado (6.800.000.000 COP), todas las cifras salen solo del informe de avance.
- **Factura:** la FV-1497 es por 445.577.090 COP y no dice a qué entregable corresponde. No hay acta de recibo firmada, que el contrato exige para facturar.
- **Compromiso vencido:** Beatriz Cuéllar debía entregar el «punto 17» el 2026-10-08. Lleva 9 días vencido, sin entrega, y ningún documento dice qué es.
- **Hallazgo de seguridad:** el hallazgo en los medios de pago y el riesgo regulatorio solo aparecen en el informe de avance, sin dueño.
- **Gobierno:** el acta no declara la autoridad del gerente, así que el supuesto cambio de fecha del despliegue no tiene quién lo apruebe. Tampoco hay solicitud de cambio.

No recomendé detener, continuar ni reestructurar. Puedo preparar el punto de comité con la lista de lo que falta, o llevar las dos contradicciones al gerente como preguntas.

La corrida quedó registrada como `2026-10-17-health-check-1`. El diagnóstico completo está en `/home/claude/banco/ronda-9/retail/espacio/estado/corridas/salida-health-check.md`.

Dos cosas que debes saber:
- No encontré la definición del «pie de rigor» en el plugin, así que escribí un pie breve propio.
- El registro de la corrida cuenta 13 proyectos y 90 hallazgos del portafolio entero, porque `compute` recorre todo. Los de PRY-200 son 10 y coinciden con lo que reporté.