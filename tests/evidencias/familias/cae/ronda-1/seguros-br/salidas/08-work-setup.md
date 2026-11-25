# /criterio-audit-work:work-setup auditoria/31452078000190-seguradora-atlantica-sintetica

Soy Justo. Pongo cada hallazgo al lado de su criterio y de su papel, y cada informe al lado de sus papeles; no cambio prioridades ni firmo informes.

Justo quedó listo para Seguradora Atlântica Sintética. Hay una señal de prioridad: el hallazgo H-01 de TR-01 lleva prioridad «Media», pero la metodología le da «alta».

**Carpeta.** Encontré una sola candidata, `auditoria/31452078000190-seguradora-atlantica-sintetica`, y la tomo: sí. Ya estaba marcada con `_CRITERIO_AUDITORIA.txt` y tiene las cuatro subcarpetas, así que no la marqué de nuevo. Tiene 29 documentos. Hay dos que quizá deberían ir en otra carpeta; no moví nada, es solo una sugerencia:
- `30-seguimiento/informe_revisor_fiscal_2026.pdf` iría en `20-trabajos/`.
- `30-seguimiento/riesgos_aceptados.xlsx` iría en `10-plan/`.

**Respuestas que ya había dado Prudencia y que confirmo:**
- **Entidad:** Seguradora Atlântica Sintética, CNPJ 31452078000190, Brasil, en BRL.
- **Periodo:** 2026-11.
- **Escala de prioridad:** alta desde 15, media desde 8 y baja desde 1, multiplicando impacto por probabilidad. Sale de `metodologia-de-auditoria.pdf`.
- **Quién aprueba el plan:** el comité de auditoría, según el estatuto.
- **Quién aprueba el programa:** la jefa de auditoría, según las aprobaciones de los programas de TR-01 y TR-02. La configuración no tiene un campo para esto, así que lo dejo dicho aquí.
- **Publicar en Rostrum:** no.
- **Dónde guardo lo que encuentro:** `estado-auditoria/31452078000190-seguradora-atlantica-sintetica`.

**Términos (versión 1.6).** Te los muestro tal cual:

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Quedaron aceptados por José Francisco Ñáñez el 2026-11-24. El comprobante está en `.criterio/terminos/aceptacion-criterio-audit-work-0.1.0-2026-11-24.md` y en el `.pdf` del mismo nombre. La configuración está en `.criterio/trabajos/31452078000190/config.json`.

**Primera ficha.** Procesé los 15 documentos de `20-trabajos/` y llevé a la ficha de 2026-11 los trabajos TR-01 y TR-02, con sus 3 hallazgos. El motor encontró 4 señales:
- `rating_inconsistent`: es la que muestra el reporte de abajo.
- `auditor_reviews_own_work`, `finding_without_workpaper` y `work_program_not_approved`: las muestran `/criterio-audit-work:workpaper-check` y `/criterio-audit-work:objectivity-check`.

# Cada hallazgo y sus elementos · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.1.0 · **Comando:** `finding-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La prioridad de un hallazgo no es la que da la metodología para su impacto y su probabilidad (norma 14.3) (`rating_inconsistent`) | TR-01 · H-01: prioridad «Media»; con impacto 4 y probabilidad 4 la metodología da «alta» (norma 14.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/PT-03.pdf` |

## El resultado

**Escala de la metodología:** alta desde 15, media desde 8, baja desde 1 (impacto por probabilidad).

| Trabajo | Hallazgo | Prioridad | La de la metodología | Le falta | Papeles |
|---|---|---|---|---|---|
| TR-01 | H-01 | Media | alta | — | PT-03 |
| TR-01 | H-02 | Media | media | — | PT-09 |
| TR-02 | H-03 | Media | media | — | PT-02 |

La prioridad la pone el auditor: aquí se dice cuándo no es la que da la metodología.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-trabajos/TR-01_credito-comercial/PT-03.pdf`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

**Reloj.** La tarea diaria necesita un sí explícito y en esta sesión nadie podía darlo, así que no la creé. Para correrlo a mano: `/criterio-audit-work:work-wake`.

**Cuándo vuelvo:** sin reloj.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.