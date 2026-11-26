# /criterio-data-governance:governance-setup datos/20605557771-aseguradora-pacifico-sintetica

Custodia quedó instalada para Aseguradora Pacífico Sintética (RUC 20605557771, Perú). En la primera revisión, el motor encontró 4 conjuntos del catálogo sin dueño o sin clasificación.

- **Carpeta:** `datos/20605557771-aseguradora-pacifico-sintetica`. Era la única candidata y ya tiene las cuatro carpetas de la estructura recomendada; la dejé marcada con `_CRITERIO_DATOS.txt`.
- **Respuestas tomadas de los documentos:** periodo 2026-11; publicar en Rostrum: sí, porque la política de datos no dice lo contrario; tolerancia 0.5 %, de la política de datos; el estado va en `estado-datos/20605557771-aseguradora-pacifico-sintetica`.
- **Configuración:** `.criterio/gobierno/20605557771/config.json`.
- **Términos 1.6:** los mostré tal cual y los registré como aceptados por José Francisco Ñáñez. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-data-governance-0.2.0-2026-11-25.md` y `.pdf`.

Procesé `00-referencia/` y `20-informes/`. A la ficha van 2 políticas, 4 plazos de conservación y 9 términos del informe de junta. El motor encontró 13 señales en total. Este reporte trae solo las 4 del catálogo. Las demás son de retención, del registro de bases y del glosario, y salen en `retention-check` y `glossary-check`.

# Cada conjunto con su dueño · Aseguradora Pacífico Sintética · periodo 2026-11

**Entidad:** Aseguradora Pacífico Sintética (20605557771) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `catalog-check`

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

---

**Cuándo vuelvo:** sin reloj. No creé la tarea programada porque pide un sí explícito y en esta prueba no lo hubo. Para correrlo a mano: `/criterio-data-governance:governance-wake`.

Lo que mostré quedó en `estado-datos/20605557771-aseguradora-pacifico-sintetica/corridas/salida-governance-setup.md`, y la corrida quedó registrada como `2026-11-25-governance-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.