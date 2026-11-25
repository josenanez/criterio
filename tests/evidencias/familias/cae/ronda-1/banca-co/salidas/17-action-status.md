# /criterio-remediation:action-status 

Los términos (versión 1.6) ya estaban vigentes, así que no registré ninguna aceptación nueva. El motor generó el reporte de 2026-11 con corte al 2026-11-24, y esto es lo que muestra:

# Los planes contra su fecha · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Agente:** Remedios, versión 0.1.0 · **Comando:** `action-status`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | `action_plan_overdue` | H-03 · Cuentas privilegiadas sin revisión trimestral: venció el 2026-09-30 sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) | Gerencia de tecnología | 55 | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |
| 2 | `action_plan_missing` | H-02 · Avalúos con más de tres años sin actualizar: comunicado el 2026-04-30 y sin responsable (norma 15.1) | — | — | `30-seguimiento/registro_hallazgos.xlsx` fila 4 |
| 3 | `due_date_extended_repeatedly` | H-03: su fecha se corrió 3 veces y la metodología permite 2 | Gerencia de tecnología | — | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |

## El resultado

**Reprogramaciones que permite la metodología:** 2.

| Hallazgo | Trabajo | Prioridad | Responsable | Fecha | Reprogramaciones | Evidencias |
|---|---|---|---|---|---|---|
| H-01 | TR-01 | Alta | Gerencia de crédito | 2026-12-31 | 0 | 0 |
| H-02 | TR-01 | Media | — | 2026-12-15 | 0 | 0 |
| H-03 | TR-02 | Media | Gerencia de tecnología | 2026-09-30 | 3 | 0 |
| RF-01 | — | Media | Gestión humana | 2026-12-31 | 0 | 0 |

**Lo que no se pudo procesar:** todo lo que llegó se procesó. **Preguntas que hizo:** ninguna.

**Fuentes:** `30-seguimiento/registro_hallazgos.xlsx`; fuentes técnicas F-01 (families/criterio-cae/FUENTES.es.md).

La corrida quedó registrada con el id `2026-11-24-action-status-1`. El reporte está en `estado-auditoria/901777321-banco-andino-sintetico/seguimiento/2026-11/reporte-action-status.md`. Lo que le mostré está en `corridas/salida-action-status.md` de esa misma carpeta.