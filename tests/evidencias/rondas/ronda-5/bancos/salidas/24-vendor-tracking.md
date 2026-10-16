# /criterio-portfolio:vendor-tracking PRY-207

**PRY-207 no tiene proveedores, así que no había nada que cruzar.** La ficha trae `vendors: []`. Ni el acta de constitución ni el informe de avance del 2026-09-24 nombran un proveedor, un contrato, entregables contractuales ni facturas. No armé tablas ni vencimientos de contrato porque habría sido inventar. Un resultado vacío del script tampoco prueba que el proveedor esté limpio, solo que no hay dato.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-16. No hubo que registrar nada.

**Lo que falta:**
- **Contratos:** `00-gobierno` solo tiene el acta.
- **Vigencia, renovación y preaviso:** no se pueden revisar sin contrato.
- **Montos facturados o aceptados:** ningún documento los declara.
- **Compromisos de proveedores:** la carpeta no tiene minutas.

**Dos cosas aparte, no de proveedores, según `compute`:**
- El proyecto declara estado verde, pero lleva 22 días en silencio desde el informe del 2026-09-24. De las fuentes de la ficha, ninguna es evidencia.
- El informe menciona una salida reprogramada y dos semanas perdidas por la rotación de un desarrollador clave, pero no hay ningún cambio registrado. El cierre del acta (2026-06-19) ya pasó.

**Siguiente paso:** pedirle a Rubén Cárdenas, el gerente, los contratos y las actas de recibo, o una confirmación por escrito de que no hay proveedores. Con eso se vuelve a correr `/vendor-tracking PRY-207`.

La salida quedó en `estado/corridas/salida-vendor-tracking.md` y la corrida en `2026-10-16-vendor-tracking-1`. El resumen de la corrida cuenta los 13 proyectos del portafolio, no solo PRY-207 (50 hallazgos en total); los de PRY-207 son `silent` y `declared_vs_evidence`.