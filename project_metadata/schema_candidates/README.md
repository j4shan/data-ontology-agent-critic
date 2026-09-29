# Schema candidates

Scratchpad for three business-domain ontology catalogs used to exercise the
Data Ontology Graph service on schemas larger than the financial snapshot.

Each candidate is one directory:

| Directory | Business | Datasets |
| --- | --- | --- |
| `manufacturing/` | Alderford Pump Company, discrete pump manufacturing | 113 |
| `retail/` | Greenbasket Markets, regional grocery retail | 110 |
| `commerce/` | Meridian Marketplace, multi-seller commerce | 113 |

A candidate directory holds `README.md`, `business-model.md`, and `yaml/`.
`README.md` introduces the business and lists BI questions whose datasets and
joins are fixed by the metadata. The YAML directory is the finalized
intermediary the graph builder loads. It contains only `.yaml` files: logical
identities, one file per subject area, and the relationship file.

Datasets are dimensions, facts, and bridges. The grain column of each dataset is
the complete population of that logical identity (`is_entity_universe: true`).
A foreign key on another dataset realizes the same identity with
`is_entity_universe: false`. The edge between those two realizations carries
directional multiplicity and match existence. A storefront-to-cashier link is
`1:many` with `always` on both sides. A storefront-to-manager link is `1:1`,
always from the storefront and optional from the employee population.

Column descriptions and closed status codes are authored. Row counts, distinct
counts, and other data statistics are absent.

`proposed/schema-update-proposal.md` asks the intermediary schema to track
`logical_identities`, `nodes`, and `edges` in separate files. The manifests
under `proposed/manifests/` are examples of that tracking. They are not builder
input.

The domain modules under `domains/` are the authoring source. Regenerate the
YAML and business notes with:

```bash
python3 emit_catalogs.py
```

Run that command from this directory.
