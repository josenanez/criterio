# /criterio-portfolio:raid-log portafolio

## RAID del portafolio Cooperativas al 2026-10-23

El portafolio tiene 33 ítems en el registro: 11 riesgos, 12 incidencias, 10 dependencias y 0 supuestos. Ninguno tiene doliente ni fecha.

**De dónde sale:**
- Las 13 fichas de `estado/records/`.
- Las secciones «Dependencias declaradas» de las 13 actas de constitución.
- Las 17 minutas y notas de reunión.
- Las solicitudes de cambio CC-01 de PRY-203 y PRY-210.

**Términos:** ya estaban vigentes (v1.2, José Francisco Ñáñez, 2026-10-23), así que no los volví a registrar.

**Qué no sé:**
- Ningún documento trae doliente, fecha, probabilidad, impacto ni mitigación de ningún ítem, y no rellené nada.
- Sin historial de movimiento por ítem no puedo decir cuáles llevan dos períodos quietos. 21 ítems quedan «sin dato».
- Las 13 actas dicen «Ninguna declarada» en dependencias, y nadie levantó supuestos. Por eso el registro de supuestos está vacío por falta de documentos, no porque no existan.

**Reclasificados (10, de riesgo a dependencia).** Aplicó la prueba «depende de alguien fuera del proyecto». Cada gerente tiene que confirmarlo.
- **Proveedor del core cooperativo** (PRY-202, 204, 206, 209): el propio texto lo describe como dependencia.
- **Proveedor sin fecha confirmada** (PRY-200, 211): el proveedor no ha confirmado la fecha de la última entrega.
- **Aprobación del reglamento por el Consejo** (PRY-199, 201, 206, 207): es la reclasificación más discutible, porque la aprobación depende de un órgano ajeno al proyecto.
- Ninguna lleva código de proyecto de destino, porque nadie lo declaró y no lo asigné.

**Detectado en reuniones y no registrado (1).** El 2026-10-23, en las notas de PRY-206, se comentó que el proveedor podría no llegar con el equipo completo a la siguiente fase, y nadie lo anotó como riesgo. Lo dejé como riesgo y no como dependencia; es criterio mío. Las otras 16 minutas solo traen compromisos.

**Necesitan decisión ahora:**
1. **Reglamento del Consejo.** El Consejo pidió ajustes en PRY-203, 204 y 208, y la aprobación sigue pendiente en PRY-199, 201, 206 y 207. Son 7 proyectos. El piloto de PRY-203 es el 2026-12-04.
2. **Proveedor del core.** Afecta a PRY-204, 206 y 209 y al propio PRY-202. La ficha de PRY-202 no registra proveedor ni contrato, así que no puedo decir que la dependencia sea de ese proyecto.
3. **Hallazgo de seguridad en PRY-201.** Está abierto desde el 2026-10-20, sin doliente ni severidad, en un proyecto declarado verde.
4. **Salida sin fecha en PRY-200 y PRY-211.** Se reprogramó por el cierre contable y no hay nueva fecha en ningún cronograma.
5. **Prueba de carga.** El mismo texto, «no alcanzó el umbral pactado y se repite», aparece en PRY-200, 201, 202, 205 y 209, y nadie lo vinculó como un solo asunto.

**Dependencias en riesgo:**
- El cruce está incompleto, porque ninguna dependencia lleva código de destino.
- PRY-202 no movió su línea base (fin 2027-04-09).
- Su hito de integración con el core está pendiente para 2027-04-09. PRY-203 marca su propia integración con el core como cumplida el 2026-09-22, sin acta de recibo. No sé si es una contradicción o son integraciones distintas, y hay que preguntarlo.

**Siguiente paso, si quieres:** puedo preparar para comité las cinco decisiones de arriba y proponer dolientes para los 33 ítems. Propondría, no asignaría. No hice ninguna de las dos cosas.

La corrida quedó registrada como `2026-10-23-raid-log-1`, con el caso «portafolio» y 163 segundos medidos. Los 67 hallazgos que muestra el registro de la corrida son señales de otras revisiones de las fichas, no de este RAID. El registro completo de los 33 ítems, con la tabla entera, está en `estado/corridas/salida-raid-log.md`.

Esto es un borrador de trabajo, no una decisión ni asesoría. Sale solo de los documentos citados; no sé lo que se habló fuera de ellos.