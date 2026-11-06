# Criterio CLO · Contratos y cumplimiento · la familia completa

[English](README.md) · `criterio-clo` · Apache 2.0

**Instala la familia CLO de una vez.** Este plugin no tiene agentes propios: trae como
dependencias a los de la familia y a Rostrum, el portal de todas las familias
([ADR 0026](../../docs/decisions/0026-una-familia-se-instala-de-una-vez.md)).

| Agente | De qué responde | Plugin | Su setup |
|---|---|---|---|
| **Fidel** | los contratos | `criterio-legal` | `/criterio-legal:legal-setup` |
| **Constanza** | el cumplimiento | `criterio-compliance` | `/criterio-compliance:compliance-setup` |
| **Rostrum** | el portal de todas las familias | `criterio-server` | `/criterio-server:server-setup` |

## Instalación

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-clo@criterio
```

Después, un solo comando los configura a todos en la misma conversación:

```
/criterio-clo:clo-setup
```

Corre el setup de cada agente en orden y pregunta una sola vez lo que comparten —la carpeta, la entidad y dónde se guarda el estado—. Los términos los muestra cada agente, y cada uno pide su propio sí.

| Comando | Qué hace |
|---|---|
| `/criterio-clo:clo-setup` | Configura la familia de una vez: corre el setup de cada agente en orden, con lo común preguntado una sola vez |

**El primer resultado** lo da el setup de cada agente, sobre tus propios documentos, antes de terminar.

**Lo que nunca hace.** No escribe ninguna configuración: la de cada agente la escribe su propio
setup. No acepta los términos por nadie: cada agente los muestra y pide su propio sí. Y no agrega
nada a lo que cada agente hace o se niega a hacer: lo que cada uno nunca hace está en su página.

**¿Solo necesitas un agente?** Instálalo solo, con su plugin: la familia no hace falta. Todo lo de
cada agente —qué hace, qué no hace, sus comandos y sus pruebas— está en su página y en la
[familia CLO](../../families/criterio-clo/README.es.md).
