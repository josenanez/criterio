# FAQ · Criterio CSO

Short answers to what people usually ask when they reach the sales function family. This file is the only source: the family's page on josenanez.com reads them from here.

## What it is

### What do Augusto and Valeria do?

Augusto puts the CRM pipeline next to its evidence and the forecast next to what backs it: which opportunity lacks the document its stage requires, which one is stalled, which one keeps slipping its close date, how much of what was committed has backing and how what closed is doing against the target. Valeria puts every sale next to its policy, its contract and its invoice: the discount against its approval level, what was won against Fidel's contracts, what was signed against Clara's invoices and the commission against the plan.

### Do they replace the head of sales?

No. They process and contrast. The forecast that is committed, the discount that is approved, the target and the commission are always decided by a person.

### Do they rate the sellers?

No. The signal belongs to the opportunity, not to whoever owns it. No report ranks or compares the people on the team, and if someone asks for the forecast or the target by seller, the agent says so and does not build it.

### What do they never do?

They do not write or change anything in the CRM, do not contact a customer, do not approve a discount or a price exception, do not set a target and do not settle or correct a commission.

## How it is used

### Do they connect to my CRM?

No. They process what the CRM exports, in CSV or Excel, with the export date in the name. A direct connection would be a different decision, with its own security review.

### Which CRM works?

Salesforce and HubSpot, each with its reader verified against the documentation it publishes: Salesforce's opportunity fields and HubSpot's deal properties. Any other CRM works with its CSV or Excel export and the column mapping the setup leaves. Microsoft Dynamics and Zoho, with their own reader, are on the roadmap.

### How does it know an opportunity has no evidence?

From the organisation's stage table: each stage says which document it requires —the proposal sent, the purchase order— and a stage also requires what the earlier ones do. The agent takes to the record every document in the evidence folder with its opportunity and type, and the engine crosses them.

### How does it know a close date slipped?

By comparing each export with the previous one: every time an open opportunity's close date moves to a later one, it counts. If the CRM exports the field history, as Salesforce does, it counts from the history.

### Where does the committed forecast come from?

From the sales committee's minutes or pack: the agent takes to the record the value committed for the period, with its citation. If the minutes commit no value, the report says it is missing and does not invent it.

### Do I need Fidel and Clara?

For crossing what was won with what was signed and invoiced, yes: Valeria takes the contract from Fidel's records and the invoice from Clara's, and never processes them again. The rest —the pipeline, the forecast, the target, the discount— works without them.

### How long until the first result?

Within the first fifteen minutes, `sales-setup` recognises each CRM export and shows the pipeline against its evidence, and `revenue-setup` shows what was won against what was signed and invoiced.

### Which countries does it serve?

The first version is tested in Colombia and Mexico. Ecuador, Peru and Chile, already in the other families' country registry, are on the roadmap.

## The data

### Do they keep my customers' contact data?

No. The record keeps the account and the opportunity, not a person's email or phone, and the engine flags a record that carries them as a problem.

### Are commissions published?

Not by default. They are the pay of identifiable people: the commission report does not appear in Rostrum unless Valeria's configuration says so.

### Where are my documents processed?

On the AI platform's infrastructure, not only on your machine. Confirm it is admissible under your policies before pointing it at confidential material.

## Status

### Is it ready to use?

Not yet: it is in construction. The engine passes its deterministic test on synthetic material from Colombia and Mexico; the round with the agents, with a key they never see, is what declares it tested, and its first version, the laboratory one, comes out with it.

### When does 1.0 arrive?

When Criterio declares it, with the three conditions of decision 0018: its planned scope released, two full rounds in a row with no new defects, and the record schema fixed.
