# /criterio-portfolio:raid-log portafolio

## RAID del portafolio (13 proyectos, PRY-199 a PRY-211) al 2026-10-14

**Documentos de los que sale:** las 13 fichas en `estado/records/`, los informes de avance, las actas de constitución, 9 minutas de comité y las notas de PRY-208 del 14/10. Los términos v1.0 ya estaban aceptados en la configuración (José Francisco Ñáñez, 2026-10-14).

**Conteo:**
- **Registrado:** 20 riesgos, 0 supuestos, 24 incidencias y 0 dependencias, es decir 44 ítems.
- **Tras reclasificar:** 8 riesgos, 18 incidencias, 12 dependencias y 6 ítems que no son RAID.
- **Sin doliente ni fecha:** los 44. Tampoco traen probabilidad, impacto ni mitigación. Lo reporto como hallazgo y no lo rellené.
- **No registrado formalmente:** 1.

**Necesitan decisión ahora:**
- **D1, proveedor del core (PRY-202, 205, 206, 207, 208, 209, 211):**
  - Estaba como riesgo, pero es una dependencia. Afecta a 7 proyectos y nadie es doliente.
  - Las actas de PRY-201, 202, 208 y 209 dicen "Ninguna declarada" en dependencias.
  - Si "el core" es PRY-202 (inferencia mía, ningún documento lo dice), su línea base venció el 2026-04-25, hace 172 días. Sigue con 43 % y sin replanificación.
- **D2, aprobación del reglamento por el Consejo (PRY-202, 204, 208, 211):** un mismo órgano externo frena a 4 proyectos. En PRY-200, 202 y 209 el Consejo ya pidió ajustes, así que ahí ya pasó.
- **D3, hallazgo de seguridad (PRY-201, 205, 209, 210, 211):** es una incidencia abierta en 5 proyectos, sin doliente, fecha ni evidencia de cierre.
- **D4, PRY-208:** el proveedor podría no llegar con el equipo completo a la siguiente fase.

**Detectado en reunión y no registrado:** solo uno, el de D4. Está en las notas de PRY-208 del 2026-10-14 ("nadie lo anotó como riesgo"). La ficha ya lo recoge con el doliente en "no encontrado", pero no está en el informe del 11/10. Las demás minutas solo traen "Avance" y "Compromisos", y no inventé ningún riesgo.

**Reclasificaciones:**
- **De riesgo a dependencia (12):** el proveedor del core (7), la aprobación del Consejo (4) y la fecha sin confirmar en PRY-209 (1). Todas dependen de alguien fuera del proyecto.
- **No son RAID (6):**
  - Dos del plan de pruebas (PRY-201 y 203).
  - Dos del concepto del supervisor recibido (PRY-203 y 210).
  - Dos del componente del proveedor pendiente de aceptación (PRY-202 y 204), que es tema de vendor-tracking.

**Lo que no pude saber:**
- **Movimiento:** hay una sola fotografía por ítem, así que no puedo medir "sin movimiento en dos períodos".
- **Texto repetido:** frases como "El equipo perdió dos semanas…" se repiten palabra por palabra en 6 proyectos. No sé si todos lo viven o si se copió.
- **Proveedor del core:** ningún documento lo nombra ni lo liga a un código de proyecto.

**Siguiente paso (queda a tu decisión):** subir D1 a D4 al comité del 2026-10-21 y proponer doliente para los 44 ítems. Propongo, no asigno.

El registro completo está en `estado/corridas/salida-raid-log.md`, y la corrida quedó registrada como `2026-10-14-raid-log-1`. No pude registrar cuántos documentos se leyeron porque el script no lo midió.