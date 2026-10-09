# AKG text format (draft v0.1)

Emit exactly one fenced `yaml` block. Use data-source terms only: `qualified_name` for datasets and
physical column names for columns. Never emit `node_id`, `edge_id`, or SQL.

## Fields

| Field | Required | Content |
| --- | --- | --- |
| `akg_version` | yes | `"0.1"` |
| `question` | yes | The question text, verbatim. |
| `snapshot` | yes | `version` and `schema_fingerprint` from `snapshot_info`. |
| `entities` | yes | Business entity names the answer depends on, one per dataset kept, as the dataset `display_name`. |
| `datasets` | yes | One item per dataset: `name` (qualified name), `role` (`fact`, `dimension`, `bridge`), `grain` (grain description), `why` (one clause). |
| `relationships` | yes | One item per traversed relationship, directed from the anchor side. See below. |
| `attributes` | yes | One item per column used: `dataset`, `column`, `usage`, and optional `note`. |
| `evidence_gaps` | yes | Unknown claims, missing datasets or columns, and ambiguous path choices. Empty list if none. |
| `alternatives` | no | Other acceptable paths considered, each as a list of relationship `from`/`to` pairs plus `reason_not_chosen`. |

`usage` is one of `measure`, `group`, `filter`, `time`, `join_only`, `output`.

### Relationship item

```yaml
- from: {dataset: <qualified_name>, columns: [<col>, ...]}
  to:   {dataset: <qualified_name>, columns: [<col>, ...]}
  identity: <identity_id>
  forward: {multiplicity: <many:1|1:many|1:1|many:many|unknown>, match_existence: <always|optional|unknown>}
  reverse: {multiplicity: ..., match_existence: ...}
  note: <optional: preserved side for unmatched rows, or why this path>
```

`forward` is the `direction` returned when traversing `from` → `to`; `reverse` is the opposite
direction. Copy values verbatim from the tool response.

## Example (illustrative domain)

```yaml
akg_version: "0.1"
question: Which stores refund a larger share of sales value than other stores in the same region?
snapshot: {version: "5.0", schema_fingerprint: "0000000000000000"}
entities: [Refund, Sale Line, Sale, Store, Region]
datasets:
  - {name: shop.sales.fact_refund, role: fact, grain: One row is one refund., why: refund value measure}
  - {name: shop.sales.fact_sale_line, role: fact, grain: One row is one sale line., why: sales value measure and refund parent}
  - {name: shop.sales.fact_sale, role: fact, grain: One row is one sale., why: carries the selling store}
  - {name: shop.org.dim_store, role: dimension, grain: One row is one store., why: group by store}
  - {name: shop.org.dim_region, role: dimension, grain: One row is one region., why: comparison peer group}
relationships:
  - from: {dataset: shop.sales.fact_refund, columns: [sale_line_id]}
    to: {dataset: shop.sales.fact_sale_line, columns: [sale_line_id]}
    identity: sale_line_identity
    forward: {multiplicity: "many:1", match_existence: always}
    reverse: {multiplicity: "1:many", match_existence: optional}
    note: sale lines without refunds stay visible from the sale-line side
  - from: {dataset: shop.sales.fact_sale_line, columns: [sale_id]}
    to: {dataset: shop.sales.fact_sale, columns: [sale_id]}
    identity: sale_identity
    forward: {multiplicity: "many:1", match_existence: always}
    reverse: {multiplicity: "1:many", match_existence: always}
  - from: {dataset: shop.sales.fact_sale, columns: [store_id]}
    to: {dataset: shop.org.dim_store, columns: [store_id]}
    identity: store_identity
    forward: {multiplicity: "many:1", match_existence: always}
    reverse: {multiplicity: "1:many", match_existence: optional}
  - from: {dataset: shop.org.dim_store, columns: [region_id]}
    to: {dataset: shop.org.dim_region, columns: [region_id]}
    identity: region_identity
    forward: {multiplicity: "many:1", match_existence: always}
    reverse: {multiplicity: "1:many", match_existence: unknown}
attributes:
  - {dataset: shop.sales.fact_refund, column: refund_amount, usage: measure}
  - {dataset: shop.sales.fact_sale_line, column: line_amount, usage: measure}
  - {dataset: shop.org.dim_store, column: store_id, usage: group}
  - {dataset: shop.org.dim_region, column: region_id, usage: group, note: peer group for the comparison}
evidence_gaps:
  - dim_store → dim_region reverse match_existence is unknown; regions with no store are not asserted either way.
alternatives:
  - path: [{from: shop.sales.fact_sale_line, to: shop.org.dim_employee}, {from: shop.org.dim_employee, to: shop.org.dim_store}]
    reason_not_chosen: home store of the cashier, not the selling store.
```
