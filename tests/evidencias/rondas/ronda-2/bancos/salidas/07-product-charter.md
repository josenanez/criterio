# /criterio-product:product-charter REQ-1030

Dejé el borrador del acta de REQ-1030 (Cuenta PyME, PRD-303) y registré la corrida. No hay firma, así que la ficha del proyecto no se creó (`portafolio.py init` no corrió).

**Verificación previa**
- **Aceptación:** REQ-1030 está aceptado desde 2026-06-25, según el acta del comité del 2026-10-13.
- **Criterio de éxito:** el único criterio es «se verifica en producción». No dice qué se mide, con qué umbral ni quién lo verifica. Lo marqué como vacío.
- **Demanda:** viene de un «Cliente entrevistado» sin nombre. La entrevista es del 2025-08-11, tiene 14 meses y no nombra al requerimiento.
- **Autoridad:** la definición no la declara.

Como nadie podía responder, seguí adelante y dejé esos tres como vacíos del acta, sin rellenarlos. Tampoco hay patrocinador, presupuesto ni hitos en ningún documento, y no propuse gerente del proyecto.

**Supuesto que pasa a riesgo:** «El segmento paga por esto» sigue sin verificar y quedó sin doliente.

**Brecha de volumen:** el caso de negocio declara `volumen_mensual` 276.747 y el tablero mide 246.553. Son 10,9 % de diferencia, bajo el umbral de 20 %, así que no es hallazgo.

**Fuera del alcance:** REQ-1031, REQ-1032, REQ-1033 y REQ-2018, porque no se pidieron en esta invocación.

**Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15). No registré nada nuevo.

**Siguiente paso:** una persona con autoridad sobre el producto firma el acta o acepta por escrito los vacíos. Después el gerente que se nombre instala `criterio-project` y corre `/pm-setup`.

Archivos en `/home/claude/banco/ronda-2/bancos/espacio/estado-producto/PRD-303/corridas/`:
- `salida-product-charter.md`
- `2026-10-15-product-charter-1.md` (la corrida registrada)