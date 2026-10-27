# Frequently asked questions · Criterio CFO

The short answers to what people usually ask when they reach the close, control and reporting family. This file is the only source: the family's page on josenanez.com reads them from here.

## What it is

### What do Clara and Tomás do?

They process what the finance function already has. Clara, the controller, prepares the monthly close with its checklist and evidence, the bank and account reconciliations, every e-invoice against its entry and the auditor's package. Tomás, FP&A, puts the approved budget next to actual and committed spend, forecasts the year-end and prepares the budget committee's material.

### Do they replace the controller or the budget team?

No. They prepare the work and check it against all of its evidence: what does not tie out, what has no support and what is reported differently from what the documents say. The status of the close is declared by the controller, and that of the budget by the head of the area.

### What do they never do?

They do not post or correct entries, file returns or regulatory reports, sign, or declare the status of the close or the budget. They give no opinion on deductibility, rates or IFRS treatments, and they never state a rate, a deadline or the value of a tax unit from memory.

### Which accounting framework do they cover?

With the accounting framework each country adopted —IFRS in Colombia, Ecuador, Peru and Chile; in Mexico, IFRS or NIF depending on the entity—, and with the DIAN, SRI, SUNAT, SII and SAT electronic invoice processed from its official technical source. Every source is in the repository with its version, its link and the date it was consulted.

## How it is used

### Which documents do they process?

The ones the finance function already produces, as they are: the trial balance and general ledger exported from the ERP, bank ledgers and statements, e-invoices in XML, the close checklist, the auditor's requests, the approved budget and its versions, purchase orders and the budget committee's minutes.

### Do I need to change my ERP?

No. They process the Excel or CSV exports the ERP already produces. Neither of them connects to the ERP or writes to it.

### How do I organise the folder?

As it is: the agents process it that way. When starting from scratch, the family recommends one folder per entity and, inside it, one per period —books, banks, invoicing, supporting documents and audit— and one per budget year —approved, commitments, forecasts and minutes—. Setup searches for the entity's root folder, offers it and, if you say yes, marks it with a visible file, `_CRITERIO_FINANZAS.txt`. It is the only thing it writes among your documents.

### How long until the first result?

In the first fifteen minutes, `finance-setup` shows the status of the period's close: every checklist task with or without its evidence, and the signals the engine raised in the tie-out, the banks, the accounts and the invoices.

### Where do I see what they found?

In each command's report and in Rostrum, the portal for every family. It shows the latest each engine wrote, what falls due with a date and the full path of the folder each agent works in.

## How it is tested

### What data was it tested on?

On synthetic material from five countries —Colombia, Ecuador, Peru, Chile and Mexico—: four industries and one control entity per country, with no defects at all, where any signal is a failure. Invoices are generated with each country's official structure, and every family signal is planted at least once.

### How do you know the engine got it right?

The material carries a key with what was planted, and the engine never sees it. The test compares every signal by its name and its key: an extra one counts the same as a missing one. The gate that checks it runs on every change to the repository.

### Is the whole family tested yet?

The engine is, and the three agents ran on all fifteen entities in the material: round 4 on the nine of Colombia, Ecuador and Peru —80 of 80 signals with none extra and 74 of 74 record data points—, round 5 on Chile —26 of 26 and 24 of 24— and round 6 on Mexico —27 of 27 and 24 of 24—. The family is declared tested; nothing has run yet on an organisation's documents.

## Data and privacy

### Do my documents leave my organisation?

They are processed on the AI platform where the agent runs, like any conversation with it. The plugins do not connect to the internet or send us anything.

### What is stored, and where?

On your machine: the close and budget records, the reports, the log of each run and the receipt for accepting the terms, which every version of the family asks for again.
