# /criterio-finance:finance-setup finanzas/155731001-2-2016-banco-istmeno

La instalación quedó lista y registrada. Lo que sigue es lo que le mostraría a la persona.

## Listo — Banco Istmeño

**Lo que miré:** 65 archivos · periodos 2026-01 a 2026-09 y presupuesto-2026 · 0 fuera de la estructura
**Términos:** aceptados por José Francisco Ñáñez el 2026-10-06 para la versión 1.0.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-1.0.0-2026-10-06.md` y `.pdf`.

# Estado del cierre · Banco Istmeño · periodo 2026-09

**Estado declarado:** en curso. Lo dice Sofía León en `2026-09/40-soportes/correo-estado-del-cierre.md`, con fecha 2026-10-05.
**Avance con evidencia:** 42.31 %. **Avance declarado:** 53.85 %, ponderados por criticidad.
El checklist no está aprobado. El estado se calcula igual, pero una persona tiene que aprobarlo antes de darlo por bueno.

**Lo que hay que atender:** C-02, "Conciliar cada cuenta bancaria", de Andrés Paz, figura cumplida. No hay soporte que empiece por C-02 en `2026-09/40-soportes/`.

| Id | Tarea | Estado |
|---|---|---|
| C-02 | Conciliar cada cuenta bancaria | cumplida sin evidencia |
| C-07 | Cuadrar el balance de comprobación | bloqueada por C-02 |
| C-08 | Revisar el cierre y sus soportes | bloqueada por C-07 |
| C-09 | Aprobar el cierre del periodo | bloqueada por C-08 |
| C-06 | Papeles de trabajo de impuestos | en plazo |
| C-01, C-03, C-04, C-05 | — | cumplidas con evidencia |

**Ruta crítica:** C-02 → C-07 → C-08 → C-09.

El motor encontró 9 señales en total: 2 de mayor contra balance, 1 de balance sin cuadrar, 1 tarea cumplida sin evidencia, 1 factura sin registrar, 1 diferencia de monto en una factura, 2 bancos sin conciliar y 1 partida envejecida. El reporte detalla solo la primera. Las otras 8 están en `estado-finanzas/155731001-2-2016-banco-istmeno/cierre/2026-09/resultados.json`.

**Qué propuse yo, porque nadie respondió:**
- Marco contable NIIF, que no tiene respaldo en ningún documento.
- Aprobador del cierre: Sofía León, porque aparece en C-08 y C-09.
- Checklist marcado como no aprobado.
- Festivos vacíos.
- Cuentas de facturas: ventas 4135, compras 5135/5145/5195 e ITBMS 2408, las que sostienen las facturas.
- Cuentas a conciliar 1305 y 2205, y bancos andino-7301 y pacifico-7302.

**Qué falta para mejorar el resultado:**
- Soporte firmado de C-02.
- Aprobación del checklist.
- Festivos del calendario.
- Confirmar el marco contable.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.

La salida completa quedó en `estado-finanzas/155731001-2-2016-banco-istmeno/corridas/salida-finance-setup.md`. La corrida quedó registrada con el id `2026-10-06-finance-setup-1`. No ofrecí marcar la carpeta con `_CRITERIO_FINANZAS.txt`, porque nadie podía responder.