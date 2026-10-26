# /criterio-treasury:treasury-scan 

Los términos (versión 1.2) ya estaban vigentes. El inventario no trae archivos nuevos ni cambiados frente a la corrida anterior (64 en total). El periodo calculado es 2026-09.

# Qué cambió en la tesorería · Banco Ribera · periodo 2026-09

**Entidad:** Banco Ribera (20710000019) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.10.0 · **Aprueba:** Contralor · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 48,000.00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 48,000.00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.csv` fila 4 |
| 2 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 1,600,000.00 | — | 20 | `00-referencia/registro-deuda.xlsx` fila 2 |

## El resultado

(El motor no trae contenido en esta sección.)

## Lo que no se pudo procesar

- `00-referencia/`: la política no trae la tasa de PEN: su exposición no se calcula

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/registro-deuda.xlsx`
- `2026-09/60-tesoreria/programa-pagos.csv`

La corrida quedó registrada como `2026-10-06-treasury-scan-1`. La salida completa está en `estado-finanzas/20710000019-banco-ribera/corridas/salida-treasury-scan.md`.