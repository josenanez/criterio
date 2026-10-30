# /criterio-finance:finance-setup finanzas/97217352-comercial-control-de-guatemala

## Listo — Comercial Control de Guatemala

**Lo que miré:** 66 archivos, con los periodos 2026-01 a 2026-09 y el presupuesto 2026. Ninguno quedó fuera de la estructura.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.0.0 (términos 1.3). El comprobante quedó en `.criterio/terminos/aceptacion-criterio-finance-1.0.0-2026-10-06.md` y `.pdf`.

**Estado del cierre de 2026-09:**
- **Declarado:** en curso, según el correo de Sofía León del 2026-10-05 (`2026-09/40-soportes/correo-estado-del-cierre.md`).
- **Avance:** 53.85 % con evidencia y 53.85 % declarado.
- **Tareas con evidencia:** C-01 a C-05 están cumplidas, cada una con su PDF de soporte en `2026-09/40-soportes/`.
- **Tareas pendientes:**
  - C-06 (papeles de impuestos) y C-07 (cuadre del balance) están en plazo y vencen el 2026-10-07.
  - C-08 y C-09 están bloqueadas por C-07.
- **Ruta crítica:** C-07 → C-08 → C-09.
- **Señales abiertas:** ninguna. El motor devolvió cero señales y todo se procesó.
- **Checklist:** no está aprobado. El estado se calcula, pero una persona tiene que aprobarlo antes de darlo por bueno.

**Cómo quedó la configuración:**
- **Entidad:** NIT 97217352, Guatemala, moneda GTQ. Los tomé del nombre de la carpeta.
- **Cuentas de facturas:** ventas 4135, IVA generado y descontable 2408, compras 5135, 5145 y 5195. Salen de las facturas del periodo.
- **Cuentas a conciliar:** 1305 y 2205, que tienen auxiliar en 2026-08 y 2026-09.
- **Bancos:** andino-9701 y pacifico-9702.
- **Aprobador:** Contralor, por defecto. No puse festivos.

**Qué falta para que esto sea mejor:**
- **Marco contable:** puse NIIF por defecto. `config` no marcó problema, pero ningún documento lo confirma.
- **Checklist:** hace falta que una persona apruebe `00-referencia/checklist-cierre.xlsx`.
- **Comandos sin correr:** `bank-reconcile`, `einvoice-check`, `ledger-check` y `account-reconcile`. Este reporte solo cubre el checklist. El cuadre del balance (C-07) vence el 2026-10-07.
- **Marca de carpeta:** no dejé `_CRITERIO_FINANZAS.txt` en los documentos, porque nadie dio el sí.

Las diez preguntas las contesté con la respuesta sugerida por los documentos, sin confirmación de nadie. Quedaron en la ficha y en el reporte.

**Dónde quedó todo:**
- **Configuración:** `.criterio/finanzas/97217352/config.json`
- **Reporte:** `estado-finanzas/97217352-comercial-control-de-guatemala/cierre/2026-09/reporte-close-status.md`
- **Corrida registrada:** `2026-10-06-finance-setup-1`, con salida en `estado-finanzas/97217352-comercial-control-de-guatemala/corridas/salida-finance-setup.md`

**Cuándo vuelvo:** a diario durante la ventana del cierre, y una vez por semana fuera de ella.