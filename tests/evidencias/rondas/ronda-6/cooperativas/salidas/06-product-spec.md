# /criterio-product:product-spec 

Terminé. El borrador de especificación de Microcrédito (PRD-305) quedó escrito y la corrida quedó registrada, pero no pude especificar ningún comportamiento. Los 13 requerimientos aceptados se llaman solo «Requerimiento REQ-45xx», y ningún documento dice qué pide cada uno. Inventar comportamiento habría sido rellenar los huecos, así que los dejé a la vista.

- **Cubiertos:** 0 de 13 aceptados tienen comportamiento que citar. Los 3 propuestos (REQ-4508, 4512 y 4513) quedan fuera del alcance.
- **Criterios de aceptación:** ninguno de los 13 se puede verificar. 10 dicen solo «se verifica en producción», sin métrica ni umbral. REQ-4500, 4505 y 4515 no tienen criterio. No propuse criterios de reemplazo.
- **Supuestos:**
  - «El proveedor cumple el tiempo pactado» lleva 73 días sin verificar (el umbral es 30) y no nombra al proveedor.
  - La cifra de volumen mensual (282.429) del caso de negocio es declarada, no medida.
  - La evidencia es una sola entrevista de hace 12 meses, que no nombra ningún requerimiento.
- **Vacíos con dueño:**
  - Cuatro requerimientos aceptados no tienen doliente: REQ-4505, 4509, 4510 y 4511. Los cierra el Comité de producto.
  - La propuesta principal y el criterio de éxito de la definición los cierra Óscar Ramírez.
  - Ningún requerimiento tiene proyecto asociado.
  - El acta no guarda la fecha de decisión de ninguno.
- **Normativa:** el país no aparece en ningún documento. Listé siete temas que la definición toca (consumidor financiero, datos personales, tasas, centrales de riesgo, proveedor tercero, consentimiento y retención), todos como «no tengo la norma a la vista». No cité ninguna norma.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no registré nada nuevo. No ofrezco `/product-charter` todavía: primero cada doliente tiene que escribir qué pide su requerimiento, y después se vuelve a correr `/product-spec`.

La corrida (`2026-10-16-product-spec-1`) tardó 61 segundos y dejó 39 hallazgos.

Archivos en `/home/claude/banco/ronda-6/cooperativas/espacio/estado-producto/PRD-305/corridas/`:
- `salida-product-spec.md`