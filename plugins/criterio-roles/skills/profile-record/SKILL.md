---
name: profile-record
description: "Cómo se registra en la ficha del periodo de Norma cada perfil de cargo: su ocupación en el estándar, sus tareas, cada requisito con la tarea y el elemento del estándar que lo apoyan, sus estudios, lo que no aplica con su motivo y su revisión, con la cita. Úsalo al procesar `10-perfiles/` o al armar un perfil nuevo. Job profile record."
---

# La ficha del periodo de Norma

Una ficha por periodo, en `<estado>/perfiles/<AAAA-MM>/ficha.json`. El estándar de ocupaciones no se copia aquí: lo procesa el motor. Aquí va solo lo que trae cada perfil.

```json
{
  "profiles": [
    {"id": "PC-07", "title": "Analista de crédito", "source": "10-perfiles/PC-07_analista-de-credito.docx",
     "occupation": {"standard": "cuoc", "code": "33121"},
     "education": {"label": "Tecnólogo", "source": "10-perfiles/PC-07_analista-de-credito.docx, p. 2"},
     "experience_alternative": true,
     "tasks": [{"id": "T1", "text": "Analizar las solicitudes de crédito y su documentación"}],
     "requirements": [
       {"id": "R1", "text": "Análisis de información financiera", "type": "conocimiento", "tasks": ["T1"],
        "element": "Finanzas", "essential": true, "source": "10-perfiles/PC-07_analista-de-credito.docx, p. 2"}],
     "not_applicable": [{"element": "Atención al cliente", "reason": "el cargo no atiende público"}],
     "last_review": "2026-02-01", "next_review": null}
  ],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`id`**: el código del perfil en la organización; si no tiene, el que trae el nombre del archivo.
- **`occupation.code`**: el código de la ocupación **tal como lo dice el perfil**. Si el perfil no lo dice, no se adivina: va vacío y el motor levanta la señal. El agente puede proponer uno con `talento.py ocupacion`, y lo registra solo con el sí de la persona.
- **`tasks`**: las funciones del perfil, cada una con su identificador.
- **`requirements`**: cada requisito como lo escribe el perfil, con su tipo (`destreza`, `conocimiento`, `estudio`, `experiencia`, `certificacion` u `otro`), **las tareas que lo apoyan** —las que el perfil relaciona o, si no lo hace, las que el texto hace evidentes; si ninguna, va vacío— y, si corresponde a una destreza o un conocimiento del estándar, su nombre o identificador en `element`. `essential` es `true` solo si el perfil lo dice indispensable.
- **`education.label`**: el nivel de estudios en las palabras del perfil; la equivalencia con la CINE la pone la configuración, no la ficha.
- **`experience_alternative`**: `true` si el perfil acepta experiencia en lugar del título.
- **`not_applicable`**: lo del estándar que el perfil excluye a propósito, **con su motivo**; sin motivo no cuenta.
- **`last_review`** y **`next_review`**: las fechas de revisión que trae el perfil.

## Lo que nunca va

- Un requisito que el perfil no trae, o una tarea que no dice.
- Un requisito reescrito para que no pida lo que pide: si dice «menor de 35 años», se registra así y el motor levanta la señal.
