# /criterio-roles:roles-setup talento/tba110315k21-tiendas-del-bajio-sinteticas

Norma quedó configurada para Tiendas del Bajío Sintéticas (RFC TBA110315K21, México) y ya produjo su primer reporte para 2026-11, con 8 puntos que atender.

**Una cosa que debe confirmar una persona:** el umbral de O*NET (desde qué importancia una destreza es exigible). Ningún documento lo fija, así que propuse **3.0**, el nivel «Importante» de la escala 1–5 de O*NET. Las señales de destrezas que faltan dependen de ese valor.

**Respuestas que tomé** (las sugeridas por los documentos):
- **Carpeta:** `talento/tba110315k21-tiendas-del-bajio-sinteticas`, la única candidata. Dejé la marca `_CRITERIO_TALENTO.txt`.
- **Periodo:** 2026-11.
- **Estándar:** O*NET (sintético), en `00-referencia/onet-31-0-sintetico/`. Lo comprobé con 41-2011.00 · Cashiers.
- **Estudios frente a la CINE:** Secundaria = 2 y Licenciatura = 6. Con O*NET esta señal no se calcula.
- **Revisión de perfiles:** cada 12 meses. Lo dice la política.
- **Lo que un perfil no puede pedir:** edad, sexo, estado civil, fotografía y apariencia. Lo dice la política.
- **Términos v1.6:** José Francisco Ñáñez los aceptó el 2026-11-16. Comprobantes en `.criterio/terminos/aceptacion-criterio-roles-0.1.0-2026-11-16.md` y `.pdf`.

**El reporte** está en `estado-talento/tba110315k21-tiendas-del-bajio-sinteticas/perfiles/2026-11/reporte-profile-check.md`. Lo que encontré:
- **Sin ocupación:** PT-04 · Almacenista no tiene código de ocupación. No le registré uno por mi cuenta.
- **Revisión vencida:** PT-01 · Cajero de tienda debía revisarse el 2026-01-10 (310 días).
- **Lo que falta frente a la ocupación:** a los dos perfiles de caja les faltan destrezas y conocimientos de su ocupación. Son 3 en PT-01 y 2 en PT-02.
- **Requisito sin tarea:** «Buena presencia», en PT-01, no se apoya en ninguna tarea.

El cálculo también encontró requisitos que la ley o la política no permiten pedir: «Profesar la religión católica» en PT-03, «Mujer entre 20 y 30 años» en PT-04 y «Buena presencia» en PT-01. También vio que los dos perfiles de caja se solapan. Eso no sale en este reporte: lo muestran `/criterio-roles:profile-language` y `/criterio-roles:profile-map`. El reporte tampoco trae la atribución que pide O*NET («O*NET 31.0 Database, USDOL/ETA»); hay que agregarla si se comparte.

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta prueba nadie podía darlo. Se corre a mano con `/criterio-roles:roles-wake`.

La configuración está en `.criterio/perfiles/TBA110315K21/config.json` y la corrida quedó registrada como `2026-11-16-roles-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.