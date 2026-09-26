# Agent instructions

## Independence from the actor

Critic evaluates an actor project, initially `../data-ontology-graph`. Do not import actor code,
copy actor internals into Critic, or reference actor graph identifiers (`node_id`, `edge_id`) in
suites, gold AKGs, or submissions. Use data-source terms: qualified dataset names and columns.
The actor location, artifact location, and socket path are always configurable inputs.

## Catalog asset isolation

Authored assets that belong to one BIRD Mini-Dev catalog must not share a file with another
catalog. `<database>` is the directory name under `resources/data/dev_databases/`.

- Reference YAML: `resources/data/reference_catalogs/<database>/`. The directory holds only that
  catalog's `.yaml` files, so it builds as a finalized actor YAML directory.
- Legacy overlay notes: `resources/data/legacy_overlays/<database>/`.
- Suites and gold AKGs are also organized per catalog.
- Never write into the vendored `resources/data/dev_databases/` or `resources/data/bird_minidev/`
  trees.
- Current catalogs are `financial` (first suite) and `student_club` (legacy notes only). Do not
  introduce `superhero` or `toxicology` assets.
