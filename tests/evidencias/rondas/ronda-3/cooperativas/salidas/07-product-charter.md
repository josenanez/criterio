# /criterio-product:product-charter REQ-4300

Escribí el borrador del acta de REQ-4300, pero no creé la ficha del proyecto porque el acta no está firmada. Nadie la firmó, y este comando no firma ni da por firmado.

**Términos.** Ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-15. No registré una aceptación nueva.

**REQ-4300 no pasa la verificación previa.** Nadie podía responder, así que tomé la respuesta sugerida: seguir y marcar cada faltante como vacío, sin rellenarlo.
- **Aceptación:** está aceptado desde 2026-06-05, con doliente Ricardo Salas. El único criterio de aceptación es «se verifica en producción», que no dice qué se mide, así que no es verificable.
- **Demanda:** no hay evidencia. «Quién lo pidió» está vacío y `evidence` está vacío. La única entrevista es de 2025-09-12, tiene 13 meses (el umbral es 12) y no menciona REQ-4300.
- **Título:** el requerimiento se llama «Requerimiento REQ-4300» y ningún documento dice qué pide. Por eso no puedo afirmar que resuelva el problema de los pensionados sin tarjeta débito.
- **Gobierno:** no están dichos el patrocinador, el gerente del proyecto ni su autoridad. Sandra Gil es la gerente del producto, no del proyecto, y no la nombré.
- **Supuesto:** «El proveedor cumple el tiempo pactado» lleva 158 días sin verificar (el umbral es 30). Lo dejé propuesto como riesgo del proyecto, sin doliente. La definición dice que no hay proyectos declarados, así que tampoco hay un proveedor citado en ningún documento.
- **Cifras:** el caso de negocio declara un volumen mensual de 250.670 y el tablero mide 256.871 (2,5 % de diferencia, bajo el umbral de 20 %). Ese volumen es del producto, no de REQ-4300, y el caso no explica de dónde sale para un producto que el segmento aún no tiene.
- **Normativa:** no hice el barrido normativo. Un producto de débito para pensionados toca pagos y datos personales, así que debe correrse antes de firmar.
- **Comité:** en el comité del 2026-10-05 solo asistió Sandra Gil.

Los otros 15 requerimientos quedan fuera del acta por no haberse pedido, no por una decisión del comité.

**Qué sigue.** Sandra Gil debe cerrar los vacíos, sobre todo la demanda y el criterio verificable. Después de la firma, el gerente del proyecto instala `criterio-project` y corre `/pm-setup`.

La corrida quedó registrada como `2026-10-15-product-charter-1`: 38 segundos, 16 requerimientos leídos y 39 señales abiertas en el producto.

Archivos en `estado-producto/PRD-303/corridas/`:
- `salida-product-charter.md`