# Instalar Criterio, paso a paso

[English](instalacion.md)

Seis pasos, de Claude Code al día hasta la familia configurada. Al final están los errores que
aparecen en la práctica, con lo que dice la pantalla y qué hacer.

## 1 · Claude Code al día: la 2.1.110 o posterior

Desde la 2.1.110, instalar una familia instala también sus agentes y a Rostrum. **Antes, se instala
solo el plugin de la familia, sin sus agentes, y no avisa.** Todo este paso se hace en la terminal,
**fuera de Claude**: si está abierto, sal con `/exit`.

**1.1 · Revisa la versión.**

```
claude --version
```

Si dice 2.1.110 o más, sigue al paso 2.

**1.2 · Actualízala.**

```
claude update
```

**1.3 · Si responde `Insufficient permissions to install update`**, Claude Code se instaló como
administrador y tu usuario no puede actualizarlo. Hay dos salidas:

- **Con permisos de administrador**, una vez: pide la contraseña de tu equipo.

  ```
  sudo claude update
  ```

- **Con la instalación nativa**, la recomendada: se actualiza sola desde ahí, sin volver a pedir
  la contraseña.

  ```
  claude install
  ```

Si `claude update` tampoco existe en tu versión, `npm i -g @anthropic-ai/claude-code@latest`, con
`sudo` delante si responde lo mismo de los permisos.

**1.4 · Comprueba** que quedó en la 2.1.110 o más:

```
claude --version
```

En **Claude Cowork** no hay que hacer nada de esto: la aplicación se actualiza sola.

## 2 · Agregar el marketplace, una vez

Dentro de Claude Code:

```
/plugin marketplace add josenanez/criterio
```

En **Claude Cowork**: Personalizar → Explorar plugins → Personal → **+** → Agregar marketplace desde
GitHub → `josenanez/criterio`.

## 3 · La demostración, antes de abrir tus documentos

Opcional, y recomendable: una organización de prueba con los agentes de seis familias ya corridos y
Rostrum sobre ella, en unos cinco minutos. Ábrela en una carpeta vacía:

```
mkdir -p ~/criterio-demostracion && cd ~/criterio-demostracion && claude
```

Y dentro:

```
/plugin install criterio-server@criterio
/reload-plugins
/criterio-server:server-demo
```

La demostración instala solo a Rostrum. Para pedirle algo a un agente sobre ese material, instala su
familia en la misma sesión (`/plugin install criterio-cfo@criterio` y `/reload-plugins`), abre Claude en
otra ventana dentro de `criterio-demo` y pídeselo por su nombre: `/criterio-finance:clara cómo va el cierre`.

## 4 · Instalar la familia

En la carpeta donde está la documentación de tu función, abre Claude e instala la familia. La CFO,
por ejemplo:

```
/plugin install criterio-cfo@criterio
/reload-plugins
```

Lo mismo con `criterio-pmo`, `criterio-clo`, `criterio-cco`, `criterio-ciso` y `criterio-ea`. Para
comprobarlo, `/plugin` → Installed: tiene que estar la familia, cada uno de sus agentes y
`criterio-server`. Si solo está la familia, es el paso 1.

## 5 · Configurarla, en una conversación

```
/criterio-cfo:cfo-setup
```

Corre el setup de cada agente en orden, pregunta una sola vez lo que comparten, pide los términos de
cada agente y, al final, ofrece la tarea programada para lo que toca cada día. Después, a cada
agente se le pide en palabras, por su nombre: `/criterio-finance:clara cómo va el cierre`.

## 6 · Recibir cada versión nueva

Se publica una versión cada viernes. Para que llegue sola, una vez: `/plugin` → Marketplaces →
criterio → Enable auto-update. Claude Code la deja apagada en los marketplaces que no son de
Anthropic. Sin ella, `/plugin marketplace update criterio` la trae a mano.

## Los errores que aparecen

| Lo que dice la pantalla | Por qué | Qué hacer |
|---|---|---|
| `Insufficient permissions to install update` o `Insufficient permissions for auto-updates` | Claude Code se instaló con npm como administrador, y actualizarlo pide permisos que tu usuario no tiene | `sudo claude update`, que pide la contraseña del equipo. O, mejor, `claude install`: la instalación nativa se actualiza sola, sin `sudo` |
| `Auto-update failed · Try claude doctor or npm i -g @anthropic-ai/claude-code` | La actualización automática no pudo instalarse, casi siempre por lo mismo de la fila anterior | Lo mismo de la fila anterior |
| `Failed to load marketplace "claude-plugins-official"` … `Invalid schema` | Es el catálogo oficial de Anthropic, que una versión vieja de Claude Code ya no entiende, y corta la instalación de cualquier plugin | Actualiza Claude Code (paso 1). Si no puedes ahora: `/plugin marketplace remove claude-plugins-official` |
| `Unknown skill: criterio-server:server-demo` o `Unknown command` | El plugin no se instaló —mira el mensaje de la instalación— o se instaló y sus comandos no se han cargado | Si la instalación falló, la fila anterior. Si no, `/reload-plugins`, o cierra y abre Claude |
| `Unknown command: /criterio-server:clara` | Cada agente se llama con el prefijo de **su** plugin, y tiene que estar instalado: Rostrum no trae a los agentes | Instala la familia (`/plugin install criterio-cfo@criterio`, `/reload-plugins`) y llámalo con su prefijo: `/criterio-finance:clara`. En la demostración, abre Claude dentro de `criterio-demo` |
| `Plugins changed. Run /reload-plugins to activate.` | Se instaló o se actualizó algo | `/reload-plugins` |
| `1 error during load. Run /doctor for details.` | Un plugin o un marketplace no cargó | `/doctor` dice cuál. Si es `claude-plugins-official`, la tercera fila |
| La familia se instaló y su setup dice que un agente no está | Claude Code anterior a la 2.1.110 | Paso 1, o instala ese agente solo: `/plugin install <su plugin>@criterio` |
| La versión nueva no llega | La actualización automática está apagada | Paso 6 |

Si aparece otro error, [ábrelo como issue](https://github.com/josenanez/criterio/issues) con lo que
dice la pantalla, tal cual: entra a esta tabla.
