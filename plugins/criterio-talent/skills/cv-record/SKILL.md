---
name: cv-record
description: "Cómo se registra en la ficha del periodo de Cándido cada hoja de vida: cada título, certificación y empleo con su soporte y sus fechas, la evidencia de cada requisito del perfil y lo que llegó y no se debe tratar, sin copiar su valor. Úsalo al procesar `30-candidatos/`. CV record, supporting documents, protected data."
---

# La ficha del periodo de Cándido

Una ficha por periodo, en `<estado>/seleccion/<AAAA-MM>/ficha.json`. El registro de vacantes, el de autorizaciones y la exportación del ATS no se copian aquí: los procesa el motor. Los perfiles los trae Norma.

```json
{
  "candidates": [
    {"id": "CAN-014", "vacancy": "VAC-03", "folder": "30-candidatos/VAC-03/CAN-014/",
     "cv": "30-candidatos/VAC-03/CAN-014/hoja-de-vida.pdf", "received": "2026-09-12",
     "claims": [
       {"id": "K1", "type": "titulo", "text": "Contador público", "cv_source": "30-candidatos/VAC-03/CAN-014/hoja-de-vida.pdf, p. 1",
        "support": "30-candidatos/VAC-03/CAN-014/diploma.pdf", "requirement": "R4"},
       {"id": "K2", "type": "empleo", "text": "Analista contable en Comercial Andina", "from": "2019-03", "to": "2022-08",
        "cv_source": "30-candidatos/VAC-03/CAN-014/hoja-de-vida.pdf, p. 1",
        "support": "30-candidatos/VAC-03/CAN-014/certificado-laboral.pdf", "support_from": "2019-03-01", "support_to": "2022-08-31"},
       {"id": "K3", "type": "certificacion", "text": "Tarjeta profesional", "support": "30-candidatos/VAC-03/CAN-014/tarjeta.pdf",
        "expires": "2027-06-30", "requirement": "R5"}],
     "evidence": [{"requirement": "R1", "source": "30-candidatos/VAC-03/CAN-014/hoja-de-vida.pdf, p. 1",
                   "quote": "Cierre contable mensual bajo NIIF"}],
     "protected": [{"type": "fotografia", "source": "30-candidatos/VAC-03/CAN-014/hoja-de-vida.pdf, p. 1"}]}
  ],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`id`**: el identificador del candidato en la organización —el del ATS—, **nunca su nombre**. El nombre no va a la ficha.
- **`claims`**: cada título, certificación y empleo que **afirma** la hoja de vida. `support` es el archivo que lo soporta —el diploma, el acta, la certificación, el certificado laboral— o `null` si no llegó. Con un empleo, las fechas de la hoja de vida en `from` y `to` y las del certificado en `support_from` y `support_to`, como las dice cada uno. Con una certificación, su vencimiento en `expires`, del soporte. `requirement` es el requisito del perfil que esa afirmación atiende, si atiende alguno.
- **`evidence`**: para cada requisito del perfil, dónde está su evidencia en la hoja de vida o en un soporte, con la cita y una frase corta textual. **Solo lo que el documento dice**: nada de inferir la personalidad, la «cultura» o el potencial.
- **`protected`**: lo que llegó y no se debe tratar —`fotografia`, `edad`, `fecha_de_nacimiento`, `sexo`, `estado_civil`, `origen`, `religion`, `salud`, `documento_de_identidad`—, **solo su tipo y dónde está**. Su valor no se copia a ninguna parte.

## Lo que nunca va

- El nombre, la fotografía, la edad, el sexo, el estado civil, el origen, la salud o el número de documento de un candidato.
- Una brecha entre dos empleos como algo que señalar: no es una señal.
- Una afirmación que la hoja de vida no hace, o una fecha que ningún documento dice.
- Un juicio sobre la persona.
