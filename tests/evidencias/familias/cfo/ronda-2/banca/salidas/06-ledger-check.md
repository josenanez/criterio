# /criterio-finance:ledger-check 

El balance de comprobación de Banco Andino de 2026-09 no cuadra. Los débitos suman 253.437.700,00 y los créditos 253.432.700,00, una diferencia de 5.000,00. La explica una sola cuenta, la 5305.

- **Mayor contra balance:** el mayor suma débitos 0,00 y créditos 0,00 para la cuenta 5305, pero el balance le asigna 5.000,00 en débitos y 0,00 en créditos.
- **Saldo inicial más movimientos:** en esa misma cuenta no dan el saldo final de 5.000,00. El motor la marca en la fila 15 de `balance-comprobacion.csv`.
- **Lo que quedó sin procesar:** nada, todo lo que llegó se procesó.

Es una señal para que alguien la revise; Clara no registra asientos ni los corrige.

Los términos (versión 1.2) ya estaban vigentes y aceptados en esta entidad, así que no hubo que registrar la aceptación otra vez. El periodo es 2026-09, el de la configuración y el último con contabilidad.

El reporte lo escribió el motor en `estado-finanzas/900123456-banco-andino/cierre/2026-09/reporte-ledger-check.md`. Lo mostrado quedó en `estado-finanzas/900123456-banco-andino/corridas/salida-ledger-check.md`. La corrida quedó registrada como `2026-10-06-ledger-check-1`.

Dos datos del reporte siguen por confirmar: el marco contable (grupo 1, valor por defecto) y el festivo 2026-10-12.