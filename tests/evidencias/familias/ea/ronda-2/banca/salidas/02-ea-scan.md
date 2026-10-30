# /criterio-assistant:ea-scan 

Corrida de prueba sin interfaz: nadie respondió preguntas y se usó la fecha de corte indicada. Las fichas de sesiones, correos y viajes se escribieron con su cita y el cálculo no devolvió observaciones sobre ellas. Los compromisos que aparecen solo en notas (sin acta firmada) no se copiaron a la ficha: esperan el acta.

# Procesar · Banco Andino · al 2026-10-26 · oficina de Presidencia

**Entidad:** Banco Andino · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 0.12.1 · **Comando:** `ea-scan`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Compromiso vencido sin documento que lo sostenga (`commitment_overdue`) | comite-de-presidencia 2026-10-05, C-1: «Entregar el informe 1 de seguimiento», venció el 2026-10-12 | Diana Cruz | 14 | `organos/comite-de-presidencia/2026-10-05/40-acta/acta-firmada.md, línea 21` |
| 2 | ídem | C-2: «Entregar el informe 2 de seguimiento», venció el 2026-10-13 | Felipe Duarte | 13 | `…/acta-firmada.md, línea 22` |
| 3 | ídem | C-3: «Entregar el informe 3 de seguimiento», venció el 2026-10-14 | Laura Gómez | 12 | `…/acta-firmada.md, línea 23` |
| 4 | ídem | C-4: «Entregar el informe 4 de seguimiento», venció el 2026-10-15 | Andrés Vela | 11 | `…/acta-firmada.md, línea 24` |
| 5 | ídem | junta-directiva 2026-09-24, C-1: «Presentar el informe de cartera vencida», venció el 2026-10-15 | Felipe Duarte | 11 | `organos/junta-directiva/2026-09-24/40-acta/acta-firmada.md, línea 14` |
| 6 | ídem | comite-de-presidencia 2026-10-05, C-5: «Entregar el informe 5 de seguimiento», venció el 2026-10-16 | Diana Cruz | 10 | `…/acta-firmada.md, línea 25` |
| 7 | ídem | C-6: «Entregar el informe 6 de seguimiento», venció el 2026-10-17 | Felipe Duarte | 9 | `…/acta-firmada.md, línea 26` |
| 8 | Correo con plazo vencido sin respuesta guardada (`correspondence_unanswered`) | oficios@supervisor.test: «Requerimiento 45: cartera reestructurada», pidió respuesta para el 2026-10-20 | — | 6 | `20-correspondencia/2026-10-08-supervisor.msg` |
| 9 | ídem | ventas@proveedor.test: «Solicitud 1», plazo 2026-10-20 | — | 6 | `20-correspondencia/2026-10-14-solicitud-1.msg` |
| 10 | ídem | «Solicitud 2», plazo 2026-10-21 | — | 5 | `20-correspondencia/2026-10-15-solicitud-2.msg` |
| 11 | ídem | «Solicitud 3», plazo 2026-10-22 | — | 4 | `20-correspondencia/2026-10-16-solicitud-3.msg` |
| 12 | ídem | «Solicitud 4», plazo 2026-10-23 | — | 3 | `20-correspondencia/2026-10-17-solicitud-4.msg` |
| 13 | ídem | «Solicitud 5», plazo 2026-10-24 | — | 2 | `20-correspondencia/2026-10-18-solicitud-5.msg` |
| 14 | Dos reuniones se cruzan en la agenda (`meeting_conflict`) | 2026-10-29: «Sesión de la junta» (14:00–17:00) con «Visita del supervisor» (15:30–16:30) | — | — | `10-agenda/agenda-2026-10-25.ics` |
| 15 | ídem | 2026-11-03: «Reunión con la firma auditora 4» (15:00–16:00) con «Visita del cliente 4» (15:30–16:30) | — | — | `10-agenda/agenda-2026-10-25.ics` |
| 16 | ídem | 2026-11-03: «Llamada con la casa matriz» (09:00–10:00) con «Revisión con tesorería» (09:00–09:30) | — | — | `10-agenda/agenda-2026-10-25.ics` |
| 17 | ídem | 2026-11-04: «Reunión con la firma auditora 1» con «Visita del cliente 1» (15:00–16:00 y 15:30–16:30) | — | — | `10-agenda/agenda-2026-10-25.ics` |
| 18 | ídem | 2026-11-05: «Reunión con la firma auditora 2» con «Visita del cliente 2» (15:00–16:00 y 15:30–16:30) | — | — | `10-agenda/agenda-2026-10-25.ics` |
| 19 | ídem | 2026-11-06: «Reunión con la firma auditora 3» con «Visita del cliente 3» (15:00–16:00 y 15:30–16:30) | — | — | `10-agenda/agenda-2026-10-25.ics` |
| 20 | Reunión durante un vuelo (`meeting_during_flight`) | «Llamada con la calificadora» (2026-10-27 19:15) cae durante el vuelo AV 9217 (19:00–20:00) | — | — | `30-viajes/MDE-itinerario-medellin.md, línea 9` |
| 21 | ídem | «Cena de la junta del gremio» (2026-11-05 18:30) cae durante el vuelo AV 9342 (18:00–19:35) | — | — | `30-viajes/UIO-itinerario-quito.md, línea 9` |
| 22 | Reunión presencial en Bogotá con el ejecutivo de viaje (`meeting_while_away`) | «Reunión con el sindicato» (2026-10-27 11:00); ese día el viaje a Medellín sigue | — | — | `30-viajes/MDE-itinerario-medellin.md` |
| 23 | ídem | «Visita a la oficina principal» (2026-10-28 14:00); ese día el viaje a Cali sigue | — | — | `30-viajes/CLO-itinerario-cali.md` |
| 24 | ídem | «Comité de riesgos» (2026-11-04 10:00); ese día el viaje a Quito sigue | — | — | `30-viajes/UIO-itinerario-quito.md` |
| 25 | Acta firmada ausente pasados los días configurados (`meeting_without_minutes`) | comite-de-presidencia 2026-09-21: pasaron 35 días y su acta no está en 40-acta/ | — | 35 | `organos/comite-de-presidencia/2026-09-21/40-acta/` |
| 26 | Decisión pendiente con plazo dentro de los días configurados (`decision_deadline`) | D-2 «Sede de la oficina regional»: plazo 2026-11-04, en 9 días | — | 9 | `…/2026-10-05/20-material/propuesta-2.md, línea 3` |
| 27 | ídem | D-1 «Proveedor de la mesa de ayuda»: plazo 2026-11-03, en 8 días | — | 8 | `…/2026-10-05/20-material/propuesta-1.md, línea 3` |
| 28 | ídem | junta-directiva D-1 «Proveedor del centro de datos alterno»: plazo 2026-11-02, en 7 días | — | 7 | `organos/junta-directiva/2026-09-24/20-material/propuesta-centro-de-datos.md, línea 3` |
| 29 | Material ausente (`meeting_without_material`) | junta-directiva 2026-10-29: faltan 3 días y su material no está en 20-material/ | — | 3 | `organos/junta-directiva/2026-10-29/20-material/` |
| 30–32 | Compromiso movido más veces de las configuradas (`commitment_rescheduled`) | comite-de-presidencia 2026-10-05, C-7, C-8 y C-9 (planes 7, 8 y 9 de mejora): cada uno se movió 3 veces; vigentes 2026-12-04, 2026-12-05 y 2026-12-06 | Laura Gómez, Andrés Vela, Diana Cruz | — | `…/acta-firmada.md, líneas 27, 28 y 29` |
| 33 | ídem | junta-directiva 2026-09-24, C-2: «Entregar el plan de continuidad del negocio» se movió 3 veces (2026-10-15, 2026-10-30, 2026-11-20) | Andrés Vela | — | `organos/junta-directiva/2026-09-24/40-acta/acta-firmada.md, línea 15` |
| 34–37 | Vuelo que no está en la agenda (`trip_not_in_agenda`) | AV 9210 (2026-10-27 06:00), AV 9341 (2026-11-03 06:00), AV 9520 (2026-10-28 06:30) y AV 9527 (2026-10-28 20:00) | — | — | `30-viajes/…, líneas 8 y 9` |
| 38–43 | Acuerdo sin fecha (`agreement_without_date`) | comite-de-presidencia 2026-10-05: A-7, A-8, A-9, A-10 y A-11; junta-directiva 2026-09-24: A-3 | — | — | `…/acta-firmada.md, líneas 14–18; junta, punto 3` |
| 44–50 | Acuerdo sin responsable (`agreement_without_owner`) | comite-de-presidencia 2026-10-05: A-1 a A-6; junta-directiva 2026-09-24: A-2 | — | — | `…/acta-firmada.md, líneas 8–13; junta, punto 2` |

*(Las filas 2–7, 9–13, 15–19, 30–50 se agrupan aquí por espacio; el reporte completo, una fila por señal, está en `estado-direccion/presidencia/reporte-ea-scan.md`.)*

## El resultado

No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

Agenda `10-agenda/agenda-2026-10-25.ics`; los seis correos con plazo vencido de `20-correspondencia/`; los tres itinerarios de `30-viajes/`; las actas firmadas del comité de presidencia (2026-10-05) y de la junta directiva (2026-09-24); las propuestas de ambas sesiones; y las carpetas de las sesiones del 2026-09-21 y del 2026-10-29.

---

**Una aclaración sobre lo anterior:** en este mensaje condensé la tabla (agrupé filas y abrevié citas). El texto íntegro, fila por fila, está en `estado-direccion/presidencia/corridas/salida-ea-scan.md`, que es lo que quedó registrado como salida de la corrida (id `2026-10-26-ea-scan-1`, 50 hallazgos). Si necesita que le muestre el reporte completo sin condensar, dígamelo.