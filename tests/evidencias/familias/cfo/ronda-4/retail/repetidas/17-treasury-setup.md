# /criterio-treasury:treasury-setup finanzas/900765432-almacenes-caribe

Dos cosas que tomé por defecto, porque nadie respondió en esta prueba. Los umbrales son los de `config.example.json`: desviación 10 %, 30 días de vencimiento y margen de covenant 10 %. Son configuración, no norma. Tampoco declaré cuentas en otra moneda, porque el extracto de pacifico-3702 ya trae la columna de moneda.

## Listo — Almacenes Caribe · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-3701 y pacifico-3702). También hay programa de pagos, política y registro de deuda.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0, términos 1.2. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06.md` y en el `.pdf` del mismo nombre.

**Lo que hay que atender**
- La política fija la tasa USD en 1, así que la posición en USD y su equivalente en COP salen iguales. Conviene verificarlo.
- La cuenta pacifico-3702 (USD) equivale a 24.000.000,00 COP, sobre el límite de exposición de 12.000.000,00. Citas: `2026-09/20-bancos/pacifico-3702/extracto.xlsx` fila 3 y `00-referencia/politica-tesoreria.csv` fila 7.
- El motor marcó una obligación por vencer (`maturity_near`). El reporte de caja no la muestra. La detalla `debt-watch`, que no corrí aquí.

**Posición de caja** (corte 2026-09-30; la caja consolidada es 32.040.800,00)

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-3701 | COP | 8.040.800,00 | 3.220.400,00 | 8.040.800,00 | 0,00 |
| pacifico-3702 | USD | 24.000.000,00 | 11.200.000,00 | 24.000.000,00 | 0,00 |

Las dos cuentas están sobre su mínimo. Todo lo que llegó se procesó, y no hubo preguntas en esta corrida.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

**Dónde quedó cada cosa:**
- Configuración: `.criterio/tesoreria/900765432-almacenes-caribe/config.json`
- Reporte completo: `estado-finanzas/900765432-almacenes-caribe/tesoreria/2026-09/reporte-cash-position.md`
- Salida guardada: `estado-finanzas/900765432-almacenes-caribe/corridas/salida-treasury-setup.md`
- Corrida registrada como `2026-10-06-treasury-setup-1`.

No marqué la raíz con `_CRITERIO_FINANZAS.txt`: ya la usan Clara y Tomás, y nadie autorizó cambiarla.