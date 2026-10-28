---
name: commission-plan
description: "Cómo calcula el motor la comisión que da el plan sobre lo ganado y facturado, contra lo que se liquidó, y por qué no se publica en Rostrum por omisión. Úsalo al explicar el reporte de comisiones o al configurar el plan. Commission plan check."
---

# Las comisiones contra el plan

## Lo que da el plan

`00-referencia/plan-comisiones` trae la tasa —en %— por línea, o una sola con `linea` = `todas`. La base de cada responsable en el periodo son **sus oportunidades ganadas con cierre en el periodo y ya facturadas**: con una factura emitida al cliente, en las fichas de Clara, desde el cierre hasta la fecha de corte. Lo ganado sin facturar no comisiona todavía.

Lo que da el plan es la suma, oportunidad por oportunidad, de su monto por la tasa de su línea.

## Contra lo liquidado

`50-comisiones/liquidacion-<AAAA-MM>` trae lo que se liquidó a cada responsable. `commission_differs_from_plan` se levanta cuando la diferencia supera `commission_tolerance` (1 por omisión), hacia arriba o hacia abajo, y cuando el plan da una comisión que la liquidación no trae.

El responsable es el de la oportunidad en el CRM —`OwnerId` en Salesforce, `Deal owner` en HubSpot—, y la liquidación lo nombra igual. Si lo nombra de otra forma, se dice; no se emparejan por parecido.

## Por qué no se publica

Las comisiones son la remuneración de personas identificables. **El reporte no se publica en Rostrum** salvo que `revenue.publish_commissions` lo diga: Rostrum no sirve su reporte, sus señales ni sus corridas (ADR 0019).

## Lo que el motor no hace

- No liquida ni corrige una comisión.
- No compara a las personas entre sí: cada fila es la de su responsable contra el plan.
