# Frequently asked questions · Criterio CLO

The short answers to what people usually ask when they reach the contracts and compliance family. This file is the only source: the family's page on josenanez.com reads them from here.

## What it is

### What do Fidel and Constanza do?

They process what the company signed and what it committed to comply with. Fidel keeps the contract register against its documents, expiries and renewal notice periods, obligations with their evidence, who signed with what authority, and what was paid against what was agreed and its guarantees. Constanza keeps the organisation's obligations matrix against its evidence, the policy review, new regulations with their assessment and the whistleblowing channel with its deadlines.

### Do they replace the legal team or the compliance officer?

No. They prepare the work and check it against all of its evidence: what falls due, what has no evidence, who signed without authority and what was paid outside what was agreed. The decision —to renew, to terminate, how a clause or a regulation is read— is always made by a person.

### Do they give legal opinions?

No. Neither of them interprets a clause, rules on the validity of a contract or a signature, or says what a regulation requires. What an obligation requires is defined by the organisation in its matrix, citing its source.

### What do they never do?

They do not decide to renew or terminate, do not draft, negotiate, sign or send contracts, amendments or notices, and do not declare the compliance status. They do not answer whistleblowing cases or process data about who reported.

## How it is used

### Which documents do they process?

The ones the area already has, as they are: the contract register, each contract with its amendments, insurance policies and guarantees, counterparty certificates, payments, the signing-authority matrix, the obligations matrix, the policy index, the regulatory register and the whistleblowing case register.

### How do I organise the folder?

As it is: the agents process it that way. When starting from scratch, the family recommends one folder per entity with its register, its policies, regulations and the channel; one per contract, with the contract, guarantees, counterparty and execution; and one per compliance period. Setup searches for the entity's root folder, offers it and, if you say yes, marks it with a visible file, `_CRITERIO_LEGAL.txt`. It is the only thing it writes among your documents.

### How long until the first result?

In the first fifteen minutes, `legal-setup` shows the contract calendar: what falls due, notice periods coming up or already past without a decision, and overdue obligations without evidence, with the signals the engine raised in the register, the signatures and the payments.

### Where do I see what they found?

In each command's report and in Rostrum, the portal for every family. It shows the latest each engine wrote, what falls due with a date —the notice period of an auto-renewing contract, the obligation that falls due— and the full path of the folder each agent works in.

## How it is tested

### What data was it tested on?

On synthetic material from five countries —Colombia, Ecuador, Peru, Chile and Mexico—: four industries and one control entity per country, with no defects at all, where any signal is a failure. Every family signal is planted at least once.

### How do you know the engine got it right?

The material carries a key with what was planted, and the engine never sees it. The test compares every signal by its name and its key: an extra one counts the same as a missing one. The gate that checks it runs on every change to the repository.

### Is the whole family tested yet?

The engine is, and Fidel and Constanza ran on all fifteen entities in the material: round 2 on the six of Colombia and Ecuador —37 of 37 signals with none extra and 808 of 815 record data points—, round 4 on Peru and Chile —37 of 37 and 812 of 813— and round 5 on Mexico —20 of 20 and 395 of 396—. Every data point missed has its defect, fixed and verified. The family is declared tested; nothing has run yet on an organisation's documents.

## Data and privacy

### Do my contracts leave my organisation?

They are processed on the AI platform where the agent runs, like any conversation with it. The plugins do not connect to the internet or send us anything.

### What is stored, and where?

On your machine: the contract and compliance records, the reports, the log of each run and the receipt for accepting the terms, which every version of the family asks for again.
