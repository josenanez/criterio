# /criterio-data-governance:governance-setup datos/901555777-banco-cordillera-sintetico

Custodia quedó configurada para Banco Cordillera Sintético (NIT 901555777). El primer reporte encontró dos conjuntos del catálogo que hay que atender: Movimientos no tiene dueño y Proveedores no tiene clasificación de confidencialidad.

Como es una prueba, cada pregunta se resolvió con la respuesta sugerida:

- **Carpeta:** `datos/901555777-banco-cordillera-sintetico`, la única candidata. Tiene los 11 documentos en su lugar y todos se pudieron procesar.
- **Entidad:** Banco Cordillera Sintético, Colombia (COP). El país lo deduje del formato del NIT, porque ningún documento lo dice.
- **Periodo:** 2026-11.
- **Rostrum:** sí se publica, porque la política de datos no dice otra cosa.
- **Estado:** se guarda en `estado-datos/901555777-banco-cordillera-sintetico`.
- **Tolerancia:** 0.5 %, según la política de datos.
- **Términos:** versión 1.6, aceptados por José Francisco Ñáñez el 2026-11-25.
- **Marca:** dejé `_CRITERIO_DATOS.txt` en la carpeta.

La configuración está en `.criterio/gobierno/901555777/config.json`. El comprobante de la aceptación quedó en `.criterio/terminos/aceptacion-criterio-data-governance-0.1.0-2026-11-25.md` y en `.pdf`.

La corrida encontró además otras señales: una política vencida, un plazo de conservación excedido, una base personal sin registro y términos que no están en el glosario. Las detallan `/criterio-data-governance:retention-check` y `/criterio-data-governance:glossary-check`.

# Cada conjunto con su dueño · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.1.0 · **Comando:** `catalog-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-02 · Movimientos: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 3 |
| 2 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-03 · Proveedores: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 4 |

## El resultado

| Conjunto | Dueño | Clasificación | Tipo | Datos personales |
|---|---|---|---|---|
| DS-01 · Clientes | Gerencia comercial | Confidencial | Clientes | sí |
| DS-02 · Movimientos | — | Restringida | Transaccional | no |
| DS-03 · Proveedores | Compras | — | Proveedores | sí |
| DS-04 · Candidatos | Gestión humana | Confidencial | Candidatos | sí |
| DS-05 · Indicadores de gestión | Planeación | Interna | Transaccional | no |

El dueño y la clasificación los asigna el área: aquí se dice cuál falta.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-catalogo/catalogo_datos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

---

No programé la revisión diaria automática, porque necesita un sí explícito y en esta prueba nadie lo da. Se corre a mano con `/criterio-data-governance:governance-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-governance-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.