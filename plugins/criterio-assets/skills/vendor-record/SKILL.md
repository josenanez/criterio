---
name: vendor-record
description: "Cómo se registra en la ficha del periodo de Domingo cada excepción aprobada sobre un activo sin soporte y cada nivel de servicio de un contrato con su crédito, con la cita. Úsalo al procesar las actas del comité de arquitectura de `30-activos/` y los contratos de `40-proveedores/`. Asset exception, service level, service credit."
---

# La ficha del periodo de Domingo

Una ficha por periodo, en `<estado>/activos/<AAAA-MM>/ficha.json`. El inventario, las licencias, el cumplimiento y las facturas de los proveedores, y la factura y el presupuesto de la nube no se copian aquí: los procesa el motor. Aquí va lo que solo traen las actas y los contratos.

```json
{
  "exceptions": [{"asset": "A-102", "until": "2027-03-31",
                  "source": "30-activos/acta_comite_de_arquitectura_2026-10.pdf"}],
  "service_levels": [{"vendor": "Nube Andina", "metric": "Disponibilidad", "target": 99.95, "credit_pct": 10,
                      "source": "40-proveedores/contrato_nube_andina.pdf"}],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`exceptions`**: cada activo al que el comité le aprueba seguir en producción sin el soporte de su fabricante, con el código del activo como lo escribe el inventario y la fecha hasta la que vale la excepción. Si el acta no dice hasta cuándo, `until` va vacío y se pregunta. Un activo que el acta solo menciona —«se evaluará su reemplazo»— no tiene excepción.
- **`service_levels`**: cada nivel de servicio de un contrato, con el proveedor como lo escriben sus facturas, la métrica como la escribe su reporte de cumplimiento, el nivel pactado como número —«99,95 %» es `99.95`— y el crédito que el contrato pacta si no se cumple, en porcentaje de la factura. Si el contrato no pacta crédito, `credit_pct` va vacío.
- **`reviewed`**: las actas y los contratos que se procesaron y no traen ninguna excepción ni nivel de servicio. Un documento citado en otro campo no va aquí.

## Lo que nunca va

- Una interpretación del contrato: si una cláusula es ambigua, se registra lo que dice y se pregunta; qué significa lo decide legal.
- Una excepción que no está en un acta.
