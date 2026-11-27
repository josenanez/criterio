# /criterio-changes:incident-check 

Dos incidentes mayores del periodo siguen sin su causa en el plazo de la política: INC-610 (sin registro de problema) e INC-620 (su problema PRB-620 no tiene causa).

# Cada incidente mayor con su causa · Software Austral Sintético · periodo 2026-11

**Entidad:** Software Austral Sintético (76543210-K) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `incident-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política (`major_incident_without_problem`) | INC-610 · S-02: incidente mayor resuelto el 2026-10-04; no tiene un registro de problema, y la política da 10 días | — | — | 42 | `20-servicio/incidentes_2026-10.xlsx` fila 5 |
| 2 | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política (`major_incident_without_problem`) | INC-620 · S-01: incidente mayor resuelto el 2026-10-12; su problema, PRB-620, no tiene causa, y la política da 10 días | — | — | 34 | `20-servicio/incidentes_2026-10.xlsx` fila 6 · `20-servicio/problemas.xlsx` fila 3 |

## El resultado

**Días de la política para registrar el problema de un incidente mayor:** 10.

| Incidente mayor | Servicio | Resuelto | Problema | Con causa |
|---|---|---|---|---|
| INC-100 | S-01 | 2026-10-03 | PRB-100 | sí |
| INC-101 | S-02 | 2026-11-20 | — | no |
| INC-610 | S-02 | 2026-10-04 | — | no |
| INC-620 | S-01 | 2026-10-12 | PRB-620 | no |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-servicio/incidentes_2026-10.xlsx`
- `20-servicio/problemas.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cto/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-incident-check-1`.