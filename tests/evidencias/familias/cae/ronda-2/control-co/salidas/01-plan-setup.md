# /criterio-audit-plan:plan-setup auditoria/901888432-banco-control-sintetico

Prudencia quedó lista para Banco Control Sintético (901888432). Procesé el estatuto, la metodología y las dos actas del comité, que quedaron en la ficha del periodo: una cancela TR-05 y la otra agrega TR-06, ambas aprobadas por el comité de auditoría. El comprobante de los términos quedó en `.criterio/terminos/aceptacion-criterio-audit-plan-0.2.2-2026-11-24.md` y su `.pdf`; la configuración, en `.criterio/plan/901888432/config.json`. No dejé la marca `_CRITERIO_AUDITORIA.txt`, porque nadie la autorizó.

# El plan contra los riesgos · Banco Control Sintético · periodo 2026-11

**Entidad:** Banco Control Sintético (901888432) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.2.2 · **Comando:** `plan-coverage`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Riesgo | Calificación | Unidad | Alto | Trabajos que lo cubren |
|---|---|---|---|---|
| R-01 · Pérdida por riesgo de crédito | Alto | U-01 | sí | TR-01 |
| R-02 · Ataque a los canales digitales | Crítico | U-02 | sí | TR-02 |
| R-03 · Fraude en pagos a proveedores | Alto | U-07 | sí | TR-04 |
| R-04 · Lavado de activos | Crítico | U-05 | sí | TR-03 |
| R-05 · Error en la liquidación de nómina | Medio | U-04 | no | TR-06 |

| Unidad | Nivel | Último trabajo | Ciclo | Vence | En el plan |
|---|---|---|---|---|---|
| U-01 · Crédito | Alto | 2025-10-15 | 12 meses | 2026-10-15 | TR-01 |
| U-02 · Tecnología | Alto | 2025-10-01 | 12 meses | 2026-10-01 | TR-02 |
| U-03 · Tesorería | Medio | 2024-12-20 | 24 meses | 2026-12-20 | — |
| U-04 · Nómina | Bajo | 2024-05-01 | 36 meses | 2027-05-01 | TR-06 |
| U-05 · Cumplimiento | Alto | 2025-12-01 | 12 meses | 2026-12-01 | TR-03 |
| U-06 · Proveedores | Medio | 2025-01-15 | 24 meses | 2027-01-15 | — |
| U-10 · Canales físicos | Bajo | 2024-05-01 | 36 meses | 2027-05-01 | — |

| Lo que el plan tiene que considerar (norma 9.4) | Considerado | Por qué no |
|---|---|---|
| el gobierno de TI | sí | — |
| el riesgo de fraude | sí | — |
| los programas de cumplimiento y ética | sí | — |

**Última evaluación de riesgos:** 2025-12-01.

Qué se audita lo decide el responsable de auditoría con el consejo: aquí se dice qué queda sin cubrir.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. No creé la tarea programada porque nadie dio un sí explícito. Para correrlo a mano: `/criterio-audit-plan:plan-wake`.

La corrida quedó registrada como `2026-11-24-plan-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.