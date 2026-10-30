# /criterio-finance:finance-setup finanzas/31452078000170-lojas-paulistas

## Listo — Lojas Paulistas

**Lo que miré:** 65 archivos, periodos 2026-01 a 2026-09 y `presupuesto-2026`, 0 fuera de la estructura.
**Términos:** aceptados a nombre de José Francisco Ñáñez el 2026-10-06 para la versión 0.12.1. El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-0.12.1-2026-10-06.md` y `.pdf`.

La configuración quedó en `.criterio/finanzas/31452078000170/config.json`. Como nadie respondió, tomé las respuestas sugeridas:
- Los prefijos de cuentas salen de las facturas del periodo.
- Los bancos y las cuentas a conciliar salen de los auxiliares.
- Sofia Leão aprueba el cierre, porque ella lo declara en su correo.
- El marco CPC (IFRS) es una propuesta mía. Ningún documento lo dice.

**Estado del cierre 2026-09:** el correo de Sofia Leão del 2026-10-05 dice que el cierre está cerrado. El motor encuentra 6 señales abiertas.
- **Avance:** 42,31 % con evidencia contra 53,85 % declarado.
- **C-02:** la conciliación de cada cuenta bancaria figura cumplida (responsable: André Pacheco), pero no hay soporte en `2026-09/40-soportes/`.
- **Ruta crítica:** C-02 → C-07 → C-08 → C-09.
- **Señales abiertas:** tarea cumplida sin evidencia, cierre declarado contra evidencia, factura sin registro, banco sin conciliar, diferencia de monto en una factura y partida conciliatoria antigua.
- **Checklist:** no está aprobado. Una persona tiene que aprobarlo antes de darlo por bueno.

El reporte completo está en `estado-finanzas/31452078000170-lojas-paulistas/cierre/2026-09/reporte-close-status.md`. La salida y la corrida quedaron registradas en `estado-finanzas/31452078000170-lojas-paulistas/corridas/`.

**Qué falta para mejorar:**
- El soporte de C-02.
- Los soportes de C-06 a C-09.
- El extracto del banco bandeirante-2901 viene en PDF.

No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta de documentos. Sin una persona que lo autorizara, no escribí nada ahí.

**Cuándo vuelvo:** a diario durante la ventana del cierre, y una vez por semana fuera de ella.