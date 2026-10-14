# /criterio-product:product-charter REQ-1030

Dejé el borrador del acta de REQ-1030, con vacíos grandes que el acta marca sin rellenar. No está firmado y no creé la ficha del proyecto. El 2026-10-14 José Francisco Ñáñez aceptó TERMS.md v1.0 y, ante la pregunta de seguir sin lo que falta, tomé la respuesta sugerida: seguir y marcar cada falta como vacío.

**Qué se pudo verificar sobre REQ-1030**
- **Aceptado:** sí, el acta del comité del 2026-10-10 lo marca así.
- **Fuente:** el registro `estado/requirements/` está vacío, así que REQ-1030 existe solo en esa acta. Su título es «Requerimiento REQ-1030», sin descripción.
- **Criterio de aceptación:** dice solo «se verifica en producción». No se puede medir.
- **Demanda:** hay una sola entrevista, del 2026-08-31, con la cita «Lo necesito y hoy no lo tengo». No nombra a REQ-1030 y es posterior a su fecha «Desde» (2026-06-25).
- **Autoridad:** la definición no la declara.

**Otros vacíos que quedaron en el acta**
- No hay patrocinador, ni gerente del proyecto, ni presupuesto o hitos, ni proyecto que lo ejecute.
- El supuesto «La red de la mina soporta el volumen» figura como «verificado», pero sin evidencia. Lo llevé al proyecto como riesgo por asignar.
- La cifra de volumen mensual declarada (198.346) difiere 9,3 % de la medida (179.966), por debajo del umbral de 20 %. No es hallazgo.
- No identifiqué restricciones normativas, pero no hice un barrido completo.
- REQ-1031, 1032, 1033, 2018 y 2026 quedaron en «No entra».

**Qué sigue:** el Comité de producto, que es la autoridad que figura en la configuración, firma el acta y asigna a un gerente de proyecto. Ese gerente instala `criterio-project` y corre `/pm-setup`.

**Archivos**
- `estado/corridas/salida-product-charter.md`: el acta completa.
- `estado/corridas/2026-10-14-product-charter-1.md`: la corrida registrada.

La corrida registró 0 requerimientos y producto «?», porque el registro está vacío y `estado/producto.json` no tiene la identidad cargada.