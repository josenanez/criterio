# /criterio-portfolio:raid-log portafolio

Terminé el RAID del portafolio y la corrida quedó registrada en `estado/corridas/2026-10-16-raid-log-1.md`. Salió de 13 proyectos: sus fichas, actas de constitución, informes de avance y las 11 minutas y notas de reunión. Los términos ya estaban vigentes (v1.1, José Francisco Ñáñez, 2026-10-16), así que no hubo que registrar nada.

No pude hacer el cruce de dependencias entre proyectos. Ninguna dependencia trae el código de un proyecto, y las 13 actas dicen «Ninguna declarada», aunque los informes muestran dependencia de proveedores y de Operaciones.

**Resultado:** 14 riesgos, 16 incidencias, 6 dependencias y 0 supuestos.
- **Reclasificación:** las fichas traían 20 riesgos y 0 dependencias. Moví 6 riesgos a dependencia:
  - «proveedor sin confirmar fecha» en PRY-203, 204 y 206.
  - «ventana de parada definida por Operaciones» en PRY-205, 208 y 209.
- **Sin doliente:** los 36 ítems registrados no tienen doliente, y los riesgos y las dependencias tampoco tienen fecha. Ninguno trae probabilidad ni impacto (los dejé «sin dato», no usé la escala alta/media/baja).
- **No registrado en reunión:** una sola, en PRY-205 (notas del 2026-10-16): el proveedor podría no llegar con el equipo completo. Las otras 10 actas solo traen compromisos.
- **Para decisión del comité:**
  - El bloqueo de la vía de acceso (5 proyectos) y el cambio de licencia ambiental (5 proyectos) no tienen doliente.
  - La ventana de parada (3 proyectos) y el proveedor sin fecha (3 proyectos) tampoco.
  - La incidencia de auditoría de seguridad de PRY-200 lleva 22 días abierta sin responsable.

Los doli entes que propongo en el informe son sugerencias, no asignaciones.

**Lo que no sé:**
- La antigüedad real de los riesgos, porque la ficha no guarda fecha de apertura.
- Si hay mitigaciones.
- Quién es el proveedor de las dependencias.
- Si los ítems con el mismo texto en varios proyectos son el mismo hecho.
- Los informes PDF los tomé de lo que ya estaba en la ficha, no los reabrí.

La corrida se registró con `--caso portafolio` porque no es de un proyecto solo, y el script lo aceptó.

El informe completo, con el registro de los 37 ítems, está en `estado/corridas/salida-raid-log.md`.