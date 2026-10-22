# /criterio-finance:einvoice-check 

Los términos vigentes (versión 1.2) ya estaban aceptados por José Francisco Ñáñez el 2026-10-06. El cruce del periodo 2026-09 deja dos señales para revisar; ninguna lleva opinión fiscal.

# Facturas electrónicas · Cooperativa Sierra Alta · periodo 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `einvoice-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura emitida 001-001-000000109 del 2026-09-28 por 4,887.50 sin registro contable | 4,887.50 | — | — | `2026-09/30-facturacion/emitidas/fe-001-001-000000109.xml` |
| 2 | Un registro que la necesita no tiene factura electrónica que lo soporte (`recorded_without_einvoice`) | documento 002-001-000000202 en las cuentas de compras por 3,395.00 sin factura electrónica en recibidas/ | 3,395.00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` fila 53 · `2026-09/10-contabilidad/libro-mayor.csv` fila 54 |

## El resultado

16 facturas y notas electrónicas procesadas · 15 cruzadas con su registro · 0 identificadas solo por la clave de acceso · 0 líneas de ventas o compras sin número de documento.

Sin opinión fiscal: lo que es criterio tributario queda como pregunta para la persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su RUC, país y moneda? → Cooperativa Sierra Alta, RUC 1790012345001, Ecuador, USD (por el nombre de la carpeta y las facturas del SRI)
- ¿Qué marco contable aplica? → NIIF para PYMES, por confirmar: ningún documento lo dice
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → Ventas 41, compras 5135/5145/5195, IVA 2408 (del balance de comprobación)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (los auxiliares que hay); bancos andino-2301 y pacifico-2302
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; sin aprobación registrada
- ¿Quién aprueba el cierre? → Sofía León, responsable de C-09 en el checklist
- ¿Hay festivos del calendario? → No encontrado: ningún documento los trae

## Fuentes

- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/30-facturacion/emitidas/fe-001-001-000000109.xml`
- Fuentes técnicas: F-04 (families/criterio-cfo/FUENTES.es.md)

---
Corrida registrada como `2026-10-06-einvoice-check-1`. El reporte del motor está en `estado-finanzas/1790012345001-cooperativa-sierra-alta/cierre/2026-09/reporte-einvoice-check.md`.