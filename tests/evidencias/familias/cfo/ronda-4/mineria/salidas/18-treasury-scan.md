# /criterio-treasury:treasury-scan 

El scan de tesorería de Minera Cóndor para 2026-09 encontró tres señales. Los términos ya estaban vigentes (versión 1.2), así que no registré ninguna aceptación nueva. No hay archivos nuevos, cambiados ni borrados respecto de la corrida anterior, y todo lo que llegó se procesó.

# Qué cambió en la tesorería · Minera Cóndor · periodo 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Pago sin las aprobaciones que pide la política (`payment_without_approval`) | Pago P-4 a Contratista de obra por 60,000.00: tiene 1 de las 2 aprobaciones que pide la política | 60,000.00 | `2026-09/60-tesoreria/programa-pagos.csv` fila 5 · `00-referencia/politica-tesoreria.csv` fila 5 |
| 2 | Saldo real lejos de la proyección (`cash_vs_forecast`) | pacifico-4102: saldo 60,000.00 contra 78,000.00 proyectado (-23.1) | 18,000.00 | `2026-09/20-bancos/pacifico-4102/extracto.xlsx` fila 3 · `2026-09/60-tesoreria/flujo-proyectado.csv` fila 3 |
| 3 | Covenant en riesgo (`covenant_at_risk`) | Crédito de tesorería · Razón corriente: 3.04 contra el límite >= 2.88 (en riesgo), desde el balance de 2026-09 | — | `00-referencia/covenants.csv` fila 2 |

## El resultado

(Sección vacía en el reporte del motor.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.csv`
- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/pacifico-4102/extracto.xlsx`
- `2026-09/60-tesoreria/flujo-proyectado.csv`
- `2026-09/60-tesoreria/programa-pagos.csv`

La salida quedó guardada en `estado-finanzas/0990054321001-minera-condor/corridas/salida-treasury-scan.md`. La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. El reporte del motor está en `estado-finanzas/0990054321001-minera-condor/tesoreria/2026-09/reporte-treasury-scan.md`.