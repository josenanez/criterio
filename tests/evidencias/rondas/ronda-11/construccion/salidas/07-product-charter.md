# /criterio-product:product-charter REQ-4500

Dejé el borrador del acta de REQ-4500 y registré la corrida. No creé la ficha del proyecto porque el acta no está firmada, y no toqué `declared`. Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-22), así que no los volví a registrar.

REQ-4500 pasa las cuatro verificaciones, algunas con mucho que corregir:
- **Aceptado:** sí, en el comité del 2026-10-16.
- **Criterio de aceptación:** dice «se verifica en producción». Indica dónde se verifica, no qué se mide.
- **Evidencia de demanda:** una sola cita anónima de una entrevista del 2026-02-03. El acta del comité la atribuye a REQ-4500, pero la entrevista no nombra ningún requerimiento.
- **Autoridad:** la definición no la declara. Seguí adelante y lo dejé como vacío del acta, como sugería el flujo.

Vacíos principales del acta:
- Falta el patrocinador y la autoridad del gerente del proyecto. No nombré gerente.
- REQ-4500 no tiene título ni necesidad propios.
- No hay criterio de éxito medible.
- El supuesto «La licencia se expide sin objeciones» sigue sin verificar y sin doliente. Pasa al proyecto como riesgo; la fecha en que se declaró (2026-09-06) no cuadra con la del documento (2025-09-25).
- No se identificó ninguna norma sobre la licencia, y no opiné sobre cumplimiento.
- La cifra del caso de negocio (214.841 mensuales) es declarada, no hay serie medida.

En «No entra» puse los otros 14 requerimientos con una razón básica. Los aceptados no se pidieron en esta invocación y los dos propuestos no tienen decisión. Ningún documento declara exclusiones de fondo y no inventé ninguna.

Lo que sigue: alguien con autoridad firma el acta, y el gerente del proyecto instala `criterio-project` y corre `/pm-setup`.

La corrida quedó registrada con 26 hallazgos en 44 segundos.

Archivos en `estado-producto/PRD-305/corridas/`:
- salida-product-charter.md
- 2026-10-22-product-charter-1.md