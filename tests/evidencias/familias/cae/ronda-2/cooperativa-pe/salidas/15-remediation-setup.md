# /criterio-remediation:remediation-setup auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica

Remedios quedó instalada para la Cooperativa de Ahorro Altiplano Sintética (RUC 20601777321, Perú) y ya corrió la primera revisión. No hice preguntas abiertas: todo salió de la metodología y del estatuto.

- **Carpeta:** `auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica`. Era la única candidata y ya tenía su marca, así que no la pedí de nuevo.
- **Metodología:** permite correr la fecha de un plan de acción hasta 2 veces (sección «Seguimiento»). El plan lo aprueba el comité de auditoría. Periodo 2026-11. Nada se publica en Rostrum.
- **Términos v1.6:** los mostré tal cual y quedaron aceptados por José Francisco Ñáñez el 2026-11-24. El comprobante está en `.criterio/terminos/aceptacion-criterio-remediation-0.2.2-2026-11-24.md` y `.pdf`.
- **Configuración:** `.criterio/seguimiento/20601777321/config.json`. El estado se guarda en `estado-auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica`.
- **Ficha 2026-11:** procesé los 4 documentos de `30-seguimiento/`. Registré la evidencia de H-20 y los hallazgos RF-01 y RF-02 del informe del revisor fiscal.

El motor encontró 7 señales. Este reporte muestra las 3 de los planes de acción; las otras 4 salen con `/criterio-remediation:closure-check` y `/criterio-remediation:committee-brief`. Son un cierre sin evidencia, un riesgo aceptado sin escalar, un hallazgo externo fuera del registro y un hallazgo que vuelve.

# Los planes contra su fecha · Cooperativa de Ahorro Altiplano Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Altiplano Sintética (20601777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.2.2 · **Comando:** `action-status`

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

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta prueba nadie lo dio. Para correrlo a mano: `/criterio-remediation:remediation-wake`.

La corrida quedó registrada como `2026-11-24-remediation-setup-1`. La salida completa está en `estado-auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica/corridas/salida-remediation-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.