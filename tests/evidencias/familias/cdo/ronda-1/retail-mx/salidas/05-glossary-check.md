# /criterio-data-governance:glossary-check 

Los términos están vigentes (versión 1.6, aceptada por José Francisco Ñáñez el 2026-11-25). Corrí el reporte del periodo 2026-11 y quedó registrado.

# El glosario y el registro · Retail Central Sintético · periodo 2026-11

**Entidad:** Retail Central Sintético (RCM190305AB1) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.1.0 · **Comando:** `glossary-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Índice de rotación»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 2 | Un término de un informe de dirección no tiene su definición en el glosario de negocio (`term_not_in_glossary`) | «Margen operacional»: el informe lo usa y el glosario de negocio no lo define | — | — | — | `20-informes/informe_junta_2026-10.pdf` |

## El resultado

| Término | Informe | En el glosario |
|---|---|---|
| Cartera vencida | `20-informes/informe_junta_2026-10.pdf` | sí |
| Clientes activos | `20-informes/informe_junta_2026-10.pdf` | sí |
| Ventas netas | `20-informes/informe_junta_2026-10.pdf` | sí |
| Margen operacional | `20-informes/informe_junta_2026-10.pdf` | no |
| Índice de rotación | `20-informes/informe_junta_2026-10.pdf` | no |

| Conjunto con datos personales | En el registro de bases |
|---|---|
| DS-01 · Clientes | sí |
| DS-03 · Proveedores | sí |
| DS-04 · Candidatos | sí |

Lo que exige la ley de cada país sobre el registro de bases de datos personales lo confirma el área: aquí se compara el catálogo con el registro de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-informes/informe_junta_2026-10.pdf`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)