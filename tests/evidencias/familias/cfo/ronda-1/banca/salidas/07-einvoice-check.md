# /criterio-finance:einvoice-check 

Cruce de las facturas electrónicas de 2026-09 de Banco Andino con el libro mayor. Hay una señal por atender: la factura SETP99000104 tiene un IVA distinto en el XML y en libros. Esto no es opinión fiscal.

# Facturas electrónicas · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.7.0 · **Aprueba:** Sofía León · **Comando:** `einvoice-check`

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

- ¿Cuál es la entidad, su NIT, país y moneda? → Banco Andino, NIT 900123456, Colombia, COP (de la carpeta finanzas/900123456-banco-andino)
- ¿Qué marco contable aplica? → Grupo 1 (F-05); solo se registra
- ¿Cuál es el periodo que se está cierrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué prefijos cruzan las facturas? → Ventas 41; compras 14, 51, 52, 61; IVA 2408 (del balance de comprobación)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (las que tienen auxiliar); bancos andino-1101 y pacifico-1102 (carpetas de 20-bancos)
- ¿Qué checklist se usa y está aprobado? → El de la organización (00-referencia/checklist-cierre.csv); sin aprobación documentada, queda como no aprobado
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (responsable de C-09); festivo 2026-10-12
- ¿Dónde se guarda el estado? → estado-finanzas/900123456-banco-andino
- ¿Acepta los términos vigentes? → Sí, José Francisco Ñáñez, versión 1.2, 2026-10-06 (dado en el encargo de la prueba)
- ¿Se deja el archivo _CRITERIO_FINANZAS.txt en la carpeta de documentos? → No; nadie autorizó escribir dentro de los documentos

## Fuentes

- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/30-facturacion/emitidas/fe-SETP99000104.xml`
- Fuentes técnicas: F-01 (families/criterio-cfo/FUENTES.es.md)

La corrida quedó registrada como `2026-10-06-einvoice-check-1`.