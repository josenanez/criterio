# criterio-cso · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada
vez, byte a byte. La clave de cada entidad, `material/<entidad>/clave.json`, la escribe el
generador al sembrar cada defecto; el motor no la ve. Los nombres, las cuentas, las personas y las
cifras son sintéticos.

## Las entidades

| Carpeta del material | País | Industria | Exportación del CRM | Defectos sembrados | Señales esperadas |
|---|---|---|---|---:|---:|
| `retail-co` | Colombia | Retail | Salesforce por API, en CSV, con el historial de campos | 5 + 16 | 21 |
| `tecnologia-co` | Colombia | Tecnología | HubSpot, en CSV | 5 + 15 | 20 |
| `control-co` | Colombia | Retail | Un CRM cualquiera, en CSV, con su mapeo de columnas | 0 | 0 |
| `manufactura-mx` | México | Manufactura | Salesforce desde un informe, en CSV, con las fechas mes/día | 5 + 15 | 20 |
| `servicios-mx` | México | Servicios | Un CRM cualquiera, en Excel, con su mapeo de columnas | 4 + 15 | 19 |
| `control-mx` | México | Servicios | HubSpot, en Excel | 0 | 0 |
| `retail-ec` | Ecuador | Retail | Dynamics 365 Sales, en Excel, sin la última actividad | 5 + 13 | 18 |
| `tecnologia-ec` | Ecuador | Tecnología | Zoho CRM, en CSV, con la última actividad por el mapeo | 5 + 15 | 20 |
| `control-ec` | Ecuador | Retail | Salesforce desde un informe, en CSV, con las fechas mes/día | 0 | 0 |
| `manufactura-pe` | Perú | Manufactura | Salesforce por API, en CSV, con el historial de campos | 5 + 15 | 20 |
| `servicios-pe` | Perú | Servicios | Dynamics 365 Sales, en Excel, sin la última actividad | 5 + 15 | 20 |
| `control-pe` | Perú | Servicios | Zoho CRM, en CSV, con la última actividad por el mapeo | 0 | 0 |
| `retail-cl` | Chile | Retail | Zoho CRM, en Excel, con la última actividad por el mapeo | 5 + 14 | 19 |
| `tecnologia-cl` | Chile | Tecnología | HubSpot, en CSV | 5 + 15 | 20 |
| `control-cl` | Chile | Retail | Dynamics 365 Sales, en Excel, sin la última actividad | 0 | 0 |

Colombia y México son el material de la ronda 1, con **80 señales sembradas**. Ecuador, Perú y Chile
son el del incremento 3, con **117**: cada uno, más de las 73 que pide un piso del 95 % sin fallas
(decisión 0020). Cada defecto sembrado es la siembra —la señal una vez— más el lote de la entidad.
Cada formato nuevo —Dynamics y Zoho— está en dos entidades con defectos y en un control.

Cada entidad trae su carpeta comercial al 5 de noviembre de 2026, con octubre cerrado: la tabla de
etapas, las metas, la matriz de descuentos, la tabla de cuentas y el plan de comisiones; tres
exportaciones del CRM —el 1 y el 16 de octubre y el 3 de noviembre—; el acta del comité del 2 de
octubre, en Word, con el pronóstico comprometido; la evidencia de cada oportunidad —la propuesta en
Markdown, la orden de compra en PDF—; las cotizaciones en PDF; y la liquidación de comisiones de
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

En Ecuador, Perú y Chile, la siembra de cada entidad:

| Entidad | Lo que se siembra |
|---|---|
| retail-ec | La etapa sin la orden de compra, la oportunidad detenida —sin cambio de un corte a otro, porque Dynamics no exporta la última actividad—, el pronóstico sin respaldo, el 22 % aprobado por el nivel 2 y la venta ganada sin contrato |
| tecnologia-ec | La detenida, la meta lejos de lo cerrado, el contrato sin factura, la comisión distinta y el cierre corrido de un corte a otro |
| manufactura-pe | El cierre corrido según el historial de Salesforce, la etapa sin su documento, el 35 % fuera de la matriz, la venta ganada sin contrato y el pronóstico sin respaldo |
| servicios-pe | La meta lejos, el contrato sin factura, la comisión distinta, el cierre corrido de un corte a otro y el 22 % aprobado por el nivel 2 |
| retail-cl | La etapa sin su documento, la detenida, el pronóstico sin respaldo, la venta ganada sin contrato y el 35 % fuera de la matriz |
| tecnologia-cl | La meta lejos, la comisión distinta, el cierre corrido de un corte a otro, el contrato sin factura y el 22 % aprobado por el nivel 2 |

## El lote

Las señales que se repiten de una oportunidad a otra se siembran además en un lote, cada una en su
propia oportunidad, cotización o contrato. Las del lote cierran en diciembre o son de clientes
nuevos: no mueven el pronóstico, la meta ni las comisiones de la siembra.

