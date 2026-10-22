# /criterio-finance:close-status 

La declaración de Sofía León del 2026-10-05 («en curso») ya estaba registrada en la ficha, así que no hubo nada nuevo que registrar. Lo declarado y lo evidenciado coinciden: las cinco tareas marcadas cumplidas tienen soporte, y las cuatro restantes siguen abiertas.

# Estado del cierre · Comercial Control · periodo 2026-09

**Entidad:** Comercial Control (1790000001001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `close-status`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Estado declarado:** en curso (`2026-09/40-soportes/correo-estado-del-cierre.md`, 2026-10-05) · **Avance con evidencia:** 53.85 % · **Avance declarado:** 53.85 % (ponderados por criticidad)

El checklist no está aprobado: el estado se calcula, y una persona tiene que aprobarlo antes de darlo por bueno.

| Id | Tarea | Responsable | Vence | Criticidad | Estado | Evidencia |
|---|---|---|---|---|---|---|
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | alta | bloqueada por otra (C-07) | — |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | alta | bloqueada por otra (C-08) | — |
| C-06 | Preparar los papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | alta | en plazo | — |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | alta | en plazo | — |
| C-01 | Cerrar los módulos de ventas, compras e inventarios | Lucía Mora | 2026-10-01 | alta | cumplida con evidencia | `2026-09/40-soportes/C-01-soporte.md` |
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | alta | cumplida con evidencia | `2026-09/40-soportes/C-02-soporte.md` |
| C-03 | Cruzar las facturas emitidas con las ventas | Lucía Mora | 2026-10-02 | alta | cumplida con evidencia | `2026-09/40-soportes/C-03-soporte.md` |
| C-04 | Conciliar cartera contra su auxiliar | Marta Ríos | 2026-10-05 | alta | cumplida con evidencia | `2026-09/40-soportes/C-04-soporte.md` |
| C-05 | Registrar provisiones y causaciones | Jorge Vela | 2026-10-05 | media | cumplida con evidencia | `2026-09/40-soportes/C-05-soporte.md` |

**Ruta crítica del cierre:** C-07 → C-08 → C-09

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta de documentos? → finanzas/1790000001001-comercial-control (la del argumento; única candidata)
- ¿Entidad, país y moneda? → Comercial Control, RUC 1790000001001, Ecuador, USD (por el nombre de la carpeta y las facturas del SRI)
- ¿Qué marco aplica en Ecuador? → No encontrado en los documentos; queda «NIIF (marco por confirmar)»
- ¿Qué periodo se está cerrando? → 2026-09 (el último con 10-contabilidad/)
- ¿Qué cuentas cruzan las facturas? → Ventas 4135; compras 1435, 5135, 5145, 5195; IVA 2408 (las del balance de comprobación)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (tienen auxiliar); bancos andino-6701 y pacifico-6702
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; no aprobado hasta que una persona lo apruebe
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (Contraloría, tarea C-09); festivos: no encontrados, lista vacía
- ¿Dónde se guarda el estado? → estado-finanzas/1790000001001-comercial-control, fuera de la carpeta de documentos
- ¿Se deja el archivo _CRITERIO_FINANZAS.txt en la carpeta? → No se dejó: no hubo una autorización expresa para escribir en los documentos

## Fuentes

- Sin documentos citados.

---
Corrida registrada como `2026-10-06-close-status-1`, con 0 hallazgos.