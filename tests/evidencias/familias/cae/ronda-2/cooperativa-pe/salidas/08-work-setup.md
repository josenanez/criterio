# /criterio-audit-work:work-setup auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica

Soy Justo. Pongo cada hallazgo al lado de su criterio y de su papel, y cada informe al lado de sus papeles; no cambio prioridades ni firmo informes.

**La carpeta:** hay una sola candidata y ya tiene la marca `_CRITERIO_AUDITORIA.txt`. Es `auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica` y tiene 00-referencia/, 10-plan/, 20-trabajos/ y 30-seguimiento/. Trabajo sobre esa y no la vuelvo a marcar.

**Esto ya se respondió en el setup de Prudencia. Como es una prueba y nadie responde, tomé cada respuesta propuesta:**
- **Entidad:** Cooperativa de Ahorro Altiplano Sintética, RUC 20601777321, Perú, en soles (PEN).
- **Periodo:** 2026-11.
- **Escala de prioridad:** alta desde 15, media desde 8 y baja desde 1, según el impacto por la probabilidad, cada uno de 1 a 5. Sale de la metodología (`00-referencia/metodologia-de-auditoria.pdf`, sección «Escala de prioridad de los hallazgos»).
- **Quién aprueba:** la jefa de auditoría aprueba el programa y los papeles, según las aprobaciones de TR-01 y TR-02 y los índices de papeles. El comité de auditoría aprueba el plan y sus cambios, según el estatuto.
- **Publicar en Rostrum:** no, porque los papeles son de la función de auditoría.
- **Dónde guardo lo que encuentro:** `estado-auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica`.

**Términos (versión 1.6, del 2026-11-16):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-24. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-audit-work-0.2.2-2026-11-24.md` y en el `.pdf` del mismo nombre. La configuración quedó en `.criterio/trabajos/20601777321/config.json`.

---

Procesé los 15 documentos de `20-trabajos/` y llevé a la ficha de 2026-11 los dos trabajos, TR-01 y TR-02, con los tres hallazgos de sus papeles. Este reporte solo revisa los elementos de cada hallazgo. El motor encontró otras señales en el periodo:
- el informe no coincide con los papeles: `/criterio-audit-work:report-check`
- hay papeles sin revisar y pasos sin ejecutar: `/criterio-audit-work:workpaper-check`
- hay una señal de objetividad: `/criterio-audit-work:objectivity-check`

# Cada hallazgo y sus elementos · Cooperativa de Ahorro Altiplano Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Altiplano Sintética (20601777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.2.2 · **Comando:** `finding-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un hallazgo no tiene su criterio, su condición, su efecto o su prioridad, o no tiene su causa raíz ni la razón por la que no se pudo identificar (normas 14.2 y 14.3) (`finding_element_missing`) | TR-01 · H-01: le falta la causa raíz ni la razón por la que no se pudo identificar (normas 14.2 y 14.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/PT-03.pdf` |
| 2 | La prioridad de un hallazgo no es la que da la metodología para su impacto y su probabilidad (norma 14.3) (`rating_inconsistent`) | TR-01 · H-01: prioridad «Media»; con impacto 4 y probabilidad 4 la metodología da «alta» (norma 14.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/PT-03.pdf` |

## El resultado

**Escala de la metodología:** alta desde 15, media desde 8, baja desde 1 (impacto por probabilidad).

| Trabajo | Hallazgo | Prioridad | La de la metodología | Le falta | Papeles |
|---|---|---|---|---|---|
| TR-01 | H-01 | Media | alta | la causa raíz ni la razón por la que no se pudo identificar | PT-03 |
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

---

**El reloj:** te propongo una tarea programada los días hábiles a las 7:00 para que Justo revise solo lo que toca cada día. Si no le toca nada, se calla; solo procesa y escribe en el estado de Criterio y no envía nada. La tarea pide un sí explícito y en esta prueba no hubo, así que no la creé. A mano se corre con `/criterio-audit-work:work-wake`.

**Cuándo vuelvo:** sin reloj.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.