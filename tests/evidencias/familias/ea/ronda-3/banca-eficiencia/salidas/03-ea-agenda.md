# /criterio-assistant:ea-agenda 

Corrí la agenda de Presidencia (Banco Andino) con corte al 2026-10-26. Los términos ya estaban vigentes (versión 1.5, aceptada con la 1.2.3), así que no registré ninguna aceptación nueva.

**El reporte, tal cual lo escribió el motor:**

# La semana · Banco Andino · al 2026-10-26 · oficina de Presidencia

**Entidad:** Banco Andino · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 1.2.3 · **Comando:** `ea-agenda`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Cruce en la agenda | 2026-10-29: «Sesión de la junta» (14:00–17:00) con «Visita del supervisor» (15:30–16:30) | `10-agenda/agenda-2026-10-25.ics` |
| 2 | Cruce | 2026-11-03: «Reunión con la firma auditora 4» (15:00–16:00) con «Visita del cliente 4» (15:30–16:30) | ídem |
| 3 | Cruce | 2026-11-03: «Llamada con la casa matriz» (09:00–10:00) con «Revisión con tesorería» (09:00–09:30) | ídem |
| 4 | Cruce | 2026-11-04: «Reunión con la firma auditora 1» (15:00–16:00) con «Visita del cliente 1» (15:30–16:30) | ídem |
| 5 | Cruce | 2026-11-05: «Reunión con la firma auditora 2» (15:00–16:00) con «Visita del cliente 2» (15:30–16:30) | ídem |
| 6 | Cruce | 2026-11-06: «Reunión con la firma auditora 3» (15:00–16:00) con «Visita del cliente 3» (15:30–16:30) | ídem |
| 7 | Reunión durante un vuelo | «Llamada con la calificadora» (2026-10-27 19:15) cae durante el vuelo AV 9217 (sale 19:00, llega 20:00) | `30-viajes/MDE-itinerario-medellin.md, línea 9` |
| 8 | Reunión durante un vuelo | «Cena de la junta del gremio» (2026-11-05 18:30) cae durante el vuelo AV 9342 (sale 18:00, llega 19:35) | `30-viajes/UIO-itinerario-quito.md, línea 9` |
| 9 | Presencial en Bogotá con viaje en curso | «Reunión con el sindicato» (2026-10-27 11:00); ese día el viaje a Medellín sigue | `30-viajes/MDE-itinerario-medellin.md` |
| 10 | Presencial en Bogotá con viaje en curso | «Visita a la oficina principal» (2026-10-28 14:00); ese día el viaje a Cali sigue | `30-viajes/CLO-itinerario-cali.md` |
| 11 | Presencial en Bogotá con viaje en curso | «Comité de riesgos» (2026-11-04 10:00); ese día el viaje a Quito sigue | `30-viajes/UIO-itinerario-quito.md` |
| 12 | Sesión sin acta | comite-de-presidencia del 2026-09-21: pasaron 35 días y su acta firmada no está en 40-acta/ | `organos/comite-de-presidencia/2026-09-21/40-acta/` |
| 13 | Sesión sin material | junta-directiva del 2026-10-29: faltan 3 días y su material no está en 20-material/ | `organos/junta-directiva/2026-10-29/20-material/` |
| 14 | Vuelo fuera de la agenda | AV 9210 (Bogotá → Medellín), 2026-10-27 06:00 | `30-viajes/MDE-itinerario-medellin.md, línea 8` |
| 15 | Vuelo fuera de la agenda | AV 9341 (Bogotá → Quito), 2026-11-03 06:00 | `30-viajes/UIO-itinerario-quito.md, línea 8` |
| 16 | Vuelo fuera de la agenda | AV 9520 (Bogotá → Cali), 2026-10-28 06:30 | `30-viajes/CLO-itinerario-cali.md, línea 8` |
| 17 | Vuelo fuera de la agenda | AV 9527 (Cali → Bogotá), 2026-10-28 20:00 | `30-viajes/CLO-itinerario-cali.md, línea 9` |

(Resumí las columnas de monto, responsable y días, que van vacías salvo en las filas 12 y 13. El reporte completo, con la tabla de la agenda, la de sesiones y la de vuelos, está en `estado-direccion/presidencia/reporte-ea-agenda.md`.)

**Sesiones de los órganos** (columnas Días / Material / Acta):
- comite-de-presidencia, 2026-09-21: -35 / 1 / no.
- comite-de-presidencia, 2026-10-05: -21 / 3 / sí.
- comite-de-presidencia, 2026-10-19: -7 / 1 / no.
- junta-directiva, 2026-09-24: -32 / 2 / sí.
- junta-directiva, 2026-10-29: 3 / no / no.

**Lo que no se pudo procesar:** `90-borradores/LEEME.txt`, un archivo en 90-borradores/ sin «BORRADOR» en el nombre.

**Preguntas que hizo:** ninguna en esta corrida.

**Corrida registrada:** copié el reporte completo a `estado-direccion/presidencia/corridas/salida-ea-agenda.md`. La corrida quedó como `2026-10-26-ea-agenda-1`, con 50 hallazgos.

- **Sesión sin acta (señal 12):** además de la del 2026-09-21, la tabla de sesiones muestra «Acta: no» para el comité del 2026-10-19. El motor no la marcó como señal.
- **Rostrum:** no se publica allí, porque la configuración lo dice así.