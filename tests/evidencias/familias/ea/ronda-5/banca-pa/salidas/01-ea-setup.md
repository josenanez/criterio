# /criterio-assistant:ea-setup direccion/presidencia-ejecutiva

Soy Ofelia. Preparo el trabajo de la oficina: la agenda contra los compromisos, cada sesión con su material y sus decisiones, el borrador del acta y lo que pide respuesta. No decido ni envío nada.

**Carpeta.** Hay una sola candidata: `direccion/presidencia-ejecutiva`, que tiene 00-referencia/, 10-agenda/, 20-correspondencia/, 30-viajes/ y 90-borradores/. Es la del argumento, así que la tomo.

**Lo que encontré:**
- Agenda: una exportación en `10-agenda/`, del 2026-10-25.
- Órganos: comite-ejecutivo, con sesiones del 2026-09-21, 2026-10-05 y 2026-10-19, y junta-directiva, con sesiones del 2026-09-24 y 2026-10-29.
- Correspondencia: 8 correos en `20-correspondencia/`, uno de ellos una respuesta de la oficina. Hay además un itinerario en `30-viajes/`.

La carpeta ya sigue la estructura recomendada. No moví ni creé nada en ella.

**Las respuestas, tomadas de los documentos** (es una sesión de prueba, así que cada una va con la propuesta):
1. El ejecutivo, quien lo asiste y la entidad: Presidencia ejecutiva, Yariela Castillo y Banco del Istmo, con país PA. Sale de `00-referencia/oficina.md`.
2. Los órganos: junta-directiva (nueve directores, el último jueves de cada mes) y comite-ejecutivo (las vicepresidencias, los lunes). Sale de `00-referencia/organos.csv`.
3. Las carpetas excluidas: ninguna.
4. El correo de la oficina: presidencia@bancoistmo.test.
5. La zona horaria: America/Panama.
6. Los umbrales: los de `config.example.json`. Son 5 días antes de una sesión para el material, 15 días para el acta, 2 movimientos de un compromiso para que suene, una agenda de 7 días como máximo, una ventana de 14 días y 14 días de plazo para una decisión.
7. Rostrum: no se publica.
8. El estado: en `estado-direccion/presidencia-ejecutiva`, fuera de la carpeta de documentos.
9. Los términos:

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

   José Francisco Ñáñez los aceptó el 2026-10-26 (términos 1.6, Ofelia 1.5.0).

**La marca `_CRITERIO_DIRECCION.txt`:** no la dejé, porque nadie la autorizó.

**Lo que quedó listo:**
- La configuración: `.criterio/direccion/presidencia-ejecutiva/config.json`. Está validada y no trajo problemas.
- El comprobante de los términos: `.criterio/terminos/aceptacion-criterio-assistant-1.5.0-2026-10-26.md` y su `.pdf`.
- Las fichas: 5 de sesiones, 7 de correos y 1 de viaje. La respuesta de la oficina no lleva ficha. Ninguna trajo `record_issues`.

Este reporte cubre la agenda: los cruces, las sesiones sin material o sin acta y los viajes. Los compromisos vencidos y los correos sin respuesta salen en `/criterio-assistant:ea-commitments` y `/criterio-assistant:ea-mail`. El motor marcó la exportación `.ics` como «no reconocida» en la conversión de texto, pero `agenda` la procesó completa.

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

**Cuándo vuelvo:** sin reloj. En esta sesión de prueba nadie dio un sí explícito a la tarea programada. Para correrlo a mano: `/criterio-assistant:ea-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.