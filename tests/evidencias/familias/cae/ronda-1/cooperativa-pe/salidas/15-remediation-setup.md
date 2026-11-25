# /criterio-remediation:remediation-setup auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica

Soy Remedios. Llevo cada hallazgo hasta su cierre, con su evidencia; no cierro nada ni acepto riesgos.

Remedios quedó instalada sobre la cooperativa y la primera revisión de los planes de acción encontró dos casos que atender: el plan del H-03 venció y el H-02 no tiene responsable.

**La carpeta.** Encontré una sola candidata:

1. `auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica`: ya tiene la marca `_CRITERIO_AUDITORIA.txt` (Cooperativa de Ahorro Altiplano Sintética · RUC 20601777321) y las cuatro carpetas, de `00-referencia/` a `30-seguimiento/`.

Tomé esa. Como ya estaba marcada, no volví a marcarla.

**Las respuestas.** Las tomé de los documentos y de lo que ya habían fijado los setups de Prudencia y de Justo:
- **Entidad:** Cooperativa de Ahorro Altiplano Sintética, RUC 20601777321, Perú (PEN). Periodo 2026-11.
- **Reprogramaciones permitidas: 2.** La metodología, en su sección «Seguimiento», dice que la fecha de un plan de acción se puede correr hasta dos veces.
- **Quién valida un cierre:** auditoría, con la evidencia de su implementación, según la misma sección. La configuración no tiene un campo para esto, así que quedó dicho en la salida de la corrida.
- **Alta dirección y consejo:** ningún documento los nombra. No los inventé, y la configuración tampoco tiene un campo para ellos. Mientras la organización no lo diga, no se puede revisar si un riesgo aceptado llegó a quien debía llegar.
- **Publicar en Rostrum:** no.
- **Dónde guardo lo que encuentro:** `estado-auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica`.
- **Estructura:** el inventario sugiere mover `informe_revisor_fiscal_2026.pdf` a `20-trabajos/` y `riesgos_aceptados.xlsx` a `10-plan/`. La guía de la estructura los pone en `30-seguimiento/`, que es donde están. No moví nada y los procesé ahí.

**Términos** (versión 1.6), mostrados tal cual:

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-24. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-remediation-0.1.0-2026-11-24.md`, con su copia en `.pdf`.

**Configuración:** quedó en `.criterio/seguimiento/20601777321/config.json` y se validó sin problemas.

**La primera ficha.** Procesé los 5 documentos de `30-seguimiento/`. A la ficha fueron 2 evidencias (H-20 y H-21) y 2 hallazgos del informe del revisor fiscal (RF-01 y RF-02). El cálculo del periodo trae además dos señales que no salen en este reporte: un hallazgo externo que no está en el registro y un hallazgo que vuelve en el mismo proceso. Las muestran `closure-check` y `committee-brief`.

# Los planes contra su fecha · Cooperativa de Ahorro Altiplano Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Altiplano Sintética (20601777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.1.0 · **Comando:** `action-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un plan de acción pasó su fecha sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) (`action_plan_overdue`) | H-03 · Cuentas privilegiadas sin revisión trimestral: venció el 2026-09-30 sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) | — | Gerencia de tecnología | 55 | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |
| 2 | Un hallazgo comunicado no tiene plan de acción, responsable o fecha (norma 15.1) (`action_plan_missing`) | H-02 · Avalúos con más de tres años sin actualizar: comunicado el 2026-04-30 y sin responsable (norma 15.1) | — | — | — | `30-seguimiento/registro_hallazgos.xlsx` fila 4 |

## El resultado

**Reprogramaciones que permite la metodología:** 2.

| Hallazgo | Trabajo | Prioridad | Responsable | Fecha | Reprogramaciones | Evidencias |
|---|---|---|---|---|---|---|
| H-01 | TR-01 | Alta | Gerencia de crédito | 2026-12-31 | 0 | 0 |
| H-02 | TR-01 | Media | — | 2026-12-15 | 0 | 0 |
| H-03 | TR-02 | Media | Gerencia de tecnología | 2026-09-30 | 2 | 0 |
| RF-01 | — | Media | Gestión humana | 2026-12-31 | 0 | 0 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-seguimiento/registro_hallazgos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. Una tarea programada necesita un sí explícito y en esta sesión nadie lo dio. Para correrlo a mano: `/criterio-remediation:remediation-wake`.

La corrida quedó registrada como `2026-11-24-remediation-setup-1`, y su salida en `estado-auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica/corridas/salida-remediation-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.