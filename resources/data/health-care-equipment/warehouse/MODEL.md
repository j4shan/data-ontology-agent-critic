# Surgical Supply Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: procedure volume and hospital demand, capital equipment and the product franchise, and reimbursement and margin. Question-to-column notes stay in `demand/coverage.md`, `capital/coverage.md`, and `finance/coverage.md`.

| | |
| --- | ---: |
| Datasets | 74 |
| Relationships | 200 |
| Logical identities | 74 |

Snowflake database `SURGICAL_SUPPLY`, account `surgicalsupply.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `surgicalsupply.`.

## What the model covers

Procedure volume and hospital demand hold the hospital, the country, and the site of care as different populations from the product. Procedure families include hips, knees, shoulders, trauma, vascular, and endoscopy. Volume, catch-up from a delayed quarter, site-of-care mix, and market growth are separate facts. Share compares Surgical Supply Inc growth with market and peer growth. Exchange-coverage effects, underlying hospital demand, customer response after the manufacturing disruption, and surgery-center buildout sit on this side. This is case volume a device maker uses, not a claim.

Capital equipment and the product franchise hold Mako, Inari, MedSurg, orthopedics, endoscopy, and the other franchises named on the calls. A capital system is Mako, Mako 4, the handheld robot, or the newer platform. The installed system is the current placement. Orders, backlog, and the quarter the backlog is planned to ship are separate from procedure volume. Supply shortages record whether a gap is limited to Inari or also hits other vascular and MedSurg products. Plant shifts are the capacity plan. Launches, trials, acquisitions, sales-force channels, and field restock are commercial facts on this slice.

Reimbursement and margin hold the physician-payment context for hip, knee, and shoulder, including the Medicare cut and the procedure and price response. Operating margin, the second-half and through-2028 path, input cost, price realization, the organic sales bridge, tariffs, and guidance are finance facts. The sales bridge keeps underlying demand, catch-up, revenue recognition, and capital apart. Tariff cost is tied to the manufacturing footprint and to China. This is not a payer remittance warehouse.

A graph build of this directory reports 74 datasets, 200 relationships, no unknown claims, and no contradictory edges.
