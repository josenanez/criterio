# Frequently asked questions · Criterio EA

The short answers to what people usually ask when they come to the executive office family. This file is the only source: the family page on josenanez.com reads them from here.

## What it is

### What does Ofelia do?

She prepares the work of the executive's office. She sets the week beside the meetings and the commitments, builds the pack for each governing body's next meeting with the record of each decision, drafts the minutes from the notes, follows the commitments in each set of minutes and says which email is waiting for a reply.

### Does she replace whoever assists the executive?

No. She prepares and checks: which meetings clash, which meeting has no materials, which minutes are still unsigned, which agreement has no owner or date. What is accepted, sent and put first is always decided by a person.

### Does she recommend what to decide?

No. Each decision arrives with the options the documents bring, in the order they bring them, with the evidence for each one, what is still unknown and the date that sets the deadline. The engine rejects a record that ranks the options or marks one as recommended.

### What does she never do?

She does not send, schedule, accept or move anything. She does not edit original minutes, calendars or emails, does not declare a commitment met without a document to back it and does not evaluate a person or a team.

## How it is used

### Which documents does she process?

The ones the office exports: the calendar as .ics, the emails saved as files, and each meeting's notice, materials, notes and signed minutes. She does not connect to the mailbox or the calendar: a direct connection is a separate decision, with its own privacy review.

### How do I organise the folder?

As it is: Ofelia processes it that way. If you start from scratch, the family recommends one folder per executive with its reference files, calendar, correspondence, drafts and one folder per meeting of each governing body. Setup looks for the office folder, proposes it and, if you say yes, marks it with a visible file, `_CRITERIO_DIRECCION.txt`. Among your documents, besides that mark, she only writes her drafts, in `90-borradores/`.

### How long until the first result?

Within the first fifteen minutes, `ea-setup` shows the calendar for the next two weeks with its clashes, the meetings without materials and those still without minutes.

### Which countries does she work in?

Any. Ofelia processes no invoices or regulations, only the calendar, the minutes and the email, so the office's country is a data point, not a limit. What does change from one office to another is how its calendar and email provider exports: that is what gets tested next.

### Where do I see what she found?

In each command's report, in her state folder. Her report is not published in Rostrum unless the configuration says so.

## How it is tested

### What data was it tested on?

On synthetic material from two countries —Colombia and Ecuador—: a president's office and a general manager's office with seeded defects, and one control office per country, with no defects at all, where any signal is a failure. Every signal is seeded at least once, and the material also tests the rules of real operation: a meeting in another time zone that only clashes after the clock change, an old calendar that gives no clashes, a draft put in `40-acta/` and an excluded folder.

### How do you know the engine got it right?

The material carries a key with what was planted, and the engine never sees it. The test compares every signal by its name and its key: an extra one counts the same as a missing one. The gate that checks it runs on every change to the repository.

### Is the family tested yet?

The engine is, against the key of the four offices. The agent's extraction —the agreements, commitments and decisions in each set of minutes, and what each email asks for— is tested in the round with the agent on the same four offices, published with every output, its cost and its grade. Nothing has run yet on a real executive's office.

## Data and privacy

### Do the calendar and the emails leave my organisation?

They are processed on the AI platform where the agent runs, like any conversation with it. The plugin does not connect to the internet or send us anything. The executive's office is among the most sensitive things an organisation has: that is why she processes exports, not accounts, and respects the folders you exclude.

### What is kept and where?

On your computer: the meeting and correspondence records, the reports, the drafts, the log of each run and the receipt for accepting the terms, which each version asks for again.
