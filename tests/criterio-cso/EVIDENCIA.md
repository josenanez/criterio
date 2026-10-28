# criterio-cso · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada
vez, byte a byte. La clave de cada entidad, `material/<entidad>/clave.json`, la escribe el
generador al sembrar cada defecto; el motor no la ve. Los nombres, las cuentas, las personas y las
cifras son sintéticos.

## Las entidades

| Carpeta del material | País | Industria | Exportación del CRM | Defectos sembrados | Señales esperadas |
|---|---|---|---|---:|---:|
| `retail-co` | Colombia | Retail | Salesforce por API, en CSV, con el historial de campos | 5 | 5 |
| `tecnologia-co` | Colombia | Tecnología | HubSpot, en CSV | 5 | 5 |
| `control-co` | Colombia | Retail | Un CRM cualquiera, en CSV, con su mapeo de columnas | 0 | 0 |
| `manufactura-mx` | México | Manufactura | Salesforce desde un informe, en CSV, con las fechas mes/día | 5 | 5 |
| `servicios-mx` | México | Servicios | Un CRM cualquiera, en Excel, con su mapeo de columnas | 4 | 4 |
| `control-mx` | México | Servicios | HubSpot, en Excel | 0 | 0 |

Cada entidad trae su carpeta comercial al 5 de noviembre de 2026, con octubre cerrado: la tabla de
etapas, las metas, la matriz de descuentos, la tabla de cuentas y el plan de comisiones; tres
exportaciones del CRM —el 1 y el 16 de octubre y el 3 de noviembre—; el acta del comité del 2 de
octubre, en Word, con el pronóstico comprometido; la evidencia de cada oportunidad —la propuesta en
Markdown, la orden de compra en PDF—; tres cotizaciones en PDF; y la liquidación de comisiones de
octubre. Trae además, como las dejarían los otros agentes, las fichas de los contratos de Fidel y
las facturas emitidas de los cierres de septiembre y octubre de Clara.

## Lo que se siembra, y la señal que tiene que levantar

| Defecto | Señal | Dónde |
|---|---|---|
| Una oportunidad en compromiso sin la orden de compra que exige su etapa | `stage_without_evidence` | retail-co, manufactura-mx |
| Una oportunidad abierta sin actividad desde el 12 de septiembre | `stalled_opportunity` | tecnologia-co, manufactura-mx |
| Una fecha de cierre corrida tres veces, según el historial de campos de Salesforce | `close_date_slipped` | retail-co |
| Una fecha de cierre corrida dos veces de un corte a otro, con un umbral de una vez | `close_date_slipped` | tecnologia-co, servicios-mx |
| Un pronóstico comprometido un 50 % por encima de lo cerrado | `forecast_unsupported` | retail-co, servicios-mx |
| Una meta un 40 % por encima de lo cerrado | `target_vs_closed` | tecnologia-co, manufactura-mx |
| Un 22 %, del nivel 3, aprobado por el cargo del nivel 2 | `discount_outside_policy` | retail-co |
| Un 35 % que ningún nivel de la matriz cubre | `discount_outside_policy` | manufactura-mx |
| Una venta ganada el 5 de octubre sin contrato en las fichas de Fidel | `won_without_contract` | retail-co, servicios-mx |
| Un contrato firmado con un cliente el 10 de septiembre sin factura en las fichas de Clara hasta el 10 de octubre | `signed_without_invoice` | tecnologia-co, manufactura-mx |
| Una comisión liquidada sobre un monto que no es el de la venta | `commission_differs_from_plan` | tecnologia-co, servicios-mx |

## Lo que se parece a un defecto y no lo es

Las entidades de control traen lo mismo que las otras, sin un defecto. **Las seis** traen además:

- **Un cierre que se corrió una sola vez**, por debajo del umbral.
- **Un descuento del nivel 2 aprobado por el gerente general**: un cargo superior también aprueba.
- **Un descuento del nivel 1 sin aprobación**: ese nivel no la pide.
- **Un contrato firmado con un cliente el 20 de octubre** cuyo plazo de facturación vence después de
  la fecha de la prueba: está en plazo, no ausente.
- **Un contrato con un proveedor sin factura emitida**: no es un cliente, y no se cruza.
- **El mejor escenario del acta**, más alto que el comprometido: el que se compara es el
  comprometido.
- **El correo y el teléfono de un contacto del cliente** en la propuesta, y una columna de contacto
  en la exportación de Salesforce y en la de HubSpot: no entran a la ficha ni a los resultados.
- **Una oportunidad perdida** con su fecha de cierre adelantada, que no cuenta como corrida.

**Cualquier señal en un control es una falla.**

## Las reglas de la operación real

| Caso | Lo que tiene que pasar | Dónde |
|---|---|---|
| Cada exportación, en su formato | Se reconoce por sus columnas, con su fecha, y se procesa entera | todas |
| Las fechas de un informe de Salesforce en mes/día | Se leen como mes/día, porque una de ellas lo resuelve | manufactura-mx |
| La empresa asociada de HubSpot, que la fuente no nombra | Se toma de la columna que dice el mapeo | tecnologia-co, control-mx |
| Una columna de correo en la exportación | No se procesa | retail-co, tecnologia-co, control-mx |
| La comisión | No se publica en Rostrum: la configuración no lo dice | todas |

## Lo que el material no prueba

- **El CRM de una organización real.** Nada de esto se ha corrido sobre las exportaciones, las
  propuestas o las liquidaciones de una empresa concreta.
- **La extracción del agente.** `evaluar.py` prueba el motor con la ficha correcta, que está en la
  clave. Que el agente lea la propuesta, el acta y la cotización y los registre bien lo prueba la
  ronda con los agentes, sobre este mismo material.
- **Microsoft Dynamics y Zoho**, que están en la hoja de ruta, ni las exportaciones de Salesforce y
  de HubSpot con los nombres de columna en español.
- **Varias monedas en una misma exportación**: cada entidad trae una sola.
- **Ecuador, Perú y Chile**, que siguen en la hoja de ruta.
