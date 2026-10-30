# /criterio-treasury:treasury-scan 

# Qué cambió en la tesorería · Almacenes del Canal · periodo 2026-09

Los términos de la versión 1.3 estaban vigentes, así que seguí sin pedir `treasury-setup`. El inventario no trae archivos nuevos, cambiados ni borrados (65 en total). Tomé 2026-09 como último periodo con datos.

**Entidad:** Almacenes del Canal (155791002-2-2017) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.0.0 · **Aprueba:** Contralor · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un pago programado no tiene las aprobaciones que pide la política para su monto (`payment_without_approval`) | pago P-4 a Contratista de obra por 45,000.00: 1 de 2 aprobaciones que pide la política | 45,000.00 | — | — | `2026-09/60-tesoreria/programa-pagos.csv` fila 5 · `00-referencia/politica-tesoreria.csv` fila 5 |
| 2 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 600,000.00 | — | 20 | `00-referencia/registro-deuda.csv` fila 2 |
| 3 | El saldo real de una cuenta se aparta de su proyección más del umbral (`cash_vs_forecast`) | pacifico-7902: saldo 45,000.00 contra 58,500.00 proyectado (-23.1) | 13,500.00 | — | — | `2026-09/20-bancos/pacifico-7902/extracto.xlsx` fila 3 · `2026-09/60-tesoreria/flujo-proyectado.xlsx` fila 3 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesoreria.csv`
- `00-referencia/registro-deuda.csv`
- `2026-09/20-bancos/pacifico-7902/extracto.xlsx`
- `2026-09/60-tesoreria/flujo-proyectado.xlsx`
- `2026-09/60-tesoreria/programa-pagos.csv`

---
Dos cosas que no cuadran con lo que pediste:

- **Aceptación de términos:** no la registré. Los términos ya estaban vigentes, así que `terminos` no pidió aceptación. La aceptación que consta es la de la versión 1.0.0.
- **Sección "El resultado":** el motor la dejó vacía y la mostré así, sin rellenarla.

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. La salida está en `<espacio>/estado-finanzas/155791002-2-2017-almacenes-del-canal/corridas/salida-treasury-scan.md`, y el reporte del motor, en `…/tesoreria/2026-09/reporte-treasury-scan.md`.