# /criterio-changes:incident-check 

Tres incidentes mayores del periodo no tienen su causa dentro del plazo de la política. La decisión sobre cada uno es del área de tecnología.

# Cada incidente mayor con su causa · Banco Meridiano Sintético · periodo 2026-11

**Entidad:** Banco Meridiano Sintético (901222444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `incident-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política (`major_incident_without_problem`) | INC-610 · S-02: incidente mayor resuelto el 2026-10-04; no tiene un registro de problema, y la política da 10 días | — | — | 42 | `20-servicio/incidentes_2026-10.xlsx` fila 5 |
| 2 | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política (`major_incident_without_problem`) | INC-620 · S-01: incidente mayor resuelto el 2026-10-12; su problema, PRB-620, no tiene causa, y la política da 10 días | — | — | 34 | `20-servicio/incidentes_2026-10.xlsx` fila 6 · `20-servicio/problemas.xlsx` fila 3 |
| 3 | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política (`major_incident_without_problem`) | INC-630 · S-03: incidente mayor resuelto el 2026-10-27; no tiene un registro de problema, y la política da 10 días | — | — | 19 | `20-servicio/incidentes_2026-10.xlsx` fila 7 |

## El resultado

**Días de la política para registrar el problema de un incidente mayor:** 10.

| Incidente mayor | Servicio | Resuelto | Problema | Con causa |
|---|---|---|---|---|
| INC-100 | S-01 | 2026-10-03 | PRB-100 | sí |
| INC-101 | S-02 | 2026-11-20 | — | no |
| INC-610 | S-02 | 2026-10-04 | — | no |
| INC-620 | S-01 | 2026-10-12 | PRB-620 | no |
| INC-630 | S-03 | 2026-10-27 | — | no |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-servicio/incidentes_2026-10.xlsx`
- `20-servicio/problemas.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cto/FUENTES.es.md)

---
Los términos ya estaban vigentes (versión 1.6), así que no registré ninguna aceptación. La corrida quedó registrada como `2026-11-25-incident-check-1`, con su salida en `estado-tecnologia/901222444-banco-meridiano-sintetico/corridas/salida-incident-check.md`.