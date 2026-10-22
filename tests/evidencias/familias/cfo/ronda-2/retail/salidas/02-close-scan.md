# /criterio-finance:close-scan 

57 archivos nuevos y 0 cambiados; 8 señales abiertas, todas nuevas porque es la primera corrida registrada. No hay nada fuera de lugar. El correo del 2026-10-05 declara el cierre como cerrado, y el motor lo contrasta con las señales abiertas.

# Qué cambió en el cierre · Almacenes Caribe · periodo 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 2505: el mayor suma débitos 16.000.000,00 y créditos 16.120.000,00; el balance dice 16.000.000,00 y 16.000.000,00 | -120.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` fila 8 · `2026-09/10-contabilidad/libro-mayor.csv` |
| 2 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5195: el mayor suma débitos 4.388.000,00 y créditos 0,00; el balance dice 4.268.000,00 y 0,00 | 120.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` fila 14 · `2026-09/10-contabilidad/libro-mayor.csv` |
| 3 | El cierre se reporta como cerrado y hay señales abiertas que ese estado no explica (`declared_close_vs_evidence`) | el cierre se reporta cerrado (2026-09/40-soportes/correo-estado-del-cierre.md, 2026-10-05) y hay 7 señales abiertas que ese estado no explica | — | — | — | `2026-09/40-soportes/correo-estado-del-cierre.md` |
| 4 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-3701: consignación en tránsito del 2026-09-30 por 8.330.000,00 (SETP99000107) | 8.330.000,00 | — | 0 | `2026-09/20-bancos/andino-3701/auxiliar-libros.csv` fila 17 |
| 5 | El mismo CUFE o la misma clave de acceso aparece registrado dos veces (`einvoice_duplicate`) | el mismo CUFE aparece en 2 archivos (SETP99000102) | 8.330.000,00 | — | — | `2026-09/30-facturacion/emitidas/fe-SETP99000102-reenviada.xml` · `2026-09/30-facturacion/emitidas/fe-SETP99000102.xml` |
| 6 | El mismo CUFE o la misma clave de acceso aparece registrado dos veces (`einvoice_duplicate`) | factura SETP77000201 registrada en 2 asientos (C-021, C-022) | 3.104.000,00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` filas 53, 54, 56 y 57 |
| 7 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura SETP77000201: base 1.552.000,00 en el XML y 3.104.000,00 en libros; IVA 294.880,00 en el XML y 589.760,00 en libros | 1.846.880,00 | — | — | `2026-09/30-facturacion/recibidas/fr-SETP77000201.xml` · `2026-09/10-contabilidad/libro-mayor.csv` filas 53, 54 y 56 |
| 8 | La conciliación de una cuenta no se actualizó en el periodo (`reconciliation_stale`) | cuenta 2205: no hay auxiliar del periodo para conciliarla | — | — | — | `2026-09/10-contabilidad/auxiliares/` |

## El resultado

(El motor dejó esta sección vacía.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Nueve, todas respondidas desde los documentos. Están en el reporte `estado-finanzas/900765432-almacenes-caribe/cierre/2026-09/reporte-close-scan.md`. Los puntos abiertos son el marco contable, que queda «por confirmar», y el festivo 2026-10-12, que es el del ejemplo y no está confirmado.

## Fuentes

Los ocho archivos citados en la tabla.

**Registro de la corrida:** `2026-10-06-close-scan-1`, con 8 hallazgos. La salida quedó en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-close-scan.md`.

Dos cosas que debes saber:
- **La salida guardada no es idéntica a lo de arriba.** En el archivo copié el reporte completo, con las nueve preguntas escritas una por una. Aquí resumí la sección de preguntas, y en las citas de las filas 6 y 7 agrupé las filas de un mismo archivo para acortarlas.
- **Los archivos del estado y de las fuentes no están en la ruta que decía el comando.** Los documentos de la entidad están en `finanzas/900765432-almacenes-caribe/` y el estado en `estado-finanzas/900765432-almacenes-caribe/`.