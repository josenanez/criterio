# /criterio-finance:finance-setup finanzas/3101457812-banco-del-valle-central-sintetico

## Listo — Banco del Valle Central (sintético)

**Lo que miré:** 66 archivos, con periodos 2026-01 a 2026-09 y `presupuesto-2026`. Ninguno está fuera de la estructura recomendada.
**Términos:** José Francisco Ñáñez aceptó la versión 1.3 el 2026-10-06. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-1.0.0-2026-10-06.md` y en el `.pdf` del mismo nombre.

# Estado del cierre · periodo 2026-09

**Estado declarado:** en curso (correo de Sofía León, 2026-10-05).
**Avance con evidencia:** 42,31 %. **Avance declarado:** 53,85 %.
El checklist no está aprobado. Una persona tiene que aprobarlo antes de darlo por bueno.

**Lo que hay que atender:** C-02, "Conciliar cada cuenta bancaria" (Andrés Paz, vence el 2026-10-02), figura cumplida y no hay soporte en `2026-09/40-soportes/`.

**Ruta crítica:** C-02 → C-07 → C-08 → C-09. C-07, C-08 y C-09 quedan bloqueadas por C-02.

El cálculo dio 6 señales en total:
- `ledger_vs_trial_balance`: 2
- `trial_balance_unbalanced`: 1
- `close_task_done_without_evidence`: 1
- `bank_unreconciled`: 1
- `einvoice_amount_mismatch`: 1

El reporte `close-status` solo detalla la de C-02, así que las otras cinco no tienen detalle todavía. Están en `resultados.json`, en la misma carpeta del reporte.

**Lo que no se pudo procesar:** nada. Todo lo que llegó se procesó.

## Cómo respondí a las preguntas
Nadie podía contestar, así que tomé la respuesta sugerida a partir de los documentos. Quedaron registradas en la ficha y en el reporte.
- **País y moneda:** Costa Rica y CRC, por los XML y el registro de deuda.
- **Marco:** NIIF, sugerido porque ningún documento lo dice.
- **Cuentas de facturas:** ventas 4135; compras 5135, 5145 y 5195; IVA 2408. Son las que sostienen las facturas.
- **Cuentas a conciliar:** 1305 y 2205, que tienen auxiliar en agosto y septiembre.
- **Bancos esperados:** andino-10101 y pacifico-10102.
- **Aprobador:** Contralor, por defecto. No hay festivos cargados.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt` porque nadie autorizó escribir en la carpeta de documentos.

## Qué falta para que esto sea mejor
- **Soporte de C-02:** falta el soporte de la conciliación bancaria. Sin él, las tareas C-07 a C-09 siguen bloqueadas.
- **Checklist:** hace falta que alguien lo apruebe.
- **R-09 del auditor:** el requerimiento sobre partidas conciliatorias de más de 90 días no está en la tabla PBC. Lo registré en la ficha (vence el 2026-10-09, Andrés Paz).
- **Festivos:** si los tienes a mano, mejoran el cálculo de la ventana del cierre.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.

Los archivos quedaron en estos lugares:
- La configuración, en `.criterio/finanzas/3101457812/config.json`.
- La ficha, en `estado-finanzas/3101457812-banco-del-valle-central-sintetico/cierre/2026-09/ficha.json`.
- El reporte, en `estado-finanzas/3101457812-banco-del-valle-central-sintetico/cierre/2026-09/reporte-close-status.md`.
- La salida de esta corrida, en `estado-finanzas/3101457812-banco-del-valle-central-sintetico/corridas/salida-finance-setup.md`. La corrida quedó registrada como `2026-10-06-finance-setup-1`.