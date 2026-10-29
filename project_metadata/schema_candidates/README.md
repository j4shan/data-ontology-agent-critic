# Schema candidates

Scratchpad for the five business-domain ontology catalogs used to assess the
Data Ontology Graph service at realistic schema sizes.

Each candidate is one directory:

| Directory | Business | Datasets |
| --- | --- | --- |
| `manufacturing-discrete/` | Alderford Pump Company, discrete pump manufacturing | 114 |
| `retail-grocery/` | Greenbasket Markets, regional grocery retail | 110 |
| `commerce-marketplace/` | Meridian Marketplace, multi-seller commerce | 113 |
| `telecom-mobile/` | Northline Mobile, national mobile charging and usage | 173 |
| `healthcare-payer/` | Harbor Medicare Services, Medicare-scale claims processing | 157 |

The directory name is the catalog label: a sector, then a hyphen, then the specialty. Qualified dataset names use that label as their first segment, for example `healthcare-payer.claim.fact_claim_header`. The Snowflake database name is the same label in uppercase, with the hyphen written as an underscore, because an unquoted Snowflake identifier cannot contain a hyphen.

A candidate directory holds `README.md`, `questions.md`, and `business-model.md`.
`README.md` introduces the business. `questions.md` is the role-based analytical question
sheet for the benchmark. No loadable intermediary YAML is committed; a reference catalog
for the actor's current schema belongs under `resources/data/reference_catalogs/<domain>/`.

Datasets are dimensions, facts, and bridges. The grain column of each dataset is
the complete population of that logical identity (`is_entity_universe: true`).
A foreign key on another dataset realizes the same identity with
`is_entity_universe: false`. The edge between those two realizations carries
directional multiplicity and match existence. A storefront-to-cashier link is
`1:many` with `always` on both sides. A storefront-to-manager link is `1:1`,
always from the storefront and optional from the employee population.

Column descriptions and closed status codes are authored. `manufacturing-discrete`,
`retail-grocery`, and `commerce-marketplace` leave row counts and join fan-out
unstated. `telecom-mobile` and `healthcare-payer` add a 30-day synthetic population
in `statistics.md` and `statistics.json`: authored fact-table volumes, plus distinct
keys and average fan-out on each inbound and outbound join.

The domain modules under `domains/` are the authoring source. Regenerate the
business notes and statistics with:

```bash
python3 emit_catalogs.py
```

Run that command from this directory.
