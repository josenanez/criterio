# /criterio-finance:finance-setup finanzas/900000001-distribuidora-control

## Listo — Distribuidora Control

**Lo que miré:** 58 archivos. Hay nueve periodos (2026-01 a 2026-09) y `presupuesto-2026`. Ninguno está fuera de la estructura.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.8.0 (términos 1.2). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-0.8.0-2026-10-06.md` y `.pdf`.

**Respuestas que tomé por mi cuenta, porque nadie podía contestar:**
- **Entidad:** Distribuidora Control, NIT 900000001, Colombia, COP. Salió de la carpeta y de las facturas XML.
- **Marco:** puse "grupo 2" como propuesta. Ningún documento lo dice, así que falta confirmarlo.
- **Cuentas que cruzan las facturas:** ventas 41; compras 14/51/52/61; IVA 2408.
- **Cuentas que se concilian:** 1305 y 2205.
- **Bancos esperados:** andino-5301 y pacifico-5302.
- **Quién aprueba:** Sofía León. Es la responsable de la tarea C-09.
- **Festivo:** 2026-10-12.
- **Checklist:** uso el de la organización, `00-referencia/checklist-cierre.csv`, y no está aprobado. Una persona tiene que aprobarlo.

No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta, porque en esta sesión nadie podía autorizarlo.

# Estado del cierre · periodo 2026-09

**Estado declarado:** en curso. Lo dice el correo de Sofía León del 2026-10-05, `2026-09/40-soportes/correo-estado-del-cierre.md`.
**Avance con evidencia:** 53,85 %. El avance declarado es el mismo, 53,85 %.
**Lo que hay que atender:** nada abierto en lo que procesa este comando.

| Id | Tarea | Responsable | Vence | Estado | Evidencia |
|---|---|---|---|---|---|
| C-01 a C-05 | Cinco tareas cumplidas | varios | 2026-10-01 a 10-05 | cumplida con evidencia | `2026-09/40-soportes/C-0N-soporte.md` |
| C-06 | Papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | en plazo | — |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | en plazo | — |
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | bloqueada por C-07 | — |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | bloqueada por C-08 | — |

**Ruta crítica:** C-07 → C-08 → C-09

**Qué falta para que esto sea mejor:**
- Los soportes C-01 a C-05 son una línea de firma cada uno. El motor los acepta como evidencia, pero no se ve qué hay detrás.
- Aún no he corrido `bank-reconcile`, `einvoice-check` ni `ledger-check`. Solo esos tres dicen si lo declarado cuadra con los datos.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

La salida quedó en `estado-finanzas/900000001-distribuidora-control/corridas/salida-finance-setup.md`. La corrida quedó registrada como `2026-10-06-finance-setup-1`, con 0 hallazgos.

Hice 0 preguntas a la persona. No medí cuántos minutos tardó en salir el primer resultado.