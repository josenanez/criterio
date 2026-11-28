# /criterio-audit-plan:plan-setup auditoria/1791234567001-cooperativa-de-ahorro-chimborazo-sintetica

Soy Prudencia. Pongo el plan de auditoría al lado de la matriz de riesgos y del universo auditable; no decido qué se audita.

**Carpeta:** encontré una sola candidata, `auditoria/1791234567001-cooperativa-de-ahorro-chimborazo-sintetica`, que tiene 00-referencia/, 10-plan/, 20-trabajos/ y 30-seguimiento/. Es una sesión de prueba, así que la tomé como respuesta sugerida.

**Lo que procesé y lo que tomé como respuesta sugerida:**
- **Entidad:** Cooperativa de Ahorro Chimborazo Sintética, RUC 1791234567001, Ecuador (EC), moneda USD.
- **Periodo:** 2026-11.
- **Ciclos de rotación:** crítico y alto, 12 meses; medio, 24; bajo, 36 (metodología, «Ciclos de rotación»).
- **Desde qué calificación un riesgo es alto:** Alto y Crítico (metodología, «Ciclos de rotación»).
- **Quién aprueba el plan y sus cambios:** el comité de auditoría (estatuto de auditoría).
- **Última evaluación de riesgos:** 2025-09-15. **Última evaluación externa de calidad:** 2021-03-31 (metodología, «Evaluaciones»).
- **Escala de prioridad:** alta desde 15, media desde 8, baja desde 1. **Reprogramaciones permitidas:** 2 (metodología).
- **Publicar en Rostrum:** no, porque los papeles son de la función.
- **Dónde guardo lo que encuentro:** `estado-auditoria/1791234567001-cooperativa-de-ahorro-chimborazo-sintetica`.
- **Marca `_CRITERIO_AUDITORIA.txt` en la carpeta:** sí, y quedó puesta.

**Términos (versión 1.6):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-24. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-audit-plan-1.1.0-2026-11-24.md` y en el `.pdf` del mismo nombre.

**Configuración:** quedó en `.criterio/plan/1791234567001/config.json`.

**La ficha:** procesé el acta 07-2026 del comité de auditoría, que aprueba cancelar TR-05, Tesorería. Es la única acta en `10-plan/actas/`.

**El primer reporte:**
- R-06 es de la unidad U-09, y U-09 no aparece en el universo auditable. U-08, la unidad de TR-07, tampoco está en él.
- El cálculo trajo además señales que este reporte no muestra: un cambio al plan sin acta, un requisito temático, la evaluación externa de calidad, un trabajo atrasado y las horas contra la capacidad. Las muestran /criterio-audit-plan:plan-status, /criterio-audit-plan:quality-status y /criterio-audit-plan:plan-capacity.

# El plan contra los riesgos · Cooperativa de Ahorro Chimborazo Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Chimborazo Sintética (1791234567001) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 1.1.0 · **Comando:** `plan-coverage`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un riesgo calificado alto o crítico en la matriz no tiene un trabajo en el plan dentro del ciclo de la metodología (`high_risk_not_covered`) | R-06 · Pérdida de información de clientes: calificado Crítico en la matriz y ningún trabajo del plan lo cubre (norma 9.4) | — | — | — | `10-plan/matriz_de_riesgos.xlsx` fila 7 |
| 2 | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo (`auditable_unit_overdue`) | U-03 · Tesorería: el último trabajo fue el 2023-03-10, su ciclo de 24 meses venció el 2025-03-10 y no está en el plan | — | — | 624 | `10-plan/universo_auditable.xlsx` fila 4 |
| 3 | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo (`auditable_unit_overdue`) | U-10 · Canales físicos: no tiene un trabajo registrado y no está en el plan; su ciclo es de 36 meses | — | — | — | `10-plan/universo_auditable.xlsx` fila 8 |
| 4 | La evaluación de riesgos que sostiene el plan tiene más de un año (norma 9.4) (`risk_assessment_outdated`) | la evaluación de riesgos que sostiene el plan es del 2025-09-15: tiene 435 días, y la norma 9.4 la pide al menos una vez al año | — | — | 70 | `00-referencia/metodologia-de-auditoria.pdf` |
| 5 | El plan no considera el gobierno de TI, el riesgo de fraude o los programas de cumplimiento y ética, ni dice por qué (norma 9.4) (`plan_area_not_considered`) | el plan no considera los programas de cumplimiento y ética ni dice por qué (norma 9.4) | — | — | — | `10-plan/plan_anual_2026.xlsx` |
| 6 | El plan no considera el gobierno de TI, el riesgo de fraude o los programas de cumplimiento y ética, ni dice por qué (norma 9.4) (`plan_area_not_considered`) | el plan no considera el riesgo de fraude ni dice por qué (norma 9.4) | — | — | — | `10-plan/plan_anual_2026.xlsx` |

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
| el riesgo de fraude | no | — |
| los programas de cumplimiento y ética | no | — |

**Última evaluación de riesgos:** 2025-09-15.

Qué se audita lo decide el responsable de auditoría con el consejo: aquí se dice qué queda sin cubrir.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/metodologia-de-auditoria.pdf`
- `10-plan/matriz_de_riesgos.xlsx`
- `10-plan/plan_anual_2026.xlsx`
- `10-plan/universo_auditable.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj, porque en esta sesión de prueba nadie dio un sí explícito para una tarea programada. Se corre a mano con `/criterio-audit-plan:plan-wake`.

La corrida quedó registrada como `2026-11-24-plan-setup-1`, con lo mostrado en `estado-auditoria/1791234567001-cooperativa-de-ahorro-chimborazo-sintetica/corridas/salida-plan-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.