# Installing Criterio, step by step

[Español](instalacion.es.md)

Six steps, from an up-to-date Claude Code to the family configured. At the end are the errors that
show up in practice, with what the screen says and what to do.

## 1 · Claude Code up to date: 2.1.110 or later

From 2.1.110 on, installing a family also installs its agents and Rostrum. **Before it, only the family
plugin installs, without its agents, and it says nothing.** Check it in the terminal, outside Claude:

```
claude --version
```

If it is older, update it, also outside Claude:

```
claude update
```

If it answers `Insufficient permissions to install update`, go to [the errors](#the-errors-that-show-up).
In **Claude Cowork** there is nothing to do: the app updates itself.

## 2 · Add the marketplace, once

Inside Claude Code:

```
/plugin marketplace add josenanez/criterio
```

In **Claude Cowork**: Customise → Explore plugins → Personal → **+** → Add marketplace from GitHub →
`josenanez/criterio`.

## 3 · The demo, before opening your documents

Optional, and recommended: a test organisation with the agents of six families already run and
Rostrum on it, in about five minutes. Open it in an empty folder:

```
mkdir -p ~/criterio-demostracion && cd ~/criterio-demostracion && claude
```

And inside:

```
/plugin install criterio-server@criterio
/reload-plugins
/criterio-server:server-demo
```

## 4 · Install the family

In the folder that holds your function's documentation, open Claude and install the family. The CFO,
for instance:

```
/plugin install criterio-cfo@criterio
/reload-plugins
```

The same with `criterio-pmo`, `criterio-clo`, `criterio-cco`, `criterio-ciso` and `criterio-ea`. To
check it, `/plugin` → Installed: the family, each of its agents and `criterio-server` must be there.
If only the family is there, it is step 1.

## 5 · Set it up, in one conversation

```
/criterio-cfo:cfo-setup
```

It runs each agent's setup in order, asks only once what they share, asks for each agent's terms and,
at the end, offers the scheduled task for what is due each day. After that, you ask each agent in
your own words, by name: `/criterio-finance:clara how is the close going`.

## 6 · Receive each new version

A version is published every Friday. For it to arrive on its own, once: `/plugin` → Marketplaces →
criterio → Enable auto-update. Claude Code leaves it off for marketplaces that are not Anthropic's.
Without it, `/plugin marketplace update criterio` brings it by hand.

## The errors that show up

| What the screen says | Why | What to do |
|---|---|---|
| `Insufficient permissions to install update` or `Insufficient permissions for auto-updates` | Claude Code was installed with npm as administrator, and updating it needs permissions your user does not have | `sudo claude update`, which asks for the computer's password. Or, better, `claude install`: the native installation updates itself, without `sudo` |
| `Auto-update failed · Try claude doctor or npm i -g @anthropic-ai/claude-code` | The automatic update could not install, almost always for the reason in the row above | The same as the row above |
| `Failed to load marketplace "claude-plugins-official"` … `Invalid schema` | It is Anthropic's official catalogue, which an old Claude Code no longer understands, and it stops any plugin from installing | Update Claude Code (step 1). If you cannot right now: `/plugin marketplace remove claude-plugins-official` |
| `Unknown skill: criterio-server:server-demo` or `Unknown command` | The plugin did not install —look at the install message— or it installed and its commands have not loaded | If the install failed, the row above. If not, `/reload-plugins`, or close and reopen Claude |
| `Plugins changed. Run /reload-plugins to activate.` | Something was installed or updated | `/reload-plugins` |
| `1 error during load. Run /doctor for details.` | A plugin or a marketplace did not load | `/doctor` says which. If it is `claude-plugins-official`, the third row |
| The family installed and its setup says an agent is missing | Claude Code older than 2.1.110 | Step 1, or install that agent on its own: `/plugin install <its plugin>@criterio` |
| The new version does not arrive | Auto-update is off | Step 6 |

If another error shows up, [open it as an issue](https://github.com/josenanez/criterio/issues) with
what the screen says, word for word: it goes into this table.
