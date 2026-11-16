---
name: occupation-standard
description: "El estándar de ocupaciones contra el que Norma revisa cada perfil: la descarga oficial de la CUOC del DANE o de O*NET, el código de cada ocupación, el umbral de importancia de O*NET, el nivel de competencia y la equivalencia de los estudios de la organización con la CINE. Úsalo en el setup de Norma, al armar un perfil nuevo o cuando un código no aparece. Occupational standard, CUOC, O*NET, ISCO."
---

# El estándar de ocupaciones

**El estándar lo elige la organización** y se procesa desde su descarga oficial, tal cual, en `00-referencia/`. Aquí no se teclea una ocupación, una destreza ni un nivel.

| Estándar | La descarga | El código | Lo que trae por ocupación |
|---|---|---|---|
| **CUOC 2026** del DANE (F-03), por omisión en Colombia | El Excel de los perfiles ocupacionales, `PerfilesOcupacionales-Excel-CUOC-2026.xlsx`, con sus hojas Ocupación, Funciones, Denominaciones, Nivel Competencia, Conocimientos, Destrezas, Ocupaciones Afines y Equivalencias | Cinco dígitos: `24111` | Descripción, funciones, denominaciones, nivel de competencia (1 a 4), conocimientos, destrezas, ocupaciones afines y su código CIUO-08 |
| **O*NET 31.0** (F-02) | La carpeta de la descarga en Excel, con Occupation Data, Task Statements, Job Zones, Essential Skills, Transferable Skills y Knowledge | `13-2011.00` | Título, tareas, zona de preparación y la importancia de cada destreza y conocimiento de 1 a 5 |

En la configuración: `standard.name` (`cuoc` u `onet`) y `standard.file`, la ruta dentro de la carpeta de documentos. Con O*NET, además, `standard.importance_threshold`: **desde qué importancia una destreza es exigible lo fija la organización**; O*NET no marca ninguna como esencial. `talento.py ocupacion --id <código>` trae una ocupación para comprobar que la descarga se procesa.

## El nivel de estudios

El documento de la CUOC 2026 (numeral 3.2) ata cada nivel de competencia a un nivel de la CINE 2011: el nivel 1 suele exigir CINE 1; el 2, CINE 2 a 4; el 3, CINE 5; el 4, CINE 6 o superior; y dice que la experiencia puede reemplazar la enseñanza formal. Para comparar, **la organización dice qué nivel de la CINE corresponde a cada forma suya de nombrar los estudios** en `education.levels` —por ejemplo `{"Bachiller": 3, "Técnico profesional": 5, "Profesional": 6}`—. El agente propone; la persona confirma. Un nivel que no está en la equivalencia no se compara: se dice. Con O*NET esta señal no se calcula: su zona de preparación describe la educación en los términos de los Estados Unidos.

## O*NET se atribuye

O*NET se usa bajo la licencia CC BY 4.0: un reporte que la cita dice de dónde sale —«O*NET 31.0 Database, USDOL/ETA»— y que se procesó.
