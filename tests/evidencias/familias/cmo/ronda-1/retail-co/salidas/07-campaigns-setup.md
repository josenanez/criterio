# /criterio-campaigns:campaigns-setup mercadeo/901333555-almacenes-del-valle-sinteticos

Próspero quedó configurado para Almacenes del Valle Sintéticos (NIT 901333555), periodo 2026-10. No hizo falta ninguna pregunta nueva: las respuestas salieron del setup de Lucía y de la política de publicidad.

- **Configuración:** `.criterio/campanas/901333555/config.json`. Las tolerancias salen de la política aprobada por la junta el 2025-03-01: 5 % sobre el presupuesto y 2 % entre un resultado y la plataforma. Lo que encuentro se publica en Rostrum y se guarda en `estado-mercadeo/901333555-almacenes-del-valle-sinteticos`.
- **Términos v1.6:** quedan aceptados por José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-campaigns-0.1.0-2026-11-25.md` y en el `.pdf` del mismo nombre.
- **Marca:** la carpeta ya tenía `_CRITERIO_MERCADEO.txt`, así que no dejé otra.
- **Ficha:** procesé el informe de resultados de octubre y llevé a la ficha tres resultados (C-01, C-03 y C-04), con el corte que el informe declara.

El cruce encontró 5 señales. El reporte de abajo trae 3. Las otras dos son una factura de pauta sin campaña ni orden y un resultado que no coincide con la plataforma; esas las muestran `/criterio-campaigns:invoice-check` y `/criterio-campaigns:result-check`.

---

# Cada campaña contra su presupuesto · Almacenes del Valle Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `budget-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-01 · Temporada de fin de año: la pauta facturada suma 108,000,000 y el presupuesto es 100,000,000; la política tolera un 5 % más | 8.000.000,00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 2 |
| 2 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-03 · Lanzamiento de la colección: terminaba el 2026-10-15 y hay pauta facturada hasta el 2026-10-31 (F-104) | 25.000.000,00 | — | 16 | `50-campanas/plan_de_mercadeo.xlsx` fila 4 · `50-campanas/facturas_de_pauta.xlsx` fila 5 |
| 3 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-02 · Clientes recurrentes: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 |

## El resultado

**Tolerancia de la política sobre el presupuesto:** 5 %.

| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |
|---|---|---|---|---|---|---|
| C-01 · Temporada de fin de año | 100,000,000 | 108,000,000 | 2026-09-01 | 2026-10-31 | 5000 ventas | Ventas atribuidas |
| C-02 · Clientes recurrentes | 40,000,000 | 18,000,000 | 2026-09-15 | 2026-11-30 | — | — |
| C-03 · Lanzamiento de la colección | 60,000,000 | 25,000,000 | 2026-09-01 | 2026-10-15 | 3000 visitas a la tienda | Visitas a la tienda |
| C-04 · Marca | 30,000,000 | 0 | 2026-08-01 | 2026-12-31 | 2 millones de impresiones | Impresiones |

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

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión nadie podía darlo. Para correrlo a mano: `/criterio-campaigns:campaigns-wake`.

La corrida quedó registrada como `2026-11-25-campaigns-setup-1`, y lo que se mostró está en `estado-mercadeo/901333555-almacenes-del-valle-sinteticos/corridas/salida-campaigns-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.