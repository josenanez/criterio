# /criterio-data-quality:lineage-setup datos/20605557771-aseguradora-pacifico-sintetica

Ariadna quedó instalada para Aseguradora Pacífico Sintética (RUC 20605557771, Perú) y ya corrió el primer cruce de cifras. De las 9 cifras del informe de junta de octubre, solo 3 coinciden con su fuente. Hay que atender 6.

**Configuración:** respuestas tomadas de los documentos y de la configuración que ya había dejado Custodia.
- **Carpeta:** `datos/20605557771-aseguradora-pacifico-sintetica`. Era la única candidata y ya tenía la marca `_CRITERIO_DATOS.txt`, así que no se volvió a pedir.
- **Periodo:** 2026-11, el mismo que usa Custodia. Las cifras del informe tienen corte al 2026-10-31.
- **Tolerancia:** 0.5 %, la que fija `00-referencia/politica_de_datos.pdf`.
- **Rostrum:** se publica, porque la política no dice lo contrario.
- **Estado:** `estado-datos/20605557771-aseguradora-pacifico-sintetica`.
- **Términos:** mostré la v1.6 tal cual y quedó registrado que José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-data-quality-0.2.0-2026-11-25.md` y `.pdf`.
- **Archivo de configuración:** `.criterio/calidad/20605557771/config.json`.

Un detalle del reporte: la columna «En el informe» muestra el índice de satisfacción y el de rotación sin decimales. El valor completo, tal como lo registré, está en la columna «Monto».

---

# Cada cifra contra su fuente · Aseguradora Pacífico Sintética · periodo 2026-11

**Entidad:** Aseguradora Pacífico Sintética (20605557771) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `figure-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Ventas netas» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 9,520,000,000 y la fuente 9,400,000,000 al mismo corte, 2026-10-31: una diferencia de 120,000,000, más allá de la tolerancia del 0.5 % | 120,000,000.00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 6 |
| 2 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Depósitos» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 5,100,000,000 y la fuente 5,000,000,000 al mismo corte, 2026-10-31: una diferencia de 100,000,000, más allá de la tolerancia del 0.5 % | 100,000,000.00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 10 |
| 3 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Índice de satisfacción» del informe 20-informes/informe_junta_2026-10.pdf: 8 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 8.10 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 4 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Índice de rotación» del informe 20-informes/informe_junta_2026-10.pdf: 4 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 4.20 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 5 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Colocaciones» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 7,600,000,000, es la de la fuente al 2026-09-30 | 7,600,000,000.00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 13 |
| 6 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Cartera vencida» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 1,180,000,000, es la de la fuente al 2026-09-30 | 1,180,000,000.00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 3 |

## El resultado

**Tolerancia de la política de datos:** 0.5 %.

| Informe | Indicador | Corte | En el informe | En la fuente | Estado |
|---|---|---|---|---|---|
| `20-informes/informe_junta_2026-10.pdf` | Cartera vencida | 2026-10-31 | 1,180,000,000 | 1,250,000,000 | otro corte |
| `20-informes/informe_junta_2026-10.pdf` | Clientes activos | 2026-10-31 | 84,200 | 84,200 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Ventas netas | 2026-10-31 | 9,520,000,000 | 9,400,000,000 | distinta |
| `20-informes/informe_junta_2026-10.pdf` | Margen operacional | 2026-10-31 | 3,400,000,000 | 3,400,000,000 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Depósitos | 2026-10-31 | 5,100,000,000 | 5,000,000,000 | distinta |
| `20-informes/informe_junta_2026-10.pdf` | Colocaciones | 2026-10-31 | 7,600,000,000 | 7,800,000,000 | otro corte |
| `20-informes/informe_junta_2026-10.pdf` | Costo de adquisición | 2026-10-31 | 185,000 | 185,000 | coincide |
| `20-informes/informe_junta_2026-10.pdf` | Índice de satisfacción | 2026-10-31 | 8 | — | sin fuente |
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

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta prueba nadie la confirmó. Para correrlo a mano: `/criterio-data-quality:lineage-wake`.

La salida de esta sesión está en `estado-datos/20605557771-aseguradora-pacifico-sintetica/corridas/salida-lineage-setup.md` y la corrida quedó registrada como `2026-11-25-lineage-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.