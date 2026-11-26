# /criterio-data-governance:glossary-check 

Los términos están vigentes (versión 1.6), así que no hizo falta registrar una aceptación nueva. El motor no pidió ninguna respuesta.

# El glosario y el registro · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `glossary-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | `personal_data_unregistered` | DS-03 · Proveedores: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales de la organización | Compras | `10-catalogo/catalogo_datos.xlsx` fila 4 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 2 | `personal_data_unregistered` | DS-32 · Beneficiarios: el catálogo dice que tiene datos personales y no está en el registro | Gerencia comercial | `10-catalogo/catalogo_datos.xlsx` fila 11 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 3 | `personal_data_unregistered` | DS-33 · Visitantes de las sedes: el catálogo dice que tiene datos personales y no está en el registro | Gerencia comercial | `10-catalogo/catalogo_datos.xlsx` fila 12 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 4 | `term_not_in_glossary` | «Costo de adquisición»: el informe lo usa y el glosario de negocio no lo define | — | `20-informes/informe_junta_2026-10.pdf` |
| 5 | `term_not_in_glossary` | «Índice de rotación»: el informe lo usa y el glosario de negocio no lo define | — | `20-informes/informe_junta_2026-10.pdf` |
| 6 | `term_not_in_glossary` | «Margen operacional»: el informe lo usa y el glosario de negocio no lo define | — | `20-informes/informe_junta_2026-10.pdf` |
| 7 | `term_not_in_glossary` | «Tasa de retención»: el informe lo usa y el glosario de negocio no lo define | — | `20-informes/informe_junta_2026-10.pdf` |

## El resultado

| Término | Informe | En el glosario |
|---|---|---|
| Cartera vencida | `informe_junta_2026-10.pdf` | sí |
| Clientes activos | `informe_junta_2026-10.pdf` | sí |
| Ventas netas | `informe_junta_2026-10.pdf` | sí |
| Margen operacional | `informe_junta_2026-10.pdf` | no |
| Depósitos | `informe_junta_2026-10.pdf` | sí |
| Gastos operacionales | `informe_junta_2026-10.pdf` | sí |
| Colocaciones | `informe_junta_2026-10.pdf` | sí |
| Provisiones | `informe_junta_2026-10.pdf` | sí |
| Costo de adquisición | `informe_junta_2026-10.pdf` | no |
| Tasa de retención | `informe_junta_2026-10.pdf` | no |
| Índice de satisfacción | `informe_junta_2026-10.pdf` | sí |
| Participación de mercado | `informe_junta_2026-10.pdf` | sí |
| Índice de rotación | `informe_junta_2026-10.pdf` | no |

| Conjunto con datos personales | En el registro de bases |
|---|---|
| DS-01 · Clientes | sí |
| DS-03 · Proveedores | no |
| DS-04 · Candidatos | sí |
| DS-32 · Beneficiarios | no |
| DS-33 · Visitantes de las sedes | no |

Lo que exige la ley de cada país sobre el registro de bases de datos personales lo confirma el área: aquí se compara el catálogo con el registro de la organización.

## Lo que no se pudo procesar
Todo lo que llegó se procesó.

## Las preguntas que hizo
Ninguna en esta corrida.

## Fuentes
- `10-catalogo/catalogo_datos.xlsx`
- `10-catalogo/registro_de_bases_personales.xlsx`
- `20-informes/informe_junta_2026-10.pdf`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-glossary-check-1`. Lo mostrado está en `estado-datos/901555777-banco-cordillera-sintetico/corridas/salida-glossary-check.md`. El motor la cuenta con 19 hallazgos, y el reporte solo muestra 7 señales.