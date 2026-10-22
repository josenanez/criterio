# /criterio-finance:account-reconcile 

Corrí la conciliación de cuentas de Cooperativa Sierra Alta para 2026-09. Hay una diferencia en la cuenta 1305 y una conciliación bancaria desactualizada. Los términos (versión 1.2) ya estaban vigentes, así que no hizo falta registrar aceptación. La corrida quedó registrada como `2026-10-06-account-reconcile-1`.

**Lo que hay que atender**
1. **Cuenta 1305 (Clientes):** el mayor dice 14,612.50 y el auxiliar suma 12,362.50. La diferencia es de 2,250.00 (balance de comprobación, fila 4, contra `1305-clientes.csv`).
2. **Cuenta bancaria pacifico-2302:** falta el extracto del periodo, por lo que su conciliación está desactualizada.

**El resultado**

| Cuenta | Nombre | Saldo según mayor | Saldo según auxiliar | Diferencia |
|---|---|---|---|---|
| 1305 | Clientes | 14,612.50 | 12,362.50 | 2,250.00 |
| 2205 | Proveedores | -22,310.00 | -22,310.00 | 0.00 |

Todo el auxiliar de 1305 (12,362.50) y todo el de 2205 (-22,310.00) están en el tramo de 0 a 30 días.

Todo lo que llegó se procesó. Las preguntas de configuración que el reporte registra las respondió con lo que dicen los documentos. Tres quedan por confirmar: el marco contable (NIIF para PYMES, que ningún documento dice), la aprobación del checklist y los festivos, que ningún documento trae.

El reporte completo está en `estado-finanzas/1790012345001-cooperativa-sierra-alta/cierre/2026-09/reporte-account-reconcile.md`. Lo que te mostré arriba lo guardé tal cual en `corridas/salida-account-reconcile.md`, en esa misma carpeta de estado.