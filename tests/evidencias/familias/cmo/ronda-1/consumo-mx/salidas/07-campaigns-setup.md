# /criterio-campaigns:campaigns-setup mercadeo/cms210415xy3-consumo-maya-sintetico

Soy Próspero. Pongo cada campaña al lado de su presupuesto, su factura y su resultado en la plataforma; no apruebo presupuestos ni juzgo campañas.

**Carpeta:** encontré una sola carpeta posible, y ya tiene la marca `_CRITERIO_MERCADEO.txt`:

1. `mercadeo/cms210415xy3-consumo-maya-sintetico`: está marcada para Consumo Maya Sintético (RFC CMS210415XY3) y tiene 00-politica/, 10-piezas/, 20-soportes/, 30-promociones/, 40-bases/ y 50-campanas/.

Te propongo esa. → Sí. Procesé 20 documentos y todos están en su lugar.

**Preguntas (respondidas con lo que dicen los documentos y el setup de Lucía):**
- **Entidad:** Consumo Maya Sintético, RFC CMS210415XY3, México (MXN). → Sí.
- **Periodo:** 2026-10, el del informe de resultados. → Sí.
- **Tolerancias:** la política de publicidad (`00-politica/politica_de_publicidad.pdf`) permite pasar el presupuesto en 5 % y una diferencia de 2 % entre el resultado y la plataforma. → Sí.
- **Publicar en Rostrum:** sí; la política no dice lo contrario. → Sí.
- **Dónde guardo lo que encuentro:** `estado-mercadeo/cms210415xy3-consumo-maya-sintetico`. → Sí.
- **Marca de la carpeta:** ya estaba puesta, así que no la vuelvo a pedir.
- **Términos (versión 1.6):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

  → José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-campaigns-0.1.0-2026-11-25.md` y `.pdf`.

**Configuración:** quedó en `.criterio/campanas/CMS210415XY3/config.json` y se validó sin problemas.

**Ficha de 2026-10:** llevé a la ficha los 3 resultados del informe (C-01, C-03 y C-04), con corte al 2026-10-31.

Hay dos señales para el área de mercadeo: C-03 tiene pauta facturada después de su fecha de fin, y C-02 no tiene meta ni indicador.

# Cada campaña contra su presupuesto · Consumo Maya Sintético · periodo 2026-10

**Entidad:** Consumo Maya Sintético (CMS210415XY3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `budget-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-03 · Lanzamiento de la colección: terminaba el 2026-10-15 y hay pauta facturada hasta el 2026-10-31 (F-104) | 25,000,000.00 | — | 16 | `50-campanas/plan_de_mercadeo.xlsx` fila 4 · `50-campanas/facturas_de_pauta.xlsx` fila 5 |
| 2 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-02 · Clientes recurrentes: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 |

## El resultado

**Tolerancia de la política sobre el presupuesto:** 5 %.

| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |
|---|---|---|---|---|---|---|
| C-01 · Temporada de fin de año | 100,000,000 | 104,000,000 | 2026-09-01 | 2026-10-31 | 5000 ventas | Ventas atribuidas |
| C-02 · Clientes recurrentes | 40,000,000 | 18,000,000 | 2026-09-15 | 2026-11-30 | — | — |
| C-03 · Lanzamiento de la colección | 60,000,000 | 25,000,000 | 2026-09-01 | 2026-10-15 | 3000 visitas a la tienda | Visitas a la tienda |
| C-04 · Marca | 30,000,000 | 7,000,000 | 2026-08-01 | 2026-12-31 | 2 millones de impresiones | Impresiones |

Si se amplía un presupuesto o se cierra una campaña lo decide el área: aquí se dice cuál se pasó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/facturas_de_pauta.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

---

**Reloj:** no programé nada porque nadie podía dar un sí explícito en esta sesión. Para correrlo a mano: `/criterio-campaigns:campaigns-wake`.

**Cuándo vuelvo:** sin reloj.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

---

La corrida quedó registrada como `2026-11-25-campaigns-setup-1`, y lo que se mostró quedó en `estado-mercadeo/cms210415xy3-consumo-maya-sintetico/corridas/salida-campaigns-setup.md`.