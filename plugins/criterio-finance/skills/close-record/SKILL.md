---
name: close-record
description: "La ficha del cierre: lo que el agente extrae de los documentos escritos —el estado declarado, los requerimientos que llegaron por correo o en Word, las preguntas que hizo— con su cita. Úsalo al registrar una declaración del estado del cierre, un requerimiento del auditor fuera de la tabla, o las respuestas de la persona. Close record, declared status, audit requests."
---

# La ficha del cierre

Una por entidad y periodo: `<estado>/cierre/<AAAA-MM>/ficha.json`. **La escribe el agente y nadie más.** El motor la lee y no la reescribe; lo que calcula va a `resultados.json`, que el agente no toca. Así cada dato tiene un solo escritor.

## Qué lleva

```json
{
  "declared": {"status": "cerrado", "source": "2026-09/50-auditoria/correo-cierre.eml", "date": "2026-10-07", "by": "Contralor"},
  "audit_requests": [
    {"id": "R-07", "request": "Detalle de partidas conciliatorias de más de 90 días", "date": "2026-10-02",
     "due": "2026-10-09", "owner": "Tesorería", "status": "", "source": "2026-09/50-auditoria/requerimientos/carta-auditor.docx"}
  ],
  "questions": [{"question": "¿Cuál es el periodo que se está cerrando?", "answer": "2026-09"}]
}
```

- **`declared`** es lo que alguien afirma sobre el estado del cierre, con la cita del documento y su fecha. Se registra tal cual: «cerrado», «en curso», «pendiente de ajustes». Si nadie lo declaró, el campo no va. Una declaración no es evidencia: el motor la compara contra las señales abiertas y, si dice cerrado y hay señales, levanta `declared_close_vs_evidence`.
- **`audit_requests`** son los requerimientos que no vienen en la tabla del auditor. Cada uno con su id, la solicitud, la fecha, el vencimiento si lo dice y la cita.
- **`questions`** son las preguntas que hiciste en la corrida y la respuesta que tomaste. El reporte las muestra.

## Las reglas

- **Cada dato con su cita**: la ruta del documento relativa a la carpeta de la entidad.
- **Una fecha que nadie dijo no se calcula.** «Esta semana» no es una fecha: el campo queda vacío.
- **«No encontrado» es una respuesta válida.** Un campo sin dato no se llena para que la ficha se vea completa.
- Si `compute` devuelve `record_issues`, la ficha quedó contra estas reglas: corrígela y vuelve a calcular.
