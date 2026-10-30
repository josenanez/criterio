# /criterio-assistant:ea-scan 

La agenda exportada es más vieja que el umbral configurado, así que el motor no calculó cruces con ella, ni de reuniones ni de vuelos. Lo que dicen las notas de las sesiones sin acta firmada no pasó a la ficha: espera el acta.

# Procesar · Cooperativa Sierra Alta · al 2026-10-26 · oficina de Gerencia general

**Entidad:** Cooperativa Sierra Alta · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 0.12.1 · **Comando:** `ea-scan`

## Lo que hay que atender

El reporte completo está en `estado-direccion/gerencia-general/reporte-ea-scan.md` y en `corridas/salida-ea-scan.md`. Son 35 señales:

| Señal | Cuántas | Qué | Cita |
|---|---|---|---|
| `commitment_overdue` | 7 | Seis informes de seguimiento (C-1 a C-6) del comité del 2026-10-05, con plazo entre el 2026-10-12 y el 2026-10-17, y el informe de cartera vencida (C-1) del consejo del 2026-09-24, con plazo el 2026-10-15. Ningún documento los sostiene como cumplidos. | `organos/comite-de-gerencia/2026-10-05/40-acta/acta-firmada.md, líneas 22 a 27`; `organos/consejo-de-administracion/2026-09-24/40-acta/acta-firmada.md, línea 14` |
| `correspondence_unanswered` | 6 | El requerimiento 45 del supervisor (plazo 2026-10-20) y las solicitudes 1 a 5 del proveedor (plazos del 2026-10-20 al 2026-10-24) no tienen respuesta guardada. | `20-correspondencia/2026-10-08-supervisor.eml`; `20-correspondencia/2026-10-14-solicitud-1.eml` a `2026-10-18-solicitud-5.eml` |
| `meeting_without_minutes` | 4 | El comité de gerencia de los días 09-21 (35 días), 09-25 (31), 09-27 (29) y 09-29 (27) no tiene acta firmada. En 40-acta/ del 09-21 solo hay un borrador. | `organos/comite-de-gerencia/<fecha>/40-acta/` |
| `decision_deadline` | 2 | La sede de la oficina regional (D-2) vence el 2026-11-04, en 9 días. El proveedor de la mesa de ayuda (D-1) vence el 2026-11-03, en 8 días. Las dos siguen pendientes. | `…/2026-10-05/20-material/propuesta-2.md, línea 3`; `…/propuesta-1.md, línea 3` |
| `commitment_rescheduled` | 3 | Los planes 7, 8 y 9 de mejora (C-7 a C-9) se movieron 3 veces cada uno. | `…/2026-10-05/40-acta/acta-firmada.md, líneas 28 a 30` |
| `agreement_without_date` | 6 | Los acuerdos A-7 a A-12 del comité del 2026-10-05 no tienen fecha. | `…/acta-firmada.md, puntos 7 a 12` |
| `agreement_without_owner` | 7 | Los acuerdos A-1 a A-6 del comité del 2026-10-05 no tienen responsable. Tampoco lo tiene A-2 del consejo del 2026-09-24, «Actualizar la política de viajes». | `…/2026-10-05/40-acta/acta-firmada.md, puntos 1 a 6`; `…/2026-09-24/40-acta/acta-firmada.md, punto 2` |

## El resultado

- Carpetas excluidas, que no se procesaron: `20-correspondencia/personal`.
- No se publica en Rostrum: así lo dice la configuración.
- No hubo `record_issues` al calcular.

## Lo que no se pudo procesar

- `organos/comite-de-gerencia/2026-09-21/40-acta/acta-BORRADOR.md`: un borrador en 40-acta/ no es el acta, que es la que se firma.
- `90-borradores/LEEME.txt`: está en 90-borradores/ sin «BORRADOR» en el nombre.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

Las citas de cada señal están en la tabla de arriba. El detalle renglón por renglón, con cada acuerdo, compromiso y correo, está en `reporte-ea-scan.md`.

---

**Resumen de la corrida** (`2026-10-26-ea-scan-1`):

- **Fichas escritas:**
  - 8 sesiones en `reuniones/`.
  - 8 correos en `correspondencia/`, sin la respuesta que envió la oficina ni el correo personal.
  - 1 viaje en `viajes/`.
- **Viaje:** el itinerario de Guayaquil (LA 1405 y LA 1412, 3 y 4 de noviembre). No pude cruzarlo con la agenda por la razón de arriba.
- **Qué fue de cada cosa:**
  - La agenda y la colección de fichas nuevas son completas para el estado actual.
  - Los términos (versión 1.3) ya estaban aceptados por José Francisco Ñáñez con fecha 2026-10-26, así que no hubo que registrarlos de nuevo.

Dos aclaraciones sobre lo que dije antes en este turno. Escribí primero una cifra de compromisos y acuerdos en las notas que no era correcta, y la corregí antes de registrar la corrida. Y en el resumen de la corrida, en la nota del motor, conté 9 correos con ficha, pero las fichas son 8; la nota registrada dice 9 por error mío y queda así en `corridas.json`.