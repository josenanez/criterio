# /criterio-treasury:treasury-setup finanzas/97217352-comercial-control-de-guatemala

## Listo — Comercial Control de Guatemala · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-9701, pacifico-9702), programa de pagos sí, política sí, registro de deuda sí.
**Términos:** aceptados por José Francisco Ñáñez el 2026-10-06 para la versión 1.0.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-1.0.0-2026-10-06.md`.

**Respuestas que tomé sin preguntar:**
- **Moneda:** ambos extractos traen la columna de moneda (GTQ), así que `treasury.currencies` quedó vacío.
- **Umbrales:** usé los de `config.example.json` (10 % de desviación, 30 días de vencimiento, 10 % de margen del covenant). Son configuración, no norma.
- **Estado:** `estado-finanzas/97217352-comercial-control-de-guatemala`, igual que Clara y Tomás.
- **Raíz:** la ruta venía en el argumento, así que no corrí `buscar-raiz` ni `marcar-raiz`.

**Dónde quedó la configuración:** `.criterio/tesoreria/97217352/config.json`. La escribí a mano y `config` la validó sin problemas.

# La posición de caja · periodo 2026-09 (corte 2026-09-30)

**Lo que hay que atender:** nada abierto en lo que procesa este comando.

**Caja consolidada:** 429,880.00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-9701 | GTQ | 129,880.00 | 54,940.00 | 129,880.00 | 0.00 |
| pacifico-9702 | GTQ | 300,000.00 | 140,000.00 | 300,000.00 | 0.00 |

Todo lo que llegó se procesó y el comando no hizo preguntas. El reporte completo está en `estado-finanzas/…/tesoreria/2026-09/reporte-cash-position.md`.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

**Corrida registrada:** `2026-10-06-treasury-setup-1`, con 0 hallazgos. La salida mostrada quedó en `estado-finanzas/…/corridas/salida-treasury-setup.md`.