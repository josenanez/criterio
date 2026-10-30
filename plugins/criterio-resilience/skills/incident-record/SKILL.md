---
name: incident-record
description: "Cómo se registra en la ficha del periodo de Amparo un incidente: su severidad, la detección, la contención y el cierre con su hora, los datos personales y los clientes afectados, cada notificación con su destinatario, su hora y su constancia, y su revisión posterior. Úsalo al procesar `70-incidentes/` o `80-revisiones/`. Incident timeline, notifications, post-incident review."
---

# La ficha del periodo de Amparo: los incidentes

Una ficha por periodo, en `<estado>/resiliencia/<AAAA-MM>/ficha.json`. La matriz de notificaciones y el calendario no se copian aquí: los procesa el motor. El orden de la línea de tiempo sigue la respuesta a incidentes del NIST SP 800-61 Rev. 3 (F-04); los plazos son los de la política de la organización.

```json
{
  "incidents": [
    {"id": "INC-0412", "title": "Ransomware en un servidor de archivos", "severity": "crítica",
     "detected_at": "2026-09-14T08:20", "contained_at": "2026-09-14T15:05", "closed_on": "2026-09-22",
     "personal_data": true, "customers_affected": false,
     "notifications": [
       {"to": "Superintendencia Financiera", "at": "2026-09-15T06:10",
        "source": "70-incidentes/INC-0412_notificacion-superintendencia.pdf"}
     ],
     "source": "70-incidentes/INC-0412_informe.docx, sección 2"}
  ],
  "reviews": [{"incident": "INC-0412", "date": "2026-09-30", "source": "80-revisiones/INC-0412_lecciones.pdf"}],
  "tests": [],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`id`**: el código del incidente como lo escribe el informe, el mismo con que empieza el nombre del archivo.
- **`severity`**: la que el informe le asignó, en el vocabulario de la política: crítica, alta, media o baja. Si el informe no la dice, va como pregunta; **el agente no la asigna**.
- **`detected_at`**, **`contained_at`**: fecha y hora, `AAAA-MM-DDTHH:MM`, como las dice la línea de tiempo del informe. La detección es cuando la organización supo del incidente, no cuando empezó el ataque. Si no hay contención registrada, se deja vacía: el motor lo cuenta.
- **`closed_on`**: el día en que el informe da el incidente por cerrado.
- **`personal_data`**, **`customers_affected`**: lo que dice el informe. Si no lo dice, `null` y una pregunta.
- **`notifications`**: una por constancia —el radicado, el correo enviado, el acuse— con su destinatario, su hora y su archivo. Una notificación que el informe menciona y de la que no hay constancia va con la cita del informe y la hora que él dice.
- **`reviews`**: la revisión posterior —las lecciones aprendidas— con su fecha y su archivo.
- **`reviewed`**: lo que se miró y no va —un borrador, un documento que no es de un incidente—, con su archivo y su motivo. Así el motor no lo vuelve a pedir.

## Lo que nunca va

- Un indicador de compromiso, una contraseña, una llave o un dato personal de un afectado.
- Una hora que el documento no dice.
- Una opinión sobre quién respondió bien o mal.
