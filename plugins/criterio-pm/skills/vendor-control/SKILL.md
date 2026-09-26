---
name: vendor-control
description: "Entregables contractuales de un proveedor contra evidencia de recibo y contra lo facturado: qué cuenta como aceptación, los estados de un entregable, el monto que permite ver una factura adelantada, y el vencimiento del contrato. Úsalo al revisar un proveedor, al preparar una factura para aprobación, al cerrar un contrato, o cuando alguien pregunte si lo que se pagó se entregó. Vendor deliverables, acceptance evidence, invoicing."
---
<!-- COPIA · la fuente es plugins/criterio-pmo/skills/vendor-control/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# Proveedores

## Las tres cosas que nunca se miran juntas

**Lo que el contrato comprometió**, **lo que se entregó** y **lo que se facturó.** Cada
una vive en un área distinta —Compras, el proyecto, Finanzas— y nadie las cruza, porque
cruzarlas exige leer el contrato, las actas de recibo y la facturación en la misma tarde.

El hallazgo típico no es el fraude. Es **un entregable dado por bueno sin acta de
recibo**, o una factura que corre por delante de la entrega mientras nadie suma.

## Qué cuenta como evidencia de recibo

Un acta de recibo firmada, un correo de aceptación explícito, o una mención en una minuta
posterior que diga que se recibió y quién lo recibió.

**No cuenta:** que el proveedor lo declare entregado. Que aparezca en su informe de
avance. Que el gerente lo mencione en pasado. Que nadie se haya quejado. Sin documento, el
estado es `unknown`, no `delivered`.

Y la distinción que importa: *entregado* no es *aceptado*. Alguien puede haber recibido la
caja sin haber revisado el contenido. Cuando el documento no permite distinguirlos, se
reporta el que el documento sustente y se dice que no se distingue.

## Los estados

| Estado | Qué es |
|---|---|
| `pending` | No ha llegado, o llegó y no hay nada que lo pruebe |
| `delivered` | Hay documento de entrega |
| `accepted` | Hay documento de aceptación por quien tiene la facultad |
| `late` | Pasó la fecha comprometida |
| `unknown` | No se puede determinar del documento |

## El monto, y por qué cambia el hallazgo

Un entregable sin monto solo permite preguntar *"¿se entregó?"*. Con monto permite
preguntar **"¿lo que se facturó corresponde a lo que se aceptó?"**, que es otra pregunta y
es la que interesa a Finanzas.

El cálculo suma el monto de los entregables en `delivered` o `accepted` y lo compara contra
lo facturado. Dos señales distintas:

- **`vendor_invoiced_without_delivery`** — hay factura y **ni un** entregable aceptado.
- **`vendor_invoiced_over_accepted`** — hay factura por encima de la suma de lo aceptado.

La segunda no existía hasta que el esquema tuvo monto por entregable, y el monto entró
porque una corrida de prueba mostró que la primera no alcanzaba: con tres entregables
aceptados y uno sin empezar, una factura adelantada pasa desapercibida.

**Solo suma lo que tiene monto declarado**, y la salida dice cuántos de cuántos lo
traen. Comparar contra una suma incompleta y no decirlo sería peor que no comparar.

## El contrato que no está en la carpeta

Pasa a menudo, y cambia el valor de todo lo demás: sin el contrato, la lista de
entregables es lo que alguien recuerda. **Se dice de entrada**, y el análisis se presenta
como lo que es, una lista de supuestos.

## El vencimiento, que casi nadie mira

Fecha de terminación, renovación automática y **plazo de preaviso**. Un contrato cuyo
preaviso vence antes del cierre del proyecto es un hallazgo urgente, no administrativo: si
la fecha pasa, la renovación ocurre sola.

## El tono

Se reporta el hecho y su documento. *"El entregable figura como aceptado y no hay acta de
recibo en la carpeta"* — no *"el proveedor no entregó"* ni *"el gerente aceptó sin
revisar"*.

Un cruce que no cuadra tiene casi siempre una explicación que los documentos no ven: un
acta que se firmó y no se archivó, una factura que corresponde a otro hito, un acuerdo
verbal con Compras. El informe abre esa conversación; no la cierra con un juicio.
