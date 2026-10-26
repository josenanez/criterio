# /criterio-treasury:treasury-scan 

Términos vigentes (versión 1.2). El inventario no trae archivos nuevos, cambiados ni borrados (64 en total). El periodo procesado es 2026-09, y el motor marcó dos señales.

# Qué cambió en la tesorería · Banco Ribera · periodo 2026-09

**Entidad:** Banco Ribera (20710000019) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.9.0 · **Aprueba:** Sofía León · **Comando:** `treasury-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien aprueba un pago no tiene la facultad según la matriz de firmas, o no está en ella (`signatory_without_authority`) | pago P-3 por 48,000.00: lo aprobó Carlos Paz, que no está en la matriz de firmas | 48,000.00 | Carlos Paz | — | `2026-09/60-tesoreria/programa-pagos.csv` fila 4 |
| 2 | Una obligación de deuda o una inversión vence dentro de los días configurados (`maturity_near`) | Crédito de tesorería (deuda, Banco del Norte) vence el 2026-10-26, en 20 días | 1,600,000.00 | — | 20 | `00-referencia/registro-deuda.xlsx` fila 2 |

## El resultado

(El reporte del motor deja esta sección vacía.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/registro-deuda.xlsx`
- `2026-09/60-tesoreria/programa-pagos.csv`

La corrida quedó registrada como `2026-10-06-treasury-scan-1`, con 2 hallazgos. La salida está en `estado-finanzas/20710000019-banco-ribera/corridas/salida-treasury-scan.md`.

Notas sobre la ejecución:
- No hizo falta registrar la aceptación de términos con el nombre de José Francisco Ñáñez. El motor ya los daba por vigentes (aceptada en 0.9.0), así que no lo hice y `/criterio-treasury:treasury-setup` no corrió.
- En el archivo guardé la línea de apertura sin cambios y en "El resultado" puse una nota entre paréntesis, que no viene del motor. Esa sección salió vacía.