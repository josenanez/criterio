# /criterio-treasury:treasury-setup finanzas/08010004578120-banco-de-occidente-sintetico

## Listo — Banco de Occidente Sintético · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-10901 y pacifico-10902). Hay programa de pagos y política de tesorería. El registro de deuda está en `00-referencia/registro-deuda.xlsx`.

**Términos:** aceptados para la versión 1.1.0 a nombre de José Francisco Ñáñez, con fecha 2026-10-06. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-treasury-1.1.0-2026-10-06.md` y en PDF.

**Lo que decidí por defecto, porque nadie respondió:**
- **Configuración:** quedó en `.criterio/tesoreria/08010004578120/config.json`. Tomé la entidad y la moneda funcional (HNL) de la configuración de Clara.
- **Umbrales:** los de `config.example.json`, que son 10 % de desviación contra la proyección, 30 días de vencimiento y 10 % de margen del covenant.
- **Estado:** `estado-finanzas/08010004578120-banco-de-occidente-sintetico`.
- **Marca de la carpeta:** no escribí `_CRITERIO_FINANZAS.txt`, porque nadie la autorizó.
- **Cuentas en otra moneda:** dejé `treasury.currencies` vacío. El motor tomó la moneda de cada cuenta del extracto.

# La posición de caja · periodo 2026-09 (corte 2026-09-30)

**Caja consolidada:** 39,279,700.00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-10901 | HNL | 279,700.00 | 89,850.00 | 279,700.00 | 0.00 |
| pacifico-10902 | USD | 1,500,000.00 | 700,000.00 | 1,500,000.00 | 0.00 |

### Lo que hay que atender
La posición en USD equivale a 39,000,000.00 HNL con la tasa de la política y supera el límite de 19,500,000.00. La fuente es `2026-09/20-bancos/pacifico-10902/extracto.pdf` (fila 3) junto con `00-referencia/politica-tesoreria.csv` (fila 7).

Además de esa señal, `compute` encontró otras dos:
- **Firmante sin autoridad** (`signatory_without_authority`).
- **Covenant en riesgo** (`covenant_at_risk`).

El reporte de `cash-position` solo muestra la de exposición. Las otras dos salen en `payment-check` y `debt-watch`, que no corrí. Ninguna de las dos está desarrollada aquí.

**Lo que no se pudo procesar:** todo lo que llegó se procesó.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La salida completa está en `estado-finanzas/08010004578120-banco-de-occidente-sintetico/corridas/salida-treasury-setup.md` y la corrida quedó registrada como `2026-10-06-treasury-setup-1`.