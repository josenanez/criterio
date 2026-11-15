# /criterio-assistant:ea-mail 

Seis correos piden respuesta, su plazo ya venció y no tienen respuesta guardada. Ninguno está marcado como rutinario en su ficha, así que no hay borradores: cada uno necesita que una persona lo responda. El del supervisor es un requerimiento y nunca se trata como rutinario.

# Correspondencia · Banco Andino · al 2026-10-26 · oficina de Presidencia

**Entidad:** Banco Andino · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 1.2.3 · **Comando:** `ea-mail`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un correo guardado pide respuesta y su plazo venció sin una respuesta guardada (`correspondence_unanswered`) | oficios@supervisor.test: «Requerimiento 45: cartera reestructurada» pidió respuesta para el 2026-10-20 y no hay una respuesta guardada | — | — | 6 | `20-correspondencia/2026-10-08-supervisor.msg` |
| 2 | Un correo guardado pide respuesta y su plazo venció sin una respuesta guardada (`correspondence_unanswered`) | ventas@proveedor.test: «Solicitud 1: confirmación de condiciones» pidió respuesta para el 2026-10-20 y no hay una respuesta guardada | — | — | 6 | `20-correspondencia/2026-10-14-solicitud-1.msg` |
| 3 | Un correo guardado pide respuesta y su plazo venció sin una respuesta guardada (`correspondence_unanswered`) | ventas@proveedor.test: «Solicitud 2: confirmación de condiciones» pidió respuesta para el 2026-10-21 y no hay una respuesta guardada | — | — | 5 | `20-correspondencia/2026-10-15-solicitud-2.msg` |
| 4 | Un correo guardado pide respuesta y su plazo venció sin una respuesta guardada (`correspondence_unanswered`) | ventas@proveedor.test: «Solicitud 3: confirmación de condiciones» pidió respuesta para el 2026-10-22 y no hay una respuesta guardada | — | — | 4 | `20-correspondencia/2026-10-16-solicitud-3.msg` |
| 5 | Un correo guardado pide respuesta y su plazo venció sin una respuesta guardada (`correspondence_unanswered`) | ventas@proveedor.test: «Solicitud 4: confirmación de condiciones» pidió respuesta para el 2026-10-23 y no hay una respuesta guardada | — | — | 3 | `20-correspondencia/2026-10-17-solicitud-4.msg` |
| 6 | Un correo guardado pide respuesta y su plazo venció sin una respuesta guardada (`correspondence_unanswered`) | ventas@proveedor.test: «Solicitud 5: confirmación de condiciones» pidió respuesta para el 2026-10-24 y no hay una respuesta guardada | — | — | 2 | `20-correspondencia/2026-10-18-solicitud-5.msg` |

## El resultado

| Recibido | De | Asunto | Pide | Plazo | Respuesta guardada |
|---|---|---|---|---|---|
| 2026-10-08 | oficios@supervisor.test | Requerimiento 45: cartera reestructurada | Detalle de la cartera reestructurada del tercer trimestre (requerimiento 45) | 2026-10-20 | no |
| 2026-10-12 | gerencia@cliente.test | Solicitud de reunión | Confirmar una reunión con el presidente | 2026-10-16 | sí |
| 2026-10-14 | ventas@proveedor.test | Solicitud 1: confirmación de condiciones | Confirmar las condiciones del contrato 1 | 2026-10-20 | no |
| 2026-10-15 | ventas@proveedor.test | Solicitud 2: confirmación de condiciones | Confirmar las condiciones del contrato 2 | 2026-10-21 | no |
| 2026-10-16 | ventas@proveedor.test | Solicitud 3: confirmación de condiciones | Confirmar las condiciones del contrato 3 | 2026-10-22 | no |
| 2026-10-17 | ventas@proveedor.test | Solicitud 4: confirmación de condiciones | Confirmar las condiciones del contrato 4 | 2026-10-23 | no |
| 2026-10-18 | ventas@proveedor.test | Solicitud 5: confirmación de condiciones | Confirmar las condiciones del contrato 5 | 2026-10-24 | no |

Los borradores de las respuestas rutinarias quedan en 90-borradores/. Ofelia nunca envía.

No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-correspondencia/2026-10-08-supervisor.msg`
- `20-correspondencia/2026-10-14-solicitud-1.msg`
- `20-correspondencia/2026-10-15-solicitud-2.msg`
- `20-correspondencia/2026-10-16-solicitud-3.msg`
- `20-correspondencia/2026-10-17-solicitud-4.msg`
- `20-correspondencia/2026-10-18-solicitud-5.msg`

---

La corrida quedó registrada como `2026-10-26-ea-mail-1`.