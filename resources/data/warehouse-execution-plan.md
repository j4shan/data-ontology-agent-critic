# Warehouse execution plan

Resume from the last checkpoint recorded here. Do not rebuild a domain whose status is `committed`.

Baseline already committed on this branch: 17 warehouses. Checkpoint A is `committed`. Thirteen industries remain in Checkpoints B, C, and D.

## How to resume

1. Read this file. The active checkpoint is the first one whose status is not `committed`.
2. For every subtask in that checkpoint, look at `resources/data/<industry>/warehouse/`.
   - No `warehouse/` directory: status stays `pending`. Build it.
   - Directory exists: run `build_snapshot_from_yaml` on `warehouse/yaml` and `detect_contradictions` on the edges. Zero unknown fields and zero contradictory edges, plus a coverage heading for every numbered question, sets the subtask to `validated`. Anything else is `in_progress`. Finish or replace that warehouse before starting another subtask in the checkpoint.
3. When every subtask in the checkpoint is `validated`, update `SOURCES.md`, `coverage.md`, and `summary-report.md`, set the checkpoint and its subtasks to `committed`, commit, and push.
4. Stop. Report the checkpoint. Wait for confirmation before the next checkpoint.
5. Do not start a later checkpoint while an earlier one has a `pending` or `in_progress` subtask.

A checkpoint is durable only after its commit is on `origin/cursor/outstanding-industry-catalogs-4890`. Uncommitted files are not a checkpoint.

## Execution shape

Two subagents, each owning the three industries in its half of the checkpoint. Time limit two hours. They write only those industry directories. They do not commit and they do not edit `SOURCES.md`, `coverage.md`, `summary-report.md`, or this plan. The parent validates, updates those files, and commits.

GPT 6.1 medium effort is not available in this environment. Use `grok-4.7-medium-fast`.

Pattern: `resources/data/technology-hardware/warehouse/`. One imaginary owner. Both companies' question sheets are mapped. Question paraphrases keep real company and product names. No new weblinks. Do not edit `questions.md`. Do not add an assessment domain. Managed care is already done. Semiconductors stays a chip model, separate from Device Inc.

Graph success: zero unknown fields and zero contradictory edges. Do not join one source column to two different columns of the same target node. Dataset floor is 70. Industries with 80 or more questions aim for 90.

## Checkpoint A

Status: `committed`

| Subtask | Agent | Industry | Owner | Slug | Database | Account | Questions | Status |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- |
| A1 | 1 | `rail-transportation/` | Railroad Inc | `railroad` | `RAILROAD` | `railroad.us-central-1` | 94 | `committed` |
| A2 | 1 | `integrated-oil-gas/` | Energy Inc | `energy` | `ENERGY` | `energy.us-central-1` | 87 | `committed` |
| A3 | 1 | `electric-utilities/` | Utility Inc | `utility` | `UTILITY` | `utility.us-east-1` | 82 | `committed` |
| A4 | 2 | `diversified-banks/` | Bank Inc | `bank` | `BANK` | `bank.us-east-1` | 92 | `committed` |
| A5 | 2 | `merchandise-retail/` | Merchandise Inc | `merchandise` | `MERCHANDISE` | `merchandise.us-east-1` | 85 | `committed` |
| A6 | 2 | `interactive-media/` | Social Inc | `social` | `SOCIAL` | `social.us-west-1` | 79 | `committed` |

Companies: CSX and Union Pacific. Chevron and Exxon Mobil. Duke Energy and Southern Company. Bank of America and JPMorgan Chase. Costco and Walmart. Alphabet and Meta Platforms.

## Checkpoint B

Status: `pending`

| Subtask | Agent | Industry | Owner | Slug | Database | Account | Questions | Status |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- |
| B1 | 1 | `aerospace-defense/` | Defense Inc | `defense` | `DEFENSE` | `defense.us-east-1` | 74 | `pending` |
| B2 | 1 | `systems-software/` | Platform Inc | `platform` | `PLATFORM` | `platform.us-west-1` | 69 | `pending` |
| B3 | 1 | `movies-entertainment/` | Studio Inc | `studio` | `STUDIO` | `studio.us-west-1` | 64 | `pending` |
| B4 | 2 | `payments/` | Payments Inc | `payments` | `PAYMENTS` | `payments.us-east-1` | 71 | `pending` |
| B5 | 2 | `investment-banking/` | Broker Inc | `broker` | `BROKER` | `broker.us-east-1` | 68 | `pending` |
| B6 | 2 | `semiconductor-materials-equipment/` | Wafer Tool Inc | `wafertool` | `WAFER_TOOL` | `wafertool.us-west-1` | 62 | `pending` |

Companies: Lockheed Martin and RTX. Microsoft and ServiceNow. Walt Disney and Netflix. Mastercard and Visa. Goldman Sachs and Morgan Stanley. Applied Materials and Lam Research.

## Checkpoint C

Status: `pending`

| Subtask | Agent | Industry | Owner | Slug | Database | Account | Questions | Status |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- |
| C1 | 1 | `semiconductors/` | Chip Inc | `chip` | `CHIP` | `chip.us-west-1` | 59 | `pending` |
| C2 | 1 | `pharmaceuticals/` | Pharma Inc | `pharma` | `PHARMA` | `pharma.us-east-1` | 58 | `pending` |
| C3 | 1 | `integrated-telecom/` | Carrier Inc | `carrier` | `CARRIER` | `carrier.us-east-1` | 56 | `pending` |
| C4 | 2 | `home-improvement-retail/` | Hardware Store Inc | `hardwarestore` | `HARDWARE_STORE` | `hardwarestore.us-east-1` | 54 | `pending` |
| C5 | 2 | `broadline-retail/` | Broadline Inc | `broadline` | `BROADLINE` | `broadline.us-west-1` | 53 | `pending` |
| C6 | 2 | `pc-insurance/` | Insurance Inc | `insurance` | `INSURANCE` | `insurance.us-east-1` | 44 | `pending` |

Companies: Broadcom and Nvidia. Eli Lilly and Merck. AT&T and Verizon. Home Depot and Lowe's. Amazon and eBay. Chubb and Progressive.

Chip Inc is a semiconductor model. It does not extend the Device Inc hardware warehouse.

## Checkpoint D

Status: `pending`

| Subtask | Agent | Industry | Owner | Slug | Database | Account | Questions | Status |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- |
| D1 | 1 | `application-software/` | App Inc | `app` | `APP` | `app.us-west-1` | 43 | `pending` |

Companies: Salesforce and Oracle. One subagent. Same validation and commit rules. Dataset floor stays 70.

## Done when

All four checkpoints are `committed`, `SOURCES.md` shows a warehouse for all 30 industries, and each new graph build has zero unknown fields and zero contradictory edges.
