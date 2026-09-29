# Rostrum · the criterio-portfolio server

**The report, for whoever does not open a folder.**

A rostrum does not measure, correct or opine: it **holds up what is already written, at
the height of whoever is going to read it.** That is why it
is called that — and if it ever computed anything, the name would stop being true.

[Español](SERVER.es.md) · back to the [plugin README](README.md)

---

![Rostrum: the report, for whoever does not open a folder](../../docs/img/en/servidor.png)

Vera produces the report as files on your machine. That serves whoever ran it, and
nobody else. **A sponsor does not open a folder of files**: they open a link, or they
open nothing.

**Rostrum** turns those files into a portal your team can consult, and — this is what
changes how it gets used — **it lets them leave the agent written questions.**

## Raising it

The report first, Rostrum second. **Rostrum does not generate the report: it holds it up.**

```
/criterio-portfolio:portfolio-report html
/criterio-portfolio:portfolio-server
```

Or by hand, which is what the command does:

```
python3 scripts/informe.py  --state <state> --salida <folder> --config <file>
python3 scripts/servidor.py --informe <folder> --estado <state> --config <file>
```

It listens on `127.0.0.1:8787`, **only on your machine**, and stops with Ctrl-C. If the
port is taken, `--puerto 8788`. With `--config` the portal carries your organisation's
name on every page; without it, it just says "Portafolio".

---

## What a visitor sees

