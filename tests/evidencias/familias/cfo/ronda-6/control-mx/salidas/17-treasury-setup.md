# /criterio-treasury:treasury-setup finanzas/CCM120615R59-comercial-control-centro

## Listo — Comercial Control Centro · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-1901, pacifico-1902) · programa de pagos sí · política sí · registro de deuda sí
**Términos:** aceptados por José Francisco Ñáñez el 2026-10-06 para la versión 0.11.0 (términos 1.2). El comprobante en Markdown y PDF está en `.criterio/terminos/`.

Nadie respondió preguntas en esta prueba, así que tomé las respuestas de los documentos:
- **Entidad y moneda:** Comercial Control Centro (CCM120615R59), MXN, copiadas de la configuración de Clara.
- **Cuentas en otra moneda:** ninguna, porque los dos extractos traen la columna de moneda en MXN.
- **Umbrales:** los de `config.example.json` (desviación 10 %, vencimiento 30 días, margen del covenant 10 %). Son configuración, no norma.
- **Estado:** `estado-finanzas/CCM120615R59-comercial-control-centro`, el mismo de Clara y Tomás.

La configuración quedó en `.criterio/tesoreria/CCM120615R59/config.json`.

# La posición de caja · Comercial Control Centro · periodo 2026-09

**Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.11.0 · **Aprueba:** Contralor

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Caja consolidada:** 455,568.00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-1901 | MXN | 95,568.00 | 35,784.00 | 95,568.00 | 0.00 |
| pacifico-1902 | MXN | 360,000.00 | 168,000.00 | 360,000.00 | 0.00 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

Sin documentos citados.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La salida quedó en `estado-finanzas/CCM120615R59-comercial-control-centro/corridas/salida-treasury-setup.md`. La corrida quedó registrada como `2026-10-06-treasury-setup-1`, con 0 hallazgos.

Una observación mía, que no sale del motor: el reporte no cita ningún documento y no trae señales. La proyección coincide exactamente con el saldo en las dos cuentas (desviación 0.00). Conviene confirmar que `flujo-proyectado.csv` se leyó. No lo verifiqué.