# /criterio-data-governance:retention-check 

Reporte de retención listo: tres políticas con la revisión vencida y tres conjuntos con registros más allá de su plazo. Archivar o borrar lo decide cada dueño del dato.

# Las políticas y los plazos · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `retention-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Conserva más de lo que fija la política (`retention_exceeded`) | DS-42 · Candidatos a prácticas: registros desde 2022-01-01; la política fija 24 meses para «Candidatos», así que todo lo anterior al 2024-11-25 pasó su plazo | Gestión humana | 1059 | `10-catalogo/catalogo_datos.xlsx` fila 13 · `00-referencia/politica_de_conservacion.pdf` |
| 2 | `retention_exceeded` | DS-43 · Proveedores históricos: registros desde 2019-01-01; la política fija 60 meses para «Proveedores», así que todo lo anterior al 2021-11-25 pasó su plazo | Compras | 1059 | `10-catalogo/catalogo_datos.xlsx` fila 14 · `00-referencia/politica_de_conservacion.pdf` |
| 3 | `retention_exceeded` | DS-04 · Candidatos: registros desde 2023-06-01; la política fija 24 meses, así que todo lo anterior al 2024-11-25 pasó su plazo | Gestión humana | 543 | `10-catalogo/catalogo_datos.xlsx` fila 5 · `00-referencia/politica_de_conservacion.pdf` |
| 4 | Revisión de política vencida (`policy_review_overdue`) | Política de calidad de datos: la revisión tocaba el 2025-05-15 y no hay versión posterior | — | 559 | `00-referencia/politica_de_calidad_de_datos.pdf` |
| 5 | `policy_review_overdue` | Política de datos: la revisión tocaba el 2025-06-30 y no hay versión posterior | — | 513 | `00-referencia/politica_de_datos.pdf` |
| 6 | `policy_review_overdue` | Política de conservación: la revisión tocaba el 2026-03-01 y no hay versión posterior | — | 269 | `00-referencia/politica_de_conservacion.pdf` |

## El resultado

| Política | Aprobada | Revisión | Documento |
|---|---|---|---|
| Política de datos | 2024-06-30 | 2025-06-30 | `00-referencia/politica_de_datos.pdf` |
| Política de calidad de datos | 2023-05-15 | 2025-05-15 | `00-referencia/politica_de_calidad_de_datos.pdf` |
| Política de conservación | 2025-09-01 | 2026-03-01 | `00-referencia/politica_de_conservacion.pdf` |

| Conjunto | Tipo | Plazo | Registro más antiguo | Lo que vence antes del |
|---|---|---|---|---|
| DS-01 | Clientes | 120 meses | 2018-03-01 | 2016-11-25 |
| DS-02 | Transaccional | 120 meses | 2017-01-01 | 2016-11-25 |
| DS-03 | Proveedores | 60 meses | 2023-01-01 | 2021-11-25 |
| DS-04 | Candidatos | 24 meses | 2023-06-01 | 2024-11-25 |
| DS-05 | Transaccional | 120 meses | 2020-01-01 | 2016-11-25 |
| DS-12 | Transaccional | 120 meses | 2024-01-01 | 2016-11-25 |
| DS-13 | Transaccional | 120 meses | 2024-01-01 | 2016-11-25 |
| DS-22 | Proveedores | 60 meses | 2024-01-01 | 2021-11-25 |
| DS-23 | Transaccional | 120 meses | 2024-01-01 | 2016-11-25 |
| DS-32 | Clientes | 120 meses | 2022-01-01 | 2016-11-25 |
| DS-33 | Clientes | 120 meses | 2022-01-01 | 2016-11-25 |
| DS-42 | Candidatos | 24 meses | 2022-01-01 | 2024-11-25 |
| DS-43 | Proveedores | 60 meses | 2019-01-01 | 2021-11-25 |

Qué se borra o se archiva lo decide el dueño del dato con la política: aquí se dice qué pasó su plazo.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica_de_calidad_de_datos.pdf`
- `00-referencia/politica_de_conservacion.pdf`
- `00-referencia/politica_de_datos.pdf`
- `10-catalogo/catalogo_datos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

Los términos (v1.6) ya estaban vigentes y aceptados en la configuración. No hizo falta registrar una aceptación nueva a nombre de José Francisco Ñáñez, así que no la registré. La salida quedó en `estado-datos/901555777-banco-cordillera-sintetico/corridas/salida-retention-check.md` y la corrida quedó registrada como `2026-11-25-retention-check-1`.