# /criterio-assistant:ea-setup direccion/direccion-general

Soy Ofelia. Preparo el trabajo de la oficina: la agenda contra los compromisos, cada sesión con su material y sus decisiones, el borrador del acta y lo que pide respuesta. No decido ni envío nada.

**Carpeta:** encontré una sola candidata, `direccion/direccion-general`. Tiene 00-referencia/, 10-agenda/, 20-correspondencia/, 30-viajes/ y 90-borradores/. Es la que uso.

**Lo que hay en ella:**
- **Agenda:** `10-agenda/agenda-2026-10-25.ics`, exportada el 2026-10-25.
- **Órganos:** comite-de-direccion (2026-09-21, 2026-10-05, 2026-10-19) y consejo-de-administracion (2026-09-24, 2026-10-29).
- **Correspondencia:** 8 correos .msg en `20-correspondencia/`. Uno es una respuesta de la oficina.

**Respuestas que tomé de los documentos:**
1. **Ejecutivo y entidad:** Dirección general, la asiste Claudia Montes. Entidad Cadena del Norte, MX (`00-referencia/oficina.md`).
2. **Órganos:** consejo-de-administracion (siete consejeros, último miércoles de cada mes) y comite-de-direccion (las direcciones, los lunes), según `00-referencia/organos.csv`.
3. **Carpetas excluidas:** ninguna.
4. **Correo de la oficina:** presidencia@cadenanorte.test.
5. **Zona horaria:** America/Mexico_City.
6. **Umbrales:** los de `config.example.json`:
   - material 5 días antes de la sesión;
   - acta 15 días después;
   - aviso a las 2 veces que se mueve un compromiso;
   - agenda de hasta 7 días de antigüedad;
   - ventana de 14 días;
   - plazo de decisión de 14 días.
7. **Rostrum:** no se publica.
8. **Estado:** `estado-direccion/direccion-general`.
9. **Términos (versión 1.6):**
   > Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

   José Francisco Ñáñez los aceptó el 2026-10-26. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-assistant-1.4.2-2026-10-26.md` y en su `.pdf`.

**Marca `_CRITERIO_DIRECCION.txt`:** no la dejé, porque nadie dio un sí explícito.

**Configuración:** escrita en `.criterio/direccion/direccion-general/config.json` y validada sin problemas.

Procesé 5 sesiones, 7 correos y 1 itinerario, y escribí sus fichas. En la agenda hay cruces, un vuelo que no está anotado, una sesión sin acta y una sesión del consejo sin material.

---

# La semana · Cadena del Norte · al 2026-10-26 · oficina de Dirección general

**Entidad:** Cadena del Norte · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 1.4.2 · **Comando:** `ea-agenda`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-10-29: «Sesión de la junta» (14:00–17:00) se cruza con «Visita del supervisor» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 2 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-04: «Reunión con la firma auditora 1» (15:00–16:00) se cruza con «Visita del cliente 1» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 3 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-05: «Reunión con la firma auditora 2» (15:00–16:00) se cruza con «Visita del cliente 2» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 4 | Dos reuniones del ejecutivo se cruzan en la agenda exportada (`meeting_conflict`) | 2026-11-06: «Reunión con la firma auditora 3» (15:00–16:00) se cruza con «Visita del cliente 3» (15:30–16:30) | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `10-agenda/agenda-2026-10-25.ics` |
| 5 | Una reunión de la agenda cae durante un vuelo del itinerario del ejecutivo (`meeting_during_flight`) | «Cena con proveedores» (2026-11-04 18:30) cae durante el vuelo AM 919, que sale a las 18:00 y llega a las 19:30 | — | — | — | `30-viajes/MTY-itinerario-monterrey.md, línea 9` · `10-agenda/agenda-2026-10-25.ics` |
| 6 | Una reunión presencial en la ciudad del ejecutivo cae mientras el itinerario lo tiene de viaje en otra (`meeting_while_away`) | «Comité de operaciones» (2026-11-03 10:00) es presencial en Ciudad de México (Sala de consejo, corporativo, Ciudad de México) y ese día el viaje a Monterrey sigue | — | — | — | `10-agenda/agenda-2026-10-25.ics` · `30-viajes/MTY-itinerario-monterrey.md` |
| 7 | Pasados los días configurados de una sesión, su acta firmada no está (`meeting_without_minutes`) | comite-de-direccion del 2026-09-21: pasaron 35 días y su acta firmada no está en 40-acta/ | — | — | 35 | `organos/comite-de-direccion/2026-09-21/40-acta/` |
| 8 | A los días configurados de una sesión de un órgano, su material no está en la carpeta (`meeting_without_material`) | consejo-de-administracion del 2026-10-29: faltan 3 días y su material no está en 20-material/ | — | — | 3 | `organos/consejo-de-administracion/2026-10-29/20-material/` |
| 9 | Un vuelo del itinerario no está en la agenda: ese tiempo se ve libre (`trip_not_in_agenda`) | el vuelo AM 902 (Ciudad de México → Monterrey) sale el 2026-11-03 07:00 y no está en la agenda: ese tiempo se ve libre | — | — | — | `30-viajes/MTY-itinerario-monterrey.md, línea 8` |

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
| 2026-11-03 10:00 | 11:00 | Comité de operaciones |
| 2026-11-03 12:00 | 14:00 | Visita al centro de distribución |
| 2026-11-04 15:00 | 16:00 | Reunión con la firma auditora 1 |
| 2026-11-04 15:30 | 16:30 | Visita del cliente 1 |
| 2026-11-04 18:00 | 19:30 | Vuelo AM 919 Monterrey–Ciudad de México |
| 2026-11-04 18:30 | 20:00 | Cena con proveedores |
| 2026-11-05 15:00 | 16:00 | Reunión con la firma auditora 2 |
| 2026-11-05 15:30 | 16:30 | Visita del cliente 2 |
| 2026-11-06 15:00 | 16:00 | Reunión con la firma auditora 3 |
| 2026-11-06 15:30 | 16:30 | Visita del cliente 3 |

| Órgano | Sesión | Días | Material | Acta |
|---|---|---|---|---|
| comite-de-direccion | 2026-09-21 | -35 | 1 | no |
| comite-de-direccion | 2026-10-05 | -21 | 3 | sí |
| comite-de-direccion | 2026-10-19 | -7 | 1 | no |
| consejo-de-administracion | 2026-09-24 | -32 | 2 | sí |
| consejo-de-administracion | 2026-10-29 | 3 | no | no |

| Viaje | Vuelo | Ruta | Sale | Llega | En la agenda |
|---|---|---|---|---|---|
| Monterrey | AM 902 | Ciudad de México → Monterrey | 2026-11-03 07:00 | 08:30 | no |
| Monterrey | AM 919 | Monterrey → Ciudad de México | 2026-11-04 18:00 | 19:30 | sí |

No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-agenda/agenda-2026-10-25.ics`
- `30-viajes/MTY-itinerario-monterrey.md`
- `30-viajes/MTY-itinerario-monterrey.md, línea 8`
- `30-viajes/MTY-itinerario-monterrey.md, línea 9`
- `organos/comite-de-direccion/2026-09-21/40-acta/`
- `organos/consejo-de-administracion/2026-10-29/20-material/`

---

**Reloj:** no creé ninguna tarea programada, porque nadie dio un sí explícito. Se corre a mano con `/criterio-assistant:ea-wake`.
**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-10-26-ea-setup-1`, con 39 hallazgos. Lo que mostré está en `estado-direccion/direccion-general/corridas/salida-ea-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.