# /criterio-remediation:action-status 

Los términos siguen vigentes (versión 1.6, aceptada en 0.2.2), así que no hizo falta registrar una aceptación nueva. Corrí el reporte del periodo 2026-11 con fecha de corte 2026-11-24.

# Los planes contra su fecha · Cooperativa de Ahorro Altiplano Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Altiplano Sintética (20601777321) · **Fecha de corte:** 2026-11-24 · **Agente:** Remedios, versión 0.2.2 · **Comando:** `action-status`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Plan vencido sin evidencia ni explicación del atraso (norma 15.2) (`action_plan_overdue`) | H-03 · Cuentas privilegiadas sin revisión trimestral: venció el 2026-09-30 | Gerencia de tecnología | 55 | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |
| 2 | Hallazgo comunicado sin plan, responsable o fecha (norma 15.1) (`action_plan_missing`) | H-02 · Avalúos con más de tres años sin actualizar: comunicado el 2026-04-30 y sin responsable | — | — | `30-seguimiento/registro_hallazgos.xlsx` fila 4 |
| 3 | Fecha corrida más veces de las que permite la metodología (`due_date_extended_repeatedly`) | H-03: se corrió 3 veces y la metodología permite 2 | Gerencia de tecnología | — | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |

## El resultado

**Reprogramaciones que permite la metodología:** 2.

| Hallazgo | Trabajo | Prioridad | Responsable | Fecha | Reprogramaciones | Evidencias |
|---|---|---|---|---|---|---|
| H-01 | TR-01 | Alta | Gerencia de crédito | 2026-12-31 | 0 | 0 |
| H-02 | TR-01 | Media | — | 2026-12-15 | 0 | 0 |
| H-03 | TR-02 | Media | Gerencia de tecnología | 2026-09-30 | 3 | 0 |
| RF-01 | — | Media | Gestión humana | 2026-12-31 | 0 | 0 |

**Lo que no se pudo procesar:** nada, todo lo que llegó se procesó. **Preguntas que hizo el motor:** ninguna.

**Fuentes:** `30-seguimiento/registro_hallazgos.xlsx`; F-01 (families/criterio-cae/FUENTES.es.md).

La corrida quedó registrada como `2026-11-24-action-status-1`. Lo que se concluya sobre estos tres puntos es del responsable de auditoría.

Dos notas sobre el proceso:
- Por error creé una carpeta `corridas` vacía en `.criterio/seguimiento/…`. La borré.
- La salida está en `estado-auditoria/20601777321-…/corridas/salida-action-status.md`. El reporte del motor está en `seguimiento/2026-11/reporte-action-status.md`.