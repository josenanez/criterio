# /criterio-finance:einvoice-check 

# Facturas electrónicas · Minera Cóndor · periodo 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `einvoice-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura recibida 002-001-000000290 del 2026-09-27 por 4,600.00 sin registro contable | 4,600.00 | — | — | `2026-09/30-facturacion/recibidas/fr-002-001-000000290.xml` |

## El resultado

18 facturas y notas electrónicas procesadas · 17 cruzadas con su registro · 0 identificadas solo por la clave de acceso · 1 líneas de ventas o compras sin número de documento.

Sin opinión fiscal: lo que es criterio tributario queda como pregunta para la persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta raíz de documentos? → finanzas/0990054321001-minera-condor (la del argumento)
- ¿Entidad, país y moneda? → Minera Cóndor, RUC 0990054321001, Ecuador, USD (por el RUC de las facturas y la carpeta)
- ¿Qué marco contable aplica? → No indicado en los documentos; queda registrado así
- ¿Qué periodo se está cerrando? → 2026-09 (el último con 10-contabilidad/)
- ¿Qué cuentas cruzan las facturas? → Ventas 41; compras 14/51/52/61; IVA 2408 (los del balance de comprobación)
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205 (tienen auxiliar); andino-4101 y pacifico-4102 (carpetas de 20-bancos)
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; sin constancia de aprobación, queda como no aprobado
- ¿Quién aprueba el cierre? → Sofía León (responsable de C-09 en el checklist)
- ¿Festivos? → Ninguno a mano; la lista queda vacía

## Fuentes

- `2026-09/30-facturacion/recibidas/fr-002-001-000000290.xml`
- Fuentes técnicas: F-04 (families/criterio-cfo/FUENTES.es.md)