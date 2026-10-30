---
name: correspondence-record
description: "Cómo se lleva a la ficha un correo guardado: si pide respuesta, qué pide, para cuándo y si es rutinario, con su cita; y cómo se escribe el borrador de una respuesta rutinaria sin enviarla nunca. Úsalo al procesar la correspondencia de la oficina. Correspondence triage, email record, draft replies."
---

# La ficha de un correo

Una por correo guardado —`.eml`, o `.msg` de Outlook— que no salió de la oficina, en `<estado>/correspondencia/<nombre del archivo sin extensión>.json`:

```json
{
  "file": "20-correspondencia/2026-10-10-regulador.eml",
  "asks_reply": true,
  "ask": "Respuesta al requerimiento 45 sobre la cartera reestructurada",
  "due": "2026-10-20",
  "routine": false,
  "source": "20-correspondencia/2026-10-10-regulador.eml, párrafo 2"
}
```

## Las reglas

1. **Los encabezados los procesa el motor**: quién, cuándo, el asunto y a qué mensaje responde. Si una respuesta de la oficina está guardada, el motor la encuentra por su `In-Reply-To`; no la marques tú.
2. **`asks_reply`** es verdadero solo si el correo pide una respuesta o una acción de la oficina. Un informe que llega para conocimiento no la pide.
3. **`due` es la fecha que el correo fija**, con su cita. Una cita de un correo es `<archivo>, párrafo N`, y puede llevar el texto citado entre « » después. Si no fija ninguna, queda vacía: el motor no inventa un plazo.
4. **`routine`** es verdadero solo para lo que se responde con un acuse, una confirmación de recibo o una cita en la agenda ya aprobada. Un requerimiento de un supervisor, una queja o algo que compromete a la entidad **nunca es rutinario**.
5. **El borrador de una respuesta rutinaria** va en `90-borradores/BORRADOR-respuesta-<nombre del correo>.md`, con `BORRADOR — no enviado` en la primera línea. **Nunca envías**: quien responde es una persona.
