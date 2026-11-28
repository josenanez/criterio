# /criterio-campaigns:campaigns-setup mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos

Soy Próspero. Pongo cada campaña al lado de su presupuesto, su factura y su resultado en la plataforma. No apruebo presupuestos ni juzgo campañas.

**Carpeta:** 1. `.` (mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos). Ya tiene la marca `_CRITERIO_MERCADEO.txt` de Almacenes del Canal Sintéticos · 155634567-2-2020, y tiene 00-politica/, 10-piezas/, 20-soportes/, 30-promociones/, 40-bases/ y 50-campanas/. Es la única carpeta que encontré y ya está marcada, así que trabajo con esa.

Procesé 27 documentos. Todos están en su lugar y ninguno es ilegible.

Esto quedó configurado:
- **Entidad:** Almacenes del Canal Sintéticos · 155634567-2-2020 · Panamá (USD). Es la misma que ya dejó configurada Lucía.
- **Periodo:** 2026-10, el que cubre el informe de resultados.
- **Tolerancias:** 5 % sobre el presupuesto de una campaña y 2 % entre el resultado reportado y la plataforma. Las dos salen de `00-politica/politica_de_publicidad.pdf`.
- **Rostrum:** sí, porque la política no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos`.
- **Marca:** la carpeta ya estaba marcada, así que no hizo falta otra.

**Términos (versión 1.6, 2026-11-16):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-campaigns-1.1.0-2026-11-25.md` y `.pdf`, y la configuración en `.criterio/campanas/155634567-2-2020/config.json`.

Pasé a la ficha de 2026-10 los 3 resultados del informe (C-01, C-03 y C-04, con corte al 2026-10-31). En octubre el cruce encontró 10 señales en total. Abajo va el reporte de presupuestos, que trae 6 de ellas.

# Cada campaña contra su presupuesto · Almacenes del Canal Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Canal Sintéticos (155634567-2-2020) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 1.1.0 · **Comando:** `budget-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-01 · Temporada de fin de año: la pauta facturada suma 108,000,000 y el presupuesto es 100,000,000; la política tolera un 5 % más | 8,000,000.00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 2 |
| 2 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-32 · Día de la familia: la pauta facturada suma 23,000,000 y el presupuesto es 20,000,000; la política tolera un 5 % más | 3,000,000.00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 8 |
| 3 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-03 · Lanzamiento de la colección: terminaba el 2026-10-15 y hay pauta facturada hasta el 2026-10-31 (F-104) | 25,000,000.00 | — | 16 | `50-campanas/plan_de_mercadeo.xlsx` fila 4 · `50-campanas/facturas_de_pauta.xlsx` fila 5 |
| 4 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-42 · Verano: terminaba el 2026-09-30 y hay pauta facturada hasta el 2026-10-20 (F-42) | 9,000,000.00 | — | 20 | `50-campanas/plan_de_mercadeo.xlsx` fila 9 · `50-campanas/facturas_de_pauta.xlsx` fila 9 |
| 5 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-02 · Clientes recurrentes: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 |
| 6 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-22 · Aniversario: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 7 |

## El resultado

**Tolerancia de la política sobre el presupuesto:** 5 %.

| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |
|---|---|---|---|---|---|---|
| C-01 · Temporada de fin de año | 100,000,000 | 108,000,000 | 2026-09-01 | 2026-10-31 | 5000 ventas | Ventas atribuidas |
| C-02 · Clientes recurrentes | 40,000,000 | 18,000,000 | 2026-09-15 | 2026-11-30 | — | — |
| C-03 · Lanzamiento de la colección | 60,000,000 | 25,000,000 | 2026-09-01 | 2026-10-15 | 3000 visitas a la tienda | Visitas a la tienda |
| C-04 · Marca | 30,000,000 | 0 | 2026-08-01 | 2026-12-31 | 2 millones de impresiones | Impresiones |
| C-12 · Reactivación | 15,000,000 | 0 | 2026-10-01 | 2026-11-30 | 800 clientes reactivados | Clientes reactivados |
| C-22 · Aniversario | 25,000,000 | 0 | 2026-10-01 | 2026-11-15 | — | — |
| C-32 · Día de la familia | 20,000,000 | 23,000,000 | 2026-09-01 | 2026-10-31 | 900 ventas | Ventas atribuidas |
| C-42 · Verano | 18,000,000 | 9,000,000 | 2026-08-01 | 2026-09-30 | 1000 visitas a la tienda | Visitas a la tienda |

Si se amplía un presupuesto o se cierra una campaña lo decide el área: aquí se dice cuál se pasó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/facturas_de_pauta.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión no hay nadie que lo dé. Para correrlo a mano: `/criterio-campaigns:campaigns-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

---
La corrida quedó registrada como `2026-11-25-campaigns-setup-1`.