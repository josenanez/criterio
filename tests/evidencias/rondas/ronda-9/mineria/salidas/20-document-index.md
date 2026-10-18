# /criterio-portfolio:document-index 

## Carpeta al 2026-10-17

**Documentos:** 76 · **Sin cambio:** 76 · **Hay que releer:** 0

Sin cambios de contenido, reguardados, renombrados, movidos ni borrados. No hay nada que releer, así que no hace falta `/portfolio-scan`.

### Citas que dejaron de resolver
Hay 22 citas rotas, todas de **PRY-211**. Los documentos citados sí existen en la carpeta. Lo que no resuelve es la ruta con la que están escritas.

| Documento citado | Campos de PRY-211 |
|---|---|
| `00-gobierno/2025-05-16-acta-constitucion.md` | 13: code, name, business_area, product, authority, sponsor, manager, committee, start_date, scope_summary, exclusions, currency, approved |
| `20-seguimiento/2026-10-14-informe-avance.md` | 7: phase, declared.status, progress_pct, as_of, committed, executed, projection |
| `10-plan/2026-10-14-cronograma-v2.xlsx` | 1: end_date |
| `20-seguimiento/2026-08-30-factura-ct-110.pdf` | 1: vendors[0].invoiced |

La causa probable es una ficha duplicada en `estado/PRY-211-control-de-polvo-en-vías/records/PRY-211.json`. Sus citas no llevan el prefijo de la carpeta del proyecto. La ficha de `estado/records/PRY-211.json` sí lo lleva. No verifiqué cuál de las dos es la vigente y no corregí nada.

Si quieres, reviso y corrijo las citas de la ficha duplicada, mostrando cada cambio.

### Formatos que no se pudieron leer
Ninguno. Este comando cuenta y compara, no lee contenido.

La corrida quedó registrada como `2026-10-17-document-index-1`, con el resultado en `estado/corridas/salida-document-index.md`. Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17, así que no los registré de nuevo.