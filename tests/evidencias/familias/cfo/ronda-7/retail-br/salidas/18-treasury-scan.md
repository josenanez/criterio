# /criterio-treasury:treasury-scan 

El scan de tesorería de Lojas Paulistas del periodo 2026-09 dio 3 señales. No hay archivos nuevos ni cambiados desde la corrida anterior (65 archivos en el inventario), y todo lo que llegó se procesó.

Los términos (versión 1.3) ya estaban vigentes y aceptados, así que no hizo falta registrar la aceptación. El motor solo marca aceptada la versión instalada, 0.12.1. No hay registro de la aceptación de José Francisco Ñáñez.

# Qué cambió en la tesorería · Lojas Paulistas · periodo 2026-09

**Entidad:** Lojas Paulistas (31452078000170) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.12.1 · **Aprueba:** Sofia Leão · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un pago programado no tiene las aprobaciones que pide la política para su monto (`payment_without_approval`) | pago P-4 a Empreiteira por 150.000,00: 1 de 2 aprobaciones que pide la política | 150.000,00 | — | — | `2026-09/60-tesoreria/programa-pagamentos.xlsx` fila 5 · `00-referencia/politica-tesouraria.csv` fila 5 |
| 2 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Capital de giro (divida, Banco Bandeirante) vence el 2026-10-26, en 20 días | 2.000.000,00 | — | 20 | `00-referencia/registro-divida.xlsx` fila 2 |
| 3 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 810.000,00 BRL, sobre el límite de 405.000,00 | 405.000,00 | — | — | `2026-09/20-bancos/litoral-2902/extrato.csv` fila 3 · `00-referencia/politica-tesouraria.csv` fila 7 |

## El resultado

(El motor dejó esta sección vacía.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesouraria.csv`
- `00-referencia/registro-divida.xlsx`
- `2026-09/20-bancos/litoral-2902/extrato.csv`
- `2026-09/60-tesoreria/programa-pagamentos.xlsx`

La salida quedó en `corridas/salida-treasury-scan.md` y la corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. El archivo guardado lleva una línea de resumen antes del encabezado. En la salida guardada puse "(El motor dejó esta sección vacía.)" y no la dejé en blanco.