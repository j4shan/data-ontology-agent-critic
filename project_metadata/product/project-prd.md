# Project PRD: Critic — Rule-Based Graph Service Evaluation

Critic is a rule-based evaluation framework for the open-source
[Data Ontology Graph](https://github.com/j4shan/data-ontology-graph) project. It uses curated test
assets, versioned schemas, and deterministic scoring code to evaluate an existing Graph Service
API. The name **Critic** describes the project's evaluation role; it does not refer to training or
running a machine-learning critic model.

| Field | Value |
| --- | --- |
| Status | Draft for product review |
| Product | Critic |
| Primary user | An AI agent or human evaluator running a Graph Service benchmark |
| Assessment target | Data Ontology Graph Service API |
| Initial catalog set | Five schema-candidate domains: `healthcare-payer`, `telecom-mobile`, `manufacturing-discrete`, `retail-grocery`, `commerce-marketplace` |

## 1. Product Goal

Critic provides a suite of test cases for benchmarking the response accuracy and service
performance of the Data Ontology Graph API.

The framework supplies the common assets and rules needed to make benchmark sessions repeatable
and comparable. It defines what enters a test, what counts as a correct answer, which service and
agent metadata identifies a run, and which results must be retained. Detailed operator procedures
belong in separate runbooks rather than this product requirements document.

## 2. Evaluation Boundary

The actor includes both the Graph Service and its preparation toolkit. Its DDL collector reads
configured source catalogs, verifies recorded hashes when applicable, and drafts YAML for
schema-owner review. Critic uses the reviewed, actor-generated catalogs as benchmark inputs,
publishes graph artifacts
through the actor's CLI, and evaluates the running Graph Service through its documented API. Critic
is also the factory for agent tools built on that API. The service and any configured AI agent
gateway remain external integrations; Critic does not import actor code, host an AI model, or
prescribe the actor's internal implementation.

| Participant | Responsibility |
| --- | --- |
| Actor preparation toolkit | The DDL collector verifies recorded source hashes when applicable, drafts catalog YAML, and publishes owner-reviewed catalogs with decisions and provenance. |
| Graph Service | The API under assessment. Its endpoint and API version are configurable inputs. |
| AI agent gateway | Runs the selected agent or model and returns its answer and available instrumentation. |
| Evaluating agent | Interprets a test prompt, interacts with the Graph Service, and returns a task-specific abstract knowledge graph (AKG). |
| Critic | Supplies test assets and agent tools, launches artifact publication through the actor's CLI, validates responses, scores answers, and persists results. |

Gold answers and agent responses use data-source terms—qualified dataset names and column names—
rather than actor-specific identifiers such as `node_id` or `edge_id`. This keeps the benchmark
independent of the service's internal representation and allows the same cases to remain useful
across API versions.

Evaluation covers two distinct concerns:

- **Response accuracy:** whether the agent returns the entities and relationships needed for the
  query task after interacting with the Graph Service.
- **Service performance:** the runtime and available instrumentation associated with that
  interaction, including tool-call trajectory and token consumption when requested by the case.

Artifact publication and catalog scoring are part of Critic's benchmark workflow. Graph Service
evaluation targets a configured service interface and records the API version that was tested.

## 3. Testing Assets

Critic maintains a curated package of metadata sources spanning five business domains:
`healthcare-payer`, `telecom-mobile`, `manufacturing-discrete`, `retail-grocery`, and
`commerce-marketplace`. Each domain keeps its catalog, question sheet, cases, and gold answers
apart from the others under [`project_metadata/schema_candidates/`](../schema_candidates/).

The actor's DDL collector publishes each owner-reviewed catalog to
`resources/data/generated_catalogs/<domain>/`. These committed actor outputs are benchmark inputs.
Each catalog has a `directory-manifest.yaml`, collection files under `yaml/`, a `decisions.md` log,
and a `provenance.yaml` record of source file hashes, generating actor version and commit, review
rounds and decision counts, identity, node, and edge counts, and unknown claims. Human-reviewed
`reference_catalogs/<domain>/` are separate gold for scoring the generated catalogs. No generated
or reference catalog has been published under `resources/data/` yet.

| ID | Requirement |
| --- | --- |
| 3.1 | Each business domain must keep its source metadata, generated and reference catalogs, cases, gold answers, and supporting manifests isolated from the other domains. |
| 3.2 | A test suite must be a versioned collection of cases associated with one source catalog and domain. |
| 3.3 | Each case must be expressed as a prompt template that supplies the query context, required response format, and any optional instrumentation requirements. |
| 3.4 | Optional instrumentation requirements may request standards-based telemetry such as [OpenTelemetry](https://opentelemetry.io/). |
| 3.5 | Each case must have a human-reviewed gold answer containing an AKG and an entity-name list derived from source evidence rather than Graph Service output. |
| 3.6 | A gold answer must support multiple accepted variants when the source permits more than one valid logical plan, such as a direct relationship or a path through a bridge dataset. |
| 3.7 | The AKG portion of a gold answer must identify the required datasets, the relationships connecting dataset-column-set endpoints, and the attributes needed for filtering, grouping, aggregation, or output. |
| 3.8 | Critic must provide a machine-readable schema for a simple declarative YAML test configuration. At minimum, the configuration identifies the agent or model, test suite, and Graph Service API version. |
| 3.9 | Generated catalogs are committed actor output and benchmark inputs kept separate from human-reviewed reference catalogs and gold. No suite, case, or gold AKG may be derived from a generated catalog; suites, gold, and submissions must use data-source terms rather than actor-internal graph identifiers. |

Statistics are excluded from the initial gold AKG until the Graph Service exposes statistics as part
of its supported evidence contract.

## 4. Evaluation Framework

The evaluation framework is code that combines a validated YAML test configuration with the
selected test assets, Graph Service endpoint, and AI agent gateway. It supports both a single
request and a batch of independent requests without changing the meaning of a case.

| ID | Requirement |
| --- | --- |
| 4.1 | Graph Service and AI agent gateway locations must be configurable; changing either integration must not require changes to test cases or scoring rules. |
| 4.2 | The framework must support single-case submission and batch submission. |
| 4.3 | Batch execution must use asynchronous orchestration, with each configured case represented as an independent task within its session. |
| 4.4 | AI agent credentials must be retrieved from secure platform storage, such as macOS Keychain, rather than stored in test YAML, source files, or session output. |
| 4.5 | The framework must extract the agent's primary AKG answer and any requested instrumentation metadata returned by the gateway or telemetry integration. |
| 4.6 | Extracted instrumentation must accommodate tool-call trajectory, token consumption, and runtime when those measurements are available. |
| 4.7 | A response that fails the versioned answer schema must be recorded as invalid with actionable findings. |

### A. Response Accuracy

Response-accuracy evaluation compares the agent's submitted AKG and entity-name list with the case's
human-reviewed gold answer. It evaluates the logical knowledge needed for the query, not executable
SQL or the Graph Service's internal identifiers.

| ID | Requirement |
| --- | --- |
| 4.A.1 | Scoring must be deterministic: the same response, gold answer, suite version, and scorer version produce the same result. |
| 4.A.2 | The scorer must report precision, recall, and F1 for each scored AKG element class and for the entity-name list. |
| 4.A.3 | When a case has accepted alternatives, the response must be scored against its best-matching gold variant. |
| 4.A.4 | Each case must have an explicit, versioned pass criterion derived from its accuracy scores. |
| 4.A.5 | Failed cases must carry a category that connects the observed error to an evaluation concern, such as a missed entity, missing relationship, or incorrect relationship. |
| 4.A.6 | The same test assets must support an optional no-service baseline so the effect of Graph Service access can be compared with otherwise equivalent agent responses. |

### B. Service Performance

Service-performance evaluation describes the cost and timing of the agent's interaction with the
Graph Service. It is reported separately from response accuracy so a correct answer is not confused
with a fast or inexpensive one.

| ID | Requirement |
| --- | --- |
| 4.B.1 | The framework must retain end-to-end runtime for every independent task. |
| 4.B.2 | When requested and available, the framework must retain the Graph Service tool-call trajectory, token consumption, and OpenTelemetry metadata associated with the task. |
| 4.B.3 | Performance results must identify the agent or model, suite version, Graph Service API version, and instrumentation availability so comparisons use compatible conditions. |
| 4.B.4 | Missing optional telemetry must be represented explicitly and must not be mistaken for a zero measurement. |
| 4.B.5 | Accuracy and performance measurements must remain separate result dimensions even when they are presented together. |

## 5. Session Management and Persistence

A **session** is one run of a validated YAML test configuration. It is the logical task group under
which the framework runs one or more independent cases against the AI agent gateway and the
configured Graph Service API.

| ID | Requirement |
| --- | --- |
| 5.1 | Every session must record its validated configuration, suite and scorer versions, Graph Service API version, declared agent or model identity, timestamps, and instrumentation availability. |
| 5.2 | Every independent task must retain its case identity, validation findings, primary answer, accuracy scores, performance measurements, and failure category when applicable. |
| 5.3 | Session output must use a structured format suitable for later reporting and visualization without reparsing console logs. |
| 5.4 | Session summaries must aggregate pass rate and accuracy metrics overall and by case difficulty, and must summarize compatible performance measurements. |
| 5.5 | Results must remain comparable across sessions that differ in Graph Service API version, suite version, or agent/model identity. |
| 5.6 | Persistence must support an optional configurable cloud-drive synchronization location while retaining a usable local session record. |
| 5.7 | Credentials and secrets must never appear in persisted session data or synchronized output. |

## 6. Acceptance Criteria

| Area | Observable acceptance condition |
| --- | --- |
| Testing assets | The curated package covers the five schema-candidate domains, preserves per-domain isolation, validates against its schemas, and records source provenance. |
| Configuration | Valid YAML selects an agent/model, suite, and Graph Service API version; invalid configuration produces actionable findings before a session starts. |
| API evaluation | The same case can run as a single request or as part of an asynchronous batch without changing its expected answer contract. |
| Accuracy | Unit tests cover perfect, partial, empty, invalid, and alternative-matching answers with known deterministic scores. |
| Performance | Runtime is retained for each task, requested optional instrumentation is captured when available, and unavailable telemetry is identified explicitly. |
| Persistence | A completed session can be loaded from structured local output for reporting or visualization, with optional cloud-drive synchronization and no stored credentials. |

## 7. Future Scope

| ID | Reserved requirement |
| --- | --- |
| 7.1 | **Statistics scoring:** extend gold answers and scoring to statistics after the Graph Service exposes them through its supported evidence contract. |
| 7.2 | **Additional instrumentation:** add compatible measurements without changing response-accuracy semantics or invalidating sessions that omit optional telemetry. |

## 8. Non-goals

| ID | Exclusion |
| --- | --- |
| 8.1 | Critic is not a learned critic model and does not train, fine-tune, or host one. |
| 8.2 | Critic does not generate Data Ontology Graph YAML catalogs; the actor's DDL collector drafts and publishes them after owner review. Critic scores generated catalogs against human-reviewed reference catalogs. |
| 8.3 | Critic does not implement the actor's graph builder or service; it launches artifact publication through the actor's CLI. |
| 8.4 | Critic does not build, serve, or correct graph knowledge and does not modify the Data Ontology Graph project. |
| 8.5 | Critic does not score SQL composition, SQL execution results, dialect correctness, physical query plans, or query efficiency. |
| 8.6 | Critic does not provide an AI model runtime; it integrates with a configurable external AI agent gateway. |
| 8.7 | This PRD does not prescribe step-by-step benchmark execution. Operational setup and run instructions belong in separate documentation. |
| 8.8 | The repository does not version secrets, large vendored data sources, or raw session output. It versions generated and reference catalogs, schemas, test definitions, gold answers, scoring code, and supporting instructions. |
