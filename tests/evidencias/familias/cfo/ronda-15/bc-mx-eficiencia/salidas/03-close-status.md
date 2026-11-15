# /criterio-finance:close-status 

El cierre de septiembre 2026 está declarado «en curso», pero C-02 figura cumplida sin ningún soporte que lo pruebe. Los términos ya estaban aceptados (José Francisco Ñáñez, 2026-10-06, versión 1.5), así que no volví a registrarlos.

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

---

Dejé la corrida registrada como `2026-10-06-close-status-1`, con 4 de 9 tareas con evidencia y 1 señal abierta. La salida está en `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/corridas/salida-close-status.md`.

Aquí no declaro el estado del cierre. Eso le toca al contralor.