# Terms of use

[Español](TERMS.es.md) · Version 1.1 · 2026-10-15

By installing, deploying, testing or running Criterio, you accept these terms. If you do not accept them, do not install it.

---

## 1. Not advice; every version is certified before it is published

Criterio produces **working drafts**. It is not advice and creates no professional relationship of any kind between you and the maintainer or any contributor.

Every version goes through an internal certification before it is published: automated tests of the code on every change, and rounds in which the three agents run all their commands on synthetic test data, built from real projects in financial entities, retail and mining, with no data from any organisation. What each agent produces is compared with an answer key, and the results —with their confidence margin, the defects found and their fix— are published in the test evidence and the legal notice: https://www.josenanez.com/agents/criterio-pmo.

## 2. Verification is yours

You are responsible for verifying every output before using it to decide, sign, report, escalate or advise. The citations exist so that verification is possible; they are not a substitute for it.

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

**One acceptance per version.** Every version of the agent family asks you to accept these terms, even when their text did not change: installing Criterio or updating it to a new version requires a new acceptance. Until the acceptance for the installed version is recorded, the plugin answers questions but produces no analysis and no report. It never assumes it, never infers it from you continuing the conversation, and never records it without an explicit yes.

**A receipt that is yours.** On acceptance, the plugin leaves on your machine, in `.criterio/terminos/`, a Markdown receipt and a PDF receipt with your name, the date, the family version, the version of these terms, their SHA-256 fingerprint and the version-register entry, followed by the full text you accepted. Earlier receipts are kept: the succession of acceptances is the trail. The technical detail is in `docs/acceptance.md`, in the repository.

**Integrity.** Every receipt keeps its integrity and may not be modified. Its SHA-256 fingerprint (SHA-2, 256 bits) is recorded in the configuration, in the acceptance log and in a `.sha256` file next to it; any change, however small, produces another fingerprint and voids it as a record. The same holds for these terms: their fingerprint is published with every version.

**Legal notice and version register.** The legal notice of the agent family and the version register —what changed in each version, which terms govern it and their fingerprint— are published at https://www.josenanez.com/agents/criterio-pmo/legal. Every register entry carries the fingerprint of the previous one, so an altered or removed entry shows.

Every report the plugin generates carries the disclaimer and the state of the records it used, so the warning travels with the document rather than staying in this repository.

## 9. Changes to these terms

These terms are versioned. A change bumps the version and the date at the top of this file and enters the version register with its fingerprint. Since every family version is accepted again, a change to the terms reaches whoever uses Criterio on the next update.

## In short

This is what the plugin shows you before asking you to accept:

> Criterio produces working drafts, not decisions or advice. It processes the documents you point it to and says what they show; it does not know what was said outside them. It can be wrong, which is why every data point comes with a citation to the document it came from: verification is yours. Your documents are processed on the AI platform's infrastructure, not only on your machine. Every version is certified before it is published; warranty and liability: Apache 2.0 licence. Every version is accepted again and leaves a receipt in Markdown and PDF with its SHA-256 fingerprint. Full terms and legal notice: https://www.josenanez.com/agents/criterio-pmo/legal

---

Full text of the licence: `LICENSE`, at the root of the repository. Plain-language limits: `DISCLAIMER.md`. Legal notice and version register: https://www.josenanez.com/agents/criterio-pmo/legal
