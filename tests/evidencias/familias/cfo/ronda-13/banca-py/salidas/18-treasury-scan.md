# /criterio-treasury:treasury-scan 

Términos vigentes (versión 1.3). No hay archivos nuevos ni cambiados desde la corrida anterior. El periodo procesado es 2026-09 y salieron tres señales.

# Qué cambió en la tesorería · Banco del Tebicuary (sintético) · periodo 2026-09

**Entidad:** Banco del Tebicuary (sintético) (88457812-7) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.2.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 180.000.000,00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 180.000.000,00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.xlsx` fila 4 |
| 2 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 3.375.000.000.000,00 PYG, sobre el límite de 1.687.500.000.000,00 | 1.687.500.000.000,00 | — | — | `2026-09/20-bancos/pacifico-13102/extracto.csv` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |
| 3 | Un indicador de un contrato de deuda, calculado desde el balance que cierra Clara, cruza su límite o queda a menos del margen de él (`covenant_at_risk`) | Crédito de tesorería · Razón corriente: 3.07 contra el límite >= 2.92 (en riesgo), desde el balance de 2026-09 | — | — | — | `00-referencia/covenants.xlsx` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.xlsx`
- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/pacifico-13102/extracto.csv`
- `2026-09/60-tesoreria/programa-pagos.xlsx`

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. Lo que se muestra arriba está guardado en `estado-finanzas/88457812-7-banco-del-tebicuary-sintetico/corridas/salida-treasury-scan.md`.

Dos cosas sobre los términos:
- El motor ya los marcó vigentes, con aceptación de la versión 1.2.0 instalada. Por eso no registré una aceptación nueva a nombre de José Francisco Ñáñez.
- Sigo sin saber si la versión de los términos (1.3) coincide con la del plugin instalado (1.2.0).