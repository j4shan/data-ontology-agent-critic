# Project Working State: Critic

This document tracks the current implementation and open decisions relative to the
[project PRD](../product/project-prd.md). It records working state, not product requirements.

Last reconciled with the repository: **2026-10-04**.

## 1. Current repository baseline

The project was initialized with its PRD and five authored catalog candidates. No framework code
exists yet.

| Area | Current baseline | Gap against the PRD |
| --- | --- | --- |
| Catalog candidates | The five schema-candidate catalogs under [`schema_candidates/`](../schema_candidates/) are the assessment corpora. | The catalogs are schema version 2 and have no `directory-manifest.yaml`, so the current actor builder will not load them. |
| Question sheets | Each domain has a role-based analytical question sheet: `healthcare-payer` (125), `telecom-mobile` (141), `manufacturing-discrete` (115), `retail-grocery` (138), and `commerce-marketplace` (127). Each sheet stays at or under 150 questions. | The sheets are not yet cases. They have no gold AKG. |
| Reference catalogs | None have been published under `resources/data/reference_catalogs/`. | A schema version 3 reference catalog still has to be published for each domain. |
| Generated catalogs | The actor's DDL collector can publish reviewed output to `resources/data/generated_catalogs/<domain>/`, with a directory manifest, collection YAML, decision log, and provenance. | No generated catalog has been published. |
| Suites and gold | Question text is drafted by role. | No suite, test case, or gold AKG has been authored. |
| Submission schema and scorer | None. | C0.1 and C0.3. |
| Instructions and tooling | Critic is the factory for agent tools built on the Graph Service API; it does not import actor code. | C0.4 through C0.6 and C0.11. |

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
7. The benchmark domains are `healthcare-payer`, `telecom-mobile`, `manufacturing-discrete`,
   `retail-grocery`, and `commerce-marketplace`.
8. Tooling is Python 3.12 with uv, a `critic` command-line entry point, and pytest.
9. Submissions and gold reference data-source terms, not actor identifiers.
10. Generated catalogs are committed actor output and benchmark inputs. Only the collector's publish
    step writes them. No suite, case, or gold AKG is derived from them; per-catalog isolation also
    applies to `generated_catalogs/<domain>/`.
11. Human-reviewed reference catalogs are gold for scoring generated catalogs. Critic hosts
    development of agent tools on the Graph Service API.

**Open**

1. Canonical reference form for a dataset and column. Qualified names such as
   `healthcare-payer.claim.fact_claim_header` need one normalized form in submissions.
2. Whether attributes count toward the initial pass criterion or are reported only.
3. Pass thresholds for each element class.
4. How to retire a question whose gold path stays ambiguous after review.
5. How to represent join direction in a relationship element, or whether scoring treats a
   relationship as an unordered endpoint pair.
6. How the baseline condition presents source metadata to the agent: catalog YAML, business model,
   or both.

## 3. TODOs

### Tier 0 — initial release

| ID | TODO | Depends on | Observable completion |
| --- | --- | --- | --- |
| C0.1 | Define the versioned AKG submission JSON Schema with dataset, relationship, and attribute elements in data-source terms. | Open decisions 1 and 5 | Valid and invalid example submissions are checked by tests. |
| C0.2 | Author one suite per schema-candidate domain from its `questions.md`: role, analytic task, question, and a human-reviewed gold AKG, including accepted alternatives. | C0.1 | Every case validates, and each gold AKG has a review record. |
| C0.3 | Implement the deterministic scorer: per-class precision, recall, and F1, best-variant matching, and the pass criterion. | C0.1 | Unit tests cover perfect, partial, empty, invalid, and alternative-matching submissions. |
| C0.4 | Implement run configuration and launch: actor location, catalog, artifact store, and socket as inputs; publish through the actor's CLI from `generated_catalogs/<domain>/`; record that catalog's provenance and store the artifact under a timestamp-independent fingerprint with actor commit and catalog hash. | Owner-reviewed generated catalog | Two publishes of the same generated catalog and actor commit produce the same fingerprint, and the run records catalog provenance. |
| C0.5 | Write model-independent agent instructions for publishing, running cases, writing submissions, scoring, and collecting results. | C0.1–C0.4 | An agent following only the instructions completes one domain run. |
| C0.6 | Implement result collection and reporting: pass rate, per-class metrics, breakdown by difficulty, failure categories, and run comparison. | C0.3 | A report compares two runs. |
| C0.7 | Define and support the baseline condition without the actor's service. | C0.5, open decision 6 | Baseline and actor runs appear in one comparison report. |
| C0.8 | Validate and document reproducible regeneration of the five authored catalog candidates. | — | A fresh checkout regenerates the candidate YAML without a diff and validates every catalog. |
| C0.9 | Score the actor's DDL collector output in `generated_catalogs/<domain>/` against the human-reviewed catalog in `reference_catalogs/<domain>/`. Not an initial-release gate. | Owner-reviewed generated catalog, C0.10 | A generated current catalog receives per-element scores against its reference catalog. |
| C0.10 | Establish a human-reviewed reference catalog for each current domain under the actor's current schema version. | C0.2 | The actor's current builder accepts every current reference catalog. |
| C0.11 | Host development of agent tools built on the Graph Service API (formerly actor skill B). | Graph Service API | Critic contains an agent tool that uses the Graph Service API without importing actor code. |

### Tier 1 — investigation

| ID | TODO | Depends on | Observable completion |
| --- | --- | --- | --- |
| C1.1 | Investigate trajectory capture through an agent skill plus hooks for step count, tool-call sequence, and token use, and a recording proxy on the actor socket. | C0.5 | A written recommendation and a prototype that records one case's trajectory. |

### Tier 2 — future

| ID | TODO | Depends on |
| --- | --- | --- |
| C2.1 | Large metadata pool suite for scale behavior, using the five schema-candidate catalogs. | C0.2 |
| C2.2 | Statistics scoring once the actor serves statistics. | Actor statistics |
