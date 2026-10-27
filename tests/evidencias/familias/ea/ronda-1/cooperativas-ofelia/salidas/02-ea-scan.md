# /criterio-assistant:ea-scan 

La exportación de la agenda es más vieja que el umbral configurado, así que el motor no calculó cruces. Las fichas de las sesiones y de los tres correos de la oficina están escritas; la carpeta personal quedó fuera, como indica la configuración.
Las notas del comité de gerencia traen un compromiso que no pasó a ninguna ficha, porque los compromisos salen del acta firmada y esa sesión solo tiene borrador.

# Procesar · Cooperativa Sierra Alta · al 2026-10-26 · oficina de Gerencia general

**Entidad:** Cooperativa Sierra Alta · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 0.11.0 · **Comando:** `ea-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un compromiso venció y ningún documento lo sostiene como cumplido (`commitment_overdue`) | consejo-de-administracion del 2026-09-24, C-1: «Presentar el informe de cartera vencida» de Verónica Paz venció el 2026-10-15 y ningún documento lo sostiene como cumplido | — | Verónica Paz | 11 | `organos/consejo-de-administracion/2026-09-24/40-acta/acta-firmada.md, línea 14` |
| 2 | Un correo guardado pide respuesta y su plazo venció sin una respuesta guardada (`correspondence_unanswered`) | oficios@supervisor.test: «Requerimiento 45: cartera reestructurada» pidió respuesta para el 2026-10-20 y no hay una respuesta guardada | — | — | 6 | `20-correspondencia/2026-10-08-supervisor.eml` |
| 3 | Pasados los días configurados de una sesión, su acta firmada no está (`meeting_without_minutes`) | comite-de-gerencia del 2026-09-21: pasaron 35 días y su acta firmada no está en 40-acta/ (lo que hay es un borrador) | — | — | 35 | `organos/comite-de-gerencia/2026-09-21/40-acta/` |
| 4 | Un acuerdo del acta no tiene responsable (`agreement_without_owner`) | consejo-de-administracion del 2026-09-24, A-2: «Actualizar la política de viajes» no tiene responsable | — | — | — | `organos/consejo-de-administracion/2026-09-24/40-acta/acta-firmada.md, punto 2` |

## El resultado

Carpetas excluidas, que no se procesaron: `20-correspondencia/personal`.
No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `organos/comite-de-gerencia/2026-09-21/40-acta/acta-BORRADOR.md`: un borrador en 40-acta/ no es el acta: el acta es la que se firma
- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-correspondencia/2026-10-08-supervisor.eml`
- `organos/comite-de-gerencia/2026-09-21/40-acta/`
- `organos/consejo-de-administracion/2026-09-24/40-acta/acta-firmada.md, línea 14`
- `organos/consejo-de-administracion/2026-09-24/40-acta/acta-firmada.md, punto 2`