# /criterio-finance:finance-setup finanzas/900123456-banco-andino

## Listo: Banco Andino

**Lo que miré:** 57 archivos, nueve periodos (2026-01 a 2026-09) y el presupuesto 2026. Ninguno está fuera de la estructura.
**Términos:** aceptados por José Francisco Ñáñez para la versión 0.7.0 de la familia (términos 1.2, 2026-10-06). El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-0.7.0-2026-10-06.md` y `.pdf`. La nota legal está en https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.7.0.

**Lo que quedó escrito:**
- La configuración está en `.criterio/finanzas/900123456/config.json`.
- El estado está en `estado-finanzas/900123456-banco-andino`.
- No dejé `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque nadie lo autorizó.

Al calcular el periodo 2026-09, el motor encontró 8 señales. El estado del cierre muestra solo la que toca a una tarea del checklist. Las otras 7 son:
- el cuadre del balance y del mayor;
- los bancos sin conciliar;
- una factura con diferencia de valor;
- una partida antigua.

Las detallan `ledger-check`, `bank-reconcile`, `einvoice-check` y `account-reconcile`.

# Estado del cierre · Banco Andino · periodo 2026-09

**Estado declarado:** en curso, según el correo de Sofía León del 2026-10-05.
**Avance con evidencia:** 42,31 %.
**Avance declarado:** 53,85 %.
Los dos porcentajes están ponderados por criticidad.

**Lo que hay que atender:** C-02, «Conciliar cada cuenta bancaria» (Andrés Paz), figura cumplida y no hay soporte en `2026-09/40-soportes/` que empiece por C-02.

| Id | Tarea | Responsable | Vence | Estado |
|---|---|---|---|---|
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | cumplida sin evidencia |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | bloqueada por C-02 |
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 |
| C-06 | Preparar los papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo |
| C-01, C-03, C-04, C-05 | Cerradas con soporte en `40-soportes/` | | | cumplida con evidencia |

**Ruta crítica del cierre:** C-02 → C-07 → C-08 → C-09.

**Lo que no se pudo procesar:** nada. Todo lo que llegó se procesó.

El checklist no está aprobado. El estado se calcula igual, pero una persona tiene que aprobarlo antes de darlo por bueno.

**Qué falta para que esto sea mejor:**
- El soporte de C-02, la conciliación bancaria firmada por Andrés Paz. Es lo que hoy bloquea la ruta crítica.
- El auxiliar de inventarios (1435), que está en el balance y no tiene auxiliar.
- Que alguien apruebe el checklist.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

El reporte completo está en `estado-finanzas/900123456-banco-andino/cierre/2026-09/reporte-close-status.md`. Esta salida quedó en `estado-finanzas/900123456-banco-andino/corridas/salida-finance-setup.md` y la corrida está registrada.

Las 10 preguntas las respondí desde los documentos, sin que nadie las contestara. Los minutos hasta el primer resultado no se midieron.