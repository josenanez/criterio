# /criterio-assistant:ea-setup direccion/presidencia

Ofelia quedó instalada sobre la oficina de Presidencia del Banco Andino. Procesé las 5 sesiones, los 8 correos recibidos y los 3 itinerarios, y crucé la agenda contra los viajes.

**Respuestas tomadas de los documentos** (`00-referencia/oficina.md` y `organos.csv`):
- **Ejecutivo y entidad:** Presidencia, asistida por Laura Gómez, en Banco Andino (CO).
- **Órganos:** junta-directiva y comite-de-presidencia.
- **Carpetas excluidas:** ninguna.
- **Correo de la oficina:** presidencia@bancoandino.test
- **Zona horaria:** America/Bogota
- **Umbrales:** los de ejemplo.
- **Rostrum:** no se publica.
- **Estado:** en `estado-direccion/presidencia`.
- **Términos 1.5:** aceptados por José Francisco Ñáñez con fecha 2026-10-26. El comprobante quedó en `.criterio/terminos/`.

**Lo que dejé sin hacer:**
- **Marca de la raíz:** nadie la autorizó, así que no dejé `_CRITERIO_DIRECCION.txt`.
- **Reloj:** no hubo un sí, así que no hay tarea programada. Se corre a mano con `/criterio-assistant:ea-wake`.

Este reporte no muestra los compromisos vencidos ni la correspondencia sin respuesta. Los muestran `/criterio-assistant:ea-commitments` y `/criterio-assistant:ea-mail`.

---

# La semana · Banco Andino · al 2026-10-26 · oficina de Presidencia

