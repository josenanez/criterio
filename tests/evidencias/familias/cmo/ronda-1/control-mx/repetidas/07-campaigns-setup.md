# /criterio-campaigns:campaigns-setup mercadeo/ccm220101zz9-consumo-control-de-mercadeo-sintetico

Soy Próspero. Pongo cada campaña al lado de su presupuesto, su factura y su resultado en la plataforma. No apruebo presupuestos ni juzgo campañas.

**Carpeta:** encontré una sola candidata, `mercadeo/ccm220101zz9-consumo-control-de-mercadeo-sintetico`. Ya estaba marcada con `_CRITERIO_MERCADEO.txt` y tiene las carpetas de `00-politica/` a `50-campanas/`, así que la tomé. Procesé 20 documentos y ninguno estaba fuera de lugar ni era ilegible.

**Respuestas tomadas de los documentos y del setup de Lucía:**
- **Entidad:** Consumo Control de Mercadeo Sintético, RFC CCM220101ZZ9, México (MXN).
- **Periodo:** 2026-10, el del informe de resultados.
- **Tolerancias:** 5 % sobre el presupuesto y 2 % entre el resultado y la plataforma, según `00-politica/politica_de_publicidad.pdf`.
- **Rostrum:** sí, porque la política no dice otra cosa.
- **Estado:** `estado-mercadeo/ccm220101zz9-consumo-control-de-mercadeo-sintetico`.
- **Marca:** la carpeta ya la tenía, así que no hizo falta otra.

**Términos (versión 1.6):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Los aceptó José Francisco Ñáñez el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-campaigns-0.1.0-2026-11-25.md` y en el `.pdf` del mismo nombre.

La configuración quedó en `.criterio/campanas/CCM220101ZZ9/config.json`. Llevé a la ficha de 2026-10 los 3 resultados del informe (C-01, C-03 y C-04, con corte al 2026-10-31).

El motor no dejó ninguna señal abierta de presupuesto en las 4 campañas del plan. El reporte, tal como lo escribió el motor:

# Cada campaña contra su presupuesto · Consumo Control de Mercadeo Sintético · periodo 2026-10

**Entidad:** Consumo Control de Mercadeo Sintético (CCM220101ZZ9) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `budget-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Tolerancia de la política sobre el presupuesto:** 5 %.

| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |
|---|---|---|---|---|---|---|
| C-01 · Temporada de fin de año | 100,000,000 | 104,000,000 | 2026-09-01 | 2026-10-31 | 5000 ventas | Ventas atribuidas |
| C-02 · Clientes recurrentes | 40,000,000 | 18,000,000 | 2026-09-15 | 2026-11-30 | 1200 recompras | Recompras |
| C-03 · Lanzamiento de la colección | 60,000,000 | 25,000,000 | 2026-09-01 | 2026-10-15 | 3000 visitas a la tienda | Visitas a la tienda |
| C-04 · Marca | 30,000,000 | 7,000,000 | 2026-08-01 | 2026-12-31 | 2 millones de impresiones | Impresiones |

Si se amplía un presupuesto o se cierra una campaña lo decide el área: aquí se dice cuál se pasó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

**Una cosa del motor que conviene revisar:** la sección de fuentes dice «Sin documentos citados». Sin embargo, la tabla sale del plan de mercadeo y de las facturas de pauta de `50-campanas/`.

**Reloj:** no creé ninguna tarea programada, porque en esta sesión nadie podía dar el sí. Para correrlo a mano: `/criterio-campaigns:campaigns-wake`.

**Cuándo vuelvo:** sin reloj.

La salida quedó en `estado-mercadeo/ccm220101zz9-consumo-control-de-mercadeo-sintetico/corridas/salida-campaigns-setup.md` y la corrida quedó registrada como `2026-11-25-campaigns-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.