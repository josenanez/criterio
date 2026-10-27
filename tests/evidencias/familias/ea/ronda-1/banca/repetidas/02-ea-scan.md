# /criterio-assistant:ea-scan 

Términos 1.2 registrados a nombre de José Francisco Ñáñez. Las notas del comité de presidencia no son acta firmada, así que sus compromisos esperan el acta. El motor de agenda sí procesó el archivo `.ics`, aunque el inventario lo listó como no soportado.

# Procesar · Banco Andino · al 2026-10-26 · oficina de Presidencia

**Entidad:** Banco Andino · **Fecha de corte:** 2026-10-26 · **Agente:** Ofelia 0.11.0 · **Comando:** `ea-scan`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | `commitment_overdue` | Junta directiva 2026-09-24, C-1: «Presentar el informe de cartera vencida» venció el 2026-10-15 y ningún documento lo sostiene como cumplido | Felipe Duarte | 11 | `acta-firmada.md, Compromisos, primer punto` |
| 2 | `correspondence_unanswered` | El supervisor, «Requerimiento 45: cartera reestructurada», pidió respuesta para el 2026-10-20 y no hay respuesta guardada | — | 6 | `20-correspondencia/2026-10-08-supervisor.eml` |
| 3 | `meeting_conflict` | 2026-10-29: «Sesión de la junta» (14:00–17:00) se cruza con «Visita del supervisor» (15:30–16:30) | — | — | `10-agenda/agenda-2026-10-25.ics` |
| 4 | `meeting_conflict` | 2026-11-03: «Llamada con la casa matriz» (09:00–10:00) se cruza con «Revisión con tesorería» (09:00–09:30) | — | — | `10-agenda/agenda-2026-10-25.ics` |
| 5 | `meeting_without_minutes` | Comité de presidencia 2026-09-21: pasaron 35 días y su acta firmada no está en 40-acta/ | — | 35 | `organos/comite-de-presidencia/2026-09-21/40-acta/` |
| 6 | `decision_deadline` | Junta directiva, D-1 «Proveedor del centro de datos alterno»: plazo el 2026-11-02, en 7 días, sigue pendiente | — | 7 | `propuesta-centro-de-datos.md: «La oferta del proveedor actual vence el 2026-11-02»` |
| 7 | `meeting_without_material` | Junta directiva 2026-10-29: faltan 3 días y su material no está en 20-material/ | — | 3 | `organos/junta-directiva/2026-10-29/20-material/` |
| 8 | `commitment_rescheduled` | Junta directiva 2026-09-24, C-2: «Entregar el plan de continuidad del negocio» se movió 3 veces (2026-10-15, 2026-10-30, 2026-11-20) | Andrés Vela | — | `acta-firmada.md, Compromisos, segundo punto` |
| 9 | `agreement_without_date` | A-3: «Contratar la auditoría del sistema de pagos» no tiene fecha | — | — | `acta-firmada.md, Acuerdos, punto 3: «Fecha: por definir»` |
| 10 | `agreement_without_owner` | A-2: «Actualizar la política de viajes» no tiene responsable | — | — | `acta-firmada.md, Acuerdos, punto 2: «sin responsable en el acta»` |

## El resultado

No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar

- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-agenda/agenda-2026-10-25.ics`
- `20-correspondencia/2026-10-08-supervisor.eml`
- `organos/comite-de-presidencia/2026-09-21/40-acta/`
- `organos/junta-directiva/2026-09-24/20-material/propuesta-centro-de-datos.md`
- `organos/junta-directiva/2026-09-24/40-acta/acta-firmada.md` (acuerdos 2 y 3, compromisos 1 y 2)
- `organos/junta-directiva/2026-10-29/20-material/`

La corrida quedó registrada como `2026-10-26-ea-scan-1`. El cálculo no devolvió `record_issues`.