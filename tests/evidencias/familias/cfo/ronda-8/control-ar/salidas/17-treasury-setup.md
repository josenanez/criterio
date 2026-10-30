# /criterio-treasury:treasury-setup finanzas/30702173554-comercial-control-del-plata

## Listo — Comercial Control del Plata · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-7101 y pacifico-7102). También hay programa de pagos, política de tesorería, registro de deuda y covenants.
**Términos:** José Francisco Ñáñez los aceptó para la versión 1.0.0 (términos 1.3) el 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-1.0.0-2026-10-06.md`, con su versión en PDF.

**Posición de caja al 2026-09-30**

| Cuenta | Saldo | Mínimo |
|---|---|---|
| andino-7101 | 16.168.800,00 | 6.884.400,00 |
| pacifico-7102 | 36.000.000,00 | 16.800.000,00 |

- **Consolidada:** 52.168.800,00 ARS.
- **Frente al mínimo:** las dos cuentas están por encima.
- **Frente a la proyección:** la desviación es 0,00 % en ambas.
- **Señales:** `compute` no encontró ninguna. No miré el resto de los comandos de tesorería.
- **Reporte completo:** `estado-finanzas/30702173554-comercial-control-del-plata/tesoreria/2026-09/reporte-cash-position.md`

**Lo que decidí sin preguntar:**
- **Entidad, moneda y periodo:** tomé el nombre, el NIT, la moneda funcional (ARS) y el periodo (2026-09) de la configuración de Clara.
- **Otras monedas:** no declaré cuentas en otra moneda.
- **Umbrales:** usé los de `config.example.json`: desviación 10 %, vencimiento 30 días y margen de covenant 10 %.
- **Estado:** `estado-finanzas/30702173554-comercial-control-del-plata`.
- **Marca de raíz:** no escribí `_CRITERIO_FINANZAS.txt` en la carpeta de documentos porque nadie lo autorizó.

**Para revisar:** la salida de `compute` no trae documentos citados y el reporte dice «Sin documentos citados». Por eso conviene verificar el saldo de cada cuenta contra su extracto.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La configuración quedó en `.criterio/tesoreria/30702173554/config.json`. La corrida quedó registrada como `2026-10-06-treasury-setup-1` y lo mostrado está en `corridas/salida-treasury-setup.md`.