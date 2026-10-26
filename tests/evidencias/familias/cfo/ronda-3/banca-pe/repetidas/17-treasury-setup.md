# /criterio-treasury:treasury-setup finanzas/20710000019-banco-ribera

## Listo — Banco Ribera · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-7101, pacifico-7102). Hay programa de pagos, política de tesorería y registro de deuda.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.9.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.9.0-2026-10-06.md` y `.pdf`.

**Decisiones que tomé por la persona (nadie podía contestar):**
- **Raíz:** usé la carpeta del argumento, `finanzas/20710000019-banco-ribera`. No la marqué con `marcar-raiz`: la prueba no autorizó esa marca.
- **Moneda y periodo:** PEN y 2026-09, como en la configuración de Clara.
- **Cuentas en otra moneda:** ninguna aparece en los documentos, así que `treasury.currencies` quedó vacío. La política sí fija un límite de exposición en USD (60,000.00).
- **Umbrales:** los de `config.example.json`: 10 % de desviación, 30 días de vencimiento y 10 % de margen del covenant. Son configuración, no norma.
- **Estado:** `estado-finanzas/20710000019-banco-ribera`, el mismo de Clara y Tomás.
- **Aprobador:** Sofía León, igual que en la configuración de Clara.

**Posición de caja al 2026-09-30 (la calculó el motor):**

| Cuenta | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|
| andino-7101 | 16,959.20 | 4,479.60 | 16,959.20 | 0.00 |
| pacifico-7102 | 120,000.00 | 56,000.00 | 120,000.00 | 0.00 |

La caja consolidada es 136,959.20. Las dos cuentas están sobre su mínimo.

**Señales que dejó el cómputo:** un firmante sin autoridad y un vencimiento cercano. Las revisan `/payment-check` y `/debt-watch`. El reporte de caja no las detalla.

**Un error mío, ya corregido:** una de mis llamadas corrió desde `20-bancos` y escribió ahí una carpeta `.criterio` con la aceptación de términos. La borré y volví a registrar la aceptación en la ruta correcta. Después de eso, el reporte salió sin nada pendiente de procesar.

**Archivos que quedaron:**
- Configuración: `.criterio/tesoreria/20710000019-banco-ribera/config.json`
- Reporte: `estado-finanzas/20710000019-banco-ribera/tesoreria/2026-09/reporte-cash-position.md`
- Salida de la corrida: `estado-finanzas/20710000019-banco-ribera/corridas/salida-treasury-setup.md`, registrada como `2026-10-06-treasury-setup-1`

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.