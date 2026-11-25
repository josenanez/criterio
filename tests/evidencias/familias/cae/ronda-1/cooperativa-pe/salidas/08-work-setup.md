# /criterio-audit-work:work-setup auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica

Soy Justo. Pongo cada hallazgo al lado de su criterio y de su papel, y cada informe al lado de sus papeles; no cambio prioridades ni firmo informes.

**Carpeta.** Solo hay una candidata, así que la tomé: `auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica`. Ya tenía la marca `_CRITERIO_AUDITORIA.txt` y tiene las cuatro carpetas: `00-referencia/`, `10-plan/`, `20-trabajos/` y `30-seguimiento/`. No hice otra marca.

**Las respuestas que tomé** (de la configuración de Prudencia y de la metodología, una línea cada una):
- **Entidad:** Cooperativa de Ahorro Altiplano Sintética, RUC 20601777321, Perú, en soles (PEN).
- **Periodo:** 2026-11.
- **Escala de prioridad:** Alta desde 15, Media desde 8 y Baja desde 1, según la sección «Escala de prioridad de los hallazgos» de la metodología.
- **Quién aprueba:** el comité de auditoría aprueba el plan, según el estatuto. La jefa de auditoría aprobó los programas de TR-01 y TR-02. La metodología no dice quién aprueba los programas ni los papeles.
- **Rostrum:** no se publica nada ahí.
- **Dónde guardo lo que encuentro:** `estado-auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica`.
- **Archivos fuera de su carpeta** (es solo una sugerencia; no moví nada):
  - `30-seguimiento/informe_revisor_fiscal_2026.pdf` iría en `20-trabajos/`.
  - `30-seguimiento/riesgos_aceptados.xlsx` iría en `10-plan/`.

**Términos, versión 1.6:**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-24. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-audit-work-0.1.0-2026-11-24.md` y en el `.pdf` del mismo nombre. La configuración quedó en `.criterio/trabajos/20601777321/config.json`.

Procesé los 15 documentos de `20-trabajos/` y crucé los 3 hallazgos de los 2 trabajos contra sus papeles. El motor levantó 4 señales en total. Este reporte trae solo una, la del hallazgo al que le falta un elemento. Las otras tres son de tipo distinto: un informe que no coincide con sus papeles, un paso del programa sin ejecutar y un papel sin revisar.

---

# Cada hallazgo y sus elementos · Cooperativa de Ahorro Altiplano Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Altiplano Sintética (20601777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.1.0 · **Comando:** `finding-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un hallazgo no tiene su criterio, su condición, su efecto o su prioridad, o no tiene su causa raíz ni la razón por la que no se pudo identificar (normas 14.2 y 14.3) (`finding_element_missing`) | TR-01 · H-01: le falta la causa raíz ni la razón por la que no se pudo identificar (normas 14.2 y 14.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/PT-03.pdf` |

## El resultado

**Escala de la metodología:** alta desde 15, media desde 8, baja desde 1 (impacto por probabilidad).

| Trabajo | Hallazgo | Prioridad | La de la metodología | Le falta | Papeles |
|---|---|---|---|---|---|
| TR-01 | H-01 | Alta | alta | la causa raíz ni la razón por la que no se pudo identificar | PT-03 |
| TR-01 | H-02 | Media | media | — | PT-02 |
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

**Cuándo vuelvo:** sin reloj. No creé la tarea diaria porque eso pide un sí explícito y en esta sesión nadie respondió. Para correrlo a mano: `/criterio-audit-work:work-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.