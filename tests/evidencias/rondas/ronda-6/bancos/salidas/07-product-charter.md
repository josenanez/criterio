# /criterio-product:product-charter REQ-4600

Escribí el borrador del acta de constitución para REQ-4600 (producto PRD-306, Microseguros), pero no creé la ficha del proyecto: el acta no está firmada.

Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-16, así que no los registré de nuevo.

**Qué falta en REQ-4600.** Cuando el comando ofrece seguir marcando lo que falta como vacío, tomé la respuesta sugerida (seguir) y no rellené nada:
- **Quién lo aceptó:** consta que está aceptado desde 2026-06-28, pero no quién lo decidió.
- **Autoridad:** la definición no la declara. «Comité de producto» es solo una propuesta por defecto.
- **Criterio de éxito:** el único criterio es «se verifica en producción», que no se puede medir.
- **Evidencia de demanda:** es una sola cita de cliente de 2025-10-05 («Lo necesito y hoy no lo tengo.») que no nombra el requerimiento.
- **Otros vacíos:** el borrador marca también como vacíos la necesidad, la prioridad, el patrocinador y el presupuesto.

**Supuesto y cifra que pasan al proyecto:**
- El supuesto «El proveedor cumple el tiempo pactado» sigue sin verificar. Pasa a ser riesgo del proyecto cuando exista gerente.
- La cifra del caso de negocio, volumen mensual de 204.945, no tiene ningún tablero de métricas contra el que contrastarla.

**Sin barrido normativo:** no revisé obligaciones normativas de microseguros. El acta lo deja como pendiente, sin afirmar ni descartar nada.

**Alcance:** solo entra REQ-4600. Los otros 15 requerimientos del registro quedan sin decisión de alcance, no descartados.

**Siguiente paso:** alguien con autoridad firma el acta y se asigna un gerente. Esa persona instala `criterio-project` y corre `/pm-setup`.

La corrida quedó registrada como `2026-10-16-product-charter-1` y tardó 30 segundos. Detectó 37 hallazgos sobre los 16 requerimientos del producto (por ejemplo, 12 evidencias vencidas y 12 requerimientos sin proyecto).

Archivos en `/home/claude/banco/ronda-6/bancos/espacio/estado-producto/PRD-306/corridas/`:
- `salida-product-charter.md`