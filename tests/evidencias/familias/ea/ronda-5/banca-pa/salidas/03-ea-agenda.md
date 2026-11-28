# /criterio-assistant:ea-agenda 

Los términos de esta versión ya estaban vigentes, así que no hubo que registrar una aceptación nueva. La agenda de la semana trae cinco cruces, un vuelo que no está en la agenda, una sesión sin material y una sin acta.

# La semana · Banco del Istmo · al 2026-10-26 · oficina de Presidencia ejecutiva

**Entidad:** Banco del Istmo · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 1.5.0 · **Comando:** `ea-agenda`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-10-29: «Sesión de la junta» (14:00–17:00) se cruza con «Visita del supervisor» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 2 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-03: «Llamada con la casa matriz» (09:00–10:00) se cruza con «Revisión con tesorería» (09:00–09:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 3 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-04: «Reunión con la firma auditora 1» (15:00–16:00) se cruza con «Visita del cliente 1» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 4 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-05: «Reunión con la firma auditora 2» (15:00–16:00) se cruza con «Visita del cliente 2» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 5 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-06: «Reunión con la firma auditora 3» (15:00–16:00) se cruza con «Visita del cliente 3» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 6 | Una reunión de la agenda cae durante un vuelo del itinerario del ejecutivo (`meeting_during_flight`) | «Cena de la asociación bancaria» (2026-11-04 18:30) cae durante el vuelo CM 204, que sale a las 18:00 y llega a las 19:40 | — | — | — | `30-viajes/BOG-itinerario-bogota.md, línea 9` · `10-agenda/agenda-2026-10-25.ics` |
| 7 | Una reunión presencial en la ciudad del ejecutivo cae mientras el itinerario lo tiene de viaje en otra (`meeting_while_away`) | «Comité de riesgos» (2026-11-03 10:00) es presencial en Ciudad de Panamá (Sala de directores, Torre del banco, Ciudad de Panamá) y ese día el viaje a Bogotá sigue | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `30-viajes/BOG-itinerario-bogota.md` |
| 8 | Pasados los días configurados de una sesión, su acta firmada no está (`meeting_without_minutes`) | comite-ejecutivo del 2026-09-21: pasaron 35 días y su acta firmada no está en 40-acta/ | — | — | 35 | `organos/comite-ejecutivo/2026-09-21/40-acta/` |
| 9 | A los días configurados de una sesión de un órgano, su material no está en la carpeta (`meeting_without_material`) | junta-directiva del 2026-10-29: faltan 3 días y su material no está en 20-material/ | — | — | 3 | `organos/junta-directiva/2026-10-29/20-material/` |
| 10 | Un vuelo del itinerario no está en la agenda: ese tiempo se ve libre (`trip_not_in_agenda`) | el vuelo CM 201 (Ciudad de Panamá → Bogotá) sale el 2026-11-03 07:00 y no está en la agenda: ese tiempo se ve libre | — | — | — | `30-viajes/BOG-itinerario-bogota.md, línea 8` |

## El resultado

Agenda exportada el 2026-10-25 (`10-agenda/agenda-2026-10-25.ics`), del 2026-10-26 al 2026-11-09.

| Inicio | Fin | Reunión |
|---|---|---|
| 2026-10-26 08:00 | 09:30 | Comité de presidencia |
| 2026-10-27 08:00 | 09:00 | Llamada con la casa matriz |
| 2026-10-27 09:00 | 09:30 | Revisión con tesorería |
| 2026-10-27 08:00 | 12:00 | Bloque de concentración (libre) |
| 2026-10-29 14:00 | 17:00 | Sesión de la junta |
| 2026-10-29 15:30 | 16:30 | Visita del supervisor |
| 2026-10-30 12:30 | 14:00 | Almuerzo con el comité de auditoría |
| 2026-11-02 | todo el día | Día sin reuniones |
| 2026-11-02 08:00 | 09:30 | Comité de presidencia |
| 2026-11-03 09:00 | 10:00 | Llamada con la casa matriz |
| 2026-11-03 09:00 | 09:30 | Revisión con tesorería |
| 2026-11-03 10:00 | 11:00 | Comité de riesgos |
| 2026-11-03 15:00 | 16:00 | Reunión con el banco corresponsal |
| 2026-11-04 15:00 | 16:00 | Reunión con la firma auditora 1 |
| 2026-11-04 15:30 | 16:30 | Visita del cliente 1 |
| 2026-11-04 18:00 | 19:40 | Vuelo CM 204 Bogotá–Ciudad de Panamá |
| 2026-11-04 18:30 | 20:00 | Cena de la asociación bancaria |
| 2026-11-05 15:00 | 16:00 | Reunión con la firma auditora 2 |
| 2026-11-05 15:30 | 16:30 | Visita del cliente 2 |
| 2026-11-06 15:00 | 16:00 | Reunión con la firma auditora 3 |
| 2026-11-06 15:30 | 16:30 | Visita del cliente 3 |

| Órgano | Sesión | Días | Material | Acta |
|---|---|---|---|---|
| comite-ejecutivo | 2026-09-21 | -35 | 1 | no |
| comite-ejecutivo | 2026-10-05 | -21 | 3 | sí |
| comite-ejecutivo | 2026-10-19 | -7 | 1 | no |
| junta-directiva | 2026-09-24 | -32 | 2 | sí |
| junta-directiva | 2026-10-29 | 3 | no | no |

| Viaje | Vuelo | Ruta | Sale | Llega | En la agenda |
|---|---|---|---|---|---|
| Bogotá | CM 201 | Ciudad de Panamá → Bogotá | 2026-11-03 07:00 | 08:40 | no |
| Bogotá | CM 204 | Bogotá → Ciudad de Panamá | 2026-11-04 18:00 | 19:40 | sí |

No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-agenda/agenda-2026-10-25.ics`
- `30-viajes/BOG-itinerario-bogota.md`
- `30-viajes/BOG-itinerario-bogota.md, línea 8`
- `30-viajes/BOG-itinerario-bogota.md, línea 9`
- `organos/comite-ejecutivo/2026-09-21/40-acta/`
- `organos/junta-directiva/2026-10-29/20-material/`