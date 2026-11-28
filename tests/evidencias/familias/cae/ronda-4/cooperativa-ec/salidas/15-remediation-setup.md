# /criterio-remediation:remediation-setup auditoria/1791234567001-cooperativa-de-ahorro-chimborazo-sintetica

Soy Remedios. Llevo cada hallazgo hasta su cierre, con su evidencia; no cierro nada ni acepto riesgos.

Remedios ya está configurada para la Cooperativa de Ahorro Chimborazo Sintética. El motor marcó 7 señales en noviembre de 2026; el reporte de abajo muestra las 3 que tocan a los planes de acción.

**Carpeta:** encontré una sola, ya marcada con `_CRITERIO_AUDITORIA.txt`:
1. `auditoria/1791234567001-cooperativa-de-ahorro-chimborazo-sintetica`: Cooperativa de Ahorro Chimborazo Sintética, RUC 1791234567001; tiene 00-referencia/, 10-plan/, 20-trabajos/ y 30-seguimiento/.

Tomé esa (respuesta sugerida). Como ya estaba marcada, no pregunté por la marca.

**Respuestas tomadas de los documentos y de la configuración de Prudencia y Justo** (todas eran la respuesta sugerida):
- **Entidad:** Cooperativa de Ahorro Chimborazo Sintética, RUC 1791234567001, Ecuador, en USD.
- **Periodo:** 2026-11.
- **Cuántas veces se puede correr la fecha de un plan:** 2. Lo dice `00-referencia/metodologia-de-auditoria.pdf`, sección Seguimiento: «hasta dos veces».
- **Publicar en Rostrum:** no, porque los papeles de la auditoría son de la función.
- **Dónde guardo lo que encuentro:** `estado-auditoria/1791234567001-cooperativa-de-ahorro-chimborazo-sintetica`.

**Términos (versión 1.6):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-24.
- **Comprobante:** `.criterio/terminos/aceptacion-criterio-remediation-1.1.0-2026-11-24.md` y su `.pdf`.
- **Configuración:** `.criterio/seguimiento/1791234567001/config.json`.

**Primera ficha (2026-11):** procesé `30-seguimiento/` y encontré:
- Una evidencia: H-20, el procedimiento de desembolso actualizado.
- Dos hallazgos del informe del revisor fiscal: RF-01 y RF-02.
- Ninguna explicación de atraso.

Las otras 4 señales son el cierre sin evidencia, el riesgo aceptado sin escalar, el hallazgo externo que no está en el registro y el hallazgo que vuelve. Las detallan `/criterio-remediation:closure-check` y `/criterio-remediation:committee-brief`.

# Los planes contra su fecha · Cooperativa de Ahorro Chimborazo Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Chimborazo Sintética (1791234567001) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 1.1.0 · **Comando:** `action-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un plan de acción pasó su fecha sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) (`action_plan_overdue`) | H-03 · Cuentas privilegiadas sin revisión trimestral: venció el 2026-09-30 sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) | — | Gerencia de tecnología | 55 | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |
| 2 | Un hallazgo comunicado no tiene plan de acción, responsable o fecha (norma 15.1) (`action_plan_missing`) | H-02 · Avalúos con más de tres años sin actualizar: comunicado el 2026-04-30 y sin responsable (norma 15.1) | — | — | — | `30-seguimiento/registro_hallazgos.xlsx` fila 4 |
| 3 | La fecha de un plan se corrió más veces de las que permite la metodología (`due_date_extended_repeatedly`) | H-03 · Cuentas privilegiadas sin revisión trimestral: su fecha se corrió 3 veces y la metodología permite 2 | — | Gerencia de tecnología | — | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |

## El resultado

**Reprogramaciones que permite la metodología:** 2.

| Hallazgo | Trabajo | Prioridad | Responsable | Fecha | Reprogramaciones | Evidencias |
|---|---|---|---|---|---|---|
| H-01 | TR-01 | Alta | Gerencia de crédito | 2026-12-31 | 0 | 0 |
| H-02 | TR-01 | Media | — | 2026-12-15 | 0 | 0 |
| H-03 | TR-02 | Media | Gerencia de tecnología | 2026-09-30 | 3 | 0 |
| RF-01 | — | Media | Gestión humana | 2026-12-31 | 0 | 0 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-seguimiento/registro_hallazgos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión nadie lo dio. Para correrlo a mano: `/criterio-remediation:remediation-wake`.

La corrida quedó registrada como `2026-11-24-remediation-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.