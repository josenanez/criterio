---
name: risk-policy
description: "Los plazos del marco de apetito de la organización en la configuración de los dos agentes: los días para reportar la exposición, cada cuánto revisa la junta la declaración, los días para registrar un evento y la ventana de los eventos repetidos; y lo que nunca se decide. Úsalo en el setup de cada agente y cuando el marco cambie. Risk appetite framework, deadlines."
---
<!-- COPIA · la fuente es plugins/criterio-risk-appetite/skills/risk-policy/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# El marco de apetito en la configuración

**El apetito, los límites, los umbrales y los plazos los fija la organización** en su marco de apetito y en su política de riesgo operacional, en `00-marco/`. Si el documento no trae un valor, **no se inventa**: se le pregunta a la persona y se registra su respuesta con la fecha.

| Valor | Dónde va | Lo usa |
|---|---|---|
| Los días después del cierre del periodo que tienen las áreas para reportar su exposición | `methodology.report_days` de la configuración, por ejemplo `10` | Severo |
| Cada cuántos meses revisa la junta la declaración de apetito | `methodology.statement_review_months`, por ejemplo `12` | Severo |
| Los días para registrar un evento de pérdida desde que se descubre | `methodology.registration_days`, por ejemplo `30` | Casandra |
| La ventana, en meses, en que dos eventos del mismo tipo en el mismo proceso cuentan como repetidos | `methodology.repeat_window_months`, por ejemplo `12` | Casandra |
| Cada límite, su sentido, su dueño y su fecha de revisión | la tabla de límites de `00-marco/` | Severo |
| Los umbrales de alerta y de límite de cada indicador clave | la tabla de indicadores de `00-marco/` | Casandra |

El periodo de la configuración es **el último periodo cerrado**: el de la exposición que reportaron las áreas y el de los valores de los indicadores.

## Lo que nunca se decide

Ningún agente fija ni cambia un límite, aprueba un exceso, acepta un riesgo, califica un riesgo en la matriz ni cierra un evento. Dicen qué está fuera y con qué cita; la decisión es de la junta, del comité de riesgos y de las áreas. Tampoco calculan capital, valor en riesgo ni pérdida esperada: procesan las cifras que la organización ya reporta.

## Lo que viene de fuera

El proceso de la gestión del riesgo —identificar, analizar, tratar, hacer seguimiento y reportar— es el de ISO 31000 (F-01), y se cita por su nombre, nunca por su texto. En una entidad vigilada se cita la norma de su país: el Sistema Integral de Administración de Riesgos de la Superintendencia Financiera en Colombia (F-10), la Resolución SBS 272-2017 en el Perú (F-11) y la Resolución CMN 4.557 en Brasil (F-12). Fuera del sector financiero, la familia sirve a cualquier organización con un marco de apetito, y no cita ninguna norma de supervisión.
