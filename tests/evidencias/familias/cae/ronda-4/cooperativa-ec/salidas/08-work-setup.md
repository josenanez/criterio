# /criterio-audit-work:work-setup auditoria/1791234567001-cooperativa-de-ahorro-chimborazo-sintetica

Justo quedó listo para la Cooperativa de Ahorro Chimborazo Sintética (RUC 1791234567001). En la primera revisión, el hallazgo H-01 de TR-01 sale sin causa y con una prioridad distinta de la que da la metodología.

- **Configuración:** quedó en `.criterio/trabajos/1791234567001/config.json`. Tomé la entidad, el periodo (2026-11), la escala de prioridad y la carpeta del estado de la metodología, del estatuto y de lo que ya había fijado Prudencia. Nada se publica en Rostrum.
- **Quién aprueba el programa y los papeles:** según las dos aprobaciones del programa, la jefa de auditoría. La metodología no lo dice y la configuración no tiene dónde guardarlo, así que no lo escribí.
- **Términos 1.6:** quedan aceptados por José Francisco Ñáñez el 2026-11-24. El comprobante está en `.criterio/terminos/aceptacion-criterio-audit-work-1.1.0-2026-11-24.md` y en el `.pdf` del mismo nombre.
- **Marca:** la carpeta ya tenía `_CRITERIO_AUDITORIA.txt` desde el 2026-11-24, así que no la volví a marcar.
- **Ficha del periodo:** procesé los 15 documentos de `20-trabajos/` y llevé TR-01 y TR-02, con sus tres hallazgos, a la ficha.
- **Otras señales:** el motor encontró además señales sobre los pasos del programa, la revisión de los papeles y la coincidencia entre el informe y los papeles. No entran en este reporte; se ven con `/criterio-audit-work:workpaper-check` y `/criterio-audit-work:report-check`.

# Cada hallazgo y sus elementos · Cooperativa de Ahorro Chimborazo Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Chimborazo Sintética (1791234567001) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 1.1.0 · **Comando:** `finding-check`

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

**Reloj:** no creé la tarea programada porque necesita un sí explícito y en esta sesión no lo hubo. Se corre a mano con `/criterio-audit-work:work-wake`.

**Cuándo vuelvo:** sin reloj.

La salida de esta corrida quedó guardada y registrada como `2026-11-24-work-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.