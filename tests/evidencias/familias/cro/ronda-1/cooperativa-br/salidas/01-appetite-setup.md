# /criterio-risk-appetite:appetite-setup riesgos/12345678000190-cooperativa-vale-sintetica

Severo ya está listo para la Cooperativa Vale Sintética, con octubre de 2026 como el último periodo cerrado. Acepté los términos a nombre de José Francisco Ñáñez con fecha 2026-11-25, y el comprobante quedó en `.criterio/terminos/aceptacion-criterio-risk-appetite-0.1.0-2026-11-25.md` y en su `.pdf`. También dejé la marca `_CRITERIO_RIESGOS.txt` en la carpeta.

- **Ficha del periodo:** lleva la revisión de la declaración por la junta del 2025-08-28 y el exceso de L-04 que aprobó el comité hasta el 2027-01-31. Lo de L-03 no va como aprobación, porque el acta solo dice que el comité «toma conhecimento» del plan.
- **Lo que no muestra este reporte:** el cálculo encontró dos señales más, la declaración que la junta no revisó a tiempo y un límite sin dueño. Salen con `/criterio-risk-appetite:framework-check`.

# Cada exposición contra su límite · Cooperativa Vale Sintética · periodo 2026-10

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `limit-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Índice de liquidez de curto prazo: Tesouraria reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesouraria | 8 | `10-exposicion/exposicao_2026-10.xlsx` fila 3 |

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Carteira vencida de crédito pessoal | máximo 6 % | 5.8 | no | — | Crédito | 2026-11-06 |
| L-02 | Índice de liquidez de curto prazo | mínimo 120 % | 131 | no | — | Tesouraria | 2026-11-18 |
| L-03 | Concentração no maior devedor | máximo 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Perdas por fraude externa sobre receitas | máximo 0.5 % | 0.62 | sí | aprobado | Operações | 2026-11-07 |
| L-05 | Exposição a contrapartes sem rating | máximo 15 % | 12 | no | — | Tesouraria | 2026-11-09 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-exposicion/exposicao_2026-10.xlsx`
- Fuentes técnicas: F-01, F-12 (families/criterio-cro/FUENTES.es.md)

---

**Revisión diaria:** te ofrecí una tarea programada para que Severo revise solo, los días hábiles a las 7:00. Para crearla hace falta un sí explícito, y en esta prueba no lo hubo, así que no la creé. A mano se corre con `/criterio-risk-appetite:appetite-wake`.

**Cuándo vuelvo:** sin reloj.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.