# /criterio-finance:finance-setup finanzas/76097001-8-comercial-control-andes

## Listo — Comercial Control Andes

**Lo que miré:** 66 archivos, periodos 2026-01 a 2026-09, ninguno fuera de la estructura.
**Términos:** aceptados a nombre de José Francisco Ñáñez el 2026-10-06 para la versión 0.10.0. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-finance-0.10.0-2026-10-06.md` y en el mismo nombre con `.pdf`.

**Estado del cierre 2026-09:**
- **Declarado:** "en curso", según el correo de Sofía León del 2026-10-05.
- **Avance:** 53,85 % con evidencia y 53,85 % declarado.
- **Cumplidas con evidencia:** C-01, C-02, C-03, C-04 y C-05.
- **En plazo:** C-06 y C-07.
- **Bloqueadas:** C-08 (por C-07) y C-09 (por C-08).
- **Ruta crítica:** C-07 → C-08 → C-09.
- **Checklist:** no está aprobado. El estado se calcula igual, pero una persona tiene que aprobarlo.

**Cosas que debes revisar:**
- **Archivos sin procesar:** `compute` devolvió `no_procesado: 15` y 0 señales. Aun así, el reporte dice "Todo lo que llegó se procesó" y no cita ninguna fuente. No sé cuáles son esos 15 archivos, así que no confíes todavía en el 0.
- **Aprobador del cierre:** quedó "Contralor", el valor por defecto, porque ningún documento nombra a otra persona.
- **Valores que puse sin confirmar** (sesión sin interfaz):
  - País CL, moneda CLP y marco de las NIIF adoptadas por el Colegio de Contadores. Salen de las facturas DTE del SII y del RUT.
  - Ventas 4135, compras 5135/5145/5195 e IVA 2408, que son las cuentas que el motor encontró sosteniendo facturas.
  - Cuentas a conciliar 1305 y 2205, y bancos andino-9701 y pacifico-9702.
  - Checklist de la organización como no aprobado, con industria "comercio", que fue un supuesto mío.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt` porque nadie lo autorizó.

**Dónde quedó todo:**
- **Configuración:** `.criterio/finanzas/76097001-8/config.json`
- **Reporte del motor:** `estado-finanzas/76097001-8-comercial-control-andes/cierre/2026-09/reporte-close-status.md`
- **Lo que te mostré:** `estado-finanzas/76097001-8-comercial-control-andes/corridas/salida-finance-setup.md`

La corrida quedó registrada con el id `2026-10-06-finance-setup-1`.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.