# /criterio-treasury:treasury-scan 

Corrí `treasury-scan` para el periodo 2026-09 de Banco Valle de Anáhuac (BVA150301K21), con `--today 2026-10-06`. El reporte encontró tres señales, todas por atender.

Los términos (versión 1.2) ya estaban vigentes, aceptados en la versión 0.11.0. Por eso no hizo falta registrar la aceptación de José Francisco Ñáñez. No había preguntas por responder.

El inventario no encontró archivos nuevos ni cambiados respecto de la corrida anterior, y todo lo que llegó se procesó.

El motor dejó en blanco la sección "El resultado" del reporte. La copié tal cual, sin llenarla.

| # | Señal | Qué | Monto |
|---|---|---|---|
| 1 | `payment_without_approval` | El pago P-4 a Contratista de obra tiene 1 de las 2 aprobaciones que pide la política. | 600,000.00 |
| 2 | `fx_exposure_over_limit` | La posición en USD equivale a 11,100,000.00 MXN, sobre el límite de 5,550,000.00. | 5,550,000.00 |
| 3 | `cash_vs_forecast` | En pacifico-1302 el saldo es 600,000.00 contra 780,000.00 proyectado (-23.1). | 180,000.00 |

Las citas de cada señal están en el reporte (programa de pagos, política de tesorería, extracto de pacifico-1302 y flujo proyectado).

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. El reporte completo está en `estado-finanzas/BVA150301K21-banco-valle-de-anahuac/tesoreria/2026-09/reporte-treasury-scan.md`. Lo que te mostré lo guardé en `estado-finanzas/BVA150301K21-banco-valle-de-anahuac/corridas/salida-treasury-scan.md`.