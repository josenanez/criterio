# /criterio-audit-work:work-setup auditoria/31452078000190-seguradora-atlantica-sintetica

Soy Justo. Pongo cada hallazgo al lado de su criterio y de su papel, y cada informe al lado de sus papeles; no cambio prioridades ni firmo informes.

Justo ya está configurado para Seguradora Atlântica Sintética. Encontré una sola carpeta: `auditoria/31452078000190-seguradora-atlantica-sintetica`. Ya tenía la marca `_CRITERIO_AUDITORIA.txt` y las cuatro subcarpetas de la estructura, así que no hubo que marcarla de nuevo.

**Respuestas que tomé de los documentos** (nadie respondió las preguntas en esta sesión):
- **Entidad:** Seguradora Atlântica Sintética, CNPJ 31452078000190, Brasil (BR), en reales (BRL). **Periodo:** 2026-11.
- **Escala de prioridad:** Alta desde 15, Media desde 8 y Baja desde 1, multiplicando impacto por probabilidad (cada uno de 1 a 5). Sale de la sección «Escala de prioridad de los hallazgos» de la metodología.
- **Quién aprueba el plan:** el Comité de auditoría, según el estatuto.
- **Quién aprueba el programa y los papeles:** ni el estatuto ni la metodología lo dicen. En los documentos de aprobación del programa de cada trabajo aparece la jefa de auditoría. No inventé este valor.
- **Publicar en Rostrum:** no. **Lo que encuentro se guarda en:** `estado-auditoria/31452078000190-seguradora-atlantica-sintetica`.
- **Términos 1.6:** se mostraron tal cual y quedan aceptados por José Francisco Ñáñez el 2026-11-24. El comprobante está en `.criterio/terminos/aceptacion-criterio-audit-work-0.2.2-2026-11-24.md` y en el `.pdf` del mismo nombre.

La configuración quedó en `.criterio/trabajos/31452078000190/config.json` y pasó la validación sin problemas.

Procesé los 15 documentos de `20-trabajos/` y todos se pudieron convertir. Llevé a la ficha de 2026-11 los trabajos TR-01 y TR-02 y sus tres hallazgos. El motor encontró 8 señales en el periodo. Este reporte muestra solo las de los hallazgos; las demás salen con `/criterio-audit-work:workpaper-check` y `/criterio-audit-work:report-check`.

# Cada hallazgo y sus elementos · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.2.2 · **Comando:** `finding-check`

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

**El reloj:** nadie dio un sí, así que no creé ninguna tarea programada. Para revisar a mano lo que toca cada día: `/criterio-audit-work:work-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-24-work-setup-1`, y lo que se mostró está en `estado-auditoria/31452078000190-seguradora-atlantica-sintetica/corridas/salida-work-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.