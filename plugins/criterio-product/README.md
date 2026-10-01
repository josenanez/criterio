# Alba · one product's agent

**Alba tells you what of your definition holds, and what holds only itself up.** You talk to the
customer, read what the customer does not say, decide what gets built and set the price. She
arrives with the chain of evidence assembled and the holes pointed out.

[Español](README.es.md) · `criterio-product` · Apache 2.0 · One instance per product

**Status: the eleven commands are built**, twelve skills, and the register's arithmetic verified
with 62 checks. **What has not been tested yet: the register over a real product's
documentation** — extraction from interviews and business cases has not been exercised outside
synthetic material. Nothing is announced as finished until the
[acceptance criteria](DISENO.es.md#criterios-de-aceptación) pass.

**This page reads on its own.** Alba works without her siblings: if all you do is define
products, everything is here, tests included. The family — how she meets Vera and Samuel — is in
the [criterio-pmo family](../../families/criterio-pmo/README.md).

---

## What it is

| | |
|---|---|
| **Whose hands it extends** | The product manager's |
| **What it works on** | **One product, before the project exists** |
| **What it looks at** | The definition, the interviews, the tickets and the metrics |
| **Cadence** | By seasons: a round of interviews, a product committee, a definition being closed |
| **Instances** | One per product |

## What it does

**What it does that nobody else does: contrasting the definition against the evidence of
demand.** It is the same comparison that holds up the whole family — declared against evidenced
— but **one step before there is a plan**, when there is still no baseline and no budget to
measure against.

**What it can answer that today nobody answers:** which claim in your definition **is not stated
anywhere**, which assumption has gone months without being verified, where the business case
asserts a number the metric does not support, and what was decided to be built that **nobody is
building**.

### The eleven commands

> They are typed with the plugin prefix: `/criterio-product:` and autocomplete does the rest. It is the only form that resolves in a Claude Code session.

| Command | What it does |
|---|---|
| `/criterio-product:product-setup` | **The first thing you run.** Looks at your folder, asks four questions and contrasts the definition you already have |
| `/criterio-product:product-discovery` | Interviews and tickets into themes with the citation of who said it, and the theme that has gone months said without anybody turning it into anything |
| `/criterio-product:product-requirements` | The register with its gaps: no owner, no acceptance criteria, accepted without anybody asking for it, and what nobody decides |
| `/criterio-product:product-definition` | The definition against the evidence of demand, and where the business and the data do not match |
| `/criterio-product:product-trace` | Requirement → decision → project → deliverable, and the two gaps above |
| `/criterio-product:product-spec` | The draft specification with verifiable criteria and the gaps pointed out, not filled in |
| `/criterio-product:product-charter` | The project charter: where the record is born and the writer changes hands |
| `/criterio-product:product-business-case` | The business case's structure with every figure cited, and the gaps with who produces them |
| `/criterio-product:product-publish` | Publishes your record where the other products can read it |
| `/criterio-product:product-overlap` | Where you step on another product: the same metric counted twice, the same project, the same segment |
| `/criterio-product:product-wake` | **The one you put on a clock.** What crossed a threshold without anybody doing anything |

### The twelve skills

They load on their own when the subject comes up. Eight are product's own; four are literal
copies from `criterio-portfolio`, because they are method and not role.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `requirement-record` | **Alba's data contract.** Schema, extraction, citation, the five states and what each one demands | Alba's own |
| `product-health` | The eleven signals, the four thresholds, in what order they are read and **which one is not a finding** | Alba's own |
| `demand-evidence` | What counts as evidence that somebody asked for something, what does not count even if it looks like it, and how it ages | Alba's own |
| `discovery-synthesis` | Interviews and tickets into themes with the citation. A theme is a set of quotations, not a claim | Alba's own |
| `assumption-tracking` | The assumption written so that it can turn out false, and the day it becomes a recorded risk | Alba's own |
| `product-metrics` | The series with its source and its definition, and the contrast between declared and measured | Alba's own |
| `specification-draft` | The verifiable acceptance criterion, and the rule of pointing out the gap instead of filling it | Alba's own |
| `regulatory-sweep` | The obligations the definition touches, cited. **It does not opine on compliance** | Alba's own |
| `project-record` | The project record: born with the charter, and Alba is the one who creates it | Copy of Vera's · also in Samuel |
| `governance-artifacts` | What a project charter contains and who decides what | Copy of Vera's · also in Samuel |
| `document-intake` | Which document has to be re-read and which not, which formats can be read and with what | Copy of Vera's · also in Samuel |
| `raid-taxonomy` | Where an assumption moves to the day nobody verifies it | Copy of Vera's · also in Samuel |

## What it is for

In a project you contrast the **status the manager declares** against the documentary evidence.
In a product you contrast the **definition** against the evidence of demand.

It is the same comparison, upstream, and it fails the same way: **nobody is lying.** The
definition was written eight months ago with the evidence there was, the evidence aged, the
business case's figure stayed, and the document is just as convincing as before.

> **tx_mensuales** · the business case of 4 March says **250,000**
> The transactional dashboard measures **180,000** as of 1 September — **28% apart**
> It is not that somebody got it wrong: it is that the figure being decided on is from March.

*«The business and the data do not match»* lets nobody do anything. The two sources and the two
dates do. That case comes from the synthetic corpus, with the answer written by hand **before**
running the calculation.

And there is a second finding of the same kind: **what was decided and nobody is building.** It
was decided in a committee, written in the minutes, and never entered any project's scope; it is
discovered months later, usually in another committee. `/criterio-product:product-trace` finds it, and also finds
the gap nobody looks for: **the project that says it builds your product, and whose record says
it builds another.** Alba does not believe her own register: she confirms it against the
project's record, which has another owner and another cadence. When the two do not match, **the
disagreement is reported and not fixed from here.**

### And what it is not for

- **It does not decide what gets built.** You decide that. Alba shows you what supports it, and
  if she decided, the comparison would be comparing the system against itself.
- **It does not talk to your customer**, and it does not read what the customer does not say. It
  is the part of the craft no agent will ever have, and it is the one that feeds everything else.
- **It does not judge whether something will be liked.**
- **It does not say whether your product complies.** It names and cites the obligations it
  touches; the judgement is legal and the responsibility is your organisation's.
- **It does not fill a gap with what is reasonable.** A specification with the holes filled in
  looks complete, gets approved, and what nobody decided ends up decided by the agent.
- **It does not write in your documentation folder.**
- **It does not guess.** Every value carries the citation of the document it came from. *«It is
  not stated anywhere»* is a valid and expected answer.

**And one thing it deliberately stops doing on the day of the charter: writing the project's
record.** She creates it with the signed charter and from then on only reads it. If two agents
wrote it, the disagreement between them would stop being a signal and would become a race.

And one that has to be said out loud: **your documents are processed on the AI platform's
infrastructure**, not only on your machine. Confirm that this is admissible under your policies
before pointing it at confidential material. Full disclaimer in
[DISCLAIMER.md](../../DISCLAIMER.md), terms in [TERMS.md](../../TERMS.md).

## Installing and configuring

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-product@criterio
/criterio-product:product-setup
```

**In Claude Cowork** — Customise → Explore plugins → Personal → **+** → Add marketplace from
GitHub → `josenanez/criterio`.

If you run a project and not a product, yours is [Samuel](../criterio-project/README.md). If you run
the portfolio, [Vera](../criterio-portfolio/README.md).

### The first result

`/criterio-product:product-setup` looks at your folder, asks four questions — one at a time, each with a suggested
answer — and **takes the definition you already have written and breaks it into claims.** With
that it shows you, in under ten minutes, three lists:

- **What the evidence supports**, with the document and the date.
- **What rests on an assumption** nobody has verified.
- **What is not stated anywhere.**

That third list is the one no review finds, **because reading a well-written document everything
looks supported.**

**What ends up configured** is written by `/criterio-product:product-setup` from your answers, on your machine and
in a file of yours: where the product's documentation is, where your register lives, how often it
is reviewed, the four thresholds, and the record that you accepted the terms, with your name and
the date. All of that is changed **by talking**.

### How often it runs

This is the difference between a command and an agent. A command waits. **This one is scheduled
and runs on its own.**

Her cadence is by seasons, and that is what produces what is due. The decision is date
arithmetic, so the code takes it and not the judgement of the moment:

```
python3 scripts/producto.py due --state <state> --config <file>
```

And `/criterio-product:product-wake` is the command the clock invokes: it looks at what crossed a threshold while
nobody was watching — an assumption that has gone too long unverified, evidence that aged, a
requirement nobody decides — and **if nothing crossed it produces nothing.** Staying quiet when
nothing happened is not an omission — it is the only reason an agent that runs every week is
still installed the following month.

Putting it on a clock is on your organisation's side: a scheduled task in Cowork, or the
system's scheduler in Claude Code. **And if unattended runs are not welcome** — in a bank that is
a reasonable answer — the cadence still says what is due, run by hand. What you lose is being
told without anyone asking.

**And if you want the product committee to see it without asking you for it**, the family has a
server that publishes it with a section for products, where whoever is looking can leave the
agent a written question. → **[Rostrum](../criterio-portfolio/SERVER.md)**

## Working with the others

Alba works alone. If the other two are installed, **there is nothing to connect**: they
meet through the project record, which is one more document in the folder.

| With whom | What happens |
|---|---|
| **Samuel** | Alba writes the project charter and with it **creates** the project record. From then on she never writes it again: he does. She reads it to confirm that the project claiming to build her product really builds it |
| **Vera** | Reads the product record Alba publishes with `/criterio-product:product-publish`, to look at the product through all the projects building it |
| **Other products** | Each publishes its record, and Alba reads them to see where she steps on another: the same metric counted twice, the same project or the same segment |

## Tests

### How it is built

The spine is the **requirement record**: a data contract every command reads and writes, with the
citation of the source document and its date on every field, and with five states that say what
each one demands. No command reads raw documents on its own. That is what makes it possible to
walk the trace — requirement → decision → project → deliverable — without reading anything again,
and to **compute instead of opine**.

And there is a seam with the project, because the object changes hands:

| | Before the charter | After |
|---|---|---|
| **The object** | The requirement register | The project record |
| **Who writes** | Alba | The project's agent, except the declared status |
| **What Alba does** | Everything | **Read only**, to know whether her product is being built |

Three scripts, which are the only thing that does not opine.
[`scripts/producto.py`](scripts/producto.py) does Alba's own arithmetic: the eleven signals, the
four thresholds, the cadence and the overlap between two products.
[`scripts/texto.py`](scripts/texto.py) turns the document into text, and
[`scripts/portafolio.py`](scripts/portafolio.py) contributes the part of the project record that Alba creates
with the charter. **The last two are literal copies of Vera's, not imports**, because an
installed plugin has to run on its own; in the repository, `scripts/sincronizar.py --check` fails
if the copies have drifted apart.

### How it is verified

```
python3 tests/criterio-product/grade.py    over two products, with a negative control
python3 scripts/producto.py selftest      62 checks over the arithmetic
```

On the standard library, with nothing installed. Over a synthetic corpus with hand-written
answers read from the documents — **including a negative control**: a product with a definition,
interviews and a register that produces not one finding. An agent that finds something there is a
noise generator.

**How the last run came out, generated from the run itself:**
[`tests/criterio-product/RESULTADOS.md`](../../tests/criterio-product/RESULTADOS.md). What each
piece of the material proves and, in the same detail, **what it does not**, in
[`EVIDENCIA.md`](../../tests/criterio-product/EVIDENCIA.md).

The full design, with the acceptance criteria and what still belongs to the person, in
[`DISENO.es.md`](DISENO.es.md), which travels with the plugin.

And the family's tests — what no agent can answer alone — in the
[family README](../../families/criterio-pmo/README.md#the-familys-tests).

