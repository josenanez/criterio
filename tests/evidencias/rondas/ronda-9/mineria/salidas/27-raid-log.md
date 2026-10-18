# /criterio-portfolio:raid-log portafolio

## RAID del portafolio al 2026-10-17

El registro RAID del portafolio tiene 36 ítems en las 13 fichas: 15 riesgos, 14 incidencias, 7 dependencias y 0 supuestos. Ninguno tiene doliente, fecha, probabilidad ni impacto. Los términos ya estaban aceptados (José Francisco Ñáñez, 2026-10-17, versión 1.1), así que seguí.

**De dónde sale.** Leí las 13 fichas, las 13 actas de constitución y las minutas y notas de reunión disponibles. La corrida quedó en `estado/corridas/2026-10-17-raid-log-1.md`, con la salida completa en `estado/corridas/salida-raid-log.md`.

**Necesitan decisión ahora**
- **Licencia ambiental:** el riesgo "cambio en la licencia ambiental" aparece en PRY-199, 201, 204, 207 y 210.
- **Vía de acceso:** el riesgo "bloqueo de la vía de acceso" aparece en PRY-202, 204, 206 y 209.
- **Hallazgo de auditoría de seguridad:** es una incidencia en PRY-200, 208 y 210.
- **Ensayo de disponibilidad:** el primer ensayo no alcanzó lo pactado y se repite en PRY-206, 207, 208 y 210.
- **PRY-200:** el riesgo "concentración del conocimiento" y la incidencia "dos semanas perdidas por rotación de un ingeniero clave" salen en el mismo informe. El riesgo parece haber ocurrido ya.

**Detectado en reuniones.** Solo encontré un ítem no registrado formalmente. Está en las notas de PRY-211 del 2026-10-17: el proveedor podría no llegar con el equipo completo para la siguiente fase. Las demás minutas solo traen compromisos.

**Reclasificaciones.** Propongo pasar 7 ítems de riesgo a dependencia: cuatro del proveedor (PRY-203, 205, 208 y 211) y tres de la ventana de parada de Operaciones (PRY-200, 202 y 206). No modifiqué las fichas; cada gerente tiene que confirmarlo.

**Lo que no pude hacer**
- **Cruce de dependencias entre proyectos:** las 13 actas dicen "Ninguna declarada". Que nadie las haya declarado no prueba que no existan.
- **Movimiento de los ítems:** las fichas no guardan historial, así que no pude medir si llevan dos períodos sin moverse.
- **Mitigaciones vencidas:** no hay mitigaciones registradas, así que no hay nada que evaluar.

Dos cosas más conviene saber antes de actuar. Los mismos textos se repiten en 3 a 5 proyectos y puede ser un solo evento o texto de plantilla. Y los informes de PRY-204 (2026-09-28) y PRY-207 (2026-09-29) pasan del umbral de 15 días de silencio, así que su RAID puede estar desactualizado.

**Siguiente paso.** Ofrezco subir al comité del 2026-10-23 los cinco asuntos de arriba. La decisión a formular en cada uno es quién es el doliente y para qué fecha. Puedo proponer dolientes a partir de los responsables de las minutas, pero los documentos no dicen quién debería ser, así que sería una propuesta y no una asignación.

La corrida midió el tiempo (72 segundos), pero no el número de documentos leídos. Los 67 hallazgos de señales que muestra el registro de la corrida son del barrido general de las fichas, no del RAID.