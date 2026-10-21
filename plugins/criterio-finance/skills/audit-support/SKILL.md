---
name: audit-support
description: "El paquete del auditor: el índice de requerimientos, cómo se nombra cada respuesta, cuándo un requerimiento está respondido con soporte y qué se hace con los que llegaron en Word, PDF o correo. Úsalo al preparar el paquete para la auditoría o revisar qué requerimientos siguen abiertos. Audit requests, PBC list, audit package."
---

# El paquete del auditor

## El índice

El auditor suele entregar sus requerimientos como una tabla —la lista de lo que el cliente prepara—: va en `<AAAA-MM>/50-auditoria/requerimientos/`, en `.xlsx` o `.csv`, con `id` y `solicitud`, y si las trae, `fecha`, `fecha_limite`, `responsable` y `estado`. Un requerimiento que llegó en Word, PDF o correo se extrae a `audit_requests` de la ficha aplicando el skill de la ficha del cierre.

## Las respuestas

Cada respuesta es un archivo en `50-auditoria/respuestas/` cuyo nombre empieza por el id del requerimiento: `R-07-partidas-conciliatorias.xlsx`. Así el índice cita dónde está, sin mover ni copiar nada.

| Estado | Cuando |
|---|---|
| Respondido con soporte | Hay un archivo de respuesta con su id |
| Respondido sin soporte | La tabla dice respondido y no hay archivo |
| Vencido | Pasó su fecha límite sin respuesta |
| Sin responder | Todavía en plazo |

`audit_request_unanswered` se levanta con los respondidos sin soporte y con los vencidos.
