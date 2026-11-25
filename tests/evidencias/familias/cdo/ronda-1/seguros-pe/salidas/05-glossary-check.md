# /criterio-data-governance:glossary-check 

Los términos estaban vigentes (versión 1.6), así que no hizo falta pedir una aceptación nueva. Un conjunto con datos personales, Proveedores, no está en el registro de la organización.

# El glosario y el registro · Aseguradora Pacífico Sintética · periodo 2026-11

**Entidad:** Aseguradora Pacífico Sintética (20605557771) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.1.0 · **Comando:** `glossary-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un conjunto con datos personales no está en el registro de bases de datos personales de la organización (`personal_data_unregistered`) | DS-03 · Proveedores: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales de la organización | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 4 · `10-catalogo/registro_de_bases_personales.xlsx` |

## El resultado

| Término | Informe | En el glosario |
|---|---|---|
| Cartera vencida | `20-informes/informe_junta_2026-10.pdf` | sí |
| Clientes activos | `20-informes/informe_junta_2026-10.pdf` | sí |
| Ventas netas | `20-informes/informe_junta_2026-10.pdf` | sí |
| Margen operacional | `20-informes/informe_junta_2026-10.pdf` | sí |

| Conjunto con datos personales | En el registro de bases |
|---|---|
| DS-01 · Clientes | sí |
| DS-03 · Proveedores | no |
| DS-04 · Candidatos | sí |

Lo que exige la ley de cada país sobre el registro de bases de datos personales lo confirma el área: aquí se compara el catálogo con el registro de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-catalogo/catalogo_datos.xlsx`
- `10-catalogo/registro_de_bases_personales.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-glossary-check-1`. El texto mostrado está en `corridas/salida-glossary-check.md`, copiado tal cual del reporte que escribió el motor.