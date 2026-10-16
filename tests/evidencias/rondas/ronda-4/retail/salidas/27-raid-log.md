# /criterio-portfolio:raid-log portafolio

Levanté el RAID del portafolio al 2026-10-15 y registré la corrida como `2026-10-15-raid-log-1`. Salió de las 13 fichas, los informes, las actas, las minutas de octubre y las notas del PRY-209. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré otra vez.

**Conteo:** 18 riesgos, 6 incidencias, 2 dependencias y 0 supuestos, más 1 riesgo no registrado.

**Lo que más pesa**
- **Hallazgo de seguridad en medios de pago:** aparece con el mismo texto como incidencia en PRY-200, 201, 204 y 211, sin doliente en ninguno. Tres de esos cuatro proyectos reportan verde. Los documentos no dicen si es un solo hallazgo o cuatro.
- **Prueba de carga de temporada:** no alcanzó el umbral pactado en PRY-204 y PRY-209, sin doliente en ninguno.
- **Único riesgo no registrado:** en las notas del PRY-209 del 2026-10-15 se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase, y nadie lo anotó. Las demás minutas de octubre solo traen compromisos.

**Falta información en todo el registro.** Los 26 ítems registrados no tienen doliente, fecha ni valoración. Lo reporté como hallazgo y no rellené nada. Tampoco pude medir "sin movimiento", porque ningún ítem trae fecha de último movimiento.

**Reclasificación.** "El proveedor no ha confirmado la fecha de la última entrega" (PRY-200 y 206) pasó de riesgo a dependencia, porque la entrega es de un tercero. Quedan como dependencias declaradas, sin confirmar.

**Cruce de dependencias.** No se pudo hacer: las 13 actas dicen "Ninguna declarada". Dejé una pregunta abierta: 9 proyectos tienen un hito de "Integración con el ERP" y existe el PRY-209 (migración del ERP), pero ningún documento dice que dependan de él.

**Límites.** No leí los PDF sin texto extraído: el acta de recibo del PRY-199 y las actas de recibo en PDF del PRY-211. Si traen riesgos, no están aquí.

Quedan dos pasos que son tuyos: subir a comité (próximo 2026-10-29) los tres puntos de decisión, y proponer un doliente por ítem. Propuse al gerente de cada proyecto, salvo en el hallazgo de pagos y la prueba de carga, que cruzan proyectos y necesitan una sola persona nombrada por el comité.

El registro completo está en `estado/corridas/salida-raid-log.md`.