| Defecto del lote | Señal | retail-co | tecnologia-co | manufactura-mx | servicios-mx |
|---|---|---:|---:|---:|---:|
| Una oportunidad en compromiso con la propuesta y sin la orden de compra | `stage_without_evidence` | 4 | 3 | 4 | 3 |
| Una oportunidad sin actividad desde el 5 de septiembre | `stalled_opportunity` | 3 | 3 | 4 | 3 |
| Una fecha de cierre corrida tres veces, según el historial de Salesforce | `close_date_slipped` | 3 | — | — | — |
| Una fecha de cierre corrida dos veces de un corte a otro, con el umbral de una | `close_date_slipped` | — | 3 | — | 3 |
| Un 22 % del nivel 3 aprobado por el cargo del nivel 2 | `discount_outside_policy` | 2 | 2 | — | 2 |
| Un 35 % que ningún nivel cubre | `discount_outside_policy` | — | — | 2 | — |
| Una venta ganada en octubre con un cliente nuevo, sin contrato | `won_without_contract` | 2 | 1 | 2 | 3 |
| Un contrato firmado en septiembre con un cliente nuevo, sin factura | `signed_without_invoice` | 2 | 3 | 3 | 1 |

El lote de Ecuador, Perú y Chile:

| Defecto del lote | retail-ec | tecnologia-ec | manufactura-pe | servicios-pe | retail-cl | tecnologia-cl |
|---|---:|---:|---:|---:|---:|---:|
| La etapa sin la orden de compra | 4 | 3 | 3 | 3 | 4 | 3 |
| La oportunidad detenida | 3 | 3 | 3 | 3 | 3 | 3 |
| El cierre corrido, según el historial de Salesforce | — | — | 3 | — | — | — |
| El cierre corrido de un corte a otro, con el umbral de una vez | — | 3 | — | 3 | — | 3 |
| El 22 % aprobado por el cargo del nivel 2 | 2 | 2 | — | 2 | — | 2 |
| El 35 % que ningún nivel cubre | — | — | 2 | — | 2 | — |
| La venta ganada con un cliente nuevo, sin contrato | 2 | 1 | 2 | 2 | 2 | 2 |
| El contrato firmado con un cliente nuevo, sin factura | 2 | 3 | 2 | 2 | 3 | 2 |

## Lo que se parece a un defecto y no lo es

Las entidades de control traen lo mismo que las otras, sin un defecto. **Las quince** traen además:

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
- **En Dynamics, una oportunidad que se gestiona sin una columna que lo diga**: la exportación no
  trae la última actividad, y su monto se revisa en cada corte; no está detenida.

**Cualquier señal en un control es una falla.**

## Las reglas de la operación real

| Caso | Lo que tiene que pasar | Dónde |
|---|---|---|
| Cada exportación, en su formato | Se reconoce por sus columnas, con su fecha, y se procesa entera | todas |
| Las fechas de un informe de Salesforce en mes/día | Se leen como mes/día, porque una de ellas lo resuelve | manufactura-mx |
| La empresa asociada de HubSpot, que la fuente no nombra | Se toma de la columna que dice el mapeo | tecnologia-co, control-mx, tecnologia-cl |
| Dynamics: el estado (Open, Won, Lost) manda sobre la etapa; la fecha llega como fecha de Excel y el monto como número | Se leen así, sin la última actividad: lo detenido sale de lo que no cambió de un corte a otro | retail-ec, servicios-pe, control-cl |
| Zoho: la última actividad no es un campo estándar | Se toma de la columna que dice el mapeo, `Last Activity Time` | tecnologia-ec, control-pe, retail-cl |
| La identificación fiscal de cada país: el RUC de Ecuador con su 001, el RUC de Perú y el RUT de Chile con su dígito | Lo ganado se cruza con el contrato y lo firmado con la factura por esa identificación | Ecuador, Perú y Chile |
| Una columna de correo en la exportación | No se procesa | retail-co, tecnologia-co, control-mx |
| La comisión | No se publica en Rostrum: la configuración no lo dice | todas |

## Lo que el material no prueba

- **El CRM de una organización real.** Nada de esto se ha corrido sobre las exportaciones, las
  propuestas o las liquidaciones de una empresa concreta.
- **La extracción del agente.** `evaluar.py` prueba el motor con la ficha correcta, que está en la
  clave. Que el agente lea la propuesta, el acta y la cotización y los registre bien lo prueba la
  ronda con los agentes, sobre este mismo material.
- **Las exportaciones con los nombres de columna en español** de Salesforce, HubSpot, Dynamics y
  Zoho: el material las trae en inglés, como las nombran sus fuentes; en español las dice el mapeo.
- **La exportación de Dynamics por su API**, con los nombres lógicos de cada columna: el lector los
  reconoce (F-06), y el material solo trae la exportación a Excel.
- **Varias monedas en una misma exportación**: cada entidad trae una sola.
- **Los países que no están en el registro**: Brasil, que sí está en la CFO y la CLO, todavía no está
  en el material de la CSO.
