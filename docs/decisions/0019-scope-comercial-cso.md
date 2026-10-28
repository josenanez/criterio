# 0019 · El alcance se amplía a la función comercial (CSO)

**Fecha:** 2026-10-28 · **Estado:** aceptada el 2026-10-28 · **Modifica:** 0012

## Contexto

La función comercial es la primera familia de la capa de negocio del mapa de la página de Agentes.
Se eligió antes que mercadeo (CMO) por tres razones:

- **Vive en documentos:** las exportaciones del CRM, las propuestas, las órdenes de compra, los
  contratos firmados, la lista de precios, la matriz de descuentos y el plan de comisiones. Mercadeo
  vive sobre todo en plataformas de pauta y tableros.
- **Cruza familias:** lo vendido contra lo firmado (Fidel, en la CLO) y contra lo facturado (Clara,
  en la CFO). Es la vista que justifica una sola plataforma y un solo Rostrum.
- **Mercadeo se apoya en ella después:** la campaña contra su resultado medido termina en las
  oportunidades y los cierres que esta familia ya tendrá en su ficha.

**El rol se define desde O\*NET**, la clasificación de ocupaciones del Departamento de Trabajo de los
Estados Unidos: la ocupación 11-2022.00 (*Sales Managers*), con 19 tareas, consultada el 28 de
octubre de 2026 ([onetonline.org](https://www.onetonline.org/link/summary/11-2022.00)). Las que esta
familia toma:

- revisar los registros y los informes de la operación para proyectar las ventas y la rentabilidad;
- establecer y vigilar las metas de venta del equipo;
- fijar la lista de precios y las tasas de descuento;
- dirigir y revisar los registros de las ventas;
- preparar el presupuesto comercial.

Cumple las cuatro condiciones de las 0006 y 0009:

- **Trabajo recurrente sobre documentos:** el pronóstico de cada semana y de cada mes, el comité
  comercial, la revisión de descuentos y la liquidación de comisiones.
- **Una brecha entre lo declarado y lo escrito:** la oportunidad que el CRM pone en una etapa y que
  ningún documento sostiene, o el negocio ganado sin contrato firmado.
- **Plazos y montos que calcula el código:** los días sin actividad, las fechas de cierre que se
  corren, el pronóstico ponderado y el descuento contra su tope.
- **Una persona que decide:** el pronóstico que se compromete, el descuento que se aprueba y la meta
  son del responsable comercial.

## Decisión

**Una familia de dos agentes**, que comparten el núcleo común, el calendario y la ficha de la
oportunidad:

- **El pronóstico:** el embudo contra su evidencia y el pronóstico contra lo que lo sostiene.
- **De la venta a la factura:** el precio y el descuento contra su política, y lo ganado contra lo
  firmado y lo facturado, con las fichas de la CLO y la CFO.

| Lo que calcula el código | Cuándo se levanta |
|---|---|
| Etapa sin evidencia | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra |
| Oportunidad detenida | Una oportunidad abierta no tiene actividad registrada en los días configurados |
| Cierre que se corre | La fecha de cierre de una oportunidad se movió más veces de las configuradas |
| Pronóstico sin respaldo | Lo comprometido supera lo que suman las oportunidades con evidencia, ponderadas por su etapa |
| Meta contra lo cerrado | Lo cerrado al corte se aparta de la meta del periodo más del umbral |
| Descuento fuera de política | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz |
| Ganado sin contrato | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel |
| Firmado sin factura | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación |
| Comisión distinta del plan | La comisión liquidada no es la que da el plan sobre lo cerrado y facturado |

**Nunca:**

- escribe ni cambia nada en el CRM;
- contacta a un cliente;
- aprueba un descuento o una excepción de precio;
- fija ni cambia una meta;
- califica o compara a las personas del equipo: dice qué oportunidad no tiene evidencia, no quién
  vende mejor.

## Reglas para la operación real

- **Procesa exportaciones, nunca sistemas.** Las oportunidades, la actividad y los contactos llegan
  como archivos exportados del CRM; no se conecta a ninguno.
- **Los datos de contacto de los clientes no entran a la ficha.** La ficha guarda la cuenta y la
  oportunidad, no el correo ni el teléfono de una persona.
- **Las comisiones no se publican en Rostrum por omisión.** Son la remuneración de personas
  identificables; se publican solo si la configuración lo dice.
- **Lo que cruza familias va por las fichas.** El contrato lo dice la ficha de Fidel y la factura la de
  Clara; esta familia no los vuelve a procesar.

## Lo que cuesta hoy

Son cifras de terceros, verificadas contra el texto de quien las publica el 28 de octubre de 2026.

| Cifra | Fuente | Muestra | Estado |
|---|---|---|---|
| **4 de cada 5** líderes de ventas y de finanzas no acertaron al menos un pronóstico trimestral de ventas en el último año; el **52 %** de los líderes de ventas dice que su pronóstico se desvía un 10 % o más | Xactly con Regina Corso Consulting, 2024 Sales Forecasting Benchmark Report ([informe](https://www.xactlycorp.com/sites/default/files/file/2024-07/2024_sales_forecasting_benchmark_report.pdf)) | 405 profesionales de ventas, finanzas y operaciones de ingresos en Norteamérica, del 19 al 28 de marzo de 2024 | Verificada |
| **28 %** de su semana dedica un vendedor a vender; el 72 % se va en otras tareas, sobre todo gestionar los negocios y capturar datos | Salesforce, State of Sales, quinta edición ([nota](https://www.salesforce.com/news/stories/sales-research-2023/)) | 7.775 profesionales de ventas en 38 países de Norteamérica, América Latina, Asia-Pacífico y Europa, del 24 de agosto al 30 de septiembre de 2022 | Verificada |
| **84 %** de los líderes de ventas dice que la analítica comercial influyó menos de lo esperado en el desempeño; el 44 % señala la mala calidad de los datos | Gartner ([comunicado](https://www.gartner.com/en/newsroom/press-releases/2024-02-06-gartner-survey-finds-sales-analytics-has-less-influence-on-sales-performance-than-what-leadership-expected)) | 303 líderes de ventas, julio de 2023 | Verificada |

## Lo que falta decidir

1. El nombre de cada agente.
2. Qué exportaciones de CRM entran primero: Salesforce, HubSpot, Microsoft Dynamics o Zoho.
3. Si la liquidación de comisiones entra en el primer incremento o en el segundo.
4. En qué países se prueba primero, con la identificación y la factura de cada uno que ya están en
   el registro de países.
