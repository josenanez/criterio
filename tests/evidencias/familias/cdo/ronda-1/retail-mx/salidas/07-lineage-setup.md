# /criterio-data-quality:lineage-setup datos/rcm190305ab1-retail-central-sintetico

Ariadna quedó configurada para Retail Central Sintético (RFC RCM190305AB1). La primera revisión encontró dos cifras del informe de junta de octubre por atender: el «Índice de rotación» no tiene fuente y la «Cartera vencida» coincide con la fuente pero al corte de septiembre, no al de octubre.

**Cómo quedó la configuración.** No pregunté nada: tomé lo que ya había fijado Custodia y lo que dice la política de datos.
- **Carpeta:** `datos/rcm190305ab1-retail-central-sintetico`, la única candidata. Ya estaba marcada con `_CRITERIO_DATOS.txt`, así que no la volví a marcar.
- **Entidad:** Retail Central Sintético · RFC RCM190305AB1 · México (MXN).
- **Periodo:** 2026-11, el mismo que fijó Custodia.
- **Tolerancia:** 0,5 %. La política de datos dice que una cifra «no puede diferir de su fuente en más del 0.5 % al mismo corte».
- **Publicar en Rostrum:** sí, porque la política no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-datos/rcm190305ab1-retail-central-sintetico`.
- **Términos (v1.6):** los aceptó José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-data-quality-0.1.0-2026-11-25.md` y en `.pdf`.
- **Archivo de configuración:** `.criterio/calidad/RCM190305AB1/config.json`.

Llevé a la ficha las cinco cifras del informe de octubre y las crucé contra las cifras de la fuente y el linaje exportados en `30-calidad/`.

Una nota sobre el reporte: en dos lugares el motor escribe «4» para el «Índice de rotación», pero el informe dice 4,2. La columna Monto sí muestra 4.20 y la ficha tiene registrado el valor del informe. Este es el reporte, tal como lo escribió el motor:

# Cada cifra contra su fuente · Retail Central Sintético · periodo 2026-11

**Entidad:** Retail Central Sintético (RCM190305AB1) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.1.0 · **Comando:** `figure-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Índice de rotación» del informe 20-informes/informe_junta_2026-10.pdf: 4 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 4.20 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 2 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Cartera vencida» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 1,180,000,000, es la de la fuente al 2026-09-30 | 1,180,000,000.00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 3 |

## El resultado

**Tolerancia de la política de datos:** 0.5 %.

| Informe | Indicador | Corte | En el informe | En la fuente | Estado |
|---|---|---|---|---|---|
| `20-informes/informe_junta_2026-10.pdf` | Cartera vencida | 2026-10-31 | 1,180,000,000 | 1,250,000,000 | otro corte |
| `20-informes/informe_junta_2026-10.pdf` | Clientes activos | 2026-10-31 | 84,200 | 84,200 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Ventas netas | 2026-10-31 | 9,420,000,000 | 9,400,000,000 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Margen operacional | 2026-10-31 | 3,400,000,000 | 3,400,000,000 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Índice de rotación | 2026-10-31 | 4 | — | sin fuente |

Cuál cifra es la correcta lo decide quien firma el informe: aquí se dice cuál no coincide con su fuente.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-informes/informe_junta_2026-10.pdf`
- `30-calidad/cifras_fuente.xlsx`
- Fuentes técnicas: F-01, F-02 (families/criterio-cdo/FUENTES.es.md)

---

El motor encontró además otras dos señales de este periodo que este reporte no muestra: un dato crítico sin ninguna regla que lo mida y una regla de calidad que no alcanza su umbral. Las detalla `/criterio-data-quality:rule-check`.

**Cuándo vuelvo:** no dejé tarea programada, porque en esta sesión sin interfaz nadie pudo dar el sí que esa tarea exige. Para correrlo a mano: `/criterio-data-quality:lineage-wake`.

Dejé la corrida registrada como `2026-11-25-lineage-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.