[Español](DISENO.es.md) · [← The family](README.md)

# criterio-cae · the family design

**Status: built, in testing (version 0.1.0).** The commands, the skills and the calculation engine
are built on the common core; the engine passes its deterministic test against the material in
`tests/criterio-cae/`. The round with the three agents comes in 0.2.0. Scope in [ADR 0033](../../docs/decisions/0033-la-familia-cae.md).

**This is the family's design sheet**: the signals the code calculates, each command with its input,
process and report, and the decisions taken. What the family does, how it installs, the folder structure
and the roadmap are on its [page](README.md).

The language model (LLM) extracts; the code calculates; the opinion —what is audited, what priority a
finding has, whether a closure holds— always belongs to the auditor. **The role is defined on the Global
Internal Audit Standards** (F-01) and their topical requirements (F-02), not on each country's law; each
signal is tied to its standard, cited by number and title.

**Where this document comes from.** The tables of agents, signals, commands and figures are not written
here: they come from [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) and [`fuentes.json`](fuentes.json).

## One agent per role

<!-- cae:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| The audit plan | **Prudencia** — from the Latin *prudentia*, a contraction of *providentia*, «seeing ahead»: the plan that looks at risk before it happens | `criterio-audit-plan` | The audit plan against the audit universe and the risk matrix: high risks with no engagement, units past their cycle, an outdated risk assessment, the areas the plan has to consider, unapproved changes, late engagements, hours that do not add up, a missing topical requirement and the external quality assessment |
| Audit engagements | **Justo** — from the Latin *iustus*, «according to law»: every finding against its criteria | `criterio-audit-work` | Each engagement against its program and its working papers: an unapproved program, a finding without its criteria, condition, cause, effect or priority, a finding with no working paper, an unexecuted step, an unreviewed paper, a report that does not say what the papers say, a priority the methodology does not give and an auditor reviewing what they were in charge of |
| Finding follow-up | **Remedios** — from the Latin *remedium*, «what heals again»: every finding until its remedy | `criterio-remediation` | Each finding until it is closed: an action plan with no owner or date, an overdue one with no evidence or explanation, a date pushed back again and again, a closure with no evidence or validation, a finding that comes back, an accepted risk that did not reach senior management or the board and an external finding missing from the register |
<!-- /cae:agentes -->

## The signals: what the code calculates

<!-- cae:senales · generado por scripts/familias.py; no se edita a mano -->
**Prudencia · The audit plan**

| Signal | Raised when |
|---|---|
| `high_risk_not_covered` | A risk rated high or critical in the matrix has no engagement in the plan within the methodology's cycle |
| `auditable_unit_overdue` | A unit in the audit universe went past its rotation cycle with no engagement |
| `risk_assessment_outdated` | The risk assessment behind the plan is more than a year old (Standard 9.4) |
| `plan_area_not_considered` | The plan does not consider IT governance, fraud risk or compliance and ethics programs, and does not say why (Standard 9.4) |
| `plan_change_unapproved` | An engagement was added, cancelled or postponed without the minutes of the body that approves the plan |
| `engagement_behind_schedule` | An engagement in the plan went past its start or close date without being under way or finished |
| `plan_hours_exceed_capacity` | The plan's hours exceed the team's available hours in the period |
| `topical_requirement_missing` | An assurance engagement on cybersecurity or third parties does not carry the topical requirement in force in its program |
| `external_assessment_overdue` | The last external quality assessment is more than five years old (Standard 8.4) |

**Justo · Audit engagements**

