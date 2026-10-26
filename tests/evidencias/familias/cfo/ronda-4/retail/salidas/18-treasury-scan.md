# /criterio-treasury:treasury-scan 

Corrida del periodo 2026-09, con los términos vigentes y sin archivos nuevos ni cambiados desde la corrida anterior. El motor encontró dos señales, y la sección "El resultado" del reporte salió vacía.

# Qué cambió en la tesorería · Almacenes Caribe · periodo 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 96.000.000.000,00 COP, sobre el límite de 48.000.000.000,00 | 48.000.000.000,00 | — | — | `2026-09/20-bancos/pacifico-3702/extracto.xlsx` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |
| 2 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 320.000.000,00 | — | 20 | `00-referencia/registro-deuda.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesoreria.csv`
- `00-referencia/registro-deuda.csv`
- `2026-09/20-bancos/pacifico-3702/extracto.xlsx`

La salida quedó en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-treasury-scan.md`. La corrida quedó registrada como `2026-10-06-treasury-scan-2` con 2 hallazgos.

Sobre los términos: el motor los dio por vigentes, con la aceptación de la versión 0.10.0. Por eso no hizo falta registrar de nuevo la aceptación de José Francisco Ñáñez, y no lo hice.