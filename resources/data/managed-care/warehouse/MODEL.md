# Health Plan Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from 3 subject slices: membership and channel, medical cost and provider, price, benefit and margin. Question-to-column notes stay in `membership_channel/coverage.md`, `medical_provider/coverage.md`, `price_benefit/coverage.md`.

| | |
| --- | ---: |
| Datasets | 89 |
| Relationships | 202 |
| Logical identities | 41 |

Snowflake database `HEALTH_PLAN`, account `healthplan.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `healthplan.`.

## What the model covers

Membership and channel own insured member-months by insurance line, state, funding arrangement, and enrollment channel; a member-month is for an insurance line, not a client of a services business. Medical cost and provider own utilization counts, pharmacy claim counts, provider panel and facility capacity, dispute cases, and coding submissions. Price, benefit, and margin own premium, incurred medical cost, claim reserves, provider reimbursement, pharmacy cost and rebates, and segment results; premium, medical cost, and the loss ratio are amounts and a percent whose premium and member-month denominators are on separate facts at shared keys.

UnitedHealth insured membership and Optum services and Elevance insured membership and Carelon services each have their own segment and business results. Blue-plan bidding is an Elevance Carelon fact and employed clinicians are an Optum fact; they are not one shared fact. Medicare Advantage and Medicaid are plan types, ASO is a funding arrangement, and Part D is a separate pharmacy benefit program dimension, so they are not one code list.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`. No column stores a conclusion marker. A scenario dimension with `reported` and `guide` replaces any guidance column on the fiscal-quarter dimension, so one quarter can be both a reported result and a later guide.

A graph build of this directory reports 89 datasets, 202 relationships, 41 logical identities, no unknown fields, and no contradictory edges.
