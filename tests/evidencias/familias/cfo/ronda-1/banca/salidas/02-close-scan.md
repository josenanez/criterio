# /criterio-finance:close-scan 

Inventario: 57 archivos nuevos, 0 cambiados y 0 borrados. Es la primera corrida de close-scan, así que las 8 señales del periodo son las que el motor calculó ahora. La declaración del cierre (correo de Sofía León, 2026-10-05) dice "en curso". No hay requerimientos del auditor fuera de la tabla.

# Qué cambió en el cierre · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.7.0 · **Aprueba:** Sofía León

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Saldo del mayor distinto al del balance (`ledger_vs_trial_balance`) | Cuenta 5305: el mayor suma débitos 0,00 y créditos 0,00; el balance dice 5.000,00 y 0,00 | -5.000,00 | — | — | `balance-comprobacion.csv` fila 15 · `libro-mayor.csv` |
| 2 | Saldo del mayor distinto al del balance (`ledger_vs_trial_balance`) | Cuenta 5305: saldo inicial más movimientos no da el saldo final (5.000,00) | 5.000,00 | — | — | `balance-comprobacion.csv` fila 15 |
| 3 | Débitos y créditos del balance no suman lo mismo (`trial_balance_unbalanced`) | Débitos 253.437.700,00 y créditos 253.432.700,00: diferencia 5.000,00 | 5.000,00 | — | — | `balance-comprobacion.csv` |
| 4 | Tarea cumplida sin soporte (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte en `2026-09/40-soportes/` que empiece por C-02 | — | Andrés Paz | — | `00-referencia/checklist-cierre.csv` fila 3 |
| 5 | Extracto y registros sin cruzar (`bank_unreconciled`) | andino-1101: cheque pendiente de cobro del 2026-07-20 por -3.000.000,00 (CH-0450) | -3.000.000,00 | — | 72 | `andino-1101/auxiliar-libros.csv` fila 2 |
| 6 | Extracto y registros sin cruzar (`bank_unreconciled`) | andino-1101: nota débito sin registrar del 2026-09-30 por -400.000,00 (sin referencia) | -400.000,00 | — | 0 | `andino-1101/extracto.csv` fila 17 |
| 7 | Valor o impuesto del XML distinto al del registro (`einvoice_amount_mismatch`) | Factura SETP99000104: IVA 1.662.500,00 en el XML y 1.663.500,00 en libros | 1.000,00 | — | — | `fe-SETP99000104.xml` · `libro-mayor.csv` filas 15 y 16 |
| 8 | Partida conciliatoria con más días de los configurados (`reconciling_item_aged`) | andino-1101: cheque pendiente de cobro lleva 72 días (CH-0450) | -3.000.000,00 | — | 72 | `andino-1101/auxiliar-libros.csv` fila 2 |

## El resultado

(El motor no trajo contenido en esta sección.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Las 10 preguntas y sus respuestas están en el reporte completo, en `estado-finanzas/900123456-banco-andino/cierre/2026-09/reporte-close-scan.md`. Las más relevantes:
- Aprueba el cierre Sofía León (responsable de C-09); el festivo es 2026-10-12.
- El checklist es el de la organización y queda como no aprobado, porque no hay aprobación documentada.
- Términos v1.2 aceptados por José Francisco Ñáñez el 2026-10-06, según el encargo de la prueba.

## Fuentes

Seis archivos: `checklist-cierre.csv`, `balance-comprobacion.csv`, `libro-mayor.csv`, `auxiliar-libros.csv` y `extracto.csv` de andino-1101, y `fe-SETP99000104.xml`.

La corrida quedó registrada como `2026-10-06-close-scan-1`, con 8 hallazgos. La salida completa está en `estado-finanzas/900123456-banco-andino/corridas/salida-close-scan.md`.

Resumí en este mensaje las secciones "Las preguntas que hizo" y "Fuentes". El archivo guardado en `corridas` tiene el reporte completo, con las 10 preguntas y las fuentes en lista.