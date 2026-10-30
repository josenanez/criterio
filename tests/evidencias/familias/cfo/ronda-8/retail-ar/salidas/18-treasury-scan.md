# /criterio-treasury:treasury-scan 

Corrí el treasury-scan de Almacenes del Plata (30714520780) para 2026-09. Salieron 3 señales, ninguna con archivos nuevos o cambiados desde la corrida anterior (64 archivos en total).

Los términos (versión 1.3) ya estaban vigentes, así que no registré ninguna aceptación nueva. La fecha de la prueba, 2026-10-06, la pasé al motor en cada llamada. La salida de esta corrida quedó en `estado-finanzas/30714520780-almacenes-del-plata/corridas/salida-treasury-scan.md`. El motor registró la corrida como `2026-10-06-treasury-scan-1`.

# Qué cambió en la tesorería · Almacenes del Plata · periodo 2026-09

**Entidad:** Almacenes del Plata (30714520780) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.0.0 · **Aprueba:** Contralor · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 18.000.000,00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 18.000.000,00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.xlsx` fila 4 |
| 2 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 65.250.000.000,00 ARS, sobre el límite de 32.625.000.000,00 | 32.625.000.000,00 | — | — | `2026-09/20-bancos/pacifico-6102/extracto.xlsx` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |
| 3 | El saldo real de una cuenta se aparta de su proyección más del umbral (`cash_vs_forecast`) | pacifico-6102: saldo 45.000.000,00 contra 58.500.000,00 proyectado (-23,1) | 13.500.000,00 | — | — | `2026-09/20-bancos/pacifico-6102/extracto.xlsx` fila 3 · `2026-09/60-tesoreria/flujo-proyectado.csv` fila 3 |

## El resultado

(El motor dejó esta sección vacía; no le agregué nada.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/pacifico-6102/extracto.xlsx`
- `2026-09/60-tesoreria/flujo-proyectado.csv`
- `2026-09/60-tesoreria/programa-pagos.xlsx`