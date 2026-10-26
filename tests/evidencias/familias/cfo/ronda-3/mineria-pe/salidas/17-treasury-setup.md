# /criterio-treasury:treasury-setup finanzas/20730000015-minera-puna-alta

## Listo — Minera Puna Alta (20730000015) · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-7301, pacifico-7302). También están el programa de pagos, la política y el registro de deuda.
**Términos:** aceptados para la versión 0.9.0 (términos 1.2) a nombre de José Francisco Ñáñez, fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.9.0-2026-10-06.md`.

**Decisiones que tomé por la persona, porque nadie podía responder:**
- Las dos cuentas están en PEN, así que no declaré cuentas en otra moneda.
- Usé los umbrales de `config.example.json`: 10 % de desviación, 30 días de vencimiento y 10 % de margen de covenant. Son configuración, no norma.
- El estado queda en `estado-finanzas/20730000015-minera-puna-alta`, fuera de la carpeta de documentos.
- No marqué la raíz con `marcar-raiz`: no hacía falta y nadie lo autorizó.

La configuración está en `.criterio/tesoreria/20730000015/config.json` y pasó la validación. El cálculo también levantó una señal de covenant. La detalla `debt-watch`, no este reporte.

# La posición de caja · Minera Puna Alta · periodo 2026-09

**Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Aprueba:** Sofía León

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | `cash_below_minimum` | andino-7301: saldo 56,802.00 PEN, bajo el mínimo de 74,162.40 | 17,360.40 | `2026-09/20-bancos/andino-7301/extracto.xlsx` fila 17 · `00-referencia/politica-tesoreria.csv` fila 2 |
| 2 | `cash_vs_forecast` | pacifico-7302: saldo 180,000.00 contra 234,000.00 proyectado (-23.1) | 54,000.00 | `2026-09/20-bancos/pacifico-7302/extracto.xlsx` fila 3 · `2026-09/60-tesoreria/flujo-proyectado.csv` fila 3 |

## El resultado

**Caja consolidada:** 236,802.00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-7301 | PEN | 56,802.00 | 74,162.40 | 56,802.00 | 0.00 |
| pacifico-7302 | PEN | 180,000.00 | 84,000.00 | 234,000.00 | -23.08 |

Todo lo que llegó se procesó. El reporte no hizo preguntas. Fuentes: la política, los dos extractos y el flujo proyectado. El reporte completo está en `estado-finanzas/20730000015-minera-puna-alta/tesoreria/2026-09/reporte-cash-position.md`.

Áurea no mueve dinero ni entra a un portal bancario: procesa las exportaciones.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La corrida quedó registrada como `2026-10-06-treasury-setup-1`, con 3 hallazgos. La salida completa está en `estado-finanzas/20730000015-minera-puna-alta/corridas/salida-treasury-setup.md`.