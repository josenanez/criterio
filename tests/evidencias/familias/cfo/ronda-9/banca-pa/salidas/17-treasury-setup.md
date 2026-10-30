# /criterio-treasury:treasury-setup finanzas/155731001-2-2016-banco-istmeno

## Listo — Banco Istmeño · tesorería 2026-09

Áurea quedó instalada sobre Banco Istmeño y calculó la primera posición de caja del periodo 2026-09.

**Lo que miré:**
- Hay 2 cuentas con extracto: andino-7301 y pacifico-7302.
- Están el programa de pagos, la política de tesorería y el registro de deuda.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.0.0. Los comprobantes (`.md` y `.pdf`) están en `.criterio/terminos/aceptacion-criterio-treasury-1.0.0-2026-10-06.*`.

**Respuestas que tomé yo, porque nadie contestaba:**
- **Entidad, moneda y estado:** la moneda funcional es USD, y la entidad y la ruta del estado salen de la configuración de Clara.
- **Otras monedas:** no declaré cuentas en otra moneda.
- **Umbrales:** usé los de `config.example.json`: 10 % de desviación, 30 días de vencimiento y 10 % de margen del covenant.
- **Marca de la raíz:** no la creé, porque nadie la autorizó.

### La posición de caja

La caja consolidada es **61,845.40 USD**.

| Cuenta | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|
| andino-7301 | 1,845.40 | 4,214.48 | 1,845.40 | 0.00 |
| pacifico-7302 | 60,000.00 | 28,000.00 | 60,000.00 | 0.00 |

**Lo que hay que atender:** andino-7301 queda 2,369.08 USD por debajo del mínimo que fija la política. Las citas son `2026-09/20-bancos/andino-7301/extracto.pdf` fila 17 y `00-referencia/politica-tesoreria.csv` fila 2.

Todo lo que llegó se procesó y el motor no hizo ninguna pregunta.

El cálculo detectó además otras dos señales que el reporte de caja no detalla: un firmante sin autoridad (`signatory_without_authority`) y un covenant en riesgo (`covenant_at_risk`). Quedan para `/payment-check` y `/debt-watch`.

**Archivos:**
- Configuración: `.criterio/tesoreria/155731001-2-2016/config.json`
- Reporte: `estado-finanzas/155731001-2-2016-banco-istmeno/tesoreria/2026-09/reporte-cash-position.md`
- Salida de esta corrida: `estado-finanzas/155731001-2-2016-banco-istmeno/corridas/salida-treasury-setup.md`
- Corrida registrada: `2026-10-06-treasury-setup-1`

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.