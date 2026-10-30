# Frequently asked questions · Criterio CISO

Short answers to what people usually ask when they arrive at the information security family. This file is the only source: the family page on josenanez.com reads them from here.

## What it is

### What do Alexis, Guillermo and Amparo do?

Alexis puts every control in the statement of applicability next to the evidence that it operated, and says which access review, critical third-party assessment and risk acceptance lapsed. Guillermo puts every scanner vulnerability next to its severity's deadline, the KEV catalog of what is exploited and the scan that proves its closure. Amparo puts every incident next to its severity's containment deadline and every notification the matrix requires, and every continuity test next to its calendar.

### Do they replace the security lead?

No. They process and contrast. Accepting a risk, approving an exception, notifying a supervisor and declaring a control met are always decided by a person.

### Do they certify my organisation against ISO/IEC 27001?

No. They do not rate maturity or certify against any standard. They take the controls from the organisation's statement of applicability, with the number and name it gives them, and say which one has no evidence that it operated.

### What do they never do?

They do not run a scan, connect to a system, a console or the internet, accept a risk, approve an exception, notify anyone, run a test or a restore, or open credentials, keys or backups.

## How it is used

### Do they connect to my scanner or my SIEM?

No. They process what the organisation exports and leaves in the folder: the scanner exports in CSV or Excel, the KEV catalog as downloaded, the reports and the registers. A direct connection would be another decision, with its own security review.

### Which scanner works?

Any that exports CSV or Excel. Guillermo recognises the common headers —host, CVE, severity, CVSS— and, if it does not, asks which column carries each field and keeps it in the configuration. The native formats of Tenable, Qualys, Rapid7 and Microsoft Defender come in a later increment, each from its source.

### Where do the deadlines come from?

From the organisation's policy. In the setup, the agent reads it and proposes each severity's remediation days or containment hours, with the page they come from, and the person confirms. If the policy does not state them, they are asked. No deadline is set by the agent.

### What is the KEV catalog?

CISA's list of the vulnerabilities being exploited, with their remediation date. Guillermo crosses it with what is open. The date is set by a directive for United States federal agencies: for the organisation it is a reference, and its deadline is still its policy's.

### How does it know a notification was late?

By the time of its record —the filing, the email sent, the acknowledgement— against the deadline in the organisation's matrix, counted from the detection time stated in the incident report.

### How long until the first result?

Each setup command takes about fifteen minutes: it looks at the folder, says what it will not open, asks the questions no document answers and shows the first report.

### Which countries does it work in?

The family is defined on international standards, not on each country's law: it works the same in any country in the registry. Each country's regulation —the supervisor's circular, the data protection law— goes into the organisation's notification matrix.

## The data

### Do they open my credentials or my backups?

No. A key file, a password vault, a database dump, a compressed archive or a file whose name says it is a secret is excluded by default. The report says which it excluded, so the person can take them out of the folder.

### Are vulnerabilities published in Rostrum?

No, unless Guillermo's configuration says so. A report of open vulnerabilities is a map for an attacker.

### Where are my documents processed?

On the infrastructure of the AI platform the agent runs on, not only on your machine. Confirm that is acceptable under your policies before pointing it at confidential material.

## Status

### Is it ready to use?

It can be installed, and it is a laboratory one, in its version 0.1.0: the engine is tested on synthetic banking, retail, healthcare and technology material, with a key it never sees and two control entities. The round with the three agents is the next step.

### Is it stable?

Not yet. A family is declared stable when its round with the agents passes the 95% confidence floor on signals and data.
