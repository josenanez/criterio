---
description: Arma el borrador de un perfil de cargo desde la ocupación de su estándar, con cada requisito atado a una tarea, para que una persona lo apruebe
argument-hint: "[código de la ocupación o nombre del cargo]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /profile-build — Un perfil nuevo desde su ocupación

> **Dónde está la configuración:** `.criterio/perfiles/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-roles:roles-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `talento.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No apruebas un perfil, no fijas un salario ni un cargo y no evalúas a una persona.** Dices qué perfil no tiene su ocupación, qué le falta frente a su estándar, qué requisito no se apoya en una tarea y qué pide que la ley o la política no permiten pedir; la decisión es de una persona. **Del estándar solo usas su descarga oficial**: ninguna ocupación, destreza ni nivel se escribe de memoria.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-roles:roles-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **occupation-standard** y **profile-record**.

## Flujo

**1. La ocupación.** Si el argumento trae un código, úsalo. Si trae el nombre de un cargo, búscalo en el índice de denominaciones de la descarga del estándar con Grep y propón las ocupaciones que lo nombran, con su código: **la persona elige**. Con el código, trae la ocupación del estándar:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" ocupacion --config <config> --id <código>
```

**2. El borrador.** Con lo que devuelve el motor —sus funciones, sus destrezas, sus conocimientos, su nivel de competencia y el nivel de la CINE que suele exigir—, propón el perfil: las tareas desde sus funciones, y cada requisito atado a una tarea y a una destreza o un conocimiento del estándar, con su fuente. Lo que la organización agregue que no esté en el estándar va marcado como suyo. **Ningún requisito pide la edad, el sexo, el estado civil, la fotografía ni un dato sensible.**

**3. Lo que decide la persona**, en una lista: el nivel de estudios con su equivalencia en `education.levels`, si acepta experiencia en lugar del título, qué requisitos son indispensables y lo que excluye del estándar con su motivo.

**4. Déjalo como borrador** en `<estado>/perfiles/borradores/<código de la ocupación>-<aaaa-mm-dd>.md`, con «BORRADOR» en la primera línea. **Nunca lo escribas entre los documentos de la organización**: el perfil lo aprueba una persona y lo deja ella en `10-perfiles/`.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-profile-build.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" corrida --config <config> --what profile-build \
    --salida <estado>/corridas/salida-profile-build.md \
    --caso <código de la ocupación> \
    --nota "ocupación, borrador y lo que decide la persona"
```
