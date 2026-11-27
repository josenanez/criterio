# /criterio-assistant:ea-agenda 

Los términos de la versión 1.6 ya estaban vigentes (aceptada con la 1.4.2), así que no pidieron una nueva aceptación. La agenda es del 2026-10-25 y cubre del 26 de octubre al 9 de noviembre. Hay cruces el 29 de octubre y los días 4, 5 y 6 de noviembre, el 4 de noviembre además hay un choque con un vuelo, y se ve una sesión sin material y otra sin acta. El reporte del motor va completo, tal cual:

# La semana · Software Austral · al 2026-10-26 · oficina de Gerencia general

**Entidad:** Software Austral · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 1.4.2 · **Comando:** `ea-agenda`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-10-29: «Sesión de la junta» (14:00–17:00) se cruza con «Visita del supervisor» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 2 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-04: «Reunión con la firma auditora 1» (15:00–16:00) se cruza con «Visita del cliente 1» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 3 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-05: «Reunión con la firma auditora 2» (15:00–16:00) se cruza con «Visita del cliente 2» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 4 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-06: «Reunión con la firma auditora 3» (15:00–16:00) se cruza con «Visita del cliente 3» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 5 | Una reunión de la agenda cae durante un vuelo del itinerario del ejecutivo (`meeting_during_flight`) | «Llamada con los inversionistas» (2026-11-04 20:00) cae durante el vuelo LA 601, que sale a las 19:00 y llega a las 23:00 | — | — | — | `30-viajes/LIM-itinerario-lima.md, línea 9` · `10-agenda/agenda-2026-10-25.ics` |
| 6 | Una reunión presencial en la ciudad del ejecutivo cae mientras el itinerario lo tiene de viaje en otra (`meeting_while_away`) | «Comité de directorio» (2026-11-03 12:00) es presencial en Santiago de Chile (Oficinas centrales, Las Condes, Santiago) y ese día el viaje a Lima sigue | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `30-viajes/LIM-itinerario-lima.md` |
| 7 | Pasados los días configurados de una sesión, su acta firmada no está (`meeting_without_minutes`) | comite-ejecutivo del 2026-09-21: pasaron 35 días y su acta firmada no está en 40-acta/ | — | — | 35 | `organos/comite-ejecutivo/2026-09-21/40-acta/` |
| 8 | A los días configurados de una sesión de un órgano, su material no está en la carpeta (`meeting_without_material`) | directorio del 2026-10-29: faltan 3 días y su material no está en 20-material/ | — | — | 3 | `organos/directorio/2026-10-29/20-material/` |
| 9 | Un vuelo del itinerario no está en la agenda: ese tiempo se ve libre (`trip_not_in_agenda`) | el vuelo LA 600 (Santiago de Chile → Lima) sale el 2026-11-03 07:00 y no está en la agenda: ese tiempo se ve libre | — | — | — | `30-viajes/LIM-itinerario-lima.md, línea 8` |

## El resultado

Agenda exportada el 2026-10-25 (`10-agenda/agenda-2026-10-25.ics`), del 2026-10-26 al 2026-11-09.

| Inicio | Fin | Reunión |
|---|---|---|
| 2026-10-26 08:00 | 09:30 | Comité de presidencia |
| 2026-10-27 08:00 | 12:00 | Bloque de concentración (libre) |
| 2026-10-29 14:00 | 17:00 | Sesión de la junta |
| 2026-10-29 15:30 | 16:30 | Visita del supervisor |
| 2026-10-30 12:30 | 14:00 | Almuerzo con el comité de auditoría |
| 2026-11-02 | todo el día | Día sin reuniones |
| 2026-11-02 08:00 | 09:30 | Comité de presidencia |
| 2026-11-03 12:00 | 13:00 | Comité de directorio |
| 2026-11-03 15:00 | 16:30 | Reunión con el cliente |
| 2026-11-04 15:00 | 16:00 | Reunión con la firma auditora 1 |
| 2026-11-04 15:30 | 16:30 | Visita del cliente 1 |
| 2026-11-04 19:00 | 23:00 | Vuelo LA 601 Lima–Santiago de Chile |
| 2026-11-04 20:00 | 21:00 | Llamada con los inversionistas |
| 2026-11-05 15:00 | 16:00 | Reunión con la firma auditora 2 |
| 2026-11-05 15:30 | 16:30 | Visita del cliente 2 |
| 2026-11-06 15:00 | 16:00 | Reunión con la firma auditora 3 |
| 2026-11-06 15:30 | 16:30 | Visita del cliente 3 |

| Órgano | Sesión | Días | Material | Acta |
|---|---|---|---|---|
| comite-ejecutivo | 2026-09-21 | -35 | 1 | no |
| comite-ejecutivo | 2026-10-05 | -21 | 3 | sí |
| comite-ejecutivo | 2026-10-19 | -7 | 1 | no |
| directorio | 2026-09-24 | -32 | 2 | sí |
| directorio | 2026-10-29 | 3 | no | no |

| Viaje | Vuelo | Ruta | Sale | Llega | En la agenda |
|---|---|---|---|---|---|
| Lima | LA 600 | Santiago de Chile → Lima | 2026-11-03 07:00 | 11:40 | no |
| Lima | LA 601 | Lima → Santiago de Chile | 2026-11-04 19:00 | 23:00 | sí |

Carpetas excluidas, que no se procesaron: `20-correspondencia/personal`.
No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-agenda/agenda-2026-10-25.ics`
- `30-viajes/LIM-itinerario-lima.md`
- `30-viajes/LIM-itinerario-lima.md, línea 8`
- `30-viajes/LIM-itinerario-lima.md, línea 9`
- `organos/comite-ejecutivo/2026-09-21/40-acta/`
- `organos/directorio/2026-10-29/20-material/`

La corrida quedó registrada como `2026-10-26-ea-agenda-1`, con 39 hallazgos en total. La salida mostrada está en `corridas/salida-ea-agenda.md`, dentro del estado de la oficina. No envié, agendé ni moví nada.