# /criterio-product:product-charter REQ-4800

El borrador del acta de REQ-4800 (producto PRD-308, Permisos de trabajo digitales) está escrito, pero no se creó la ficha del proyecto. El acta necesita una firma y todavía no tiene quien firme, porque el documento no nombra patrocinador. Tampoco se escribió el estado declarado.

Los términos vigentes (v1.1) ya estaban aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-18, así que no registré nada nuevo.

REQ-4800 está aceptado, pero le faltan varias cosas, y el acta las marca como vacíos en vez de rellenarlas:
- **Necesidad:** no está descrita. El título es genérico y la propuesta de la definición es texto de relleno.
- **Criterio de éxito:** el único criterio es «se verifica en producción», sin métrica, umbral ni responsable. La definición del producto tampoco declara criterio de éxito.
- **Evidencia de demanda:** es una sola entrevista con un cliente, del 2025-09-27. No menciona REQ-4800 y tiene 12 meses y 3 semanas, por encima del umbral de 12 meses.
- **Gobierno:**
  - No se nombra patrocinador.
  - Javier Hoyos es gerente de producto, no consta como gerente de proyecto.
  - La autoridad del gerente del proyecto no está declarada.
  - La autoridad del producto («Comité de producto») es un valor por defecto de la instalación, no algo que diga un documento.
- **Presupuesto e hitos:** no están declarados en ningún documento.
- **Barrido normativo:** no se hizo, y el acta no opina sobre cumplimiento.

El acta lleva dos supuestos que pasan al proyecto como riesgos, ambos sin doliente:
- **«Operaciones adopta la herramienta»:** su verificación cita una entrevista con doce clientes que no está en `10-descubrimiento`. Además, el segmento del producto es Supervisores, no Operaciones.
- **Volumen mensual de 98.890:** su única fuente es el propio caso de negocio.

En «No entra» están los otros 11 requerimientos. Para los tres que siguen propuestos, la razón es que no están aceptados. Para los ocho aceptados, ningún documento da la razón, así que la dejé a quien firme.

Cuando el acta esté firmada, se crea la ficha con `portafolio.py init`. Su gerente instala `criterio-project` y corre primero `/pm-setup`.

La corrida quedó registrada como `2026-10-18-product-charter-1` (51 segundos, 30 hallazgos sobre los 12 requerimientos).

Archivos en `/home/claude/banco/ronda-10/mineria/espacio/estado-producto/PRD-308/corridas/`:
- `salida-product-charter.md`