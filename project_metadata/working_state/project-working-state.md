# Project Working State: Critic

This document tracks the current implementation and open decisions relative to the
[project PRD](../product/project-prd.md). It records working state, not product requirements.

Last reconciled with the repository: **2026-10-04**.

## 1. Current repository baseline

The project was initialized with its PRD and migrated test assets. No framework code exists yet.

| Area | Current baseline | Gap against the PRD |
| --- | --- | --- |
| Data sources | The five schema-candidate catalogs under [`schema_candidates/`](../schema_candidates/) are the assessment corpora. `financial` and `student_club` were removed because they are too small for ontology assessment. | The catalogs are schema version 2 and have no `directory-manifest.yaml`, so the current actor builder will not load them. |
| Question sheets | Each domain has a role-based analytical question sheet: `healthcare-payer` (125), `telecom-mobile` (141), `manufacturing-discrete` (115), `retail-grocery` (138), and `commerce-marketplace` (127). Each sheet stays at or under 150 questions. | The sheets are not yet cases. They have no gold AKG. |
| Reference catalog | None. The removed `financial` reference catalog is not a benchmark target. | A schema version 3 reference catalog still has to be published for each domain. |
| Suites and gold | Question text is drafted by role. | No suite, test case, or gold AKG has been authored. |
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
7. The benchmark domains are the five schema-candidate catalogs. `financial` and `student_club` are excluded.
8. Tooling is Python 3.12 with uv, a `critic` command-line entry point, and pytest.
9. Submissions and gold reference data-source terms, not actor identifiers.

**Open**

1. Canonical reference form for a dataset and column. Qualified names such as
   `healthcare-payer.claim.fact_claim_header` need one normalized form in submissions.
2. Whether attributes count toward the initial pass criterion or are reported only.
3. Pass thresholds for each element class.
4. How to retire a question whose gold path stays ambiguous after review.
5. How to represent join direction in a relationship element, or whether scoring treats a
   relationship as an unordered endpoint pair.
6. How the baseline condition presents the schema to the agent: raw DDL, description CSVs, or both.

## 3. TODOs

### Tier 0 — initial release

| ID | TODO | Depends on | Observable completion |
| --- | --- | --- | --- |
| C0.1 | Define the versioned AKG submission JSON Schema with dataset, relationship, and attribute elements in data-source terms. | Open decisions 1 and 5 | Valid and invalid example submissions are checked by tests. |
| C0.2 | Author one suite per schema-candidate domain from its `questions.md`: role, analytic task, question, and a human-reviewed gold AKG, including accepted alternatives. | C0.1 | Every case validates, and each gold AKG has a review record. |
| C0.3 | Implement the deterministic scorer: per-class precision, recall, and F1, best-variant matching, and the pass criterion. | C0.1 | Unit tests cover perfect, partial, empty, invalid, and alternative-matching submissions. |
| C0.4 | Implement run configuration and launch: actor location, catalog, artifact store, and socket as inputs; publish through the actor's CLI; store the artifact under a timestamp-independent fingerprint with actor commit and catalog hash. | — | Two publishes of the same catalog and actor commit produce the same fingerprint. |
| C0.5 | Write model-independent agent instructions for publishing, running cases, writing submissions, scoring, and collecting results. | C0.1–C0.4 | An agent following only the instructions completes one domain run. |
| C0.6 | Implement result collection and reporting: pass rate, per-class metrics, breakdown by difficulty, failure categories, and run comparison. | C0.3 | A report compares two runs. |
| C0.7 | Define and support the baseline condition without the actor's service. | C0.5, open decision 6 | Baseline and actor runs appear in one comparison report. |
| C0.8 | Withdrawn. BIRD Mini-Dev sources are not part of the benchmark. | — | No `financial` or `student_club` assets remain in the repository. |
| C0.9 | Score YAML produced by the actor's generation skill (actor skill A) against a domain reference catalog. Not an initial-release gate. | Actor skill A | Generated YAML for one schema-candidate domain receives per-element scores against its reference catalog. |

### Tier 1 — investigation

| ID | TODO | Depends on | Observable completion |
| --- | --- | --- | --- |
| C1.1 | Investigate trajectory capture through an agent skill plus hooks for step count, tool-call sequence, and token use, and a recording proxy on the actor socket. | C0.5 | A written recommendation and a prototype that records one case's trajectory. |
| C1.2 | Withdrawn. `student_club` is not an assessment domain. | — | No `student_club` suite is authored. |

### Tier 2 — future

| ID | TODO | Depends on |
| --- | --- | --- |
| C2.1 | Large metadata pool suite for scale behavior, using the five schema-candidate catalogs. | C0.2 |
| C2.2 | Statistics scoring once the actor serves statistics. | Actor statistics |
