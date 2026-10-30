# /criterio-treasury:treasury-setup finanzas/08010007330150-comercial-control-de-honduras

Áurea quedó instalada y calculó la primera posición de caja de 2026-09: la caja consolidada es 1,430,925.00 HNL y no hay señales abiertas.

**Lo que encontré en la carpeta:**
- Hay 2 cuentas con extracto (`andino-12701` y `pacifico-12702`).
- Están el programa de pagos, la política de tesorería y el registro de deuda.

**Posición de caja (30 de septiembre de 2026):**

| Cuenta | Saldo | Mínimo | Proyectado |
|---|---|---|---|
| `andino-12701` | 530,925.00 | 235,462.50 | 530,925.00 |
| `pacifico-12702` | 900,000.00 | 420,000.00 | 900,000.00 |

Las dos cuentas están por encima de su mínimo y sin desviación contra la proyección.

**Respuestas que tomé por defecto, porque no había nadie a quien preguntar:**
- **Moneda funcional:** HNL, la misma que usa Clara.
- **Cuentas en otra moneda:** ninguna.
- **Umbrales:** los de `config.example.json` (desviación 10 %, vencimiento 30 días, margen de covenant 10 %).
- **Estado:** `estado-finanzas/08010007330150-comercial-control-de-honduras`.

**Términos:** los mostré tal cual y los registré a nombre de José Francisco Ñáñez, con fecha 2026-10-06, versión 1.1.0. Los comprobantes quedaron en `.criterio/terminos/`.

**Archivos:**
- **Configuración:** `.criterio/tesoreria/08010007330150/config.json`
- **Reporte:** `estado-finanzas/08010007330150-comercial-control-de-honduras/tesoreria/2026-09/reporte-cash-position.md`
- **Salida de la corrida:** `estado-finanzas/08010007330150-comercial-control-de-honduras/corridas/salida-treasury-setup.md`

Con la fecha de prueba (2026-10-06), `compute` y `reporte` no marcaron ninguna señal. El `inventario` dice que la carpeta ya trae un programa de pagos con 4 pagos, y el comando de pagos todavía no lo ha revisado. Tampoco se ha calculado aún la deuda ni los covenants.