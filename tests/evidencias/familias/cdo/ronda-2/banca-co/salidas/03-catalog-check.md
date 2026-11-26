# /criterio-data-governance:catalog-check 

El catálogo trae 13 conjuntos. 3 no tienen dueño de negocio y 3 no tienen clasificación de confidencialidad. La asignación es del área de datos y de cada dueño.

Los términos estaban vigentes (versión 1.6, aceptada por José Francisco Ñáñez el 2026-11-25), así que no hizo falta registrarlos otra vez.

# Cada conjunto con su dueño · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `catalog-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | Sin dueño de negocio (`dataset_without_owner`) | DS-02 · Movimientos | — | `10-catalogo/catalogo_datos.xlsx` fila 3 |
| 2 | Sin dueño de negocio (`dataset_without_owner`) | DS-12 · Pagos a proveedores | — | `10-catalogo/catalogo_datos.xlsx` fila 7 |
| 3 | Sin dueño de negocio (`dataset_without_owner`) | DS-13 · Campañas de mercadeo | — | `10-catalogo/catalogo_datos.xlsx` fila 8 |
| 4 | Sin clasificación de confidencialidad (`dataset_without_classification`) | DS-03 · Proveedores | Compras | `10-catalogo/catalogo_datos.xlsx` fila 4 |
| 5 | Sin clasificación de confidencialidad (`dataset_without_classification`) | DS-22 · Contratos con proveedores | Compras | `10-catalogo/catalogo_datos.xlsx` fila 9 |
| 6 | Sin clasificación de confidencialidad (`dataset_without_classification`) | DS-23 · Inventario de activos | Compras | `10-catalogo/catalogo_datos.xlsx` fila 10 |

## El resultado

| Conjunto | Dueño | Clasificación | Tipo | Datos personales |
|---|---|---|---|---|
| DS-01 · Clientes | Gerencia comercial | Confidencial | Clientes | sí |
| DS-02 · Movimientos | — | Restringida | Transaccional | no |
| DS-03 · Proveedores | Compras | — | Proveedores | sí |
| DS-04 · Candidatos | Gestión humana | Confidencial | Candidatos | sí |
| DS-05 · Indicadores de gestión | Planeación | Interna | Transaccional | no |
| DS-12 · Pagos a proveedores | — | Interna | Transaccional | no |
| DS-13 · Campañas de mercadeo | — | Interna | Transaccional | no |
| DS-22 · Contratos con proveedores | Compras | — | Proveedores | no |
| DS-23 · Inventario de activos | Compras | — | Transaccional | no |
| DS-32 · Beneficiarios | Gerencia comercial | Confidencial | Clientes | sí |
| DS-33 · Visitantes de las sedes | Gerencia comercial | Confidencial | Clientes | sí |
| DS-42 · Candidatos a prácticas | Gestión humana | Interna | Candidatos | no |
| DS-43 · Proveedores históricos | Compras | Interna | Proveedores | no |

El dueño y la clasificación los asigna el área: aquí se dice cuál falta.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-catalogo/catalogo_datos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-catalog-check-1`. Lo mostrado está en `estado-datos/901555777-banco-cordillera-sintetico/corridas/salida-catalog-check.md`.