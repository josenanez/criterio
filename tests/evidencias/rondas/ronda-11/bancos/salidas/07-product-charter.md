# /criterio-product:product-charter REQ-4200

Escribí el borrador del acta de REQ-4200, pero no está listo para firmar. No creé la ficha del proyecto: eso va después de la firma.

Los términos ya estaban vigentes (versión 0.8.0, aceptados por José Francisco Ñáñez el 2026-10-23). No hizo falta pedirlos otra vez.

El REQ-4200 está aceptado, pero le faltan cuatro cosas. Las dejé como vacíos del acta, sin rellenar, que era la respuesta sugerida:
- **Autoridad:** ningún documento dice quién decide qué se construye. Tampoco consta quién aceptó el requerimiento; el comité del 2026-10-22 solo registra a Elena Duarte como asistente.
- **Criterio de éxito:** el único criterio es «se verifica en producción». No hay métrica, umbral ni fecha.
- **Demanda:** la entrevista del 2025-10-15 («Lo necesito y hoy no lo tengo.») no nombra este requerimiento. Además tiene más de 12 meses; esa señal la marcó el script al registrar la corrida y no está en el borrador.
- **Patrocinador y gerente del proyecto:** no constan. Elena Duarte es gerente de producto, no del proyecto, así que no propuse a nadie.

Otros puntos del borrador:
- **Supuesto de pago:** el supuesto «el segmento paga por esto» figura como confirmado. Su evidencia es un documento técnico del proveedor (2026-09-04) que no está en la carpeta, así que no se puede comprobar.
- **Volumen mensual:** el caso de negocio declara 289.875 y el tablero mide 235.072, un −18,9 %. Queda bajo el umbral de 20 %, por lo que no es hallazgo.
- **Normativa:** el barrido de restricciones normativas no se hizo. Quedó como pendiente, sin opinión sobre cumplimiento.
- **Alcance excluido:** los otros 15 requerimientos (REQ-4201 a REQ-4215) quedan fuera porque pediste solo el REQ-4200. Dejé escrito que no se evaluaron.

Después de la firma, el gerente del proyecto (aún sin nombrar) instala `criterio-project` y corre `/pm-setup`.

La corrida quedó registrada, con 35 segundos medidos y 35 hallazgos sobre los 16 requerimientos del registro.

Archivos en `estado-producto/PRD-302/corridas/`:
- salida-product-charter.md
- 2026-10-23-product-charter.md