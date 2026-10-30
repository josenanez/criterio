# /criterio-treasury:treasury-setup finanzas/89090314-minera-del-motagua

## Listo — Minera del Motagua · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-8901 y pacifico-8902) · programa de pagos sí · política sí · registro de deuda sí.
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 (versión 1.0.0, términos 1.3). El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-1.0.0-2026-10-06.md`.

**Supuestos de esta prueba sin interfaz** (nadie respondió, así que usé lo que dicen los documentos):
- La moneda funcional es GTQ, tomada de la configuración de Clara.
- No hay cuentas en otra moneda, así que `treasury.currencies` quedó vacío.
- Los umbrales son los de `config.example.json`: 10 % de desviación, 30 días de vencimiento y 10 % de margen del covenant. Son configuración, no norma.
- El estado se guarda en `estado-finanzas/89090314-minera-del-motagua`, el mismo que usan Clara y Tomás.
- No marqué la raíz con `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

La configuración quedó en `.criterio/tesoreria/89090314/config.json` y el motor la validó sin problemas.

### La posición de caja al 2026-09-30
**Caja consolidada:** 1,097,200.00 GTQ.

| Cuenta | Saldo | Mínimo | Proyectado |
|---|---|---|---|
| andino-8901 | 347,200.00 | 441,640.00 | 347,200.00 |
| pacifico-8902 | 750,000.00 | 350,000.00 | 750,000.00 |

La desviación contra la proyección es 0.00 % en ambas cuentas.

### Lo que hay que atender
El motor encontró 3 señales.
1. **Caja bajo el mínimo.** andino-8901 está 94,440.00 por debajo del mínimo de la política. La cita es `2026-09/20-bancos/andino-8901/extracto.pdf` fila 17 y `00-referencia/politica-tesoreria.csv` fila 2. Esta es la única que sale en el reporte de cash-position.
2. **Un firmante sin autoridad** (`signatory_without_authority`).
3. **Un covenant en riesgo** (`covenant_at_risk`).

Las señales 2 y 3 salieron en el cálculo, pero no están en este reporte. Las detallan `payment-check` y `debt-watch`.

Todo lo que llegó se procesó, sin archivos ilegibles. El reporte completo está en `estado-finanzas/89090314-minera-del-motagua/tesoreria/2026-09/reporte-cash-position.md`. La salida está en `corridas/salida-treasury-setup.md` y la corrida quedó registrada como `2026-10-06-treasury-setup-1`.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.