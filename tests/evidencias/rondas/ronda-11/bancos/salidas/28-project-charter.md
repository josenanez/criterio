# /criterio-portfolio:project-charter PRY-208 revisar

Revisé el acta de PRY-208 (Motor de decisión) y dejé la corrida registrada. La revisión completa está en `/tmp/claude-0/-home-claude/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/r11/bancos/espacio/estado/corridas/salida-project-charter.md`.

**Acta previa:** sí existe, aprobada el 2025-05-28. Los términos v1.2 ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-23), así que no los registré otra vez.

**Qué falta y qué consecuencia tiene:**
- **Autoridad del gerente:** no está en el acta ni en el informe. Rubén Cárdenas no tiene un monto ni un tipo de cambio que pueda decidir sin comité. Hoy hay dos historias fuera del sprint y un hallazgo de seguridad, y nadie sabe quién decide qué.
- **Objetivo de negocio:** el acta dice «Entregar motor de decisión para Tecnología», que es la solución, no el objetivo. Así no se puede juzgar si el 63 % de avance acerca al negocio a algo.
- **Alcance y exclusiones:**
  - El alcance son tres marcadores, «Componente 1, 2, 3», sin contenido.
  - La exclusión es «lo que otro proyecto cubre», sin nombrar el proyecto.
  - Con eso no se puede decidir si las dos historias que quedaron fuera son un cambio de alcance.
- **Criterio de éxito:** «en producción y medido» no es medible, y no dice quién lo mide.
- **Sin definir:** supuestos, restricciones, hitos y cadencia del comité.
- **Dependencias:** el acta dice «Ninguna declarada», pero el informe cita una dependencia con el core y un proveedor sin fecha de entrega.
- **Sí están:** patrocinador (Felipe Arango), gerente y Comité de Riesgos.

**Lo que el acta ya no sostiene:** el cierre comprometido era el 2026-05-21 y venció hace 155 días, un 45 % de la duración planificada, con umbral de 10 %. El informe de hoy declara **verde** con 63 % de avance. La ficha solo tiene la línea base original, sin ninguna replanificación aprobada. Del presupuesto, el informe declara comprometido el 67 %, ejecutado el 47 % y proyección al cierre del 97,5 % de los 18.000 MM COP; esas cifras no las verifiqué.

Dejé como pendiente de definir todo lo que ningún documento sustenta. No inventé nada.

**Lo que no sé:**
- Si existe una replanificación o una política de autoridad fuera de la carpeta.
- Qué son los componentes 1, 2 y 3.
- Por qué el registro de la corrida muestra cero señales automáticas para PRY-208 pese a la fecha vencida. Eso hay que mirarlo aparte.

**Siguientes pasos que ofrezco:**
- Llevar la definición de autoridad al comité con `/steering-pack`.
- Pasar los supuestos implícitos al registro RAID con `/raid-log`.
- Abrir un control de cambios por la fecha vencida con `/change-control`.