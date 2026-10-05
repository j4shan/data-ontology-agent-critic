# Agent instructions

## Independence from the actor

Critic evaluates an actor project, initially `../data-ontology-graph`. Do not import actor code,
copy actor internals into Critic, or reference actor graph identifiers (`node_id`, `edge_id`) in
suites, gold AKGs, or submissions. Use data-source terms: qualified dataset names and columns.
The actor location, artifact location, and socket path are always configurable inputs.

## Catalog asset isolation

Authored assets that belong to one business domain must not share a file with another domain.

- Schema-candidate catalogs live under `project_metadata/schema_candidates/<domain>/`.
- Each domain's question sheet is `questions.md` in that directory.
- Reference YAML lives under `resources/data/reference_catalogs/<domain>/`. Each directory contains
  only that domain's `.yaml` files and is gold for scoring generated catalogs.
- Generated catalogs live under `resources/data/generated_catalogs/<domain>/`. Each committed
  directory contains only that domain's `directory-manifest.yaml`, `yaml/` collection files,
  `decisions.md`, and `provenance.yaml`. Only the actor's DDL collector publish step writes them.
  No suite, case, or gold AKG is derived from generated output.
- Suites and gold AKGs are also organized per domain.
- Current domains are `healthcare-payer`, `telecom-mobile`, `manufacturing-discrete`,
  `retail-grocery`, and `commerce-marketplace`.
- Do not add another assessment domain without explicit direction.
