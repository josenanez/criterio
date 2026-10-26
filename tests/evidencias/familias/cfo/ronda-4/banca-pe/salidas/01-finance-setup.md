# /criterio-finance:finance-setup finanzas/20710000019-banco-ribera

## Listo — Banco Ribera

**Lo que miré:** 64 archivos · nueve periodos (2026-01 a 2026-09) y presupuesto-2026 · 0 fuera de la estructura.
**Términos:** aceptados para la versión 0.10.0 (términos 1.2) por José Francisco Ñáñez. El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-0.10.0-2026-10-06.md` y `.pdf`.

**Respuestas tomadas por defecto:** nadie respondió, así que usé lo que muestran los documentos. El marco (NIIF oficializadas por el CNC) y las cuentas son propuestas sin confirmar. Las cuentas salen de los datos: ventas 4135, compras 5135/5145/5195, IVA 2408, conciliación 1305 y 2205, bancos andino-7101 y pacifico-7102. No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta, porque nadie dijo que sí. La configuración quedó en `.criterio/finanzas/20710000019/config.json`.

# Estado del cierre · Banco Ribera · periodo 2026-09

**Aprueba:** Sofía León · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | `close_task_done_without_evidence` | C-02 (conciliar cada cuenta bancaria) figura cumplida y no hay soporte en `2026-09/40-soportes/` que empiece por C-02 | Andrés Paz | `00-referencia/checklist-cierre.csv` fila 3 |
| 2 | `declared_close_vs_evidence` | El cierre se reporta cerrado (correo del 2026-10-05) y hay 4 señales abiertas que ese estado no explica | — | `2026-09/40-soportes/correo-estado-del-cierre.md` |

## El resultado

**Estado declarado:** cerrado (correo de Sofía León, 2026-10-05). **Avance con evidencia:** 42.31 %. **Avance declarado:** 53.85 % (ponderados por criticidad).

| Id | Tarea | Responsable | Vence | Estado |
|---|---|---|---|---|
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | cumplida sin evidencia |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | bloqueada por C-02 |
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 |
| C-06 | Preparar los papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo |
| C-01 | Cerrar los módulos de ventas, compras e inventarios | Lucía Mora | 2026-10-01 | cumplida con evidencia |
| C-03 | Cruzar las facturas emitidas con las ventas | Lucía Mora | 2026-10-02 | cumplida con evidencia |
| C-04 | Conciliar cartera contra su auxiliar | Marta Ríos | 2026-10-05 | cumplida con evidencia |
| C-05 | Registrar provisiones y causaciones | Jorge Vela | 2026-10-05 | cumplida con evidencia |

**Ruta crítica del cierre:** C-02 → C-07 → C-08 → C-09

**Otras señales abiertas:** el motor cuenta además `einvoice_duplicate` 1, `bank_unreconciled` 1 y `einvoice_amount_mismatch` 1. El reporte de estado no las detalla; las detallan `/bank-reconcile` y `/einvoice-check`.

**Lo que no se pudo procesar:** nada, todo se procesó.

**Qué falta para que esto sea mejor:**
- El soporte firmado de C-02. Sin él, C-07, C-08 y C-09 siguen bloqueadas.
- Los festivos del calendario.
- Que una persona confirme el marco contable y las cuentas propuestas.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

La salida quedó en `estado-finanzas/20710000019-banco-ribera/corridas/salida-finance-setup.md` y la corrida quedó registrada con el id `2026-10-06-finance-setup-1`. Hice 8 preguntas, todas respondidas desde los documentos. No medí los minutos hasta el primer resultado.

El reporte completo del motor está en `estado-finanzas/20710000019-banco-ribera/cierre/2026-09/reporte-close-status.md`.