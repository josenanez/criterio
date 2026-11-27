# /criterio-remediation:committee-brief 

Términos vigentes (versión 1.6), así que no hizo falta registrar de nuevo la aceptación.

# Lo que el comité tiene que saber · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.2.2 · **Comando:** `committee-brief`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Riesgo aceptado por encima del apetito sin constancia de discusión con la alta dirección ni de llegada al consejo (norma 11.5) (`risk_accepted_not_escalated`) | RA-01 · Sistema central sin soporte del fabricante: aceptado el 2026-06-01 | — | — | `30-seguimiento/riesgos_aceptados.xlsx` fila 2 |
| 2 | Plan de acción vencido sin evidencia ni explicación documentada del atraso (norma 15.2) (`action_plan_overdue`) | H-03 · Cuentas privilegiadas sin revisión trimestral: venció el 2026-09-30 | Gerencia de tecnología | 55 | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |
| 3 | Hallazgo externo que no está en el registro con su plan (`external_finding_untracked`) | RF-02 · Caja menor sin arqueo en el trimestre (Revisor fiscal) | — | — | `30-seguimiento/informe_revisor_fiscal_2026.pdf` |
| 4 | La misma condición vuelve a aparecer tras el cierre de su hallazgo (`finding_repeated`) | H-01: la misma condición que H-20 en Crédito, cerrado el 2025-09-15 | — | — | `30-seguimiento/registro_hallazgos.xlsx` filas 3 y 2 |

## El resultado

**Planes abiertos:** 4 · **Vencidos sin evidencia ni explicación:** 1 · **Hallazgos que vuelven:** 1.

| Riesgo aceptado por encima del apetito | Alta dirección | Resuelto | Consejo |
|---|---|---|---|
| RA-01 · Sistema central sin soporte del fabricante | no | no | no |

| Hallazgo externo | De | En el registro |
|---|---|---|
| RF-01 | Revisor fiscal | sí |
| RF-02 | Revisor fiscal | no |

Este es el material; lo que se concluye y se comunica al comité es del responsable de auditoría.

**Lo que no se pudo procesar:** todo lo que llegó se procesó. **Preguntas que hizo:** ninguna.

**Fuentes:** `30-seguimiento/informe_revisor_fiscal_2026.pdf`, `30-seguimiento/registro_hallazgos.xlsx`, `30-seguimiento/riesgos_aceptados.xlsx`, y F-01 (families/criterio-cae/FUENTES.es.md).

La salida está en `estado-auditoria/31452078000190-seguradora-atlantica-sintetica/corridas/salida-committee-brief.md`. El motor registró la corrida como `2026-11-24-committee-brief-1`. El reporte completo del motor está en `seguimiento/2026-11/reporte-committee-brief.md`, dentro de esa misma carpeta de estado.

Dos aclaraciones sobre lo que mostré arriba:
- Quité la columna «Monto» de la tabla porque venía vacía en las cuatro filas. El archivo de salida sí la conserva, tal como la escribió el motor.
- Agregué al archivo de salida una línea inicial sobre los términos vigentes, que no está en el reporte del motor.