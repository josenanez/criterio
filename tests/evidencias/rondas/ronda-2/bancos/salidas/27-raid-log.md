# /criterio-portfolio:raid-log portafolio

Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-15), así que no hubo nada que aceptar de nuevo. Esta es la salida completa. Es idéntica a `estado/corridas/salida-raid-log.md`.

Fuentes: las 13 fichas de `estado/records/` (extraídas de los informes de avance, actas de constitución y comités, citados en cada fila), las minutas de comité de PRY-199, 200, 201, 202, 203, 204, 206, 208 y 210, y las notas de reunión de PRY-206 del 2026-10-15. Escala de valoración: no hay una definida en la configuración; se usaría alta/media/baja, y ningún ítem trae probabilidad ni impacto, así que no los relleno.

## RAID — Portafolio al 2026-10-15
6 riesgos · 0 supuestos · 14 incidencias · 13 dependencias (33 ítems en 13 proyectos)
33 sin doliente · 33 sin fecha · 0 con movimiento medible (ninguna ficha trae fecha de último movimiento) · 1 no registrado formalmente

**Id.** Los Id son de esta salida (`código-Rnn`), porque el registro de origen no numera sus ítems.

### Necesitan decisión ahora
| Id | Tipo | Qué | Doliente | Desde | Por qué sube |
|---|---|---|---|---|---|
| PRY-199-R01, PRY-201-R06, PRY-205-R16, PRY-207-R21 | dependencia | Calendario de liberaciones del core (PRY-199, 201, 205, 207) | sin doliente | sin fecha | Afecta a varios proyectos del portafolio y a ninguno le consta una contraparte; ningún acta declara la dependencia ni el código del proyecto del que depende |
| PRY-202-R10, PRY-207-R22, PRY-209-R29, PRY-210-R31, PRY-211-R32 | dependencia | El proveedor no ha confirmado la fecha de la última entrega (PRY-202, 207, 209, 210, 211) | sin doliente | sin fecha | Doliente fuera del proyecto sin respuesta registrada; cinco proyectos con la misma exposición |
| PRY-206-R20 | dependencia | El proveedor podría no llegar con el equipo completo a la siguiente fase (PRY-206) | sin doliente | 2026-10-15 | Dicho en reunión, nadie lo anotó; el gerente decide si lo formaliza (ver abajo) |
| PRY-200-R05, PRY-207-R23 | incidencia | La prueba de carga no alcanzó el umbral pactado y se repite (PRY-200, 207) | sin doliente | 2026-10-10 (PRY-200) · 2026-09-26 (PRY-207) | La de PRY-207 es la incidencia abierta más antigua del portafolio (19 días) y no tiene doliente |
| PRY-204-R15 | incidencia | Hallazgo de seguridad en la revisión de arquitectura (PRY-204) | sin doliente | 2026-10-12 | Incidencia sin doliente ni fecha; el informe no dice qué decisión pide |

No puedo afirmar que algún ítem lleve «más de dos períodos sin movimiento»: las fichas no registran cuándo se movió cada uno, solo cuándo apareció en un informe. Esa señal queda sin medir.

### Detectados en reuniones, no registrados formalmente
| Qué | Tipo | Dicho en | Fecha |
|---|---|---|---|
| El proveedor podría no llegar con el equipo completo para la siguiente fase («nadie lo anotó como riesgo») | dependencia (proveedor; la ficha lo traía como riesgo) | PRY-206 · `2026-10-15-notas-reunion.txt` | 2026-10-15 |

Es el único. Las otras nueve minutas de comité (PRY-199, 200, 201, 202, 203, 204, 206 del 10-12, 208 y 210) solo traen asistentes, temas «Avance» y «Compromisos», y una tabla de compromisos: no dicen nada de riesgos. Los compromisos vencidos o sin fecha de esas minutas son materia de `/pm-commitments`, no de este registro.

### Sin doliente o sin fecha
Los 33 ítems carecen de doliente y de fecha. Se reporta como hallazgo y no se rellena. Detalle por ítem en el registro completo (columnas Doliente y Fecha en «—»).

### Reclasificados (y por qué)
Trece ítems estaban como riesgo y pasan a dependencia:
- **Calendario del core** (PRY-199-R01, PRY-201-R06, PRY-205-R16, PRY-207-R21): depende de un tercero; no es incierto sino ajeno.
- **Equipo de seguridad** (PRY-201-R07, PRY-208-R25, PRY-209-R28): depende de la disponibilidad de un equipo ajeno al proyecto.
- **Proveedor que no ha confirmado la fecha** (PRY-202-R10, PRY-207-R22, PRY-209-R29, PRY-210-R31, PRY-211-R32): depende de un proveedor externo.
- **Proveedor sin el equipo completo** (PRY-206-R20): depende de un proveedor externo.

