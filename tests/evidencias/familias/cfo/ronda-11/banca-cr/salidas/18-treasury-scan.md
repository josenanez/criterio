# /criterio-treasury:treasury-scan 

Corrida de 2026-09 con fecha de prueba 2026-10-06. Los términos (versión 1.3) ya estaban vigentes, así que no registré ninguna aceptación nueva. El inventario no trae archivos nuevos ni cambiados (66 en total). Salieron 3 señales, las tres para revisar:

# Qué cambió en la tesorería · Banco del Valle Central (sintético) · periodo 2026-09

**Entidad:** Banco del Valle Central (sintético) (3101457812) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.0.0 · **Aprueba:** Contralor · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 12.000.000,00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 12.000.000,00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.xlsx` fila 4 |
| 2 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 15.150.000.000,00 CRC, sobre el límite de 7.575.000.000,00 | 7.575.000.000,00 | — | — | `2026-09/20-bancos/pacifico-10102/extracto.pdf` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |
| 3 | Un indicador de un contrato de deuda, calculado desde el balance que cierra Clara, cruza su límite o queda a menos del margen de él (`covenant_at_risk`) | Crédito de tesorería · Razón corriente: 3.29 contra el límite >= 3.13 (en riesgo), desde el balance de 2026-09 | — | — | — | `00-referencia/covenants.xlsx` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.xlsx`
- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/pacifico-10102/extracto.pdf`
- `2026-09/60-tesoreria/programa-pagos.xlsx`

La salida quedó en `estado-finanzas/3101457812-banco-del-valle-central-sintetico/corridas/salida-treasury-scan.md`. La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos.