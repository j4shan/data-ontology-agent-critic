# Starbucks warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: demand, coffeehouse operations, and finance. Question-to-column notes stay in `demand/coverage.md`, `operations/coverage.md`, and `finance/coverage.md`.

| | |
| --- | ---: |
| Datasets | 76 |
| Relationships | 203 |
| Logical identities | 35 |

Snowflake database `STARBUCKS`, account `starbucks.us-west-2`. Node ids use the `sf:` prefix. Periods are Starbucks fiscal periods.

## What the model covers

Demand separates a transaction, a transaction line, and a comparable-sales bridge component. Morning and afternoon are daypart rows. Channels include cafe, drive-thru, delivery, and mobile order. Beverage platforms include brewed coffee, espresso, cold, refresher, energy, and protein. Rewards members and non-member demand are different populations. Delivery incrementality is its own fact so an in-store trip is not assumed to be the same order. Marketing spend that explains demand sits with campaigns. Menu cuts and assortment holes are their own facts.

Coffeehouse operations own the store, the ownership type (company-operated or licensed), and the licensee. Green Apron is a labor-model cohort with an install date and a weekly outcome, not only a store flag. The operating week carries labor hours, labor dollars, hours open, and ticket time. Remodels, closures, sales transferred from closures, and the new-unit pipeline are separate facts. A company-versus-licensed comparison fact holds the operating gap.

Finance holds the journal, North America company-operated operating margin, and a margin bridge. The bridge isolates coffee, other product cost, distribution, store labor, marketing, occupancy, and G&A. Tariff refunds are their own fact, with a flag for whether guidance included them. Product-cost savings are stored so they can be netted against commodity inflation. Guidance is a scenario fact with drivers for the high and low ends of the earnings range. A cost-savings roadmap separates work that hits this year from work that hits later. Marketing spend on the ledger is the P&L amount, distinct from the campaign-response fact on the demand side.

A graph build of this directory reports 76 datasets, 203 relationships, no unknown claims, and no contradictory edges.
