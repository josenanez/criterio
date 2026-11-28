# /criterio-data-governance:glossary-check 

Los términos vigentes están al día. Del catálogo, dos conjuntos con datos personales no están en el registro de bases, y tres términos del informe de junta no están en el glosario.

# El glosario y el registro · Banco Austral Sintético · periodo 2026-11

**Entidad:** Banco Austral Sintético (97123456-k) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 1.0.0 · **Comando:** `glossary-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un conjunto con datos personales no está en el registro de bases de datos personales de la organización (`personal_data_unregistered`) | DS-03 · Proveedores: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales de la organización | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 4 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 2 | Un conjunto con datos personales no está en el registro de bases de datos personales de la organización (`personal_data_unregistered`) | DS-32 · Beneficiarios: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales de la organización | — | Gerencia comercial | — | `10-catalogo/catalogo_datos.xlsx` fila 9 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 3 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Costo de adquisición»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 4 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Índice de rotación»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 5 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Margen operacional»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |

## El resultado

| Término | Informe | En el glosario |
|---|---|---|
| Cartera vencida | `20-informes/informe_junta_2026-10.pdf` | sí |
| Clientes activos | `20-informes/informe_junta_2026-10.pdf` | sí |
| Ventas netas | `20-informes/informe_junta_2026-10.pdf` | sí |
| Margen operacional | `20-informes/informe_junta_2026-10.pdf` | no |
| Depósitos | `20-informes/informe_junta_2026-10.pdf` | sí |
| Colocaciones | `20-informes/informe_junta_2026-10.pdf` | sí |
| Costo de adquisición | `20-informes/informe_junta_2026-10.pdf` | no |
| Índice de satisfacción | `20-informes/informe_junta_2026-10.pdf` | sí |
| Índice de rotación | `20-informes/informe_junta_2026-10.pdf` | no |

| Conjunto con datos personales | En el registro de bases |
|---|---|
| DS-01 · Clientes | sí |
| DS-03 · Proveedores | no |
| DS-04 · Candidatos | sí |
| DS-32 · Beneficiarios | no |

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

---
Corrida registrada como `2026-11-25-glossary-check-1`. Una nota sobre los términos: el motor los da por vigentes (versión 1.6), así que no hizo falta registrar la aceptación de José Francisco Ñáñez que se indicaba para esta prueba. No corrí `governance-setup`.