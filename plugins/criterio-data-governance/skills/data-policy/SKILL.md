---
name: data-policy
description: "La política de datos de la organización en la configuración de las dos agentes: la diferencia que tolera entre una cifra y su fuente, y lo que nunca se procesa. Úsalo en el setup de cada agente, al comparar una cifra con su fuente y cuando la política cambie. Data policy, tolerance, retention."
---

# La política de datos

**Las tolerancias, los umbrales y los plazos los fija la organización.** Salen de su política de datos y de su política de conservación, en `00-referencia/`. Si la política no trae un valor, **no se inventa**: se le pregunta a la persona y se registra su respuesta con la fecha.

| Valor | Dónde va | Lo usa |
|---|---|---|
| La diferencia, en porcentaje, que se tolera entre una cifra de un informe y la de su fuente al mismo corte | `methodology.tolerance_pct` de la configuración, por ejemplo `0.5` | Ariadna |
| El plazo de conservación de cada tipo de dato, en meses | la ficha de Custodia, `retention[]`, con la cita de la política | Custodia |
| La fecha de revisión de cada política | la ficha de Custodia, `policies[]`, con la cita | Custodia |
| El umbral de cada regla de calidad | la tabla de reglas de `30-calidad/` | Ariadna |

## Lo que viene de fuera

Las áreas de la gestión de datos son las de DAMA-DMBOK (F-01): Custodia trabaja el gobierno de los datos; Ariadna, la calidad y los metadatos con el linaje. En una entidad financiera, la cifra de riesgo que llega a la junta se contrasta como piden los principios de BCBS 239 (F-02): exacta, completa y oportuna. La característica de calidad con que se escribe una regla es la de ISO/IEC 25012 (F-03). Se citan por su nombre, nunca por su texto.

**Lo que exige la ley de cada país sobre el registro de bases de datos personales está por verificar, país por país**: mientras tanto, Custodia compara el catálogo con el registro que lleva la organización, y lo dice así.
