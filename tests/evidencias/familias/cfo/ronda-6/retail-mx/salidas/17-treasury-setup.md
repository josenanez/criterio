# /criterio-treasury:treasury-setup finanzas/TBA180912Q37-tiendas-del-bajio

Áurea quedó instalada para Tiendas del Bajío (TBA180912Q37) y ya calculó la posición de caja de 2026-09.

**Lo que miré:** 2 cuentas con extracto (andino-1701 y pacifico-1702), con programa de pagos, política y registro de deuda presentes.

**Preguntas:** hice cero. Las respondí con los documentos:
- **Moneda:** MXN, como en la configuración de Clara. Ambos extractos vienen en MXN, así que no hay cuentas en otra moneda.
- **Umbrales:** los de `config.example.json`: 10 % de desviación, 30 días de vencimiento y 10 % de margen del covenant.
- **Estado:** `estado-finanzas/TBA180912Q37-tiendas-del-bajio`, igual que Clara.

**Términos:** José Francisco Ñáñez los aceptó (2026-10-06) para la versión 0.11.0 (términos 1.2). El comprobante en Markdown y PDF quedó en `.criterio/terminos/`.

**Posición de caja al 2026-09-30:**

| Cuenta | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|
| andino-1701 | 165,060.00 | 67,530.00 | 165,060.00 | 0.00 |
| pacifico-1702 | 450,000.00 | 210,000.00 | 450,000.00 | 0.00 |

La caja consolidada es de 615,060.00 MXN. Las dos cuentas están por encima de su mínimo. El reporte de este comando no marca nada abierto.

El cálculo del periodo dejó 3 señales que corresponden a otros comandos:
- **Firmante sin autoridad:** 1, para `/payment-check`.
- **Vencimiento cercano:** 1, para `/debt-watch`.
- **Covenant en riesgo:** 1, para `/debt-watch`.

No les puse cifras porque este comando no las calcula.

**Archivos:**
- La configuración quedó en `.criterio/tesoreria/TBA180912Q37/config.json`.
- El reporte quedó en `estado-finanzas/TBA180912Q37-tiendas-del-bajio/tesoreria/2026-09/reporte-cash-position.md`.
- La salida y la corrida registrada quedaron en `corridas/salida-treasury-setup.md`.

No medí los minutos hasta el primer resultado.

Vuelvo cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.