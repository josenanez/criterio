# /criterio-portfolio:raid-log portafolio

**Sale de:** las 13 fichas (PRY-199 a PRY-211), los informes de avance, las actas de constitución, 14 minutas de comité y las notas de reunión del 2026-10-15 de PRY-201. Los términos están vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo. No hay escala de valoración definida y ningún ítem trae probabilidad ni impacto.

## RAID — portafolio al 2026-10-15
15 riesgos · 0 supuestos · 12 incidencias · 8 dependencias
35 sin doliente · 35 sin fecha de resolución · 1 no registrado formalmente

No pude medir cuáles ítems llevan dos períodos sin movimiento. Cada ítem tiene una sola observación y no hay historial.

### Reclasificado
- **"El proveedor no ha confirmado la fecha de la última entrega"** pasa de riesgo a dependencia declarada y sin confirmar. Aparece en PRY-199, 200, 202, 203, 205, 206, 207 y 210. Depende de un tercero y las actas de esos proyectos dicen "Ninguna declarada". El informe no nombra al proveedor, así que no hay código de proyecto que citar.

### Necesitan decisión ahora
Las tres primeras afectan a varios proyectos a la vez, lo que las hace subir a comité.

| Qué | Tipo | Dónde | Doliente | Desde |
|---|---|---|---|---|
| Hallazgo de seguridad en los medios de pago | Incidencia | PRY-199, 202, 203, 209 | no identificado | 2026-10-03 a 2026-10-14 |
| La prueba de carga de temporada no alcanzó el umbral y se repite | Incidencia | PRY-199, 203, 211 | no identificado | 2026-10-11 a 2026-10-14 |
| Dos semanas perdidas por rotación de un desarrollador clave | Incidencia | PRY-201, 208, 210 | no identificado | 2026-09-27 a 2026-10-12 |
| El proveedor podría no llegar con el equipo completo para la siguiente fase | Riesgo | PRY-201 | no identificado | 2026-10-15 |

La decisión para el comité del 2026-10-22 sería quién es el doliente de cada incidencia transversal y para cuándo se resuelve. El riesgo de PRY-201 sube porque su dueño es externo y nadie lo anotó.

### Detectados en reuniones, no registrados
| Qué | Tipo | Dicho en | Fecha |
|---|---|---|---|
| El proveedor podría no llegar con el equipo completo para la siguiente fase | Riesgo | Notas de PRY-201: "nadie lo anotó como riesgo" | 2026-10-15 |

Es el único. Las otras 13 minutas solo traen compromisos, y no inventé ningún riesgo. PRY-201 tiene dos proveedores (CT-963 y CT-978) y la nota no dice de cuál habla. La ficha ya lo contiene, con probabilidad, impacto, doliente y fecha en "no declarado".

### Sin doliente o sin fecha
Los 35 ítems carecen de doliente y de fecha de resolución, y no rellené ninguno.
- **15 riesgos:** faltan doliente, fecha, probabilidad e impacto.
- **12 incidencias:** solo traen fecha de inicio.
- **8 dependencias:** falta el doliente, nombrar la contraparte, la confirmación y la fecha.

### Dependencias en riesgo
No pude cruzar dependencias entre proyectos. Las 13 actas dicen "Ninguna declarada", pero eso no prueba que no existan. Las 8 dependencias son de proveedor y ninguna está confirmada. El informe más reciente de cada uno dice que el proveedor no ha confirmado la fecha.

### Lo que debe verificar
- **Texto idéntico en proyectos que no se parecen.** El "hallazgo de seguridad en los medios de pago" aparece también en Iluminación LED (PRY-199) y la "prueba de carga de temporada" en esa misma, y la "rotación de un desarrollador" en Etiquetas electrónicas (PRY-210). Puede ser texto de plantilla copiado en los informes. Conviene confirmarlo con cada gerente antes de llevarlo a comité.
- **"Congelamiento de cambios en temporada alta"** (PRY-201, 203, 204, 208 y 211) es una restricción conocida, no algo incierto. Lo dejé como riesgo porque los informes lo llaman así.
- **PRY-201:** el despliegue en la cadena vence el 2026-10-16 y sigue pendiente sin evidencia, con 39 % declarado. La ficha del PM da fin al 2026-12-07. No es un ítem RAID; es tema para `/health-check`.
- No encontré mitigaciones con fecha en ninguna ficha, así que no pude revisar mitigaciones vencidas.

El registro completo de 35 ítems, uno por fila con su fuente, está en el archivo de salida.

### Después
Puedo subir a comité las tres incidencias transversales y el riesgo del proveedor de PRY-201, y proponer un doliente para cada ítem sin doliente. Propondría, no asignaría.

**Corrida registrada:** `2026-10-15-raid-log-1`, 61 segundos, 13 proyectos. La salida completa está en `estado/corridas/salida-raid-log.md`.