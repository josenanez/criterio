# /criterio-portfolio:raid-log portafolio

Terminé el registro RAID del portafolio al 2026-10-17 y dejé la corrida registrada. Sale de las 13 fichas de PRY-199 a PRY-211, de las reuniones de siete proyectos y de las actas de constitución. Los términos ya estaban vigentes a nombre de José Francisco Ñáñez, así que no los registré de nuevo.

**Conteo:** 12 riesgos, 0 supuestos, 18 incidencias y 8 dependencias. Ningún riesgo, incidencia ni dependencia tiene doliente. Los 12 riesgos tampoco tienen fecha, probabilidad ni impacto, y no los rellené.

**Lo que más pesa:**
- **Dependencias reclasificadas:** ocho ítems figuraban como riesgos y los pasé a dependencias porque dependen de un tercero. Son tres «proveedor del core cooperativo» (PRY-199, 206 y 209) y cinco «proveedor sin fecha confirmada» (PRY-201, 207, 208, 209 y 211).
- **Dependencia del core:** ninguna acta declara dependencias y ninguna cita un código de proyecto. PRY-202 (Core cooperativo) es el candidato, pero ningún documento lo confirma. Si lo fuera, su cierre de línea base (2026-05-16) ya venció.
- **Riesgo no registrado:** en las notas de PRY-200 del 2026-10-17 se dijo que el proveedor podría no llegar con el equipo completo para la siguiente fase. Soluciones Solidarias es proveedor de PRY-200 y PRY-199. Que sea el mismo proveedor de las notas es una inferencia mía, porque las notas no lo nombran.
- **Incidencias repetidas sin doliente:** la prueba de carga bajo el umbral aparece en cuatro proyectos y el hallazgo de seguridad en tres.
- **Por revisar:** «Se ajustó el plan de pruebas con seguridad» (cuatro proyectos) describe una acción ya hecha, no un problema abierto. No lo reclasifiqué; lo dejé marcado.

**Lo que no sé:**
- Quién es el doliente de cada ítem.
- Cuándo se movió cada ítem por última vez. Por eso no puedo decir cuáles llevan dos períodos quietos.
- Si hay algún supuesto: nadie levantó ninguno.
- Qué es nuevo y qué se cerró: no hay un RAID previo con el que comparar.

La corrida quedó registrada con sus 69 señales abiertas. La salida completa está en `estado/corridas/salida-raid-log.md`.

Puedo preparar la decisión formulada de los ítems que cumplen el criterio de escalamiento (los que afectan a otro proyecto) para el comité del 2026-10-24, y proponer dolientes sin asignarlos. No lo hice: espero tu indicación.