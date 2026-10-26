# /criterio-treasury:treasury-setup finanzas/20790000014-comercial-control-sur

## Listo — Comercial Control Sur · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-7901 y pacifico-7902). También hay programa de pagos, política de tesorería y registro de deuda.
**Términos:** quedan aceptados a nombre de José Francisco Ñáñez para la versión 0.9.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.9.0-2026-10-06.md`.

Nadie podía responder en esta sesión, así que tomé estas respuestas por defecto:
- **Carpeta raíz:** la del argumento.
- **Otras monedas:** ninguna, las dos cuentas están en PEN.
- **Umbrales:** los de `config.example.json`: desviación 10 %, vencimiento 30 días, margen del covenant 10 %.
- **Estado:** `estado-finanzas/20790000014-comercial-control-sur`.

### La posición de caja (periodo 2026-09, corte 2026-09-30)

**Caja consolidada:** 117,516.00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-7901 | PEN | 27,516.00 | 10,758.00 | 27,516.00 | 0.00 |
| pacifico-7902 | PEN | 90,000.00 | 42,000.00 | 90,000.00 | 0.00 |

- **Por atender:** nada abierto.
- **Sin procesar:** nada.
- **Fuentes:** el reporte no citó documentos.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

### Dónde quedó cada cosa
- **Configuración:** `.criterio/tesoreria/20790000014/config.json`.
- **Reporte del motor:** `estado-finanzas/20790000014-comercial-control-sur/tesoreria/2026-09/reporte-cash-position.md`.
- **Salida de esta corrida:** `estado-finanzas/20790000014-comercial-control-sur/corridas/salida-treasury-setup.md`. Quedó registrada como `2026-10-06-treasury-setup-1`, con 0 hallazgos.

No marqué la raíz con `marcar-raiz`: nadie lo autorizó.