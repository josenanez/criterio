# /criterio-finance:close-status 

Sofía León declaró el cierre de septiembre como cerrado el 2026-10-05, pero el checklist no lo respalda. Solo 5 de las 9 tareas tienen soporte, y el avance con evidencia es 53,85 %. Clara no declara el estado del cierre: muestra contra qué. El checklist sigue sin aprobar, así que el estado es un cálculo que una persona debe aprobar.

# Estado del cierre · Almacenes Caribe · periodo 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | El cierre se reporta como cerrado y hay señales abiertas que ese estado no explica (`declared_close_vs_evidence`) | Se reporta cerrado (2026-10-05) y hay 7 señales abiertas que ese estado no explica | `2026-09/40-soportes/correo-estado-del-cierre.md` |

## El resultado

**Estado declarado:** cerrado · **Avance con evidencia:** 53,85 % · **Avance declarado:** 53,85 % (ponderados por criticidad)

| Id | Tarea | Responsable | Vence | Criticidad | Estado | Evidencia |
|---|---|---|---|---|---|---|
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | alta | bloqueada por otra (C-07) | — |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | alta | bloqueada por otra (C-08) | — |
| C-06 | Preparar los papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | alta | en plazo | — |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | alta | en plazo | — |
| C-01 | Cerrar los módulos de ventas, compras e inventarios | Lucía Mora | 2026-10-01 | alta | cumplida con evidencia | `C-01-soporte.md` |
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | alta | cumplida con evidencia | `C-02-soporte.md` |
| C-03 | Cruzar las facturas emitidas con las ventas | Lucía Mora | 2026-10-02 | alta | cumplida con evidencia | `C-03-soporte.md` |
| C-04 | Conciliar cartera contra su auxiliar | Marta Ríos | 2026-10-05 | alta | cumplida con evidencia | `C-04-soporte.md` |
| C-05 | Registrar provisiones y causaciones | Jorge Vela | 2026-10-05 | media | cumplida con evidencia | `C-05-soporte.md` |

**Ruta crítica del cierre:** C-07 → C-08 → C-09

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

El reporte completo, con las preguntas que hizo y las fuentes, está en `estado-finanzas/900765432-almacenes-caribe/cierre/2026-09/reporte-close-status.md`.

- **Términos:** estaban vigentes (versión 1.2, aceptada por José Francisco Ñáñez el 2026-10-06), así que no hizo falta registrar nada.
- **Declaración:** el correo de Sofía León del 2026-10-05 ya estaba en `declared` de la ficha, con su cita.
- **Corrida:** quedó registrada como `2026-10-06-close-status-1`, con la salida en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-close-status.md`.