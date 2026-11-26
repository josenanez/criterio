# /criterio-risk-appetite:appetite-setup riesgos/12345678000190-cooperativa-vale-sintetica

Soy Severo. Pongo cada exposición al lado de su límite y cada límite al lado de su dueño y su revisión; no apruebo excesos ni cambio límites.

**Carpeta:** 1. `riesgos/12345678000190-cooperativa-vale-sintetica`. Tiene 00-marco/, 10-exposicion/, 20-indicadores/, 30-eventos/ y 40-actas/. Era la única candidata, así que la usé. Tiene 11 documentos y todos están en su carpeta.

**Lo que tomé de los documentos (no se hizo ninguna pregunta):**
- **Entidad:** Cooperativa Vale Sintética · CNPJ 12345678000190 · Brasil (BRL).
- **Último periodo cerrado:** 2026-10, según `exposicao_2026-10.xlsx`.
- **Plazo para reportar la exposición:** 10 días corridos después del cierre (declaração de apetite, p. 1).
- **Revisión de la declaración por el conselho:** cada 12 meses (declaração de apetite, p. 1).
- **Publicar en Rostrum:** sí, porque el marco no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-riesgos/12345678000190-cooperativa-vale-sintetica`.
- **Marca `_CRITERIO_RIESGOS.txt`:** sí, ya está en la carpeta.

**Términos (versión 1.6, del 2026-11-16):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-risk-appetite-0.2.0-2026-11-25.md` y en el `.pdf` con el mismo nombre.
La configuración quedó en `.criterio/apetito/12345678000190/config.json`.

**Ficha 2026-10:**
- La declaração de apetite, con la última revisión del conselho el 2025-08-28.
- Tres excesos que el comitê de riscos aprobó en su sesión del 2026-11-12: L-04, L-06 y L-07.
- Sobre L-03, el acta solo dice que el comitê «toma conocimiento» del plan, así que no lo registré como aprobación.

Hay dos excesos sin plan ni aprobación, L-01 y L-12, los dos de la Diretoria de crédito. Tesouraria reportó dos exposiciones fuera de plazo. El motor también encontró señales en el marco: la declaración, límites sin dueño o con la revisión vencida y riesgos sin límite. Esas las muestran `/criterio-risk-appetite:framework-check` y `/criterio-risk-appetite:coverage-check`.

---

# Cada exposición contra su límite · Cooperativa Vale Sintética · periodo 2026-10

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `limit-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-12 · Carteira vencida imobiliária: la exposición de 2026-10 es 4.6 % y el límite máximo es 4; no hay plan de acción ni aprobación del exceso | 0,60 | Diretoria de crédito | — | `00-marco/limites.xlsx` fila 9 · `10-exposicion/exposicao_2026-10.xlsx` fila 9 |
| 2 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Carteira vencida de crédito pessoal: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0,40 | Diretoria de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicao_2026-10.xlsx` fila 2 |
| 3 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Índice de liquidez de curto prazo: Tesouraria reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesouraria | 8 | `10-exposicion/exposicao_2026-10.xlsx` fila 3 |
| 4 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-42 · Limites de contraparte utilizados: Tesouraria reportó su exposición de 2026-10 el 2026-11-16, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesouraria | 6 | `10-exposicion/exposicao_2026-10.xlsx` fila 12 |

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Carteira vencida de crédito pessoal | máximo 6 % | 6.4 | sí | — | Crédito | 2026-11-06 |
| L-02 | Índice de liquidez de curto prazo | mínimo 120 % | 131 | no | — | Tesouraria | 2026-11-18 |
| L-03 | Concentração no maior devedor | máximo 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Perdas por fraude externa sobre receitas | máximo 0.5 % | 0.62 | sí | aprobado | Operações | 2026-11-07 |
| L-05 | Exposição a contrapartes sem rating | máximo 15 % | 12 | no | — | Tesouraria | 2026-11-09 |
| L-06 | Perdas operacionais sobre o patrimônio | máximo 1 % | 1.1 | sí | aprobado | Operações | 2026-11-08 |
| L-07 | Exposição ao maior banco correspondente | máximo 20 % | 23 | sí | aprobado | Tesouraria | 2026-11-09 |
| L-12 | Carteira vencida imobiliária | máximo 4 % | 4.6 | sí | — | Diretoria de crédito | 2026-11-06 |
| L-22 | Concentração setorial da carteira | máximo 25 % | 21 | no | — | Diretoria de crédito | 2026-11-05 |
| L-32 | Exposição em moeda estrangeira | máximo 20 % | 14 | no | — | Tesouraria | 2026-11-04 |
| L-42 | Limites de contraparte utilizados | máximo 80 % | 62 | no | — | Tesouraria | 2026-11-16 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- `10-exposicion/exposicao_2026-10.xlsx`
- Fuentes técnicas: F-01, F-12 (families/criterio-cro/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. En esta sesión nadie dijo que sí a la tarea programada. Para correrlo a mano: `/criterio-risk-appetite:appetite-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

La corrida quedó registrada como `2026-11-25-appetite-setup-1`. Lo que se mostró está en `estado-riesgos/12345678000190-cooperativa-vale-sintetica/corridas/salida-appetite-setup.md`.