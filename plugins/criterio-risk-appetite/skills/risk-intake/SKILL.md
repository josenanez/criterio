---
name: risk-intake
description: "Qué documentos procesa la familia CRO, dónde va cada uno, qué tablas procesa el motor directamente y qué extrae el agente a la ficha. Úsalo al recorrer la carpeta de riesgos de una entidad, al recibir una matriz de riesgos, unos límites, una exposición, unos indicadores clave, una base de eventos o un acta, al explicar dónde va un archivo o cuando una tabla no trae las columnas esperadas. Risk office document intake, folder structure."
---

# Los documentos del área de riesgos

## Dos clases de documento, dos formas de procesarlo

**Las tablas las procesa el motor directamente.** La matriz de riesgos, los límites del marco, los indicadores clave con sus umbrales, la exposición de cada periodo, los planes de acción, los valores y las acciones de los indicadores y la base de eventos de pérdida llegan como `.csv` o `.xlsx`. Nada de eso se transcribe ni se resume: `riesgos.py` lo procesa con su fila de origen, que es la cita.

**Lo que solo trae un documento escrito lo extrae el agente a la ficha.** La fecha en que la junta revisó la declaración de apetito y cada exceso que aprobó el comité —Severo, con **appetite-record**—; cada acción sobre un indicador clave que quedó en un acta —Casandra, con **kri-record**—. Se convierte con `riesgos.py convertir` y se registra con su cita. El código no lo inventa ni lo infiere.

## Lo que nunca se hace

**Ningún agente se conecta a un sistema, fija un límite, aprueba un exceso ni calcula capital** (decisión 0035). Procesan las exportaciones y las cifras que reportan las áreas y los modelos de la organización; no los reemplazan.

## Las columnas de una tabla

El motor reconoce las columnas por su nombre y por sus variantes más comunes, en español, en portugués y en inglés:

| Tabla | Archivo, por lo que lleva su nombre | Columnas que necesita | Opcionales | En `columns` |
|---|---|---|---|---|
| La matriz de riesgos | `00-marco/matriz` | `riesgo` | `nombre`, `calificacion`, `proceso`, `dueno` | `matriz` |
| Los límites del marco | `00-marco/limites` | `limite`, `valor_del_limite` | `riesgo`, `metrica`, `sentido`, `dueno`, `proxima_revision`, `unidad` | `limites` |
| Los indicadores clave | `00-marco/indicadores` | `indicador` | `nombre`, `riesgo`, `umbral_de_alerta`, `umbral_de_limite`, `sentido`, `dueno` | `indicadores` |
| La exposición del periodo | `10-exposicion/exposicion` | `limite`, `exposicion` | `periodo`, `fecha_de_reporte`, `area` | `exposicion` |
| Los planes de acción | `10-exposicion/planes` | `limite` | `plan`, `responsable`, `fecha_compromiso` | `planes` |
| Los valores de los indicadores | `20-indicadores/valores` | `indicador`, `valor` | `periodo` | `valores` |
| Las acciones sobre los indicadores | `20-indicadores/acciones` | `indicador` | `accion`, `periodo`, `responsable` | `acciones` |
| La base de eventos de pérdida | `30-eventos/eventos` | `evento` | `fecha_de_ocurrencia`, `fecha_de_descubrimiento`, `fecha_de_registro`, `proceso`, `tipo`, `causa`, `monto`, `riesgo` | `eventos` |

El **sentido** de un límite es `máximo` —por omisión— o `mínimo`: un indicador de liquidez o de solvencia se excede por debajo. El de un indicador clave es `mayor` —por omisión, más es peor— o `menor`. Si hay varias exposiciones o varios archivos de valores, el motor toma el del periodo por su nombre (`exposicion_2026-10.xlsx`) o por su columna `periodo`.

Cuando una tabla llama una columna de otra forma, el motor dice cuál falta. **No adivines**: pregúntale a la persona cómo se llama y regístralo en `columns` de la configuración, por tabla.

## La estructura recomendada

<!-- cro:intake · generado por scripts/familias.py; no se edita a mano -->
Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo está fuera de su lugar y dónde iría (ADR 0007). El marco tiene un solo lugar, `00-marco/`, y los dos agentes lo usan: Severo procesa cada exposición contra su límite, y Casandra cada indicador contra su umbral y cada evento contra la matriz.

Una carpeta por entidad, con su identificación fiscal al inicio del nombre. Dentro, el marco de apetito con la matriz de riesgos, los límites y los indicadores clave; la exposición que reportan las áreas con sus planes de acción; los valores y las acciones de los indicadores; la base de eventos de pérdida, y las actas del comité de riesgos y de la junta.

```
riesgos/
└── <entidad>/
    ├── 00-marco/
    ├── 10-exposicion/
    ├── 20-indicadores/
    ├── 30-eventos/
    └── 40-actas/
estado-riesgos/
```

**`<entidad>/`** · Lo que el área de riesgos lleva de la entidad

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-marco/` | La declaración de apetito, la política de riesgo operacional con sus plazos, la matriz de riesgos de la segunda línea, los límites del marco y los indicadores clave con sus umbrales | Severo, Casandra |
| `10-exposicion/` | La exposición que reporta cada área contra cada límite, por periodo, con su fecha de reporte, y los planes de acción de los excesos | Severo |
| `20-indicadores/` | El valor de cada indicador clave por periodo y las acciones acordadas sobre los que están en alerta | Casandra |
| `30-eventos/` | La exportación de la base de eventos de pérdida: cada evento con sus fechas, su proceso, su tipo, su causa, su monto y su riesgo | Casandra |
| `40-actas/` | Las actas del comité de riesgos y de la junta, con los excesos aprobados, la revisión de la declaración y las acciones sobre los indicadores | Severo, Casandra |

**`estado-riesgos/`** · Lo que escriben Severo y Casandra: la configuración, la ficha de cada periodo, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /cro:intake -->
