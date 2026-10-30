# /criterio-finance:finance-setup finanzas/87145200-almacenes-del-altiplano

## Listo — Almacenes del Altiplano

**Lo que miré:** 65 archivos. Hay nueve periodos, de 2026-01 a 2026-09, y el presupuesto 2026. Ninguno está fuera de la estructura.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.0.0 (términos 1.3). Los comprobantes en Markdown y PDF están en `.criterio/terminos/aceptacion-criterio-finance-1.0.0-2026-10-30.md` y `.pdf`.

**Cómo quedó:**
- **Configuración:** `.criterio/finanzas/87145200-almacenes-del-altiplano/config.json`. El motor la validó sin problemas.
- **Estado:** `estado-finanzas/87145200-almacenes-del-altiplano`.
- **País y moneda:** Guatemala y GTQ. Los deduje de las facturas FEL de la SAT.
- **Marco contable:** NIIF. Es una propuesta mía, porque ningún documento lo dice.
- **Checklist:** usé el de la organización y lo tomé como aprobado.
- **Quién aprueba el cierre:** Sofía León, responsable de C-09. No encontré festivos y no puse ninguno.
- **Archivo `_CRITERIO_FINANZAS.txt`:** no lo dejé en la carpeta de documentos, porque nadie lo autorizó.

**La aceptación quedó con fecha 2026-10-30, no 2026-10-06.** `aceptar` no recibe `--today` y toma la fecha del sistema. Lo anoté en la ficha y en la corrida. Si necesitas el comprobante con la fecha de la prueba, hay que cambiar el motor.

### Estado del cierre · periodo 2026-09

El estado declarado es «cerrado». Sofía León lo escribió en un correo del 2026-10-05, y el motor lo contradice. El avance con evidencia es 42.31 % y el declarado es 53.85 %, ponderados por criticidad.

**Lo que hay que atender**
1. **C-02, conciliar cada cuenta bancaria (Andrés Paz):** figura cumplida y no hay soporte firmado en `2026-09/40-soportes/`.
2. **Cierre declarado como cerrado:** hay 5 señales abiertas que ese estado no explica.

El motor cuenta seis señales en total. Además de las dos de arriba hay cuatro: una factura electrónica no registrada, un banco sin conciliar, una diferencia de monto en una factura electrónica y una partida conciliatoria antigua. Su detalle sale en `bank-reconcile` y `einvoice-check`, no en este reporte.

| Id | Tarea | Responsable | Vence | Estado |
|---|---|---|---|---|
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | cumplida sin evidencia |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | bloqueada por C-02 |
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 |
| C-06 | Preparar los papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo |
| C-01 | Cerrar los módulos de ventas, compras e inventarios | Lucía Mora | 2026-10-01 | cumplida con evidencia |
| C-03 | Cruzar las facturas emitidas con las ventas | Lucía Mora | 2026-10-02 | cumplida con evidencia |
| C-04 | Conciliar cartera contra su auxiliar | Marta Ríos | 2026-10-05 | cumplida con evidencia |
| C-05 | Registrar provisiones y causaciones | Jorge Vela | 2026-10-05 | cumplida con evidencia |

**Ruta crítica:** C-02 → C-07 → C-08 → C-09. Todo lo que llegó se procesó.

**Qué falta para mejorar esto:** el soporte firmado de C-02.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.

La corrida quedó registrada como `2026-10-30-finance-setup-1`, con la salida completa en `estado-finanzas/87145200-almacenes-del-altiplano/corridas/salida-finance-setup.md`. Las 9 respuestas a las preguntas las tomé yo de los documentos, y están en la ficha.