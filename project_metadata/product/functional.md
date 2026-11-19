# Critic — Functional Product Requirements

## Actors

<a id="1.1"></a>

**1.1** Evaluators configure and run benchmark experiments, maintain benchmark evidence and
reference answers, and inspect results. Ontology graph service developers use those results to
identify improvements and regressions in the service’s benefit to question-answering agents.
Answering agents discover relevant evidence through their assigned tools and construct an AKG for
each question.

## Capabilities

<a id="2.1"></a>

**2.1** Critic runs controlled experiments comparing incremental discovery through raw YAML search
and reading with incremental discovery through graph API tools backed by the same YAML evidence.
Comparisons use the same questions, answer requirements, and agent configuration unless a factor is
deliberately varied. Experiments support repeated trials and additional cells for comparing service
builds, models, reasoning settings, or tool configurations. The graph-access cell uses the
service's bundled question-answering skill, including its answer validation. The raw-YAML cell uses
Critic-provided guidance for the same answer contract, with instruction-only validation and no
service tools. Cell-specific assembly guidance is identified as part of the experimental conditions.

<a id="2.2"></a>

**2.2** Critic quantitatively assesses AKG quality against independently reviewed reference
selections, expressed as AKGs in the public contract, and measures tokens consumed throughout evidence discovery and answer construction.
Quality assessment compares selected nodes, relationships, and their metadata, recognizing valid
alternatives, essential missing knowledge, irrelevant selections, and unsupported claims. Quality
and token cost remain separately visible when ranking answers and comparing cells. Scoring
definitions and token-accounting methods are recorded with results so comparisons can be interpreted
and reproduced.

<a id="2.3"></a>

**2.3** Critic renders saved benchmark results through a reusable template containing a text summary
and graph visualizations. Reports show experimental conditions, aggregate and per-question
differences in AKG quality and token consumption, variability across trials, and representative
failures and limitations. Repeating an experiment after a service change shows whether the graph’s
marginal benefit has improved, remained unchanged, or regressed.

<a id="2.4"></a>

**2.4** Critic maintains YAML schema metadata, question sheets, and reviewed reference answers
organized by business domain. Benchmark inputs can be authored through any process that produces
YAML conforming to the public metadata contract. Benchmark assets use qualified dataset names and
column references, and each experiment identifies its evidence, reference answers, scoring
definitions, agent configuration, and service under assessment. Saved submissions and measurements
support subsequent reporting and re-scoring.

## Concepts

<a id="3.1"></a>

**3.1** An AKG is a task-specific selection of datasets and relationships from the knowledge in the
YAML evidence, preserving its meaning. Every value in an AKG can be inferred from that YAML, so an
answer built through graph API tools and one built from the YAML alone take the same form. An AKG may
contain multiple disconnected components. Separate candidate interpretations remain separate AKGs.
Critic follows the canonical AKG definition and public contract maintained by `data-ontology-graph`
with its bundled question-answering skill; Critic owns the independent reference selections,
raw-YAML cell guidance, and assessment criteria used to measure agent outputs.

<a id="3.2"></a>

**3.2** A reference answer is a reviewed selection of ontology knowledge sufficient and relevant to
a question, established through independent analysis of the source evidence rather than the
evaluated agent’s answer or graph API responses. A question may have multiple accepted reference
selections or unresolved evidence gaps. Additional analysis resources support reference
construction; evidence support and review establish its authority.

<a id="3.3"></a>

**3.3** The graph service’s marginal benefit is the observed difference between graph-access and
raw-YAML cells in AKG quality and token consumption under comparable conditions. Greater similarity
to a reference, fewer tokens, or a better combination of the two can demonstrate benefit. The
measured benefit includes the effect of the service's bundled skill and answer validation. A smaller
AKG is useful when it remains sufficient; size reduction alone does not establish correctness.

## Exclusions

<a id="4.1"></a>

**4.1** YAML collector performance and output quality are outside Critic’s measurement scope. Critic
evaluates the ontology graph service independently through its public interfaces and does not import
actor implementation code. Benchmark cases, reference selections, and submissions remain independent
of actor-specific graph identifiers.
