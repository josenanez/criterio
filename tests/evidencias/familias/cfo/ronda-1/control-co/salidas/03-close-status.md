# /criterio-finance:close-status 

Sofía León declaró el 2026-10-05 que el cierre de septiembre está «en curso», y los soportes lo confirman. Los términos 1.2 ya estaban aceptados el 2026-10-06 a nombre de José Francisco Ñáñez, y la declaración ya estaba en la ficha.

# Estado del cierre · Distribuidora Control · periodo 2026-09

**Entidad:** Distribuidora Control (900000001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.7.0 · **Aprueba:** Sofía León · **Comando:** `close-status`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Estado declarado:** en curso (`2026-09/40-soportes/correo-estado-del-cierre.md`, 2026-10-05) · **Avance con evidencia:** 53,85 % · **Avance declarado:** 53,85 % (ponderados por criticidad)

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

- ¿Cuál es la entidad, su NIT, país y moneda? → Distribuidora Control, NIT 900000001, Colombia, COP (sesión sin interfaz: tomado de la carpeta y las facturas)
- ¿Qué marco o grupo NIIF aplica? → No encontrado en los documentos; queda 'por confirmar'
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → Ventas 41; compras 14, 51, 52, 61; IVA generado y descontable 2408
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205 (traen auxiliar); bancos andino-5301 y pacifico-5302
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv, sin aprobar
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (responsable de C-09); festivo 2026-10-12
- ¿Dónde se guarda el estado? → estado-finanzas/900000001-distribuidora-control
- ¿Se deja la marca _CRITERIO_FINANZAS.txt en la carpeta? → No: sin interfaz no hay un sí para escribir dentro de los documentos

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-close-status-1` con 0 hallazgos. El texto mostrado está en `estado-finanzas/900000001-distribuidora-control/corridas/salida-close-status.md`.