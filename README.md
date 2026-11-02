# Critic

An independent testing and evaluation framework for knowledge-context solutions that help an AI
agent assemble an abstract knowledge graph (AKG) for an analytical question. Critic supplies test
data, suites, gold AKGs, a submission schema, deterministic scoring, and result collection. The
first actor under evaluation is [`../data-ontology-graph`](../data-ontology-graph/).

The test catalogs are `frappe-erp` and `apache-ofbiz`.

Critic does not host or call a model. Any agent follows Critic's written instructions to publish
an actor artifact, answer suite cases with AKG submissions, and score and collect the results.
Critic also develops agent tools on the Graph Service API. It does not import actor code.

The product requirements are in the [project PRD](project_metadata/product/project-prd.md).

## Layout

```
project_metadata/        PRD and product settings
resources/test_yamls/    schema version 4 test catalogs
  frappe-erp/
  apache-ofbiz/
artifacts/, runs/        published actor artifacts and run output (local only)
```

## Status

Framework code is not yet implemented. The two test catalogs are schema version 4 YAML under
`resources/test_yamls/`.
