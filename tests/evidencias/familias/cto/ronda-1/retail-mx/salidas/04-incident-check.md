# /criterio-changes:incident-check 

Tres de los cinco incidentes mayores del periodo 2026-11 no tienen su causa dentro de los 10 días de la política. Los términos están vigentes (versión 1.6). Este comando no pidió registrar ninguna aceptación, así que no registré a José Francisco Ñáñez.

# Cada incidente mayor con su causa · Retail del Golfo Sintético · periodo 2026-11

**Entidad:** Retail del Golfo Sintético (RGS180610QW4) · **Fecha de corte:** 2026-11-25 · **Agente:** Fausto 0.1.0 · **Comando:** `incident-check`

## Lo que hay que atender

| # | Qué | Días | Cita |
|---|---|---|---|
| 1 | INC-610 · S-02: resuelto el 2026-10-04. No tiene registro de problema y la política da 10 días. | 42 | `20-servicio/incidentes_2026-10.xlsx` fila 5 |
| 2 | INC-620 · S-01: resuelto el 2026-10-12. Su problema, PRB-620, no tiene causa. | 34 | `20-servicio/incidentes_2026-10.xlsx` fila 6 · `20-servicio/problemas.xlsx` fila 3 |
| 3 | INC-630 · S-03: resuelto el 2026-10-27. No tiene registro de problema. | 19 | `20-servicio/incidentes_2026-10.xlsx` fila 7 |

## El resultado

| Incidente mayor | Servicio | Resuelto | Problema | Con causa |
|---|---|---|---|---|
| INC-100 | S-01 | 2026-10-03 | PRB-100 | sí |
| INC-101 | S-02 | 2026-11-20 | — | no |
| INC-610 | S-02 | 2026-10-04 | — | no |
| INC-620 | S-01 | 2026-10-12 | PRB-620 | no |
| INC-630 | S-03 | 2026-10-27 | — | no |

INC-101 tampoco tiene problema ni causa, pero el motor no lo señala como vencido.

Todo lo que llegó se procesó, y no hubo preguntas en esta corrida. Las fuentes fueron `20-servicio/incidentes_2026-10.xlsx` y `20-servicio/problemas.xlsx`. La decisión sobre estos incidentes es del comité de cambios y del área de tecnología.

La corrida quedó registrada con el id `2026-11-25-incident-check-1`. Guardé el reporte del motor en `estado-tecnologia/rgs180610qw4-retail-del-golfo-sintetico/cambios/2026-11/reporte-incident-check.md`. La salida, tal cual la vio la persona, está en `estado-tecnologia/rgs180610qw4-retail-del-golfo-sintetico/corridas/salida-incident-check.md`. Esa copia es el reporte del motor, sin este resumen.