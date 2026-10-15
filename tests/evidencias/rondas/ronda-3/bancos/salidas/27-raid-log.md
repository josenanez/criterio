# /criterio-portfolio:raid-log portafolio

Terminé el RAID del portafolio y la corrida quedó registrada como `2026-10-15-raid-log-1`. Este es el resultado.

## RAID del portafolio (13 proyectos) al 2026-10-15
Salió de las 13 fichas, los 13 informes de avance, las 13 actas de constitución, 4 contratos, 2 solicitudes de cambio, 21 minutas y las notas de PRY-207 del 2026-10-15. Los términos estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-15.

Tras reclasificar quedan 32 ítems: 7 riesgos, 6 supuestos, 9 incidencias y 10 dependencias.

**Ningún ítem trae probabilidad, impacto, doliente, fecha ni último movimiento.** Lo dejé como hallazgo y no lo rellené. Los ids (`PRY-xxx-R/S/I/D n`) los asigné yo, porque las fichas no traen.

### Necesitan decisión ahora
Ninguno tiene doliente.

- **Calendario de liberaciones del core (dependencia).** Seis proyectos lo listan: PRY-200, 203, 204, 206, 207 y 208. Además, PRY-199, 200 y 203 reportan historias fuera del sprint por esa causa. Afecta a otros proyectos.
- **Disponibilidad del equipo de seguridad (supuesto).** Seis proyectos cuentan con ella: PRY-199, 200, 202, 206, 210 y 211. PRY-202, 203 y 205 ya tienen hallazgos de seguridad abiertos.
- **PRY-205, en rojo.** Tiene dos incidencias abiertas desde el 2026-10-13: un hallazgo de seguridad y una prueba de carga que no alcanzó el umbral.
- **PRY-204, en rojo.** Tiene el riesgo de un cambio regulatorio que puede mover el alcance. Son 18.000 M COP aprobados, sin doliente ni fecha.

La prueba de carga fallida aparece con texto idéntico en PRY-200, 202, 205 y 210, y el hallazgo de seguridad en PRY-202, 203 y 205. Puede ser un problema común o texto de plantilla en los informes. No lo sé.

### Detectados en reuniones y no registrados
- **PRY-207, notas del 2026-10-15:** el proveedor podría no llegar con el equipo completo para la siguiente fase. Las notas dicen que nadie lo anotó como riesgo. Es el único riesgo dicho al pasar en las 21 minutas; el resto son tablas de compromisos. No hay contrato de PRY-207 en la carpeta, así que no sé quién es el proveedor.
- **Salidos de informes, no de reuniones:**
  - Dos historias fuera del sprint por la dependencia con el core, en PRY-199, 200 y 203. Es una incidencia que no está en el RAID.
  - «Se reprogramó la salida por ventana de cambio» en PRY-201, 204, 205, 207, 208 y 209. Los informes no dicen cuánto movió la fecha.

### Reclasificaciones
- **Dependencia:** 6 ítems «calendario del core» y 4 de «proveedor sin confirmar fecha» estaban como riesgo. Dependen de alguien fuera del proyecto.
- **Supuesto:** 6 ítems de «disponibilidad del equipo de seguridad» estaban como riesgo. Se dan por ciertos sin verificar. Si ese equipo es ajeno al proyecto sería una dependencia; los documentos no lo dicen.
- Se quedan como riesgo el cambio regulatorio (PRY-204, 205, 209) y la concentración del conocimiento (PRY-202, 209, 211).
- No modifiqué las fichas; la reclasificación es una propuesta para cada gerente.

### Dependencias en riesgo
- **Core:** no puedo cruzarla. Las 13 actas dicen «Ninguna declarada» y ningún documento dice qué proyecto es «el core». PRY-201 (Core de depósitos) y el hito «Integración con el core» de PRY-202, que se movió +66 días, son solo una hipótesis.
- **PRY-201:** lleva 24 días sin informe y su cierre comprometido era el 2026-10-12.
- **Proveedor:** PRY-199, 201, 203 y 205 dependen de una fecha que el proveedor no ha confirmado. Es una dependencia declarada, no acordada. Solo PRY-199 tiene contrato (CT-199), con el primer entregable pendiente para el 2026-11-14.

### Lo que no sé
- No pude evaluar «sin movimiento en dos períodos» ni «mitigación vencida». No hay fechas de movimiento ni mitigaciones, y hay un solo informe por proyecto.
- No revisé los cronogramas `.xlsx`.

### Después
Los cuatro puntos de decisión cumplen el criterio de escalamiento para el comité del 2026-10-21. Puedo prepararlos con la decisión formulada. También puedo proponer doliente para los ítems sin él; propongo, no asigno. En esta prueba no había a quién preguntar, así que no hice ninguna de las dos cosas.

El registro completo de los 32 ítems está en `/home/claude/banco/ronda-3/bancos/espacio/estado/corridas/salida-raid-log.md`. La corrida tardó 102 segundos. Registró 68 señales abiertas del portafolio y no medí cuántos documentos leí.