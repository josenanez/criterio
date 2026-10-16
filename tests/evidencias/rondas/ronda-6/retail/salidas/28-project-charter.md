# /criterio-portfolio:project-charter PRY-202 revisar

Revisé el acta de PRY-202 (Centro de distribución norte) y dejé la corrida registrada como `2026-10-16-project-charter-1`.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no hubo que volver a registrarlos.

Hay acta previa, aprobada el 2025-08-03. Lo que le falta y lo que eso provoca:

- **Autoridad del gerente:** no está declarada. Por eso la reprogramación del despliegue que reporta el informe no se puede clasificar como decisión de Andrés Lozano o como cambio que debía ir al Comité de Arquitectura.
- **Objetivo, alcance y exclusiones:** el objetivo es la solución, no un resultado medible. Los tres componentes no se describen. Las exclusiones dicen solo "lo que otro proyecto cubre", sin nombrar proyecto.
- **Supuestos, restricciones y dependencias:** ausentes, y el acta declara "Ninguna" dependencia. Los dos riesgos del informe, la regulación de datos personales y los jefes de tienda para el piloto, son supuestos que nunca se declararon y hoy no tienen dueño.
- **Criterio de éxito, hitos y cadencia:** el criterio ("en producción y medido") no dice qué se mide ni quién lo mide. No hay hitos, y tampoco cadencia del comité.
- **Fecha de cierre:** el cierre pactado era el 2026-04-24 y venció hace casi seis meses. El informe sigue en verde con 55 % de avance. No da nueva fecha, y no hay cambio de línea base aprobado.

El patrocinador (Elena Duarte) sí está con nombre. No completé ningún campo faltante: quedaron como pendientes de definir.

Leí solo dos documentos (el acta y el informe del 2026-10-16), así que no sé qué se acordó fuera de ellos.

Siguientes pasos que ofrezco:
- Llevar la definición de la autoridad del gerente al Comité de Arquitectura como decisión.
- Pasar los supuestos al registro RAID.
- Tratar el cierre vencido con `/change-control`.

Archivos están en `/home/claude/banco/ronda-6/retail/espacio/estado/corridas/`:
- `salida-project-charter.md`
- `2026-10-16-project-charter-1.md`