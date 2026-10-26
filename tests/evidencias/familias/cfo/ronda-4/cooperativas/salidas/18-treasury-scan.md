# /criterio-treasury:treasury-scan 

Los términos (versión 1.2) estaban vigentes con la aceptación ya registrada, así que no hubo que registrar nada. El periodo es 2026-09, el último con documentos, con fecha de prueba 2026-10-06.

Desde la corrida anterior no hay archivos nuevos, cambiados ni borrados (59 en total). La corrida arrojó 3 señales y un archivo que falta:

# Qué cambió en la tesorería · Cooperativa Sierra Alta · periodo 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 12,000.00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 12,000.00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.xlsx` fila 4 |
| 2 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 400,000.00 | — | 20 | `00-referencia/registro-deuda.csv` fila 2 |
| 3 | El saldo real de una cuenta se aparta de su proyección más del umbral (`cash_vs_forecast`) | andino-2301: saldo 6,560.00 contra 8,528.00 proyectado (-23.1) | 1,968.00 | — | — | `2026-09/20-bancos/andino-2301/extracto.pdf` fila 17 · `2026-09/60-tesoreria/flujo-proyectado.xlsx` fila 2 |

## El resultado

(El motor dejó esta sección vacía.)

## Lo que no se pudo procesar

- `2026-09/20-bancos/pacifico-2302`: no está el extracto

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/registro-deuda.csv`
- `2026-09/20-bancos/andino-2301/extracto.pdf`
- `2026-09/60-tesoreria/flujo-proyectado.xlsx`
- `2026-09/60-tesoreria/programa-pagos.xlsx`

La corrida quedó registrada como `2026-10-06-treasury-scan-1` con 3 hallazgos. Lo que se mostró está guardado en `estado-finanzas/1790012345001-cooperativa-sierra-alta/corridas/salida-treasury-scan.md`.