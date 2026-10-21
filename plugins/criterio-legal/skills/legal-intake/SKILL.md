---
name: legal-intake
description: "Qué documentos procesa la familia CLO, dónde va cada uno, qué tablas procesa el motor directamente y qué extrae el agente a la ficha. Úsalo al recorrer la carpeta legal de una entidad, al recibir un contrato, un otrosí, una póliza o una matriz nueva, al explicar dónde va un archivo o cuando una exportación no trae las columnas esperadas. Legal and compliance document intake, folder structure."
---

# Los documentos de la función legal y de cumplimiento

## Dos clases de documento, dos formas de procesarlo

**Las tablas las procesa el motor directamente.** El registro de contratos, la exportación de pagos por contrato, la matriz de atribuciones, la matriz de obligaciones, el índice de políticas, el registro normativo y el registro de casos del canal llegan como `.csv` o `.xlsx`. Nada de eso se transcribe ni se resume: `legal.py` lo procesa con su fila de origen, que es la cita.

**Lo que solo trae un documento escrito lo extrae el agente a la ficha.** El contrato y cada otrosí, la póliza, el certificado de existencia y representación de la contraparte, el acta o el correo en que alguien decide renovar o terminar, el informe de cumplimiento que declara un estado, el boletín que anuncia una norma. Se convierte con `legal.py convertir` y se registra en la ficha con su cita: la ficha de cada contrato con **contract-record**, la del periodo de cumplimiento con **compliance-record**. El código no lo inventa ni lo infiere.

## Las columnas de una tabla

El motor reconoce las columnas por su nombre y por sus variantes más comunes:

| Tabla | Archivo, por cómo empieza su nombre | Columnas que necesita | Opcionales |
|---|---|---|---|
| `register` | `10-registro/registro-contratos` | `codigo`, `valor`, `terminacion`, `estado` | `contraparte`, `objeto`, `tipo`, `inicio`, `responsable` |
| `payments` | `10-registro/pagos` | `contrato`, `fecha`, `valor` | `documento` |
| `authority` | `00-referencia/matriz-atribuciones` | `nombre`, `monto_maximo` | `cargo`, `tipo`, `desde`, `hasta` |
| `obligations` | `00-referencia/matriz-obligaciones` | `id`, `obligacion`, `periodicidad`, `dia_limite` | `fuente`, `tipo`, `responsable`, `evidencia_esperada`, `criticidad`, `estado` |
| `policies` | `20-politicas/indice-politicas` | `codigo`, `politica`, `proxima_revision` | `version`, `responsable`, `aprobada` |
| `regulatory` | `30-normativa/registro-normativo` | `id`, `norma`, `registrada` | `publicada`, `aplica`, `evaluacion`, `responsable` |
| `cases` | `40-canal/casos` | `id`, `recibido` | `respondido`, `tipo`, `estado` |

Cuando una tabla las llama de otra forma, el motor dice cuáles faltan. **No adivines**: pregúntale a la persona cómo se llama la columna y regístralo en `columns` de la configuración, por tabla. Los números llegan con coma o con punto decimal; las fechas en ISO, `dd/mm/aaaa` o como número de serie de Excel. El motor los normaliza; un valor que no puede procesar lo reporta.

## La evidencia se reconoce por su nombre

La evidencia de una obligación es un archivo cuyo nombre empieza por el id de la obligación y un guion bajo: `OB-07_informe-sagrilaft-sep.pdf`, `OBL-2_acta-entrega.pdf`. Va en `40-ejecucion/` del contrato si la obligación es del contrato, y en `cumplimiento-<AAAA-MM>/10-evidencias/` si es de la matriz. Un archivo con otro nombre no cuenta como evidencia, aunque lo sea: el inventario lo muestra y se le pide a la persona que lo nombre así.

## La estructura recomendada

<!-- clo:intake · generado por scripts/familias.py; no se edita a mano -->
Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo está fuera de su lugar y dónde iría (ADR 0007). Cada contrato tiene un solo lugar, su carpeta en `contratos/`: Fidel la procesa y Constanza toma de su ficha las obligaciones de cumplimiento.

Una carpeta por entidad, con el NIT o el RUC al inicio del nombre. Dentro, lo que la organización lleva para toda la entidad, una carpeta por contrato y una por periodo de cumplimiento.

```
legal/
└── <entidad>/
    ├── 00-referencia/
    ├── 10-registro/
    ├── 20-politicas/
    ├── 30-normativa/
    ├── 40-canal/
    ├── contratos/<código>/
    │   ├── 10-contrato/
    │   ├── 20-garantias/
    │   ├── 30-contraparte/
    │   └── 40-ejecucion/
    └── cumplimiento-<AAAA-MM>/
        ├── 10-evidencias/
        └── 20-reportes/
estado-legal/
```

**`<entidad>/`** · Lo que la organización lleva para toda la entidad

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-referencia/` | La matriz de atribuciones —quién firma qué y hasta qué monto— y la matriz de obligaciones de cumplimiento | Fidel, Constanza |
| `10-registro/` | El registro de contratos que lleva la organización y la exportación de pagos por contrato del ERP, con la fecha de corte en el nombre | Fidel |
| `20-politicas/` | El índice de políticas con su versión y su próxima revisión, y cada política | Constanza |
| `30-normativa/` | El registro normativo, los boletines y las evaluaciones de impacto de cada norma nueva | Constanza |
| `40-canal/` | El registro de casos del canal de denuncias, con su fecha de recepción y de respuesta | Constanza |

**`contratos/<código>/`** · Un contrato, con su código al inicio del nombre de la carpeta

| Carpeta | Qué va | Agente |
|---|---|---|
| `10-contrato/` | El contrato firmado y cada otrosí | Fidel |
| `20-garantias/` | Las pólizas y garantías aportadas | Fidel |
| `30-contraparte/` | El certificado de existencia y representación de la contraparte y sus documentos | Fidel |
| `40-ejecucion/` | Actas de entrega, informes y la evidencia de cada obligación, con su id al inicio del nombre | Fidel, Constanza |

**`cumplimiento-<AAAA-MM>/`** · Un periodo de cumplimiento

| Carpeta | Qué va | Agente |
|---|---|---|
| `10-evidencias/` | La evidencia de cada obligación del periodo, con su id al inicio del nombre | Constanza |
| `20-reportes/` | El informe de cumplimiento del periodo | Constanza |

**`estado-legal/`** · Lo que escriben Fidel y Constanza: la configuración, las fichas de cada contrato, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /clo:intake -->

## Lo que nunca se hace

- **Mover, renombrar o crear** algo dentro de los documentos de la organización. La estructura se sugiere; el inventario dice dónde iría cada archivo. La única excepción es la marca de la carpeta raíz, `_CRITERIO_<…>.txt`, que se deja solo con el sí de la persona y que ningún inventario cuenta como documento (ADR 0011).
- **Escribir el estado dentro de la carpeta de documentos.** El estado vive en `estado-legal/<entidad>/`.
- **Adivinar el formato** de un archivo que no se pudo procesar: se reporta con lo que le falta.
- **Calificar un documento.** Que un contrato sea válido, que una cláusula obligue o que una norma aplique lo decide una persona.
