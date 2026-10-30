# /criterio-treasury:treasury-scan 

Los términos ya estaban vigentes (versión 1.3, aceptada por la versión 1.1.0 instalada), así que no hizo falta registrar una aceptación nueva. Corrí el escaneo de tesorería de Banco de Occidente Sintético (08010004578120) para 2026-09 con `--today 2026-10-06`. Salieron 3 señales. No hubo archivos nuevos, cambiados ni borrados respecto de la corrida anterior (66 archivos en total).

# Qué cambió en la tesorería · Banco de Occidente Sintético · periodo 2026-09

**Entidad:** Banco de Occidente Sintético (08010004578120) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.1.0 · **Aprueba:** Contralor · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 600,000.00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 600,000.00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.csv` fila 4 |
| 2 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 39,000,000.00 HNL, sobre el límite de 19,500,000.00 | 19,500,000.00 | — | — | `2026-09/20-bancos/pacifico-10902/extracto.pdf` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |
| 3 | Un indicador de un contrato de deuda, calculado desde el balance que cierra Clara, cruza su límite o queda a menos del margen de él (`covenant_at_risk`) | Crédito de tesorería · Razón corriente: 3.02 contra el límite >= 2.87 (en riesgo), desde el balance de 2026-09 | — | — | — | `00-referencia/covenants.csv` fila 2 |

## El resultado

(El motor dejó esta sección vacía, y no agregué cifras que él no dio).

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.csv`
- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/pacifico-10902/extracto.pdf`
- `2026-09/60-tesoreria/programa-pagos.csv`

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. Lo que se mostró está en `estado-finanzas/08010004578120-banco-de-occidente-sintetico/corridas/salida-treasury-scan.md`.