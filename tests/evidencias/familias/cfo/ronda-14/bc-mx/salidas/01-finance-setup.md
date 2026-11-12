# /criterio-finance:finance-setup finanzas/DNO190402B43-distribuidora-del-noroeste

## Listo: Distribuidora del Noroeste (RFC DNO190402B43)

**Lo que miré:** 62 archivos · periodos 2026-01 a 2026-09 y presupuesto 2026 · 0 fuera de la estructura recomendada
**Términos:** aceptados por José Francisco Ñáñez para la versión 1.5.4 (términos 1.5) · el comprobante quedó en `.criterio/terminos/aceptacion-criterio-finance-1.5.4-2026-10-06.md` y `.pdf`

En septiembre el motor encontró 8 señales. Este reporte del estado del cierre solo muestra la que toca al checklist: C-02 aparece cumplida, pero no tiene soporte, y es la primera tarea de la ruta crítica. Sofía León declaró el cierre «en curso» en su correo del 2026-10-05, y eso coincide con los documentos.

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

- ¿Cuál es la entidad: nombre, identificación fiscal, país y moneda? → Distribuidora del Noroeste, RFC DNO190402B43, México, MXN (sugerida desde el nombre de la carpeta y los CFDI 4.0 del periodo)
- ¿Qué marco contable adoptó la entidad? → NIF del CINIF (sugerida: la mayoría de las no listadas en México, F-20; ningún documento dice otro)
- ¿Cuál es el periodo que se está cerrando? → 2026-09
- ¿Qué cuentas cruzan las facturas? → Ventas 4135; compras 5135, 5145, 5195; IVA generado 2408; IVA descontable 2408 (las que sostienen las facturas del periodo)
- ¿Qué cuentas se concilian contra auxiliar y qué cuentas bancarias se esperan? → 1305 y 2205; bancos andino-4301 y pacifico-4302
- ¿Qué checklist se usa? → El de la organización: 00-referencia/checklist-cierre.csv
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (C-09 del checklist); sin festivos registrados
- ¿Dónde se guarda el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste
- ¿Acepta los términos de esta versión? → Sí, José Francisco Ñáñez, 2026-10-06

## Fuentes

- `00-referencia/checklist-cierre.csv`

---

**Lo que falta para que esto sea mejor:**
- El auxiliar de la cuenta 2205 (proveedores). Estuvo en agosto y no llegó en septiembre.
- El soporte de C-02 en `2026-09/40-soportes/`.
- Que la entidad confirme su marco contable. Quedó NIF del CINIF porque es la respuesta sugerida.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella. No programé ninguna tarea, porque en esta prueba nadie dio un sí explícito. Se corre a mano con `/criterio-finance:finance-wake`.

**Dónde quedó todo:**
- La configuración está en `.criterio/finanzas/DNO190402B43/config.json`.
- El estado está en `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/`.
- La corrida quedó registrada como `2026-10-06-finance-setup-1`.
- Dejé `_CRITERIO_FINANZAS.txt` en la carpeta de documentos. Lo hice porque esa era la respuesta sugerida; nadie dio un sí explícito.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.