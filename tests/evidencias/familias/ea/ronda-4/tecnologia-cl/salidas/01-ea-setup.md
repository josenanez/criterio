# /criterio-assistant:ea-setup direccion/gerencia-general

Soy Ofelia. Preparo el trabajo de la oficina: la agenda contra los compromisos, cada sesión con su material y sus decisiones, el borrador del acta y lo que pide respuesta. No decido ni envío nada.

**La carpeta.** Encontré una sola candidata: `direccion/gerencia-general`, que tiene 00-referencia/, 10-agenda/, 20-correspondencia/, 30-viajes/ y 90-borradores/. Tomé esa, porque es la prueba.

**Lo que hay en ella:**
- **Agenda:** una exportación en `10-agenda/`, `agenda-2026-10-25.ics`, del 2026-10-25.
- **Órganos:** `comite-ejecutivo`, con sesiones del 2026-09-21, 2026-10-05 y 2026-10-19, y `directorio`, con sesiones del 2026-09-24 y 2026-10-29.
- **Correspondencia:** 9 correos en `20-correspondencia/`, uno de ellos en `personal/`.

La carpeta ya sigue la estructura recomendada, así que no moví ni creé nada en los documentos.

**Las preguntas, con la respuesta que tomé de los documentos:**
1. **Ejecutivo y quien asiste:** Gerencia general, asistida por Catalina Vergara. La entidad es Software Austral y el país CL, que saqué de la zona horaria de la oficina. Viene de `00-referencia/oficina.md`.
2. **Órganos:** el directorio (cinco directores, último martes de cada mes) y el comité ejecutivo (las gerencias, los lunes). Viene de `00-referencia/organos.csv`.
3. **Carpetas excluidas:** `20-correspondencia/personal`, según `oficina.md`.
4. **Correo de la oficina:** presidencia@austral-soft.test, según `oficina.md`.
5. **Zona horaria:** America/Santiago, según `oficina.md`.
6. **Umbrales:** los de `config.example.json`:
   - el material, 5 días antes de la sesión;
   - el acta, 15 días después;
   - un compromiso suena con 2 reprogramaciones;
   - la agenda, 7 días de antigüedad como máximo;
   - una ventana de 14 días;
   - y 14 días de plazo para una decisión.
7. **Rostrum:** no se publica.
8. **Dónde guardo lo que encuentro:** en `estado-direccion/gerencia-general`, fuera de la carpeta de documentos.
9. **Términos (versión 1.6):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-10-26.

**La marca `_CRITERIO_DIRECCION.txt`:** no la dejé. Nadie la autorizó en esta prueba y solo hay una carpeta candidata.

**Listo.** La configuración está en `.criterio/direccion/gerencia-general/config.json` y quedó validada sin problemas. El comprobante de la aceptación está en `.criterio/terminos/aceptacion-criterio-assistant-1.4.2-2026-10-26.md` y en su `.pdf`.

**Las primeras fichas:** 5 sesiones, 7 correos y 1 itinerario. La respuesta guardada de la oficina no lleva ficha y `personal/` está excluida. El motor no encontró problemas en las fichas. Ningún correo es rutinario, así que no escribí borradores de respuesta.

El motor ya calculó los compromisos vencidos o movidos de más, los acuerdos sin responsable o sin fecha, las decisiones con plazo y los correos sin respuesta. No salen en el reporte de la agenda: los muestran `/criterio-assistant:ea-commitments`, `/criterio-assistant:ea-mail` y `/criterio-assistant:ea-prep`.

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

---

**El reloj.** Propongo una tarea programada los días hábiles a las 7:00, para que Ofelia revise sola lo que toca cada día. En esta prueba nadie dio un sí explícito, así que no la creé. Se corre a mano con `/criterio-assistant:ea-wake`.

**Cuándo vuelvo:** sin reloj.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

---

**Notas de la prueba**, fuera de lo que se mostró:
- **La carpeta excluida sí se convirtió.** El paso `convertir` del motor convirtió `20-correspondencia/personal/2026-10-01-colegio.eml` y guardó su texto en la caché, aunque la carpeta está excluida. No tiene ficha y el reporte la da como no procesada. Conviene revisar ese paso.
- **La agenda se procesó, aunque `convertir` diga lo contrario.** `convertir` marca el `.ics` como «formato no reconocido», pero el comando `agenda` sí lo procesó.
- **El reporte cuenta cero preguntas.** El reporte de la agenda dice «Las preguntas que hizo: ninguna», aunque se respondieron las 9 desde los documentos. No hay en el motor un paso para registrarlas.
- **Registro.** La corrida quedó registrada como `2026-10-26-ea-setup-1`, con 39 hallazgos.