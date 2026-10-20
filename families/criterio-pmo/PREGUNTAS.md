# Frequently asked questions · Criterio PMO

Short answers to what people usually ask when they reach the project governance family. This file is the only source: the family's page on josenanez.com reads them from here.

## What it is

### What do Vera, Samuel, Alba and Rostrum do?

They process what the project office has already written. Vera builds one record per project with the citation of every data point and consolidates the portfolio; Samuel keeps the commitments from each meeting of a project; Alba checks a product's definition against the evidence of demand; Rostrum publishes the report for whoever never opens a folder.

### Do they replace the PMO?

No. They prepare working drafts and say what changed, what contradicts what and what no document supports. No agent declares a project's status: a person does.

### What do I need to use them?

A paid Claude plan, the desktop app if the documents live on your computer, and a folder with the documentation as it is. A messy folder is the normal case.

### How do I organise the folder?

As it is: the agents process it that way, and the tests check it with four different layouts. Starting from scratch, the family recommends one folder per project and one per product, each starting with its code, and inside four folders: governance, plan, tracking and meetings for a project; definition, discovery, metrics and decisions for a product. The detail is in the family README.

## How it is tested

### What data was it tested on?

On test data from four industries —financial institutions (banks and credit unions), retail and mining in South America—, built to be more demanding than those organisations' usual documentation: over 500 documents per round in Markdown, Word, PDF, Excel and CSV; contradictions between documents; commitments moved up to six times; milestones declared met with no receipt; projects gone silent; vendor deliveries with no evidence; and in each industry one healthy project that must raise no alert.

### How do you know an agent got it right?

Each round comes with a key of what the material holds, derived from the facts the generator wrote. No agent sees it: every session is audited and the number of reads is published (zero in all of them). Every figure is published with its count and its 95% confidence margin.

### Where is the evidence?

In the repository, under `tests/evidencias/`: what each command showed in each round, the key, the grading, and every defect with its origin, the commit that fixes it and the round that verified it. The family's page summarises it.

### Has it been used in an organisation yet?

Not yet on a specific organisation's documentation: that is the next step, and what will decide version 1.0. If your PMO wants to be among the first, open an issue in the repository.

## Data and privacy

### Do my documents leave my organisation?

They are processed on the AI platform where the agent runs, like any conversation with it. The plugins do not connect to the internet and send us nothing.

### What is stored, and where?

On your computer: the records, the reports, the log of each run and the receipt for accepting the terms. None of it travels anywhere.

### Do you collect usage statistics?

No. Today the only way back is the one you choose: an issue on GitHub. Sharing findings to improve the family will always be a question, and nothing is ever sent without a yes.

## Versions and licence

### Why is the version not 1.0 yet?

Because the record schema may change with the first use on real documentation, and a 1.0 promises it will not. 1.0 comes when the schema survives that use.

### How much does it cost?

Nothing. It is open source under Apache 2.0: use it in your organisation without asking permission, and adapt it. The contribution on the page is voluntary and unlocks nothing.

### What do I accept before using it?

The terms of each version. The agent shows them, asks for an explicit yes and leaves a receipt in Markdown and PDF with the SHA-256 fingerprint of the terms. Every new version is accepted again.

## Help

### How do I report an error?

With an issue in the repository and the document that shows it, with nobody's real data. Security flaws go through GitHub's private report, never in a public issue.

### Can I build an agent for another function?

Yes. The repository explains the method and the acceptance criteria, and the finance and legal families are declared and not yet built: a function's agent should be written by someone who knows the work.