| Signal | Raised when |
|---|---|
| `work_program_not_approved` | The work program has no approval from the chief audit executive before its first paper (Standard 13.6) |
| `finding_element_missing` | A finding lacks its criteria, condition, effect or priority, or has neither its root cause nor the reason it could not be identified (Standards 14.2 and 14.3) |
| `finding_without_workpaper` | A finding cites no working paper, or cites one that does not exist (Standard 14.6) |
| `procedure_not_executed` | A step in the work program has no working paper and no reason why it does not apply (Standard 12.3) |
| `workpaper_not_reviewed` | A working paper has no supervisor review and chief audit executive approval before the report date (Standards 12.3 and 14.6) |
| `report_differs_from_workpapers` | The report carries a finding, a priority or a figure different from its papers |
| `rating_inconsistent` | A finding's priority is not the one the methodology gives for its impact and likelihood (Standard 14.3) |
| `auditor_reviews_own_work` | An auditor assigned to an assurance engagement was in charge of the audited activity in the previous twelve months (Standard 2.2) |

**Remedios · Finding follow-up**

| Signal | Raised when |
|---|---|
| `action_plan_missing` | A communicated finding has no action plan, owner or date (Standard 15.1) |
| `action_plan_overdue` | An action plan went past its date with no evidence of implementation and no documented explanation of the delay (Standard 15.2) |
| `due_date_extended_repeatedly` | A plan's date was pushed back more times than the methodology allows |
| `closure_without_evidence` | A plan was closed with no evidence of implementation or no audit validation (Standard 15.2) |
| `finding_repeated` | The same condition, in the same process, appears again after its finding was closed |
| `risk_accepted_not_escalated` | Management accepted a risk above appetite and there is no record that it was discussed with senior management or, if unresolved, that it reached the board (Standard 11.5) |
| `external_finding_untracked` | A finding from the statutory auditor, the external auditor or the supervisor is not in the register with its plan |
<!-- /cae:senales -->

## Prudencia's commands, in order of importance

<!-- cae:comandos-prudencia · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `plan-setup` | The root folder. Questions: entity and its tax ID, country, the period, the rotation cycle of each risk level, from which rating a risk is high, who approves the plan under the charter, the date of the last risk assessment and of the last external quality assessment | Inventory of what is there; processes the universe, the risk matrix and the plan in `10-plan/` and says how many rows it recognises; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the recognised tables; the period's first record |
| 1 | `plan-scan` | The universe, the matrix, the plan, the minutes and the team's capacity in `10-plan/`, and the period's record | Brings each new set of minutes into the record —which engagement it adds, cancels or postpones and who approved it—, with its citation; recalculates the signals | What went into the record; the minutes not yet in it; the new signals; what could not be processed and why |
| 2 | `plan-coverage` | The risk matrix, the audit universe and the plan in `10-plan/`, with the cycle in the configuration | Matches each high risk with the plan's engagements and each unit in the universe with its last engagement; checks that the plan considers IT governance, fraud and compliance and ethics, and that the risk assessment is under a year old | High risks with no engagement, units past their cycle, areas not considered and the age of the risk assessment |
| 3 | `plan-status` | The plan in `10-plan/` and the minutes in the record | Each engagement against its start and close dates, and each change to the plan against the minutes that approve it | Late engagements and unapproved changes, each with its date and citation |
| 4 | `plan-capacity` | The plan and the team's capacity in `10-plan/` | Adds up the plan's hours and the team's available hours in the period; checks that each assurance engagement on cybersecurity or third parties carries its topical requirement in force | Plan hours against available hours and the engagements without their topical requirement |
| 5 | `quality-status` | The date of the last external quality assessment, from the configuration or `00-referencia/` | Counts the years since the last external assessment against the five that Standard 8.4 sets | The date of the last one, of the next one and how long is left or how long has passed |
| 6 | `plan-wake` | The configuration and the run log | Decides whether the plan needs processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | What ran and why, or nothing |
| 7 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /cae:comandos-prudencia -->

## Justo's commands, in order of importance

