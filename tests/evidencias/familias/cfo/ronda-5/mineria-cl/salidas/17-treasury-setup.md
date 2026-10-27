# /criterio-treasury:treasury-setup finanzas/76089001-4-minera-atacama-norte

## Listo — Minera Atacama Norte · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-8901 y pacifico-8902). Hay programa de pagos, política de tesorería y registro de deuda.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06.md`.

Como nadie podía contestar, tomé las respuestas sugeridas de los documentos:
- **Moneda funcional:** CLP, la de la configuración de Clara.
- **Otras monedas:** ninguna cuenta está en otra moneda.
- **Umbrales:** los de `config.example.json`: 10 % de desviación, 30 días de vencimiento y 10 % de margen de covenant.
- **Estado:** `estado-finanzas/76089001-4-minera-atacama-norte`.
- **Marca de la raíz:** no puse `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

La configuración quedó en `.criterio/tesoreria/76089001-4-minera-atacama-norte/config.json`.

Esto es lo que salió de la posición de caja (reporte del motor):

### La posición de caja · periodo 2026-09 (corte 2026-09-30)

**Lo que hay que atender**

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | `cash_below_minimum` | andino-8901: saldo 8.732.100,00 CLP, bajo el mínimo de 11.078.520,00 | 2.346.420,00 | `2026-09/20-bancos/andino-8901/extracto.xlsx` fila 17 · `00-referencia/politica-tesoreria.csv` fila 2 |

**Caja consolidada:** 26.732.100,00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-8901 | CLP | 8.732.100,00 | 11.078.520,00 | 8.732.100,00 | 0,00 |
| pacifico-8902 | CLP | 18.000.000,00 | 8.400.000,00 | 18.000.000,00 | 0,00 |

Todo lo que llegó se procesó, y no hubo preguntas en esta corrida.

El cálculo dio otras dos señales que este reporte no detalla: `signatory_without_authority` (1) y `covenant_at_risk` (1). Las verán `/payment-check` y `/debt-watch`.

Áurea no mueve dinero ni entra a un portal bancario: procesa las exportaciones.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La salida completa quedó en `estado-finanzas/76089001-4-minera-atacama-norte/corridas/salida-treasury-setup.md`. La corrida quedó registrada como `2026-10-06-treasury-setup-1`, con 3 hallazgos.