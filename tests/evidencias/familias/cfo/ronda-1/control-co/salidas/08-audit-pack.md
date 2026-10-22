# /criterio-finance:audit-pack 

Paquete del auditor de 2026-09 generado, mostrado y registrado como corrida `2026-10-06-audit-pack-1`.

Los términos (versión 1.2) estaban vigentes y registrados a nombre de José Francisco Ñáñez. No había requerimientos fuera de la tabla, así que no hubo nada que convertir. El índice solo cita dónde está cada archivo; no los mueve ni los copia.

# Paquete del auditor · Distribuidora Control · periodo 2026-09

**Entidad:** Distribuidora Control (900000001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.7.0 · **Aprueba:** Sofía León · **Comando:** `audit-pack`

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

Los archivos quedaron en estas rutas:
- **Reporte del motor:** `estado-finanzas/900000001-distribuidora-control/cierre/2026-09/reporte-audit-pack.md`
- **Salida de la corrida:** `estado-finanzas/900000001-distribuidora-control/corridas/salida-audit-pack.md`

Los requerimientos R-04 y R-05 siguen sin responder. Vencen el 2026-10-09 y el 2026-10-08, y con la fecha de la prueba (2026-10-06) aún no han vencido.