# /criterio-treasury:treasury-scan 

Corrí `treasury-scan` para el periodo 2026-09 de Minera Cordillera de Cuyo, y salieron tres señales. No hay archivos nuevos ni cambiados frente a la corrida anterior, y todo lo que llegó se procesó.

Los términos ya estaban vigentes (versión 1.3), así que no hubo nada que registrar. Dejé la aceptación de José Francisco Ñáñez como está, porque el motor no la pidió.

Este es el reporte tal como lo escribió el motor:

# Qué cambió en la tesorería · Minera Cordillera de Cuyo · periodo 2026-09

**Entidad:** Minera Cordillera de Cuyo (30709031143) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.0.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un pago programado no tiene las aprobaciones que pide la política para su monto (`payment_without_approval`) | pago P-4 a Contratista de obra por 90.000.000,00: 1 de 2 aprobaciones que pide la política | 90.000.000,00 | — | — | `2026-09/60-tesoreria/programa-pagos.csv` fila 5 · `00-referencia/politica-tesoreria.csv` fila 5 |
| 2 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 1.200.000.000,00 | — | 20 | `00-referencia/registro-deuda.xlsx` fila 2 |
| 3 | Un indicador de un contrato de deuda, calculado desde el balance que cierra Clara, cruza su límite o queda a menos del margen de él (`covenant_at_risk`) | Crédito de tesorería · Razón corriente: 2.99 contra el límite >= 2.84 (en riesgo), desde el balance de 2026-09 | — | — | — | `00-referencia/covenants.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.csv`
- `00-referencia/politica-tesoreria.csv`
- `00-referencia/registro-deuda.xlsx`
- `2026-09/60-tesoreria/programa-pagos.csv`

La sección "El resultado" salió vacía en el reporte del motor. No agregué nada en su lugar.

La salida quedó en `estado-finanzas/30709031143-minera-cordillera-de-cuyo/corridas/salida-treasury-scan.md`. La corrida quedó registrada como `2026-10-06-treasury-scan-1` con 3 hallazgos.