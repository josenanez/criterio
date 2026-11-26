# /criterio-data-governance:governance-wake 

Hoy tocaba la revisión semanal (`governance-scan`). No había peticiones abiertas y no llegaron documentos nuevos, cambiados ni borrados. Recalculé el periodo y las señales siguen abiertas. No asigné dueños, no puse clasificaciones y no borré nada: esas decisiones son del área de datos y del dueño de cada conjunto.

# Qué cambió en el gobierno · Retail Central Sintético · periodo 2026-11

**Entidad:** Retail Central Sintético (RCM190305AB1) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `governance-scan`

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

- ¿Qué carpeta es la de la entidad? → datos/rcm190305ab1-retail-central-sintetico (única candidata, con 00-referencia/, 10-catalogo/, 20-informes/ y 30-calidad/)
- Entidad, identificación fiscal y país → Retail Central Sintético · RFC RCM190305AB1 · México (MXN), según el nombre de la carpeta y los documentos
- Periodo → 2026-11, el mes en curso a la fecha de la prueba
- ¿Se publica en Rostrum? → Sí: la política de datos no dice otra cosa
- ¿Dónde se guarda el estado? → estado-datos/rcm190305ab1-retail-central-sintetico
- ¿Acepta los términos 1.6? → Sí, José Francisco Ñáñez, 2026-11-25
- ¿Se marca la carpeta con _CRITERIO_DATOS.txt? → Sí

## Fuentes

- `00-referencia/politica_de_conservacion.pdf`
- `00-referencia/politica_de_datos.pdf`
- `10-catalogo/catalogo_datos.xlsx`
- `10-catalogo/registro_de_bases_personales.xlsx`
- `20-informes/informe_junta_2026-10.pdf`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

---

Las dos corridas quedaron registradas en `estado-datos/rcm190305ab1-retail-central-sintetico/corridas/`: `2026-11-25-governance-scan-2` y `2026-11-25-governance-wake-1`.