---
name: contract-record
description: "Cómo se lleva a la ficha lo que dice un contrato: partes, valor, fechas, renovación, preaviso, firmantes, otrosíes, garantías, certificado de la contraparte, obligaciones y la decisión de renovar o terminar, cada dato con su cita. Úsalo al procesar un contrato, un otrosí, una póliza o un acta que decide sobre un contrato. Contract record extraction, contract data, amendments."
---

# La ficha de un contrato

Una ficha por contrato, en `<estado>/contratos/<código>.json`. **Lo que el documento no dice se deja vacío**: una fecha, un monto o un firmante que nadie escribió no se completa por contexto ni por costumbre. El motor valida la ficha y dice qué le falta (`record_issues`).

## Los campos

```json
{
  "code": "CTR-014",
  "type": "servicios",
  "counterparty": {"name": "Soluciones Andinas S.A.S.", "id": "901234567"},
  "value": 480000000,
  "start": "2025-11-01",
  "end": "2026-10-31",
  "signed_on": "2025-10-28",
  "signed_by_both": true,
  "auto_renewal": true,
  "notice_days": 60,
  "renewal_months": 12,
  "signatories": [{"name": "Marta Ríos", "role": "Gerente general", "party": "entidad"},
                  {"name": "Luis Pardo", "role": "Representante legal", "party": "contraparte"}],
  "amendments": [{"id": "OT-1", "date": "2026-04-15", "added_value": 60000000, "new_end": null,
                  "signed": true, "signed_by": "Marta Ríos", "source": "contratos/CTR-014-soluciones/10-contrato/otrosi-1.pdf"}],
  "guarantees_required": [{"type": "cumplimiento", "months_after_end": 4, "source": "…/contrato.pdf, cláusula 12"}],
  "guarantees_provided": [{"type": "cumplimiento", "until": "2027-02-28", "insurer": "…", "source": "contratos/CTR-014-soluciones/20-garantias/poliza-cumplimiento.pdf"}],
  "counterparty_certificate": {"issued_on": "2025-10-10", "source": "contratos/CTR-014-soluciones/30-contraparte/certificado.pdf"},
  "obligations": [{"id": "OBL-1", "what": "Informe mensual de servicio", "due": "2026-10-05", "who": "Soluciones Andinas",
                   "kind": "entrega", "source": "…/contrato.pdf, cláusula 5"}],
  "decision": {"action": "renovar", "date": "2026-08-20", "source": "contratos/CTR-014-soluciones/40-ejecucion/acta-comite.pdf"},
  "source": "contratos/CTR-014-soluciones/10-contrato/contrato.pdf"
}
```

## Cómo se decide cada uno

- **`value`** es el valor inicial que dice el contrato, sin los otrosíes: cada otrosí lleva su `added_value`. El motor suma.
- **`end`** es la terminación del contrato original. Si un otrosí la cambia, va en su `new_end`; el motor toma la del último otrosí firmado.
- **`auto_renewal`** es verdadero solo si el contrato dice que se prorroga sin un acto nuevo. **`notice_days`** son los días de anticipación con que se avisa la no renovación, como los escribe el contrato. **`renewal_months`**, por cuánto se prorroga; si no lo dice, se deja vacío y el motor usa el de la configuración.
- **`signed_by_both`** es verdadero cuando el documento tiene la firma de las dos partes. Un documento sin firmar, o firmado por una sola, es `false`; un otrosí en ese estado lleva `"signed": false`.
- **`signatories`**: cada firmante con su nombre como aparece en el documento y `party` `entidad` o `contraparte`. El nombre se escribe igual que en la matriz de atribuciones para que el motor lo cruce; si no coincide, se pregunta.
- **`guarantees_required`**: lo que el contrato exige, con su vigencia como la escribe —una fecha (`until`) o meses después de la terminación (`months_after_end`)—. **`guarantees_provided`**: lo que dice cada póliza de `20-garantias/`, con su vigencia.
- **`obligations`**: cada obligación con fecha que el contrato establece, con un id propio, su fecha (`due`), quién la cumple (`who`) y la cláusula. **`kind`** es `cumplimiento` cuando la obligación es regulatoria o de cumplimiento —reportar a un supervisor, mantener una certificación, entregar una declaración de origen de fondos—: esas las cruza Constanza con la matriz.
- **`decision`** solo se registra cuando un documento la toma: un acta, un correo de quien decide, una carta de preaviso. **Que el agente piense que conviene renovar no es una decisión.**

## La cita

Cada dato apunta al documento del que salió en `source`, con la cláusula o la página cuando el documento la tiene. Lo que se dedujo de otro dato no es un dato: no va.

## Lo que nunca se hace

- Interpretar una cláusula ambigua: se registra lo que dice y la duda va a `questions` de la ficha del periodo o a la conversación.
- Calificar la validez del contrato, de una firma o de una garantía.
- Recomendar renovar, terminar o renegociar.
