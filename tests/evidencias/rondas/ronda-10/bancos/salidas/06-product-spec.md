# /criterio-product:product-spec 

Terminé: el borrador de especificación de PRD-304 (Tarjeta de crédito digital) quedó escrito y la corrida registrada, pero salió como esqueleto, no como especificación completa. Del registro no se puede escribir ningún comportamiento: en los 17 requerimientos aceptados no está dicho qué problema resuelve cada uno, y en el acta del comité solo se llaman «Requerimiento REQ-xxxx». Rellenarlo con lo razonable habría sido inventar la especificación.

Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-18), así que no hubo que registrarlos de nuevo.

- **Alcance:** entran los 17 aceptados. REQ-4401 queda fuera porque solo está propuesto.
- **Criterios de aceptación:** 3 requerimientos no tienen criterio (REQ-4400, 4412 y 4414). Los otros 14 dicen «se verifica en producción», que no se puede verificar.
- **Supuesto de demanda:** el registro lo da por verificado, pero el documento del proveedor que lo sustenta no está en la carpeta y el anexo solo dice «se confirmó».
- **Vacíos con dueño:**
  - Ningún requerimiento tiene proyecto que lo ejecute.
  - REQ-4407 y 4408 no tienen doliente.
  - Ninguna decisión del comité nombra a quien decidió.
  - No hay criterio de éxito del producto.
  - Ningún documento nombra otro equipo con trabajo pendiente.
- **Obligaciones normativas:** ningún documento dice el país, así que no cité ninguna norma. Las dejé como «no tengo la norma a la vista» o «sin resolver», para la revisión jurídica.
- **Cobertura:** el comportamiento cubierto es 0 de 17; el documento lo dice así.
- **Siguiente paso:** no ofrecí `/product-charter` porque los vacíos siguen abiertos.

Un dato por si lo buscas: la corrida registró 41 hallazgos en 67 segundos, sobre 18 requerimientos.

Quedó en `/home/claude/banco/ronda-10/bancos/espacio/estado-producto/PRD-304/corridas/salida-product-spec.md`. El registro de la corrida está en `corridas/2026-10-18-product-spec-1.md` de esa misma carpeta.