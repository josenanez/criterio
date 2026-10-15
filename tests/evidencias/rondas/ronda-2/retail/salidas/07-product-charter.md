# /criterio-product:product-charter REQ-1030

Redacté el borrador del acta de REQ-1030 (Pago con QR, PRD-303). Es un borrador sin firma, así que no creé la ficha del proyecto.

Los términos (v1.1) ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez el 2026-10-15, así que no los volví a registrar.

**Lo que encontré al verificar los requisitos.** REQ-1030 sí está aceptado, desde 2026-08-13, pero tres de las cuatro condiciones quedan flojas o vacías:
- **Criterio de aceptación:** dice «se verifica en producción», que no es verificable porque no señala qué se mide ni con qué umbral.
- **Evidencia de demanda:** es débil. Viene de una sola entrevista de 2025-09-29, de un cliente sin nombre, y tiene 381 días.
- **Autoridad del gerente:** falta en la configuración y en la definición.

No había nadie para decidir, así que tomé la respuesta sugerida: seguir y marcar cada falta como vacío del acta, sin rellenarla.

**El borrador.**
- **Entra:** solo REQ-1030, cuyo doliente es Felipe Arango.
- **No entra:** REQ-1031, REQ-1032, REQ-2017 y REQ-2025. Los dejé fuera por selección (el argumento era solo REQ-1030), no porque alguien lo decidiera; quien firme debe confirmarlo.
- **Supuesto que pasa a riesgo:** «La demanda se sostiene sin descuento», con 212 días sin verificar. No tiene doliente asignado.
- **Normativa:** señalé cuatro materias que van a revisión jurídica: pagos con QR, datos personales, consumidor financiero y retención de transacciones. No hay norma a la vista y el país no consta.
- **Vacíos:**
  - Patrocinador y gerente de proyecto: no están dichos. María Restrepo es gerente del producto, no consta como gerente de proyecto, y no la propuse.
  - Criterio de éxito y propuesta (qué se construye).
  - Necesidad propia de REQ-1030.
  - Presupuesto e hitos.

**Quién sigue.** Cuando el acta tenga firma y gerente, ese gerente instala `criterio-project` y corre `/pm-setup`. Después, `/product-trace` podrá confirmar la traza contra su ficha. La ficha se crea entonces con `PRD-303` como producto y con `declared` vacío por diseño.

La corrida quedó registrada como `2026-10-15-product-charter-1`, con 8 hallazgos. El texto completo está en `estado-producto/PRD-303/corridas/salida-product-charter.md`.