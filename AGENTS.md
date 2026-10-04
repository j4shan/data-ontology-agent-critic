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
- Suites and gold AKGs are also organized per domain.
- Current domains are `healthcare-payer`, `telecom-mobile`, `manufacturing-discrete`,
  `retail-grocery`, and `commerce-marketplace`.
- Do not reintroduce `financial`, `student_club`, `superhero`, or `toxicology` assessment
  assets. `financial` and `student_club` are too small for ontology assessment.
