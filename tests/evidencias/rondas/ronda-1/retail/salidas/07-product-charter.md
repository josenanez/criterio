# /criterio-product:product-charter REQ-1010

Dejé el borrador del acta de REQ-1010, pero no está lista para firmar: tiene ocho vacíos y no creé la ficha del proyecto.

Los términos ya constaban aceptados por José Francisco Ñáñez (versión 1.0, 2026-10-14). Ante cada pregunta tomé la respuesta sugerida: seguir y marcar el vacío sin rellenarlo.

**Qué encontré sobre REQ-1010**
- **Aceptado:** sí, desde 2026-03-28, según el acta del comité del 2026-10-14. El doliente es Felipe Arango.
- **Criterio de aceptación:** no es verificable. Solo dice «se verifica en producción».
- **Demanda:** una única cita anónima («Cliente entrevistado») del 2025-10-02, de hace más de 12 meses. No menciona REQ-1010.
- **Autoridad del gerente:** la definición no dice qué puede decidir el gerente. La configuración solo da como autoridad del producto al Comité de producto.
- **Requerimiento mismo:** el registro de requerimientos está vacío. REQ-1010 solo existe como una fila del acta de comité, sin texto ni título propio.

**Qué más quedó marcado como vacío**
- No hay criterio de éxito del producto, ni patrocinador, ni presupuesto, ni hitos.
- Un programa de puntos probablemente toca datos personales, pero no hice barrido normativo y no cité ninguna norma.
- El supuesto «el proveedor cumple» figura como verificado sin decir cómo.
- La cifra de volumen mensual (200.866) es solo declarada.
- Los tres últimos pasan al proyecto como riesgos, con doliente por asignar.
- REQ-1011 y REQ-1012 quedan fuera del alcance por defecto, porque el argumento solo pidió REQ-1010. Esa exclusión no es un juicio sobre su valor.

**Lo que no hice**
- No nombré gerente del proyecto.
- No ejecuté `portafolio.py init`, porque no hay firma. Tampoco escribí ningún estado declarado.
- El siguiente paso es que el gerente del proyecto instale `criterio-project` y corra `/pm-setup`, una vez firmada el acta.

La corrida quedó registrada como `2026-10-14-product-charter-1`.

Archivos en `.criterio/producto/PRD-301/estado/corridas/`:
- `salida-product-charter.md`