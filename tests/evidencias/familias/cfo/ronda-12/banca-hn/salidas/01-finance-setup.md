# /criterio-finance:finance-setup finanzas/08010004578120-banco-de-occidente-sintetico

## Listo — Banco de Occidente Sintético

Instalé a Clara sobre la entidad y calculé el estado del cierre de septiembre de 2026: está declarado «en curso» y la tarea C-02 figura cumplida sin soporte.

**Lo que miré:** 66 archivos, periodos 2026-01 a 2026-09 más `presupuesto-2026`, y ninguno fuera de la estructura.
**Términos:** José Francisco Ñáñez los aceptó para la versión 1.1.0 (términos 1.3) el 2026-10-06. Los comprobantes quedaron en `.criterio/terminos/aceptacion-criterio-finance-1.1.0-2026-10-06.md` y `.pdf`.

**Estado del cierre:**
- **Declarado:** «en curso», según Sofía León en el correo del 2026-10-05.
- **Avance:** 42.31 % con evidencia, contra 53.85 % declarado.
- **C-02 (conciliar bancos):** figura cumplida y no hay soporte `C-02` en `40-soportes/`. Bloquea la ruta crítica C-02 → C-07 → C-08 → C-09.
- **Checklist:** no está aprobado.

El reporte completo quedó en `estado-finanzas/08010004578120-banco-de-occidente-sintetico/cierre/2026-09/reporte-close-status.md`.

**Qué falta para mejorarlo:**
- El soporte de la tarea C-02.
- Que una persona apruebe el checklist.
- El comando `compute` levantó 7 señales, pero este reporte solo muestra la primera. Las otras 6 son:
  - dos diferencias entre el mayor y el balance;
  - un balance de comprobación que no cuadra;
  - una factura fuera de la autorización;
  - un banco sin conciliar;
  - una diferencia de monto en una factura.
  Las revisan otros comandos (`ledger-check`, `bank-reconcile`, `einvoice-check`).

**Respuestas que tomé por defecto (nadie contestó):**
- **Marco contable:** NIIF, porque la carpeta no lo declara.
- **Aprobador del cierre:** «Contralor».
- **Festivos:** ninguno.
- **Cuentas de las facturas:** ventas 4135, IVA 2408 y compras 5135, 5145 y 5195.
  - `cuentas` no devolvió ninguna, porque las facturas de Honduras no traen XML.
  - Esas tres de compras las propuse porque sus débitos más el ISV de 15 % cuadran con lo acreditado en 2205.
  - Dejé fuera 5105 y 5305, que ninguna factura sostiene.
- **Cuentas que se concilian:** 1305 y 2205, que tienen auxiliar en agosto y septiembre.
- **Bancos esperados:** `andino-10901` y `pacifico-10902`.

No dejé `_CRITERIO_FINANZAS.txt` en la carpeta: nadie dio el sí para marcarla. Registré la corrida (`2026-10-06-finance-setup-1`). No medí los minutos hasta el primer resultado.

**Cuándo vuelvo:** a diario durante la ventana del cierre, y una vez por semana fuera de ella.