# Frequently asked questions · Criterio CTO

Short answers to what people usually ask when they reach the technology family. This file is the only source: the family page on josenanez.com reads them from here.

## What it is

### What do Fausto and Domingo do?

Fausto puts each production change next to its approval and review, each deployment next to its change, each major incident next to its cause and each service next to the level agreed with the business. Domingo puts each asset next to its owner and its manufacturer's support, each licence next to its use, each vendor next to its service level and the cloud bill next to its budget.

### Do they approve changes or choose vendors?

No. No agent approves a change, decides an architecture, rates an incident, chooses a vendor, decides to renew or retire an asset or interprets a contract. They say what is missing and where, with the citation; the decision belongs to the change board, the architecture board, the technology office and legal.

### And security?

It belongs to the CISO family: vulnerabilities, controls and security incidents are processed by Alexis, Guillermo and Amparo. The CTO takes from technology what is not security.

### What frameworks do they work on?

ISO/IEC 20000-1, service management, for changes, incidents and service levels, and ISO/IEC 19770-1, IT asset management. In a supervised entity in Colombia, also the Financial Superintendency's External Circular 005 of 2019, on the cloud. They are cited by name, never by their text.

## How it is used

### Does it connect to ServiceNow, Jira or my cloud?

No. It processes the Excel or CSV exports of the changes, deployments, incidents, inventory, licences and cloud bill, and the documents the organisation leaves in its folder: the policy, the service catalogue, the board minutes and the vendor contracts.

### Who sets the deadlines and levels?

The organisation, in its change and service level policy and its service catalogue. The setup proposes the deadlines and thresholds from those documents and the person confirms them; who approved each change is in the board minutes.

## Status

### Has it been tested?

The engine is tested against all its synthetic material, with a key the agents never see and two control entities with no signal. The round with the two agents comes in 0.2.0. It has not been tested on a specific organisation's documentation.
