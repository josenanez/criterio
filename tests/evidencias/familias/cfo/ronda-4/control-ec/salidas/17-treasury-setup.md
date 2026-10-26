# /criterio-treasury:treasury-setup finanzas/1790000001001-comercial-control

## Listo — Comercial Control · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-6701 y pacifico-6702). También encontré el programa de pagos, la política de tesorería y el registro de deuda.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0 con fecha 2026-10-06. El comprobante quedó en `.criterio/terminos/`, en Markdown y PDF.

**La configuración:** quedó en `.criterio/tesoreria/1790000001001/config.json`, y el motor la validó sin problemas. Reusé los datos de la configuración de Clara y Tomás:
- **Entidad:** Comercial Control, Ecuador, en USD, con Sofía León como aprobadora.
- **Moneda:** todas las cuentas están en USD, así que no hay cuentas en otra moneda.
- **Umbrales:** los de `config.example.json` (desviación 10 %, vencimiento 30 días, covenant 10 %). Son configuración, no norma.
- **Estado:** `estado-finanzas/1790000001001-comercial-control`.

No marqué la raíz porque no hizo falta.

### La posición de caja (reporte del motor)

**Entidad:** Comercial Control (1790000001001) · **Corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Aprueba:** Sofía León

**Lo que hay que atender:** nada abierto en lo que procesa este comando.

**Caja consolidada:** 69,933.75

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-6701 | USD | 24,933.75 | 10,966.88 | 24,933.75 | 0.00 |
| pacifico-6702 | USD | 45,000.00 | 21,000.00 | 45,000.00 | 0.00 |

Todo lo que llegó se procesó. El comando no hizo preguntas. El reporte quedó en `estado-finanzas/1790000001001-comercial-control/tesoreria/2026-09/reporte-cash-position.md`.

**La corrida:** quedó registrada como `2026-10-06-treasury-setup-1`, con 0 hallazgos. Hice cero preguntas a la persona porque la prueba no tenía interfaz y todo salió de los documentos.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.