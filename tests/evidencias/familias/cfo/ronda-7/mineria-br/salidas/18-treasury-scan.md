# /criterio-treasury:treasury-scan 

Los términos (versión 1.3) ya estaban vigentes. El inventario no trae archivos nuevos ni cambiados respecto de la corrida anterior, y salieron 3 señales en el periodo 2026-09.

# Qué cambió en la tesorería · Mineração Serra Azul · periodo 2026-09

**Entidad:** Mineração Serra Azul (28903114000160) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.12.1 · **Aprueba:** Sofia Leão · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 120.000,00: lo aprobó Carlos Peixoto, que no está en la matriz de firmas | 120.000,00 | Carlos Peixoto | — | `2026-09/60-tesoreria/programa-pagamentos.xlsx` fila 4 |
| 2 | El saldo de una cuenta o de la caja consolidada queda por debajo del mínimo que fija la política (`cash_below_minimum`) | bandeirante-3101: saldo 169.841,48 BRL, bajo el mínimo de 213.809,78 | 43.968,30 | — | — | `2026-09/20-bancos/bandeirante-3101/extrato.csv` fila 17 · `00-referencia/politica-tesouraria.csv` fila 2 |
| 3 | Un indicador de un contrato de deuda, calculado desde el balance que cierra Clara, cruza su límite o queda a menos del margen de él (`covenant_at_risk`) | Capital de giro · Liquidez corrente: 2.92 contra el límite >= 2.77 (en riesgo), desde el balance de 2026-09 | — | — | — | `00-referencia/covenants.xlsx` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/covenants.xlsx`
- `00-referencia/politica-tesouraria.csv`
- `2026-09/20-bancos/bandeirante-3101/extrato.csv`
- `2026-09/60-tesoreria/programa-pagamentos.xlsx`

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 3 hallazgos. El texto de arriba está guardado en `corridas/salida-treasury-scan.md`.

Dos notas sobre la prueba:
- Elegí 2026-09 como periodo porque es el último con carpeta en el inventario.
- La sección "El resultado" salió vacía en el reporte del motor. La mostré tal cual y no agregué nada.