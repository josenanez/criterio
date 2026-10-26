# /criterio-treasury:treasury-scan 

Inventario sin archivos nuevos, cambiados ni borrados frente a la corrida anterior (64 en total). El motor detectó 3 señales en el periodo 2026-09.

# Qué cambió en la tesorería · Banco Ribera · periodo 2026-09

**Entidad:** Banco Ribera (20710000019) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.9.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 48,000.00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 48,000.00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.csv` fila 4 |
| 2 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 1,600,000.00 | — | 20 | `00-referencia/registro-deuda.xlsx` fila 2 |
| 3 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 120,000.00 PEN, sobre el límite de 60,000.00 | 60,000.00 | — | — | `2026-09/20-bancos/pacifico-7102/extracto.csv` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |

## El resultado

(El motor dejó esta sección vacía en el reporte.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesoreria.csv`
- `00-referencia/registro-deuda.xlsx`
- `2026-09/20-bancos/pacifico-7102/extracto.csv`
- `2026-09/60-tesoreria/programa-pagos.csv`

Los términos (versión 1.2) ya estaban vigentes, así que no registré ninguna aceptación nueva a nombre de José Francisco Ñáñez. La corrida quedó registrada como `2026-10-06-treasury-scan-2` con 3 hallazgos.

Una diferencia entre lo que escribí y lo que quedó en el archivo: la línea "(El motor dejó esta sección vacía en el reporte.)" la agregué solo aquí, y `salida-treasury-scan.md` tiene esa sección en blanco, tal como la entregó el motor.