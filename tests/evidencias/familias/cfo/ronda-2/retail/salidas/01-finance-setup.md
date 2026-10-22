# /criterio-finance:finance-setup finanzas/900765432-almacenes-caribe

## Listo — Almacenes Caribe

**Lo que miré:** 57 archivos · periodos 2026-01 a 2026-09 (9) y presupuesto-2026 · 0 fuera de la estructura.
**Términos:** aceptados por José Francisco Ñáñez para la versión 0.8.0 (términos 1.2). El comprobante quedó en `.criterio/terminos/aceptacion-criterio-finance-0.8.0-2026-10-06.md` y `.pdf`.

Sofía León declaró el cierre de septiembre como cerrado el 2026-10-05. El motor encontró 7 señales abiertas que ese estado no explica. El avance con evidencia es 53,85 %, igual al declarado. El checklist es el de la organización y no está aprobado.

No marqué la carpeta con `_CRITERIO_FINANZAS.txt`, porque nadie podía responder en esta sesión. Tampoco medí los minutos hasta el primer resultado.

**Lo que hay que atender:** la señal `declared_close_vs_evidence`, que cita `2026-09/40-soportes/correo-estado-del-cierre.md`. Según el motor, las 7 señales abiertas son:
- 2 de `ledger_vs_trial_balance`
- 1 de `bank_unreconciled`
- 2 de `einvoice_duplicate`
- 1 de `einvoice_amount_mismatch`
- 1 de `reconciliation_stale`

El detalle por señal está en `resultados.json`. No lo abrí.

**Checklist:**

| Estado | Tareas |
|---|---|
| Cumplidas con evidencia | C-01 a C-05 |
| En plazo | C-06 y C-07 |
| Bloqueadas | C-08 y C-09 |

La ruta crítica es C-07 → C-08 → C-09. Aprueba Sofía León.

**Qué falta para que esto sea mejor:**
- el auxiliar de proveedores (2205), que se concilia pero no tiene auxiliar en la carpeta;
- el marco contable de la entidad, que quedó «por confirmar»;
- la aprobación del checklist por una persona;
- la confirmación de los festivos: dejé el 2026-10-12, que viene del ejemplo.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

Archivos en la carpeta de la sesión:
- configuración: `.criterio/finanzas/900765432/config.json`
- reporte: `estado-finanzas/900765432-almacenes-caribe/cierre/2026-09/reporte-close-status.md`
- salida de la corrida: `estado-finanzas/900765432-almacenes-caribe/corridas/salida-finance-setup.md`