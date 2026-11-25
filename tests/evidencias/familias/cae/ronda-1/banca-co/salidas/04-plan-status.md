# /criterio-audit-plan:plan-status 

Los términos (versión 1.6) ya estaban vigentes. Hay dos señales abiertas, y las dos son sobre TR-06 · Nómina: el plan lo agrega sin acta que lo apruebe, y no ha empezado.

# El avance y los cambios del plan · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.1.0 · **Comando:** `plan-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un trabajo se agregó, se canceló o se aplazó sin el acta del órgano que aprueba el plan (`plan_change_unapproved`) | TR-06 · Nómina: el plan lo agrega y no hay un acta del órgano que aprueba el plan que lo apruebe (norma 9.4) | — | — | — | `10-plan/plan_anual_2026.xlsx` fila 7 |
| 2 | Un trabajo del plan pasó su fecha de inicio o de cierre sin estar en curso o terminado (`engagement_behind_schedule`) | TR-06 · Nómina: tenía que empezar el 2026-11-02 y sigue Planeado | — | — | 22 | `10-plan/plan_anual_2026.xlsx` fila 7 |

## El resultado

| Trabajo | Unidad | Inicio | Cierre | Estado | Horas |
|---|---|---|---|---|---|
| TR-01 · Crédito comercial | U-01 | 2026-02-02 | 2026-04-30 | Terminado | 500.0 |
| TR-02 · Ciberseguridad de canales | U-02 | 2026-03-02 | 2026-05-29 | Terminado | 400.0 |
| TR-03 · Prevención de lavado | U-05 | 2026-06-01 | 2026-12-18 | En curso | 300.0 |
| TR-04 · Pagos a proveedores | U-06 | 2026-09-21 | 2026-12-11 | En curso | 300.0 |
| TR-06 · Nómina | U-04 | 2026-11-02 | 2027-01-29 | Planeado | 200.0 |
| TR-07 · Gobierno corporativo | U-08 | 2026-10-05 | 2026-12-18 | En curso | 500.0 |

| Cambio | Trabajo | Aprobado | Por | Acta |
|---|---|---|---|---|
| cancela | TR-05 | sí | Comité de auditoría | `10-plan/actas/acta-07-2026.pdf, p. 1` |
| agrega | TR-06 | no | — | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-plan/plan_anual_2026.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

La corrida quedó registrada como `2026-11-24-plan-status-1`.