---
description: Configura la familia CISO de una vez — Alexis, Guillermo y Amparo — en una sola conversación, con lo común preguntado una sola vez
argument-hint: "[ruta de la carpeta] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-ciso/familia.json por scripts/familias.py; no se edita a mano -->

# /ciso-setup — La familia CISO, de una vez

Instalar `criterio-ciso` instaló a Alexis (`criterio-security`), Guillermo (`criterio-vulnerability`) y Amparo (`criterio-resilience`), y a Rostrum
(`criterio-server`). Este comando los deja listos en una sola conversación: lo que comparten se
pregunta una vez, y cada agente pregunta solo lo suyo.

**Este comando no escribe ninguna configuración.** La de cada agente la escribe su propio setup,
con su motor y sus validaciones. Aquí solo se ordena el recorrido.

## Flujo

**0. Preséntate, en una línea.**

> Vamos a dejar lista la familia CISO: Alexis, el gobierno y los controles; Guillermo, las vulnerabilidades; Amparo, la respuesta y la recuperación. Lo que comparten te lo pregunto una sola vez.

**1. Corre el setup de cada agente, en este orden**, uno después del otro y en esta misma conversación:

1. **Alexis** — `/criterio-security:security-setup`
2. **Guillermo** — `/criterio-vulnerability:vuln-setup`
3. **Amparo** — `/criterio-resilience:resilience-setup`

Invócalos tú, con la herramienta que corre los comandos. Si no puedes invocar un comando, dile a la
persona exactamente cuál escribir y espera a que termine. Si el argumento trae una ruta, pásasela
al primero.

**Si el setup de un agente no existe, el agente no está instalado**: casi siempre es un Claude Code
anterior a la 2.1.110, que instala el plugin de la familia sin sus agentes. Dilo en una línea, con
las dos salidas —actualizar con `claude update`, fuera de Claude, o instalar ese agente con
`/plugin install <su plugin>@criterio`— y sigue con el siguiente.

**2. Lo que ya se respondió no se vuelve a preguntar.** El primer setup encuentra la carpeta, la
entidad y dónde guardar el estado. Antes de cada setup siguiente, di en una línea lo que ya quedó
fijado: ese setup lo toma de la conversación y solo pide confirmarlo.

**3. Los términos los muestra cada setup.** No los resumas, no los agrupes y no los aceptes por la
persona: cada agente pide su propio sí.

**4. Si la persona no quiere uno de los agentes, sáltalo.** Cada agente funciona solo. Dilo en una
línea y sigue con el siguiente.

**5. Al final, la familia en una tabla:** una fila por agente —configurado o saltado— con el primer
resultado que mostró su setup, en sus palabras. Y el siguiente paso, en una línea: para verlo fuera de
la conversación, `/criterio-server:server-setup` publica lo de la familia en Rostrum.

**6. El reloj, una tarea para la familia** ([decisión 0028](../../../docs/decisions/0028-el-setup-ofrece-el-reloj.md)).
Solo con los agentes que quedaron configurados; los saltados no entran. Pregunta:

> ¿Quieres que Alexis, Guillermo y Amparo revisen solo lo que toca cada día? Te propongo una tarea programada
> los días hábiles a las 7:00: cada uno decide según su frecuencia si le toca algo y, si no, se calla.
> Solo procesa y escribe en el estado de Criterio; no envía nada.

**Solo con un sí explícito**, y a la hora que la persona confirme o cambie. Según dónde corres:

- **Si tienes una herramienta para crear tareas programadas** —en Cowork, la de las tareas
  programadas de la app—, créala para la carpeta raíz, con la hora confirmada y esta instrucción:
  «En esta carpeta, corre en orden /criterio-security:security-wake, /criterio-vulnerability:vuln-wake y /criterio-resilience:resilience-wake. Solo procesa y escribe en el estado de Criterio; no envíes nada. Si un paso necesita un permiso que no tienes, detente y déjalo dicho.»
- **Si no** —Claude Code en una terminal—, usa el programador del equipo. Busca la ruta de Claude
  con `which claude`, crea `.criterio/reloj/` en la carpeta raíz, muestra la línea completa y, con
  un sí, agrégala a `crontab`. El equipo tiene que estar encendido a esa hora.

  ```
  0 7 * * 1-5 cd "<carpeta raíz>" && "<ruta de claude>" -p "En esta carpeta, corre en orden /criterio-security:security-wake, /criterio-vulnerability:vuln-wake y /criterio-resilience:resilience-wake. Solo procesa y escribe en el estado de Criterio; no envíes nada. Si un paso necesita un permiso que no tienes, detente y déjalo dicho." --allowedTools "Skill,Read,Glob,Grep,Write,Edit,Bash(python3:*),Bash(ls:*),Bash(mkdir:*)" >> ".criterio/reloj/ciso.log" 2>&1
  ```

**Después de cada versión nueva, la tarea se detiene** hasta que alguien acepte los términos de esa
versión en una sesión con la persona presente: una aceptación por versión, nunca desatendida. Dilo
al crearla.

**Si la persona dice que no**, di en una línea cómo se corre a mano: `/criterio-security:security-wake`, `/criterio-vulnerability:vuln-wake` y `/criterio-resilience:resilience-wake`.
Y en la tabla del final, una fila más: la tarea, con su hora y dónde quedó, o «sin reloj».
