# /criterio-data-governance:glossary-check 

Los términos estaban vigentes (v1.6, ya aceptados), así que no hizo falta registrar una aceptación nueva. Corrí el reporte de 2026-11 con corte 2026-11-25 y registré la corrida (`2026-11-25-glossary-check-1`).

No hubo preguntas en esta sesión.

# El glosario y el registro · Banco Canal Sintético · periodo 2026-11

**Entidad:** Banco Canal Sintético (155698765-2-2018) · **Fecha de corte:** 2026-11-25 · **Agente:** Custodia 1.1.0 · **Comando:** `glossary-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | `personal_data_unregistered` | DS-03 · Proveedores: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales | Compras | `10-catalogo/catalogo_datos.xlsx` fila 4 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 2 | `personal_data_unregistered` | DS-32 · Beneficiarios: el catálogo dice que tiene datos personales y no está en el registro | Gerencia comercial | `10-catalogo/catalogo_datos.xlsx` fila 9 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 3 | `term_not_in_glossary` | «Costo de adquisición»: el informe lo usa y el glosario no lo define | — | `20-informes/informe_junta_2026-10.pdf` |
| 4 | `term_not_in_glossary` | «Índice de rotación»: el informe lo usa y el glosario no lo define | — | `20-informes/informe_junta_2026-10.pdf` |
| 5 | `term_not_in_glossary` | «Margen operacional»: el informe lo usa y el glosario no lo define | — | `20-informes/informe_junta_2026-10.pdf` |

## El resultado

| Término | En el glosario |
|---|---|
| Cartera vencida, Clientes activos, Ventas netas, Depósitos, Colocaciones, Índice de satisfacción | sí |
| Margen operacional, Costo de adquisición, Índice de rotación | no |

| Conjunto con datos personales | En el registro de bases |
|---|---|
| DS-01 · Clientes | sí |
| DS-03 · Proveedores | no |
| DS-04 · Candidatos | sí |
| DS-32 · Beneficiarios | no |

Lo que exige la ley de cada país sobre el registro de bases de datos personales lo confirma el área: aquí se compara el catálogo con el registro de la organización.

**Lo que no se pudo procesar:** todo lo que llegó se procesó.

**Fuentes:** `10-catalogo/catalogo_datos.xlsx`, `10-catalogo/registro_de_bases_personales.xlsx`, `20-informes/informe_junta_2026-10.pdf`.

El reporte completo está en `estado-datos/155698765-2-2018-banco-canal-sintetico/gobierno/2026-11/reporte-glossary-check.md`. La salida queda en `corridas/salida-glossary-check.md`, en la misma carpeta de estado.

Dejé al principio de ese archivo de salida una línea que no está en el reporte del motor, sobre los términos vigentes. Así que no es copia exacta de lo mostrado, y el encabezado completo (procesado, preguntas) lo resumí aquí.