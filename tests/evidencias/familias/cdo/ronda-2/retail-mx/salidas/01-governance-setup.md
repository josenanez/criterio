# /criterio-data-governance:governance-setup datos/rcm190305ab1-retail-central-sintetico

Soy Custodia. Pongo cada dato del catálogo al lado de quien responde por él, de su clasificación y de su plazo; no asigno dueños ni borro nada.

Esta sesión no tenía a nadie que respondiera, así que tomé cada respuesta de lo que dicen los documentos:

- **Carpeta:** 1. `datos/rcm190305ab1-retail-central-sintetico`, con 00-referencia/, 10-catalogo/, 20-informes/ y 30-calidad/. Era la única candidata.
- **Entidad:** Retail Central Sintético · RFC RCM190305AB1 · México (MXN).
- **Periodo:** 2026-11.
- **Rostrum:** sí, porque la política de datos no dice otra cosa.
- **Estado:** `estado-datos/rcm190305ab1-retail-central-sintetico`.
- **Marca:** `_CRITERIO_DATOS.txt` quedó en la carpeta de la entidad.
- **Términos 1.6:** los aceptó José Francisco Ñáñez el 2026-11-25. Les mostré el `en_corto` tal cual. El comprobante está en `.criterio/terminos/aceptacion-criterio-data-governance-0.2.0-2026-11-25.md` y en el `.pdf` del mismo nombre.
- **Configuración:** `.criterio/gobierno/RCM190305AB1/config.json`.

Procesé las dos políticas y el informe de junta de octubre. A la ficha de 2026-11 llevé las dos políticas con su fecha de revisión, los cuatro plazos de conservación y los nueve términos del informe. El motor también encontró señales sobre la revisión de las políticas, la conservación, el registro de bases y el glosario; esas las muestran `/criterio-data-governance:retention-check` y `/criterio-data-governance:glossary-check`.

# Cada conjunto con su dueño · Retail Central Sintético · periodo 2026-11

**Entidad:** Retail Central Sintético (RCM190305AB1) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `catalog-check`

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

- ¿Qué carpeta es la de la entidad? → datos/rcm190305ab1-retail-central-sintetico (única candidata, con 00-referencia/, 10-catalogo/, 20-informes/ y 30-calidad/)
- Entidad, identificación fiscal y país → Retail Central Sintético · RFC RCM190305AB1 · México (MXN), según el nombre de la carpeta y los documentos
- Periodo → 2026-11, el mes en curso a la fecha de la prueba
- ¿Se publica en Rostrum? → Sí: la política de datos no dice otra cosa
- ¿Dónde se guarda el estado? → estado-datos/rcm190305ab1-retail-central-sintetico
- ¿Acepta los términos 1.6? → Sí, José Francisco Ñáñez, 2026-11-25
- ¿Se marca la carpeta con _CRITERIO_DATOS.txt? → Sí

## Fuentes

- `10-catalogo/catalogo_datos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

---

**El reloj:** no creé la tarea programada porque necesita un sí explícito y en esta sesión nadie lo dio. Para correrlo a mano: `/criterio-data-governance:governance-wake`.

**Cuándo vuelvo:** sin reloj.

La primera vez que pedí el reporte, el motor falló: en la ficha había escrito las preguntas con las claves `q`/`a` y el motor espera `question`/`answer`. Las corregí, volví a calcular y el reporte salió bien.

Lo que mostré quedó guardado en `estado-datos/rcm190305ab1-retail-central-sintetico/corridas/salida-governance-setup.md`, y la corrida quedó registrada como `2026-11-25-governance-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.