# /criterio-treasury:treasury-setup finanzas/155831003-2-2013-comercial-control-del-istmo

## Listo — Comercial Control del Istmo · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-8301 y pacifico-8302). Hay programa de pagos, flujo proyectado, política de tesorería, matriz de firmas, covenants y registro de deuda.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.0.0 (términos 1.3), con fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-1.0.0-2026-10-06.md`.

**Respuestas por defecto que usé, porque nadie contestaba:**
- **Raíz:** la del argumento.
- **Entidad, moneda y periodo:** los de la configuración de Clara (USD, 2026-09).
- **Cuentas en otra moneda:** ninguna.
- **Umbrales:** los de `config.example.json` (desviación 10 %, 30 días, margen de covenant 10 %).
- **Estado:** `estado-finanzas/155831003-2-2013-comercial-control-del-istmo`.
- **Exposición cambiaria:** la política no trae límite.

# La posición de caja · periodo 2026-09 (corte 2026-09-30)

**Caja consolidada:** 41,595.60

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-8301 | USD | 5,595.60 | 1,597.80 | 5,595.60 | 0.00 |
| pacifico-8302 | USD | 36,000.00 | 16,800.00 | 36,000.00 | 0.00 |

No hay nada abierto en lo que procesa este comando, y todo lo que llegó se procesó. Las dos cuentas están sobre su mínimo.

**Dos cosas para revisar:**
- **Proyectado igual al saldo:** sale idéntico al saldo en las dos cuentas (desviación 0.00) y el reporte no cita fuentes. Conviene confirmar que el motor leyó `60-tesoreria/flujo-proyectado.xlsx`.
- **Aceptación duplicada:** llamé a `aceptar` una primera vez sin `--today`, y quedó un comprobante con fecha 2026-10-30. Lo repetí con `--today 2026-10-06` y quedó el correcto. El de 2026-10-30 sigue en `.criterio/terminos/`, y no lo borré.

**Dónde quedó todo:**
- **Configuración:** `.criterio/tesoreria/155831003-2-2013-comercial-control-del-istmo/config.json`. La carpeta lleva el nombre completo de la entidad, como la de Clara, y no solo el RUC.
- **Reporte:** `estado-finanzas/155831003-2-2013-comercial-control-del-istmo/tesoreria/2026-09/reporte-cash-position.md`.
- **Corrida registrada:** `2026-10-06-treasury-setup-1`, con 0 hallazgos. Lo que te mostré está en `estado-finanzas/155831003-2-2013-comercial-control-del-istmo/corridas/salida-treasury-setup.md`.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.