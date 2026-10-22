# /criterio-finance:einvoice-check 

Procesé las 18 facturas y notas del periodo 2026-09 de Almacenes Caribe, y las 18 cruzaron con su registro. El cruce dejó 3 señales: dos duplicados y una diferencia de valor. Los términos 1.2 estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-06.

# Facturas electrónicas · Almacenes Caribe · periodo 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `einvoice-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Mismo CUFE registrado dos veces (`einvoice_duplicate`) | El mismo CUFE aparece en 2 archivos (SETP99000102) | 8.330.000,00 | `2026-09/30-facturacion/emitidas/fe-SETP99000102-reenviada.xml` · `…/fe-SETP99000102.xml` |
| 2 | Mismo CUFE registrado dos veces (`einvoice_duplicate`) | Factura SETP77000201 registrada en 2 asientos (C-021, C-022) | 3.104.000,00 | `2026-09/10-contabilidad/libro-mayor.csv` filas 53, 54, 56, 57 |
| 3 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | Factura SETP77000201: base 1.552.000,00 en el XML y 3.104.000,00 en libros; IVA 294.880,00 en el XML y 589.760,00 en libros | 1.846.880,00 | `fr-SETP77000201.xml` · `libro-mayor.csv` filas 53, 54, 56 |

## El resultado

- 18 facturas y notas electrónicas procesadas, 18 cruzadas con su registro.
- 0 identificadas solo por la clave de acceso.
- 2 líneas de ventas o compras sin número de documento.

Sin opinión fiscal: lo que es criterio tributario queda como pregunta para la persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- **Entidad:** Almacenes Caribe, NIT 900765432, Colombia, COP.
- **Marco contable:** no se encontró en los documentos, queda «por confirmar».
- **Periodo:** 2026-09.
- **Cuentas:** ventas 41, compras 14/51/52/61, IVA 2408.
- **Conciliación:** cuentas 1305 y 2205, bancos andino-3701 y pacifico-3702. Solo existe auxiliar de 1305.
- **Checklist:** el de la organización, sin aprobación registrada.
- **Aprobador y festivos:** Sofía León, festivo 2026-10-12 (sin confirmar).
- **Términos:** aceptados por José Francisco Ñáñez, 2026-10-06.

## Fuentes

- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/30-facturacion/emitidas/fe-SETP99000102.xml`
- `2026-09/30-facturacion/emitidas/fe-SETP99000102-reenviada.xml`
- `2026-09/30-facturacion/recibidas/fr-SETP77000201.xml`
- Fuente técnica: F-01

El reporte completo lo escribió el motor en `estado-finanzas/900765432-almacenes-caribe/cierre/2026-09/reporte-einvoice-check.md`. Lo que le mostré aquí es una versión condensada de ese reporte, no el texto íntegro.

La salida guardada en `corridas/salida-einvoice-check.md` es copia del reporte del motor, no de este resumen. La corrida quedó registrada como `2026-10-06-einvoice-check-1`, con 8 hallazgos.