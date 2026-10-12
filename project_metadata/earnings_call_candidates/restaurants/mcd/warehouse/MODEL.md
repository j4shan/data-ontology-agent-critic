# Burger Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: guest demand, the restaurant system, and finance. Question-to-column notes stay in `guest/coverage.md`, `system/coverage.md`, and `finance/coverage.md`.

| | |
| --- | ---: |
| Datasets | 71 |
| Relationships | 283 |
| Logical identities | 38 |

Snowflake database `BURGER`, account `burger.us-east-1`. Node ids use the `sf:` prefix.

## What the model covers

Guest demand is a check, a check line, and a restaurant-day sales row, kept as different grains. Daypart, income cohort, offer, protein, beverage platform, and loyalty frequency are their own datasets. Comparable sales split into traffic, check, and price. Baseline guest counts are stored apart from promoted guest counts. Weather and the prior-year food-safety comparison are columns on the restaurant-day sales fact. Loyalty frequency and the remaining global technology-stack blockers are a rollout fact, not a note on the member row.

The restaurant system holds the restaurant, the franchisee, and the operator as different populations. An ownership spell records company-operated versus franchised operation. Franchisee period cash flow is not the company-operated margin. Openings, remodels, kitchen equipment, development results by segment, commodity cost, and supplier shipments sit on this side. Segments are the U.S., international operated markets, and developmental license markets.

Finance holds the journal, company-operated restaurant P&L, a monthly margin bridge, royalty charges, rent charges, G&A, capex by project type, franchisee support payments, currency, and segment consolidation. The margin bridge keeps inflation, mix, and price apart. Beef cost and energy cost are commodity portions of that bridge, not a single food-cost bucket. Franchisee profit stays on the system cash-flow fact.

A graph build of this directory reports 71 datasets, 283 relationships, no unknown claims, and no contradictory edges.
