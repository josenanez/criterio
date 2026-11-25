# /criterio-data-governance:governance-setup datos/rcm190305ab1-retail-central-sintetico

Custodia ya funciona sobre Retail Central Sintético (RFC RCM190305AB1, México). Aceptó los términos José Francisco Ñáñez, versión 1.6, el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-data-governance-0.1.0-2026-11-25.md` y en `.pdf`. La carpeta de datos quedó marcada con `_CRITERIO_DATOS.txt`.

Crucé el catálogo contra la política de datos y hay un conjunto sin clasificación de confidencialidad. `compute` también encontró una política con la revisión vencida y términos del informe que no están en el glosario. Esas señales salen en `/criterio-data-governance:retention-check` y `/criterio-data-governance:glossary-check`.

Respuestas que tomé de los documentos, una por pregunta:
- **Carpeta:** `datos/rcm190305ab1-retail-central-sintetico`, la única que encontré.
- **Entidad:** el nombre sale de la política de datos; el RFC y el país, del nombre de la carpeta.
- **Periodo:** 2026-11.
- **Publicar en Rostrum:** sí, porque la política de datos no dice lo contrario.
- **Dónde guardo lo que encuentro:** en `estado-datos/rcm190305ab1-retail-central-sintetico`.
- **Tolerancia entre una cifra y su fuente:** 0.5 %, según la política de datos.
- **Marcar la carpeta:** sí.

# Cada conjunto con su dueño · Retail Central Sintético · periodo 2026-11

**Entidad:** Retail Central Sintético (RCM190305AB1) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.1.0 · **Comando:** `catalog-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-03 · Proveedores: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 4 |

## El resultado

| Conjunto | Dueño | Clasificación | Tipo | Datos personales |
|---|---|---|---|---|
| DS-01 · Clientes | Gerencia comercial | Confidencial | Clientes | sí |
| DS-02 · Movimientos | Gerencia de operaciones | Restringida | Transaccional | no |
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

**Reloj:** no creé la tarea diaria porque nadie dio un sí explícito. Para correr la revisión a mano: `/criterio-data-governance:governance-wake`.

**Cuándo vuelvo:** sin reloj.

La configuración quedó en `.criterio/gobierno/RCM190305AB1/config.json` y la corrida quedó registrada como `2026-11-25-governance-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.