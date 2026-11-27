# /criterio-remediation:action-status 

Los términos (v1.6) ya estaban vigentes, así que no pedí aceptarlos de nuevo. El reporte salió con corte al 2026-11-24 y la corrida quedó registrada.

# Los planes contra su fecha · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.2.2 · **Comando:** `action-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un plan de acción pasó su fecha sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) (`action_plan_overdue`) | H-03 · Cuentas privilegiadas sin revisión trimestral: venció el 2026-09-30 sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) | — | Gerencia de tecnología | 55 | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |
| 2 | Un hallazgo comunicado no tiene plan de acción, responsable o fecha (norma 15.1) (`action_plan_missing`) | H-02 · Avalúos con más de tres años sin actualizar: comunicado el 2026-04-30 y sin responsable (norma 15.1) | — | — | — | `30-seguimiento/registro_hallazgos.xlsx` fila 4 |
| 3 | La fecha de un plan se corrió más veces de las que permite la metodología (`due_date_extended_repeatedly`) | H-03 · Cuentas privilegiadas sin revisión trimestral: su fecha se corrió 3 veces y la metodología permite 2 | — | Gerencia de tecnología | — | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |

## El resultado

**Reprogramaciones que permite la metodología:** 2.

| Hallazgo | Trabajo | Prioridad | Responsable | Fecha | Reprogramaciones | Evidencias |
|---|---|---|---|---|---|---|
| H-01 | TR-01 | Alta | Gerencia de crédito | 2026-12-31 | 0 | 0 |
| H-02 | TR-01 | Media | — | 2026-12-15 | 0 | 0 |
| H-03 | TR-02 | Media | Gerencia de tecnología | 2026-09-30 | 3 | 0 |
| RF-01 | — | Media | Gestión humana | 2026-12-31 | 0 | 0 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-seguimiento/registro_hallazgos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

El reporte está en `estado-auditoria/901777321-banco-andino-sintetico/seguimiento/2026-11/reporte-action-status.md`. Copié lo mostrado a `corridas/salida-action-status.md`. La corrida quedó registrada como `2026-11-24-action-status-1`.

Qué se hace con H-03 y H-02, y si se pide la explicación del atraso, lo decide el responsable de auditoría. Yo no cierro hallazgos ni valido evidencias.