# /criterio-product:product-spec 

Dejé el borrador de especificación de PRD-301 (Puntos de fidelización), pero sin sección de comportamiento. Los 12 requerimientos aceptados no dicen qué hacen, y rellenarlos con lo razonable habría decidido por el equipo lo que nadie decidió. Es un borrador y lo cierra Beatriz Cuéllar.

Los términos (v1.2) ya estaban vigentes a nombre de José Francisco Ñáñez, 2026-10-23, así que no volví a registrarlos.

**Qué encontré en el registro (17 requerimientos):**
- **Alcance:** 12 están aceptados: REQ-2030, 4100, 4101, 4102, 4103, 4106, 4107, 4109, 4110, 4111, 4112 y 4115. Los otros 5 están propuestos y quedan fuera, porque nadie los decidió.
- **Criterios de aceptación:** 7 dicen solo «se verifica en producción», que no es verificable. Los otros 5 (REQ-4101, 4103, 4106, 4109, 4110) no tienen ninguno.
- **Qué hace cada uno:** ninguno trae su necesidad, y los títulos son marcadores («Requerimiento REQ-xxxx»).
- **Quién decidió:** el campo está vacío en los 12.
- **Proyecto que los ejecuta:** ninguno tiene.
- **Evidencia de demanda:** es una sola ronda de entrevistas del 2025-08-29, con más de 12 meses, y no nombra ningún requerimiento. REQ-2030 y REQ-4115 se aceptaron además sin evidencia ni quién los pidió.
- **Doliente:** REQ-4103 no tiene.
- **Supuesto:** «Las tiendas soportan el volumen» sigue sin verificar y sin dueño. El volumen mensual medido (310.136) está +4,4 % sobre lo declarado en el caso de negocio (297.074), por debajo del umbral de 20 %.
- **Normativa:** el país no consta y no tengo la norma a la vista, así que no cité ninguna. Hay que llevar a revisión jurídica los datos personales, los menores dentro de «Jóvenes» y la protección al consumidor.
- **Siguiente paso:** no ofrezco `/product-charter`, porque los vacíos siguen abiertos y el producto no tiene criterio de éxito.

La corrida quedó registrada como `2026-10-23-product-spec-1` (45 s, 17 requerimientos, 40 hallazgos). Antes de registrarla corrí un `cd` que movió el directorio de trabajo, y por eso usé rutas absolutas en esta última parte.

Archivos en `estado-producto/PRD-301/corridas/`:
- `salida-product-spec.md`