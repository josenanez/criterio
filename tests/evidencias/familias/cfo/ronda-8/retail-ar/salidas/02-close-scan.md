# /criterio-finance:close-scan 

Inventario: 64 archivos nuevos y 0 cambiados. Hay 6 señales abiertas y ninguna es nueva: son las mismas que dejó la corrida de `finance-setup`. Los términos 1.3 ya estaban aceptados por José Francisco Ñáñez el 2026-10-06. Convertí a texto los 4 documentos de `50-auditoria` y los 5 de `40-soportes`. La ficha ya traía el estado declarado: cerrado, según Sofía León el 2026-10-05.

# Qué cambió en el cierre · Almacenes del Plata · periodo 2026-09

**Entidad:** Almacenes del Plata (30714520780) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.0.0 · **Aprueba:** Contralor · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una tarea figura cumplida y ningún documento la sostiene (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte en 2026-09/40-soportes/ que empiece por C-02 | — | Andrés Paz | — | `00-referencia/checklist-cierre.xlsx` fila 3 |
| 2 | El cierre se reporta como cerrado y hay señales abiertas que ese estado no explica (`declared_close_vs_evidence`) | el cierre se reporta cerrado (2026-09/40-soportes/correo-estado-del-cierre.md, 2026-10-05) y hay 5 señales abiertas que ese estado no explica | — | — | — | `2026-09/40-soportes/correo-estado-del-cierre.md` |
| 3 | Un registro que la necesita no tiene factura electrónica que lo soporte (`recorded_without_einvoice`) | documento 00002-00000202 en las cuentas de compras por 5.092.500,00 sin factura electrónica en recibidas/ | 5.092.500,00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` filas 56 y 57 |
| 4 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-6101: cheque pendiente de cobro del 2026-06-15 por -4.500.000,00 (CH-0450) | -4.500.000,00 | — | 107 | `2026-09/20-bancos/andino-6101/auxiliar-libros.csv` fila 2 |
| 5 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura 00001-00000104: IVA 1.968.750,00 en el XML y 1.968.760,00 en libros | 10,00 | — | — | `2026-09/30-facturacion/emitidas/fe-00001-00000104.xml` · `2026-09/10-contabilidad/libro-mayor.csv` filas 15 y 16 |
| 6 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-6101: cheque pendiente de cobro lleva 107 días (CH-0450) | -4.500.000,00 | — | 107 | `2026-09/20-bancos/andino-6101/auxiliar-libros.csv` fila 2 |

## El resultado

(Vacío en la salida del motor.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta raíz de documentos? → finanzas/30714520780-almacenes-del-plata (la del argumento)
- ¿Entidad, identificación fiscal, país y moneda? → Almacenes del Plata, CUIT 30714520780, Argentina, ARS (por el nombre de la carpeta y el registro del motor)
- ¿Qué marco contable aplica? → NIIF (FACPCE); no hay documento que lo declare, queda como supuesto
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → ventas 4135; compras 5135, 5145, 5195; IVA generado y descontable 2408
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205; bancos andino-6101 y pacifico-6102
- ¿Hay checklist aprobado? → Hay 00-referencia/checklist-cierre.xlsx; se marca como no aprobado hasta que una persona lo apruebe
- ¿Quién aprueba el cierre y qué festivos hay? → Contralor (por defecto); sin festivos cargados
- ¿Dónde se guarda el estado? → estado-finanzas/30714520780-almacenes-del-plata
- ¿Se acepta los términos 1.3? → Sí, José Francisco Ñáñez, 2026-10-06
- ¿Se deja la marca _CRITERIO_FINANZAS.txt en la carpeta? → No se pidió ni se autorizó; no se escribió nada en los documentos

## Fuentes

- `00-referencia/checklist-cierre.xlsx`
- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/20-bancos/andino-6101/auxiliar-libros.csv`
- `2026-09/30-facturacion/emitidas/fe-00001-00000104.xml`
- `2026-09/40-soportes/correo-estado-del-cierre.md`

La corrida quedó registrada como `2026-10-06-close-scan-1`, con 6 hallazgos. Abreviaciones respecto del reporte del motor:

- **Citas de la tabla:** en las señales 3 y 5 junté las filas del mismo archivo (por ejemplo, "filas 56 y 57").
- **Preguntas:** acorté algunas respuestas. El archivo `corridas/salida-close-scan.md` guarda el reporte completo del motor, sin recortes.
- **"El resultado":** la sección vino vacía del motor. La dejé con la nota "(Vacío en la salida del motor.)" en esta respuesta.