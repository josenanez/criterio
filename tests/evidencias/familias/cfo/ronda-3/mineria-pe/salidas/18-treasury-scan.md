# /criterio-treasury:treasury-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior (63 en total). Procesé el periodo 2026-09 y salieron tres señales.

# Qué cambió en la tesorería · Minera Puna Alta · periodo 2026-09

**Entidad:** Minera Puna Alta (20730000015) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.9.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | `cash_below_minimum` | andino-7301: saldo 56,802.00 PEN, bajo el mínimo de 74,162.40 | 17,360.40 | `2026-09/20-bancos/andino-7301/extracto.xlsx` fila 17 · `00-referencia/politica-tesoreria.csv` fila 2 |
| 2 | `cash_vs_forecast` | pacifico-7302: saldo 180,000.00 contra 234,000.00 proyectado (-23.1) | 54,000.00 | `2026-09/20-bancos/pacifico-7302/extracto.xlsx` fila 3 · `2026-09/60-tesoreria/flujo-proyectado.csv` fila 3 |
| 3 | `covenant_at_risk` | Crédito de tesorería · Razón corriente: 2.81 contra el límite >= 2.67 (en riesgo), desde el balance de 2026-09 | — | `00-referencia/covenants.csv` fila 2 |

En las tres señales, responsable y días quedan sin dato.

## Lo que no se pudo procesar
Todo lo que llegó se procesó.

## Las preguntas que hizo
Ninguna en esta corrida. Nadie tenía que responder nada.

## Fuentes
- `00-referencia/covenants.csv`
- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/andino-7301/extracto.xlsx`
- `2026-09/20-bancos/pacifico-7302/extracto.xlsx`
- `2026-09/60-tesoreria/flujo-proyectado.csv`

La salida quedó en `estado-finanzas/20730000015-minera-puna-alta/corridas/salida-treasury-scan.md`. La corrida quedó registrada como `2026-10-06-treasury-scan-1` con 3 hallazgos.

Los términos (versión 1.2) ya estaban vigentes, aceptados con la versión 0.9.0, así que no registré ninguna aceptación nueva a nombre de José Francisco Ñáñez.