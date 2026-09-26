# Acceptance criteria · criterio-product

Nothing ships until all of these pass. They are written before the code on purpose: a
criterion written afterwards describes what was built, not what was needed.

## The register

1. **Every field carries its citation** — source document and date — or the state
   `not_found`. A field with a value and no source is a defect, not a degraded case.
2. **A requirement states the problem, not the solution.** If what is written already
   decides how, the conversation about what is needed never happened.
3. **A proposed requirement is not asked for evidence or acceptance criteria.** Nobody has
   said it will be built. Demanding them turns the register into paperwork, and the test
   asserts that no signal fires.
4. **The five states are closed.** A state outside the vocabulary is computed as `unknown`
   and never invented into something else.

## The definition against the evidence

5. **Every claim of the definition lands in exactly one of three buckets**: held up by
   evidence, held up by a declared assumption, or not stated anywhere. The third one is
   reported, not omitted.
6. **A contradiction carries both sources and both dates.** A signal that names the
   disagreement without naming the two documents does not ship: it lets nobody do anything.
7. **A difference below the threshold is not reported.** Imprecision reported as
   contradiction ends the report's readership, and the test asserts the quiet case is quiet.

## The seam with the project

8. **The agent never writes `declared`**, not even at the moment it creates the record. The
   person declares; the agent shows what against.
9. **One record, one writer.** Alba creates the project record with the signed charter and
   writes it no more. The test enumerates what was written.
10. **A trace is confirmed against the project's record, never against the register itself.**
    With no records folder in reach, no trace is reported as confirmed — and that is stated
    in the output rather than assumed.
11. **The charter is a draft until a person signs it.** The record is created after the
    signature, never before.

## Evidence

12. **A synthetic corpus with known answers**, including a negative control: a product whose
    definition, interviews and register produce no finding. An agent that reports on a
    healthy product is a noise generator.
13. **Every figure in the documentation comes from a run**, and the run is reproducible from
    the repository with the standard library and nothing installed.
14. **The copied scripts are byte-identical to their source**, and the check that proves it
    runs in the same gate as everything else.
