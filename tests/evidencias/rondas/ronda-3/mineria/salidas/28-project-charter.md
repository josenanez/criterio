# /criterio-portfolio:project-charter PRY-200 revisar

Revisé el acta de PRY-200 (Mantenimiento predictivo de camiones, del 2026-03-23) y le faltan los campos de gobierno que importan. Los términos estaban vigentes (v0.3.9, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrar nada nuevo. Corrí el modo revisar con solo dos documentos: el acta y el informe de avance del 2026-10-14.

**Qué falta y qué consecuencia tiene**

| Campo | Estado | Consecuencia |
|---|---|---|
| **Autoridad del gerente** | Ausente | Todo ajuste de alcance o presupuesto sube al Comité de Operaciones. La proyección al cierre (9.776.375.957 COP) ya supera lo aprobado (9.500.000.000 COP) en 276.375.957 COP (+2,9 %), y no se puede saber si Rubén Cárdenas puede absorberlo. |
| Objetivo de negocio | Es la solución repetida, sin problema que resolver | No hay base para decidir si el proyecto vale su costo cuando se retrasa. |
| Alcance | "Componente 1, 2 y 3" sin descripción | No se distingue un cambio de alcance de una aclaración. |
| Exclusiones | "Lo que otro proyecto cubre", sin nombrar cuál | Si dos proyectos construyen lo mismo, nadie lo ve. |
| Criterio de éxito | "En producción y medido", sin métrica ni quién mide | El cierre queda a discreción de quien lo declare. |
| Supuestos, restricciones y cadencia del comité | Ausentes | El acta no registra al proveedor sin fecha de última entrega, que el informe ya menciona como riesgo. |
| Hitos | Solo inicio (2026-04-02) y cierre (2027-03-24) | El 42 % de avance declarado no se puede contrastar con nada. |

Patrocinador (Laura Vélez), gerente (Rubén Cárdenas), presupuesto y fechas sí están.

Los campos que faltan quedaron marcados como pendientes de definir; no completé ninguno.

**Siguientes pasos que ofrezco**
- **Autoridad del gerente:** llevar esa definición al Comité de Operaciones, que según la configuración se reúne el 2026-10-19. Se puede preparar con `/criterio-portfolio:steering-pack`.
- **Supuestos:** pasar los que salieron de la revisión al registro RAID con `/criterio-portfolio:raid-log`.

La corrida quedó registrada como `2026-10-15-project-charter-1`, con el texto completo en `salida-project-charter.md`. Dos cosas de ese registro:
- La corrida figura sobre 13 proyectos aunque el caso es PRY-200.
- Los 63 hallazgos que lista son señales abiertas de todo el portafolio, no de esta revisión. Para PRY-200 no lista ninguno.

Archivos (dentro de `/home/claude/banco/ronda-3/mineria/espacio/estado/corridas/`):
- `salida-project-charter.md`
- `2026-10-15-project-charter-1.md`