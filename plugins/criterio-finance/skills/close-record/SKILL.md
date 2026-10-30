---
name: close-record
description: "La ficha del cierre: lo que el agente extrae de los documentos escritos —el estado declarado, los requerimientos que llegaron por correo o en Word, las facturas de Honduras, las preguntas que hizo— con su cita. Úsalo al registrar una declaración del estado del cierre, un requerimiento del auditor fuera de la tabla, una factura con CAI o las respuestas de la persona. Close record, declared status, audit requests, CAI invoices."
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
  "invoices": {
    "08019002265431:000-001-01-00000120": {"number": "000-001-01-00000120", "cai": "3E5A1C-7B2D90-4F11A8-0C6E3B-92D4F7-11",
      "authorized_range": {"from": "000-001-01-00000001", "to": "000-001-01-00000500"}, "issue_deadline": "2026-12-31",
      "date": "2026-09-15", "issuer_rtn": "08019002265431", "customer_rtn": "08019010017725",
      "taxable": 10000.00, "isv": 1500.00, "total": 11500.00, "source": "2026-09/30-facturacion/recibidas/fr-000-001-01-00000120.pdf"}
  },
  "questions": [{"question": "¿Cuál es el periodo que se está cerrando?", "answer": "2026-09"}]
}
```

- **`declared`** es lo que alguien afirma sobre el estado del cierre, con la cita del documento y su fecha. Se registra tal cual: «cerrado», «en curso», «pendiente de ajustes». Si nadie lo declaró, el campo no va. Una declaración no es evidencia: el motor la compara contra las señales abiertas y, si dice cerrado y hay señales, levanta `declared_close_vs_evidence`.
- **`audit_requests`** son los requerimientos que no vienen en la tabla del auditor. Cada uno con su id, la solicitud, la fecha, el vencimiento si lo dice y la cita.
- **`invoices`** son las facturas de Honduras, que no tienen un XML (decisión 0024). Una por cada documento de `<AAAA-MM>/30-facturacion/emitidas/` y `recibidas/`, con el RTN del emisor y el número correlativo como llave —dos proveedores pueden tener el mismo número—, y los datos como los imprime la factura: la CAI, el rango autorizado (`from` y `to`), la fecha límite de emisión, la fecha de emisión, el RTN del emisor y del cliente, el subtotal gravado (`taxable`), el ISV y el total. Las cifras van como números, sin el símbolo de la moneda. En los demás países el campo no va: el motor procesa el XML.
- **`questions`** son las preguntas que hiciste en la corrida y la respuesta que tomaste. El reporte las muestra.

## Las reglas

- **Cada dato con su cita**: la ruta del documento relativa a la carpeta de la entidad.
- **Una fecha que nadie dijo no se calcula.** «Esta semana» no es una fecha: el campo queda vacío.
- **«No encontrado» es una respuesta válida.** Un campo sin dato no se llena para que la ficha se vea completa.
- Si `compute` devuelve `record_issues`, la ficha quedó contra estas reglas: corrígela y vuelve a calcular.
