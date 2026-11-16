---
description: Arma la búsqueda de una vacante: las cadenas para el buscador de quien recluta y las personas de la base interna con la misma ocupación
argument-hint: "[identificador de la vacante]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /talent-search — La búsqueda de una vacante

> **Dónde está la configuración:** `.criterio/seleccion/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-talent:talent-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `talento.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Ninguna decisión sobre una persona es tuya.** No rechazas, no descartas, no das un puntaje y no ordenas candidatos por un número: presentas cada requisito con su evidencia, en el orden del identificador del candidato. **No usas la fotografía, la edad, el sexo, el estado civil, el origen, la religión ni la salud de nadie**: si llegan, la ficha registra solo su tipo y dónde, y el motor los excluye. **No entras a redes ni buscas personas** fuera de lo que la organización entrega.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-talent:talent-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **selection-policy**.

## Flujo

**1. La vacante.** Si el argumento no la trae, pregúntala. Con ella, una sola llamada:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" busqueda --config <config> --id <vacante>
```

**2. Muestra lo que devuelve, tal cual:** las cadenas de búsqueda, desde las denominaciones de la ocupación en el estándar y los requisitos esenciales del perfil, y las personas de la base interna con la misma ocupación o una afín, en el orden de su identificador.

**Las cadenas las corre quien recluta, en su buscador.** Tú no entras a LinkedIn ni a ninguna otra red, no compras bases y no buscas a nadie fuera de lo que la organización entrega. **Las personas de la base interna no se ordenan por ningún número**: se dice cuáles tienen la ocupación, y quien recluta decide a quién contactar.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-talent-search.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" corrida --config <config> --what talent-search \
    --salida <estado>/corridas/salida-talent-search.md \
    --caso <vacante> \
    --nota "cadenas de búsqueda y base interna"
```
