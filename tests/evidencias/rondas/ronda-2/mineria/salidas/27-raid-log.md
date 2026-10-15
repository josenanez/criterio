# /criterio-portfolio:raid-log portafolio

Términos vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15). No hizo falta volver a registrarlos.

## RAID del portafolio de minería al 2026-10-15

**Registrado hoy:** 23 riesgos, 0 supuestos, 12 incidencias y 0 dependencias, 35 ítems en total. Tras reclasificar quedan 12 riesgos, 12 incidencias y 11 dependencias.

- **Sin doliente ni fecha:** los 35 ítems. Tampoco tienen probabilidad ni impacto. Las fichas no traen identificadores, así que usé etiquetas propias como `203·I1`.
- **Sin movimiento:** no se puede medir. Solo hay un corte guardado (el del 2026-10-15), así que no sé qué ítems llevan dos períodos quietos.
- **No registrado formalmente:** 1 riesgo, en PRY-205. Las notas del 2026-10-15 dicen que el proveedor podría no llegar con el equipo completo para la siguiente fase y que nadie lo anotó. En las otras 11 minutas no apareció lenguaje de riesgo.

**Reclasificados.** Los 11 pasan de riesgo a dependencia porque dependen de un tercero que el proyecto no controla.
- "El proveedor no ha confirmado la fecha de la última entrega" aparece en 200, 201, 202, 203, 206, 210 y 211.
- "Ventana de parada de planta definida por operaciones" aparece en 199, 200, 205 y 206.
- No toqué las fichas. La reclasificación queda solo en este informe.

**Necesitan decisión ahora:**
- **PRY-203:** cierra el 2026-10-17, tiene la entrega del proveedor sin confirmar y declara verde.
- **PRY-206:** lleva 20 días sin informe ni minuta (umbral de 15) y tiene un hallazgo de auditoría abierto.
- **PRY-205:** el riesgo no registrado del proveedor, con fin el 2026-11-06.
- **PRY-200, 202 y 209:** son los tres proyectos en rojo, con incidencias sin responsable.
- **PRY-211:** el primer ensayo de disponibilidad falló y se repite, pero el proyecto declara verde.
- **Proveedor compartido:** Ingeniería Minera del Sur S.A.S. figura en los contratos de 199, 202, 210 y 211.

**Dependencias entre proyectos.** No pude cruzarlas: ninguna dependencia lleva el código del proyecto del que depende. Hoy nadie sabría si algún proyecto depende de 207, 208 o 211, que movieron su línea base.

**Qué no sé.** Quién es doliente de cada ítem, desde cuándo está abierto, y cuál proveedor es el que no confirma. Tampoco releí los informes de avance (salvo el de PRY-208) ni los 5 PDF. Esos ítems salen de lo que ya recogieron las fichas.

**Después.** Ofrezco subir a comité los ítems de "Necesitan decisión ahora". No propuse ni asigné dolientes. Falta su decisión sobre las 11 reclasificaciones.

La corrida quedó registrada como `2026-10-15-raid-log-1`. Las cifras de corrida están en `estado/corridas.json` y la salida completa, con las 35 filas, está en `estado/corridas/salida-raid-log.md`.