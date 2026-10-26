# /criterio-treasury:treasury-setup finanzas/20790000014-comercial-control-sur

## Listo — Comercial Control Sur · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-7901 y pacifico-7902). Hay programa de pagos, política de tesorería y registro de deuda.
**Términos:** aceptados para la versión 0.10.0 (términos 1.2) por José Francisco Ñáñez, 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06.md`.

Tomé las respuestas de los documentos y de la configuración de Clara: misma entidad, moneda funcional PEN, mismo estado `estado-finanzas/20790000014-comercial-control-sur`. Usé los umbrales de `config.example.json` (10 % de desviación, 30 días de vencimiento, 10 % de margen del covenant). Son configuración, no norma. No declaré cuentas en otra moneda, y el motor leyó ambas en PEN. La configuración quedó en `.criterio/tesoreria/20790000014/config.json`.

# La posición de caja · Comercial Control Sur · periodo 2026-09

**Entidad:** Comercial Control Sur (20790000014) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `cash-position`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Caja consolidada:** 117,516.00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-7901 | PEN | 27,516.00 | 10,758.00 | 27,516.00 | 0.00 |
| pacifico-7902 | PEN | 90,000.00 | 42,000.00 | 90,000.00 | 0.00 |

Áurea no mueve dinero ni entra a un portal bancario: procesa las exportaciones.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La salida completa quedó en `estado-finanzas/20790000014-comercial-control-sur/corridas/salida-treasury-setup.md`, y la corrida se registró como `2026-10-06-treasury-setup-1`.

El reporte del motor sale con "Sin documentos citados" en Fuentes. No lo completé, porque las fuentes las cita el motor.