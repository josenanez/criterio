# /criterio-product:product-charter REQ-4000

Dejé el borrador del acta de constitución de REQ-4000 y registré la corrida, pero no creé la ficha del proyecto porque el acta no está firmada. El acta tiene 10 vacíos declarados, y no rellené ninguno.

- **Configuración:** el argumento `REQ-4000` es un requerimiento, no un código de producto. Usé el único producto configurado, PRD-300 «Venta en línea».
- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no registré nada nuevo.
- **Verificación previa:** la aceptación, el criterio de éxito, la demanda y la autoridad tienen faltas. Como nadie podía responder, tomé la respuesta sugerida: seguir y marcar cada falta como vacío del acta.
  - **Aceptación:** el acta del comité (2026-10-09) lo lista como «aceptado» desde 2026-05-16, pero no dice quién lo aceptó. El único asistente es María Restrepo.
  - **Criterio de éxito:** solo dice «se verifica en producción», que no se puede medir.
  - **Demanda:** hay una sola cita de un cliente (2025-11-24) y no nombra el requerimiento; el acta del comité se la atribuye.
  - **Autoridad:** la definición no la declara. El acta del comité nombra «Comité de producto» pero no dice quién decide en él.
- **Supuesto que pasa a riesgo:** «El proveedor cumple el tiempo pactado» sigue sin verificar. Lleva unos 86 días, y el umbral es 30. Queda sin doliente. Además lleva fecha 2026-07-21 dentro de una definición fechada 2025-11-26, y ningún documento nombra al proveedor.
- **Lo que no entra:** los otros 15 requerimientos quedan fuera. REQ-4002, REQ-4003 y REQ-4005 siguen propuestos. Los demás no se pidieron para esta acta.
- **Normativa:** no hice barrido. No se sabe si aplica alguna obligación, y el acta no afirma que no.
- **Gobierno:** patrocinador, gerente del proyecto, presupuesto e hitos no están dichos en ningún documento. El acta no nombra a nadie.
- **Después:** el acta del comité dice «Se mantiene el plan», pero ningún proyecto ejecuta REQ-4000. Cuando se asigne el gerente del proyecto, instala `criterio-project` y corre `/pm-setup`.

La corrida quedó registrada como `2026-10-15-product-charter-1`: 35 segundos, 16 requerimientos y 25 hallazgos abiertos en todo el producto.

Archivos en `estado-producto/PRD-300/corridas/`:
- `salida-product-charter.md`