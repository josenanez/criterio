# /criterio-finance:finance-setup finanzas/0990054321001-minera-condor

## Listo — Minera Cóndor

**Lo que miré:** 57 archivos · periodos 2026-01 a 2026-09 y presupuesto-2026 · 0 fuera de la estructura.
**Términos:** aceptados para la versión 0.8.0 (términos 1.2) por José Francisco Ñáñez, 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-0.8.0-2026-10-06.md` y `.pdf`.

Además de las dos señales de abajo, el cálculo levantó otras cinco que este reporte no detalla:
- 2 de bancos sin conciliar.
- 1 factura electrónica sin registro.
- 1 requerimiento del auditor sin responder.
- 1 partida conciliatoria antigua.

Las detallan `bank-reconcile`, `einvoice-check` y `audit-pack`.

# Estado del cierre · Minera Cóndor · periodo 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Tarea cumplida sin documento que la sostenga (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: no hay soporte en `2026-09/40-soportes/` que empiece por C-02 | Andrés Paz | — | `00-referencia/checklist-cierre.csv` fila 3 |
| 2 | Tarea vencida sin evidencia (`close_task_overdue`) | C-05 · Registrar provisiones y causaciones: venció el 2026-10-05 | Jorge Vela | 1 | `00-referencia/checklist-cierre.csv` fila 6 |

## El resultado

**Estado declarado:** en curso (correo de Sofía León, 2026-10-05) · **Avance con evidencia:** 34.62 % · **Avance declarado:** 46.15 % (ponderados por criticidad)

El checklist no está aprobado. El estado se calcula, pero una persona tiene que aprobarlo antes de darlo por bueno.

| Id | Tarea | Responsable | Vence | Estado | Evidencia |
|---|---|---|---|---|---|
| C-01 | Cerrar los módulos de ventas, compras e inventarios | Lucía Mora | 2026-10-01 | cumplida con evidencia | `C-01-soporte.md` |
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | cumplida sin evidencia | — |
| C-03 | Cruzar las facturas emitidas con las ventas | Lucía Mora | 2026-10-02 | cumplida con evidencia | `C-03-soporte.md` |
| C-04 | Conciliar cartera contra su auxiliar | Marta Ríos | 2026-10-05 | cumplida con evidencia | `C-04-soporte.md` |
| C-05 | Registrar provisiones y causaciones | Jorge Vela | 2026-10-05 | vencida | — |
| C-06 | Preparar los papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo | — |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | bloqueada por C-02 y C-05 | — |
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 | — |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 | — |

**Ruta crítica del cierre:** C-02 → C-07 → C-08 → C-09

**Lo que no se pudo procesar:** todo lo que llegó se procesó.

**Las preguntas que hizo:** nadie respondió en esta sesión. Tomé nueve respuestas de los documentos y quedaron en la ficha.
- Entidad: Minera Cóndor, RUC 0990054321001, Ecuador, USD.
- Marco contable: no está en los documentos, así que quedó registrado como «no indicado».
- Periodo: 2026-09.
- Cuentas: ventas 41; compras 14/51/52/61; IVA 2408; se concilian 1305 y 2205.
- Bancos: andino-4101 y pacifico-4102.
- Checklist: el de la organización, sin constancia de aprobación.
- Quien aprueba: Sofía León.
- Festivos: ninguno a mano, lista vacía.

**Qué falta para que esto sea mejor:**
- El soporte firmado de C-02.
- El soporte de C-05.
- La aprobación del checklist.
- El marco contable.
- Los festivos del calendario.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

La corrida quedó registrada como `2026-10-06-finance-setup-1`. El reporte completo está en `estado-finanzas/0990054321001-minera-condor/cierre/2026-09/reporte-close-status.md`.

No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque nadie podía autorizarlo en esta sesión. No medí los minutos hasta el primer resultado.