# /criterio-treasury:treasury-scan 

Términos vigentes (versión 1.3). El inventario no trae archivos nuevos, cambiados ni borrados contra la corrida anterior. El motor calculó el periodo 2026-09 y dejó tres señales.

# Qué cambió en la tesorería · Minera del Motagua · periodo 2026-09

**Entidad:** Minera del Motagua (89090314) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.0.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 300,000.00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 300,000.00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.csv` fila 4 |
| 2 | El saldo de una cuenta o de la caja consolidada queda por debajo del mínimo que fija la política (`cash_below_minimum`) | andino-8901: saldo 347,200.00 GTQ, bajo el mínimo de 441,640.00 | 94,440.00 | — | — | `2026-09/20-bancos/andino-8901/extracto.pdf` fila 17 · `00-referencia/politica-tesoreria.csv` fila 2 |
| 3 | Un indicador de un contrato de deuda, calculado desde el balance que cierra Clara, cruza su límite o queda a menos del margen de él (`covenant_at_risk`) | Crédito de tesorería · Razón corriente: 3.39 contra el límite >= 3.22 (en riesgo), desde el balance de 2026-09 | — | — | — | `00-referencia/covenants.csv` fila 2 |

## El resultado

(El motor dejó esta sección vacía en el reporte).

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.csv`
- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/andino-8901/extracto.pdf`
- `2026-09/60-tesoreria/programa-pagos.csv`

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. Lo que te mostré está en `estado-finanzas/89090314-minera-del-motagua/corridas/salida-treasury-scan.md`.

Sobre el procedimiento:
- **Fecha de corte:** tomé 2026-09 como periodo porque es el último con documentos y la fecha de la prueba es 2026-10-06.
- **Registro de aceptación:** los términos ya estaban vigentes, así que no registré ninguna aceptación nueva a nombre de José Francisco Ñáñez. El motor muestra que quedó aceptada la versión 1.0.0 del plugin.
- **Sección vacía:** en el reporte del motor, «El resultado» salió sin contenido. Lo dejé tal cual y no le agregué cifras.
- **Archivo guardado:** al guardar la salida, quité del texto «tal cual» las palabras «(El motor dejó esta sección vacía en el reporte)» que aquí añadí.