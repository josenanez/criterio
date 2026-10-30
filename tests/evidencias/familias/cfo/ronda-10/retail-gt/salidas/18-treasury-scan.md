# /criterio-treasury:treasury-scan 

Términos vigentes (versión 1.3), así que no hizo falta registrar una aceptación nueva. El inventario no trae archivos nuevos ni cambiados frente a la corrida anterior. Procesé el periodo 2026-09 con fecha 2026-10-06.

# Qué cambió en la tesorería · Almacenes del Altiplano · periodo 2026-09

**Entidad:** Almacenes del Altiplano (87145200) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.0.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un pago programado no tiene las aprobaciones que pide la política para su monto (`payment_without_approval`) | pago P-4 a Contratista de obra por 360,000.00: 1 de 2 aprobaciones que pide la política | 360,000.00 | — | — | `2026-09/60-tesoreria/programa-pagos.xlsx` fila 5 · `00-referencia/politica-tesoreria.csv` fila 5 |
| 2 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 4,800,000.00 | — | 20 | `00-referencia/registro-deuda.xlsx` fila 2 |
| 3 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 2,772,000.00 GTQ, sobre el límite de 1,386,000.00 | 1,386,000.00 | — | — | `2026-09/20-bancos/pacifico-8702/extracto.xlsx` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |

## El resultado

(El motor dejó esta sección vacía; no agrego cifras que no trae.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesoreria.csv`
- `00-referencia/registro-deuda.xlsx`
- `2026-09/20-bancos/pacifico-8702/extracto.xlsx`
- `2026-09/60-tesoreria/programa-pagos.xlsx`

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. Lo mostrado está en `estado-finanzas/87145200-almacenes-del-altiplano/corridas/salida-treasury-scan.md`. Ahí la sección «El resultado» quedó vacía, igual que en el reporte del motor. Le agregué dos líneas de contexto antes del encabezado y la nota de esa sección solo en esta respuesta, no en el archivo.