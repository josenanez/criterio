# /criterio-product:product-wake 

## Tarjeta de crédito digital (PRD-304) · 2026-10-18

Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-18), así que no los registré de nuevo.

Toca la revisión del registro (`review`). Es la primera corrida y no hay corte anterior, así que no puedo separar lo que cruzó un umbral desde entonces. Todo lo de abajo es la línea base, y desde la próxima corrida solo reportaré lo nuevo.

**Necesita decisión del Comité de producto**
- **REQ-4401** lleva 65 días sin decidirse (umbral 60). Su doliente es Carlos Peña y la facultad es del Comité de producto. Falta llevarlo al comité.
- **Sin criterio de aceptación:** REQ-4400, REQ-4412 y REQ-4414, ya aceptados.
- **Sin doliente:** REQ-4407 y REQ-4408, ya aceptados.
- **Aceptados sin evidencia de demanda:** REQ-2038, 4402, 4409, 4410 y 4413.

**Evidencia que se queda sin sustento**
- **13 requerimientos** se apoyan en la entrevista del 2025-10-03, que cumple 12 meses (umbral 12) y no nombra ninguno de ellos.
- **Qué se queda sin sustento:** la afirmación de la definición de que Personas no tiene tarjeta de crédito digital.

**Trazas**
- **Sin proyecto:** 17 de 17 requerimientos aceptados no tienen proyecto asignado. No hay trazas que confirmar.

**Definición**
- **Declarado contra medido:** el volumen mensual declarado es 263.889 y el medido es 272.644, una brecha de 3,3 % (umbral 20 %). No hay contradicción.
- **Criterio de éxito:** no está dicho en ninguna parte.

**Lo que no sé**
- **Fichas:** la ruta de fichas de la configuración (`estado`) hace fallar `compute`, porque mezcla archivos que no son fichas. Usé `estado/records`, que sí las tiene. Conviene corregir la configuración.
- **Documentos:** no releí ninguno, así que las cifras salen del registro ya construido.

**Registro:** dejé constancia de la revisión y escribí el corte `2026-10-18`. La corrida `2026-10-18-product-wake-1` quedó registrada con 41 hallazgos sobre 18 requerimientos, en 35 s. Lo que mostré está en `estado-producto/PRD-304/corridas/salida-product-wake.md`.

**Vuelvo el 2026-11-17.**