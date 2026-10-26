# /criterio-treasury:treasury-scan 

Términos vigentes (versión 1.2). El inventario no trae archivos nuevos ni cambiados frente a la corrida anterior. Procesé el periodo 2026-09 y salieron tres señales.

# Qué cambió en la tesorería · Minera Puna Alta · periodo 2026-09

**Entidad:** Minera Puna Alta (20730000015) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El saldo de una cuenta o de la caja consolidada queda por debajo del mínimo que fija la política (`cash_below_minimum`) | andino-7301: saldo 56,802.00 PEN, bajo el mínimo de 74,162.40 | 17,360.40 | — | — | `2026-09/20-bancos/andino-7301/extracto.xlsx` fila 17 · `00-referencia/politica-tesoreria.csv` fila 2 |
| 2 | El saldo real de una cuenta se aparta de su proyección más del umbral (`cash_vs_forecast`) | pacifico-7302: saldo 180,000.00 contra 234,000.00 proyectado (-23.1) | 54,000.00 | — | — | `2026-09/20-bancos/pacifico-7302/extracto.xlsx` fila 3 · `2026-09/60-tesoreria/flujo-proyectado.csv` fila 3 |
| 3 | Un indicador de un contrato de deuda, calculado desde el balance que cierra Clara, cruza su límite o queda a menos del margen de él (`covenant_at_risk`) | Crédito de tesorería · Razón corriente: 2.81 contra el límite >= 2.67 (en riesgo), desde el balance de 2026-09 | — | — | — | `00-referencia/covenants.csv` fila 2 |

## El resultado

(El reporte del motor no trae texto en esta sección.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.csv`
- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/andino-7301/extracto.xlsx`
- `2026-09/20-bancos/pacifico-7302/extracto.xlsx`
- `2026-09/60-tesoreria/flujo-proyectado.csv`

**Lo que no hice:**
- **Registro de los términos:** no registré la aceptación a nombre de José Francisco Ñáñez, porque el comando no la pidió: `terminos` ya devolvió vigente (aceptada en la versión 0.10.0).
- **Archivo de salida:** `estado-finanzas/20730000015-minera-puna-alta/corridas/salida-treasury-scan.md` es una copia del reporte del motor sin la línea aclaratoria de la sección "El resultado". Esa línea la agregué después, solo en esta respuesta.

La corrida quedó registrada como `2026-10-06-treasury-scan-1` con 3 hallazgos. El reporte completo está en `estado-finanzas/20730000015-minera-puna-alta/tesoreria/2026-09/reporte-treasury-scan.md`.