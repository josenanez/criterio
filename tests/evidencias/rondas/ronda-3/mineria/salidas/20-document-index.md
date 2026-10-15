# /criterio-portfolio:document-index 

## Carpeta al 2026-10-15

**Documentos:** 80 · **Sin cambio:** 80 · **Hay que releer:** 0

No hay documentos nuevos, cambiados, reguardados, renombrados ni borrados, y el índice no reportó formatos ilegibles. No hace falta `/portfolio-scan`.

**Citas que dejaron de resolver:** hay 11, todas de PRY-203, en los campos `pm_record.identity.{code, name, business_area, product, sponsor, manager, committee}`, `pm_record.plan.{start_date, end_date}` y `pm_record.money.{currency, approved}`. Todas citan `00-gobierno/2025-09-21-acta-constitucion.md`.

El acta no se borró ni se renombró. Está en `PRY-203-despacho-automático-de-flota/00-gobierno/2025-09-21-acta-constitucion.md`. La sección `pm_record` de la ficha la cita sin la carpeta del proyecto, y el resto de la ficha sí la cita completa. El fallo está en la cita, no en el documento.

No corregí nada. Propongo cambiar las 11 citas a la ruta completa, una por una y mostrando el cambio, si lo aprueban.

**Términos:** ya estaban vigentes (v0.3.9, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

**Corrida:** quedó registrada como `2026-10-15-document-index-1`, con la salida guardada en `estado/corridas/salida-document-index.md`. Tardó 28 segundos. El registro no recoge el número de documentos leídos, porque este comando solo cuenta y compara hashes.