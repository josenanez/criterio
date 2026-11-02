# /criterio-treasury:treasury-setup finanzas/88457812-7-banco-del-tebicuary-sintetico

## Listo — Banco del Tebicuary (sintético) · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-13101 y pacifico-13102). Hay programa de pagos, flujo proyectado, política de tesorería, matriz de firmas, registro de deuda y covenants.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.2.0 (términos 1.3). El comprobante quedó en `.criterio/terminos/aceptacion-criterio-treasury-1.2.0-2026-10-06.md` y `.pdf`. Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Como nadie respondía preguntas, tomé estas respuestas por defecto:
- **Carpeta raíz:** la del argumento.
- **Moneda funcional:** PYG, la de la configuración de Clara.
- **Cuenta en otra moneda:** pacifico-13102 en USD, porque su extracto trae la columna de moneda.
- **Umbrales:** 10 % de desviación, 30 días de vencimiento y 10 % de margen del covenant, los de `config.example.json`.
- **Estado:** `estado-finanzas/88457812-7-banco-del-tebicuary-sintetico`.

No marqué la raíz con `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

# La posición de caja · periodo 2026-09 (corte 2026-09-30)

**Caja consolidada:** 3.375.030.390.000,00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-13101 | PYG | 30.390.000,00 | 195.000,00 | 30.390.000,00 | 0,00 |
| pacifico-13102 | USD | 450.000.000,00 | 210.000.000,00 | 450.000.000,00 | 0,00 |

Las dos cuentas están sobre su mínimo y coinciden con la proyección.

**Lo que hay que atender:** la posición en USD, convertida con la tasa de la política, equivale a 3.375.000.000.000,00 PYG. Eso supera el límite de exposición de 1.687.500.000.000,00 (señal `fx_exposure_over_limit`). Las citas son `2026-09/20-bancos/pacifico-13102/extracto.csv` fila 3 y `00-referencia/politica-tesoreria.csv` fila 7.

**Lo que no se pudo procesar:** nada. Todo lo que llegó se procesó.

El cómputo levantó otras dos señales que este reporte no detalla: `signatory_without_authority` (1) y `covenant_at_risk` (1). Salen en `payment-check` y `debt-watch`.

El reporte lo escribió el motor en `estado-finanzas/88457812-7-banco-del-tebicuary-sintetico/tesoreria/2026-09/reporte-cash-position.md`. La salida completa y la corrida quedaron registradas (`2026-10-06-treasury-setup-1`).

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.