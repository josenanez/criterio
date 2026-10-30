# /criterio-treasury:treasury-scan 

Términos vigentes (versión 1.3). Inventario: 65 archivos, sin nuevos, cambiados ni borrados. Periodo procesado: 2026-09.

El motor no tuvo que aceptar términos ni pedir nada nuevo. Los términos ya estaban aceptados desde la versión 1.0.0, así que no registré ninguna aceptación nueva. Eso no coincide con tu instrucción de registrar a José Francisco Ñáñez como quien acepta. Si querías un comprobante nuevo para esta versión, hay que correr `/criterio-treasury:treasury-setup`.

# Qué cambió en la tesorería · Banco Istmeño · periodo 2026-09

**Entidad:** Banco Istmeño (155731001-2-2016) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.0.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 24,000.00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 24,000.00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.csv` fila 4 |
| 2 | El saldo de una cuenta o de la caja consolidada queda por debajo del mínimo que fija la política (`cash_below_minimum`) | andino-7301: saldo 1,845.40 USD, bajo el mínimo de 4,214.48 | 2,369.08 | — | — | `2026-09/20-bancos/andino-7301/extracto.pdf` fila 17 · `00-referencia/politica-tesoreria.csv` fila 2 |
| 3 | Un indicador de un contrato de deuda, calculado desde el balance que cierra Clara, cruza su límite o queda a menos del margen de él (`covenant_at_risk`) | Crédito de tesorería · Razón corriente: 2.97 contra el límite >= 2.82 (en riesgo), desde el balance de 2026-09 | — | — | — | `00-referencia/covenants.xlsx` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.xlsx`
- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/andino-7301/extracto.pdf`
- `2026-09/60-tesoreria/programa-pagos.csv`

La sección "El resultado" salió vacía en el reporte del motor. La dejé tal cual, sin rellenarla.

La salida quedó en `estado-finanzas/155731001-2-2016-banco-istmeno/corridas/salida-treasury-scan.md`. La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos.