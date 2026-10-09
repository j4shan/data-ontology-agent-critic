---
name: akg-assembly
description: Build a task-specific abstract knowledge graph (AKG) for one analytical question by calling the Data Ontology Graph service. Use when a question must be answered as an AKG of datasets, relationships, and attributes from a published graph snapshot.
---

# AKG assembly

Produce one AKG document for one question. Every dataset, column, and relationship in the AKG
must come from a graph-service response in this session. Write the AKG in the format in
[references/akg-format.md](references/akg-format.md).

## 0. Connect

Call the service through `scripts/graph_call.py`. Set the socket once:

```bash
export DOG_SOCKET=<socket path given by the caller>
python3 scripts/graph_call.py snapshot_info
```

Record `version` and `schema_fingerprint` for the AKG `snapshot` field. If the call fails, stop
and report the error; do not answer from memory.

Command form: `python3 scripts/graph_call.py <method> '<params JSON>'`. Output is a compact
projection. Add `--full` only when a field you need is missing from the compact form.

| Method | Params | Use |
| --- | --- | --- |
| `search` | `{"query": str, "kind": [str, ...] (optional), "limit": int}` | Find candidate datasets, columns, identities. Kinds are `identity`, `dataset`, `entity_definition`, and `column`. |
| `get_dataset` | `{"node_id": str}` | Grain, columns, entity definitions of one dataset. |
| `get_identity` | `{"identity_id": str, "entity_universe"?: [str], "limit"?: int}` | Datasets that realize one logical identity; `truncated` reports whether `limit` cut the list. |
| `get_hops` | `{"node_id": str, "limit"?: int}` | Relationships touching one dataset, directed outward; `truncated` reports whether `limit` cut the list. |
| `find_paths` | `{"from_node_id", "to_node_id", "max_hops", "limit"}` | Ranked join paths between two datasets. |
| `get_relationship` | `{"edge_id": str, "from_node_id": str (optional)}` | Canonical endpoints and directions; with `from_node_id`, also directions relative to that endpoint. |
| `expand_subgraph` | `{"seed_node_ids": [..], "max_depth", "max_nodes", "max_edges"}` | Neighborhood listing. Use `max_depth` 1 only. |

## 1. Decompose the question

Before any call, write these lists in your scratch notes:

- **Measures**: quantities or counts the question compares (e.g. refund amount, units sold).
- **Cuts**: populations the answer is grouped by (e.g. store, shift, product version).
- **Filters and conditions**: status values, thresholds, "no X", "never X", "only one X".
- **Time**: the day or period the comparison runs across, and which event it dates.
- **Populations that must stay visible when unmatched**: phrases like "including … never
  shipped", "no receipt", "absent from". Each needs an optional-side relationship.

## 2. Find candidate datasets

1. Search each concept by its singular head noun or business phrase (`refund`, `basket`,
   `production schedule`). Add `kind` when the needed evidence type is known: use `dataset` and
   `column` for measures and filters, and `identity` and `entity_definition` for business keys.
   Use more than one kind in the same request when both are useful.
2. The response has one group per requested kind. Each group has two row tables:
   `subject_rows`, read by position through `subject_row_header`, and `match_rows`, read through
   `match_row_header` (`key`, `match_type`, `match_field`, `matched_term`, `matched_value`). Join
   them by `key`. A subject has one match row for each field value that matched, so compare
   `matched_value` with the query to tell a whole-name match ("Plant") from a word inside a longer
   name ("Bridge Item Plant"), and use `match_field` to tell a name or synonym match from an ID or
   description match. Subjects are ordered by best `match_type` (`exact`, `prefix`, `phrase`,
   `all_words`), then alphabetically; that order is not a relevance ranking.
3. Multi-word queries also match fragments of a dataset's `qualified_name` or `display_name` and of
   an identity's `name`: `phrase` when the words are consecutive and in order (`main.fact_scrap`
   finds `mfg.main.fact_scrap_rate_daily`), `all_words` when they appear in any order. Each query
   word may be the start of a word (`scrap_rate_dai`). All words must be in the same name. Other
   fields, including columns, match a multi-word query only when they start with the phrase.
4. `dataset` hits are candidates. `column` hits point to the dataset that holds a measure or
   filter. `entity_definition` and `identity` hits mean the concept is a key: call `get_identity`
   to list every dataset that realizes it, and take the one whose `entity_universe` is `complete`
   as the population dataset.
