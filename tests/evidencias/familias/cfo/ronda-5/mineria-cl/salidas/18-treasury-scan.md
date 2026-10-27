# /criterio-treasury:treasury-scan 

# Qué cambió en la tesorería · Minera Atacama Norte · periodo 2026-09

**Entidad:** Minera Atacama Norte (76089001-4) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 7.200.000,00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 7.200.000,00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.csv` fila 4 |
| 2 | El saldo de una cuenta o de la caja consolidada queda por debajo del mínimo que fija la política (`cash_below_minimum`) | andino-8901: saldo 8.732.100,00 CLP, bajo el mínimo de 11.078.520,00 | 2.346.420,00 | — | — | `2026-09/20-bancos/andino-8901/extracto.xlsx` fila 17 · `00-referencia/politica-tesoreria.csv` fila 2 |
| 3 | Un indicador de un contrato de deuda, calculado desde el balance que cierra Clara, cruza su límite o queda a menos del margen de él (`covenant_at_risk`) | Crédito de tesorería · Razón corriente: 2.79 contra el límite >= 2.65 (en riesgo), desde el balance de 2026-09 | — | — | — | `00-referencia/covenants.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.csv`
- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/andino-8901/extracto.xlsx`
- `2026-09/60-tesoreria/programa-pagos.csv`

---
Notas de la corrida:
- Los términos (v1.2) ya estaban vigentes y aceptados en la versión 0.10.0, así que no hubo que registrar la aceptación.
- No hubo archivos nuevos, cambiados ni borrados respecto de la corrida anterior (63 archivos).
- Tomé 2026-09 como periodo: es el último del inventario.
- La sección "El resultado" salió vacía en el reporte del motor y la dejé así.
- La salida quedó guardada en `estado-finanzas/76089001-4-minera-atacama-norte/corridas/salida-treasury-scan.md`. La corrida quedó registrada como `2026-10-06-treasury-scan-1` con 3 hallazgos.