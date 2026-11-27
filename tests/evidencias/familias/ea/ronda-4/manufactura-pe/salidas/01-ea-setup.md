# /criterio-assistant:ea-setup direccion/gerencia-general

Soy Ofelia. Preparo el trabajo de la oficina: la agenda contra los compromisos, cada sesión con su material y sus decisiones, el borrador del acta y lo que pide respuesta. No decido ni envío nada.

Ofelia quedó instalada en la oficina de Gerencia general de Industrias del Rímac. La configuración se validó sin problemas y el cálculo levantó 40 señales sin errores en las fichas. Lo principal de la agenda: 5 cruces, una cena que cae durante el vuelo de regreso de Arequipa y el directorio del 2026-10-29 todavía sin material.

**La carpeta.** Encontré una sola candidata, `direccion/gerencia-general`, y la tomé como la carpeta de la oficina. Ya sigue la estructura recomendada, así que no moví ni creé nada dentro.
- **Agenda:** `10-agenda/agenda-2026-10-25.ics`, exportada el 2026-10-25.
- **Sesiones en `organos/`:** comite-de-gerencia (2026-09-21, 2026-10-05, 2026-10-19) y directorio (2026-09-24, 2026-10-29).
- **Correos en `20-correspondencia/`:** 8.

**Las respuestas, tomadas de los documentos:**
1. **Ejecutivo y quien asiste:** Gerencia general, con Silvia Chávez como asistente; entidad Industrias del Rímac, país PE (`00-referencia/oficina.md`).
2. **Órganos:** directorio (siete directores, el último jueves de cada mes) y comite-de-gerencia (las gerencias, los lunes), según `00-referencia/organos.csv`.
3. **Carpetas excluidas:** ninguna.
4. **Correo de la oficina:** presidencia@rimac-ind.test.
5. **Zona horaria:** America/Lima.
6. **Umbrales:** los de `config.example.json`:
   - material 5 días antes de la sesión;
   - acta en 15 días;
   - el compromiso suena a las 2 movidas;
   - agenda de máximo 7 días de antigüedad;
   - ventana de 14 días;
   - plazo de decisión de 14 días.
7. **Rostrum:** no se publica.
8. **Estado:** `estado-direccion/gerencia-general`.
9. **Términos (versión 1.6):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-10-26. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-assistant-1.4.2-2026-10-26.md` y en su `.pdf`.

**La marca.** No dejé `_CRITERIO_DIRECCION.txt` en la carpeta porque nadie dio un sí explícito.

**La configuración** quedó en `.criterio/direccion/gerencia-general/config.json`.

**Las fichas.** Procesé las 5 sesiones, los 7 correos que llegaron a la oficina y el itinerario a Arequipa. La respuesta que la oficina guardó la cruza el motor. Este reporte cubre solo la agenda: los compromisos vencidos se ven con `/criterio-assistant:ea-commitments` y los correos sin respuesta con `/criterio-assistant:ea-mail`.

# La semana · Industrias del Rímac · al 2026-10-26 · oficina de Gerencia general

**Entidad:** Industrias del Rímac · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 1.4.2 · **Comando:** `ea-agenda`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Cruce (`meeting_conflict`) | 2026-10-29: «Sesión de la junta» (14:00–17:00) se cruza con «Visita del supervisor» (15:30–16:30) | — | `10-agenda/agenda-2026-10-25.ics` |
| 2 | Cruce (`meeting_conflict`) | 2026-11-03: «Llamada con la casa matriz» (09:00–10:00) se cruza con «Revisión con tesorería» (09:00–09:30) | — | `10-agenda/agenda-2026-10-25.ics` |
| 3 | Cruce (`meeting_conflict`) | 2026-11-04: «Reunión con la firma auditora 1» (15:00–16:00) se cruza con «Visita del cliente 1» (15:30–16:30) | — | `10-agenda/agenda-2026-10-25.ics` |
| 4 | Cruce (`meeting_conflict`) | 2026-11-05: «Reunión con la firma auditora 2» (15:00–16:00) se cruza con «Visita del cliente 2» (15:30–16:30) | — | `10-agenda/agenda-2026-10-25.ics` |
| 5 | Cruce (`meeting_conflict`) | 2026-11-06: «Reunión con la firma auditora 3» (15:00–16:00) se cruza con «Visita del cliente 3» (15:30–16:30) | — | `10-agenda/agenda-2026-10-25.ics` |
| 6 | Reunión durante un vuelo (`meeting_during_flight`) | «Cena de la junta del gremio industrial» (2026-11-05 18:30) cae durante el vuelo LA 2118, que sale a las 18:00 y llega a las 19:30 | — | `30-viajes/AQP-itinerario-arequipa.md, línea 9` · `10-agenda/agenda-2026-10-25.ics` |
| 7 | Reunión presencial durante el viaje (`meeting_while_away`) | «Comité de producción» (2026-11-04 10:00) es presencial en Lima (Sala de directorio, planta de Ate, Lima) y ese día el viaje a Arequipa sigue | — | `10-agenda/agenda-2026-10-25.ics` · `30-viajes/AQP-itinerario-arequipa.md` |
| 8 | Sesión sin acta (`meeting_without_minutes`) | comite-de-gerencia del 2026-09-21: pasaron 35 días y su acta firmada no está en 40-acta/ (lo que hay es un borrador) | 35 | `organos/comite-de-gerencia/2026-09-21/40-acta/` |
| 9 | Sesión sin material (`meeting_without_material`) | directorio del 2026-10-29: faltan 3 días y su material no está en 20-material/ | 3 | `organos/directorio/2026-10-29/20-material/` |
| 10 | Vuelo fuera de la agenda (`trip_not_in_agenda`) | el vuelo LA 2111 (Lima → Arequipa) sale el 2026-11-03 06:00 y no está en la agenda: ese tiempo se ve libre | — | `30-viajes/AQP-itinerario-arequipa.md, línea 8` |

## El resultado

Agenda exportada el 2026-10-25, del 2026-10-26 al 2026-11-09: 22 eventos. La tabla completa está en `estado-direccion/gerencia-general/reporte-ea-agenda.md`.

| Órgano | Sesión | Días | Material | Acta |
|---|---|---|---|---|
| comite-de-gerencia | 2026-09-21 | -35 | 1 | no |
| comite-de-gerencia | 2026-10-05 | -21 | 3 | sí |
| comite-de-gerencia | 2026-10-19 | -7 | 1 | no |
| directorio | 2026-09-24 | -32 | 2 | sí |
| directorio | 2026-10-29 | 3 | no | no |

| Viaje | Vuelo | Ruta | Sale | Llega | En la agenda |
|---|---|---|---|---|---|
| Arequipa | LA 2111 | Lima → Arequipa | 2026-11-03 06:00 | 07:30 | no |
| Arequipa | LA 2118 | Arequipa → Lima | 2026-11-05 18:00 | 19:30 | sí |

No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `organos/comite-de-gerencia/2026-09-21/40-acta/acta-BORRADOR.md`: un borrador en 40-acta/ no es el acta, porque el acta es la que se firma.
- `90-borradores/LEEME.txt`: está en 90-borradores/ sin «BORRADOR» en el nombre.

## Las preguntas que hizo

Ninguna en esta corrida.

---

**Cuándo vuelvo:** sin reloj. No creé la tarea programada porque nadie dio un sí explícito; a mano se corre con `/criterio-assistant:ea-wake`.

La corrida quedó registrada como `2026-10-26-ea-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.