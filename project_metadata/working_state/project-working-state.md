# Project Working State: Critic

This document tracks the current implementation and open decisions relative to the
[project PRD](../product/project-prd.md). It records working state, not product requirements.

Last reconciled with the repository: **2026-09-25**.

## 1. Current repository baseline

The project was initialized with its PRD and migrated test assets. No framework code exists yet.

| Area | Current baseline | Gap against the PRD |
| --- | --- | --- |
| Data sources | The BIRD Mini-Dev SQLite catalogs and description CSVs were moved from the actor repository to [`resources/data/dev_databases/`](../../resources/data/dev_databases/). The SQLite question set and gold SQL were copied to [`resources/data/bird_minidev/`](../../resources/data/bird_minidev/). Both are local only; provenance and hashes are in [SOURCES.md](../../resources/data/SOURCES.md). | No fetch script reproduces the sources on a fresh machine. |
| Reference catalog | The reviewed [financial catalog](../../resources/data/reference_catalogs/financial/catalog.yaml) builds as a finalized YAML directory with the actor's publisher. | Reference catalogs for later suites do not exist. |
| Legacy overlays | Pre-YAML overlay and annotation files for `financial` and `student_club` are kept under [`resources/data/legacy_overlays/`](../../resources/data/legacy_overlays/) as authoring notes. The actor builder does not accept them. | They are input to future reference-catalog authoring only. |
| Suites and gold | The 32 `financial` questions are available as source material. | No suite, test case, or gold AKG has been authored. |
| Submission schema and scorer | None. | C0.1 and C0.3. |
| Instructions and tooling | None. | C0.4 through C0.6. |

## 2. Decisions

**Settled**

1. Critic is a separate sibling repository. It evaluates the actor as an independent project and
   does not import actor code.
2. The actor's source location, artifact location, and socket path are configurable inputs.
3. Critic owns the testing criteria: the AKG submission schema, gold AKGs, scorer, and pass
   criteria.
4. Scoring is at the logical-plan level: datasets, relationships, and attributes. SQL composition,
   execution, and efficiency are out of scope.
5. Critic provides no agent gateway. Any agent follows written instructions.
6. The repository commits agent instructions, launch, scoring, and collection code, and authored
   test definitions. Vendored data sources, published artifacts, and run output are local only.
7. The first suite is `financial` only.
8. Tooling is Python 3.12 with uv, a `critic` command-line entry point, and pytest.
9. Submissions and gold reference data-source terms, not actor identifiers.

**Open**

1. Canonical reference form for a dataset and column. The actor uses `financial.main.account`,
   while BIRD SQL uses `account`. Critic needs one normalized form and a declared mapping rule.
2. Whether attributes count toward the initial pass criterion or are reported only.
3. Pass thresholds for each element class.
4. How to quarantine cases whose BIRD gold SQL is wrong or ambiguous.
5. How to represent join direction in a relationship element, or whether scoring treats a
   relationship as an unordered endpoint pair.
6. How the baseline condition presents the schema to the agent: raw DDL, description CSVs, or both.

## 3. TODOs

### Tier 0 — initial release

| ID | TODO | Depends on | Observable completion |
| --- | --- | --- | --- |
| C0.1 | Define the versioned AKG submission JSON Schema with dataset, relationship, and attribute elements in data-source terms. | Open decisions 1 and 5 | Valid and invalid example submissions are checked by tests. |
| C0.2 | Author the `financial` suite: 32 cases with question, evidence, difficulty, provenance, and gold AKG. Derive a draft gold from each gold SQL, then human-review it and add accepted alternatives. | C0.1 | Every case validates, and each gold AKG has a review record. |
| C0.3 | Implement the deterministic scorer: per-class precision, recall, and F1, best-variant matching, and the pass criterion. | C0.1 | Unit tests cover perfect, partial, empty, invalid, and alternative-matching submissions. |
| C0.4 | Implement run configuration and launch: actor location, catalog, artifact store, and socket as inputs; publish through the actor's CLI; store the artifact under a timestamp-independent fingerprint with actor commit and catalog hash. | — | Two publishes of the same catalog and actor commit produce the same fingerprint. |
| C0.5 | Write model-independent agent instructions for publishing, running cases, writing submissions, scoring, and collecting results. | C0.1–C0.4 | An agent following only the instructions completes one `financial` run. |
| C0.6 | Implement result collection and reporting: pass rate, per-class metrics, breakdown by difficulty, failure categories, and run comparison. | C0.3 | A report compares two runs. |
| C0.7 | Define and support the baseline condition without the actor's service. | C0.5, open decision 6 | Baseline and actor runs appear in one comparison report. |
| C0.8 | Add a fetch-and-verify script for vendored sources against the hashes in SOURCES.md. | — | A fresh checkout obtains and verifies the `financial` sources. |
| C0.9 | Score YAML produced by the actor's generation skill (actor skill A) against the reference catalog. Not an initial-release gate. | Actor skill A | Generated `financial` YAML receives per-element scores against the reference catalog. |

### Tier 1 — investigation

| ID | TODO | Depends on | Observable completion |
| --- | --- | --- | --- |
| C1.1 | Investigate trajectory capture through an agent skill plus hooks for step count, tool-call sequence, and token use, and a recording proxy on the actor socket. | C0.5 | A written recommendation and a prototype that records one case's trajectory. |
| C1.2 | Author the `student_club` reference catalog and suite, using the legacy overlays as input. | C0.2 | The second suite scores through the same tooling. |

### Tier 2 — future

| ID | TODO | Depends on |
| --- | --- | --- |
| C2.1 | Large metadata pool suite for scale behavior. | C1.2 |
| C2.2 | Statistics scoring once the actor serves statistics. | Actor statistics |
