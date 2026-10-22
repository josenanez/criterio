# /criterio-finance:einvoice-check 

Los términos (versión 1.2) ya estaban aceptados por José Francisco Ñáñez el 2026-10-06. Cruzadas las facturas de 2026-09 con el libro mayor, hay una señal por atender: una diferencia de IVA en la factura SETP99000104.

# Facturas electrónicas · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `einvoice-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura SETP99000104: IVA 1.662.500,00 en el XML y 1.663.500,00 en libros | 1.000,00 | — | — | `2026-09/30-facturacion/emitidas/fe-SETP99000104.xml` · `2026-09/10-contabilidad/libro-mayor.csv` fila 15 · `2026-09/10-contabilidad/libro-mayor.csv` fila 16 |

## El resultado

17 facturas y notas electrónicas procesadas · 17 cruzadas con su registro · 0 identificadas solo por la clave de acceso · 1 líneas de ventas o compras sin número de documento.

Sin opinión fiscal: lo que es criterio tributario queda como pregunta para la persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su país y su moneda? → Banco Andino, NIT 900123456, Colombia, COP (tomado del nombre de la carpeta)
- ¿Qué marco contable aplica? → grupo 1 (propuesta por defecto; ningún documento lo declara, por confirmar)
- ¿Cuál es el periodo que se está cerrando? → 2026-09 (el último con 10-contabilidad)
- ¿Qué cuentas cruzan las facturas? → ventas 41; compras 14, 51, 52, 61; IVA generado y descontable 2408 (visto en el balance)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (hay auxiliar); bancos andino-1101 y pacifico-1102
- ¿Qué checklist se usa? → el de la organización, 00-referencia/checklist-cierre.csv
- ¿Quién aprueba el cierre? → Sofía León (Contraloría, responsable de C-09)
- ¿Festivos del calendario? → 2026-10-12 (festivo por defecto, por confirmar)
- ¿Dónde se guarda el estado? → estado-finanzas/900123456-banco-andino

## Fuentes

- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/30-facturacion/emitidas/fe-SETP99000104.xml`
- Fuentes técnicas: F-01 (families/criterio-cfo/FUENTES.es.md)

La corrida quedó registrada como `2026-10-06-einvoice-check-1`.