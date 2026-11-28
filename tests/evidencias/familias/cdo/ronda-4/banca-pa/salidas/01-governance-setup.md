# /criterio-data-governance:governance-setup datos/155698765-2-2018-banco-canal-sintetico

Soy Custodia. Pongo cada dato del catálogo al lado de quien responde por él, de su clasificación y de su plazo; no asigno dueños ni borro nada.

**Carpeta:** encontré una sola candidata, `datos/155698765-2-2018-banco-canal-sintetico`, con 00-referencia/, 10-catalogo/, 20-informes/ y 30-calidad/. Tomé el sí. Tiene 11 documentos, todos en su lugar y ninguno ilegible.

**Preguntas y la respuesta sugerida que tomé en cada una:**
1. **Entidad:** Banco Canal Sintético, identificación fiscal 155698765-2-2018, Panamá (PA), moneda USD.
2. **Periodo:** 2026-11.
3. **¿Se publica en Rostrum?** Sí; la política de datos no dice otra cosa.
4. **Dónde guardo lo que encuentro:** en `estado-datos/155698765-2-2018-banco-canal-sintetico`.
5. **Términos:** se mostró el texto de la versión 1.6 tal cual. Los aceptó José Francisco Ñáñez el 2026-11-25.
6. **¿Dejo la marca `_CRITERIO_DATOS.txt` en la carpeta?** Sí.

**Listo:**
- **Configuración:** `.criterio/gobierno/155698765-2-2018/config.json`
- **Comprobante de aceptación:** `.criterio/terminos/aceptacion-criterio-data-governance-1.1.0-2026-11-25.md` y su `.pdf`
- **Marca:** quedó en la carpeta de la entidad.

**Primera ficha (2026-11):** de `00-referencia/` llevé a la ficha 2 políticas con sus fechas de revisión y 4 plazos de conservación. Del informe a la junta de octubre llevé 9 términos. El cálculo del periodo dejó 13 señales.

# Cada conjunto con su dueño · Banco Canal Sintético · periodo 2026-11

**Entidad:** Banco Canal Sintético (155698765-2-2018) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 1.1.0 · **Comando:** `catalog-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-02 · Movimientos: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 3 |
| 2 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-12 · Pagos a proveedores: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 7 |
| 3 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-03 · Proveedores: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 4 |
| 4 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-22 · Contratos con proveedores: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 8 |

## El resultado

| Conjunto | Dueño | Clasificación | Tipo | Datos personales |
|---|---|---|---|---|
| DS-01 · Clientes | Gerencia comercial | Confidencial | Clientes | sí |
| DS-02 · Movimientos | — | Restringida | Transaccional | no |
| DS-03 · Proveedores | Compras | — | Proveedores | sí |
| DS-04 · Candidatos | Gestión humana | Confidencial | Candidatos | sí |
| DS-05 · Indicadores de gestión | Planeación | Interna | Transaccional | no |
| DS-12 · Pagos a proveedores | — | Interna | Transaccional | no |
| DS-22 · Contratos con proveedores | Compras | — | Proveedores | no |
| DS-32 · Beneficiarios | Gerencia comercial | Confidencial | Clientes | sí |
| DS-42 · Candidatos a prácticas | Gestión humana | Interna | Candidatos | no |

El dueño y la clasificación los asigna el área: aquí se dice cuál falta.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-catalogo/catalogo_datos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

**Las otras 9 señales** son políticas con la revisión vencida, plazos de conservación superados, bases personales sin registrar y términos que faltan en el glosario. Se ven con `/criterio-data-governance:retention-check` y `/criterio-data-governance:glossary-check`.

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta prueba nadie lo dio. Para correrlo a mano: `/criterio-data-governance:governance-wake`.

La corrida quedó registrada como `2026-11-25-governance-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.