---
name: talent-intake
description: "Qué documentos procesa la familia CHRO, dónde va cada uno, qué tablas procesa el motor directamente, qué extrae el agente a la ficha y qué nunca se pide ni se trata. Úsalo al recorrer la carpeta de talento de una entidad, al recibir un perfil de cargo, una hoja de vida, un soporte o una exportación del ATS, al explicar dónde va un archivo o cuando una tabla no trae las columnas esperadas. Talent document intake, folder structure."
---

# Los documentos del talento

## Dos clases de documento, dos formas de procesarlo

**Las tablas las procesa el motor directamente.** La descarga oficial del estándar de ocupaciones —el Excel de los perfiles ocupacionales de la CUOC o los archivos de O*NET—, el registro de vacantes, el de autorizaciones, la exportación del ATS y la base de talento interna llegan como `.csv` o `.xlsx`. Nada de eso se transcribe ni se resume: `talento.py` lo procesa con su fila de origen, que es la cita.

**Lo que solo trae un documento escrito lo extrae el agente a la ficha.** El perfil de cargo con sus tareas y sus requisitos —Norma, con **profile-record**—; cada hoja de vida con sus títulos, certificaciones y empleos, y cada soporte —Cándido, con **cv-record**—. Se convierte con `talento.py convertir` y se registra con su cita. El código no lo inventa ni lo infiere.

## Lo que nunca se pide ni se trata

**Ningún agente decide sobre una persona** (decisión 0031). No se rechaza, no se descarta, no se da un puntaje y no se ordenan candidatos por un número.

**Lo que no se trata:** la fotografía, la edad o la fecha de nacimiento, el sexo, el estado civil, el origen, la religión, la afiliación política o sindical, la salud y el número del documento de identidad de un candidato. Si llegan en una hoja de vida, la ficha registra solo **qué tipo de dato llegó y dónde**, nunca su valor, y el motor lo excluye del análisis y lo dice. Una imagen en la carpeta de un candidato que no es un soporte se toma por una fotografía.

**Lo que un perfil no puede pedir** lo dicen la ley de datos personales del país (`datos_sensibles.json`, con su artículo) y la política de selección de la organización (`selection.prohibited_requirements`).

## Las columnas de una tabla

El motor reconoce las columnas por su nombre y por sus variantes más comunes, en español y en inglés:

| Tabla | Archivo, por cómo empieza su nombre | Columnas que necesita | Opcionales | En `columns` |
|---|---|---|---|---|
| El registro de vacantes | `20-vacantes/registro-vacantes`, `vacantes` o `requisiciones` | `vacante`, `apertura` | `perfil`, `cierre`, `estado`, `plazo_dias`, `responsable` | `vacancies` |
| El registro de autorizaciones | `40-autorizaciones/registro-autorizaciones` o `autorizaciones` | `candidato`, `fecha` | `finalidad`, `fuente` | `authorizations` |
| La exportación del ATS | `50-ats/` con `ats`, `postulaciones` o `applications` en el nombre | `candidato`, `vacante` | `fecha` (de la postulación), `estado` (la etapa), `fecha_estado` | `ats` |
| La base de talento interna | `50-ats/base-interna` o `base-de-talento` | `persona` | `ocupacion` (su código), `cargo`, `area` | `internal` |

El estándar de ocupaciones, en **occupation-standard**. Cuando una tabla llama una columna de otra forma, el motor dice cuál falta. **No adivines**: pregúntale a la persona cómo se llama y regístralo en `columns` de la configuración, por tabla.

## La estructura recomendada

<!-- chro:intake · generado por scripts/familias.py; no se edita a mano -->
Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo está fuera de su lugar y dónde iría (ADR 0007). La referencia tiene un solo lugar, `00-referencia/`, y los dos agentes la usan: Norma procesa los perfiles contra el estándar de ocupaciones y Cándido la selección contra la política.

Una carpeta por entidad, con su identificación fiscal al inicio del nombre. Dentro, la política de selección y el estándar de ocupaciones, los perfiles de cargo, el registro de vacantes, una carpeta por candidato con su hoja de vida y sus soportes, las autorizaciones de tratamiento de datos y las exportaciones del ATS. Nunca la fotografía, la edad ni la salud de un candidato como requisito: el motor las excluye.

```
talento/
└── <entidad>/
    ├── 00-referencia/
    ├── 10-perfiles/
    ├── 20-vacantes/
    ├── 30-candidatos/
    ├── 40-autorizaciones/
    └── 50-ats/
estado-talento/
```

**`<entidad>/`** · Lo que la organización lleva para su selección y sus perfiles de cargo

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-referencia/` | La política de selección —el plazo de cobertura de una vacante, la conservación de los datos, quién aprueba— y la descarga oficial del estándar de ocupaciones: el Excel de los perfiles ocupacionales de la CUOC del DANE o la carpeta de O*NET | Norma, Cándido |
| `10-perfiles/` | Los perfiles de cargo y el manual de funciones, uno por cargo, con su código o su nombre en el archivo | Norma |
| `20-vacantes/` | El registro de vacantes: cada una con su perfil, su fecha de apertura y la de su cierre | Cándido |
| `30-candidatos/` | Una carpeta por vacante y, dentro, una por candidato con su identificador: la hoja de vida y sus soportes —diplomas, actas de grado, certificaciones y certificados laborales— | Cándido |
| `40-autorizaciones/` | El registro de autorizaciones de tratamiento de datos de los candidatos, con su fecha | Cándido |
| `50-ats/` | La exportación del sistema de selección (ATS) —cada candidato con su vacante, su postulación y su etapa— y la base de talento interna | Cándido |

**`estado-talento/`** · Lo que escriben Norma y Cándido: la configuración, la ficha de cada periodo, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /chro:intake -->
