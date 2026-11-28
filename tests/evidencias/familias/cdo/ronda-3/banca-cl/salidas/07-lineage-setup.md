# /criterio-data-quality:lineage-setup datos/97123456-k-banco-austral-sintetico

Ariadna quedó instalada sobre Banco Austral Sintético (RUT 97123456-K, Chile) y su primera revisión de cifras ya corrió. De las 9 cifras del informe a la junta de octubre, 3 coinciden con su fuente y 6 necesitan atención.

**Qué quedó listo**
- **Configuración:** `.criterio/calidad/97123456-k/config.json`, con periodo 2026-11, tolerancia de 0,5 % según la política de datos y publicación en Rostrum.
- **Respuestas:** las tomé de la configuración que ya había dejado Custodia y de la política de datos.
- **Términos v1.6:** aceptados por José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-data-quality-1.0.0-2026-11-25.md` y `.pdf`.
- **Marca:** la carpeta ya estaba marcada, así que no la volví a marcar.
- **Corrida:** registrada como `2026-11-25-lineage-setup-1`.

**Un ajuste en el camino:** el primer reporte falló porque escribí las preguntas de la ficha como texto y el motor las espera como pregunta y respuesta. Lo corregí, recalculé y el reporte salió bien.

**Un detalle de presentación:** en la tabla del resultado, los dos índices aparecen sin su decimal; la ficha y la columna de monto los traen completos.

# Cada cifra contra su fuente · Banco Austral Sintético · periodo 2026-11

**Entidad:** Banco Austral Sintético (97123456-k) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 1.0.0 · **Comando:** `figure-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Ventas netas» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 9,520,000,000 y la fuente 9,400,000,000 al mismo corte, 2026-10-31: una diferencia de 120,000,000, más allá de la tolerancia del 0.5 % | 120.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 6 |
| 2 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Depósitos» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 5,100,000,000 y la fuente 5,000,000,000 al mismo corte, 2026-10-31: una diferencia de 100,000,000, más allá de la tolerancia del 0.5 % | 100.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 10 |
| 3 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Índice de satisfacción» del informe 20-informes/informe_junta_2026-10.pdf: 8 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 8,10 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 4 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Índice de rotación» del informe 20-informes/informe_junta_2026-10.pdf: 4 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 4,20 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 5 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Colocaciones» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 7,600,000,000, es la de la fuente al 2026-09-30 | 7.600.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 13 |
| 6 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Cartera vencida» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 1,180,000,000, es la de la fuente al 2026-09-30 | 1.180.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 3 |

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

- Entidad, RUT y país → Banco Austral Sintético, 97123456-K, CL (de la configuración de Custodia)
- Periodo → 2026-11 (el mismo de Custodia)
- Diferencia tolerada entre una cifra y su fuente → 0.5 % (00-referencia/politica_de_datos.pdf)
- ¿Se publica en Rostrum? → Sí; la política de datos no dice otra cosa
- Dónde se guarda el estado → estado-datos/97123456-k-banco-austral-sintetico
- Términos v1.6 → Aceptados por José Francisco Ñáñez el 2026-11-25

## Fuentes

- `20-informes/informe_junta_2026-10.pdf`
- `30-calidad/cifras_fuente.xlsx`
- Fuentes técnicas: F-01, F-02 (families/criterio-cdo/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta prueba no hubo nadie que lo diera. Para correr la revisión a mano: `/criterio-data-quality:lineage-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.