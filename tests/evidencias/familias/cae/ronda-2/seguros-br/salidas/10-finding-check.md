# /criterio-audit-work:finding-check 

**finding-check, periodo 2026-11, Seguradora Atlântica Sintética.** Los términos (versión 1.6) ya estaban vigentes y aceptados, así que no registré ninguna aceptación nueva. El único hallazgo con problemas es TR-01 · H-01, que tiene dos señales. Los otros dos, TR-01 · H-02 y TR-02 · H-03, no tienen nada pendiente.

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

La corrida quedó registrada como `2026-11-24-finding-check-1`, con 8 hallazgos en el registro. La salida completa está en `estado-auditoria/31452078000190-seguradora-atlantica-sintetica/corridas/salida-finding-check.md`.

Hay dos cosas que ajustar en el procedimiento:
- **Fecha:** el sistema marca hoy como 2026-11-26, pero pasé `--today 2026-11-24` al motor, como pedía la prueba. Por eso el corte y la corrida llevan 2026-11-24.
- **Reporte:** copié el archivo del motor a `corridas/salida-finding-check.md` sin cambiarlo. Es lo que mostré arriba, pero no añadí las dos o tres líneas de contexto antes del encabezado: están en este mensaje.