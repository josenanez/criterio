# /criterio-portfolio:raid-log portafolio

Este es el registro RAID del portafolio al 2026-10-14. Sale de las 13 fichas, de 5 de las 13 actas (solo su sección de dependencias) y de las únicas notas de reunión de la carpeta, las de PRY-211. Los términos ya estaban aceptados (versión 1.0, 2026-10-14). La corrida quedó registrada como `2026-10-14-raid-log-1`, en 87 segundos.

**Resumen**
- **Cifras:** hay 19 riesgos, 23 incidencias, 1 dependencia y 0 supuestos, 43 ítems en total tras reclasificar.
- **Doliente y fechas:** ninguno de los 43 tiene doliente, y ningún riesgo tiene fecha, probabilidad ni impacto. Lo dejé sin llenar.
- **Sin movimiento:** 6 ítems llevan más de 15 días sin movimiento, 3 en PRY-208 (19 días) y 3 en PRY-210 (16 días).
- **Escalamiento a comité:** ningún ítem cumple de forma demostrable un criterio de escalamiento. Para decisión del comité quedan cuatro grupos de incidencias sin doliente, que el archivo detalla:
  - el hallazgo de seguridad en medios de pago, en 5 proyectos;
  - la prueba de carga fallida, en 3;
  - el despliegue reprogramado sin fecha nueva, en 7;
  - el componente del proveedor pendiente de aceptación, en 4.
- **Dicho en reunión:** el único riesgo sin registrar es el del proveedor de PRY-211, que podría no llegar con el equipo completo. Sigue marcado como no registrado formalmente.

**Reclasificaciones**
- **PRY-201:** «el proveedor no ha confirmado la fecha» pasa de riesgo a dependencia declarada, no acordada.
- **PRY-200, PRY-206 y PRY-210:** el «congelamiento de temporada» sale de riesgos porque ya ocurrió: esos tres reportan el despliegue reprogramado.
- **PRY-204:** «se ajustó el plan de pruebas» no es incidencia, es un cambio.

**Lo que no pude saber**
- **Dependencias entre proyectos:** no pude cruzarlas. Ninguna ficha declara dependencia de otro proyecto y solo revisé 5 de las 13 actas, que dicen «Ninguna declarada».
- **Hallazgo de seguridad en PRY-199:** aparece en el proyecto de iluminación LED en bodegas y no está sustentado que le corresponda. Confírmalo antes de formalizarlo.
- **Riesgos repetidos:** varios riesgos tienen redacción idéntica en proyectos de rubros distintos. No sé si son reales o vienen de una plantilla de informe.
- **Informes de avance:** no releí los originales; me apoyé en lo que las fichas citan de ellos.
- **Ofrecimiento pendiente:** puedo proponer doliente para los ítems que no tienen (propongo, no asigno) y preparar la subida a comité.

Archivos en `estado-portafolio/corridas/`:
- `salida-raid-log.md`
- `2026-10-14-raid-log-1.md`