<!-- cae:comandos-justo · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `work-setup` | The root folder. Questions: entity and its tax ID, country, the period, the methodology's priority scale —each level with its impact and likelihood— and who approves the program and the papers | Inventory of what is there; recognises the engagements in `20-trabajos/` and the team in `00-referencia/`; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the recognised engagements; the period's first record |
| 1 | `work-scan` | The programs, working papers and reports in `20-trabajos/`, and the period's record | Brings each new or changed finding into the record —its criteria, condition, cause, effect, priority and the papers it cites— and what the report says, with its citation; recalculates the signals | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `finding-check` | The findings in the record and the priority scale in the configuration | Checks that each finding has its criteria, condition, effect, priority and root cause —or the reason it could not be identified—, and that its priority is the one the methodology gives for its impact and likelihood | Each finding with what it lacks and the priority the methodology gives |
| 3 | `workpaper-check` | The work program and the index of working papers of each engagement in `20-trabajos/` | Checks that the program was approved before the first paper, that each step has its paper or the reason it does not apply, that each paper has its review and approval before the report and that each finding cites a paper that exists | Each engagement with its program, the steps with no paper, the papers with no review and the findings with no paper |
| 4 | `report-check` | What the record holds from each engagement's report and working papers | Matches each finding in the report with the one in its papers: that it is there, with the same priority and the same figures | The differences between the report and the papers, each with both citations |
| 5 | `objectivity-check` | Each engagement's assignments and the team's role history in `00-referencia/` | Matches each auditor assigned to an assurance engagement with the activities they were in charge of in the previous twelve months (Standard 2.2) | The assignments with a possible impairment, with the date and citation |
| 6 | `work-wake` | The configuration and the run log | Decides whether the engagements need processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | What ran and why, or nothing |
| 7 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /cae:comandos-justo -->

## Remedios's commands, in order of importance

<!-- cae:comandos-remedios · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `remediation-setup` | The root folder. Questions: entity and its tax ID, country, the period and how many times the methodology allows a plan's date to be pushed back | Inventory of what is there; processes the findings register and the accepted-risk register in `30-seguimiento/` and says how many rows it recognises; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the recognised registers; the period's first record |
| 1 | `remediation-scan` | The findings register, the evidence, the accepted risks and the external reports in `30-seguimiento/`, and the period's record | Brings each new piece of evidence and explanation of delay, and the findings of each external report, into the record, with their citation; recalculates the signals | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `action-status` | The findings register in `30-seguimiento/` and the record | Each action plan against its owner, its date and its reschedules; the overdue ones, with their evidence or the documented explanation of the delay | Plans with no owner or date, the overdue ones and those pushed back more than the methodology allows, with the days |
| 3 | `closure-check` | The findings register, the evidence in `30-seguimiento/` and the earlier findings | Checks that each closure has its evidence and its audit validation, and looks for the same condition in the same process among findings already closed | Closures with no evidence or validation and findings that come back, with both citations |
| 4 | `committee-brief` | The findings register, the accepted-risk register and the external reports in `30-seguimiento/` | Gathers what is overdue, what repeats, the risks accepted above appetite that did not reach senior management or the board (Standard 11.5) and the external findings missing from the register | The brief for the committee, each point with its citation; no audit conclusion |
| 5 | `remediation-wake` | The configuration and the run log | Decides whether follow-up needs processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | What ran and why, or nothing |
| 6 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /cae:comandos-remedios -->

## Third-party figures

<!-- cae:cifras · generado por scripts/familias.py; no se edita a mano -->
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (ACFE), C-02 (ACFE), C-03 (ACFE).
<!-- /cae:cifras -->

## Decisions closed

- The names, Prudencia, Justo and Remedios, and the structure: three agents, their twenty-four signals and their commands (decision 0033).
- The Global Internal Audit Standards are cited by number and title: their text has all rights reserved.
- Each country's regulation supports no signal until verified in its official text: Colombia (F-10) and Brazil (F-12) are verified; Peru (F-11) is not yet. ISO 19011 stays out of 0.1.0 until its current edition is verified.
- The public sector stays out of 0.1.0.
