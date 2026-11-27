# /criterio-audit-work:work-setup auditoria/901777321-banco-andino-sintetico

Soy Justo. Pongo cada hallazgo al lado de su criterio y de su papel, y cada informe al lado de sus papeles. No cambio prioridades ni firmo informes.

Justo ya está listo para el Banco Andino Sintético, y la primera revisión de hallazgos encontró dos problemas, los dos en el hallazgo H-01 del trabajo TR-01: le falta la causa y su prioridad no es la que da la metodología.

**Carpeta:** había una sola, `auditoria/901777321-banco-andino-sintetico`, y ya estaba marcada con `_CRITERIO_AUDITORIA.txt` para el Banco Andino Sintético · NIT 901777321. La tomé. Encontré 27 documentos, ninguno fuera de lugar ni ilegible.

**No hizo falta preguntar nada nuevo.** Tomé los valores de la configuración de Prudencia y los crucé contra la metodología y el estatuto:
- **Entidad:** Banco Andino Sintético, NIT 901777321, Colombia, en pesos colombianos.
- **Periodo:** 2026-11.
- **Escala de prioridad:** impacto por probabilidad, de 1 a 5 cada uno. Alta desde 15, Media desde 8 y Baja desde 1.
- **Quién aprueba:** el plan lo aprueba el comité de auditoría, según el estatuto. El programa de cada trabajo lo aprueba la jefa de auditoría, según los documentos de aprobación de TR-01 y TR-02.
- **Publicar en Rostrum:** no, porque los papeles son de la función.
- **Estado:** queda en `estado-auditoria/901777321-banco-andino-sintetico`, fuera de los documentos.
- **Marca de la carpeta:** ya estaba, así que no la volví a pedir.

**Términos, versión 1.6:**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-24. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-audit-work-0.2.2-2026-11-24.md` y en `.pdf`.

**Configuración:** quedó en `.criterio/trabajos/901777321/config.json` y el motor la validó sin problemas.

**La primera ficha:** procesé los 15 documentos de `20-trabajos/`, con dos trabajos y tres hallazgos en los papeles.

# Cada hallazgo y sus elementos · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.2.2 · **Comando:** `finding-check`

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

**Las demás señales del cálculo:** el cálculo levantó 8 señales en total; las otras 6 salen en otros reportes:
- Un paso que no se ejecutó, un papel sin revisión, el hallazgo que cita un papel inexistente y el programa sin aprobación salen con `/criterio-audit-work:workpaper-check`.
- La diferencia entre el informe y los papeles sale con `/criterio-audit-work:report-check`.
- El auditor que revisa su propio trabajo sale con `/criterio-audit-work:objectivity-check`.

**Cuándo vuelvo:** sin reloj, porque nadie dio un sí explícito y sin eso no programo nada. Para correrlo a mano: `/criterio-audit-work:work-wake`.

La corrida quedó registrada como `2026-11-24-work-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.