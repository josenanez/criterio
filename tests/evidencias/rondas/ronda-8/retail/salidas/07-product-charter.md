# /criterio-product:product-charter REQ-4901

Dejé el borrador del acta de constitución de REQ-4901, pero la ficha del proyecto no se creó porque el acta aún no está firmada.

**Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los volví a registrar.

**Qué falta en REQ-4901.** Está aceptado, pero no cumple tres condiciones del paso 1:
- **Criterios de aceptación:** no tiene ninguno, y la definición del producto tampoco declara un criterio de éxito.
- **Quién lo aceptó:** el acta del comité del 2026-10-16 no lo dice. La fecha de aceptación, 2026-05-17, es anterior a esa acta y no hay documento de la decisión.
- **Autoridad del gerente del proyecto:** no está declarada. Solo consta que la autoridad del producto es el Comité de producto.

**Qué pide REQ-4901.** El acta del comité solo trae el identificador, así que no sé qué se necesita. La única entrevista (2025-10-11, «Lo necesito y hoy no lo tengo») no nombra el requerimiento.

Como nadie podía responder, tomé la respuesta sugerida: seguí y marqué esos puntos como vacíos del acta, sin rellenarlos. El borrador también registra:
- **Vacíos de gobierno:** no hay patrocinador ni gerente del proyecto; Elena Duarte es gerente del producto.
- **Supuestos y normativa:** cuatro supuestos pasan al proyecto como riesgos y hay cinco restricciones normativas sin resolver, con el país sin declarar.
- **Presupuesto e hitos:** no hay ninguno declarado.
- **Fechas inconsistentes:** la definición es del 2025-11-12 pero cita un supuesto declarado el 2026-03-28 y una verificación del 2026-08-21.
- **Alcance excluido:** quedan fuera los 4 requerimientos propuestos y los otros 10 aceptados.

**Firma y siguiente paso.** Lo firma el Comité de producto. Después se crea la ficha con `portafolio.py init`, dejando el estado declarado vacío. El gerente del proyecto, que la organización aún debe nombrar, instala `criterio-project` y corre `/pm-setup`.

**Corrida registrada:** 32 segundos, 15 requerimientos revisados y 34 hallazgos abiertos. La salida completa quedó en `salida-product-charter.md`.

Archivos en `/home/claude/banco/ronda-8/retail/espacio/estado-producto/PRD-309/corridas/`:
- `salida-product-charter.md`
- `2026-10-17-product-charter-1.md`