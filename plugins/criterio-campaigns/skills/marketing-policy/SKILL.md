---
name: marketing-policy
description: "La política de publicidad de la organización en la configuración de los dos agentes: la tolerancia sobre el presupuesto de una campaña, la diferencia que se tolera entre un resultado y la plataforma, quién aprueba cada pieza y lo que nunca se decide. Úsalo en el setup de cada agente y cuando la política cambie. Advertising policy, tolerances, approval."
---
<!-- COPIA · la fuente es plugins/criterio-claims/skills/marketing-policy/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# La política de publicidad en la configuración

**Las tolerancias, las metas y quién aprueba cada pieza los fija la organización** en su política de publicidad, en `00-politica/`. Si la política no trae un valor, **no se inventa**: se le pregunta a la persona y se registra su respuesta con la fecha.

| Valor | Dónde va | Lo usa |
|---|---|---|
| El porcentaje que se tolera por encima del presupuesto de una campaña | `methodology.budget_tolerance_pct` de la configuración, por ejemplo `5` | Próspero |
| La diferencia, en porcentaje, que se tolera entre un resultado reportado y la plataforma al mismo corte | `methodology.result_tolerance_pct`, por ejemplo `2` | Próspero |
| El presupuesto, la meta, el indicador, las fechas y la base de contactos de cada campaña | el plan de mercadeo de `50-campanas/` | Próspero, Lucía |
| Quién aprobó cada pieza y cuándo | el registro de piezas de `10-piezas/` | Lucía |
| La autorización para mercadeo de cada base | el registro de bases de `40-bases/` | Lucía |

## Lo que nunca se decide

Ningún agente aprueba una pieza, juzga la creatividad, dice si una afirmación es verdadera, aprueba un presupuesto ni decide cuál de dos cifras es la correcta. Dicen qué falta y con qué cita; la decisión es del área de mercadeo, de legal y de quien firma el informe.

## Lo que viene de fuera

El soporte de lo que se afirma, la identificación de la publicidad y los testimonios de los influenciadores son los del Código de Publicidad y Comunicaciones de Mercadeo de la ICC (F-01); el resultado de una campaña contra su medición, el de los estándares de resultados y calidad de datos del MRC (F-02). En una entidad de Colombia, lo que se anuncia obliga a quien lo anuncia y una promoción informa sus condiciones de tiempo, modo y lugar, por el Estatuto del Consumidor (F-10). Se citan por su nombre y sus artículos, nunca por su texto. La ley de publicidad de los demás países está por verificar, y no sostiene ninguna señal.
