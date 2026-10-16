# /criterio-product:product-requirements 

Terminé el registro de requerimientos de Tarjeta débito (PRD-303) y la corrida quedó guardada, con 42 hallazgos en 29 segundos. Los términos ya estaban vigentes, así que no registré ninguna aceptación nueva.

**Registro al 2026-10-15:** 18 requerimientos, 12 aceptados y 6 propuestos. El 91,7 % de los decididos tiene evidencia y el 0 % tiene un proyecto que lo ejecute.

En el orden de lectura del comando:

1. **Se va a construir y nadie lo pidió:** REQ-4301 está aceptado desde 2026-05-17, sin evidencia y con «—» en «Quién lo pidió».
2. **Decidido y nadie lo construye:** los 12 aceptados no tienen proyecto. La carpeta de fichas `estado/records` no existe, así que no hay forma de confirmarlo. El acta del comité también pone «—» en todos.
3. **Sin doliente:** REQ-4305, REQ-4306 y REQ-4314 dicen «sin asignar».
4. **Sin criterio de aceptación:** REQ-2030 y REQ-4302. En los demás el criterio es solo «se verifica en producción».
5. **Decidido sin documento:** ninguna de las 12 aceptaciones tiene un documento propio. El acta del 2026-10-12 solo lista los estados y su única decisión escrita es «Se mantiene el plan».
6. **Lleva meses sin decidirse:** seis propuestos llevan entre 65 y 214 días, y el más viejo es REQ-4309. La facultad de decidir es del Comité de producto; Natalia Ospina, la gerente, fue la única asistente al comité.
7. **Evidencia vieja:** 17 de los 18 se apoyan en una sola entrevista del 2025-09-19, que no está vinculada a ningún requerimiento.

Aparte, el supuesto «El reglamento vigente lo permite» lleva 43 días sin verificar. El volumen mensual medido queda 18,4 % por debajo del declarado, bajo el umbral de 20 %.

El siguiente paso que propone el comando es `/product-trace` para los 12 aceptados sin proyecto.

Archivos en `/home/claude/banco/ronda-4/cooperativas/espacio/estado-producto/PRD-303/corridas/`:
- `salida-product-requirements.md`
- `2026-10-15-product-requirements-1.md`