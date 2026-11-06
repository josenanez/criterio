# Criterio CLO · Contracts and compliance · the whole family

[Español](README.es.md) · `criterio-clo` · Apache 2.0

**Install the CLO family at once.** This plugin has no agents of its own: it brings the
family's agents and Rostrum, the portal for every family, as dependencies
([ADR 0026](../../docs/decisions/0026-una-familia-se-instala-de-una-vez.md)).

| Agent | Plugin | Its setup |
|---|---|---|
| **Fidel** | `criterio-legal` | `/criterio-legal:legal-setup` |
| **Constanza** | `criterio-compliance` | `/criterio-compliance:compliance-setup` |
| **Rostrum** | `criterio-server` | `/criterio-server:server-setup` |

## Install

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-clo@criterio
```

It needs Claude Code 2.1.110 or later: before it, only this plugin installs, without its agents,
and it says nothing. If something fails, [the installation step by step](../../docs/instalacion.md).

Then one command sets them all up in the same conversation:

```
/criterio-clo:clo-setup
```

It runs each agent's setup in order and asks only once what they share —the folder, the entity and where
the state is kept—. Each agent shows its own terms and asks for its own yes. At the end it offers a scheduled
task for what is due each day, and creates it only with a yes.

| Command | What it does |
|---|---|
| `/criterio-clo:clo-setup` | Sets the family up at once: runs each agent's setup in order, asking only once what they share |

**The first result** comes from each agent's setup, on your own documents, before it finishes.

**What it never does.** It writes no configuration: each agent's own setup writes its own. It
accepts the terms for nobody: each agent shows them and asks for its own yes. And it adds nothing
to what each agent does or refuses to do: what each one never does is on its page.

**Only need one agent?** Install it on its own, with its plugin: the family is not needed. Everything
about each agent —what it does, what it does not, its commands and its tests— is on its page and in
the [CLO family](../../families/criterio-clo/README.md).
