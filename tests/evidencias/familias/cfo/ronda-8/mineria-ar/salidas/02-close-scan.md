# /criterio-finance:close-scan 

Archivos nuevos o cambiados: 67 nuevos, 0 cambiados, 0 borrados. Hay 4 señales abiertas. El motor no da el conteo de la corrida anterior, así que no puedo decir cuántas de las 4 son nuevas.

La declaración de Sofía León (2026-10-05) dice que el cierre está «en curso». La ficha ya coincidía con el correo y la carta del auditor, así que no la modifiqué. Los términos ya estaban vigentes, por lo que no registré ninguna aceptación.

# Qué cambió en el cierre · Minera Cordillera de Cuyo · periodo 2026-09

**Entidad:** Minera Cordillera de Cuyo (30709031143) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.0.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El mismo CUFE o la misma clave de acceso aparece registrado dos veces (`einvoice_duplicate`) | el mismo CAE aparece en 2 archivos (00001-00000102) | 26.317.500,00 | — | — | `2026-09/30-facturacion/emitidas/fe-00001-00000102-reenviada.xml` · `2026-09/30-facturacion/emitidas/fe-00001-00000102.xml` |
| 2 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura emitida 00001-00000109 del 2026-09-28 por 14.520.000,00 sin registro contable | 14.520.000,00 | — | — | `2026-09/30-facturacion/emitidas/fe-00001-00000109.xml` |
| 3 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-6701: nota débito sin registrar del 2026-09-30 por -1.200.000,00 (sin referencia) | -1.200.000,00 | — | 0 | `2026-09/20-bancos/andino-6701/extracto.xlsx` fila 17 |
| 4 | Un requerimiento del auditor no tiene respuesta con soporte (`audit_request_unanswered`) | R-05 · Contratos de los proveedores principales: vencido, venció el 2026-10-02 | — | Jorge Vela | 4 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.xlsx` fila 6 |

## El resultado

(El motor dejó esta sección vacía.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta raíz de la entidad? → finanzas/30709031143-minera-cordillera-de-cuyo (la dio el argumento)
- ¿Nombre, CUIT, país y moneda? → Minera Cordillera de Cuyo · 30709031143 · AR · ARS (nombre de la carpeta, CUIT de los comprobantes)
- ¿Cuál es el marco contable? → NIIF adoptadas por la FACPCE (RT 26): propuesta por defecto, ningún documento lo dice; por confirmar
- ¿Cuál es el periodo que se cierra? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → ventas 4135; compras 5135, 5145, 5195; IVA generado y descontable 2408
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205; bancos andino-6701 y pacifico-6702
- ¿Qué checklist se usa y quién aprueba? → 00-referencia/checklist-cierre.xlsx, sin aprobar; aprueba Sofía León (tarea C-09)
- ¿Festivos y carpeta de estado? → sin festivos a la mano; estado en estado-finanzas/30709031143-minera-cordillera-de-cuyo
- ¿Se marca la carpeta con _CRITERIO_FINANZAS.txt? → no se marcó: no hubo un sí de la persona

## Fuentes

- `2026-09/20-bancos/andino-6701/extracto.xlsx`
- `2026-09/30-facturacion/emitidas/fe-00001-00000102-reenviada.xml`
- `2026-09/30-facturacion/emitidas/fe-00001-00000102.xml`
- `2026-09/30-facturacion/emitidas/fe-00001-00000109.xml`
- `2026-09/50-auditoria/requerimientos/pbc-2026-09.xlsx`

**Dos diferencias con lo que se guardó:**
- **Líneas añadidas:** en `salida-close-scan.md` quedó una segunda línea de introducción que aquí omití. Esa línea decía que la ficha y R-09 «quedaron como estaban».
- **Texto acortado:** abreviué el texto de dos respuestas en «Las preguntas que hizo».

La corrida quedó registrada como `2026-10-06-close-scan-1`, con 4 hallazgos.