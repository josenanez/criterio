# /criterio-treasury:treasury-scan 

# Qué cambió en la tesorería · Tiendas del Bajío · periodo 2026-09

**Entidad:** Tiendas del Bajío (TBA180912Q37) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.11.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 180,000.00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 180,000.00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.csv` fila 4 |
| 2 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 6,000,000.00 | — | 20 | `00-referencia/registro-deuda.csv` fila 2 |
| 3 | Un indicador de un contrato de deuda, calculado desde el balance que cierra Clara, cruza su límite o queda a menos del margen de él (`covenant_at_risk`) | Crédito de tesorería · Razón corriente: 3.23 contra el límite >= 3.06 (en riesgo), desde el balance de 2026-09 | — | — | — | `00-referencia/covenants.xlsx` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.xlsx`
- `00-referencia/registro-deuda.csv`
- `2026-09/60-tesoreria/programa-pagos.csv`

---
Notas de la corrida:
- Los términos (versión 1.2) ya estaban vigentes con la aceptación registrada en 0.11.0. No hizo falta registrar una aceptación nueva.
- El inventario no encontró archivos nuevos, cambiados ni borrados (65 en total).
- La sección «El resultado» salió vacía en el reporte del motor. No agregué nada.
- La corrida quedó registrada como `2026-10-06-treasury-scan-1` con 3 hallazgos. La salida está en `estado-finanzas/TBA180912Q37-tiendas-del-bajio/corridas/salida-treasury-scan.md`.