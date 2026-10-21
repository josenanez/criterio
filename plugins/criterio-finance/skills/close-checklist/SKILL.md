---
name: close-checklist
description: "El checklist del cierre: el modelo de columnas, cómo se prueba cada tarea con su soporte, el calendario en días hábiles y el checklist recomendado por industria como borrador. Úsalo al cargar o revisar el checklist, al explicar por qué una tarea cumplida no tiene evidencia o al recomendar uno. Month-end close checklist, evidence, critical path."
---

# El checklist del cierre

## El modelo

Una hoja en `00-referencia/checklist-cierre.xlsx` (o `.csv`) con estas columnas:

| Columna | Qué lleva | Obligatoria |
|---|---|---|
| `id` | Identificador único de la tarea, por ejemplo `C-07` | Sí |
| `tarea` | Qué se hace | Sí |
| `area` | Contabilidad, tesorería, impuestos, nómina… | No |
| `responsable` | Una persona, no un área | Sí |
| `dia_limite` | Día hábil del cierre en que vence (`D+3`) o una fecha | Sí |
| `depende_de` | Ids de las tareas que tienen que estar antes | No |
| `evidencia_esperada` | Qué documento la prueba | No |
| `criticidad` | Alta, media o baja | No (media) |
| `estado` | Lo que declara el equipo: cumplida, en curso, pendiente | No |

`D+3` es el tercer día hábil después del fin de mes, sin sábados, domingos ni los festivos de `holidays` en la configuración.

## Cuándo una tarea está cumplida

**Cuando un soporte lo prueba**: un archivo en `<AAAA-MM>/40-soportes/` cuyo nombre empieza por el id de la tarea (`C-07-conciliacion-firmada.pdf`). Que la columna `estado` diga cumplida no la cierra: queda *cumplida sin evidencia* y se señala `close_task_done_without_evidence`. Una tarea sin evidencia después de su día límite es `close_task_overdue`; una que espera a otra sin evidencia queda *bloqueada por otra*.

El avance se calcula con evidencia y declarado, los dos ponderados por criticidad (alta 3, media 2, baja 1), y la ruta crítica es la cadena más larga de tareas sin evidencia siguiendo sus dependencias.

## El checklist recomendado

Si la organización no tiene uno, Clara ofrece el de `references/checklist-recomendado.csv`: las tareas comunes a cualquier cierre y las propias de cada industria de las pruebas —banca, cooperativas, retail y minería—. **Es un borrador**: no es una norma ni lo exige ninguna. Se activa con `checklist.source: "recomendado"` e `checklist.industry` en la configuración, y mientras una persona no lo apruebe (`checklist.approved: true`) el reporte lo dice. Los responsables vienen por rol; la persona los cambia por nombres.
