# /criterio-treasury:treasury-scan 

Términos vigentes (versión 1.2). El inventario no trae archivos nuevos, cambiados ni borrados frente a la corrida anterior. El periodo procesado es 2026-09. Hay dos señales nuevas.

# Qué cambió en la tesorería · Almacenes Caribe · periodo 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 320.000.000,00 | — | 20 | `00-referencia/registro-deuda.csv` fila 2 |
| 2 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 24.000.000,00 COP, sobre el límite de 12.000.000,00 | 12.000.000,00 | — | — | `2026-09/20-bancos/pacifico-3702/extracto.xlsx` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |

## El resultado

(El motor dejó esta sección vacía en el reporte.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesoreria.csv`
- `00-referencia/registro-deuda.csv`
- `2026-09/20-bancos/pacifico-3702/extracto.xlsx`

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 2 hallazgos. El reporte está en `estado-finanzas/900765432-almacenes-caribe/tesoreria/2026-09/reporte-treasury-scan.md`.

Dos aclaraciones sobre cómo corrí esto:
- **Términos:** estaban vigentes, así que no hizo falta registrar la aceptación de José Francisco Ñáñez.
- **Archivo de la corrida:** en `salida-treasury-scan.md` quedó el reporte del motor tal cual. Le añadí al inicio las dos líneas de contexto de arriba, sin cifras. La nota "(El motor dejó esta sección vacía…)" la agregué solo en esta respuesta; no está en el archivo.