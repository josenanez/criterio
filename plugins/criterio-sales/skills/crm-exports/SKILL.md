---
name: crm-exports
description: "Cómo se procesa cada exportación del CRM: Salesforce por el nombre de cada campo o su etiqueta, HubSpot por la etiqueta de cada propiedad, Dynamics 365 Sales por la etiqueta o el nombre lógico de cada columna, Zoho CRM por la etiqueta de cada campo, y cualquier otro en CSV o Excel con su mapeo de columnas; la fecha de la exportación, la tabla de etapas y el historial de la fecha de cierre. Úsalo al configurar el CRM, cuando una exportación no se reconoce o le faltan columnas, o al explicar cómo se cuentan los cierres que se corren. CRM exports, Salesforce, HubSpot, Dynamics 365, Zoho, column mapping."
---

# Las exportaciones del CRM

**Ningún agente se conecta al CRM.** Procesa lo que el CRM exporta, en `10-crm/`, con la fecha de la exportación en el nombre (`oportunidades-2026-10-15.csv`). Cada exportación es un corte del embudo: el motor compara cada corte con el anterior para decir qué cambió, cuántas veces se corrió cada cierre y desde cuándo no se mueve una oportunidad. **Se guardan todas**, no solo la última.

## Cómo reconoce el motor cada formato

| CRM | Cómo lo reconoce | Qué procesa | La fuente |
|---|---|---|---|
| **Salesforce** | Las columnas `StageName` y `CloseDate` (la exportación por API o Data Loader) o `Stage` y `Close Date` (un informe) | `Id`, `Name`, `AccountId`, `Amount`, `CloseDate`, `StageName`, `Probability`, `ForecastCategoryName`, `IsClosed`, `IsWon`, `LastActivityDate`, `OwnerId`, `CreatedDate`, `CurrencyIsoCode`, por su nombre o por su etiqueta | F-02 |
| **Salesforce, el historial** | Las columnas `Field`, `OldValue` y `NewValue` | Las filas con `Field` = `CloseDate`: cada vez que la fecha nueva es posterior a la anterior, es una vez que se corrió | F-03 |
| **HubSpot** | Las columnas `Record ID` y `Deal Stage` | `Record ID`, `Deal Name`, `Deal Stage`, `Pipeline`, `Amount`, `Close Date`, `Deal owner`, `Create Date`, `Last Activity Date`, `Deal probability`, `Forecast category`, `Currency` | F-04 |
| **Dynamics 365 Sales** | La columna de la fecha estimada de cierre: `Est. close date` (la exportación a Excel de una vista) o `estimatedclosedate` (la API) | `opportunityid`, `name`, `parentaccountid`, `estimatedvalue`, `estimatedclosedate`, `stepname`, `statecode`, `closeprobability`, `msdyn_forecastcategory`, `ownerid`, `transactioncurrencyid`, por su nombre lógico o por su etiqueta (`Topic`, `Account`, `Est. revenue`, `Pipeline Phase`, `Status`…) | F-06, F-07 |
| **Zoho CRM** | Las columnas `Deal Name` y `Closing Date` | `Record ID`, `Deal Name`, `Account Name`, `Amount`, `Closing Date`, `Stage`, `Probability`, `Deal Owner` | F-08, F-09 |
| **Cualquier otro** | Ninguna de las anteriores | Las columnas en español más comunes —`id`, `nombre`, `cuenta`, `etapa`, `monto`, `cierre`, `responsable`, `ultima_actividad`, `linea`— y lo que diga el mapeo | — |

Las fuentes, con su versión y su fecha de consulta, en `families/criterio-cco/FUENTES.es.md`. Un campo que no esté ahí verificado no se procesa.

**Cuatro datos son obligatorios** en cualquier formato: el id de la oportunidad, la etapa, el monto y la fecha de cierre. Sin uno de ellos la exportación no se procesa, y el motor dice cuál falta.

## El mapeo de columnas

`crm.columns` en la configuración dice qué columna trae cada dato cuando el motor no la reconoce. Manda sobre todo lo demás:

```json
"crm": {"format": "hubspot", "date_order": "dmy",
        "columns": {"cuenta": "Associated Company", "linea": "Línea de negocio"}}
```

- **HubSpot no fija el nombre de la columna de la empresa asociada** (F-05): sale en su propia columna, con un nombre que depende de la exportación. Pregúntale a la persona cuál es y regístralo en `cuenta`.
- **En Dynamics, el estado manda sobre la etapa**: `Status` (statecode) dice si la oportunidad está abierta (`Open`), ganada (`Won`) o perdida (`Lost`) (F-06); la etapa es la fase del proceso de la entidad, `Pipeline Phase`, y va en la tabla de etapas como cualquier otra. La exportación a Excel trae la fecha como fecha y el monto como número, sin símbolo (F-07).
- **En Zoho, la última actividad no es un campo estándar** (F-08): si la exportación la trae, pregúntale a la persona cuál es la columna y regístrala en `ultima_actividad`. Si no la trae, el motor toma el último corte en que la oportunidad cambió.
- **La línea de negocio** no es un campo estándar de ningún CRM: si las metas o el plan de comisiones van por línea, la columna que la trae va en `linea`.
- Los nombres se comparan sin tildes ni mayúsculas.

`ventas.py exportacion --config <config> --file <archivo>` dice el formato que reconoció, las columnas que faltan y cuántas filas procesó, sin calcular nada.

## Las fechas

Un informe de Salesforce exporta las fechas en el formato de quien lo exporta: `10/20/2026` o `20/10/2026`. Si alguna fecha de la columna lo resuelve —un número mayor que 12— el motor usa ese orden; si ninguna lo resuelve, el de `crm.date_order` (`dmy` o `mdy`). Pregúntalo en el setup si la primera exportación no lo resuelve.

## La tabla de etapas

Cada etapa del CRM tiene una fila en `00-referencia/etapas`: su orden, su probabilidad, si es `abierta`, `ganada` o `perdida`, y el documento que exige. **Una etapa exige también lo que exigen las anteriores**: una oportunidad en negociación necesita la propuesta que exigió la etapa de propuesta. Una etapa de la exportación que no está en la tabla se reporta como no procesada.

Si la exportación de Salesforce trae `IsWon` e `IsClosed`, mandan sobre el tipo de la tabla.

## La última actividad

La dice el CRM —`LastActivityDate` en Salesforce, `Last Activity Date` en HubSpot, la columna que diga el mapeo en Zoho—. Si la exportación no la trae, el motor toma el último corte en que la oportunidad cambió de etapa, de monto o de fecha de cierre: con un solo corte eso subestima los días, y nunca los inventa.
