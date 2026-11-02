# Agent instructions

## Cloud sessions

While working in a cloud session, keep rolling commits into one feature branch unless the user requests a new feature branch.

## Independence from the actor

Critic evaluates an actor project, initially `../data-ontology-graph`. Do not import actor code,
copy actor internals into Critic, or reference actor graph identifiers (`node_id`, `edge_id`) in
suites, gold AKGs, or submissions. Use data-source terms: qualified dataset names and columns.
The actor location, artifact location, and socket path are always configurable inputs.

## Catalog asset isolation

Authored assets that belong to one business domain must not share a file with another domain.

- Test catalogs live under `resources/test_yamls/<domain>/`. Each directory holds that
  domain's `directory-manifest.yaml`, `yaml/` collection, `questions.md`, and `forget-log.yaml`.
- Current domains are `frappe-erp` and `apache-ofbiz`.
- Do not add another assessment domain without explicit direction.
