# Acceptance criteria · criterio-pm

Nothing ships until all of these pass. They are written before the code on purpose: a
criterion written afterwards describes what was built, not what was needed.

## The record

1. **The agent never writes `declared`.** Not a documentation rule: a write-path
   restriction, and the selftest attempts it and asserts it fails.
2. **Every field carries its citation** — source document and date — or the state
   `not_found`. A field with a value and no source is a defect, not a degraded case.
3. **Two records never merge.** Escuadra's record and Plomada's reading of the same
   project stay separate files with separate owners, and no command writes both.

## Publishing

4. **Publishing is explicit.** `ficha-pm.json` reaches the project's governance folder
   only when a command puts it there. No command writes anything else outside the
   agent's own state, and the test enumerates what was written.
5. **A published record is a valid document**: Plomada reads it with its ordinary
   document intake, and every citation in it resolves.

## Commitments

6. **A commitment extracted from minutes carries who, what, by when, and the source.**
   A commitment with no date is counted separately — it cannot be overdue, and it must
   not vanish from the report, which is the failure this was built to end.
7. **The same commitment rescheduled is one commitment with a history**, not three. A
   third reschedule is reported as a block, not as three overdue items.
8. **The same question is never asked twice.** If nobody answered, the next run reports
   *"asked on the 12th, no answer"* — itself a finding — instead of asking again.

## Shared arithmetic

9. **The copied scripts are byte-identical to their source**, and the check that proves
   it runs in the same gate as everything else.
10. **Each copy runs standalone.** The installed plugin imports nothing from the other
    plugin's path.

## Evidence

11. **A synthetic corpus with known answers**, including a negative control: a project
    whose meetings produce no finding. An agent that reports on a healthy project is a
    noise generator.
12. **Every figure in the documentation comes from a run**, and the run is reproducible
    from the repository with the standard library and nothing installed.
