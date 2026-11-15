# /criterio-finance:finance-setup finanzas/DNO190402B43-distribuidora-del-noroeste

Soy Clara. Proceso los documentos de tu cierre y te muestro qué cuadra, qué no y qué no tiene soporte.

Usé la carpeta que venía en el argumento: `finanzas/DNO190402B43-distribuidora-del-noroeste`. Nadie iba a responder, así que tomé cada respuesta de los documentos:
1. **Entidad:** Distribuidora del Noroeste, RFC DNO190402B43, México, MXN. Salen del nombre de la carpeta y del emisor de los CFDI.
2. **Marco contable:** NIF del CINIF, que usa la mayoría de las empresas no listadas en México (F-20). Ningún documento lo dice, así que falta confirmarlo.
3. **Periodo:** 2026-09, el último que tiene `10-contabilidad/`.
4. **Cuentas que cruzan las facturas:** ventas 4135; compras 5135, 5145 y 5195; IVA generado y descontable 2408. Son las que sostienen las facturas del periodo.
5. **Cuentas que se concilian:** 1305 y 2205, que tienen auxiliar en 2026-09 o en 2026-08. Bancos: andino-4301 y pacifico-4302.
6. **Checklist:** el de la organización, `00-referencia/checklist-cierre.csv`.
7. **Quién aprueba:** Sofía León, responsable de C-09. No hay festivos a mano.
8. **Dónde guardo el estado:** `estado-finanzas/DNO190402B43-distribuidora-del-noroeste`.
9. **Términos:** los acepta José Francisco Ñáñez, con fecha 2026-10-06.

No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta porque nadie dio ese sí.

## Listo — Distribuidora del Noroeste

**Lo que miré:** 62 archivos · periodos 2026-01 a 2026-09 · presupuesto 2026 · 0 fuera de la estructura
**Términos:** aceptados para la versión 1.5.4 · comprobante en `.criterio/terminos/aceptacion-criterio-finance-1.5.4-2026-10-06.md` y `.pdf`

El reporte de abajo trae solo la señal del checklist. El cálculo del periodo encontró 8 señales en total; las demás se ven con `/criterio-finance:bank-reconcile`, `/criterio-finance:einvoice-check`, `/criterio-finance:ledger-check` y `/criterio-finance:account-reconcile`.

# Estado del cierre · Distribuidora del Noroeste · periodo 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `close-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una tarea figura cumplida y ningún documento la sostiene (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte en 2026-09/40-soportes/ que empiece por C-02 | — | Andrés Paz | — | `00-referencia/checklist-cierre.csv` fila 3 |

## El resultado

**Estado declarado:** en curso (`2026-09/40-soportes/correo-estado-del-cierre.md`, 2026-10-05) · **Avance con evidencia:** 42.31 % · **Avance declarado:** 53.85 % (ponderados por criticidad)

| Id | Tarea | Responsable | Vence | Criticidad | Estado | Evidencia |
|---|---|---|---|---|---|---|
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | alta | cumplida sin evidencia | — |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | alta | bloqueada por otra (C-02) | — |
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | alta | bloqueada por otra (C-07) | — |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | alta | bloqueada por otra (C-08) | — |
| C-06 | Preparar los papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | alta | en plazo | — |
| C-01 | Cerrar los módulos de ventas, compras e inventarios | Lucía Mora | 2026-10-01 | alta | cumplida con evidencia | `2026-09/40-soportes/C-01-soporte.md` |
| C-03 | Cruzar las facturas emitidas con las ventas | Lucía Mora | 2026-10-02 | alta | cumplida con evidencia | `2026-09/40-soportes/C-03-soporte.pdf` |
| C-04 | Conciliar cartera contra su auxiliar | Marta Ríos | 2026-10-05 | alta | cumplida con evidencia | `2026-09/40-soportes/C-04-soporte.md` |
| C-05 | Registrar provisiones y causaciones | Jorge Vela | 2026-10-05 | media | cumplida con evidencia | `2026-09/40-soportes/C-05-soporte.pdf` |

**Ruta crítica del cierre:** C-02 → C-07 → C-08 → C-09

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Esta es la carpeta de documentos de la entidad? → Sí: finanzas/DNO190402B43-distribuidora-del-noroeste, la que trae el argumento
- ¿Cuál es la entidad (nombre, identificación fiscal, país y moneda)? → Distribuidora del Noroeste · RFC DNO190402B43 · México · MXN, del nombre de la carpeta y del emisor de los CFDI
- ¿Qué marco contable adoptó la entidad? → NIF del CINIF, el de la mayoría de las no listadas en México (F-20); ningún documento lo dice
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → Ventas 4135 · compras 5135, 5145, 5195 · IVA generado 2408 · IVA descontable 2408, las que sostienen las facturas del periodo
- ¿Qué cuentas se concilian contra auxiliar y qué cuentas bancarias se esperan? → 1305 y 2205, con auxiliar en 2026-09 o 2026-08; bancos andino-4301 y pacifico-4302
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv
- ¿Quién aprueba el cierre y qué festivos tiene el calendario? → Sofía León, responsable de C-09; sin festivos a mano
- ¿Dónde se guarda el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste
- ¿Se marca la carpeta con _CRITERIO_FINANZAS.txt? → No: nadie dio el sí en esta sesión de prueba

## Fuentes

- `00-referencia/checklist-cierre.csv`

**Qué falta para que esto sea mejor:**
- El soporte de C-02 en `2026-09/40-soportes/`.
- El auxiliar de 2205-proveedores para 2026-09: estaba en 2026-08 y en este periodo no aparece.
- Que alguien confirme el marco contable.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella. No creé la tarea programada porque nadie la confirmó; se corre a mano con `/criterio-finance:finance-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

---
La configuración quedó en `.criterio/finanzas/DNO190402B43-distribuidora-del-noroeste/config.json` y la validación no encontró problemas. La corrida quedó registrada como `2026-10-06-finance-setup-1`. Una corrección sobre la nota de esa corrida: dice que la conciliación vencida es la de 2205, pero el motor no dijo qué cuenta es; lo confirma `/criterio-finance:account-reconcile`.