# /criterio-finance:audit-pack 

Términos vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-06). Nada llegó en Word, PDF o correo fuera de la tabla del auditor. R-01 a R-03 constan como respondidas con soporte, pero cada archivo de respuesta solo dice que fue entregado. Conviene revisar que el soporte real esté.

# Paquete del auditor · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `audit-pack`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Requerimiento | Solicitud | Responsable | Vence | Estado | Respuesta |
|---|---|---|---|---|---|
| R-01 | Conciliaciones bancarias de septiembre | Andrés Paz | 2026-10-03 | respondido con soporte | `2026-09/50-auditoria/respuestas/R-01-respuesta.md` |
| R-02 | Auxiliar de cartera con antigüedad | Marta Ríos | 2026-10-03 | respondido con soporte | `2026-09/50-auditoria/respuestas/R-02-respuesta.md` |
| R-03 | Detalle de facturas emitidas | Lucía Mora | 2026-10-03 | respondido con soporte | `2026-09/50-auditoria/respuestas/R-03-respuesta.md` |
| R-04 | Actas del comité de presupuesto | Sofía León | 2026-10-09 | sin responder | — |
| R-05 | Contratos de los proveedores principales | Jorge Vela | 2026-10-08 | sin responder | — |

El índice no mueve ni copia archivos: cita dónde está cada uno.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su país y su moneda? → Banco Andino, NIT 900123456, Colombia, COP (tomado del nombre de la carpeta)
- ¿Qué marco contable aplica? → grupo 1 (propuesta por defecto; ningún documento lo declara, por confirmar)
- ¿Cuál es el periodo que se está cerrando? → 2026-09 (el último con 10-contabilidad)
- ¿Qué cuentas cruzan las facturas? → ventas 41; compras 14, 51, 52, 61; IVA generado y descontable 2408 (visto en el balance)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (hay auxiliar); bancos andino-1101 y pacifico-1102
- ¿Qué checklist se usa? → el de la organización, 00-referencia/checklist-cierre.csv
- ¿Quién aprueba el cierre? → Sofía León (Contraloría, responsable de C-09)
- ¿Festivos del calendario? → 2026-10-12 (festivo por defecto, por confirmar)
- ¿Dónde se guarda el estado? → estado-finanzas/900123456-banco-andino

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-audit-pack-1`, con la salida en `estado-finanzas/900123456-banco-andino/corridas/salida-audit-pack.md`.