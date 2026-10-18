# /criterio-portfolio:vendor-tracking PRY-211

En PRY-211 hay un entregable del proveedor facturado sin acta de recibo y dos entregables vencidos sin evidencia. Falta el dato de vigencia y preaviso del contrato.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los volví a registrar. El contrato CT-110 con Servicios Ambientales del Norte sí está en la carpeta.

| Entregable | Fecha comprometida | Estado | Evidencia |
|---|---|---|---|
| Licenciamiento del software | 2025-09-26 | Vencido 386 días | Ninguna |
| Bolsa de horas de ingeniería | 2026-01-27 | Vencido 263 días | Ninguna |
| Calibración de sensores | 2026-05-30 | Declarado aceptado | Ninguna acta en la carpeta |

- **Facturado:** hay una sola factura, FV-1110, por 392.117.057 COP. Ese monto coincide con lo aceptado, así que el script no levanta la señal de factura por encima de lo aceptado. Esa coincidencia depende de una aceptación que ningún documento prueba, y el contrato exige acta firmada por el gerente para facturar.
- **Qué cubre la factura:** FV-1110 no dice a qué entregable corresponde. Su valor equivale a uno de los tres, no a la suma.
- **Compromisos vencidos:** no hay ninguno a nombre del proveedor. El 2026-10-17 se comentó que podría no llegar con el equipo completo a la siguiente fase, y nadie lo registró como riesgo.
- **Sin dato:** el contrato no trae vigencia, renovación ni preaviso. No pude evaluar si un preaviso vence antes del cierre del proyecto (2026-11-28). Tampoco hay fecha ni firmante de la aceptación de Calibración de sensores.

El cruce más delicado es la factura contra la aceptación sin acta; propongo llevarlo a comité junto con los dos vencimientos.

La corrida quedó registrada como `2026-10-17-vendor-tracking-1` (40 segundos, caso PRY-211). La salida completa está en `/home/claude/banco/ronda-9/mineria/espacio/estado/corridas/salida-vendor-tracking.md`.