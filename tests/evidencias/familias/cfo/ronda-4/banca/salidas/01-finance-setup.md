# /criterio-finance:finance-setup finanzas/900123456-banco-andino

## Listo — Banco Andino

**Lo que miré:** 63 archivos, nueve periodos (2026-01 a 2026-09) y presupuesto-2026. Ninguno está fuera de la estructura.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-0.10.0-2026-10-06.md` y `.pdf`.

Nadie podía contestar, así que tomé las respuestas sugeridas:
- **Marco contable:** grupo 1. Ningún documento lo dice, queda por confirmar.
- **Cuentas de las facturas:** 41, 14/51/52/61 y 2408.
- **Cuentas que se concilian:** 1305 y 2205.
- **Bancos:** andino-1101 y pacifico-1102.
- **Aprueba el cierre:** Sofía León.

No marqué la carpeta con `_CRITERIO_FINANZAS.txt`, porque no hubo quién autorizara escribir en los documentos.

El motor registró 8 señales en total. Son el cuadre del mayor y del balance, bancos sin conciliar, una factura con diferencia de monto y una partida antigua. El reporte de abajo detalla solo la que afecta al checklist.

# Estado del cierre · Banco Andino · periodo 2026-09

**Estado declarado:** en curso (correo de Sofía León, 2026-10-05). **Avance con evidencia:** 42,31 %. **Avance declarado:** 53,85 %.

El checklist no está aprobado. El estado se calcula, pero una persona tiene que aprobarlo antes de darlo por bueno.

**Lo que hay que atender:** C-02 (Conciliar cada cuenta bancaria, Andrés Paz) figura cumplida y no hay soporte en `2026-09/40-soportes/` que empiece por C-02.

| Id | Tarea | Responsable | Vence | Estado |
|---|---|---|---|---|
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | cumplida sin evidencia |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | bloqueada por C-02 |
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 |
| C-06 | Preparar los papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo |
| C-01, C-03, C-04, C-05 | Los cuatro con soporte en `40-soportes/` | | | cumplidas con evidencia |

**Ruta crítica del cierre:** C-02 → C-07 → C-08 → C-09. Todo lo que llegó se procesó.

**Qué falta para que sea mejor:** la aprobación del checklist por una persona, el soporte firmado de C-02 y la confirmación del marco contable.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

La corrida quedó registrada, con id `2026-10-06-finance-setup-1`. La salida completa está en `estado-finanzas/900123456-banco-andino/corridas/salida-finance-setup.md` y el reporte en `estado-finanzas/900123456-banco-andino/cierre/2026-09/reporte-close-status.md`.