5. If a query returns no useful candidates, try in order: a shorter stem (`calibrat`), a synonym
   from the question, then the likely dataset prefix (`fact_`, `dim_`, `bridge_` plus the noun).
6. `limit` applies to each group separately. When a group's `truncated` is true, repeat with a
   larger `limit` (up to 200), or with `kind` set to that group, before concluding a dataset is
   absent.

## 3. Confirm each candidate

Call `get_dataset` on every candidate you intend to keep. Keep a dataset only if one of these
holds:

- its grain is the event or population the measure counts, or
- it holds a column needed as a measure, cut, filter, or time, or
- it is a required intermediate on a selected path (step 4).

Record for each kept dataset: `qualified_name`, grain description, role (`fact`, `dimension`,
`bridge` from tags), and the exact column names you will use. Never cite a column that is not in
the `columns` list of a `get_dataset` response.

## 4. Choose anchors and connect them

1. **Anchor** = the dataset whose grain carries the measure. A question with measures from
   different events has one anchor per event.
2. For each anchor, call `get_hops` once. Direct hops to cut datasets are preferred over paths.
3. For each cut or filter dataset not reached by a direct hop, call
   `find_paths` with `max_hops` 4 and `limit` 50. Never use `max_hops` above 5.
4. Select a path with these rules, in order:
   1. Reject paths with `fan_out_hops` > 0 when walking from an anchor to a cut. A `1:many` hop
      after a `many:1` hop goes through a shared dimension into an unrelated fact (fan trap).
   2. Among fan-out-free paths, take the one whose columns carry the meaning the question asks
      for. Read the column descriptions from `get_dataset`: the store of a sale line is the store
      on the sale it belongs to, not the home store of the cashier who rang it. Prefer the chain
      through the business process the anchor records (header → line → event) over chains
      through an actor attribute (employee, shift, user) unless the question cuts by that actor.
   3. Reject role-playing columns whose description names a different role
      (`store_manager_employee_id` is not "employee who works at the store").
   4. Prefer fewer hops only after rules 1–3.
5. **Two or more anchors** (drill-across): connect each anchor separately to the shared cut
   datasets (product, location, calendar day). Do not chain anchor → dimension → anchor as one path.
   Record the shared cuts as the relationship between the anchors' results.
6. When `find_paths` returns `truncated: true` and no acceptable path is in the list, call
   `get_hops` on the anchor and on the cut and look for a common neighbor before raising the
   limit.

## 5. Record relationship evidence

For every relationship in the AKG, copy from the tool response:

- both endpoints as `qualified_name` plus `dataset_columns`,
- `direction` (multiplicity, match_existence) as traversed from the anchor side,
- `reverse_direction` from the same `find_paths` or `get_hops` hop, or call `get_relationship`
  with the traversal origin as `from_node_id` and copy its relative `direction` and
  `reverse_direction`.

`get_relationship` always retains canonical `endpoint_a`/`endpoint_b` and `a_to_b`/`b_to_a`
evidence. Do not manually invert those fields. Supplying `from_node_id` makes the relative fields
authoritative for the requested traversal and reports `unknown_fields` relative to that direction.

Apply match existence to the question:

- A population that must stay visible when unmatched needs `optional` on that side; state the
  preserved side in the relationship `note`.
- `unknown` multiplicity or match existence is recorded as `unknown` and listed under
  `evidence_gaps`. Never restate it as optional or always.

## 6. Assemble and check

Write the AKG per [references/akg-format.md](references/akg-format.md), then verify every line:

- [ ] Every dataset appears in at least one relationship, or is the sole dataset.
- [ ] Every relationship endpoint pair appeared in a `get_hops`, `find_paths`, or
      `get_relationship` response.
- [ ] Every attribute column appeared in that dataset's `get_dataset` columns.
- [ ] Every measure, cut, filter, and time item from step 1 maps to an attribute.
- [ ] Every unmatched-population phrase from step 1 maps to an `optional` relationship side
      or an `evidence_gaps` entry.
- [ ] No `node_id`, `edge_id`, or SQL appears in the AKG.

## Call budget

Aim for at most 30 service calls per question. Do not call `expand_subgraph` with `max_depth`
above 1; at depth 2 it returns tens of datasets. Do not call `get_hops` on a hub dimension
(calendar day, location, product) unless that dataset is the anchor; their hop lists are large and
mostly unrelated facts.
