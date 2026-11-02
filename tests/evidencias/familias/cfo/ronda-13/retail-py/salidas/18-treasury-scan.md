# /criterio-treasury:treasury-scan 

Los términos (versión 1.3) ya estaban vigentes con una aceptación anterior, así que no hizo falta registrar otra. No hubo archivos nuevos ni cambiados (65 en total). Tomé 2026-09 como periodo porque es el último del inventario.

# Qué cambió en la tesorería · Distribuidora del Ybytyruzú (sintética) · periodo 2026-09

**Entidad:** Distribuidora del Ybytyruzú (sintética) (88612904-4) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.2.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un pago programado no tiene las aprobaciones que pide la política para su monto (`payment_without_approval`) | pago P-4 a Contratista de obra por 300.000.000,00: 1 de 2 aprobaciones que pide la política | 300.000.000,00 | — | — | `2026-09/60-tesoreria/programa-pagos.xlsx` fila 5 · `00-referencia/politica-tesoreria.csv` fila 5 |
| 2 | El saldo de una cuenta o de la caja consolidada queda por debajo del mínimo que fija la política (`cash_below_minimum`) | andino-13701: saldo 79.900.000,00 PYG, bajo el mínimo de 105.880.000,00 | 25.980.000,00 | — | — | `2026-09/20-bancos/andino-13701/extracto.pdf` fila 16 · `00-referencia/politica-tesoreria.csv` fila 2 |
| 3 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 4.000.000.000,00 | — | 20 | `00-referencia/registro-deuda.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesoreria.csv`
- `00-referencia/registro-deuda.csv`
- `2026-09/20-bancos/andino-13701/extracto.pdf`
- `2026-09/60-tesoreria/programa-pagos.xlsx`

La sección «El resultado» salió vacía en el reporte del motor y la dejé así, sin completarla.

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. Lo mostrado está guardado en `estado-finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica/corridas/salida-treasury-scan.md`.