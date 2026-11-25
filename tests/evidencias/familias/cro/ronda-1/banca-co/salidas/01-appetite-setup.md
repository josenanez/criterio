# /criterio-risk-appetite:appetite-setup riesgos/901777333-banco-andino-sintetico

Severo quedó instalado para Banco Andino Sintético (901777333). Esta es la primera revisión de límites, del periodo 2026-10. Como en esta prueba nadie responde, tomé cada respuesta de los documentos:

- **Carpeta:** `riesgos/901777333-banco-andino-sintetico`. Era la única candidata.
- **Entidad:** Banco Andino Sintético, 901777333, Colombia, en pesos colombianos.
- **Último periodo cerrado:** 2026-10.
- **Plazos:** 10 días para reportar la exposición y revisión de la junta cada 12 meses, según la declaración de apetito. 30 días para registrar un evento y una ventana de 12 meses para los repetidos, según la política de riesgo operacional.
- **Publicar en Rostrum:** sí.
- **Dónde guardo lo que encuentro:** `estado-riesgos/901777333-banco-andino-sintetico`.
- **Términos v1.6:** los aceptó José Francisco Ñáñez el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-risk-appetite-0.1.0-2026-11-25.md` y en su `.pdf`.
- **Marca:** `_CRITERIO_RIESGOS.txt` quedó en la carpeta.
- **Configuración:** `.criterio/apetito/901777333/config.json`.

En la ficha de 2026-10 quedaron dos datos:
- La junta revisó la declaración por última vez el 2025-08-28.
- El comité aprobó el exceso de L-04 hasta el 2027-01-31.

Sobre L-03, el acta solo «toma nota del plan». Eso no es una aprobación del exceso, así que no la registré como tal.

El cálculo encontró además señales del marco que este reporte no muestra: un límite sin dueño, una revisión de límite vencida, la declaración sin revisar en el plazo y un riesgo sin límite. Se ven con `/criterio-risk-appetite:framework-check` y `/criterio-risk-appetite:coverage-check`.

# Cada exposición contra su límite · Banco Andino Sintético · periodo 2026-10

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `limit-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Cartera vencida de consumo: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0,40 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |
| 2 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Indicador de cobertura de liquidez: Tesorería reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 8 | `10-exposicion/exposicion_2026-10.xlsx` fila 3 |

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Cartera vencida de consumo | máximo 6 % | 6.4 | sí | — | Crédito | 2026-11-06 |
| L-02 | Indicador de cobertura de liquidez | mínimo 120 % | 131 | no | — | Tesorería | 2026-11-18 |
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
- Fuentes técnicas: F-01, F-10 (families/criterio-cro/FUENTES.es.md)

## Cuándo vuelvo

No quedó tarea programada, porque nadie dijo que sí a la revisión diaria en esta sesión. Para correrla a mano: `/criterio-risk-appetite:appetite-wake`.

La corrida quedó registrada como `2026-11-25-appetite-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.