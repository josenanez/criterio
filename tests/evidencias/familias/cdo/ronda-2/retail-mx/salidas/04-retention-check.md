# /criterio-data-governance:retention-check 

Los términos 1.6 estaban vigentes, así que corrí el reporte con fecha de corte 2026-11-25. El motor lo escribió y quedó registrado como `2026-11-25-retention-check-1`. Los términos ya constaban como aceptados por José Francisco Ñáñez, con fecha 2026-11-25.

Hay cuatro señales abiertas.

**Conjuntos que conservan registros pasado su plazo**
- **DS-42, Candidatos a prácticas:** conserva registros desde 2022-01-01 y la política fija 24 meses. Todo lo anterior al 2024-11-25 pasó su plazo. Es responsabilidad de Gestión humana.
- **DS-04, Candidatos:** conserva registros desde 2023-06-01 con el mismo plazo de 24 meses. Todo lo anterior al 2024-11-25 pasó su plazo. También es de Gestión humana.

**Políticas con la revisión vencida**
- **Política de datos:** su revisión tocaba el 2025-06-30 y no hay una versión posterior.
- **Política de conservación:** su revisión tocaba el 2026-03-01 y no hay una versión posterior.

Los demás conjuntos están dentro de su plazo, y todo lo que llegó se procesó. Qué se archiva o se borra lo decide el dueño del dato con la política.

El registro de la corrida cuenta 13 hallazgos. El reporte lista solo las cuatro señales de arriba y no explica la diferencia.

El reporte completo, con las tablas de políticas y conjuntos, las preguntas que hizo y las fuentes, está en `estado-datos/rcm190305ab1-retail-central-sintetico/gobierno/2026-11/reporte-retention-check.md`. Lo mismo, tal cual, se guardó en `estado-datos/rcm190305ab1-retail-central-sintetico/corridas/salida-retention-check.md`. Este mensaje no repite las tablas; el reporte las trae completas.