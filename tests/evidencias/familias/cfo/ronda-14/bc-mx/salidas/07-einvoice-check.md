# /criterio-finance:einvoice-check 

Distribuidora del Noroeste está en México, así que sus facturas son CFDI en XML. No hizo falta el paso de conversión que se usa para Honduras: el motor cruzó directamente los XML de `30-facturacion/` contra las cuentas de ventas, compras e IVA.

Las tres señales son de compras. Hay una factura recibida registrada dos veces, y la base y el IVA de ese registro en libros no coinciden con su XML. Hay además un registro de compras sin XML en `recibidas/`. Si se trata de un error de registro o de otra cosa, lo decides tú; aquí no se da opinión fiscal.

# Facturas electrónicas · Distribuidora del Noroeste · periodo 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `einvoice-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El mismo CUFE o la misma clave de acceso aparece registrado dos veces (`einvoice_duplicate`) | factura B000201 registrada en 2 asientos (C-021, C-022) | 69,840.00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` fila 53 · `2026-09/10-contabilidad/libro-mayor.csv` fila 54 · `2026-09/10-contabilidad/libro-mayor.csv` fila 56 · `2026-09/10-contabilidad/libro-mayor.csv` fila 57 |
| 2 | Un registro que la necesita no tiene factura electrónica que lo soporte (`recorded_without_einvoice`) | documento B000202 en las cuentas de compras por 61,110.00 sin factura electrónica en recibidas/ | 61,110.00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` fila 59 · `2026-09/10-contabilidad/libro-mayor.csv` fila 60 |
| 3 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura B000201: base 34,920.00 en el XML y 69,840.00 en libros; IVA 5,587.20 en el XML y 11,174.40 en libros | 40,507.20 | — | — | `2026-09/30-facturacion/recibidas/fr-B000201.xml` · `2026-09/10-contabilidad/libro-mayor.csv` fila 53 · `2026-09/10-contabilidad/libro-mayor.csv` fila 54 · `2026-09/10-contabilidad/libro-mayor.csv` fila 56 |

## El resultado

16 facturas y notas electrónicas procesadas · 16 cruzadas con su registro · 0 identificadas solo por la clave de acceso · 1 líneas de ventas o compras sin número de documento.

Sin opinión fiscal: lo que es criterio tributario queda como pregunta para la persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad: nombre, identificación fiscal, país y moneda? → Distribuidora del Noroeste, RFC DNO190402B43, México, MXN (sugerida desde el nombre de la carpeta y los CFDI 4.0 del periodo)
- ¿Qué marco contable adoptó la entidad? → NIF del CINIF (sugerida: la mayoría de las no listadas en México, F-20; ningún documento dice otro)
- ¿Cuál es el periodo que se está cerrando? → 2026-09
- ¿Qué cuentas cruzan las facturas? → Ventas 4135; compras 5135, 5145, 5195; IVA generado 2408; IVA descontable 2408 (las que sostienen las facturas del periodo)
- ¿Qué cuentas se concilian contra auxiliar y qué cuentas bancarias se esperan? → 1305 y 2205; bancos andino-4301 y pacifico-4302
- ¿Qué checklist se usa? → El de la organización: 00-referencia/checklist-cierre.csv
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (C-09 del checklist); sin festivos registrados
- ¿Dónde se guarda el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste
- ¿Acepta los términos de esta versión? → Sí, José Francisco Ñáñez, 2026-10-06

## Fuentes

- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/30-facturacion/recibidas/fr-B000201.xml`
- Fuentes técnicas: F-19 (families/criterio-cfo/FUENTES.es.md)

---

La corrida quedó registrada como `2026-10-06-einvoice-check-1`. El motor contó 8 hallazgos. Lo que se mostró está guardado en `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/corridas/salida-einvoice-check.md`.