# /criterio-product:product-requirements 

## Registro — Venta en línea (PRD-300) · al 2026-10-18

Hay 15 requerimientos y los 15 están en estado `aceptado`. El 60% tiene evidencia y ninguno tiene proyecto que lo ejecute. La carpeta de fichas de proyectos (`estado/`) está vacía. Por eso el 0% significa que no hay ninguna traza que confirmar, no que se haya comprobado que nadie lo construye.

En orden de lectura:

1. **Se va a construir y nadie lo pidió (6, sin evidencia):**
   - REQ-4001 (Andrés Lozano)
   - REQ-4003 (Sandra Gil)
   - REQ-4004 (Ricardo Salas)
   - REQ-4009 (Gustavo Neira)
   - REQ-4011 (Paula Céspedes)
   - REQ-4012 (Javier Hoyos)

   La configuración dice que la autoridad es el Comité de producto, así que le toca decidir si se sostienen sin evidencia.
2. **Decidido y nadie lo construye (los 15):** ninguno tiene proyecto asociado. Corresponde `/product-trace`.
3. **Sin criterio de aceptación (4):** REQ-2028, REQ-4000, REQ-4011 y REQ-4013. REQ-4011 también está sin evidencia.
4. **Evidencia vieja (9):** REQ-2028, 4000, 4002, 4005, 4006, 4007, 4008, 4010 y 4013. Lo más nuevo que los sostiene es del 2025-08-30, hace 13 meses (el umbral es 12).
   - Los nueve citan la misma frase, «Lo necesito y hoy no lo tengo». El acta la atribuye a «Cliente entrevistado», sin nombrar al cliente ni vincularla a un requerimiento. Es evidencia genérica repetida, no una por requerimiento.

Lo que no salió:
- **Sin doliente:** no hay ninguno; los 15 tienen una persona.
- **Lleva meses sin decidirse:** no hay ninguno, porque no hay requerimientos propuestos.
- **Decidido sin documento que lo respalde:** `compute` no calcula esta señal, así que no afirmo nada. Hay un solo acta de decisión, la del comité del 2026-10-13, y todas las decisiones son anteriores a ella.
- **Sin dato:** el criterio de éxito de la definición (`success`) y la autoridad (`authority`) no vienen en el estado. `authority` sí está en la configuración.

Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-18, así que no los registré de nuevo.

La salida completa está en `estado-producto/PRD-300/corridas/salida-product-requirements.md`. La corrida quedó registrada como `2026-10-18-product-requirements-1`: 34 hallazgos y 33 segundos medidos.