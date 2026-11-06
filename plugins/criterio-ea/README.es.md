# Criterio EA · Dirección · la familia completa

[English](README.md) · `criterio-ea` · Apache 2.0

**Instala la familia EA de una vez.** Este plugin no tiene agentes propios: trae como
dependencias a los de la familia y a Rostrum, el portal de todas las familias
([ADR 0026](../../docs/decisions/0026-una-familia-se-instala-de-una-vez.md)).

| Agente | De qué responde | Plugin | Su setup |
|---|---|---|---|
| **Ofelia** | la oficina de dirección | `criterio-assistant` | `/criterio-assistant:ea-setup` |
| **Rostrum** | el portal de todas las familias | `criterio-server` | `/criterio-server:server-setup` |

## Instalación

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-ea@criterio
```

Necesita Claude Code 2.1.110 o posterior: antes, se instala solo este plugin, sin sus agentes, y no
avisa. Si algo falla, [la instalación paso a paso](../../docs/instalacion.es.md).

Después, su setup:

```
/criterio-assistant:ea-setup
```

**El primer resultado** lo da el setup de cada agente, sobre tus propios documentos, antes de terminar.

**Lo que nunca hace.** No escribe ninguna configuración: la de cada agente la escribe su propio
setup. No acepta los términos por nadie: cada agente los muestra y pide su propio sí. Y no agrega
nada a lo que cada agente hace o se niega a hacer: lo que cada uno nunca hace está en su página.

**¿Solo necesitas un agente?** Instálalo solo, con su plugin: la familia no hace falta. Todo lo de
cada agente —qué hace, qué no hace, sus comandos y sus pruebas— está en su página y en la
[familia EA](../../families/criterio-ea/README.es.md).