![The portal's landing page](../../docs/img/portal/portada.png)

Three sections, in the order someone asks: **how everything is going, then the project
that is theirs, then the product they care about.**

The landing page also says **how old the report is**, which is precisely what nobody
knows when a PDF is forwarded to them. It is not recomputed when the page opens, and
that is declared rather than hidden.

> **The pages are in Spanish today.** `report.language` is declared in the
> configuration and not yet read — it is the open gap on this side of the plugin, and
> it is written down in [`DISENO.es.md`](DISENO.es.md) rather than
> quietly left out. The screenshots here come from the repository's
> [synthetic corpus](../../tests/criterio-portfolio/), as of 2026-09-30; "Banco del Ejemplo"
> is test material.

### 1 · PMO reports — how the portfolio is going

![The PMO report](../../docs/img/portal/informes-pmo.png)

What **only shows up looking at everything together**, and is therefore on no single
project's page: how many greens the evidence does not support, what has gone weeks
without a new document, and who sponsors more than one thing at a time.

That last one is not a finding on its own, and the page says so: it becomes one when
two of those projects compete for the same date or the same team, **and that is not in
the folder — the person knows it.**

### The committee gets its own view

![The decisions view](../../docs/img/portal/decisiones.png)

Not the previous one trimmed down: **a different object**. Only what exceeds the
authority of whoever manages each project, framed as a closed question, with its
figures and with **what it costs not to decide it**.

The difference matters. Hand a sponsor the filtered internal view and they do what
sponsors do: fix on one detail and derail the committee. Here each block is a decision
of theirs, and if there is none, it says so.

### 2 · Projects

![The project list](../../docs/img/portal/proyectos.png)

The list, **ordered by what most demands attention rather than by code**. Every row
carries what the project declares, what the evidence says, how long it has been silent,
and the product it belongs to.

![A project's report](../../docs/img/portal/proyecto.png)

And inside, the report: governance, plan, money, overdue milestones, overdue
commitments, and **what is not stated anywhere**. Every value with the citation of the
document it came from and its date, so it can be opened and verified.

At the very top, the link to the **product it came from**.

### 3 · Products

![The product list](../../docs/img/portal/productos.png)

A project ends; a product outlives every project that built it.

The list flags two things a normal portfolio report does not: when **more than one
committee is looking at the same product**, and when the status its projects declare
**is not supported by the evidence**. A product showing green with ten signals is
exactly the reading this portal exists to prevent.

Below, the projects that do not say which product they build. It is not their mistake
— some projects do not build a product — but until it is stated, their progress is
invisible from that side.

![A product's report](../../docs/img/portal/producto.png)

**Here is what no other page can say.** When a product is built by two projects
reporting to different committees, each committee sees its project and **none of them
sees the product**. From inside a project that cannot be detected, because from inside
one you do not see the other.

Three things follow, and they belong to this page alone:

- **No committee sees it whole**, with which one looks at which.
- **More than one sponsor answers for it**, so there is no single answer to whom it
  gets escalated.
- **The healthy project does not save the product**: it does not land until all of them
  land, so its status is the worst of them, not the average.

And what the page does **not** say, declared on the page itself: for this product there
is no adoption, revenue, production incident or satisfaction data. None of that is in
the project folder — it is operational data and it lives in another system.

---

## Asking the agent for something

The landing page has a form. **It answers nobody on the spot**, and saying so is more
honest than "we'll be in touch shortly": it writes the question into the queue and the
agent handles it when it wakes.

Three subjects, and the third is the most valuable:

| Subject | What the agent does |
|---|---|
| *Review a project against its documents* | Diagnoses it from zero, assuming nothing from its own report |
| *Explain where a value came from* | Traces it back to its document and cites it |
| *Something in the report does not match what I know* | **Someone is telling you which document is missing.** It is recorded as a finding, with who said it and when — it is not written into the record |

That last one is what turns the portal into more than a screen. The person who knows
the sponsor changed at the committee on the 11th is not going to go and fix a charter;
they will tell whatever is in front of them, if what is in front of them listens.

**An open request breaks the agent's silence.** It is the only thing that makes it
speak without being date arithmetic, because a person asked and is waiting:

```
python3 scripts/portafolio.py due       --state <state> --config <file>
python3 scripts/portafolio.py requests  --state <state>
python3 scripts/portafolio.py answered  --state <state> --id <identifier>
```

An unmarked request comes back tomorrow, and that is correct.

## Publishing it inside your organisation

There are two shapes and they are not equivalent. If you do not know which you want,
**start with the first**: it goes up in ten seconds, and with it running in your hands
the conversation with security is no longer asking permission for an idea.

**To look at it for a while.** Someone raises it, looks, and shuts it down. No
infrastructure to ask anyone for. What is lost: the sponsor has no link that works
tomorrow.

**Left running.** It lives on a PMO machine and the sponsor has a stable link. That is
where the value is, and also the conversation. `--abierto` makes it listen beyond the
machine, and the program warns you at startup.

### What to ask for

| What is asked for | Why |
|---|---|
| A machine inside the network and a port | That is where it lives. **It does not need to reach the internet** |
| Publishing it behind the access control they already use | See below |
| That machine staying on | If it goes off, the link stops working. There is no high availability and none is needed: the report regenerates |

### What **not** to ask for

Usually half the conversation, so it is worth carrying written down: no database, no
service account with permissions, no certificate of its own, no internet access, and
nothing touching any of your documentation folders.

## What Rostrum never does

- **It does not compute.** It serves pages already written to disk. Opening the page
  triggers no document reading, which is why two people see exactly the same thing. If
  it computed on the fly, the portfolio would stop being a single one.
- **It does not write any record.** The only thing it creates is the request file, in a
  folder of its own. **The write path to the portfolio does not exist in that
  program**, and the selftest proves it by comparing the record byte for byte before
  and after sending a request.
- **It authenticates nobody, and that is deliberate.** A hundred-line server on the
  standard library is not going to authenticate better than the proxy your organisation
  already has, and promising it would is exactly what this plugin does not do. So it
  listens only on your machine unless you say otherwise, and when you do, it warns you.
- **It sends nothing.** No email, no notification. If the report has to reach an inbox,
  today a person forwards it.

---

From here down is for whoever is going to publish it.

## The routes

| Route | What it is | For whom |
|---|---|---|
| `/` | The landing page, with the three sections and the form | Everyone |
| `/pmo` | How the portfolio is going | The PMO |
| `/decisiones` | What needs a decision | The committee and the sponsor |
| `/corridas` | The history: what ran, what it found, and what is being carried | Everyone |
| `/historia/<code>` | Since when a project has been carrying each signal, and which one was resolved | The PMO and the manager |
| `/corte?a=&b=` | What changed field by field between two cut-off dates | Whoever asks "since when" |
| `/proyectos` | The project list | Everyone |
| `/p/<code>` | A project's report | Whoever manages it, and whoever asks |
| `/productos` | The product list | Whoever answers for a product |
| `/producto/<name>` | A product's report | Whoever answers for a product |
| `/estado.json` | How old the report is and how many requests are open | A mechanism, not a person |
| `/peticion` | `POST` · leaves a question for the agent | The landing page's form |

The named routes **redirect to the file** rather than serving it in place. The reason is
that the pages link to each other by file name, because they also have to work **opened
from disk, zipped or printed**: the server is a projection, not the owner. If `/pmo`
served the file without redirecting, its links would point at routes that do not exist
from there.

`/estado.json` is where a mechanism of your own can find out there is a new report, if
one day you want it to reach an inbox unattended. **Sending mail on someone's behalf is
an authority this agent will not have**, so that step is taken by something of yours,
not by the plugin.


## The history, and why it is not deleted

A real organisation produces reports, charts and documents every day, and that trail **is**
the project's memory. The portal showed only the present and overwrote itself: there was no
way to know what had been said before a decision, nor to present progress, nor to
understand where a project stands beyond today.

Three views, and all three read without writing:

- **`/corridas`** — what ran, how many documents had to be re-read, how long it took, how
  many findings, and **how many more or fewer than last time**. Below, what is being
  carried: a signal that fired once is noise; one that has lasted several consecutive
  cut-offs is a decision nobody has taken.
- **`/historia/<code>`** — for one project, since when it has been carrying each signal and
  **which one was resolved, with the date**. That something got resolved is history too.
- **`/corte?a=&b=`** — what changed field by field between two cut-offs. It answers "since
  when" without anyone having to remember: three sponsors in eighteen months explains more
  than any root-cause analysis.

**Nothing is pruned, and nothing needs to be.** A snapshot of fifty projects weighs 112 KB,
and three years of weekly runs fit in 17 MB; with three hundred projects, in 100 MB. What
is not stored is the rendered report — it weighs seven times more — because it is produced
again when someone asks for it. Deleting the trail would delete the project's history, and
with it any tracking that holds up.

And there is a symmetry the product needs. Criterio demands that a PMO's declarations have
evidence. If the PMO's own report overwrites itself, **nobody can audit the PMO**. A run
history subjects the agent to its own rule.

All three pages say it in one line, and it is not boilerplate: this is the history of
**what the agent read in the documents**, not of what happened, and not a judgement about
anyone.

## How it is verified

```
python3 scripts/servidor.py --selftest
```

Thirty-seven checks, on the standard library, with nothing raised by hand. A server exposing
a portfolio has **two ways of failing that you cannot see by looking at the screen**,
and those are the ones checked: serving a file that is not part of the report — paths
with `..`, absolute paths, a neighbour on disk — and having a write path to the record.

Also: that the server's three sections are the same as `informe.py`'s, that every
declared route actually answers, and that every redirect lands on a page that exists. A
redirect to a page that is not there is a 404 with extra steps.

The run in detail, in
[`tests/criterio-portfolio/EVIDENCIA.md`](../../tests/criterio-portfolio/EVIDENCIA.md) (Spanish, as
working documents).