Se quedan como riesgo: concentración del conocimiento en una persona (PRY-200, 202, 204) y cambio regulatorio en discusión (PRY-203, 206, 208). Se quedan como incidencia las que ya ocurrieron (prueba de carga, rotación del desarrollador, hallazgo de seguridad, historias fuera del sprint, salida reprogramada). No encontré ningún supuesto registrado ni dicho en los documentos; no invento uno.

### Dependencias en riesgo
| Id | Depende de | Confirmada | Qué pasó |
|---|---|---|---|
| Las 13 dependencias (ver registro) | Ninguna lleva código de proyecto: son «el core», «el proveedor» o «el equipo de seguridad» | No: declaradas, no acordadas; ningún documento muestra confirmación de la contraparte | Las 13 actas de constitución dicen «Ninguna declarada» en dependencias, aunque los informes sí las reportan |

No puedo hacer el cruce de portafolio: sin código de proyecto no sé si «el core» es PRY-201 (Core de depósitos), y no lo asumo. Lo que sí consta: PRY-200, 202, 203, 207, 208 y 210 tienen cronograma posterior a la v1 (movieron fechas); PRY-199, 204, 205 y 211 reprogramaron la salida o tienen historias fuera por el core sin cronograma que lo refleje. Si el gerente confirma de qué proyecto depende cada una, el cruce se hace.

### Registro completo
El registro completo tiene los 33 ítems. Ninguno trae probabilidad, impacto, doliente, fecha ni último movimiento, así que esas columnas van en «—». Está en el archivo, con la fuente de cada fila. Aquí queda por proyecto (⟲ = reclasificado):

- **PRY-199:** R01 dependencia ⟲ (calendario del core), R02 incidencia (historias fuera del sprint), R03 incidencia (salida reprogramada sin cronograma).
- **PRY-200:** R04 riesgo (concentración del conocimiento), R05 incidencia (prueba de carga).
- **PRY-201:** R06 dependencia ⟲ (calendario del core), R07 dependencia ⟲ (equipo de seguridad), R08 incidencia (rotación de un desarrollador).
- **PRY-202:** R09 riesgo (concentración del conocimiento), R10 dependencia ⟲ (proveedor), R11 incidencia (salida reprogramada), R12 incidencia (historias fuera del sprint).
- **PRY-203:** R13 riesgo (cambio regulatorio).
- **PRY-204:** R14 riesgo (concentración del conocimiento), R15 incidencia (hallazgo de seguridad).
- **PRY-205:** R16 dependencia ⟲ (calendario del core), R17 incidencia (historias fuera del sprint), R18 incidencia (salida reprogramada).
- **PRY-206:** R19 riesgo (cambio regulatorio), R20 dependencia ⟲ (proveedor sin equipo completo, dicho en reunión).
- **PRY-207:** R21 dependencia ⟲ (calendario del core), R22 dependencia ⟲ (proveedor), R23 incidencia (prueba de carga).
- **PRY-208:** R24 riesgo (cambio regulatorio), R25 dependencia ⟲ (equipo de seguridad), R26 incidencia (rotación), R27 incidencia (historias fuera del sprint).
- **PRY-209:** R28 dependencia ⟲ (equipo de seguridad), R29 dependencia ⟲ (proveedor), R30 incidencia (rotación).
- **PRY-210:** R31 dependencia ⟲ (proveedor).
- **PRY-211:** R32 dependencia ⟲ (proveedor), R33 incidencia (salida reprogramada sin cronograma).

## Después
Subiría a comité (2026-10-22) con la decisión formulada: (1) quién es el doliente del calendario del core y de qué proyecto depende, para PRY-199, 201, 205 y 207; (2) quién gestiona con el proveedor la fecha de última entrega en PRY-202, 207, 209, 210 y 211. Para el resto propongo doliente, sin asignarlo: el gerente de cada proyecto (los nombres están en las fichas) como candidato natural. Es una propuesta; la asignación es de ustedes.

**Pie de rigor.** Salen de documentos: lo reportado en informes, actas y minutas, citado por ítem. No sé: qué se habló fuera de esos documentos, si algún ítem se movió desde su aparición, ni si hay dolientes o mitigaciones fuera de la ficha. No he modificado las fichas ni asignado nada. Criterio produce borradores de trabajo, no decisiones; la verificación es suya.

---

Tres cosas sobre cómo quedó la corrida:
- **Resumen del registro.** En el archivo guardado, el «Registro completo» es la tabla de 33 filas con su fuente. Aquí lo resumí por proyecto para acortarlo, así que lo que ves no es literalmente el archivo en esa sección.
- **Primera pasada.** Me equivoqué al registrarla: escribí «12 actas» en lugar de 13 y «9 reclasificados» en lugar de 13.
- **Corrección y tiempo.** Corregí el archivo y volví a registrar la corrida como `2026-10-15-raid-log-2`. Esa segunda corrida no tiene el tiempo medido, porque el marcador de arranque ya se había consumido con la primera. La medición válida (87 s) está en `2026-10-15-raid-log-1`, que conserva la nota con los errores.