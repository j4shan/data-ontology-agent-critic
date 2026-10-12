# Computer Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: traditional server and storage demand, AI-server backlog and supply, and price versus volume. Question-to-column notes stay in `traditional/coverage.md`, `ai/coverage.md`, and `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 60 |
| Relationships | 106 |
| Logical identities | 60 |

Snowflake database `COMPUTER`, account `computer.us-central-1`. Node ids use the `sf:` prefix. Qualified names start with `computer.`.

## What the model covers

Traditional server and storage demand owns product category, customer type, country, region, channel, and the fiscal calendar. Traditional servers, storage, PCs, and networking are categories on that demand. Orders, deferred units, pull-forward, the installed-base upgrade cycle, and PC refresh drivers are demand facts. They do not store the unit price.

AI-server backlog and supply owns AI platforms, architecture, purchased components, and suppliers. Backlog, AI orders, AI shipments, CPU racks, ranked constraints, purchase commitments, and supply agreements are supply facts. DRAM, NAND, and boards are commodities Computer Inc buys. The slice does not describe a wafer fab.

Price versus volume owns the category price file, with unit price, price change, and price headroom. A growth bridge stores a price effect, a volume effect, and a share effect as separate amounts and does not replace the price file or the demand quantity. ISG, CSG, AI-server, and gross-margin facts stay on this side. Storage attach and shipment attach are their own facts, not columns on the AI shipment.

A graph build of this directory reports 60 datasets, 106 relationships, no unknown claims, and no contradictory edges.
