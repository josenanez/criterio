# /criterio-finance:finance-setup finanzas/900123456-banco-andino

Clara quedó instalada sobre Banco Andino (NIT 900123456, Colombia, COP). El cierre de 2026-09 está en curso y el motor levantó 8 señales.

**Lo que miré:** 63 archivos, periodos 2026-01 a 2026-09 y `presupuesto-2026`, ninguno fuera de la estructura.

**Términos:** José Francisco Ñáñez aceptó la versión 0.9.0 (términos 1.2). Los comprobantes quedaron en `.criterio/terminos/aceptacion-criterio-finance-0.9.0-2026-10-06.md` y `.pdf`.

**Estado del cierre:**
- **Avance:** con evidencia 42,31 %; declarado 53,85 %. El correo de Sofía León del 2026-10-05 dice que el cierre está en curso.
- **Qué lo frena:** C-02 (conciliar cada cuenta bancaria) figura cumplida y no hay soporte `C-02` en `2026-09/40-soportes/`. Eso bloquea C-07, C-08 y C-09.
- **Ruta crítica:** C-02 → C-07 → C-08 → C-09.
- **Otras 7 señales:** el reporte de `close-status` solo detalla la de C-02. Las otras son 2 de libro mayor contra balance, 1 de balance descuadrado, 2 de bancos sin conciliar, 1 de factura con monto distinto y 1 partida conciliatoria antigua. Las muestran `ledger-check`, `bank-reconcile` y `einvoice-check`, que no corrí.
- **Checklist sin aprobar:** quedó como `approved: false` porque no hay aprobación registrada. Una persona tiene que aprobarlo.

**Respuestas tomadas por defecto:** nadie respondió, así que usé estas respuestas, que el reporte lista como preguntas.
- **Marco:** grupo 1 de NIIF, sin confirmar.
- **Cuentas que cruzan las facturas:** las de siempre (ventas 41; compras 14, 51, 52, 61; IVA 2408). El balance trae 4135 y 5105–5195, así que conviene confirmarlas.
- **Cuentas que se concilian:** 1305 y 2205, que son las que tienen auxiliar.
- **Bancos esperados:** andino-1101 y pacifico-1102.
- **Quién aprueba:** Sofía León.
- **Festivos:** solo el 2026-10-12 del ejemplo.

No dejé `_CRITERIO_FINANZAS.txt` en la carpeta porque nadie autorizó marcarla.

**Para mejorar el resultado:** falta el soporte firmado de C-02 y la aprobación del checklist. También faltan auxiliares para las cuentas que hoy no tienen, como 1435 Inventarios.

**Archivos:** todos están en `.../scratchpad/r3/banca/espacio/`.
- `.criterio/finanzas/900123456-banco-andino/config.json`
- `estado-finanzas/900123456-banco-andino/cierre/2026-09/reporte-close-status.md`
- `estado-finanzas/900123456-banco-andino/corridas/salida-finance-setup.md`

La corrida quedó registrada como `2026-10-06-finance-setup-1`. Hice 0 preguntas y no medí los minutos hasta el primer resultado.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.