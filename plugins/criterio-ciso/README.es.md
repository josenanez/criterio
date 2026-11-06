# Criterio CISO · La seguridad de la información · la familia completa

[English](README.md) · `criterio-ciso` · Apache 2.0

**Instala la familia CISO de una vez.** Este plugin no tiene agentes propios: trae como
dependencias a los de la familia y a Rostrum, el portal de todas las familias
([ADR 0026](../../docs/decisions/0026-una-familia-se-instala-de-una-vez.md)).

| Agente | De qué responde | Plugin | Su setup |
|---|---|---|---|
| **Alexis** | el gobierno y los controles | `criterio-security` | `/criterio-security:security-setup` |
| **Guillermo** | las vulnerabilidades | `criterio-vulnerability` | `/criterio-vulnerability:vuln-setup` |
| **Amparo** | la respuesta y la recuperación | `criterio-resilience` | `/criterio-resilience:resilience-setup` |
| **Rostrum** | el portal de todas las familias | `criterio-server` | `/criterio-server:server-setup` |

## Instalación

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-ciso@criterio
```

Después, un solo comando los configura a todos en la misma conversación:

```
/criterio-ciso:ciso-setup
```

Corre el setup de cada agente en orden y pregunta una sola vez lo que comparten —la carpeta, la entidad y dónde
se guarda el estado—. Los términos los muestra cada agente, y cada uno pide su propio sí. Al final ofrece una
tarea programada para lo que toca cada día, y la crea solo con un sí.

| Comando | Qué hace |
|---|---|
| `/criterio-ciso:ciso-setup` | Configura la familia de una vez: corre el setup de cada agente en orden, con lo común preguntado una sola vez |

**El primer resultado** lo da el setup de cada agente, sobre tus propios documentos, antes de terminar.

**Lo que nunca hace.** No escribe ninguna configuración: la de cada agente la escribe su propio
setup. No acepta los términos por nadie: cada agente los muestra y pide su propio sí. Y no agrega
nada a lo que cada agente hace o se niega a hacer: lo que cada uno nunca hace está en su página.

**¿Solo necesitas un agente?** Instálalo solo, con su plugin: la familia no hace falta. Todo lo de
cada agente —qué hace, qué no hace, sus comandos y sus pruebas— está en su página y en la
[familia CISO](../../families/criterio-ciso/README.es.md).
