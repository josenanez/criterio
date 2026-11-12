# /criterio-treasury:treasury-setup finanzas/DNO190402B43-distribuidora-del-noroeste

Las dos cuentas tienen más caja que su mínimo y cuadran exactamente con lo proyectado. La política no fija un límite de exposición en otra moneda. Por ahora no hace falta, porque ninguna cuenta está en otra moneda, pero sí faltaría si se abre una.

## Listo — Distribuidora del Noroeste · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto · programa de pagos sí · política sí · registro de deuda sí
**Términos:** aceptados para la versión 1.5.4 · comprobante en `.criterio/terminos/`

# La posición de caja · Distribuidora del Noroeste · periodo 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `cash-position`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Caja consolidada:** 704,232.00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-4301 | MXN | 164,232.00 | 64,116.00 | 164,232.00 | 0.00 |
| pacifico-4302 | MXN | 540,000.00 | 252,000.00 | 540,000.00 | 0.00 |

Áurea no mueve dinero ni entra a un portal bancario: procesa las exportaciones.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana. No dejé una tarea programada porque en esta prueba nadie la autorizó; se corre a mano con `/criterio-treasury:treasury-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

---

Hay dos detalles del reporte que conviene revisar:
- **Fuentes vacías:** el reporte dice «Sin documentos citados», aunque los saldos salen de los extractos y los mínimos de `politica-tesoreria.csv`.
- **Preguntas en cero:** dice «Ninguna», pero respondí 5 preguntas con lo que traían los documentos.

La configuración quedó en `.criterio/tesoreria/DNO190402B43/config.json` y la corrida quedó registrada como `2026-10-06-treasury-setup-1`.