# /criterio-data-governance:glossary-check 

Los términos ya estaban vigentes (versión 1.6, aceptada en la 0.2.0), así que no hizo falta registrar una aceptación nueva. Corrí `glossary-check` para 2026-11 con corte al 2026-11-25. El reporte tiene cinco señales abiertas y se muestra completo debajo.

# El glosario y el registro · Aseguradora Pacífico Sintética · periodo 2026-11

**Entidad:** Aseguradora Pacífico Sintética (20605557771) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `glossary-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | `personal_data_unregistered` | DS-03 · Proveedores: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales | Compras | `10-catalogo/catalogo_datos.xlsx` fila 4 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 2 | `personal_data_unregistered` | DS-32 · Beneficiarios: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales | Gerencia comercial | `10-catalogo/catalogo_datos.xlsx` fila 9 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 3 | `term_not_in_glossary` | «Costo de adquisición»: el informe lo usa y el glosario no lo define | — | `20-informes/informe_junta_2026-10.pdf` |
| 4 | `term_not_in_glossary` | «Índice de rotación»: el informe lo usa y el glosario no lo define | — | `20-informes/informe_junta_2026-10.pdf` |
| 5 | `term_not_in_glossary` | «Margen operacional»: el informe lo usa y el glosario no lo define | — | `20-informes/informe_junta_2026-10.pdf` |

## El resultado

| Término | En el glosario |
|---|---|
| Cartera vencida | sí |
| Clientes activos | sí |
| Ventas netas | sí |
| Margen operacional | no |
| Depósitos | sí |
| Colocaciones | sí |
| Costo de adquisición | no |
| Índice de satisfacción | sí |
| Índice de rotación | no |

Todos los términos son del `20-informes/informe_junta_2026-10.pdf`.

| Conjunto con datos personales | En el registro de bases |
|---|---|
| DS-01 · Clientes | sí |
| DS-03 · Proveedores | no |
| DS-04 · Candidatos | sí |
| DS-32 · Beneficiarios | no |

Lo que exige la ley de cada país sobre el registro de bases de datos personales lo confirma el área. Aquí solo se compara el catálogo con el registro de la organización.

## Lo que no se pudo procesar
Todo lo que llegó se procesó.

## Las preguntas que hizo
Ninguna en esta corrida.

## Fuentes
- `10-catalogo/catalogo_datos.xlsx`
- `10-catalogo/registro_de_bases_personales.xlsx`
- `20-informes/informe_junta_2026-10.pdf`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

El texto de arriba abrevia el reporte: quité las columnas «Monto» y «Días», que venían vacías, y la columna «Informe» de la tabla de términos.

La corrida quedó registrada como `2026-11-25-glossary-check-1`, con 13 hallazgos. Guardé la salida en `corridas/salida-glossary-check.md` copiando el reporte que escribió el motor. Esa copia es el reporte completo, con las columnas que aquí quité, y no el texto abreviado.