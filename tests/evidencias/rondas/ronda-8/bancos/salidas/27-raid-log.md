# /criterio-portfolio:raid-log portafolio

## RAID del portafolio (PRY-199 a PRY-211) al 2026-10-17

El registro RAID del portafolio está hecho y la corrida quedó registrada. Salió de las fichas de los 13 proyectos, los informes de avance, 15 minutas y notas de reunión, las actas de constitución y, para PRY-202, la solicitud de cambio CC-01 y el cronograma v2. Leí el texto convertido de los documentos, no los originales PDF, DOCX ni XLSX.

Ningún documento trae probabilidad ni impacto, así que esas columnas dicen «no informado». Los ids de ítem (por ejemplo `199-D1`) los puse yo, solo para poder referirme a cada uno.

**Cifras:** 32 ítems en total: 8 riesgos, 0 supuestos, 14 incidencias y 10 dependencias. Ninguno tiene doliente ni fecha de resolución. Uno es un riesgo que nadie registró formalmente. Si ítems llevan «sin movimiento» no lo sé: cada ítem aparece en un solo informe y no hay historial.

- **Las actas no declaran dependencias.** Las 13 dicen «Ninguna declarada», pero los informes reportan 10. Reclasifiqué 10 ítems que los informes listaban como riesgos: el calendario de liberaciones del core (PRY-204, 209, 211), la fecha sin confirmar del proveedor (PRY-202, 203, 210) y la disponibilidad del equipo de seguridad (PRY-199, 201, 206, 208).
- **Riesgo no registrado:** en las notas de PRY-202 del 2026-10-17 se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase, y nadie lo anotó. No encontré otros en las demás minutas. PRY-200, 206, 207 y 209 no tienen minutas.
- **Informes vencidos:** con el umbral de 15 días de silencio, los de PRY-206 (24 días), PRY-200 (23) y PRY-211 (20) están desactualizados.

**Necesitan decisión ahora**, porque afectan a varios proyectos o no tienen doliente:
- **Calendario del core.** Afecta a 6 proyectos (204, 209, 211, y las historias fuera del sprint en 201, 203 y 208). Los informes dicen «el core» sin código de proyecto, así que no puedo afirmar que sea PRY-201.
- **Equipo de seguridad.** Hay 4 revisiones finales que dependen de él y 5 hallazgos de seguridad abiertos con redacción idéntica. Esa repetición puede ser plantilla. Se asume que el equipo es ajeno a los proyectos, pero los informes no lo dicen.
- **PRY-202.** El proveedor no confirma la fecha de la última entrega. El cronograma v2 ya movió la salida a producción de 2027-04-14 a 2027-06-29 (+76 días), pero CC-01 sigue pendiente de presentarse al comité.
- **Cambio regulatorio en discusión** (PRY-205 y PRY-208), sin doliente.

El archivo completo, con todas las tablas y el pie de rigor, está en `estado/corridas/salida-raid-log.md`. Lo que no sé: si «el core» es PRY-201, de quién es el equipo de seguridad y el movimiento real de los ítems.

Para el comité del 2026-10-20 puedes subir esas cuatro decisiones. Puedo proponer dolientes, sin asignarlos, y tú decides si formalizas el riesgo de PRY-202.