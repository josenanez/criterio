# /criterio-portfolio:raid-log portafolio

El registro RAID del portafolio al 2026-10-14 está hecho y la corrida quedó registrada (`2026-10-14-raid-log-1`). Salió de las 13 fichas de PRY-199 a PRY-211 y de las minutas y notas de reunión de ocho proyectos. No releí los informes de avance. Los términos v1.0 ya estaban aceptados en la configuración.

El resultado son 9 riesgos, 18 incidencias, 7 dependencias y ningún supuesto, 34 ítems en total.

- **No registrado formalmente:** solo hay uno, en las notas de PRY-208 del 2026-10-14: "el proveedor podría no llegar con el equipo completo para la siguiente fase", y nadie lo anotó. Las demás minutas solo traen compromisos.
- **Reclasificaciones:** reclasifiqué 7 ítems de riesgo a dependencia, porque dependen de alguien fuera del proyecto. Son "ventana de parada de planta" (Operaciones, en PRY-201, 206 y 208) y "proveedor sin confirmar fecha" (PRY-199, 204, 206 y 207). Es una propuesta; no toqué las fichas.
- **Doliente:** los 34 ítems no tienen doliente. Los riesgos y las dependencias tampoco tienen fecha, y lo reporto como hallazgo sin rellenarlo.
- **Sin movimiento:** tres dependencias llevan más de 15 días sin moverse (PRY-206 ×2 y PRY-208). Usé el umbral de 15 días de la configuración, porque las fuentes no definen "período".
- **Para decidir:** el riesgo de PRY-208, los hallazgos de la auditoría de seguridad sin doliente en seis proyectos y los equipos entregados sin aceptación documentada en PRY-200 y PRY-201. No subí nada a comité ni asigné dolientes.
- **Lo que no sé:** probabilidad e impacto no constan en ninguna fuente, así que no apliqué el criterio de escalamiento por valoración. Las dependencias no nombran el proyecto del que dependen, por lo que no pude cruzar fechas entre proyectos.

Los números de la corrida no coinciden con el RAID. La corrida cuenta 39 hallazgos de señales de gobierno de las fichas (hitos sin evidencia, compromisos vencidos, facturación contra lo aceptado y similares), no ítems RAID. Y marcó `documentos: null`, es decir que no midió documentos leídos.

Archivos en `/home/claude/banco/ronda-1/mineria/espacio/estado/portafolio/corridas/`:
- salida-raid-log.md
- 2026-10-14-raid-log-1.md