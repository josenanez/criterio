# /criterio-treasury:treasury-setup finanzas/08010006129040-almacenes-del-valle-de-sula

## Listo — Almacenes del Valle de Sula · tesorería 2026-09

**Lo que miré:**
- 2 cuentas con extracto (andino-11301 y pacifico-11302).
- Programa de pagos: sí.
- Política: sí.
- Registro de deuda: sí.

**Términos:** aceptados para la versión 1.1.0 por José Francisco Ñáñez, con fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-1.1.0-2026-10-06.md`.

**Respuestas que tomé yo, porque nadie podía contestar:**
- Carpeta raíz: la del argumento.
- Moneda funcional: HNL, la que dice la configuración de Clara.
- Cuentas en otra moneda: ninguna.
- Umbrales: los de `config.example.json`, que son 10 % de desviación, 30 días y 10 % de margen.
- Estado: `estado-finanzas/08010006129040-almacenes-del-valle-de-sula`.

### La posición de caja (periodo 2026-09, corte 2026-09-30)

**Caja consolidada:** 1,553,400.00 HNL

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-11301 | HNL | 353,400.00 | 464,080.00 | 353,400.00 | 0.00 |
| pacifico-11302 | HNL | 1,200,000.00 | 560,000.00 | 1,200,000.00 | 0.00 |

**Lo que hay que atender:** `andino-11301` queda 110,680.00 HNL por debajo del mínimo de la política. La cita es `2026-09/20-bancos/andino-11301/extracto.pdf` fila 17 y `00-referencia/politica-tesoreria.csv` fila 2.

**Otras señales del cálculo:** el motor registró tres en total. Las otras dos son un pago sin aprobación (`payment_without_approval`) y un vencimiento cercano (`maturity_near`). Este reporte no las detalla. Salen en `payment-check` y `debt-watch`.

Todo lo que llegó se procesó. Áurea no mueve dinero ni entra a ningún portal bancario.

**Dónde quedó:**
- Configuración: `.criterio/tesoreria/08010006129040/config.json`.
- Reporte: `estado-finanzas/08010006129040-almacenes-del-valle-de-sula/tesoreria/2026-09/reporte-cash-position.md`.
- Salida de esta corrida: `estado-finanzas/08010006129040-almacenes-del-valle-de-sula/corridas/salida-treasury-setup.md`. La corrida quedó registrada con el id `2026-10-06-treasury-setup-1`.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.