# /criterio-assistant:ea-scan 

Corrida de prueba sin interfaz: los términos ya estaban vigentes y no hubo preguntas. Las notas de los dos comités de presidencia solo traen un compromiso sin acta firmada, así que esperan el acta y no entraron a las fichas de acuerdos.

# Procesar · Banco Andino · al 2026-10-26 · oficina de Presidencia

**Entidad:** Banco Andino (None) · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 0.11.0 · **Comando:** `ea-scan`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Un compromiso venció y ningún documento lo sostiene como cumplido (`commitment_overdue`) | junta-directiva del 2026-09-24, C-1: «Presentar el informe de cartera vencida» de Felipe Duarte venció el 2026-10-15 y ningún documento lo sostiene como cumplido | Felipe Duarte | 11 | `organos/junta-directiva/2026-09-24/40-acta/acta-firmada.md, línea 14` |
| 2 | Un correo guardado pide respuesta y su plazo venció sin una respuesta guardada (`correspondence_unanswered`) | oficios@supervisor.test: «Requerimiento 45: cartera reestructurada» pidió respuesta para el 2026-10-20 y no hay una respuesta guardada | — | 6 | `20-correspondencia/2026-10-08-supervisor.eml` |
| 3 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-10-29: «Sesión de la junta» (14:00–17:00) se cruza con «Visita del supervisor» (15:30–16:30) | — | — | `10-agenda/agenda-2026-10-25.ics` |
| 4 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-03: «Llamada con la casa matriz» (09:00–10:00) se cruza con «Revisión con tesorería» (09:00–09:30) | — | — | `10-agenda/agenda-2026-10-25.ics` |
| 5 | Pasados los días configurados de una sesión, su acta firmada no está (`meeting_without_minutes`) | comite-de-presidencia del 2026-09-21: pasaron 35 días y su acta firmada no está en 40-acta/ | — | 35 | `organos/comite-de-presidencia/2026-09-21/40-acta/` |
| 6 | Una decisión pendiente tiene una fecha que la fija dentro de los días configurados (`decision_deadline`) | junta-directiva, D-1: «Proveedor del centro de datos alterno» tiene plazo el 2026-11-02, en 7 días, y sigue pendiente | — | 7 | `organos/junta-directiva/2026-09-24/20-material/propuesta-centro-de-datos.md, línea 3` |
| 7 | A los días configurados de una sesión de un órgano, su material no está en la carpeta (`meeting_without_material`) | junta-directiva del 2026-10-29: faltan 3 días y su material no está en 20-material/ | — | 3 | `organos/junta-directiva/2026-10-29/20-material/` |
| 8 | Un compromiso se movió más veces de las configuradas (`commitment_rescheduled`) | junta-directiva del 2026-09-24, C-2: «Entregar el plan de continuidad del negocio» se movió 3 veces (2026-10-15, 2026-10-30, 2026-11-20) | Andrés Vela | — | `…/40-acta/acta-firmada.md, línea 15` |
| 9 | Un acuerdo del acta no tiene fecha (`agreement_without_date`) | junta-directiva del 2026-09-24, A-3: «Contratar la auditoría del sistema de pagos» no tiene fecha | — | — | `…/40-acta/acta-firmada.md, punto 3` |
| 10 | Un acuerdo del acta no tiene responsable (`agreement_without_owner`) | junta-directiva del 2026-09-24, A-2: «Actualizar la política de viajes» no tiene responsable | — | — | `…/40-acta/acta-firmada.md, punto 2` |

## El resultado

No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

Las citas de la tabla, más `10-agenda/agenda-2026-10-25.ics` y `20-correspondencia/2026-10-08-supervisor.eml`.

*Nota: en esta vista abrevié las columnas y las fuentes. El reporte completo está en `estado-direccion/presidencia/reporte-ea-scan.md`, y la corrida quedó registrada como `2026-10-26-ea-scan-1`.*