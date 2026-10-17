# /criterio-product:product-charter REQ-4100

Dejé el borrador del acta de REQ-4100 (Alerta de taludes, PRD-301). No creé la ficha del proyecto: el acta no está firmada y la ficha se crea después de la firma. No corrí `portafolio.py init`.

Los términos (v1.1, familia 0.3.13) ya estaban vigentes a nombre de José Francisco Ñáñez, con fecha 2026-10-17. No hubo que registrarlos otra vez.

REQ-4100 está aceptado, pero le faltan varias cosas. Seguí adelante con ellas marcadas como vacíos del acta, como pide el comando, y no las rellené:
- **Autoridad:** ningún documento dice quién decide. El producto trae "Comité de producto" solo como propuesta por defecto.
- **Doliente:** el acta del comité dice "sin asignar".
- **Criterio de aceptación:** dice "se verifica en producción", que no se puede medir.
- **Evidencia de demanda:** es una sola cita anónima de un "Cliente entrevistado". La entrevista no nombra el requerimiento y ya pasó el umbral de 12 meses.
- **Definición:** la "Propuesta principal" no tiene texto y no hay criterio de éxito del producto.
- **Supuesto:** "La red de la mina soporta el volumen" lleva 58 días sin verificar (el umbral es 30). Pasa al proyecto como riesgo, pero hoy no tiene doliente.
- **Patrocinador, presupuesto, hitos y proyecto que lo ejecuta:** no están dichos en ningún documento.
- **Alcance y normativa:** esta acta cubre solo REQ-4100. Los otros 16 requerimientos del acta quedan fuera, con la razón por cada uno. No hice barrido normativo.

Siguiente paso: alguien con autoridad sobre el producto firma el acta y se nombra al gerente del proyecto. Ese gerente instala `criterio-project` y corre `/pm-setup`.

La corrida quedó registrada como `2026-10-17-product-charter-1` (41 s, 39 hallazgos).

Archivos en `/home/claude/banco/ronda-7/mineria/espacio/estado-producto/PRD-301/corridas/`:
- `salida-product-charter.md` (el borrador completo)