# Frequently asked questions · Criterio CDO

Short answers to what people arriving at the data family usually ask. This file is the only source: the family's page on josenanez.com reads them from here.

## What it is

### What do Custodia and Ariadna do?

Custodia puts each dataset in the data catalog beside its owner, classification and retention period, and says which policy is overdue, which report term is not in the glossary and which database with personal data is missing from the organisation's register. Ariadna follows each figure in the management reports back to its source: the one that does not match, the one from another cut-off, the broken lineage and the quality rule that fails.

### Do they correct data or figures?

No. No agent assigns an owner, decides a classification, deletes data or corrects a figure. They say what is missing and where, with the citation; the decision is the data office's and whoever signs the report.

### What frameworks do they work on?

On the DAMA-DMBOK areas —governance, quality and metadata with lineage—, the Basel Committee's BCBS 239 principles for the risk figure that reaches the board, and ISO/IEC 25012 for data quality. They are cited by name, never by their text.

## How it is used

### Does it connect to my databases or my catalog?

No. It processes the Excel or CSV exports of the catalog, the lineage, the source figures and the quality rules, and the documents the organisation leaves in its folder: the policies, the glossary and the reports. The setup maps the columns of any export.

### Does it process personal data?

No. From a database with personal data it processes only its metadata: its name, owner, classification and whether it is in the register. If an extract with people's records arrives, it is not opened.

### Who sets the tolerance, thresholds and periods?

The organisation, in its data and retention policies. The setup proposes them from those documents and the person confirms them.

## Status

### Is it tested?

The engine is tested against all its synthetic material, with a key the agents never see and two control entities with no signal at all. In 0.2.0, the two agents ran on every entity in the material, with a key they never see; in 1.0.0, round 2 in Colombia, Mexico and Peru: 94 signals and 348 data items, with a floor of 96.0% on signals and 98.9% on data, and no control with a signal. It is stable and launched. It has not been tested on a specific organisation's documentation.
