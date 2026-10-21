---
name: contract-calendar
description: "Cómo se arma el calendario de los contratos: la terminación con sus otrosíes, la fecha límite del preaviso de no renovación, la prórroga automática y cada obligación con fecha contra su evidencia. Úsalo al preparar el calendario de vencimientos, al explicar por qué un contrato aparece como prorrogado o cuando alguien pregunta qué vence. Contract expiry calendar, renewal notice, obligations tracking."
---

# Lo que vence

## Las fechas las calcula el motor

De la ficha de cada contrato, `legal.py` calcula:

- **La terminación documentada**: la del contrato, o la del último otrosí firmado que la cambió.
- **El límite del preaviso**, en un contrato con renovación automática: la terminación menos los `notice_days` que dice el contrato. Después de esa fecha, sin una decisión registrada, el contrato se prorroga en sus términos.
- **La terminación efectiva**: con renovación automática y sin decisión de terminar, la terminación avanza de prórroga en prórroga hasta hoy. Es la que usa el motor para decir si el contrato está vigente y si un pago cae por fuera.
- **Cada obligación con fecha** contra su evidencia en `40-ejecucion/` del contrato: un archivo cuyo nombre empieza por el id de la obligación.

No se recalcula ninguna fecha a mano. Si el reporte no trae una fecha, se dice qué dato de la ficha falta.

## Las señales

| Señal | Cuándo |
|---|---|
| `contract_expiring` | Un contrato sin renovación automática vence dentro de los días configurados y no tiene decisión registrada |
| `notice_deadline_near` | El límite del preaviso de un contrato con renovación automática cae dentro de los días configurados, sin decisión |
| `renewal_notice_missed` | Pasó el límite del preaviso sin decisión: el contrato se prorroga en sus términos |
| `contract_obligation_overdue` | Una obligación del contrato pasó su fecha y no hay evidencia en `40-ejecucion/` |

Una decisión registrada —en la ficha, con el documento que la toma— apaga las tres primeras. **La decisión la toma una persona**: Fidel muestra la fecha y la consecuencia que escribe el contrato, no recomienda renovar ni terminar.

## Lo que nunca se hace

- Contar días hábiles o calendario por criterio propio: los días son los que escribe el contrato, y si el contrato no lo dice, se pregunta.
- Dar por cumplida una obligación porque «seguro se entregó»: sin evidencia, no está.
- Decir si una prórroga es válida o si un preaviso tardío surte efecto.
