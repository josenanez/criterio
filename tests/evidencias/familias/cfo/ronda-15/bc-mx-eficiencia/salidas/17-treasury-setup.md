# /criterio-treasury:treasury-setup finanzas/DNO190402B43-distribuidora-del-noroeste

Áurea quedó lista para Distribuidora del Noroeste. Las dos cuentas bancarias tienen la caja por encima de su mínimo y coinciden con la proyección; no hay nada abierto.

Las respuestas a las preguntas salieron de los documentos y de la configuración de Clara, y nadie tuvo que contestar nada. No escribí la marca de la raíz porque nadie la autorizó. Hay un detalle en el reporte: la sección de fuentes salió vacía («Sin documentos citados») aunque las cifras salen de los extractos. Así lo escribió el motor y lo muestro tal cual.

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

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana. **No quedó tarea programada:** necesita un sí explícito y esta prueba no lo trae. Para correrlo a mano: `/criterio-treasury:treasury-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

Archivos:
- Configuración: `.criterio/tesoreria/DNO190402B43-distribuidora-del-noroeste/config.json`
- Reporte: `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/tesoreria/2026-09/reporte-cash-position.md`
- Corrida registrada como `2026-10-06-treasury-setup-1`