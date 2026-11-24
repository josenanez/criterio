---
name: audit-intake
description: "Qué documentos procesa la familia CAE, dónde va cada uno, qué tablas procesa el motor directamente y qué extrae el agente a la ficha. Úsalo al recorrer la carpeta de auditoría de una entidad, al recibir un plan, un acta, un programa, un papel de trabajo, un informe, un registro de hallazgos o una evidencia, al explicar dónde va un archivo o cuando una tabla no trae las columnas esperadas. Internal audit document intake, folder structure."
---
<!-- COPIA · la fuente es plugins/criterio-audit-plan/skills/audit-intake/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# Los documentos de la auditoría interna

## Dos clases de documento, dos formas de procesarlo

**Las tablas las procesa el motor directamente.** El universo auditable, la matriz de riesgos, el plan anual, el equipo con sus horas y sus cargos anteriores, las asignaciones, el programa y el índice de papeles de cada trabajo, el registro de hallazgos y el de riesgos aceptados llegan como `.csv` o `.xlsx`. Nada de eso se transcribe ni se resume: `auditoria.py` lo procesa con su fila de origen, que es la cita.

**Lo que solo trae un documento escrito lo extrae el agente a la ficha.** Las actas del comité —Prudencia, con **plan-record**—; cada hallazgo de los papeles y del informe —Justo, con **finding-record**—; cada evidencia, cada explicación de atraso y cada hallazgo de un informe externo —Remedios, con **follow-up-record**—. Se convierte con `auditoria.py convertir` y se registra con su cita. El código no lo inventa ni lo infiere.

## La opinión es del auditor

**Ningún agente concluye sobre el control interno** (decisión 0033). No se cambia la prioridad de un hallazgo, no se cierra un plan, no se acepta un riesgo y no se edita un papel de trabajo. Las Normas Globales de Auditoría Interna se citan por su número y su título, nunca por su texto.

## Las columnas de una tabla

El motor reconoce las columnas por su nombre y por sus variantes más comunes, en español y en inglés:

| Tabla | Archivo, por cómo empieza su nombre | Columnas que necesita | Opcionales | En `columns` |
|---|---|---|---|---|
| El universo auditable | `10-plan/universo` | `unidad` | `nombre`, `nivel`, `ultimo_trabajo` | `universo` |
| La matriz de riesgos | `10-plan/matriz` | `riesgo`, `calificacion` | `descripcion`, `unidad` | `matriz` |
| El plan anual | `10-plan/plan` | `trabajo` | `nombre`, `unidad`, `riesgos`, `tipo`, `tema`, `inicio`, `cierre`, `estado`, `horas`, `requisito_tematico`, `cambio` | `plan` |
| El equipo | `00-referencia/equipo` | `auditor`, `horas_disponibles` | — | `equipo` |
| Los cargos anteriores | `00-referencia/cargos` | `auditor`, `unidad` | `desde`, `hasta` | `cargos` |
| Las asignaciones | `20-trabajos/asignaciones` | `trabajo`, `auditor` | `unidad`, `inicio`, `tipo` | `asignaciones` |
| El programa de un trabajo | `20-trabajos/<trabajo>/programa` | `paso` | `objetivo`, `papel`, `no_aplica` | `programa` |
| El índice de papeles | `20-trabajos/<trabajo>/indice` | `papel` | `paso`, `fecha`, `revisado_por`, `fecha_revision`, `aprobado_por`, `fecha_aprobacion` | `papeles` |
| El registro de hallazgos | `30-seguimiento/registro_hallazgos` | `hallazgo` | `trabajo`, `origen`, `proceso`, `condicion`, `prioridad`, `comunicado`, `plan`, `responsable`, `fecha_compromiso`, `reprogramaciones`, `estado`, `fecha_cierre`, `validado_por`, `referencia_externa` | `hallazgos` |
| Los riesgos aceptados | `30-seguimiento/riesgos_aceptados` | `riesgo` | `descripcion`, `fecha`, `por_encima_del_apetito`, `discutido_alta_direccion`, `resuelto`, `escalado_consejo` | `aceptados` |

Varios temas o riesgos en una celda van separados por punto y coma. Cuando una tabla llama una columna de otra forma, el motor dice cuál falta. **No adivines**: pregúntale a la persona cómo se llama y regístralo en `columns` de la configuración, por tabla.

## La estructura recomendada

<!-- cae:intake · generado por scripts/familias.py; no se edita a mano -->
Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo está fuera de su lugar y dónde iría (ADR 0007). La referencia tiene un solo lugar, `00-referencia/`, y los tres agentes la usan: Prudencia procesa el plan contra la matriz de riesgos, Justo cada trabajo contra la metodología y Remedios cada hallazgo hasta su cierre.

Una carpeta por entidad, con su identificación fiscal al inicio del nombre. Dentro, el estatuto y la metodología de auditoría con el equipo, el plan con el universo auditable, la matriz de riesgos y las actas del comité, una carpeta por trabajo con su programa, sus papeles y su informe, y el seguimiento de los hallazgos con sus evidencias.

```
auditoria/
└── <entidad>/
    ├── 00-referencia/
    ├── 10-plan/
    ├── 20-trabajos/
    └── 30-seguimiento/
estado-auditoria/
```

**`<entidad>/`** · Lo que la auditoría interna lleva de la entidad

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-referencia/` | El estatuto y la metodología de auditoría —los ciclos, la escala de prioridad, los plazos de seguimiento—, el informe de la última evaluación externa de calidad y el equipo: cada auditor con sus horas disponibles y los cargos que tuvo | Prudencia, Justo, Remedios |
| `10-plan/` | El universo auditable, la matriz de riesgos de la segunda línea, el plan anual con sus trabajos y sus horas, y las actas del comité que lo aprueban y lo cambian | Prudencia |
| `20-trabajos/` | Una carpeta por trabajo con su código: el programa de trabajo, el índice de papeles, los papeles de trabajo y el informe | Justo |
| `30-seguimiento/` | El registro de hallazgos y planes de acción, una carpeta por hallazgo con sus evidencias y explicaciones de atraso, el registro de riesgos aceptados y los informes del revisor fiscal, del auditor externo y del supervisor | Remedios |

**`estado-auditoria/`** · Lo que escriben Prudencia, Justo y Remedios: la configuración, la ficha de cada periodo, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /cae:intake -->
