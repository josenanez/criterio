---
name: forecast-backing
description: "Cómo calcula el motor el respaldo del pronóstico —lo cerrado más lo ponderado por etapa con evidencia— y la meta prorrateada por los días del periodo, y por qué nunca se compara a las personas. Úsalo al explicar el reporte del pronóstico o el de la meta, o cuando alguien pide el detalle por vendedor. Weighted forecast, target pacing."
---

# El pronóstico y la meta

## El respaldo del pronóstico

Lo comprometido es el `declared_forecast` de la ficha. El respaldo es lo que lo sostiene en los documentos:

- **Lo cerrado**: las oportunidades ganadas con fecha de cierre en el periodo, hasta la fecha de corte, por su monto.
- **Lo ponderado con evidencia**: las oportunidades abiertas que cierran en el periodo y tienen todos los documentos que exige su etapa, cada una por su monto por la probabilidad de su etapa en la tabla de etapas.

**Lo ponderado sin evidencia se muestra aparte y no sostiene nada**: una oportunidad en negociación sin propuesta en la ficha pesa en el CRM, no en el respaldo.

`forecast_unsupported` se levanta cuando lo comprometido supera el respaldo en más de `thresholds.forecast_tolerance_pct` (10 % por omisión). Comprometer menos que el respaldo no es una señal.

## La meta al corte

La meta del periodo de `00-referencia/metas` se prorratea por los días transcurridos: al día 20 de un mes de 31, lo esperado es 20/31 de la meta. `target_vs_closed` se levanta cuando lo cerrado se aparta de lo esperado en más de `thresholds.target_threshold_pct` (15 % por omisión), hacia arriba o hacia abajo. Si la meta trae `linea`, se compara por línea.

## Nunca por persona

El pronóstico y la meta se miran por periodo y por línea, **nunca por vendedor**. Si alguien pide el detalle por persona, dilo y no lo armes: comparar a las personas del equipo es algo que esta familia no hace (ADR 0019). La señal es de la oportunidad, no de quien la lleva.

## Lo que el motor no hace

- No corrige la probabilidad de una etapa: la dice la tabla de la organización.
- No propone un pronóstico ni una meta: los dos son de una persona.
