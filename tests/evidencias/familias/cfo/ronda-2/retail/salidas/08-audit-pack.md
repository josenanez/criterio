# /criterio-finance:audit-pack 

Los cinco requerimientos del auditor ya estaban en la tabla `pbc-2026-09.csv`, así que no hubo nada que convertir. Tres tienen respuesta con soporte y dos siguen sin responder.

# Paquete del auditor · Almacenes Caribe · periodo 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `audit-pack`

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

- ¿Cuál es la entidad, su NIT, país y moneda? → Almacenes Caribe, NIT 900765432, Colombia, COP (de la carpeta; sesión sin interfaz)
- ¿Qué marco contable aplica? → No encontrado en los documentos: queda «por confirmar»
- ¿Cuál es el periodo que se está cerrando? → 2026-09 (el último con 10-contabilidad)
- ¿Qué prefijos de cuentas cruzan las facturas? → Ventas 41, compras 14/51/52/61, IVA generado y descontable 2408 (los habituales; el balance tiene 4135, 5105-5305 y 2408)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205; bancos andino-3701 y pacifico-3702 (las carpetas de 20-bancos). Solo existe auxiliar de 1305
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; sin aprobación registrada, queda como no aprobado
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (Contraloría, responsable de C-09 en el checklist); festivo 2026-10-12 (el del ejemplo, sin confirmar)
- ¿Dónde se guarda el estado? → estado-finanzas/900765432-almacenes-caribe
- ¿Se acepta el texto de los términos? → Sí, José Francisco Ñáñez, 2026-10-06 (indicado en la sesión de prueba)

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-audit-pack-1`. El reporte del motor está en `estado-finanzas/900765432-almacenes-caribe/cierre/2026-09/reporte-audit-pack.md`.