**Entidad:** Banco Andino · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 1.2.3 · **Comando:** `ea-agenda`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-10-29: «Sesión de la junta» (14:00–17:00) se cruza con «Visita del supervisor» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 2 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-03: «Reunión con la firma auditora 4» (15:00–16:00) se cruza con «Visita del cliente 4» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 3 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-03: «Llamada con la casa matriz» (09:00–10:00) se cruza con «Revisión con tesorería» (09:00–09:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 4 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-04: «Reunión con la firma auditora 1» (15:00–16:00) se cruza con «Visita del cliente 1» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 5 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-05: «Reunión con la firma auditora 2» (15:00–16:00) se cruza con «Visita del cliente 2» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 6 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-06: «Reunión con la firma auditora 3» (15:00–16:00) se cruza con «Visita del cliente 3» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 7 | Una reunión de la agenda cae durante un vuelo del itinerario del ejecutivo (`meeting_during_flight`) | «Llamada con la calificadora» (2026-10-27 19:15) cae durante el vuelo AV 9217, que sale a las 19:00 y llega a las 20:00 | — | — | — | `30-viajes/MDE-itinerario-medellin.md, línea 9` · `10-agenda/agenda-2026-10-25.ics` |
| 8 | Una reunión de la agenda cae durante un vuelo del itinerario del ejecutivo (`meeting_during_flight`) | «Cena de la junta del gremio» (2026-11-05 18:30) cae durante el vuelo AV 9342, que sale a las 18:00 y llega a las 19:35 | — | — | — | `30-viajes/UIO-itinerario-quito.md, línea 9` · `10-agenda/agenda-2026-10-25.ics` |
| 9 | Una reunión presencial en la ciudad del ejecutivo cae mientras el itinerario lo tiene de viaje en otra (`meeting_while_away`) | «Reunión con el sindicato» (2026-10-27 11:00) es presencial en Bogotá (Sede principal, Bogotá) y ese día el viaje a Medellín sigue | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `30-viajes/MDE-itinerario-medellin.md` |
| 10 | Una reunión presencial en la ciudad del ejecutivo cae mientras el itinerario lo tiene de viaje en otra (`meeting_while_away`) | «Visita a la oficina principal» (2026-10-28 14:00) es presencial en Bogotá (Oficina principal, Bogotá) y ese día el viaje a Cali sigue | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `30-viajes/CLO-itinerario-cali.md` |
| 11 | Una reunión presencial en la ciudad del ejecutivo cae mientras el itinerario lo tiene de viaje en otra (`meeting_while_away`) | «Comité de riesgos» (2026-11-04 10:00) es presencial en Bogotá (Sala de juntas, sede principal, Bogotá) y ese día el viaje a Quito sigue | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `30-viajes/UIO-itinerario-quito.md` |
| 12 | Pasados los días configurados de una sesión, su acta firmada no está (`meeting_without_minutes`) | comite-de-presidencia del 2026-09-21: pasaron 35 días y su acta firmada no está en 40-acta/ | — | — | 35 | `organos/comite-de-presidencia/2026-09-21/40-acta/` |
| 13 | A los días configurados de una sesión de un órgano, su material no está en la carpeta (`meeting_without_material`) | junta-directiva del 2026-10-29: faltan 3 días y su material no está en 20-material/ | — | — | 3 | `organos/junta-directiva/2026-10-29/20-material/` |
| 14 | Un vuelo del itinerario no está en la agenda: ese tiempo se ve libre (`trip_not_in_agenda`) | el vuelo AV 9210 (Bogotá → Medellín) sale el 2026-10-27 06:00 y no está en la agenda: ese tiempo se ve libre | — | — | — | `30-viajes/MDE-itinerario-medellin.md, línea 8` |
| 15 | Un vuelo del itinerario no está en la agenda: ese tiempo se ve libre (`trip_not_in_agenda`) | el vuelo AV 9341 (Bogotá → Quito) sale el 2026-11-03 06:00 y no está en la agenda: ese tiempo se ve libre | — | — | — | `30-viajes/UIO-itinerario-quito.md, línea 8` |
| 16 | Un vuelo del itinerario no está en la agenda: ese tiempo se ve libre (`trip_not_in_agenda`) | el vuelo AV 9520 (Bogotá → Cali) sale el 2026-10-28 06:30 y no está en la agenda: ese tiempo se ve libre | — | — | — | `30-viajes/CLO-itinerario-cali.md, línea 8` |
| 17 | Un vuelo del itinerario no está en la agenda: ese tiempo se ve libre (`trip_not_in_agenda`) | el vuelo AV 9527 (Cali → Bogotá) sale el 2026-10-28 20:00 y no está en la agenda: ese tiempo se ve libre | — | — | — | `30-viajes/CLO-itinerario-cali.md, línea 9` |

## El resultado

Agenda exportada el 2026-10-25 (`10-agenda/agenda-2026-10-25.ics`), del 2026-10-26 al 2026-11-09.

| Inicio | Fin | Reunión |
|---|---|---|
| 2026-10-26 08:00 | 09:30 | Comité de presidencia |
| 2026-10-27 08:00 | 12:00 | Bloque de concentración (libre) |
| 2026-10-27 08:00 | 09:00 | Llamada con la casa matriz |
| 2026-10-27 09:00 | 09:30 | Revisión con tesorería |
| 2026-10-27 11:00 | 12:00 | Reunión con el sindicato |
| 2026-10-27 19:00 | 20:00 | Vuelo AV 9217 Medellín–Bogotá |
| 2026-10-27 19:15 | 19:45 | Llamada con la calificadora |
| 2026-10-28 14:00 | 15:00 | Visita a la oficina principal |
| 2026-10-29 14:00 | 17:00 | Sesión de la junta |
| 2026-10-29 15:30 | 16:30 | Visita del supervisor |
| 2026-10-30 12:30 | 14:00 | Almuerzo con el comité de auditoría |
| 2026-11-02 | todo el día | Día sin reuniones |
| 2026-11-02 08:00 | 09:30 | Comité de presidencia |
| 2026-11-03 09:00 | 10:00 | Llamada con la casa matriz |
| 2026-11-03 09:00 | 09:30 | Revisión con tesorería |
| 2026-11-03 15:00 | 16:00 | Reunión con la firma auditora 4 |
| 2026-11-03 15:30 | 16:30 | Visita del cliente 4 |
| 2026-11-04 08:00 | 09:00 | Comité de crédito |
| 2026-11-04 10:00 | 11:00 | Comité de riesgos |
| 2026-11-04 11:30 | 12:30 | Reunión con el banco corresponsal |
| 2026-11-04 15:00 | 16:00 | Reunión con la firma auditora 1 |
| 2026-11-04 15:30 | 16:30 | Visita del cliente 1 |
| 2026-11-05 15:00 | 16:00 | Reunión con la firma auditora 2 |
| 2026-11-05 15:30 | 16:30 | Visita del cliente 2 |
| 2026-11-05 18:00 | 19:35 | Vuelo AV 9342 Quito–Bogotá |
| 2026-11-05 18:30 | 20:00 | Cena de la junta del gremio |
| 2026-11-06 15:00 | 16:00 | Reunión con la firma auditora 3 |
| 2026-11-06 15:30 | 16:30 | Visita del cliente 3 |

| Órgano | Sesión | Días | Material | Acta |
|---|---|---|---|---|
| comite-de-presidencia | 2026-09-21 | -35 | 1 | no |
| comite-de-presidencia | 2026-10-05 | -21 | 3 | sí |
| comite-de-presidencia | 2026-10-19 | -7 | 1 | no |
| junta-directiva | 2026-09-24 | -32 | 2 | sí |
| junta-directiva | 2026-10-29 | 3 | no | no |

| Viaje | Vuelo | Ruta | Sale | Llega | En la agenda |
|---|---|---|---|---|---|
| Cali | AV 9520 | Bogotá → Cali | 2026-10-28 06:30 | 07:30 | no |
| Cali | AV 9527 | Cali → Bogotá | 2026-10-28 20:00 | 21:00 | no |
| Medellín | AV 9210 | Bogotá → Medellín | 2026-10-27 06:00 | 07:00 | no |
| Medellín | AV 9217 | Medellín → Bogotá | 2026-10-27 19:00 | 20:00 | sí |
| Quito | AV 9341 | Bogotá → Quito | 2026-11-03 06:00 | 07:35 | no |
| Quito | AV 9342 | Quito → Bogotá | 2026-11-05 18:00 | 19:35 | sí |

No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-agenda/agenda-2026-10-25.ics`
- `30-viajes/CLO-itinerario-cali.md`
- `30-viajes/CLO-itinerario-cali.md, línea 8`
- `30-viajes/CLO-itinerario-cali.md, línea 9`
- `30-viajes/MDE-itinerario-medellin.md`
- `30-viajes/MDE-itinerario-medellin.md, línea 8`
- `30-viajes/MDE-itinerario-medellin.md, línea 9`
- `30-viajes/UIO-itinerario-quito.md`
- `30-viajes/UIO-itinerario-quito.md, línea 8`
- `30-viajes/UIO-itinerario-quito.md, línea 9`
- `organos/comite-de-presidencia/2026-09-21/40-acta/`
- `organos/junta-directiva/2026-10-29/20-material/`

---

**Cuándo vuelvo:** sin reloj.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

La corrida quedó registrada como `2026-10-26-ea-setup-1`, con 50 hallazgos. La salida completa está en `estado-direccion/presidencia/corridas/salida-ea-setup.md`.