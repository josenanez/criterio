# /criterio-data-governance:retention-check 

Dos políticas pasaron su fecha de revisión y dos conjuntos de candidatos conservan registros más allá de su plazo. Archivar o borrar lo decide el dueño del dato.

# Las políticas y los plazos · Banco Canal Sintético · periodo 2026-11

**Entidad:** Banco Canal Sintético (155698765-2-2018) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 1.1.0 · **Comando:** `retention-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Un conjunto conserva registros más tiempo del que fija la política para su tipo (`retention_exceeded`) | DS-42 · Candidatos a prácticas: conserva registros desde el 2022-01-01, y la política fija 24 meses para «Candidatos»: todo lo anterior al 2024-11-25 pasó su plazo | Gestión humana | 1059 | `10-catalogo/catalogo_datos.xlsx` fila 10 · `00-referencia/politica_de_conservacion.pdf` |
| 2 | Un conjunto conserva registros más tiempo del que fija la política para su tipo (`retention_exceeded`) | DS-04 · Candidatos: conserva registros desde el 2023-06-01, y la política fija 24 meses para «Candidatos»: todo lo anterior al 2024-11-25 pasó su plazo | Gestión humana | 543 | `10-catalogo/catalogo_datos.xlsx` fila 5 · `00-referencia/politica_de_conservacion.pdf` |
| 3 | Una política de datos o de conservación pasó su fecha de revisión (`policy_review_overdue`) | Política de datos: su revisión tocaba el 2025-06-30 y no hay una versión posterior | — | 513 | `00-referencia/politica_de_datos.pdf` |
| 4 | Una política de datos o de conservación pasó su fecha de revisión (`policy_review_overdue`) | Política de conservación: su revisión tocaba el 2026-03-01 y no hay una versión posterior | — | 269 | `00-referencia/politica_de_conservacion.pdf` |

## El resultado

| Política | Aprobada | Revisión | Documento |
|---|---|---|---|
| Política de datos | 2024-06-30 | 2025-06-30 | `00-referencia/politica_de_datos.pdf` |
| Política de conservación | 2025-09-01 | 2026-03-01 | `00-referencia/politica_de_conservacion.pdf` |

| Conjunto | Tipo | Plazo | Registro más antiguo | Lo que vence antes del |
|---|---|---|---|---|
| DS-01 | Clientes | 120 meses | 2018-03-01 | 2016-11-25 |
| DS-02 | Transaccional | 120 meses | 2017-01-01 | 2016-11-25 |
| DS-03 | Proveedores | 60 meses | 2023-01-01 | 2021-11-25 |
| DS-04 | Candidatos | 24 meses | 2023-06-01 | 2024-11-25 |
| DS-05 | Transaccional | 120 meses | 2020-01-01 | 2016-11-25 |
| DS-12 | Transaccional | 120 meses | 2024-01-01 | 2016-11-25 |
| DS-22 | Proveedores | 60 meses | 2024-01-01 | 2021-11-25 |
| DS-32 | Clientes | 120 meses | 2022-01-01 | 2016-11-25 |
| DS-42 | Candidatos | 24 meses | 2022-01-01 | 2024-11-25 |

Qué se borra o se archiva lo decide el dueño del dato con la política: aquí se dice qué pasó su plazo.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica_de_conservacion.pdf`
- `00-referencia/politica_de_datos.pdf`
- `10-catalogo/catalogo_datos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-retention-check-1`. Los términos ya estaban vigentes, así que no hizo falta registrar la aceptación.