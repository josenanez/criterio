---
name: won-to-cash
description: "Cómo se cruza lo ganado en el CRM con los contratos de las fichas de Fidel y lo firmado con las facturas de las fichas de Clara, por la identificación del cliente, sin volver a procesar sus documentos. Úsalo al explicar el reporte de la venta a la factura, al configurar dónde están las fichas de Fidel y de Clara o cuando una cuenta no tiene identificación. Won to contract to invoice."
---

# De lo ganado a la factura

**Valeria no procesa contratos ni facturas electrónicas.** El contrato lo dice la ficha de Fidel (`criterio-legal`) y la factura la de Clara (`criterio-finance`): Valeria las lee de su estado, como ellos las escriben (ADR 0019).

## La identificación del cliente es la costura

El CRM conoce la cuenta; Fidel y Clara conocen la identificación fiscal. `00-referencia/cuentas` las pone una al lado de la otra: cada cuenta del CRM —por su id o por su nombre— con el NIT o el RFC del cliente. **Una cuenta ganada que no está en la tabla no se cruza**: el reporte la dice como no procesada, y no se completa por parecido de nombre.

## Ganado sin contrato

Una oportunidad ganada en los últimos `won_lookback_days` (90 por omisión) tiene su contrato si en las fichas de Fidel hay uno **firmado por las dos partes** con ese cliente, vigente el día en que se ganó o firmado después. Pasados `contract_grace_days` desde el cierre (15 por omisión) sin ese contrato, se levanta `won_without_contract`.

## Firmado sin factura

Un contrato de Fidel con un cliente de la tabla de cuentas, firmado en los últimos `signed_lookback_days` (120 por omisión), tiene su factura si en las fichas de Clara hay una **factura emitida a ese cliente** entre la firma y la firma más `invoice_days` (30 por omisión). Si el plazo venció sin ella, se levanta `signed_without_invoice`.

**Un periodo que Clara no ha cerrado no se da por ausente.** Si el plazo cae en un mes que todavía no tiene su cierre en las fichas de Clara, el reporte lo dice como pendiente, no como señal.

## Dónde están las fichas

- **Fidel**: `revenue.contract_records`, la carpeta `contratos/` de su estado (`estado-legal/<entidad>/contratos/`).
- **Clara**: `revenue.invoice_records`, la carpeta de su estado que tiene `cierre/` (`estado-finanzas/<entidad>/`). Cada cierre trae sus facturas emitidas en `cierre/<AAAA-MM>/resultados.json`.

En el setup, búscalas con Glob y propone la ruta que encontraste; nunca una que no comprobaste.
