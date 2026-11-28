# /criterio-data-governance:governance-wake 

Hoy tocaba la revisión semanal (`governance-scan`) de Banco Austral Sintético. No había peticiones abiertas en el portal. Los términos ya estaban aceptados para esta versión, así que no hubo que registrar la aceptación de José Francisco Ñáñez.

Esta semana no llegaron documentos nuevos ni cambiados. La ficha del periodo cubre todo lo que hay y no quedó nada sin procesar. Las 13 señales siguen abiertas, y decidir cada una les toca al área de datos y al dueño de cada conjunto.

# Qué cambió en el gobierno · Banco Austral Sintético · periodo 2026-11

**Entidad:** Banco Austral Sintético (97123456-k) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 1.0.0 · **Comando:** `governance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un conjunto con datos personales no está en el registro de bases de datos personales de la organización (`personal_data_unregistered`) | DS-03 · Proveedores: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales de la organización | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 4 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 2 | Un conjunto con datos personales no está en el registro de bases de datos personales de la organización (`personal_data_unregistered`) | DS-32 · Beneficiarios: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales de la organización | — | Gerencia comercial | — | `10-catalogo/catalogo_datos.xlsx` fila 9 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 3 | Un conjunto conserva registros más tiempo del que fija la política para su tipo (`retention_exceeded`) | DS-42 · Candidatos a prácticas: conserva registros desde el 2022-01-01, y la política fija 24 meses para «Candidatos»: todo lo anterior al 2024-11-25 pasó su plazo | — | Gestión humana | 1059 | `10-catalogo/catalogo_datos.xlsx` fila 10 · `00-referencia/politica_de_conservacion.pdf` |
| 4 | Un conjunto conserva registros más tiempo del que fija la política para su tipo (`retention_exceeded`) | DS-04 · Candidatos: conserva registros desde el 2023-06-01, y la política fija 24 meses para «Candidatos»: todo lo anterior al 2024-11-25 pasó su plazo | — | Gestión humana | 543 | `10-catalogo/catalogo_datos.xlsx` fila 5 · `00-referencia/politica_de_conservacion.pdf` |
| 5 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-02 · Movimientos: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 3 |
| 6 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-12 · Pagos a proveedores: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 7 |
| 7 | Una política de datos o de conservación pasó su fecha de revisión (`policy_review_overdue`) | Política de datos: su revisión tocaba el 2025-06-30 y no hay una versión posterior | — | — | 513 | `00-referencia/politica_de_datos.pdf` |
| 8 | Una política de datos o de conservación pasó su fecha de revisión (`policy_review_overdue`) | Política de conservación: su revisión tocaba el 2026-03-01 y no hay una versión posterior | — | — | 269 | `00-referencia/politica_de_conservacion.pdf` |
| 9 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-03 · Proveedores: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 4 |
| 10 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-22 · Contratos con proveedores: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 8 |
| 11 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Costo de adquisición»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 12 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Índice de rotación»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 13 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Margen operacional»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |

## El resultado

**Conjuntos en el catálogo:** 9 · **Con datos personales:** 4 · **Políticas en la ficha:** 2 · **Términos de los informes:** 9.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica_de_conservacion.pdf`
- `00-referencia/politica_de_datos.pdf`
- `10-catalogo/catalogo_datos.xlsx`
- `10-catalogo/registro_de_bases_personales.xlsx`
- `20-informes/informe_junta_2026-10.pdf`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

---

Quedaron registradas las dos corridas, `2026-11-25-governance-scan-2` y `2026-11-25-governance-wake-1`, con caso 2026-11. El motor generó el reporte del scan una segunda vez sin cambios en el resultado.

Lo que se mostró quedó guardado en:
- `<espacio>/estado-datos/97123456-k-banco-austral-sintetico/corridas/salida-governance-scan.md`
- `<espacio>/estado-datos/97123456-k-banco-austral-sintetico/corridas/salida-governance-wake.md`