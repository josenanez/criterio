# Terms of use

[Español](TERMS.es.md) · Version 1.5 · 2026-11-09

By installing, deploying, testing or running Criterio, you accept these terms. If you do not accept them, do not install it.

---

## 1. Not advice; every version is tested before it is published

Criterio gives **analysis tested against the evidence** to whoever decides: every data point with a citation to the document it comes from. It is not advice, it does not replace the judgement of whoever decides, and it creates no professional relationship of any kind between you and the maintainer or any contributor.

Every version goes through an internal validation before it is published: automated tests of the code on every change, and rounds in which each family's agents run their commands on synthetic test material from several industries and countries, with control entities where any signal is a failure, with no data from any organisation. What each agent produces is compared with an answer key, and the results —with their confidence margin, the defects found and their fix— are published in each family's test evidence, at https://www.josenanez.com/agents, and in the legal notice.

## 2. The decision, and its verification, belong to whoever signs it

Before using an analysis from Criterio to decide, sign, report, escalate or advise, you verify it against its sources and answer for that decision. The citations exist so that verification takes seconds; they are not a substitute for it.

## 3. What it can and cannot know

Its input is the documents you point it at. It does not know what was decided outside them. An absent finding is not evidence that nothing is wrong.

## 4. Your data

Documents you process are handled by the AI platform you run this on, under that platform's terms, not only on your machine. Confirm that this is admissible under your policies, your contracts and the applicable data protection law before processing confidential or personal material. That assessment is yours.

Do not send this project any client documents, real personal data, or confidential material. Contributions containing them will be rejected.

## 5. Warranty and liability

Governed by the Apache 2.0 licence, sections 7 and 8.

## 6. Contributions

Contributions are licensed under Apache 2.0 by the act of submitting them. By contributing you state that you wrote the content or have the right to submit it, and that it contains no confidential or client material.

Contributors are credited by name. Credit records who wrote something; it is not a warranty.

## 7. Trademarks

Apache 2.0 grants no trademark rights. "Criterio" and the maintainer's name may not be used to endorse or promote derivative products without written permission. Anthropic's marks are its own; this project is not affiliated with, endorsed by, or sponsored by Anthropic.

## 8. How acceptance is recorded

**One acceptance, as long as these terms do not change.** You accept these terms once, when you set Criterio up. That acceptance stays in force when you update any family to a new version, as long as the text of these terms is the same: updating does not ask you to accept again. We recommend always using the latest stable version of each family, which is the one that is tested and published with its evidence. Until the acceptance is recorded, the plugin answers questions but produces no analysis and no report. It never assumes it, never infers it from you continuing the conversation, and never records it without an explicit yes.

**A receipt that is yours.** On acceptance, the plugin leaves on your machine, in `.criterio/terminos/`, a Markdown receipt and a PDF receipt with your name, the date, the family version, the version of these terms, their SHA-256 fingerprint and the version-register entry, followed by the full text you accepted. Earlier receipts are kept: the succession of acceptances is the trail. The technical detail is in `docs/acceptance.md`, in the repository.

**Integrity.** Every receipt keeps its integrity and may not be modified. Its SHA-256 fingerprint (SHA-2, 256 bits) is recorded in the configuration, in the acceptance log and in a `.sha256` file next to it; any change, however small, produces another fingerprint and voids it as a record. The same holds for these terms: their fingerprint is published with every version.

**Legal notice and version register.** Criterio's legal notice and the version register —what changed in each version, which version each family is at, which terms govern it and their fingerprint— are published at https://www.josenanez.com/agents/criterio-pmo/legal. Every register entry carries the fingerprint of the previous one, so an altered or removed entry shows.

Every report the plugin generates carries the disclaimer and the state of the records it used, so the warning travels with the document rather than staying in this repository.

## 9. Changes to these terms

These terms are versioned. A change bumps the version and the date at the top of this file and enters the version register with its fingerprint. No change to these terms applies to you without your express acceptance: when the text changes, the plugin shows it to you and asks you to accept it before producing any analysis or report, and leaves a new receipt. If you do not accept it, you can keep using the version you already accepted.

## In short

This is what the plugin shows you before asking you to accept:

> Criterio gives management analysis tested against the evidence: every figure, every signal and every deadline with a citation to the document it comes from. It does not replace the judgement of whoever decides, nor professional advice: the decision, and its verification, belong to whoever signs it. It processes the documents you point it to and says what they show; what was agreed outside them it does not know. It is run by a language model (LLM), which can be wrong, which is why no data point arrives without its source. Your documents are processed on the infrastructure of the AI platform where you run it, not only on your machine. Every version is tested before it is published and its evidence is public; warranty and liability are those of the Apache 2.0 licence. It is accepted once and leaves a receipt in Markdown and PDF with its SHA-256 fingerprint; updating does not ask you to accept again unless these terms change. Full terms and legal notice: https://www.josenanez.com/agents/criterio-pmo/legal

---

Full text of the licence: `LICENSE`, at the root of the repository. Plain-language limits: `DISCLAIMER.md`. Legal notice and version register: https://www.josenanez.com/agents/criterio-pmo/legal
