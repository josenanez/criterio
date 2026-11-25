# /criterio-audit-plan:plan-setup auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica

Prudencia quedó lista para la Cooperativa de Ahorro Altiplano Sintética (RUC 20601777321), periodo 2026-11. En el plan encontré un riesgo crítico sin un trabajo que lo cubra y dos unidades del universo que pasaron su ciclo de rotación. Este es el reporte tal cual:

# El plan contra los riesgos · Cooperativa de Ahorro Altiplano Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Altiplano Sintética (20601777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.1.0 · **Comando:** `plan-coverage`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un riesgo calificado alto o crítico en la matriz no tiene un trabajo en el plan dentro del ciclo de la metodología (`high_risk_not_covered`) | R-06 · Pérdida de información de clientes: calificado Crítico en la matriz y ningún trabajo del plan lo cubre (norma 9.4) | — | — | — | `10-plan/matriz_de_riesgos.xlsx` fila 7 |
| 2 | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo (`auditable_unit_overdue`) | U-03 · Tesorería: el último trabajo fue el 2023-03-10, su ciclo de 24 meses venció el 2025-03-10 y no está en el plan | — | — | 624 | `10-plan/universo_auditable.xlsx` fila 4 |
| 3 | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo (`auditable_unit_overdue`) | U-10 · Canales físicos: no tiene un trabajo registrado y no está en el plan; su ciclo es de 36 meses | — | — | — | `10-plan/universo_auditable.xlsx` fila 8 |

## El resultado

| Riesgo | Calificación | Unidad | Alto | Trabajos que lo cubren |
|---|---|---|---|---|
| R-01 · Pérdida por riesgo de crédito | Alto | U-01 | sí | TR-01 |
| R-02 · Ataque a los canales digitales | Crítico | U-02 | sí | TR-02 |
| R-03 · Fraude en pagos a proveedores | Alto | U-06 | sí | TR-04 |
| R-04 · Lavado de activos | Crítico | U-05 | sí | TR-03 |
| R-05 · Error en la liquidación de nómina | Medio | U-04 | no | TR-06 |
| R-06 · Pérdida de información de clientes | Crítico | U-09 | sí | — |

| Unidad | Nivel | Último trabajo | Ciclo | Vence | En el plan |
|---|---|---|---|---|---|
| U-01 · Crédito | Alto | 2025-10-15 | 12 meses | 2026-10-15 | TR-01 |
| U-02 · Tecnología | Alto | 2025-10-01 | 12 meses | 2026-10-01 | TR-02 |
| U-03 · Tesorería | Medio | 2023-03-10 | 24 meses | 2025-03-10 | — |
| U-04 · Nómina | Bajo | 2024-05-01 | 36 meses | 2027-05-01 | TR-06 |
| U-05 · Cumplimiento | Alto | 2025-12-01 | 12 meses | 2026-12-01 | TR-03 |
| U-06 · Proveedores | Medio | 2025-01-15 | 24 meses | 2027-01-15 | TR-04 |
| U-10 · Canales físicos | Bajo | — | 36 meses | — | — |

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

- `10-plan/matriz_de_riesgos.xlsx`
- `10-plan/universo_auditable.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

---

**Lo que quedó hecho:**
- **Configuración:** `.criterio/plan/20601777321/config.json`. Todos los valores de la metodología salen del estatuto y de la metodología de `00-referencia/`. Las 12 preguntas se respondieron con la respuesta sugerida, porque nadie podía contestar.
- **Términos:** la versión 1.6 quedó aceptada por José Francisco Ñáñez el 2026-11-24. El comprobante está en `.criterio/terminos/aceptacion-criterio-audit-plan-0.1.0-2026-11-24.md` y `.pdf`.
- **Marca:** `_CRITERIO_AUDITORIA.txt` quedó en la carpeta de la entidad.
- **Ficha:** llevé el acta 07-2026 a la ficha. En ella el comité de auditoría aprueba cancelar TR-05.
- **Otras señales:** `compute` dio 6 señales. Además de las 3 de cobertura, salieron un cambio al plan sin aprobación, un requisito temático faltante y un trabajo atrasado. Esas tres las muestran `/criterio-audit-plan:plan-status` y `/criterio-audit-plan:plan-capacity`.
- **Estructura:** el inventario propone mover dos archivos de `30-seguimiento/`, pero la guía de estructura los ubica justo ahí. Las dos fuentes se contradicen, así que no moví nada.
- **Corrida:** quedó registrada como `2026-11-24-plan-setup-1`.

**Cuándo vuelvo:** sin reloj. Crear la tarea programada pide un sí explícito y en esta prueba no lo hubo. A mano se corre con `/criterio-audit-plan:plan-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.