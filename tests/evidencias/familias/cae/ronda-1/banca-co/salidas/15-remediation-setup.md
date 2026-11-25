# /criterio-remediation:remediation-setup auditoria/901777321-banco-andino-sintetico

Remedios ya quedó lista para Banco Andino Sintético (NIT 901777321), periodo 2026-11. La aceptación de José Francisco Ñáñez quedó registrada. El comprobante está en `.criterio/terminos/aceptacion-criterio-remediation-0.1.0-2026-11-24.md` y en su `.pdf`. La configuración quedó en `.criterio/seguimiento/901777321/config.json`.

- **Alta dirección y consejo:** ningún documento de la carpeta dice quiénes son, así que la escalada de un riesgo aceptado no tiene a quién apuntar. La configuración de ejemplo tampoco tiene un campo para ese dato.
- **Ficha:** procesé los 4 documentos de `30-seguimiento/`. A la ficha pasaron la evidencia de H-20, que no trae fecha, y los hallazgos RF-01 y RF-02 del informe del revisor fiscal.
- **Otras señales:** el cálculo encontró también otras señales que no salen en este reporte: cierres sin evidencia, hallazgos que vuelven, un riesgo aceptado sin escalar y un hallazgo externo fuera del registro. Se ven con `/criterio-remediation:closure-check` y `/criterio-remediation:committee-brief`.

# Los planes contra su fecha · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.1.0 · **Comando:** `action-status`

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

No creé la tarea diaria de las 7:00 porque en esta prueba nadie dio un sí explícito. Remedios se corre a mano con `/criterio-remediation:remediation-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-24-remediation-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.