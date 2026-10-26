# /criterio-treasury:treasury-scan 

Los términos de la versión 0.9.0 ya estaban vigentes, así que no hizo falta registrar una aceptación nueva. El inventario no trae archivos nuevos, cambiados ni borrados frente a la corrida anterior. El cálculo del periodo 2026-09 dio tres señales.

# Qué cambió en la tesorería · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.9.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un pago programado no tiene las aprobaciones que pide la política para su monto (`payment_without_approval`) | pago P-4 a Contratista de obra por 30.000.000,00: 1 de 2 aprobaciones que pide la política | 30.000.000,00 | — | — | `2026-09/60-tesoreria/programa-pagos.xlsx` fila 5 · `00-referencia/politica-tesoreria.csv` fila 5 |
| 2 | El saldo de una cuenta o de la caja consolidada queda por debajo del mínimo que fija la política (`cash_below_minimum`) | andino-1101: saldo 13.273.400,00 COP, bajo el mínimo de 16.928.080,00 | 3.654.680,00 | — | — | `2026-09/20-bancos/andino-1101/extracto.xlsx` fila 17 · `00-referencia/politica-tesoreria.csv` fila 2 |
| 3 | Un indicador de un contrato de deuda, calculado desde el balance que cierra Clara, cruza su límite o queda a menos del margen de él (`covenant_at_risk`) | Crédito de tesorería · Razón corriente: 3.07 contra el límite >= 2.92 (en riesgo), desde el balance de 2026-09 | — | — | — | `00-referencia/covenants.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.csv`
- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/andino-1101/extracto.xlsx`
- `2026-09/60-tesoreria/programa-pagos.xlsx`

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. Lo que te mostré está guardado en `estado-finanzas/900123456-banco-andino/corridas/salida-treasury-scan.md`.