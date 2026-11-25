---
name: data-intake
description: "Qué documentos procesa la familia CDO, dónde va cada uno, qué tablas procesa el motor directamente y qué extrae la agente a la ficha. Úsalo al recorrer la carpeta de datos de una entidad, al recibir un catálogo, un registro de bases, un glosario, un informe, un linaje, una regla de calidad o sus resultados, al explicar dónde va un archivo o cuando una tabla no trae las columnas esperadas. Data office document intake, folder structure."
---
<!-- COPIA · la fuente es plugins/criterio-data-governance/skills/data-intake/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# Los documentos del área de datos

## Dos clases de documento, dos formas de procesarlo

**Las tablas las procesa el motor directamente.** La exportación del catálogo, el registro de bases de datos personales, el glosario, el linaje, las cifras de la fuente, las reglas de calidad, sus resultados y la lista de datos críticos llegan como `.csv` o `.xlsx`. Nada de eso se transcribe ni se resume: `datos.py` lo procesa con su fila de origen, que es la cita.

**Lo que solo trae un documento escrito lo extrae la agente a la ficha.** Las políticas con su fecha de revisión, los plazos de conservación y los términos de los informes —Custodia, con **governance-record**—; cada cifra de un informe con su indicador, su valor y su corte —Ariadna, con **figure-record**—. Se convierte con `datos.py convertir` y se registra con su cita. El código no lo inventa ni lo infiere.

## Lo que nunca se procesa

**Ninguna agente se conecta a una base ni a un sistema, y ninguna procesa un dato personal** (decisión 0034). Procesan exportaciones; de una base con datos personales, solo sus metadatos: su nombre, su dueño, su clasificación y si está en el registro. Si llega una extracción con registros de personas, no se abre: se dice que llegó y que no se procesa.

## Las columnas de una tabla

El motor reconoce las columnas por su nombre y por sus variantes más comunes, en español y en inglés:

| Tabla | Archivo, por cómo empieza su nombre | Columnas que necesita | Opcionales | En `columns` |
|---|---|---|---|---|
| El catálogo de datos | `10-catalogo/catalogo` | `conjunto` | `nombre`, `dueno`, `clasificacion`, `tipo`, `datos_personales`, `dato_mas_antiguo`, `sistema` | `catalogo` |
| El registro de bases de datos personales | `10-catalogo/registro_de_bases` | `conjunto` | `numero_de_registro`, `fecha_de_registro` | `registro` |
| El glosario de negocio | `00-referencia/glosario` | `termino` | `definicion`, `dueno` | `glosario` |
| El linaje | `30-calidad/linaje` | `indicador` | `paso`, `sistema_de_origen`, `conjunto` | `linaje` |
| Las cifras de la fuente | `30-calidad/cifras_fuente` | `indicador`, `corte`, `valor` | — | `fuente` |
| Las reglas de calidad | `30-calidad/reglas_calidad` | `regla`, `dato` | `umbral` | `reglas` |
| Los resultados de las reglas | `30-calidad/resultados_calidad` | `regla`, `resultado` | `periodo` | `resultados` |
| Los datos críticos | `30-calidad/datos_criticos` | `dato` | `dueno` | `criticos` |

Cuando una tabla llama una columna de otra forma, el motor dice cuál falta. **No adivines**: pregúntale a la persona cómo se llama y regístralo en `columns` de la configuración, por tabla.

## La estructura recomendada

<!-- cdo:intake · generado por scripts/familias.py; no se edita a mano -->
Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo está fuera de su lugar y dónde iría (ADR 0007). La referencia tiene un solo lugar, `00-referencia/`, y las dos agentes la usan: Custodia procesa el catálogo contra las políticas y el glosario, y Ariadna cada cifra contra su fuente con la tolerancia de la política.

Una carpeta por entidad, con su identificación fiscal al inicio del nombre. Dentro, las políticas de datos y de conservación con el glosario de negocio, la exportación del catálogo con el registro de bases de datos personales, los informes de dirección con sus cifras, y el linaje, las cifras de la fuente y las reglas de calidad con sus resultados.

```
datos/
└── <entidad>/
    ├── 00-referencia/
    ├── 10-catalogo/
    ├── 20-informes/
    └── 30-calidad/
estado-datos/
```

**`<entidad>/`** · Lo que el área de datos lleva de la entidad

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-referencia/` | La política de datos —con sus tolerancias y sus plazos de revisión—, la política de conservación con el plazo de cada tipo de dato y el glosario de negocio | Custodia, Ariadna |
| `10-catalogo/` | La exportación del catálogo de datos —cada conjunto con su dueño, su clasificación, su tipo y su registro más antiguo— y el registro de bases de datos personales de la organización | Custodia |
| `20-informes/` | Los informes de dirección, de junta y al supervisor, con sus cifras y su fecha de corte | Custodia, Ariadna |
| `30-calidad/` | La exportación del linaje de cada cifra, las cifras de la fuente por corte, las reglas de calidad con su umbral, sus resultados por periodo y la lista de datos críticos | Ariadna |

**`estado-datos/`** · Lo que escriben Custodia y Ariadna: la configuración, la ficha de cada periodo, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /cdo:intake -->
