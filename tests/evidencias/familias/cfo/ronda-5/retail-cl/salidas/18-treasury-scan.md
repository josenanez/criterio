# /criterio-treasury:treasury-scan 

Los términos (versión 1.2) ya estaban vigentes y aceptados, así que no hizo falta registrar la aceptación. El inventario tiene 66 archivos, sin nuevos, cambiados, borrados ni ilegibles. Procesé el periodo 2026-09, el último disponible.

# Qué cambió en la tesorería · Tiendas Pacífico · periodo 2026-09

**Entidad:** Tiendas Pacífico (76083001-1) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.10.0 · **Aprueba:** Contralor · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un pago programado no tiene las aprobaciones que pide la política para su monto (`payment_without_approval`) | pago P-4 a Contratista de obra por 7.500.000,00: 1 de 2 aprobaciones que pide la política | 7.500.000,00 | — | — | `2026-09/60-tesoreria/programa-pagos.csv` fila 5 · `00-referencia/politica-tesoreria.csv` fila 5 |
| 2 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 7.125.000.000,00 CLP, sobre el límite de 3.562.500.000,00 | 3.562.500.000,00 | — | — | `2026-09/20-bancos/pacifico-8302/extracto.pdf` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |
| 3 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 100.000.000,00 | — | 20 | `00-referencia/registro-deuda.csv` fila 2 |

## El resultado

(El motor dejó esta sección vacía.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesoreria.csv`
- `00-referencia/registro-deuda.csv`
- `2026-09/20-bancos/pacifico-8302/extracto.pdf`
- `2026-09/60-tesoreria/programa-pagos.csv`

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. Lo mostrado está guardado en `estado-finanzas/76083001-1-tiendas-pacifico/corridas/salida-treasury-scan.md`.