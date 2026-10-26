# /criterio-treasury:treasury-setup finanzas/20710000019-banco-ribera

Áurea quedó instalada para Banco Ribera (RUC 20710000019) y calculó la primera posición de caja de 2026-09. La caja consolidada es 120,000.00, pero la exposición en PEN no se pudo calcular.

**Cuentas**
| Cuenta | Moneda | Saldo | Mínimo |
|---|---|---|---|
| `andino-7101` | PEN | 16,959.20 | 4,479.60 |
| `pacifico-7102` | USD | 120,000.00 | 56,000.00 |

La proyección coincide con el saldo en ambas cuentas, así que la desviación es 0.00 %.

**Lo que quedó sin calcular:** la política solo trae la tasa de USD, no la de PEN, así que no se calculó la exposición en PEN.

**Supuestos míos**
- Puse la moneda funcional en USD porque la política trae `tasa;USD;1` y el límite de exposición en USD. Es una suposición mía y conviene confirmarla.
- Los umbrales son los de `config.example.json`: desviación 10 %, vencimiento 30 días, margen del covenant 10 %.
- No marqué la carpeta con `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó. Hacerlo es opcional.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06.md` y en el `.pdf` del mismo nombre.

**Señales para otros comandos:** el cálculo dejó una de firmante sin facultad, para `/criterio-treasury:payment-check`, y una de vencimiento cercano, para `/criterio-treasury:debt-watch`.

**Archivos**
- Configuración: `.criterio/tesoreria/20710000019-banco-ribera/config.json`
- Reporte: `estado-finanzas/20710000019-banco-ribera/tesoreria/2026-09/reporte-cash-position.md`
- Salida registrada: `estado-finanzas/20710000019-banco-ribera/corridas/salida-treasury-setup.md`

La corrida quedó registrada con id `2026-10-06-treasury-setup-1`; no medí los minutos hasta el primer resultado.