# /criterio-assets:assets-setup tecnologia/155612345-2-2019-banco-del-istmo-sintetico

Soy Domingo. Pongo cada activo al lado de su dueño y su soporte, y cada proveedor al lado de su nivel; no elijo proveedores ni interpreto contratos.

**Carpeta:** encontré una sola candidata, `tecnologia/155612345-2-2019-banco-del-istmo-sintetico`, que tiene 00-politica/, 10-cambios/, 20-servicio/, 30-activos/, 40-proveedores/ y 50-nube/. Tomo esa. Trae 23 documentos; ninguno está fuera de lugar ni es ilegible.

**Respuestas** (sesión de prueba: en cada pregunta tomo la respuesta sugerida)
- **Entidad:** Banco del Istmo Sintético, 155612345-2-2019, Panamá, USD. Ya la había fijado el setup de Fausto.
- **Periodo:** 2026-10.
- **Licencias pagadas sin uso que se toleran:** 15 %, según la política de cambios y de niveles de servicio.
- **Tolerancia sobre el presupuesto de cada cuenta de la nube:** 5 %, según la misma política.
- **Publicar en Rostrum:** sí, porque la política no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-tecnologia/155612345-2-2019-banco-del-istmo-sintetico`, la misma carpeta que usa Fausto.
- **Términos 1.6:** José Francisco Ñáñez los aceptó el 2026-11-25. Este es el texto que aceptó: «Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal»
- **Marca `_CRITERIO_TECNOLOGIA.txt` en la carpeta:** sí.

**Listo.**
- La configuración está en `.criterio/activos/155612345-2-2019/config.json`.
- El comprobante de los términos está en `.criterio/terminos/aceptacion-criterio-assets-0.2.0-2026-11-25.md` y en el `.pdf` del mismo nombre.
- La marca quedó en la carpeta de la entidad.

**Primera ficha, periodo 2026-10.** Procesé las 2 actas del comité de arquitectura y los 4 contratos.
- **Excepciones:** van 2 a la ficha, A-320 hasta el 2026-09-30 y A-101 hasta el 2027-03-31. El acta solo menciona A-103 («se evaluará su reemplazo»), así que no tiene excepción.
- **Niveles de servicio:** van 4, cada uno con su crédito: Centro de Datos Uno, Enlaces del Pacífico, Mesa de Ayuda Sintética y Nube Andina.
- **Señales:** el cálculo dio 12 en total, 2 de cada una de estas clases: activo fuera de soporte, activo sin dueño, software usado sin licencia, licencias pagadas sin uso, proveedor que incumplió sin el crédito en su factura y cuenta de la nube por encima de su presupuesto.

Este reporte muestra solo las señales de los activos. Las de licencias, proveedores y nube salen con `/criterio-assets:license-check`, `/criterio-assets:vendor-check` y `/criterio-assets:cloud-check`.

# Cada activo con su dueño y su soporte · Banco del Istmo Sintético · periodo 2026-10

**Entidad:** Banco del Istmo Sintético (155612345-2-2019) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.2.0 · **Comando:** `asset-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-310 · Servidor de la base de datos de clientes: corre en producción y su fabricante terminó el soporte el 2025-12-31; no tiene una excepción aprobada | — | — | 329 | `30-activos/inventario_de_activos.xlsx` fila 8 |
| 2 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-320 · Sistema operativo del servidor de pagos: corre en producción y su fabricante terminó el soporte el 2026-06-30; su excepción venció el 2026-09-30 | — | — | 148 | `30-activos/inventario_de_activos.xlsx` fila 9 |
| 3 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-210 · Servidor de integración: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 6 |
| 4 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-220 · Balanceador de carga: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 7 |

## El resultado

| Activo | Dueño | Ambiente | Fin de soporte | Excepción hasta |
|---|---|---|---|---|
| A-100 · Sistema central | Infraestructura | Producción | 2028-12-31 | — |
| A-101 · Servidor de reportes | Infraestructura | Producción | 2026-03-31 | 2027-03-31 |
| A-102 · Servidor del laboratorio | Infraestructura | Pruebas | 2024-06-30 | — |
| A-103 · Plataforma de correo | Infraestructura | Producción | 2026-12-31 | — |
| A-210 · Servidor de integración | — | Producción | 2029-06-30 | — |
| A-220 · Balanceador de carga | — | Producción | 2029-06-30 | — |
| A-310 · Servidor de la base de datos de clientes | Infraestructura | Producción | 2025-12-31 | — |
| A-320 · Sistema operativo del servidor de pagos | Infraestructura | Producción | 2026-06-30 | 2026-09-30 |

Si un activo se renueva, se retira o se exceptúa lo decide el comité de arquitectura: aquí se dice cuál corre sin dueño o sin soporte.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-activos/inventario_de_activos.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

---

**El reloj:** no creé la tarea programada, porque necesita un sí explícito y en esta sesión de prueba nadie puede darlo. Para correrlo a mano: `/criterio-assets:assets-wake`.

**Cuándo vuelvo:** sin reloj.

Esta salida quedó registrada como la corrida `2026-11-25-assets-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.