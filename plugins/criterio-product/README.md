# criterio-product

**Alba tells you what your definition holds up on, and what holds up on nothing.** You talk to
the customer, read what the customer does not say, decide what gets built and set the price.
She arrives with the chain of evidence assembled and the gaps marked.

[Español](README.es.md) · Apache 2.0 · One instance per product

**Status: the eight commands are built**, along with twelve skills and the register's
arithmetic verified by 52 checks. **What has not been tested yet: the register over a real
product's documentation** — extraction from interviews and business cases has not been
exercised outside synthetic material. Nothing is announced as finished until the
[acceptance criteria](ACCEPTANCE.md) pass.

---

## Install

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-product@criterio
/product-setup
```

If you run a project rather than a product, yours is
[`criterio-pm`](../criterio-pm/README.md). If you run the portfolio,
[`criterio-pmo`](../criterio-pmo/README.md).

## The first result

`/product-setup` looks at your folder, asks four questions — one at a time, each with a
suggested answer — and **takes the definition you already have written and breaks it into
claims.** With that it shows you, in under ten minutes, three lists:

- **What the evidence holds up**, with the document and the date.
- **What rests on an assumption** nobody has verified.
- **What is not stated anywhere.**

That third list is the one no review finds, **because reading a well-written document
everything looks substantiated.**

## The same comparison, one step before the project

In a project you contrast the **status the manager declares** against the documentary
evidence. In a product you contrast the **definition** against the evidence of demand.

The same comparison, upstream, and it fails the same way: **nobody is lying.** The definition
was written eight months ago with the evidence available then, the evidence aged, the business
case figure stayed, and the document reads just as convincingly.

> **monthly_tx** · the business case of 4 March says **250,000**
> The transactional dashboard measures **180,000** as of 1 September — **28% apart**
> It is not that somebody got it wrong: the figure being decided on is from March.

*"Business and data disagree"* lets nobody do anything. Both sources and both dates do.

## What it never does

- **It does not decide what gets built.** You do. Alba shows you what holds it up, and if she
  decided, the comparison would be comparing the system against itself.
- **It does not talk to your customer**, and it does not read what the customer leaves unsaid.
  That is the part of the craft no agent will ever have, and it is what feeds everything else.
- **It does not judge whether something will land well.**
- **It does not say whether your product complies.** It names and cites the obligations the
  definition touches; the judgement is legal and the responsibility is your organisation's.
- **It does not fill a gap with something reasonable.** A specification with the holes filled
  in looks complete, gets approved, and what nobody decided ends up decided by the agent.
- **It does not write in your documentation folder.**
- **It does not guess.** Every value carries the citation of the document it came from.
  *"Not stated anywhere"* is a valid and expected answer.

And one that has to be said out loud: **your documents are processed on the AI platform's
infrastructure**, not only on your machine. Confirm that is admissible under your policies
before pointing it at confidential material. Full disclaimer in
[DISCLAIMER.md](../../DISCLAIMER.md), terms in [TERMS.md](../../TERMS.md).

---

## What was decided and nobody is building

It was decided in a committee, written into the minutes, and never made it into any project's
scope. It surfaces months later, usually in another committee.

`/product-trace` finds it with a filter, and it also finds the gap nobody looks for: **the
project that claims to be executing your product, and whose record says it is executing
another one.** Alba does not take her own register's word for it: she confirms it against the
project's record, which has a different owner and a different cadence.

When the two disagree, **the disagreement is reported and not fixed from here.** It is the same
rule that governs a project's two records, one level up.

## Where Alba ends and the project begins

`/product-charter` is the system's seam: the moment a defined problem becomes a plan with an
owner, authority and a success criterion.

| | Before the charter | After |
|---|---|---|
| **The object** | The requirement register | The project's record |
| **Who writes** | Alba | The project agent, except the declared status |
| **What Alba does** | Everything | **Reads only**, to know whether her product is being built |

**One record, one writer.** Alba creates it with the signed charter and never writes it again:
if two agents wrote it, the disagreement between them would stop being a signal and become a
race.

## The eight commands

| Command | What it does |
|---|---|
| `/product-setup` | **The first thing you run.** Looks at your folder, asks four questions and contrasts the definition you already have |
| `/product-discovery` | Interviews and tickets into themes with the citation of who said it, and the theme said for months that nobody has turned into anything |
| `/product-requirements` | The register with its gaps: no owner, no acceptance criteria, accepted with nobody having asked for it, and what nobody decides |
| `/product-definition` | The definition against the evidence of demand, and where business and data disagree |
| `/product-trace` | Requirement → decision → project → deliverable, and the two gaps above |
| `/product-spec` | The specification draft with verifiable criteria and the gaps marked, not filled |
| `/product-charter` | The charter: where the record is born and the writer changes hands |
| `/product-wake` | **The one you put on a clock.** What crossed a threshold with nobody doing anything |

## The twelve skills

They load on their own when the topic appears. Eight are product's own; four are literal
copies from `criterio-pmo`, because they are method and not role.

| Skill | What it encapsulates |
|---|---|
| `requirement-record` | **Alba's data contract.** Schema, extraction, citation, the five states and what each one demands |
| `product-health` | The ten signals, the four thresholds, the order they are read in and **which one is not a finding** |
| `demand-evidence` | What counts as evidence that somebody asked for this, what does not though it looks like it, and how it ages |
| `discovery-synthesis` | Interviews and tickets into themes with citations. A theme is a set of quotes, not a claim |
| `assumption-tracking` | The assumption written so it can turn out false, and the day it becomes a registered risk |
| `product-metrics` | The series with its source and its definition, and the contrast between declared and measured |
| `specification-draft` | The verifiable acceptance criterion, and the rule of marking the gap instead of filling it |
| `regulatory-sweep` | The obligations the definition touches, cited. **It does not opine on compliance** |
| `project-record` | The project record: it is born with the charter, and Alba is the one who creates it |
| `governance-artifacts` | What a charter contains and who decides what |
| `document-intake` | Which document has to be re-read and which does not, which formats can be read and with what |
| `raid-taxonomy` | Where an assumption moves to the day nobody verifies it |

## How it is verified

```
python3 tests/criterio-product/grade.py    over two products, with a negative control
python3 scripts/producto.py selftest      52 checks over the arithmetic
```

On the standard library, with nothing installed. Over a synthetic corpus with answers written
by hand from the documents — **including a negative control**: a product with a definition,
interviews and a register that produces not a single finding. An agent that finds something
there is a noise generator.

What that run proves and, in the same detail, **what it does not**, in
[`tests/criterio-product/EVIDENCIA.md`](../../tests/criterio-product/EVIDENCIA.md).

The full design, with the three classes of function and what stays with the person, in
[`docs/agents/product-manager.md`](../../docs/agents/product-manager.md) — in Spanish, as a
working document.
