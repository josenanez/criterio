# /criterio-audit-work:work-setup auditoria/BAS0811207K3-banco-del-anahuac-sintetico

Soy Justo. Pongo cada hallazgo al lado de su criterio y de su papel, y cada informe al lado de sus papeles. No cambio prioridades ni firmo informes.

**Carpeta.** Hay una sola candidata y la tomé: `auditoria/BAS0811207K3-banco-del-anahuac-sintetico`. Ya tenía el archivo `_CRITERIO_AUDITORIA.txt` con «Banco del Anáhuac Sintético · RFC BAS0811207K3» y trae `00-referencia/`, `10-plan/`, `20-trabajos/` y `30-seguimiento/`. No la volví a marcar.

**Respuestas que tomé** (la sesión es de prueba y nadie responde, así que salen del setup de Prudencia o de los documentos):
- **Entidad:** Banco del Anáhuac Sintético, RFC BAS0811207K3, México, en pesos (MXN).
- **Periodo:** 2026-11.
- **Escala de prioridad:** alta desde 15, media desde 8 y baja desde 1, según impacto por probabilidad (cada uno de 1 a 5). Sale de `00-referencia/metodologia-de-auditoria.pdf`, sección «Escala de prioridad de los hallazgos».
- **Quién aprueba:** la jefa de auditoría aprueba el programa y los papeles, según la aprobación del programa de TR-01 y TR-02 y los índices de papeles. El comité de auditoría aprueba el plan, según el estatuto.
- **Rostrum:** no se publica, porque los papeles son de la función (decisión 0014).
- **Estado:** `estado-auditoria/BAS0811207K3-banco-del-anahuac-sintetico`.

**Términos (versión 1.6, del 2026-11-16):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-24. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-audit-work-1.0.0-2026-11-24.md` y en su `.pdf`.

**Configuración:** quedó en `.criterio/trabajos/BAS0811207K3/config.json` y el motor la validó sin problemas.

Procesé los 15 documentos de `20-trabajos/` y llevé TR-01 y TR-02 a la ficha. El papel de H-01 no trae causa, así que la dejé vacía. Las demás señales del periodo, sobre papeles, programa, informe y objetividad, salen con `/criterio-audit-work:workpaper-check`, `/criterio-audit-work:report-check` y `/criterio-audit-work:objectivity-check`.

---

# Cada hallazgo y sus elementos · Banco del Anáhuac Sintético · periodo 2026-11

**Entidad:** Banco del Anáhuac Sintético (BAS0811207K3) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 1.0.0 · **Comando:** `finding-check`

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

**Cuándo vuelvo:** sin reloj. No creé la tarea programada porque eso pide un sí explícito y en esta prueba nadie responde. Para correrlo a mano: `/criterio-audit-work:work-wake`.

La corrida quedó registrada como `2026-11-24-work-setup-1`, con esta salida en `estado-auditoria/BAS0811207K3-banco-del-anahuac-sintetico/corridas/salida-work-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.