# Security

[Español](SECURITY.es.md)

## How to report a vulnerability

**Do not open a public issue.** Use GitHub private reporting: this repository's
**Security** tab → **Report a vulnerability**. Only the maintainer sees it.

Include the plugin version (`/plugin` → Installed), the command, and how to reproduce it.
You will get an acknowledgement in a reasonable time; there is no service-level agreement.

## What counts as a vulnerability here

- A command or hook that reads, writes or sends anything outside the folders the person
  configured.
- A script that executes content from a document as if it were an instruction.
- Any path by which project data ends up somewhere the person did not choose.

## What Criterio does on your machine

The plugins install Claude Code *hooks* that run `scripts/rastro.py` with Python on your
machine: they record each run in `.criterio/corridas/` inside your folder, and block
subagent launches when the configuration says so. They make no network calls. The
scripts use only the Python standard library. Read them before installing: they are text.
