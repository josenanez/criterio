# /criterio-treasury:treasury-setup finanzas/900765432-almacenes-caribe

## Listo — Almacenes Caribe · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-3701 y pacifico-3702). También hay programa de pagos, política de tesorería y registro de deuda.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.10.0, por tu indicación de la prueba. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06-2.md`.

**Configuración:** la dejé en `.criterio/tesoreria/900765432-almacenes-caribe/config.json`.
- Entidad, moneda funcional (COP), periodo (2026-09) y quien aprueba (Sofía León) salen de la configuración de Clara.
- Los umbrales son los del ejemplo: 10 %, 30 días y 10 %. Son configuración, no norma.
- `currencies` quedó vacío porque los extractos traen su columna de moneda.
- El estado queda en `estado-finanzas/900765432-almacenes-caribe`.
- No hice preguntas, porque nadie podía responder.

La carpeta ya tenía la configuración de Clara, así que no hizo falta buscar ni marcar la raíz.

# La posición de caja · Almacenes Caribe · periodo 2026-09

**Corte:** 2026-09-30 · **Aprueba:** Sofía León

**Lo que hay que atender**

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | `fx_exposure_over_limit` | La posición en USD equivale a 96.000.000.000,00 COP, sobre el límite de 48.000.000.000,00 de la política. | `2026-09/20-bancos/pacifico-3702/extracto.xlsx` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |

**Resultado.** Caja consolidada: 96.008.040.800,00.

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-3701 | COP | 8.040.800,00 | 3.220.400,00 | 8.040.800,00 | 0,00 |
| pacifico-3702 | USD | 24.000.000,00 | 11.200.000,00 | 24.000.000,00 | 0,00 |

Las dos cuentas están sobre su mínimo y no se desvían de la proyección. El motor procesó todo lo que llegó.

El cálculo marcó además un vencimiento cercano (`maturity_near`). No sale en este reporte; se ve con `/debt-watch`.

El reporte completo está en `estado-finanzas/900765432-almacenes-caribe/tesoreria/2026-09/reporte-cash-position.md`.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La corrida quedó registrada como `2026-10-06-treasury-setup-2`. La salida está en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-treasury-setup.md`.