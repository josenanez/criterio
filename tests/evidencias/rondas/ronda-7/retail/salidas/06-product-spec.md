# /criterio-product:product-spec 

# Especificación — Tarjeta de la tienda (PRD-309) · borrador del 2026-10-17

Es un borrador, no una especificación aprobada. Lo cierra Diana Molina con el comité de producto.

El registro permite abrir la especificación, pero no escribir su comportamiento. Los 9 requerimientos aceptados no tienen título, necesidad ni prioridad, y su único criterio de aceptación es «se verifica en producción». Dejé las secciones de comportamiento sin escribir en vez de rellenarlas con lo razonable.

- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo.
- **Entra:** los 9 aceptados: REQ-2026, 4900, 4901, 4903, 4904, 4905, 4906, 4907 y 4911.
- **No entra:** REQ-4902, 4908, 4909 y 4910, que siguen en `propuesto`.
- **Criterios de aceptación:**
  - Siete requerimientos solo traen «se verifica en producción». No se puede verificar sin discutir ni medir hoy.
  - REQ-4907 y REQ-4911 no traen criterio alguno.
  - No propuse cifras de reemplazo, porque serían decisiones del negocio.
- **Supuestos:**
  - «El proveedor cumple el tiempo pactado» no está verificado y no tiene dueño en el registro.
  - El volumen mensual declarado en el caso de negocio es 272.424 y el tablero mide 208.658 (23,4 % menos). Los cortes son distintos y el tablero no dice cómo cuenta el volumen.
- **Vacíos con dueño:**
  - **Falta en los requerimientos:** necesidad, prioridad y criterio de éxito del producto.
  - **REQ-4907:** no tiene dueño, criterio ni evidencia.
  - **Evidencia de demanda:** REQ-2026, 4903, 4904 y 4907 no la tienen.
  - **Decisión:** el acta no nombra quién decidió las aceptaciones.
  - **Casos borde y otros equipos:** los casos borde no están definidos y ningún proyecto ni equipo está acordado.
- **Normativa:** no sé el país ni tengo las normas a la vista, así que no cité ninguna. Listé cinco áreas que toca una tarjeta (datos personales, consumidor financiero, pagos, retención y proveedor) con el estado «no tengo la norma a la vista». No dije nada sobre cumplimiento.
- **Aceptados sin cubrir:** los 9. El registro no trae con qué escribir su comportamiento.
- **Siguiente paso:** no ofrezco `/product-charter` todavía. Antes hacen falta los vacíos cerrados y un criterio de éxito.

La corrida quedó registrada como `2026-10-17-product-spec-1` (40 s, 13 requerimientos, 32 señales).

Archivos están en `/home/claude/banco/ronda-7/retail/espacio/estado-producto/PRD-309/corridas/`:
- `salida-product-spec.md`