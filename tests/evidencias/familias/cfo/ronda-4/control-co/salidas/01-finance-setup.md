# /criterio-finance:finance-setup finanzas/900000001-distribuidora-control

## Listo — Distribuidora Control

**Lo que miré:** 64 archivos · periodos 2026-01 a 2026-09 y presupuesto-2026 · 0 fuera de la estructura.
**Términos:** aceptados para la versión 0.10.0 (términos 1.2) a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes quedaron en `.criterio/terminos/aceptacion-criterio-finance-0.10.0-2026-10-06.md` y `.pdf`.

**Respuestas que tomé yo, sin interlocutor:**
- **Entidad:** Distribuidora Control, NIT 900000001, CO, COP. Salen del nombre de la carpeta.
- **Marco:** grupo 1. Ningún documento lo dice, así que es el valor por defecto y hay que confirmarlo.
- **Periodo:** 2026-09, el último con `10-contabilidad/`.
- **Cuentas de las facturas:**
  - Ventas: 4135.
  - Compras: 5135, 5145 y 5195.
  - IVA generado y descontable: 2408.
  - Son las que sostienen facturas en el mayor.
- **Cuentas que se concilian:** 1305 y 2205, que tienen auxiliar.
- **Bancos:** andino-5301 y pacifico-5302.
- **Checklist:** el de la organización (`00-referencia/checklist-cierre.xlsx`), sin aprobar.
- **Aprobador:** Sofía León, responsable de C-09.
- **Festivo:** 2026-10-12.
- **No marqué la carpeta** con `_CRITERIO_FINANZAS.txt`, porque en esta prueba no se escribe nada dentro de los documentos.

# Estado del cierre · Distribuidora Control · periodo 2026-09

**Procesado:** 2026-10-06 · **Aprueba:** Sofía León

**Lo que hay que atender:** nada abierto en lo que procesa este comando.

**Estado declarado:** en curso. Lo dice el correo de Sofía León del 2026-10-05, `2026-09/40-soportes/correo-estado-del-cierre.md`. **Avance con evidencia:** 53,85 %. **Avance declarado:** 53,85 %.

El checklist no está aprobado. El estado se calcula igual, pero una persona tiene que aprobarlo antes de darlo por bueno.

| Id | Tarea | Responsable | Vence | Estado | Evidencia |
|---|---|---|---|---|---|
| C-01 | Cerrar los módulos de ventas, compras e inventarios | Lucía Mora | 2026-10-01 | cumplida con evidencia | `2026-09/40-soportes/C-01-soporte.md` |
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | cumplida con evidencia | `2026-09/40-soportes/C-02-soporte.pdf` |
| C-03 | Cruzar las facturas emitidas con las ventas | Lucía Mora | 2026-10-02 | cumplida con evidencia | `2026-09/40-soportes/C-03-soporte.md` |
| C-04 | Conciliar cartera contra su auxiliar | Marta Ríos | 2026-10-05 | cumplida con evidencia | `2026-09/40-soportes/C-04-soporte.md` |
| C-05 | Registrar provisiones y causaciones | Jorge Vela | 2026-10-05 | cumplida con evidencia | `2026-09/40-soportes/C-05-soporte.md` |
| C-06 | Preparar los papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo | — |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | en plazo | — |
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 | — |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 | — |

**Ruta crítica:** C-07 → C-08 → C-09.

**Lo que no se pudo procesar:** todo lo que llegó se procesó.

**Qué falta para que esto sea mejor:**
- **El reporte de close-status solo mira el checklist.** Que no traiga señales no quiere decir que las cuentas cuadren. Los cruces contra la contabilidad (`bank-reconcile`, `einvoice-check`, `ledger-check`, `account-reconcile`) aún no se han corrido.
- **El checklist hay que aprobarlo.** Falta que una persona lo apruebe.
- **El marco contable (grupo 1) hay que confirmarlo.**
- **La auditoría tiene dos requerimientos abiertos.** R-04 (actas del comité de presupuesto) vence el 2026-10-09. R-05 (contratos de los proveedores principales) vence el 2026-10-08.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

**Dónde quedó todo**
- **Configuración:** `.criterio/finanzas/900000001/config.json`, validada sin problemas.
- **Estado:** `estado-finanzas/900000001-distribuidora-control/`.
- **Salida de esta corrida:** `corridas/salida-finance-setup.md`, registrada como `2026-10-06-finance-setup-1`.