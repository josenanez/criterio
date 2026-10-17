# /criterio-portfolio:raid-log portafolio

Hice el registro RAID de los 13 proyectos (PRY-199 a PRY-211) al 2026-10-17 y dejé la corrida registrada. Ningún ítem tiene doliente ni fecha, y no pude confirmar si «el core» es PRY-201. La evidencia es el archivo `estado/corridas/salida-raid-log.md`.

Los términos ya estaban vigentes (aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo.

**Qué hay en el registro**
- **Cifras:** hay 13 riesgos, 0 supuestos, 17 incidencias y 7 dependencias. Son 36 ítems registrados más 1 riesgo que nadie registró formalmente.
- **Reclasificados:** pasé 7 riesgos a dependencia. Son 4 de «el proveedor no ha confirmado la fecha» (202, 203, 207, 210) y 3 de «calendario de liberaciones del core» (201, 204, 208).
- **No registrado:** en las notas de PRY-205 del 2026-10-17 se dijo que el proveedor podría no llegar con el equipo completo para la siguiente fase. Las otras 15 minutas de comité solo traen compromisos.
- **Hallazgos de falta de datos:** ningún ítem tiene doliente. Los 19 riesgos tampoco tienen fecha, probabilidad ni impacto. No los rellené. PRY-207 lleva 23 días sin informe, por encima del umbral de 15.
- **Dependencias:** ninguna de las 13 actas declara dependencias con código de proyecto.

**Lo que subiría a comité**
1. PRY-201 movió su piloto de 2026-10-15 a 2027-01-30, y su CC-01 (+107 días) sigue pendiente de comité. Los proyectos 199, 200 y 202 reportan historias fuera del sprint por «dependencia con el core». Ningún documento dice que «el core» sea PRY-201, así que hay que confirmarlo.
2. Cuatro proyectos (203, 208, 209, 211) tienen un hallazgo de seguridad abierto, y cuatro (199, 203, 209, 211) registran el riesgo de disponibilidad del equipo de seguridad. Es el mismo cuello de botella.
3. En PRY-209, la factura FV-1258 supera en 365.708.982 COP el único entregable recibido del contrato CT-258. Además, la bolsa de horas vence el 2026-10-20.
4. PRY-211 recibió la salida a producción el 2026-10-17, pero su informe del 2026-10-16 sigue con el hallazgo de seguridad y la prueba de carga abiertos.

**Lo que no sé**
- Los dolientes, la probabilidad y el impacto de cualquier ítem.
- Qué proveedor es cada uno de los riesgos de proveedor.
- Algunas actas de recibo y cronogramas no los leí a fondo.
- Leí los documentos desde el caché de texto, no desde los originales.
- «Último movimiento» es la fecha del informe, no una fecha real de movimiento.

La corrida quedó como `2026-10-17-raid-log-1`. Tardó 109 segundos y registró 13 proyectos, con su nota. No se midió el número de documentos.