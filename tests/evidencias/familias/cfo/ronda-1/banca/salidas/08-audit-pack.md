# /criterio-finance:audit-pack 

Términos vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-06). Todos los requerimientos ya estaban en la tabla del auditor, así que no hubo nada que convertir.

R-04 y R-05 siguen sin responder. Ninguno está vencido a la fecha de la prueba, pero R-05 vence el 2026-10-08 y R-04 el 2026-10-09.

# Paquete del auditor · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.7.0 · **Aprueba:** Sofía León · **Comando:** `audit-pack`

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

- ¿Cuál es la entidad, su NIT, país y moneda? → Banco Andino, NIT 900123456, Colombia, COP (de la carpeta finanzas/900123456-banco-andino)
- ¿Qué marco contable aplica? → Grupo 1 (F-05); solo se registra
- ¿Cuál es el periodo que se está cierrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué prefijos cruzan las facturas? → Ventas 41; compras 14, 51, 52, 61; IVA 2408 (del balance de comprobación)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (las que tienen auxiliar); bancos andino-1101 y pacifico-1102 (carpetas de 20-bancos)
- ¿Qué checklist se usa y está aprobado? → El de la organización (00-referencia/checklist-cierre.csv); sin aprobación documentada, queda como no aprobado
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (responsable de C-09); festivo 2026-10-12
- ¿Dónde se guarda el estado? → estado-finanzas/900123456-banco-andino
- ¿Acepta los términos vigentes? → Sí, José Francisco Ñáñez, versión 1.2, 2026-10-06 (dado en el encargo de la prueba)
- ¿Se deja el archivo _CRITERIO_FINANZAS.txt en la carpeta de documentos? → No; nadie autorizó escribir dentro de los documentos

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-audit-pack-1`.