# /criterio-treasury:treasury-setup finanzas/76083001-1-tiendas-pacifico

## Listo — Tiendas Pacífico · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto · programa de pagos sí · política sí · registro de deuda sí
**Términos:** aceptados a nombre de José Francisco Ñáñez para la versión 0.10.0, con fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06.md`.

En una línea por pregunta, como pediste:
- **Carpeta raíz:** usé la del argumento, `finanzas/76083001-1-tiendas-pacifico`.
- **Moneda y periodo:** tomé la moneda funcional (CLP) y el periodo (2026-09) de la configuración de Clara.
- **Cuentas en otra moneda:** dejé `treasury.currencies` vacío, porque el motor leyó la moneda del extracto. El extracto de pacifico-8302 la trae como USD.
- **Umbrales:** los de `config.example.json` (10 % de desviación, 30 días de vencimiento, 10 % de margen del covenant). Son configuración, no norma.
- **Dónde guardo lo que encuentro:** `estado-finanzas/76083001-1-tiendas-pacifico`, el mismo estado de Clara y Tomás.

# La posición de caja · Tiendas Pacífico · periodo 2026-09

**Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Aprueba:** Contralor

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | `fx_exposure_over_limit` | La posición en USD, convertida con la tasa de la política, equivale a 7.125.000.000,00 CLP. El límite es 3.562.500.000,00. | `2026-09/20-bancos/pacifico-8302/extracto.pdf` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |

Además de esa señal, el motor detectó dos más: `payment_without_approval` (un pago sin aprobación suficiente) y `maturity_near` (un vencimiento cercano). El reporte de `cash-position` solo detalla la de exposición. Las otras dos las detallan `/payment-check` y `/debt-watch`.

## El resultado

**Caja consolidada:** 7.126.025.250,00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-8301 | CLP | 1.025.250,00 | 262.625,00 | 1.025.250,00 | 0,00 |
| pacifico-8302 | USD | 7.500.000,00 | 3.500.000,00 | 7.500.000,00 | 0,00 |

| Moneda | Posición en moneda funcional | Límite |
|---|---|---|
| USD | 7.125.000.000,00 | 3.562.500.000,00 |

Áurea no mueve dinero ni entra a un portal bancario: procesa las exportaciones.

**Lo que no se pudo procesar:** todo lo que llegó se procesó.
**Las preguntas que hizo:** ninguna en esta corrida.
**Fuentes:** `00-referencia/politica-tesoreria.csv` · `2026-09/20-bancos/pacifico-8302/extracto.pdf`

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La salida completa quedó en `estado-finanzas/76083001-1-tiendas-pacifico/corridas/salida-treasury-setup.md`. La corrida quedó registrada como `2026-10-06-treasury-setup-1`, con 3 hallazgos.

La configuración quedó en `.criterio/tesoreria/76083001-1-tiendas-pacifico/config.json`. Para el nombre de la carpeta usé el mismo identificador que Clara, NIT más nombre, y no solo el NIT. No creé ni moví nada dentro de la carpeta de documentos.