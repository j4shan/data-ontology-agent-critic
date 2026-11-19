# Project Working State: Critic

This document tracks the current implementation and open issues relative to the
[functional PRD](../product/functional.md). It records working state, not product requirements;
requirements and design decisions live only under [`product/`](../product/). Work items are
detailed in the execution plan (`project_metadata/plans/critic-execution-plan.md`, local only) and
cited here by its W and D numbers.

Last reconciled with the repository: **2026-10-26**.

## 1. Current repository baseline

No framework code exists. Critic currently holds its PRD, agent instructions, and the retiring
`skills/akg-assembly/` skill.

| Area | Current baseline | Gap against the PRD |
| --- | --- | --- |
| Benchmark inputs | None. The schema-2 domain catalogs, their question sheets and generators, and the schema-3 earnings-call catalogs and source research were deleted on 2026-10-26 as stale. New candidates will be provided. | No YAML evidence or question sheet exists for any domain ([2.4](../product/functional.md#2.4)). |
| Reference answers | None. Reference answers will be supplied as prebuilt AKGs per question. | No reference selection exists ([2.2](../product/functional.md#2.2), [3.2](../product/functional.md#3.2)). |
| Submission contract | Follows the `data-ontology-graph` public AKG contract ([3.1](../product/functional.md#3.1)); AKG format 3 is finalized but not yet merged there (section 2). | Not adopted (W2.1). |
| Raw-YAML cell guidance | None. | The Critic-owned control-cell skill does not exist (W4.4). |
| `skills/akg-assembly/` | Superseded by the graph project's bundled `query-graph-api` skill. Its `graph_call.py` reads the retired `get_hops` tables and no longer works against the service. | To be deleted (D11). |
| Framework | None. | Scaffold, runner, scorer, and reports (W0.2 onward). |
| Documentation | `README.md` and `resources/data/SOURCES.md` predate the deletion of the benchmark inputs and the graph project's redesign. | Refresh with the first new candidates. |

## 2. Graph project dependency

Critic evaluates `data-ontology-graph` through its public interfaces. Its state as of 2026-10-26:

| Item | State |
| --- | --- |
| Branch | `feat/akg-file-mode`, commits `3737412`, `9b91e84`, `bd4b386` plus uncommitted work, not pushed. `origin/main` is still `012d98a` (PR #6). The workspace version is final. |
| YAML input | Intermediary schema 4 only. Entity definitions state `unique`, `total`, and `conforms`; YAML authors no relationships, and the builder derives one for every two definitions of a logical entity, with multiplicity and match existence. |
| Graph API | `graph.get_edges` replaces `get_hops`; `max_edges` replaces `max_hops`. Directed edges are keyless arrays named by one `edge_fields` header, grouped in `edge_groups` by logical entity ID, then entity definition; `limit` applies per entity definition. `find_paths` lists `paths` whose steps carry `identity_id`. Every response uses one dataset record shape. |
| AKG contract | Format 3: `format_version`, `datasets` as a list of response dataset records holding the selected directed edges at `standard` positions, reasoning in `usage` keyed by `edge_id`, gaps naming (`node_id`, `edge_id`), optional `graph.snapshot`. `check` and `resolve` work against the service or a YAML directory. |
| Bundled skill | `query-graph-api`: `graph_call.py METHOD PARAMS --why TEXT` prints responses unchanged and appends each call to a response log; `akg.py` builds the AKG only from logged responses. The skill sets no call budget or limits of its own. |
| Identifiers | `node_id` is authored in the YAML (`<accessor-family>:<catalog>.<object>`, for example `sqlite:lending.account`). `edge_id` is formed from both endpoints' `node_id`, `identity_id`, and columns, in canonical order. |

## 3. Open issues

| # | Issue | Blocks | Next step |
| --- | --- | --- | --- |
| 1 | No benchmark inputs. | W1, W3, every run | Receive the new candidates as schema-4 YAML with question sheets. |
| 2 | AKG format 3 is final but unmerged in the graph project. | W2.1, W4.4, W5 | Build against the workspace version; re-check when it merges to `main`. |
| 3 | Graph identifiers in submissions (D12): AKG format 3 requires `node_id` and `edge_id`, while [4.1](../product/functional.md#4.1) keeps submissions independent of actor-specific identifiers. `node_id` is authored in the YAML and `edge_id` is formed from YAML terms, so neither is service-only. | W2.1, W5.1 | Clarify 4.1 to permit identifiers stated in or formed from the YAML evidence. |
| 4 | Control-cell answers in format 3 (W4.4): an agent working from YAML alone must write directed-edge arrays in `edge_fields` order, a canonical `edge_id`, effective descriptions, and derived multiplicity and match existence. A control answer may fail on form rather than knowledge. | W4.4, W5 | Write the control skill from the bundled skill's check rules; score on normalized keys and report checker findings separately. |
| 5 | Post-run validity check of control answers: the graph project's `check` against a YAML directory can serve as Critic's validator. | W4.5 | Confirm `check` with YAML input on a hand-written format 3 AKG. |
| 6 | Scoring keys (plan §3.3, D1–D3) predate directed edges and the term "logical entity". AKG equivalence is an open issue in the graph project (its C7). | W5.1 | Restate keys on datasets, directed edges (`edge_id` plus start dataset), and logical entity IDs. |
| 7 | Reference tiers (D15): the AKG contract cannot mark required, accepted, forbidden, or must-flag elements. | W2.2, W5.3 | Define the per-question sidecar beside each reference AKG set. |
| 8 | Cost limits and traces: the bundled skill no longer bounds calls, so Critic's run configuration owns caps and timeouts. The test cell's response log is a trace source; the control cell needs its own. | W2.4, W4.6 | Add caps and timeouts to the run configuration; take test-cell traces from the response log. |
| 9 | `skills/akg-assembly/` is broken and superseded. | — | Delete it (D11). |
| 10 | Uncommitted documentation reorganisation on `feat/initial-akg-benchmark`: new `product/functional.md`, removed `project-prd.md`, `repository-requirements.md`, and placeholder directories, plus the catalog deletion. | — | Commit when reviewed. |

## 4. Work items

Status of the execution plan's work streams:

| Stream | Status |
| --- | --- |
| W0 Foundation | Not started; W0.2 scaffold is the first code task. |
| W1 Evidence and inputs | Blocked by issue 1. |
| W2 Contracts | W2.1 blocked by issues 2 and 3; W2.2 by issue 7; W2.3–W2.5 can start. |
| W3 Reference answers | Blocked by issue 1 and the supplied reference AKGs. |
| W4 Runner and cost capture | W4.1–W4.3 can start; W4.4 blocked by issue 4. |
| W5 Scoring | Blocked by issues 3 and 6. |
| W6 Results and experiments | Not started. |
