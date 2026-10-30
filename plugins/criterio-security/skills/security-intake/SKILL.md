---
name: security-intake
description: "Qué documentos procesa la familia CISO, dónde va cada uno, qué tablas procesa el motor directamente, qué extrae el agente a la ficha y qué nunca se abre. Úsalo al recorrer la carpeta de seguridad de una entidad, al recibir una evidencia, una exportación del escáner, un informe de incidente o una prueba, al explicar dónde va un archivo o cuando una tabla no trae las columnas esperadas. Security document intake, folder structure."
---

# Los documentos de la seguridad de la información

## Dos clases de documento, dos formas de procesarlo

**Las tablas las procesa el motor directamente.** La declaración de aplicabilidad, la tabla de sistemas, el registro de terceros, el inventario de activos, la matriz de notificaciones, el calendario de continuidad, el registro de riesgos, cada exportación del escáner, el catálogo KEV, el seguimiento de la remediación y el registro de excepciones llegan como `.csv` o `.xlsx`. Nada de eso se transcribe ni se resume: `seguridad.py` lo procesa con su fila de origen, que es la cita.

**Lo que solo trae un documento escrito lo extrae el agente a la ficha.** La evidencia de un control, la revisión de accesos de un sistema, la evaluación de un tercero —Alexis, con **control-evidence-record**—; la política con sus plazos —Guillermo y Amparo, en su setup—; el informe de un incidente con su línea de tiempo y sus notificaciones, su revisión posterior y cada prueba de continuidad —Amparo, con **incident-record** y **continuity-record**—. Se convierte con `seguridad.py convertir` y se registra con su cita. El código no lo inventa ni lo infiere.

## Lo que nunca se abre

**Credenciales, llaves y respaldos.** Un `.pem`, un `.key`, un `.pfx`, un `.kdbx`, un `.ovpn`, un volcado de base de datos, un archivo comprimido o un archivo cuyo nombre dice que es una contraseña o un secreto. `seguridad.py excluidos` los lista con su motivo; el agente no los abre con Read ni de ninguna otra forma, y el reporte dice qué excluyó. Si la persona los dejó en la carpeta, se le sugiere sacarlos: la carpeta de evidencia no es un lugar para secretos.

## Las columnas de una tabla

El motor reconoce las columnas por su nombre y por sus variantes más comunes:

| Tabla | Archivo, por cómo empieza su nombre | Columnas que necesita | Opcionales | En `columns` |
|---|---|---|---|---|
| La declaración de aplicabilidad | `00-referencia/declaracion`, `soa` o `aplicabilidad` | `control`, `aplicable` | `nombre`, `estado`, `responsable`, `periodicidad` | `soa` |
| Los sistemas | `00-referencia/sistemas` | `sistema`, `revision_dias` (cada cuántos días se revisan sus accesos) | `criticidad`, `responsable` | `systems` |
| Los terceros | `00-referencia/terceros` | `tercero`, `evaluacion_dias` | `critico` (sí o no), `servicio` | `third_parties` |
| El inventario de activos | `00-referencia/inventario` o `activos` | `activo` | `alcance` (sí o no), `criticidad`, `responsable`, `tipo` | `assets` |
| La matriz de notificaciones | `00-referencia/matriz-notificaciones` | `destinatario`, `cuando`, `plazo_horas` | `norma` | `notifications` |
| El calendario de continuidad | `00-referencia/calendario` | `prueba`, `tipo` (continuidad, recuperación o restauración), `frecuencia_dias` | `sistema`, `responsable` | `calendar` |
| El registro de riesgos | `40-riesgos/registro-riesgos` | `riesgo`, `decision`, `revision` (la fecha de revisión) | `descripcion`, `aceptado_por` | `risks` |
| El seguimiento | `60-remediacion/seguimiento` | `activo`, `vulnerabilidad`, `estado` | `fecha_cierre`, `ticket` | `tracker` |
| Las excepciones | `60-remediacion/excepciones` | `vulnerabilidad`, `vence` | `activo` (vacío es todos), `aprobada_por` | `exceptions` |

Las exportaciones del escáner y el catálogo KEV, en **scanner-exports**. Cuando una tabla llama una columna de otra forma, el motor dice cuál falta. **No adivines**: pregúntale a la persona cómo se llama y regístralo en `columns` de la configuración, por tabla. Las fechas llegan en ISO, `dd/mm/aaaa` o como número de serie de Excel; la periodicidad, en días o en palabras —mensual, trimestral, semestral, anual—.

## La estructura recomendada

<!-- ciso:intake · generado por scripts/familias.py; no se edita a mano -->
Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo está fuera de su lugar y dónde iría (ADR 0007). La referencia tiene un solo lugar, `00-referencia/`, y los tres agentes la usan: Alexis procesa los controles, Guillermo las vulnerabilidades y Amparo los incidentes y las pruebas.

Una carpeta por entidad, con su identificación fiscal al inicio del nombre. Dentro, las políticas y los registros de referencia, la evidencia de cada control, las revisiones de acceso, las evaluaciones de terceros, el registro de riesgos, las exportaciones del escáner, la remediación, los incidentes, sus revisiones y las pruebas de continuidad. Nunca credenciales, llaves ni respaldos: el motor los excluye.

```
seguridad/
└── <entidad>/
    ├── 00-referencia/
    ├── 10-controles/
    ├── 20-accesos/
    ├── 30-terceros/
    ├── 40-riesgos/
    ├── 50-escaneos/
    ├── 60-remediacion/
    ├── 70-incidentes/
    ├── 80-revisiones/
    └── 90-continuidad/
estado-seguridad/
```

**`<entidad>/`** · Lo que la organización lleva para toda la seguridad de la información

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-referencia/` | Las políticas —de seguridad, de gestión de vulnerabilidades y de respuesta a incidentes—, la declaración de aplicabilidad, la tabla de sistemas, el registro de terceros, el inventario de activos, la matriz de notificaciones y el calendario de continuidad | Alexis, Guillermo, Amparo |
| `10-controles/` | La evidencia de cada control, con el número del control al inicio del nombre y el periodo que cubre: el informe, el registro, la captura o el acta que dice que el control operó | Alexis |
| `20-accesos/` | Las revisiones de acceso de cada sistema, con el sistema y la fecha en el nombre | Alexis |
| `30-terceros/` | Las evaluaciones de seguridad de cada tercero: el cuestionario, el informe o la certificación que entregó, con su fecha | Alexis |
| `40-riesgos/` | El registro de riesgos, con la decisión sobre cada uno, quién aceptó y hasta cuándo, y el documento de cada aceptación | Alexis |
| `50-escaneos/` | Las exportaciones del escáner de vulnerabilidades, en CSV o Excel, con la fecha del escaneo en el nombre, y el catálogo KEV de CISA tal como se descarga | Guillermo |
| `60-remediacion/` | El seguimiento de la remediación —cada vulnerabilidad con su estado y su fecha de cierre— y el registro de excepciones con su aprobación y su vencimiento | Guillermo |
| `70-incidentes/` | El informe de cada incidente, con su línea de tiempo —la detección, la contención y el cierre— y cada notificación que se hizo, con su constancia | Amparo |
| `80-revisiones/` | La revisión posterior de cada incidente: las lecciones aprendidas y las acciones que salen de ellas | Amparo |
| `90-continuidad/` | El informe de cada prueba del plan de continuidad, del de recuperación y de cada restauración de un respaldo, con su fecha y su resultado | Amparo |

**`estado-seguridad/`** · Lo que escriben Alexis, Guillermo y Amparo: la configuración, la ficha de cada periodo, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /ciso:intake -->
