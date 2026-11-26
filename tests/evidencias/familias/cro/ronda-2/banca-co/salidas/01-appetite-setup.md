# /criterio-risk-appetite:appetite-setup riesgos/901777333-banco-andino-sintetico

Severo quedó instalado para Banco Andino Sintético. En el periodo 2026-10 hay 3 límites excedidos sin plan ni aprobación y 3 reportes de exposición que llegaron tarde.

**Respuestas que tomé de los documentos, porque nadie respondía en esta prueba:**
- **Entidad:** Banco Andino Sintético, NIT 901777333, Colombia (COP). Usé la única carpeta candidata.
- **Último periodo cerrado:** 2026-10, por `exposicion_2026-10.xlsx`.
- **Plazos:** la declaración de apetito dice 10 días para reportar la exposición y revisión de la junta cada 12 meses. La política operacional dice 30 días para registrar un evento y 12 meses para contar eventos repetidos.
- **Rostrum:** sí, porque el marco no dice otra cosa.
- **Estado:** `estado-riesgos/901777333-banco-andino-sintetico`.
- **Marca de la carpeta:** sí. `_CRITERIO_RIESGOS.txt` quedó en la carpeta de la entidad.
- **Términos v1.6:** los aceptó José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-appetite-0.2.0-2026-11-25.md` y `.pdf`.

La configuración está en `.criterio/apetito/901777333/config.json`.

**Ficha 2026-10:**
- La junta revisó la declaración el 2025-08-28 (`00-marco/declaracion_de_apetito.pdf`, p. 1).
- El comité aprobó los excesos de L-04 hasta el 2027-01-31, L-06 hasta el 2027-02-28 y L-07 hasta el 2027-03-31 (`40-actas/acta_comite_riesgos_2026-10.pdf`, p. 1).
- Sobre L-03 el comité solo tomó nota del plan, así que no lo registré como aprobación.

**El motor encontró 16 señales en total.** Fuera de este reporte quedan otras 10:
- 3 riesgos sin límite.
- 1 declaración de apetito vencida.
- 3 límites sin dueño.
- 3 límites con la revisión vencida.

Esas salen en `/criterio-risk-appetite:coverage-check` y `/criterio-risk-appetite:framework-check`.

---

# Cada exposición contra su límite · Banco Andino Sintético · periodo 2026-10

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `limit-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-13 · Cartera vencida comercial: la exposición de 2026-10 es 5.9 % y el límite máximo es 5; no hay plan de acción ni aprobación del exceso | 0,90 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 10 · `10-exposicion/exposicion_2026-10.xlsx` fila 10 |
| 2 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-12 · Cartera vencida de vivienda: la exposición de 2026-10 es 4.6 % y el límite máximo es 4; no hay plan de acción ni aprobación del exceso | 0,60 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 9 · `10-exposicion/exposicion_2026-10.xlsx` fila 9 |
| 3 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Cartera vencida de consumo: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0,40 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |
| 4 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-43 · Pérdidas por errores operativos sobre ingresos: Operaciones reportó su exposición de 2026-10 el 2026-11-21, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Operaciones | 11 | `10-exposicion/exposicion_2026-10.xlsx` fila 16 |
| 5 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Indicador de cobertura de liquidez: Tesorería reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 8 | `10-exposicion/exposicion_2026-10.xlsx` fila 3 |
| 6 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-42 · Cupos de contraparte utilizados: Tesorería reportó su exposición de 2026-10 el 2026-11-16, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 6 | `10-exposicion/exposicion_2026-10.xlsx` fila 15 |

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Cartera vencida de consumo | máximo 6 % | 6.4 | sí | — | Crédito | 2026-11-06 |
| L-02 | Indicador de cobertura de liquidez | mínimo 120 % | 131 | no | — | Tesorería | 2026-11-18 |
| L-03 | Concentración en el mayor deudor | máximo 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Pérdidas por fraude externo sobre ingresos | máximo 0.5 % | 0.62 | sí | aprobado | Operaciones | 2026-11-07 |
| L-05 | Exposición a contrapartes sin calificación | máximo 15 % | 12 | no | — | Tesorería | 2026-11-09 |
| L-06 | Pérdidas operacionales sobre el patrimonio | máximo 1 % | 1.1 | sí | aprobado | Operaciones | 2026-11-08 |
| L-07 | Exposición al mayor banco corresponsal | máximo 20 % | 23 | sí | aprobado | Tesorería | 2026-11-09 |
| L-12 | Cartera vencida de vivienda | máximo 4 % | 4.6 | sí | — | Vicepresidencia de crédito | 2026-11-06 |
| L-13 | Cartera vencida comercial | máximo 5 % | 5.9 | sí | — | Vicepresidencia de crédito | 2026-11-06 |
| L-22 | Concentración sectorial de la cartera | máximo 25 % | 21 | no | — | Vicepresidencia de crédito | 2026-11-05 |
| L-23 | Descalce de plazos a 30 días | máximo 10 % | 7 | no | — | Tesorería | 2026-11-05 |
| L-32 | Exposición en moneda extranjera | máximo 20 % | 14 | no | — | Tesorería | 2026-11-04 |
| L-33 | Inversiones de baja liquidez | máximo 8 % | 5 | no | — | Tesorería | 2026-11-04 |
| L-42 | Cupos de contraparte utilizados | máximo 80 % | 62 | no | — | Tesorería | 2026-11-16 |
| L-43 | Pérdidas por errores operativos sobre ingresos | máximo 0.3 % | 0.2 | no | — | Operaciones | 2026-11-21 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- `10-exposicion/exposicion_2026-10.xlsx`
- Fuentes técnicas: F-01, F-10 (families/criterio-cro/FUENTES.es.md)

---

**Reloj:** no creé la tarea programada porque sin nadie presente no hubo un sí explícito. Se corre a mano con `/criterio-risk-appetite:appetite-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-appetite-setup-1`, y la salida está en `estado-riesgos/901777333-banco-andino-sintetico/corridas/salida-appetite-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.