# Surgical Robot Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: procedure volume, the installed system base, and margin, tariffs, and innovation revenue. Question-to-column notes stay in `procedure/coverage.md`, `installed/coverage.md`, and `finance/coverage.md`.

| | |
| --- | ---: |
| Datasets | 65 |
| Relationships | 168 |
| Logical identities | 65 |

Snowflake database `SURGICAL_ROBOT`, account `surgicalrobot.us-west-1`. Node ids use the `sf:` prefix. Qualified names start with `surgicalrobot.`.

## What the model covers

Procedure volume holds the hospital, the country, and the site of care apart from the system. Procedure categories include general surgery, gynecology, urology, bariatric, cardiac, and biopsy. Volume, U.S. versus international growth, the remaining procedure opportunity, bariatric drag, late-2025 timing, and surgery-center mix are separate facts. Instrument growth versus procedure growth, and the cardiac gap the newer platforms address, sit on this side. Coverage policy records Medicaid and exchange effects. This is case volume a device maker uses.

The installed system base holds da Vinci 5, Xi, refurbished Xi, single-port, and the lower-priced form factor as generations. An installed system is the current placement, including a retained Xi after a da Vinci 5 purchase. Placements, utilization, after-hours use, generation mix, and redeployed systems are separate facts. Features cover force feedback, advanced imaging, augmented dexterity, biopsy, the digital hub, cloud accounts, and the digital subscription. Clearances, instruments still required, distributors, the China joint venture, refurbished offers, tiered pricing, and capital-budget conversations are on this slice.

Margin, tariffs, and innovation revenue hold gross margin, the bridge, da Vinci 5 contribution margin versus Xi, the tariff headwind, and revenue from new products compared with procedure growth. Surgery-center economics keep capital cost, Medicare and commercial rates, instrument cost, and sterilization apart. Facility margin records how much of the new-plant uplift is sustainable. Payment rates are the device maker's view of those procedure economics.

A graph build of this directory reports 65 datasets, 168 relationships, no unknown claims, and no contradictory edges.
