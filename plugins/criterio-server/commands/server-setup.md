---
description: Arma el mapa de Rostrum. Encuentra en la carpeta de trabajo a cada agente de cada familia, muestra dónde está su estado y deja escrito lo que la persona confirma.
argument-hint: "[carpeta de trabajo] o vacío para la carpeta donde corre la sesión"
allowed-tools: Read, Glob, Grep, Bash(python3:*), Bash(ls:*)
---

# /server-setup — El mapa de las familias

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías. **Y sin subagentes en paralelo:** todo se hace en esta misma conversación, uno tras otro.

> **Rostrum no adivina dónde está nada.** Cada agente deja su configuración en `.criterio/<área>/config.json` o `.criterio/<área>/<instancia>/config.json` de la carpeta donde trabaja, y esa configuración dice dónde está su estado. El mapa se arma con eso, y **lo que no está en el mapa no se sirve** (ADR 0010).

## Flujo

**0. Preséntate, en una línea**

> Soy Rostrum. Publico lo que los agentes ya escribieron, para quien no abre una carpeta. No calculo nada ni escribo ninguna ficha.

**1. La carpeta de trabajo.** Es la que contiene `.criterio/`, la carpeta desde donde corren los agentes. Si el argumento no la trae, propón la carpeta de esta sesión y confírmala con la persona.

**2. Lo que hay en ella:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mapa.py" descubrir --raiz <carpeta de trabajo>
```

Muéstralo como una tabla, una fila por agente e instancia, con la familia, el agente, la entidad o el caso, la carpeta de sus documentos y la de su estado. Si la carpeta de documentos tiene su marca (`marcada`, el archivo `_CRITERIO_<QUÉ>.txt`), dilo con el nombre del archivo; las de `sin_marca` se marcan desde el setup de su agente, no desde aquí (ADR 0011). Lo que venga en `problemas` va debajo, tal cual. Las configuraciones de `no_publica` —la oficina de Ofelia, por omisión— no entran al portal porque su configuración lo dice: nómbralas en una línea, y si alguien quiere publicarla, se cambia hablando con su setup, no aquí. Por ejemplo, un estado que todavía no existe porque el agente no ha corrido. **No lo arregles tú**: di qué comando de qué agente lo resuelve.

Si no encontró a ningún agente, dilo en una línea y di qué falta: cada familia se instala y se configura con su propio setup —`/criterio-portfolio:portfolio-setup`, `/criterio-finance:finance-setup`, `/criterio-legal:legal-setup`…—, y después se vuelve aquí.

**3. La confirmación.** Pregunta, una vez y con la tabla a la vista, si alguna entrada se queda fuera del portal. Puede ser una entidad de prueba, o un caso que no se publica. Pregunta también el nombre de la organización si la configuración de la PMO no lo trae.

**4. Los términos.** Corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mapa.py" terminos --config <carpeta de trabajo>/.criterio/rostrum/config.json`. Si no están vigentes, muestra **tal cual** su `en_corto` con el enlace a la nota legal, pide un sí explícito y el nombre de quien acepta, y regístralo:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mapa.py" aceptar --config <carpeta de trabajo>/.criterio/rostrum/config.json --por "<nombre>"
```

**5. El mapa, escrito:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mapa.py" guardar --raiz <carpeta de trabajo> --sin <id que se queda fuera> --organizacion "<nombre>"
```

Un `--sin` por cada entrada que la persona dejó fuera; ninguno si no dejó ninguna. Queda en `<carpeta de trabajo>/.criterio/rostrum/config.json`. Las rutas van relativas a la carpeta de trabajo, así que el mapa no publica la carpeta de nadie.

**6. Para volver a revisarlo**, cuando se instala una familia nueva o un agente cambia de estado:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mapa.py" revisar --mapa <carpeta de trabajo>/.criterio/rostrum/config.json
```

Lo `nuevo` entra volviendo a guardar; lo que la persona dejó fuera no vuelve solo.

## Cierre

En dos líneas: cuántos agentes e instancias quedaron en el mapa, de qué familias, y el comando que levanta el portal, `/criterio-server:server-start`.

## Lo que este comando no hace

- No crea, mueve ni edita la configuración ni el estado de ningún agente: solo los procesa.
- No levanta el servidor: eso es `server-start`.
