# /criterio-finance:bank-reconcile 

Concilié las dos cuentas bancarias de Banco Andino (NIT 900123456) para 2026-09. La diferencia sin explicar es 0,00 en ambas, y todo lo que llegó se procesó. Los términos (versión 1.2) ya estaban vigentes, así que no hizo falta registrarlos otra vez. Dejé la corrida registrada con el id `2026-10-06-bank-reconcile-1`.

**andino-1101** tiene dos partidas abiertas:

| Partida | Valor | Días abierta |
|---|---|---|
| Cheque pendiente de cobro CH-0450, del 2026-07-20 | -3.000.000,00 | 72 (tramo 61-90) |
| Nota débito sin registrar, del 2026-09-30, sin referencia | -400.000,00 | 0 |

- **Saldos:** el banco dice 13.273.400,00 y los libros 10.673.400,00.
- **Cheque CH-0450:** el motor lo marcó además como partida vencida por antigüedad, porque lleva más días de los configurados.

**pacifico-1102** no tiene partidas abiertas: banco y libros marcan 30.000.000,00.

El reporte completo está en `estado-finanzas/900123456-banco-andino/cierre/2026-09/reporte-bank-reconcile.md`. Lo que te mostré, tal cual, lo guardé en `estado-finanzas/900123456-banco-andino/corridas/salida-bank-reconcile.md`.