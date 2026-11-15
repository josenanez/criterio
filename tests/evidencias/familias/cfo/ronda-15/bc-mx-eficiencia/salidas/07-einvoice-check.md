# /criterio-finance:einvoice-check 

Cruce de las facturas de 2026-09 contra la contabilidad de Distribuidora del Noroeste (México, así que no hubo conversión de Honduras). Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-06, y no hizo falta registrarlos otra vez.

# Facturas electrónicas · Distribuidora del Noroeste · periodo 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `einvoice-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El mismo CUFE o la misma clave de acceso aparece registrado dos veces (`einvoice_duplicate`) | factura B000201 registrada en 2 asientos (C-021, C-022) | 69,840.00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` filas 53, 54, 56 y 57 |
| 2 | Un registro que la necesita no tiene factura electrónica que lo soporte (`recorded_without_einvoice`) | documento B000202 en las cuentas de compras por 61,110.00 sin factura electrónica en recibidas/ | 61,110.00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` filas 59 y 60 |
| 3 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura B000201: base 34,920.00 en el XML y 69,840.00 en libros; IVA 5,587.20 en el XML y 11,174.40 en libros | 40,507.20 | — | — | `2026-09/30-facturacion/recibidas/fr-B000201.xml` · `2026-09/10-contabilidad/libro-mayor.csv` filas 53, 54 y 56 |

## El resultado

16 facturas y notas electrónicas procesadas · 16 cruzadas con su registro · 0 identificadas solo por la clave de acceso · 1 línea de ventas o compras sin número de documento.

Sin opinión fiscal: lo que es criterio tributario queda como pregunta para la persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Se tomó la respuesta sugerida de los documentos en cada una:

- Carpeta de documentos: `finanzas/DNO190402B43-distribuidora-del-noroeste`, la que trae el argumento.
- Entidad: Distribuidora del Noroeste · RFC DNO190402B43 · México · MXN.
- Marco contable: NIF del CINIF. Ningún documento lo dice.
- Periodo: 2026-09, el último con `10-contabilidad/`.
- Cuentas que cruzan las facturas: ventas 4135 · compras 5135, 5145, 5195 · IVA 2408.
- Cuentas a conciliar: 1305 y 2205; bancos andino-4301 y pacifico-4302.
- Checklist: el de la organización, `00-referencia/checklist-cierre.csv`.
- Aprobación: Sofía León, sin festivos a mano.
- Estado: `estado-finanzas/DNO190402B43-distribuidora-del-noroeste`.
- Marcar la carpeta con `_CRITERIO_FINANZAS.txt`: no, porque nadie dio el sí en esta sesión de prueba.

## Fuentes

- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/30-facturacion/recibidas/fr-B000201.xml`
- Fuentes técnicas: F-19 (`families/criterio-cfo/FUENTES.es.md`)

La corrida quedó registrada como `2026-10-06-einvoice-check-1`, con 8 hallazgos. La salida completa está en `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/corridas/salida-einvoice-check.md`, y el reporte en `cierre/2026-09/reporte-einvoice-check.md`.