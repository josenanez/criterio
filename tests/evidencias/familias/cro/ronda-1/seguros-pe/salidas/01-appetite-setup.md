# /criterio-risk-appetite:appetite-setup riesgos/20607773331-seguros-del-sur-sintetica

Soy Severo. Pongo cada exposición al lado de su límite y cada límite al lado de su dueño y su revisión; no apruebo excesos ni cambio límites.

Severo quedó listo para Seguros del Sur Sintética. En 2026-10 hay un exceso que no tiene plan de acción ni aprobación: el del límite L-01.

**La configuración, con las respuestas tomadas de los documentos:**
- **Carpeta:** `riesgos/20607773331-seguros-del-sur-sintetica`. Era la única candidata y encontré sus 11 documentos en su lugar.
- **Entidad:** Seguros del Sur Sintética, RUC 20607773331, Perú (PEN).
- **Periodo:** el último cerrado es 2026-10.
- **Plazos:** según la declaración, la exposición se reporta en 10 días y la junta revisa la declaración cada 12 meses. Según la política de riesgo operacional, un evento se registra en 30 días y los repetidos se cuentan en una ventana de 12 meses.
- **Publicar en Rostrum:** sí.
- **Estado:** queda en `estado-riesgos/20607773331-seguros-del-sur-sintetica`.
- **Términos v1.6:** los aceptó José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-appetite-0.1.0-2026-11-25.md` y `.pdf`.
- **Marca:** dejé `_CRITERIO_RIESGOS.txt` en la carpeta.
- **Configuración:** `.criterio/apetito/20607773331/config.json`.

**Ficha de 2026-10:**
- La junta revisó la declaración el 2026-02-26.
- El comité aprobó el exceso de L-04 hasta el 2027-01-31, en su sesión del 2026-11-12.
- Sobre L-03 el acta solo toma nota del plan, así que no lo registré como aprobación.

El motor encontró otras dos señales: un riesgo sin límite y un límite con la revisión vencida. Las muestran `/criterio-risk-appetite:coverage-check` y `/criterio-risk-appetite:framework-check`.

# Cada exposición contra su límite · Seguros del Sur Sintética · periodo 2026-10

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `limit-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Cartera vencida de consumo: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0.40 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Cartera vencida de consumo | máximo 6 % | 6.4 | sí | — | Crédito | 2026-11-06 |
| L-02 | Indicador de cobertura de liquidez | mínimo 120 % | 131 | no | — | Tesorería | 2026-11-10 |
| L-03 | Concentración en el mayor deudor | máximo 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Pérdidas por fraude externo sobre ingresos | máximo 0.5 % | 0.62 | sí | aprobado | Operaciones | 2026-11-07 |
| L-05 | Exposición a contrapartes sin calificación | máximo 15 % | 12 | no | — | Tesorería | 2026-11-09 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- `10-exposicion/exposicion_2026-10.xlsx`
- Fuentes técnicas: F-01, F-11 (families/criterio-cro/FUENTES.es.md)

## Cuándo vuelvo

Sin reloj: en esta sesión de prueba nadie dio un sí explícito a la tarea programada. Para correrlo a mano: `/criterio-risk-appetite:appetite-wake`.

La corrida quedó registrada como `2026-11-25-appetite-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.