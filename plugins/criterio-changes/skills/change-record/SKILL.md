---
name: change-record
description: "Cómo se registra en la ficha del periodo de Fausto cada aprobación de un cambio y cada revisión posterior que quedó en un acta del comité de cambios, con la cita. Úsalo al procesar las actas de `10-cambios/`. Change record, approval, post-implementation review."
---

# La ficha del periodo de Fausto

Una ficha por periodo, en `<estado>/cambios/<AAAA-MM>/ficha.json`. La exportación de cambios, los despliegues, los incidentes, los problemas y la disponibilidad no se copian aquí: los procesa el motor. Aquí va lo que solo traen las actas del comité de cambios.

```json
{
  "approvals": [{"change": "CHG-1001", "date": "2026-10-02", "authority": "Comité de cambios",
                 "source": "10-cambios/acta_comite_de_cambios_2026-10-02.pdf"}],
  "reviews": [{"change": "CHG-1003", "date": "2026-10-14",
               "source": "10-cambios/acta_comite_de_cambios_2026-10-16.pdf"}],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`approvals`**: cada cambio que el acta aprueba, con el código del cambio como lo escribe la exportación, la fecha en que se aprobó —la de la sesión, si el acta no dice otra— y la autoridad que lo aprobó, en las palabras del acta. Un cambio que el acta menciona sin aprobarlo —«se aplaza», «se pide más información»— no va aquí.
- **`reviews`**: cada revisión posterior de un cambio que quedó en un acta —la de un cambio de emergencia o la de uno fallido o revertido—, con el código del cambio y la fecha en que se revisó. Que el acta diga que el cambio «se revisará» no es una revisión.
- **`reviewed`**: las actas que se procesaron y no traen ninguna aprobación ni revisión. Un acta citada en otro campo no va aquí.

## Lo que nunca va

- Una aprobación que no está en un acta: si la exportación dice «aprobado» y ninguna acta lo dice, no va a la ficha, y el motor lo dice.
- Un juicio sobre si un cambio debió aprobarse o sobre su riesgo.
