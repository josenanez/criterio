---
name: obligations-matrix
description: "El modelo de la matriz de obligaciones de cumplimiento —id, fuente, responsable, periodicidad, fecha límite, evidencia esperada y criticidad— y cómo se decide si una obligación está cumplida, vencida o sin evidencia. Úsalo al configurar la matriz, al evaluar un periodo o cuando una fila no tiene responsable o fuente. Compliance obligations register, ISO 37301."
---

# La matriz de obligaciones

**Las obligaciones las define la organización.** Constanza no trae ninguna, no dice cuáles exige una norma y no completa una fila con lo que «suele» pedirse. Procesa la matriz que la organización lleva y la pone al lado de su evidencia.

El modelo sigue la idea de ISO 37301 (F-01): cada obligación con la fuente de la que sale, quien responde por ella y la evidencia que la prueba. Va en `00-referencia/matriz-obligaciones.csv` o `.xlsx`, con las columnas de `references/matriz-obligaciones.csv`:

| Columna | Qué va |
|---|---|
| `id` | Un id corto y único, `OB-07`. La evidencia empieza por él |
| `obligacion` | Qué hay que hacer, en una línea |
| `fuente` | La norma, el contrato o la política de la que sale, con su número: `Circular 027 de 2026`, `Contrato CTR-014 OBL-3`, `Política P-04` |
| `tipo` | Reporte, registro, capacitación, certificación… como la organización los clasifique |
| `responsable` | Quién responde por ella |
| `periodicidad` | `mensual`, `bimestral`, `trimestral`, `semestral`, `anual` o `única` |
| `dia_limite` | `día 15` del mes siguiente al periodo, `D+10` en días hábiles después del cierre del periodo, o una fecha |
| `evidencia_esperada` | Qué archivo la prueba |
| `criticidad` | `alta`, `media` o `baja` |
| `estado` | Lo que declara el responsable, si lo declara |

## Cómo decide el motor

La evidencia de una obligación es un archivo de `cumplimiento-<AAAA-MM>/10-evidencias/` cuyo nombre empieza por su id. El motor busca en la ventana de su periodicidad —el periodo, los tres últimos si es trimestral, los doce si es anual— y la clasifica:

| Estado | Cuándo | Señal |
|---|---|---|
| Cumplida con evidencia | Hay evidencia en la ventana | — |
| Cumplida sin evidencia | La matriz la declara cumplida y no hay evidencia | `compliance_done_without_evidence` |
| Vencida | Pasó su fecha límite sin evidencia | `compliance_obligation_overdue`, con la severidad de su criticidad |
| En plazo | Todavía no vence | `compliance_evidence_stale` si el ciclo anterior tampoco tuvo evidencia |

Además: `obligation_without_owner` y `obligation_without_source` para la fila que no tiene responsable o fuente, y `contract_obligation_not_in_matrix` cuando una obligación de cumplimiento de un contrato —de las fichas de Fidel, `kind: cumplimiento`— no aparece en la matriz. **Para que cruce, la `fuente` de la fila cita el código del contrato y el id de la obligación**: `Contrato CTR-014 OBL-3`.

El avance del periodo es el porcentaje de obligaciones con evidencia, ponderado por criticidad. Lo calcula el motor.

## Lo que nunca se hace

- Agregar, quitar o reescribir una obligación de la matriz.
- Decir que una norma exige algo, o que no lo exige.
- Dar por cumplida una obligación con una evidencia que no lleva su id en el nombre: se le pide a la persona que la nombre así.
