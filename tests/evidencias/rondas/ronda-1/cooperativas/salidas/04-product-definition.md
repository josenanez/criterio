# /criterio-product:product-definition 

La definición de Crédito de libranza (PRD-300) casi no tiene evidencia que la sostenga, y no hay nada que la contradiga. Los términos 1.0 ya estaban aceptados por José Francisco Ñáñez el 2026-10-14. No hubo preguntas que responder.

- **Contradicciones:** ninguna. La única evidencia de demanda es una frase de un cliente sin nombre, del 2025-10-11: «Lo necesito y hoy no lo tengo». Sostiene una necesidad de ese cliente, no que el segmento no tenga oferta. Es débil, y con 12 meses y 3 días ya pasó el umbral de 12 meses.
- **Cifras:** el volumen mensual de 211.347 y el «retorno esperado en 24 meses» no tienen serie medida. `metrics/` está vacío. El volumen se cita a sí mismo como fuente, y el retorno no trae cifra ni base de cálculo.
- **Supuesto del proveedor:** «El proveedor cumple el tiempo pactado» figura como «verificado», pero ningún documento muestra la verificación. Lleva 41 días desde su declaración (2026-09-03); lo calculé yo restando fechas, porque `compute` no lo dio.
- **No está dicho en ninguna parte:**
  - El éxito, el proveedor, la «propuesta principal», quiénes son los asociados urbanos y cuántos son.
  - El origen del volumen y el retorno.
  - Qué proyecto construye el producto.
  - Qué plan «se mantiene».
- **Normativa:** listé los frentes que toca (crédito de libranza, consumidor financiero, datos personales, retención de información). Cada uno está en estado «no tengo la norma a la vista», porque ningún documento cita norma ni fija el país. No cité ninguna de memoria.
- **Para cerrar la definición:** falta el criterio de éxito. Por eso no ofrezco `/product-charter`. Sí ofrezco convertir el supuesto del proveedor y el volumen en riesgos con doliente.

`compute` salió vacío porque `producto.json` está sin poblar, no tiene requerimientos y `metrics/` está vacío. Por eso `compute` marca como desconocidos problema, para quién, éxito y autoridad, aunque el texto de la definición sí enuncia un problema y un segmento.

La definición lleva fecha 2026-05-09, pero trae un supuesto declarado el 2026-09-03.

Registré la corrida como `2026-10-14-product-definition-1`, con 0 hallazgos y 33 segundos. La salida completa está en `estado/PRD-300/corridas/salida-product-definition.md`.