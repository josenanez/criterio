# /criterio-product:product-requirements 

## Registro — Trazabilidad (PRD-304) · al 2026-10-17

Hay 16 requerimientos: 11 aceptados y 5 propuestos. El registro tiene 40 hallazgos en 6 señales. La corrida quedó registrada como `2026-10-17-product-requirements-1`, y el resultado completo está en `estado-producto/PRD-304/corridas/salida-product-requirements.md`.

Los términos ya estaban vigentes (versión 0.3.13, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrarlos de nuevo.

Las cifras que salen del cálculo:

- **81.8% de lo decidido tiene evidencia** (9 de 11). Pero es una sola cita genérica de un cliente entrevistado, del 2025-10-15. La propia nota del registro dice que la entrevista no nombra ninguno de estos requerimientos.
- **0% tiene proyecto que lo ejecute.** Es «no se pudo confirmar», no «nadie lo construye»: la carpeta de fichas de proyecto (`estado/`) está vacía.
- **Se va a construir y nadie lo pidió:** REQ-4401 y REQ-4414 están aceptados sin ninguna cita de quien los pidió.
- **Sin doliente:** REQ-4400, REQ-4414 y REQ-4405. Andrés Lozano, como gerente del producto, designaría a la persona.
- **Sin criterio de aceptación (aceptados):** REQ-4400, REQ-4402, REQ-4404, REQ-4410 y REQ-4414.
- **Quién decidió:** el campo está vacío en los 11 aceptados. Todos citan el acta del comité del 2026-09-16, pero sus decisiones son de abril a agosto, así que el acta las registró después.
- **Lleva meses y nadie lo decide** (umbral de 60 días): REQ-4415 (178 días), REQ-4408 (143), REQ-4405 (140), REQ-4411 (95) y REQ-4407 (71). Quien tiene la facultad es el Comité de producto. Propongo decidirlos en el próximo comité mensual, no cerrarlos por viejos.
- **Evidencia vieja** (umbral de 12 meses): 14 requerimientos, todos con esa misma cita del 2025-10-15.

El caso de negocio declara un `volumen_mensual` de 240425 sin medición que lo contraste, y no trae cifra de `retorno_esperado`.

Para seguir, `/product-trace` necesita las fichas de los proyectos. Todavía no aplica `/product-charter`: ningún aceptado tiene a la vez doliente, criterio y evidencia propia.