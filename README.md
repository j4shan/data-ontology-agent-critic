# Critic

An independent testing and evaluation framework for knowledge-context solutions that help an AI
agent assemble an abstract knowledge graph (AKG) for a data-query task. Critic supplies test data,
suites, gold AKGs, a submission schema, deterministic scoring, and result collection. The first
actor under evaluation is [`../data-ontology-graph`](../data-ontology-graph/).

Critic does not host or call a model. Any agent follows Critic's written instructions to publish
an actor artifact, answer suite cases with AKG submissions, and score and collect the results.

The product requirements are in the [project PRD](project_metadata/product/project-prd.md);
current state and TODOs are in the
[working state](project_metadata/working_state/project-working-state.md).

## Layout

```
project_metadata/        PRD, specs, agent instructions, working state
resources/data/
  SOURCES.md             provenance and hashes of vendored sources
  dev_databases/         BIRD Mini-Dev SQLite catalogs and descriptions (local only)
  bird_minidev/          BIRD Mini-Dev SQLite questions and gold SQL (local only)
  reference_catalogs/    reviewed YAML catalogs for the actor builder
  legacy_overlays/       pre-YAML authoring notes
resources/schema/        AKG submission schema (planned)
artifacts/, runs/        published actor artifacts and run output (local only)
```

## Status

Initialized with the PRD and migrated test assets. Framework code is not yet implemented; see the
Tier 0 TODOs in the working state.
