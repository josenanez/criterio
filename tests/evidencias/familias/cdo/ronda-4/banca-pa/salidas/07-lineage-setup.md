# /criterio-data-quality:lineage-setup datos/155698765-2-2018-banco-canal-sintetico

Ariadna quedó lista sobre Banco Canal Sintético. De las 9 cifras del informe de junta de octubre de 2026, solo 3 coinciden con la fuente: 2 son distintas, 2 salen de otro corte y 2 no tienen fuente.

**Lo que se respondió** (prueba sin interfaz; tomé la respuesta que sugerían los documentos):
1. **Carpeta:** `datos/155698765-2-2018-banco-canal-sintetico`. Era la única candidata y ya estaba marcada con `_CRITERIO_DATOS.txt`, así que no pregunté por la marca.
2. **Entidad:** Banco Canal Sintético, RUC 155698765-2-2018, Panamá, en USD. Ya la había fijado Custodia.
3. **Periodo:** 2026-11, el mismo de Custodia.
4. **Tolerancia entre cifra y fuente:** 0.5 %, la que fija la política de datos.
5. **Publicar en Rostrum:** sí, porque la política no dice otra cosa.
6. **Dónde guardo lo que encuentro:** `estado-datos/155698765-2-2018-banco-canal-sintetico`.
7. **Términos (versión 1.6):** los mostré tal cual. Los aceptó José Francisco Ñáñez el 2026-11-25.

La configuración quedó en `.criterio/calidad/155698765-2-2018/config.json`. El comprobante de aceptación quedó en `.criterio/terminos/aceptacion-criterio-data-quality-1.1.0-2026-11-25.md` y en `.pdf`.

Procesé el informe de junta de 2026-10 y crucé sus 9 cifras contra las de la fuente en `30-calidad/`. El reporte redondea los dos índices sin fuente en el detalle y en la tabla de resultado: muestra 8 y 4. Su columna «Monto» trae los valores completos, 8.10 y 4.20. El reporte va tal cual:

---

# Cada cifra contra su fuente · Banco Canal Sintético · periodo 2026-11

**Entidad:** Banco Canal Sintético (155698765-2-2018) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 1.1.0 · **Comando:** `figure-check`

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

El motor encontró 14 señales en total. Este reporte solo cubre las 6 de las cifras contra su fuente. Las otras 8 son del linaje, de los datos críticos y de las reglas de calidad, y se ven con `/criterio-data-quality:lineage-check` y `/criterio-data-quality:rule-check`.

**Reloj:** no creé la tarea diaria de los días hábiles a las 7:00, porque necesita un sí explícito y en esta prueba nadie podía darlo. Para correrlo a mano: `/criterio-data-quality:lineage-wake`.
**Cuándo vuelvo:** sin reloj.

**Registro de la corrida:** la registré dos veces. La primera, `2026-11-25-lineage-setup-1`, salió sin el reporte completo. La segunda, `2026-11-25-lineage-setup-2`, la reemplaza y lo trae entero; la nota de la corrida lo dice.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.