# Critic

An independent testing and evaluation framework for knowledge-context solutions that help an AI
agent assemble an abstract knowledge graph (AKG) for an analytical question. The first actor
under evaluation is [`../data-ontology-graph`](../data-ontology-graph/).

Critic does not host or call a model, and it does not import actor code. The product requirements
are in the [project PRD](project_metadata/product/project-prd.md).

## Layout

```
project_metadata/product/                     product requirements and repository settings
project_metadata/earnings_call_candidates/    earnings-call source pool
resources/test_yamls/                         schema version 4 test catalogs
  frappe-erp/
  apache-ofbiz/
skills/akg-assembly/                          skill that assembles an AKG from the graph service
```

## Test catalogs

`frappe-erp` and `apache-ofbiz` are schema version 4 YAML. Each directory has
`directory-manifest.yaml`, `yaml/`, `questions.md`, and `forget-log.yaml`.
