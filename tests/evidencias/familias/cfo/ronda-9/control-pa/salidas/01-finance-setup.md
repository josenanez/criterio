# /criterio-finance:finance-setup finanzas/155831003-2-2013-comercial-control-del-istmo

## Listo — Comercial Control del Istmo (RUC 155831003-2-2013, PA, USD)

**Lo que miré:** 66 archivos, periodos 2026-01 a 2026-09 y presupuesto-2026. Ninguno está fuera de la estructura.

**Términos:** los acepté para la versión 1.0.0 (términos 1.3) a nombre de José Francisco Ñáñez, como indicaba la prueba. Los comprobantes quedaron en `.criterio/terminos/aceptacion-criterio-finance-1.0.0-2026-10-06.md` y `.pdf`.

**Estado del cierre 2026-09:**
- Sofía León declaró el cierre «en curso» en un correo del 2026-10-05.
- El avance con evidencia es 53.85 % y el declarado también es 53.85 %.
- C-01 a C-05 están cumplidas con evidencia. C-06 y C-07 están en plazo.
- C-08 está bloqueada por C-07 y C-09 por C-08. La ruta crítica es C-07 → C-08 → C-09.
- El reporte dice «Nada abierto». Eso solo vale para `close-status`: todavía no corrí el cuadre del mayor, la conciliación de bancos, las facturas contra la contabilidad ni la conciliación de cuentas.

**Decisiones que tomé por mi cuenta, porque nadie podía contestar:**
- **Marco contable:** NIIF. Es una sugerencia; ningún documento lo confirma.
- **Cuentas:**
  - Ventas 4135.
  - Compras 5135, 5145 y 5195.
  - IVA generado y descontable 2408.
  - Conciliación de 1305 y 2205, que tienen auxiliar en agosto y septiembre.
  - Bancos andino-8301 y pacifico-8302.
- **Aprobadora:** Sofía León, Contralora, según la matriz de firmas y el correo del cierre.
- **Checklist:** existe uno en `00-referencia/`, pero nada dice que esté aprobado. Lo dejé como no aprobado y el reporte lo advierte.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`. Escribir dentro de los documentos pide un sí de la persona.
- **Festivos:** no los encontré, así que la lista quedó vacía.

**Qué falta para mejorarlo:**
- Que una persona apruebe el checklist.
- Correr `ledger-check`, `bank-reconcile`, `einvoice-check` y `account-reconcile`.

**Cuándo vuelvo:** a diario durante la ventana del cierre, y una vez por semana fuera de ella.

La configuración está en `.criterio/finanzas/155831003-2-2013-comercial-control-del-istmo/config.json`. El reporte completo está en `estado-finanzas/155831003-2-2013-comercial-control-del-istmo/cierre/2026-09/reporte-close-status.md`. La corrida quedó registrada como `2026-10-06-finance-setup-1`.