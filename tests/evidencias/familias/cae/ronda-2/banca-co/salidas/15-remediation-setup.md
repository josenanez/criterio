# /criterio-remediation:remediation-setup auditoria/901777321-banco-andino-sintetico

Remedios quedó instalada sobre Banco Andino Sintético (NIT 901777321) para el periodo 2026-11. El primer reporte trae 3 señales en los planes de acción, dos de ellas sobre H-03.

- **Configuración:** está en `.criterio/seguimiento/901777321/config.json`. La entidad, el periodo y el lugar del estado los tomé de las configuraciones que ya habían dejado los otros dos agentes. Las 2 reprogramaciones que se permiten salen de la metodología, en la sección Seguimiento. Lo que encuentre no se publica en Rostrum.
- **Términos v1.6:** quedaron aceptados por José Francisco Ñáñez el 2026-11-24. El comprobante está en `.criterio/terminos/aceptacion-criterio-remediation-0.2.2-2026-11-24.md` y `.pdf`.
- **Marca:** la carpeta ya tenía `_CRITERIO_AUDITORIA.txt`, así que no la volví a poner.
- **Ficha 2026-11:** procesé los 4 documentos de `30-seguimiento/`. Llevé a la ficha la evidencia de H-20 (procedimiento de desembolso actualizado, 2025-09-12) y los hallazgos RF-01 y RF-02 del informe del revisor fiscal.

---

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

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión de prueba nadie lo dio. A mano se corre con `/criterio-remediation:remediation-wake`.

La corrida quedó registrada como `2026-11-24-remediation-setup-1`, y lo que se mostró está en `estado-auditoria/901777321-banco-andino-sintetico/corridas/salida-remediation-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.