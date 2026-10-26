# /criterio-treasury:treasury-setup finanzas/20710000019-banco-ribera

## Listo — Banco Ribera · tesorería 2026-09

Nadie podía contestar en esta prueba. Tomé la respuesta que sugerían los documentos en cada pregunta.

**Lo que miré:** 2 cuentas con extracto (andino-7101 y pacifico-7102). Hay programa de pagos, política de tesorería y registro de deuda.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.9.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.9.0-2026-10-06-2.md` y `.pdf`.

**Lo que respondí por la persona:**
- **Raíz:** la carpeta del argumento, `finanzas/20710000019-banco-ribera`. No la marqué con `marcar-raiz` porque la prueba no lo autorizó.
- **Entidad y periodo:** Banco Ribera, PEN, 2026-09, con Sofía León como aprobadora, igual que en la configuración de Clara.
- **Política:** usé `00-referencia/politica-tesoreria.csv` tal cual.
- **Otras monedas:** dejé `treasury.currencies` vacío. El extracto de pacifico-7102 trae la columna de moneda (USD) y el motor la toma de ahí.
- **Umbrales:** los de `config.example.json`: 10 % de desviación, 30 días de vencimiento y 10 % de margen del covenant. Son configuración, no norma.
- **Estado:** `estado-finanzas/20710000019-banco-ribera`.

**Lo que encontré al empezar:** la carpeta de corridas tenía rastros de una instalación anterior, pero no existía la configuración de tesorería. La escribí de nuevo en `.criterio/tesoreria/20710000019-banco-ribera/config.json` y registré otra vez la aceptación de términos.

**Posición de caja al 2026-09-30 (la calculó el motor):**

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-7101 | PEN | 16,959.20 | 4,479.60 | 16,959.20 | 0.00 |
| pacifico-7102 | USD | 120,000.00 | 56,000.00 | 120,000.00 | 0.00 |

La caja consolidada es 136,959.20. Las dos cuentas están sobre su mínimo.

**Lo que hay que atender:** la posición en USD equivale a 120,000.00 PEN con la tasa de la política, sobre el límite de 60,000.00 (`fx_exposure_over_limit`). El reporte cita `pacifico-7102/extracto.csv`, fila 3, y `politica-tesoreria.csv`, fila 7.

El cómputo dejó otras dos señales: un firmante sin autoridad (`signatory_without_authority`) y un vencimiento cercano (`maturity_near`). `/payment-check` y `/debt-watch` las detallan; el reporte de caja no.

**Archivos:**
- Reporte: `estado-finanzas/20710000019-banco-ribera/tesoreria/2026-09/reporte-cash-position.md`
- Salida de la corrida: `estado-finanzas/20710000019-banco-ribera/corridas/salida-treasury-setup.md`, registrada como `2026-10-06-treasury-setup-2`

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.