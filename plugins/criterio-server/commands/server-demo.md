---
description: La demostración de Criterio en cinco minutos — una organización de prueba con los agentes de seis familias ya corridos y Rostrum levantado sobre ella, sin procesar ningún documento tuyo
argument-hint: "[carpeta donde dejarla] o vacío para ./criterio-demo"
allowed-tools: Read, Glob, Bash(python3:*), Bash(ls:*)
---

# /server-demo — Criterio funcionando, antes de abrir tus documentos

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías. **Y sin subagentes en paralelo:** todo se hace en esta misma conversación, uno tras otro.

## Para qué existe

Quien instala Criterio quiere verlo funcionar antes de abrirle sus propios documentos. Esto es eso:
una organización de prueba —un banco, una cadena de almacenes, un banco de la región andina y una
presidencia— con los agentes de seis familias ya corridos sobre ella, y Rostrum mostrándolo
([decisión 0029](https://github.com/josenanez/criterio/blob/main/docs/decisions/0029-la-demostracion.md)).

**Nada tuyo se procesa.** El material es sintético, sale de las pruebas del repositorio y viene
con el plugin. Lo que muestra cada agente lo calculó su propio motor sobre ese material.

## Flujo

**1. Preséntalo en dos líneas** y propón dónde dejarlo:

> Te dejo una organización de prueba en `./criterio-demo`, con los agentes de la PMO, la CFO, la CLO,
> la CCO, la CISO y la EA ya corridos, y levanto Rostrum sobre ella. Nada tuyo se procesa. ¿Ahí?

Si el argumento trae otra carpeta, esa. **Si `criterio-demo` ya existe ahí, no la sobrescribas:**
pregunta si se usa la que hay o se deja en otra carpeta.

**2. Descomprímela**, en la carpeta que contiene a `criterio-demo`:

```
python3 -m zipfile -e "${CLAUDE_PLUGIN_ROOT}/demo/criterio-demo.zip" <carpeta>
```

**3. Los términos de Rostrum**, como en cualquier agente:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mapa.py" terminos --config <carpeta>/criterio-demo/.criterio/rostrum/config.json
```

Si no están vigentes, muestra tal cual su `en_corto` con el enlace a la nota legal, pide un sí
explícito y el nombre para el comprobante, y regístralo:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mapa.py" aceptar --config <carpeta>/criterio-demo/.criterio/rostrum/config.json --por "<nombre>"
```

Sin el sí, no se levanta.

**4. Levanta Rostrum, en segundo plano**, para que la conversación siga:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/servidor.py" --mapa <carpeta>/criterio-demo/.criterio/rostrum/config.json
```

Escucha en `127.0.0.1:8787`, solo en este equipo. Si el puerto está ocupado, `--puerto 8788`.

**5. El recorrido, en cuatro enlaces**, con lo que se ve en cada uno:

| Enlace | Qué se ve |
|---|---|
| `http://127.0.0.1:8787/` | Lo que pide atención hoy, de todas las familias, y una tarjeta por familia |
| `http://127.0.0.1:8787/resumen/cfo` | El resumen ejecutivo de una familia en una página: el que se lleva al comité |
| `http://127.0.0.1:8787/vence` | Lo pendiente con fecha, de todos los agentes, en una sola lista |
| `http://127.0.0.1:8787/pmo` | El informe del portafolio: los verdes que la evidencia no sostiene |

Di de cuándo es el material: los agentes calcularon entre septiembre y noviembre de 2026, así que lo que
aparece como «ya pasó» es la fecha de hoy contra la del material. **La oficina de Ofelia no está en
el portal:** por omisión no se publica, y es a propósito.

**6. El siguiente paso.** La demostración instala solo a Rostrum: los agentes no están instalados todavía.
Dilo así, en tres pasos:

1. **Instalar la familia que se quiere probar**, en esta misma sesión, que es la que mantiene Rostrum
   levantado: `/plugin install criterio-cfo@criterio` y después `/reload-plugins`.
2. **Abrir Claude en la carpeta de la demostración**, en otra ventana de la terminal:
   `cd <carpeta>/criterio-demo && claude`. La configuración de cada agente está ahí.
3. **Pedírselo al agente por su nombre**, con el prefijo de su propio plugin, no el de Rostrum:
   `/criterio-finance:clara cómo va el cierre`. Cada agente pide sus términos.

Para sus propios documentos, lo mismo en la carpeta de su función: `/plugin install criterio-<familia>@criterio`
y su setup.

## Lo que no hace

No procesa ningún documento tuyo, no escribe fuera de la carpeta de la demostración y no deja nada
corriendo cuando se cierra la sesión. Para dejar Rostrum corriendo de verdad es
`/criterio-server:server-start`.
