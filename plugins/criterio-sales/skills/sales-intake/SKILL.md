---
name: sales-intake
description: "Qué documentos procesa la familia CSO, dónde va cada uno, qué tablas procesa el motor directamente y qué extrae el agente a la ficha. Úsalo al recorrer la carpeta comercial de una entidad, al recibir una exportación del CRM, una propuesta, una orden de compra, una cotización o una liquidación, al explicar dónde va un archivo o cuando una tabla no trae las columnas esperadas. Sales document intake, folder structure."
---

# Los documentos de la función comercial

## Dos clases de documento, dos formas de procesarlo

**Las tablas las procesa el motor directamente.** Las exportaciones de oportunidades del CRM, el historial de la fecha de cierre, la tabla de etapas, las metas, la matriz de descuentos, la tabla de cuentas, el plan de comisiones y la liquidación de cada periodo llegan como `.csv` o `.xlsx`. Nada de eso se transcribe ni se resume: `ventas.py` lo procesa con su fila de origen, que es la cita. Cómo se procesa cada exportación del CRM, en **crm-exports**.

**Lo que solo trae un documento escrito lo extrae el agente a la ficha.** La propuesta enviada, la orden de compra y el acta de aceptación de cada oportunidad; el acta o el paquete del comité comercial con el pronóstico que se compromete; cada cotización o pedido con su descuento y su aprobación. Se convierte con `ventas.py convertir` y se registra en la ficha del periodo con su cita: la de Augusto con **pipeline-record**, la de Valeria con **deal-record**. El código no lo inventa ni lo infiere.

## Las columnas de una tabla

El motor reconoce las columnas por su nombre y por sus variantes más comunes:

| Tabla | Archivo, por cómo empieza su nombre | Columnas que necesita | Opcionales |
|---|---|---|---|
| `stages` | `00-referencia/etapas` | `etapa`, `orden`, `probabilidad` | `exige` (los documentos que pide, separados por coma o `+`), `tipo` (`abierta`, `ganada` o `perdida`) |
| `targets` | `00-referencia/metas` | `periodo` (AAAA-MM), `meta` | `linea` |
| `discounts` | `00-referencia/matriz-descuentos` | `nivel`, `tope` (el descuento máximo del nivel, en %) | `aprueba` (el cargo que lo aprueba; `ninguno` si no pide aprobación) |
| `accounts` | `00-referencia/cuentas` | `cuenta` (el id o el nombre de la cuenta en el CRM), `identificacion` (el NIT o el RFC del cliente) | `nombre` |
| `commission_plan` | `00-referencia/plan-comisiones` | `tasa` (en %) | `linea` (`todas` si es una sola) |
| `commission_settlement` | `50-comisiones/liquidacion-<AAAA-MM>` | `responsable`, `liquidado` | — |

Cuando una tabla las llama de otra forma, el motor dice cuáles faltan. **No adivines**: pregúntale a la persona cómo se llama la columna y regístralo en `columns` de la configuración, por tabla. Los números llegan con coma o con punto decimal; las fechas en ISO, `dd/mm/aaaa` o como número de serie de Excel. El motor los normaliza; un valor que no puede procesar lo reporta.

## La evidencia se reconoce por su nombre

Cada documento de evidencia de una oportunidad empieza por el id de la oportunidad, tal como lo trae el CRM, seguido de un guion bajo: `OPP-1042_propuesta.pdf`, `OPP-1042_orden-compra.pdf`. Cada cotización empieza por su id: `COT-2210_cotizacion.pdf`. Un documento de `30-evidencia/` que empieza por el id de una oportunidad del embudo y no está en la ficha, el motor lo dice: hay que llevarlo.

## Los datos de contacto no entran

Una exportación del CRM puede traer el correo o el teléfono de un contacto. El motor no los procesa, y la ficha no los guarda: guarda la cuenta y la oportunidad. Una ficha con un correo o un teléfono la marca el motor como un problema de la ficha.

<!-- cso:intake · generado por scripts/familias.py; no se edita a mano -->
Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo está fuera de su lugar y dónde iría (ADR 0007). Las exportaciones del CRM tienen un solo lugar, `10-crm/`: Augusto procesa el embudo y Valeria toma de ahí lo ganado para cruzarlo con los contratos y las facturas.

Una carpeta por entidad, con el NIT o el RFC al inicio del nombre. Dentro, la referencia de la función comercial, las exportaciones del CRM con su fecha, el comité, la evidencia de cada oportunidad, las cotizaciones y las liquidaciones de comisiones.

```
comercial/
└── <entidad>/
    ├── 00-referencia/
    ├── 10-crm/
    ├── 20-comite/
    ├── 30-evidencia/
    ├── 40-cotizaciones/
    └── 50-comisiones/
estado-comercial/
```

**`<entidad>/`** · Lo que la organización lleva para toda la función comercial

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-referencia/` | La tabla de etapas —el documento que exige cada una y su probabilidad—, las metas del año, la matriz de descuentos, el plan de comisiones y la tabla de cuentas con la identificación de cada cliente | Augusto, Valeria |
| `10-crm/` | Las exportaciones de oportunidades del CRM, en CSV o Excel, con la fecha de la exportación en el nombre, y el historial de la fecha de cierre si el CRM lo exporta | Augusto, Valeria |
| `20-comite/` | Las actas y los paquetes del comité comercial, con el pronóstico que se compromete para el periodo | Augusto |
| `30-evidencia/` | Las propuestas enviadas, las órdenes de compra y las actas de aceptación, con el id de la oportunidad al inicio del nombre | Augusto |
| `40-cotizaciones/` | Las cotizaciones y los pedidos con su precio, su descuento y su aprobación, con el id de la cotización al inicio del nombre | Valeria |
| `50-comisiones/` | La liquidación de comisiones de cada periodo, con el periodo en el nombre | Valeria |

**`estado-comercial/`** · Lo que escriben Augusto y Valeria: la configuración, la ficha de cada periodo, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /cso:intake -->
