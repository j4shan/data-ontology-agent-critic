# Critic

An independent testing and evaluation framework for knowledge-context solutions that help an AI
agent assemble an abstract knowledge graph (AKG) for an analytical question. Critic supplies test
data, suites, gold AKGs, a submission schema, deterministic scoring, and result collection. The
first actor under evaluation is [`../data-ontology-graph`](../data-ontology-graph/).

The assessment domains are `healthcare-payer`, `telecom-mobile`, `manufacturing-discrete`,
`retail-grocery`, and `commerce-marketplace`. `financial` and `student_club` are excluded because
they are too small for ontology assessment.

Critic does not host or call a model. Any agent follows Critic's written instructions to publish
an actor artifact, answer suite cases with AKG submissions, and score and collect the results.

The product requirements are in the [project PRD](project_metadata/product/project-prd.md);
current state and TODOs are in the
[working state](project_metadata/working_state/project-working-state.md).

## Layout

```
project_metadata/        PRD, specs, agent instructions, working state
  schema_candidates/     five domain catalogs and role-based question sheets
resources/schema/        AKG submission schema (planned)
artifacts/, runs/        published actor artifacts and run output (local only)
```

## Status

Framework code is not yet implemented. Role-based question sheets for the five domains are
drafted. See the Tier 0 TODOs in the working state.
