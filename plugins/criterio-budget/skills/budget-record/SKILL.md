---
name: budget-record
description: "La ficha del presupuesto: lo que el agente extrae de los documentos escritos —actas de aprobación y de traslado, lo que cada área declara, la versión que usa un informe, los compromisos del comité— con su cita. Úsalo al procesar un acta, una declaración de un área o el acta del comité anterior. Budget record, minutes, transfers, area statements."
---

# La ficha del presupuesto

Una por entidad y año: `<estado>/presupuesto/<AAAA>/ficha.json`. **La escribe el agente y nadie más**; el motor la lee y lo que calcula va a `resultados.json`.

## Qué lleva

```json
{
  "minutes": [
    {"type": "aprobacion", "version": 1, "date": "2026-01-20", "source": "presupuesto-2026/40-actas/acta-01-aprobacion.docx"},
    {"type": "traslado", "date": "2026-06-28", "source": "presupuesto-2026/40-actas/acta-05-traslados.docx",
     "movements": [{"from": {"area": "Comercial", "line": "Publicidad"}, "to": {"area": "Comercial", "line": "Eventos"}, "amount": 25000000}]}
  ],
  "area_statements": [{"area": "Comercial", "says": "dentro", "source": "presupuesto-2026/30-proyecciones/correo-comercial.eml", "date": "2026-09-30"}],
  "reports": [{"source": "informe-gerencia-septiembre.pdf", "budget_version": "1"}],
  "committee_commitments": [{"what": "Revisar el contrato de vigilancia", "owner": "Administración", "status": "abierto", "evidence": null, "source": "presupuesto-2026/40-actas/acta-06-comite.docx"}],
  "questions": [{"question": "¿Cuál es la versión aprobada?", "answer": "La 1, acta del 20 de enero"}]
}
```

- **`minutes`**: cada acta con su tipo —`aprobacion`, `traslado`, `adicion`, `reduccion`—. La de aprobación dice qué versión aprueba; la de traslado, cada movimiento con su línea de origen, de destino y su valor, tal como lo dice el acta. El área y la línea se escriben como en el presupuesto.
- **`area_statements`**: lo que un área afirma de su presupuesto —«estamos dentro»—, con la cita. El motor lo contrasta con los números y levanta `declared_vs_evidence` si no lo sostienen.
- **`reports`**: la versión del presupuesto que usa un informe, si la dice.
- **`committee_commitments`**: lo que el comité anterior dejó encargado, con su estado y la evidencia que lo prueba.

## Las reglas

Cada dato con su cita; un valor que el acta no dice no se calcula; «no encontrado» es una respuesta válida. Si `compute` trae `record_issues`, corrige la ficha y vuelve a calcular.
