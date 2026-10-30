# /criterio-treasury:treasury-scan 

Los términos vigentes (v1.3) ya estaban aceptados en la configuración. El comando `terminos` los dio por vigentes con `--today 2026-10-06`, así que no registré una aceptación nueva.

El inventario no encontró archivos nuevos, cambiados ni borrados, y todo lo que llegó se procesó. Corrí el periodo 2026-09, el último con datos.

# Qué cambió en la tesorería · Almacenes del Valle de Sula · periodo 2026-09

**Entidad:** Almacenes del Valle de Sula (08010006129040) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.1.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un pago programado no tiene las aprobaciones que pide la política para su monto (`payment_without_approval`) | pago P-4 a Contratista de obra por 1,200,000.00: 1 de 2 aprobaciones que pide la política | 1,200,000.00 | — | — | `2026-09/60-tesoreria/programa-pagos.xlsx` fila 5 · `00-referencia/politica-tesoreria.csv` fila 5 |
| 2 | El saldo de una cuenta o de la caja consolidada queda por debajo del mínimo que fija la política (`cash_below_minimum`) | andino-11301: saldo 353,400.00 HNL, bajo el mínimo de 464,080.00 | 110,680.00 | — | — | `2026-09/20-bancos/andino-11301/extracto.pdf` fila 17 · `00-referencia/politica-tesoreria.csv` fila 2 |
| 3 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 16,000,000.00 | — | 20 | `00-referencia/registro-deuda.csv` fila 2 |

## El resultado

(El reporte del motor trae esta sección vacía.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesoreria.csv`
- `00-referencia/registro-deuda.csv`
- `2026-09/20-bancos/andino-11301/extracto.pdf`
- `2026-09/60-tesoreria/programa-pagos.xlsx`

Dejé la corrida registrada como `2026-10-06-treasury-scan-1` con 3 hallazgos. La salida mostrada quedó en `estado-finanzas/08010006129040-almacenes-del-valle-de-sula/corridas/salida-treasury-scan.md`.

Al guardar esa salida cambié una cosa: en "El resultado" escribí "(El reporte del motor trae esta sección vacía.)" en lugar de dejarla en blanco. Esa frase no está en la copia guardada, que es el reporte tal cual lo escribió el motor.