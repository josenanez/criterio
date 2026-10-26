<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/en/criterio-cfo-oscuro.svg"><img src="../../docs/img/marca/en/criterio-cfo-claro.svg" alt="Criterio CFO · The finance function" height="48"></picture>

# Áurea · Treasury

<img src="../../docs/img/en/robot-aurea.gif" alt="Áurea" width="220" align="right">

**Áurea puts cash, payments and debt next to their policy.** You answer for the entity's cash.
She arrives with each account against its minimum and projection, each scheduled payment against
who may approve it, currency exposure against its limit and each covenant calculated from the
books Clara closes.

[Español](README.es.md) · `criterio-treasury` · Apache 2.0 · One instance per entity

**Status: the six commands built**, her skill and the calculation engine, tested by its self-test.
Her round with the agent on the test material is the next step; nothing has yet been run on an
organisation's documents. Nothing is announced as finished until it passes the
[acceptance criteria](ACCEPTANCE.md).

**She is the third agent of the CFO's office** ([ADR 0016](../../docs/decisions/0016-tesoreria-tercer-agente-cfo.md)):
she shares the engine, the folder and the period with Clara. The family is in
[criterio-cfo](../../families/criterio-cfo/README.md).

---

## What it is

The third capability of the CFO's office: treasury. O*NET puts treasurers and controllers in the
same occupation (11-3031.01), which is why Áurea lives in the CFO family and not apart.

## What it does

<!-- cfo:comandos · generado por scripts/familias.py; no se edita a mano -->
### The six commands

> They are typed with the plugin prefix: `/criterio-treasury:` and autocomplete does the rest. It is the only form that resolves in a Claude Code session.

| Command | What it does |
|---|---|
| `/criterio-treasury:treasury-setup` | The configuration, the inventory and the first cash position |
| `/criterio-treasury:treasury-scan` | Treasury up to date, with what changed and the new signals |
| `/criterio-treasury:cash-position` | Each account's cash against its minimum and projection, and the currency exposure |
| `/criterio-treasury:payment-check` | Each scheduled payment against who may approve it |
| `/criterio-treasury:debt-watch` | Debt against its maturity and what its contract requires |
| `/criterio-treasury:treasury-wake` | What treasury needs today; silent when nothing does |
<!-- /cfo:comandos -->

<!-- cfo:skills · generado por scripts/familias.py; no se edita a mano -->
### The two skills

They load on their own when the subject comes up. They are the knowledge the commands share, and they are consulted like a manual.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `finance-intake` | Which documents the family processes, where each one goes, what the engine processes directly and what the agent extracts to the record | Copy of Clara's · also in Tomás |
| `treasury-control` | Treasury against its policy: cash against its minimum and projection, payments against their approvers and the signing-authority matrix, currency exposure and covenants calculated from the trial balance | Own |
<!-- /cfo:skills -->

## What it is for

For treasury to reach the committee and the bank with cash, payments and debt checked against
their policy, without assembling it by hand. What she processes:

| Document | Where |
|---|---|
| Each account's statement, the same one Clara reconciles | `<AAAA-MM>/20-bancos/<account>/` |
| The payment schedule, with who approved each payment, and the projected cash flow | `<AAAA-MM>/60-tesoreria/` |
| The treasury policy, the signing-authority matrix, the debt register and the covenants | `00-referencia/` |
| The period's trial balance, for the covenants | `<AAAA-MM>/10-contabilidad/` |

**The policy is the organisation's.** Áurea does not propose it as a rule: without a policy there
is no cash minimum and no approvers by amount, and the report says so.

### What she never does

Áurea **never** moves money, makes a payment, logs into a bank portal, negotiates with a bank or
recommends an investment, a financing or a hedge. She processes the exports treasury already has,
and a person always takes the decision.

## Installing and configuring

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-treasury@criterio
```

Then `/criterio-treasury:treasury-setup`. **The first result, in the first fifteen minutes:** the cash position of each account against its minimum and its projection, taken from its own statements. Her report is not published to Rostrum by default: it
carries balances and accounts.

## Working with the others

Áurea does not talk to Clara or Tomás: she takes the statements Clara reconciles and the trial
balance Clara closes, from the same folder, and writes her own record in `tesoreria/` of the shared
state. Rostrum shows what falls due in her debt register; her report with balances is published only
if the configuration says so.

## Tests

Áurea's engine passes its self-test on a minimal entity with everything wrong: cash below its
minimum, deviation against the projection, currency exposure, payments without approval, signatories
without authority, maturities and covenants. The results are in [`tests/criterio-treasury/RESULTADOS.md`](../../tests/criterio-treasury/RESULTADOS.md),
and what is missing to call her tested, in the [acceptance criteria](ACCEPTANCE.md).

