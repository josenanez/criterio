# /criterio-product:product-charter REQ-1000

Dejé el borrador del acta de REQ-1000 (Crédito de libranza, PRD-300), pero no creé la ficha del proyecto: el acta no está firmada y la ficha se crea solo después de la firma.

Los términos ya estaban vigentes, así que no los registré de nuevo. Ya constaban a nombre de José Francisco Ñáñez, versión 1.1, 2026-10-15.

Al revisar el requerimiento, seguí con los vacíos marcados en el acta, sin rellenarlos. REQ-1000 está aceptado, pero le faltan estas cosas:
- **Criterio de éxito:** «se verifica en producción» no se puede medir.
- **Demanda:** la única cita es de la entrevista del 2025-09-20 («Lo necesito y hoy no lo tengo»). No nombra REQ-1000 y ya tiene 12 meses.
- **Qué pide:** el campo de necesidad está vacío (`not_found`).
- **Gobierno:** ningún documento dice quién es el patrocinador, el gerente del proyecto ni qué autoridad tiene.
- **Presupuesto e hitos:** no están declarados.
- **Normativa:** no hice el barrido de obligaciones normativas, así que esa sección queda sin resolver.

Hay además una contradicción en las cifras: el caso de negocio declara un volumen mensual de 156.447 y el tablero del 2026-10-15 mide 121.498, un 22,3% menos. El acta lleva esa cifra como supuesto del proyecto.

REQ-1001 a REQ-1003 quedaron fuera del alcance, solo porque el argumento pedía REQ-1000. El acta lo dice y deja la decisión a quien firme.

El proyecto necesita un gerente. Esa persona instala `criterio-project` y corre `/pm-setup` primero.

La corrida quedó registrada con 32 segundos y 9 hallazgos.

Archivos en `estado-producto/PRD-300/corridas/`:
- `salida-product-charter.md`
- `2026-10-15-product-charter-1.md`