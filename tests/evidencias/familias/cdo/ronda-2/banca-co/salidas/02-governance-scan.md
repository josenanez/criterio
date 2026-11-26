# /criterio-data-governance:governance-scan 

Es la primera vez que corre el escaneo en esta carpeta, así que todos los documentos cuentan como nuevos y no hay una corrida anterior con la cual comparar.
La ficha del periodo ya recogía las políticas, los plazos de conservación y los términos tal como los traen los documentos, así que no hubo nada que agregar.

# Qué cambió en el gobierno · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `governance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un conjunto con datos personales no está en el registro de bases de datos personales de la organización (`personal_data_unregistered`) | DS-03 · Proveedores: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales de la organización | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 4 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 2 | Un conjunto con datos personales no está en el registro de bases de datos personales de la organización (`personal_data_unregistered`) | DS-32 · Beneficiarios: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales de la organización | — | Gerencia comercial | — | `10-catalogo/catalogo_datos.xlsx` fila 11 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 3 | Un conjunto con datos personales no está en el registro de bases de datos personales de la organización (`personal_data_unregistered`) | DS-33 · Visitantes de las sedes: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales de la organización | — | Gerencia comercial | — | `10-catalogo/catalogo_datos.xlsx` fila 12 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 4 | Un conjunto conserva registros más tiempo del que fija la política para su tipo (`retention_exceeded`) | DS-42 · Candidatos a prácticas: conserva registros desde el 2022-01-01, y la política fija 24 meses para «Candidatos»: todo lo anterior al 2024-11-25 pasó su plazo | — | Gestión humana | 1059 | `10-catalogo/catalogo_datos.xlsx` fila 13 · `00-referencia/politica_de_conservacion.pdf` |
| 5 | Un conjunto conserva registros más tiempo del que fija la política para su tipo (`retention_exceeded`) | DS-43 · Proveedores históricos: conserva registros desde el 2019-01-01, y la política fija 60 meses para «Proveedores»: todo lo anterior al 2021-11-25 pasó su plazo | — | Compras | 1059 | `10-catalogo/catalogo_datos.xlsx` fila 14 · `00-referencia/politica_de_conservacion.pdf` |
| 6 | Un conjunto conserva registros más tiempo del que fija la política para su tipo (`retention_exceeded`) | DS-04 · Candidatos: conserva registros desde el 2023-06-01, y la política fija 24 meses para «Candidatos»: todo lo anterior al 2024-11-25 pasó su plazo | — | Gestión humana | 543 | `10-catalogo/catalogo_datos.xlsx` fila 5 · `00-referencia/politica_de_conservacion.pdf` |
| 7 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-02 · Movimientos: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 3 |
| 8 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-12 · Pagos a proveedores: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 7 |
| 9 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-13 · Campañas de mercadeo: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 8 |
| 10 | Una política de datos o de conservación pasó su fecha de revisión (`policy_review_overdue`) | Política de calidad de datos: su revisión tocaba el 2025-05-15 y no hay una versión posterior | — | — | 559 | `00-referencia/politica_de_calidad_de_datos.pdf` |
| 11 | Una política de datos o de conservación pasó su fecha de revisión (`policy_review_overdue`) | Política de datos: su revisión tocaba el 2025-06-30 y no hay una versión posterior | — | — | 513 | `00-referencia/politica_de_datos.pdf` |
| 12 | Una política de datos o de conservación pasó su fecha de revisión (`policy_review_overdue`) | Política de conservación: su revisión tocaba el 2026-03-01 y no hay una versión posterior | — | — | 269 | `00-referencia/politica_de_conservacion.pdf` |
| 13 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-03 · Proveedores: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 4 |
| 14 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-22 · Contratos con proveedores: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 9 |
| 15 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-23 · Inventario de activos: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 10 |
| 16 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Costo de adquisición»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 17 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Índice de rotación»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 18 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Margen operacional»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 19 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Tasa de retención»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |

## El resultado

**Conjuntos en el catálogo:** 13 · **Con datos personales:** 5 · **Políticas en la ficha:** 3 · **Términos de los informes:** 13.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica_de_calidad_de_datos.pdf`
- `00-referencia/politica_de_conservacion.pdf`
- `00-referencia/politica_de_datos.pdf`
- `10-catalogo/catalogo_datos.xlsx`
- `10-catalogo/registro_de_bases_personales.xlsx`
- `20-informes/informe_junta_2026-10.pdf`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)