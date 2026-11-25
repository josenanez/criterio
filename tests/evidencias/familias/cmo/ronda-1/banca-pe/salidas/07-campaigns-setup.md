# /criterio-campaigns:campaigns-setup mercadeo/20603335551-banco-altiplano-sintetico

Soy Próspero. Pongo cada campaña al lado de su presupuesto, su factura y su resultado en la plataforma; no apruebo presupuestos ni juzgo campañas.

**Carpeta:** encontré una sola candidata y ya estaba marcada con `_CRITERIO_MERCADEO.txt`: Banco Altiplano Sintético, RUC 20603335551. Tiene las carpetas de `00-politica/` a `50-campanas/` y 19 documentos. Trabajé sobre esa carpeta.

Como en esta prueba nadie responde, tomé cada respuesta de los documentos:
- **Entidad:** Banco Altiplano Sintético, RUC 20603335551, Perú, en soles (PEN). Es la misma que ya tiene configurada Lucía.
- **Periodo:** 2026-10, el del informe de resultados.
- **Tolerancias:** 5 % sobre el presupuesto y 2 % de diferencia con la plataforma. Las dos salen de `00-politica/politica_de_publicidad.pdf`.
- **Publicar en Rostrum:** sí, porque la política no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-mercadeo/20603335551-banco-altiplano-sintetico`.
- **Marca:** la carpeta ya estaba marcada, así que no puse otra.

**Términos (v1.6):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-campaigns-0.1.0-2026-11-25.md` y en el `.pdf` del mismo nombre. La configuración quedó en `.criterio/campanas/20603335551/config.json`.

Procesé los 4 documentos de `50-campanas/` y llevé a la ficha los 3 resultados que reporta el informe: C-01, C-03 y C-04, con corte al 2026-10-31. El motor encontró 3 señales en el periodo y este primer reporte trae la de presupuesto. Las otras dos tienen su propio comando: la factura de pauta sin campaña ni orden está en `/criterio-campaigns:invoice-check` y el resultado que no coincide con la plataforma, en `/criterio-campaigns:result-check`.

# Cada campaña contra su presupuesto · Banco Altiplano Sintético · periodo 2026-10

**Entidad:** Banco Altiplano Sintético (20603335551) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `budget-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-01 · Temporada de fin de año: la pauta facturada suma 108,000,000 y el presupuesto es 100,000,000; la política tolera un 5 % más | 8,000,000.00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 2 |

## El resultado

**Tolerancia de la política sobre el presupuesto:** 5 %.

| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |
|---|---|---|---|---|---|---|
| C-01 · Temporada de fin de año | 100,000,000 | 108,000,000 | 2026-09-01 | 2026-10-31 | 5000 ventas | Ventas atribuidas |
| C-02 · Clientes recurrentes | 40,000,000 | 18,000,000 | 2026-09-15 | 2026-11-30 | 1200 recompras | Recompras |
| C-03 · Lanzamiento de la colección | 60,000,000 | 25,000,000 | 2026-09-01 | 2026-10-15 | 3000 visitas a la tienda | Visitas a la tienda |
| C-04 · Marca | 30,000,000 | 0 | 2026-08-01 | 2026-12-31 | 2 millones de impresiones | Impresiones |

Si se amplía un presupuesto o se cierra una campaña lo decide el área: aquí se dice cuál se pasó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. La tarea programada solo se crea con un sí explícito y en esta prueba nadie lo dio. Para correrlo a mano: `/criterio-campaigns:campaigns-wake`.

La corrida quedó registrada como `2026-11-25-campaigns-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.