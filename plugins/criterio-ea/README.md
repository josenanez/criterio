# Criterio EA · Executive office · the whole family

[Español](README.es.md) · `criterio-ea` · Apache 2.0

**Install the EA family at once.** This plugin has no agents of its own: it brings the
family's agents and Rostrum, the portal for every family, as dependencies
([ADR 0026](../../docs/decisions/0026-una-familia-se-instala-de-una-vez.md)).

| Agent | Plugin | Its setup |
|---|---|---|
| **Ofelia** | `criterio-assistant` | `/criterio-assistant:ea-setup` |
| **Rostrum** | `criterio-server` | `/criterio-server:server-setup` |

## Install

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-ea@criterio
```

Then its setup:

```
/criterio-assistant:ea-setup
```

**The first result** comes from each agent's setup, on your own documents, before it finishes.

**What it never does.** It writes no configuration: each agent's own setup writes its own. It
accepts the terms for nobody: each agent shows them and asks for its own yes. And it adds nothing
to what each agent does or refuses to do: what each one never does is on its page.

**Only need one agent?** Install it on its own, with its plugin: the family is not needed. Everything
about each agent —what it does, what it does not, its commands and its tests— is on its page and in
the [EA family](../../families/criterio-ea/README.md).
