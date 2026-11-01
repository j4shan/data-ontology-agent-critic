# Problem Report: Ubiquitous Partitioning Keys (`tenant_id` / `company_id`) Induce Complete-Graph Cliques in Derived Relationships

## 1. Summary

In multi-tenant SaaS, ERP, and regulated enterprise databases, a boundary identifier such as `tenant_id`, `company_id`, `org_id`, or `legal_entity_id` is physically present on nearly every operational and analytical dataset to enforce data isolation, row-level security, or legal entity boundaries. For example, in ERPNext (`frappe/erpnext`), `company` (`Link -> Company`) appears on over 300 DocTypes spanning accounting, inventory, manufacturing, selling, buying, and HR.

Under the current `data-ontology-graph` relationship derivation model (`product/graph-model.md` §3.1, implemented in `src/data_ontology_graph/model/derivation.py`), **every pair of entity definitions that realize the same logical entity produces a `JoinRelationship`**. When $N$ datasets realize `tenant_identity` (1 master `tenant` dataset with `unique: true` and $N - 1$ member datasets with `unique: false`), the graph builder does **not** produce an $(N - 1)$-edge star topology centered on `tenant`. Instead, it produces a **complete clique $K_N$ of $\binom{N}{2} = \frac{N(N - 1)}{2}$ relationships**:
- $N - 1$ hub-to-spoke relationships (`1:many` / `many:1`) between `tenant` and each tenant-scoped dataset, plus
- $\binom{N - 1}{2}$ spoke-to-spoke relationships (`many:many`, `match_existence: unknown`) directly connecting every tenant-scoped dataset to every other tenant-scoped dataset.

In a 1,000-dataset enterprise catalog where 800 datasets carry `tenant_id`, this single logical entity generates **319,600 derived relationships** and places all 800 datasets at **hop distance 1** from one another—degrading `expand_subgraph`, `find_paths`, and `find_connecting_subgraph`.

Per Critic's independence and realism principles, **benchmark catalogs must not omit or distort real-world `tenant_id` / `company_id` columns to work around actor graph mechanics**. Instead, this report documents the failure modes in `data-ontology-graph` so the actor can evolve to handle ubiquitous scope keys natively.

---

## 2. Root Cause in the Actor Implementation

### 2.1 Pairwise Clique Generation (`src/data_ontology_graph/model/derivation.py`)

`derive_relationships` groups all entity definitions by `identity_id` and emits a `JoinRelationship` for every 2-combination:

```python
for identity_id in sorted(by_identity):
    members = sorted(by_identity[identity_id], key=lambda item: item[1].key(item[0]))
    for (node_a, definition_a), (node_b, definition_b) in combinations(members, 2):
        endpoint_a = _endpoint(node_a, definition_a)
        endpoint_b = _endpoint(node_b, definition_b)
        relationships.append(...)
```

Because `combinations(members, 2)` does not distinguish between:
1. A **primary/unique realization** (`unique: true`) joined to a **foreign realization** (`unique: false`), and
2. Two **non-unique foreign realizations** (`unique: false` on both sides) of a high-fan-out partitioning key,

any two unrelated tables (e.g., `salary_slip` in HR and `stock_bin` in WMS) receive a direct 1-hop `many:many` relationship solely because both tables have a `tenant_id` column.

### 2.2 Alphabetical Truncation in `expand_subgraph` (`src/data_ontology_graph/query/neighbourhood.py`)

In `expand()`, the breadth-first frontier marks every neighbour across **all** outgoing edges at `distance = level + 1` *before* `max_nodes` and per-group `limit` are applied:

```python
for level in range(depth):
    following = []
    for node_id in frontier:
        for edge in edges.get(node_id, ()):
            target = edge.target.node_id
            if allowed(edge) and target not in distance:
                distance[target] = level + 1
                following.append(target)
    frontier = following

ordered = sorted(distance.items(), key=lambda item: (item[1], item[0]))
selected = ordered if max_nodes is None else ordered[:max_nodes]
```

And only **after** `selected` is sliced to `[:max_nodes]` does `expand()` filter the seed dataset's `EdgeGroup`s to targets in `kept = {node_id for node_id, _ in selected}`:

```python
groups[node_id] = group_edges(
    (edge for edge in edges.get(node_id, ()) if allowed(edge)),
    limit=limit, listed=lambda edge: edge.target.node_id in kept,
)
```

**Consequence:**
When a seed dataset has `tenant_id`, **every other tenant-scoped dataset in the catalog has `distance = 1`**. Sorting by `(distance, node_id)` orders all distance-1 datasets alphabetically by `node_id`, and `ordered[:max_nodes]` keeps only the first `max_nodes` alphabetically. If a true `many:1` foreign-key target (such as `m_employee` from `z_salary_slip`) sorts alphabetically after `max_nodes` unrelated tables (`a_tenant`, `b_distractor_01`, ...), **`m_employee` is excluded from `kept` and its entire `employee_identity` edge group disappears from the response**.

### 2.3 Shortcut Pollution in `find_paths` (`src/data_ontology_graph/query/paths.py`)

- **Default call (`allowed_multiplicities=None`):**
  Every `many:many` edge on `tenant_identity` has traversal cost `1`. Consequently:
  - Path 1 between `z_salary_slip` and `z_stock_bin` is the 1-hop `many:many` edge `z_salary_slip[tenant_id] -> z_stock_bin[tenant_id]`.
  - Paths 2 through $k$ are 2-hop hybrids that take one real edge and one `tenant_id` edge (e.g., `z_salary_slip[tenant_id] -> m_department[tenant_id] -> z_stock_bin[warehouse_id]`).
  - The actual 3-hop domain path (`z_salary_slip -> m_employee -> m_department -> z_stock_bin`) is pushed behind $O(N)$ spurious 1-hop and 2-hop `tenant_id` paths.
- **With `allowed_multiplicities=["1:1", "many:1", "1:many"]`:**
  `PathGraph` splits each entity definition into `ready` (`2 * d`) and `arrived` (`2 * d + 1`) states and requires a `0`-cost pivot to a *different* entity definition on the same dataset (`other != definition` at `paths.py:169`) between consecutive relationship traversals. This prevents traversing `z_salary_slip[tenant_id] -(many:1)-> a_tenant[tenant_id] -(1:many)-> z_stock_bin[tenant_id]` via the `same` definition on `a_tenant`.
  **However**, if the `a_tenant` (or `Company`) master table has **any second entity definition** (for example, `country_identity` on `tenant.country_id` or `currency_identity` on `tenant.default_currency_id`), `PathGraph` can pivot `a_tenant[tenant_id] -> a_tenant[country_id]` at cost `0` and jump in 2 hops to any table with `country_id` or `currency_id`.

### 2.4 Steiner-Tree Collapse in `find_connecting_subgraph` (`src/data_ontology_graph/query/connecting.py`)

`connecting_tree()` runs unweighted multi-source BFS over `self.index.adjacency` with no multiplicity filter and no hub-degree weighting:

```python
for current in frontier:
    for edge in adjacency.get(current, ()):
        other = edge.opposite(current).node_id
```

When all terminal datasets share `tenant_identity`, `connecting_tree()` immediately finds a cost-1 boundary edge between every pair of terminals on `tenant_id` at `level = 0` and returns only the terminal datasets linked by `tenant_identity` (`many:many`), omitting all intermediate domain bridge datasets.

---

## 3. Empirical Reproduction

Running the same 20-dataset mini-enterprise graph (`z_salary_slip -> m_employee -> m_department -> z_stock_bin`, plus `a_tenant` and 14 alphabetically-earlier tables `b_distractor_01..14`) through `GraphReadService` with and without a ubiquitous `tenant_id` produces the following verified output:

### 3.1 Without Ubiquitous `tenant_id` (20 nodes, 110 edges)

- **`expand_subgraph(seed="z_salary_slip", max_depth=1, max_nodes=6)`:**
  - Returned datasets: `['z_salary_slip', 'm_employee']` (`truncated=False`)
- **`find_paths("z_salary_slip" -> "z_stock_bin", limit=3, max_edges=5)`:**
  - Path 1 (3 hops): `z_salary_slip[employee_id] -(many:1)-> m_employee[employee_id]`, `m_employee[dept_id] -(many:1)-> m_department[dept_id]`, `m_department[warehouse_id] -(1:many)-> z_stock_bin[warehouse_id]`
- **`find_connecting_subgraph(["z_salary_slip", "z_stock_bin"])`:**
  - Returned datasets: `['m_department', 'm_employee', 'z_salary_slip', 'z_stock_bin']` connected through `employee_identity`, `department_identity`, and `warehouse_identity`.

### 3.2 With Ubiquitous `tenant_id` (20 nodes, 195 edges)

- **`expand_subgraph(seed="z_salary_slip", max_depth=1, max_nodes=6)`:**
  - Returned datasets: `['z_salary_slip', 'a_tenant', 'b_distractor_01', 'b_distractor_02', 'b_distractor_03', 'b_distractor_04']` (`truncated=True`)
  - **`m_employee` is completely missing from the returned subgraph**, and `z_salary_slip`'s `employee_identity` edge group is omitted because `m_employee` fell outside the alphabetical `max_nodes=6` slice.
- **`find_paths("z_salary_slip" -> "z_stock_bin", limit=3, max_edges=5)` (default multiplicities):**
  - Path 1 (1 hop): `z_salary_slip[tenant_id] -(many:many)-> z_stock_bin[tenant_id]`
  - Path 2 (2 hops): `z_salary_slip[tenant_id] -(many:many)-> m_department[tenant_id]`, `m_department[warehouse_id] -(1:many)-> z_stock_bin[warehouse_id]`
  - Path 3 (2 hops): `z_salary_slip[employee_id] -(many:1)-> m_employee[employee_id]`, `m_employee[tenant_id] -(many:many)-> z_stock_bin[tenant_id]`
  - **The true 3-hop path is evicted from the top-3 results.**
- **`find_connecting_subgraph(["z_salary_slip", "z_stock_bin"])`:**
  - Returned datasets: `['z_salary_slip', 'z_stock_bin']` linked only by `z_salary_slip[tenant_id] -> z_stock_bin[tenant_id]` (`many:many`).
  - **Both intermediate domain tables (`m_employee`, `m_department`) are dropped.**

---

## 4. Scale Impact on 1,000-Dataset Enterprise Catalogs

For an enterprise catalog with $N = 1,000$ datasets where a boundary/reference key appears on $k$ datasets:

| Ubiquitous Logical Entity | Typical Realizations ($k$) | Derived Clique Edges $\binom{k}{2}$ | Spoke-to-Spoke `many:many` Edges $\binom{k-1}{2}$ |
| --- | ---: | ---: | ---: |
| `tenant_identity` / `company_identity` | 800 | 319,600 | 318,801 |
| `currency_identity` | 300 | 44,850 | 44,551 |
| `status_type_identity` / `uom_identity` | 200 | 19,900 | 19,701 |
| `date_key_identity` | 150 | 11,175 | 11,026 |

Over **99.5%** of the edges generated for these identities are spoke-to-spoke `many:many` relationships between two non-unique foreign keys (`unique: false` on both endpoints).

---

## 5. Candidate Directions for the Actor (`data-ontology-graph`)

Without changing Critic's faithfully modeled enterprise schemas, the actor can address this at one or more layers:

1. **Per-Group Fair Sampling in `expand_subgraph` (`neighbourhood.py`):**
   Instead of flattening all outgoing edges into a single distance-1 set and slicing alphabetically by `node_id`, allocate the `max_nodes` budget across distinct `EdgeGroup`s (or prioritize `many:1` / `1:1` / low-fan-out `identity_id` groups before high-fan-out `many:many` groups) so that a high-degree `tenant_identity` group never starves `employee_identity` or other selective keys on the seed dataset.
2. **Multiplicity / Information-Content Cost in `find_connecting_subgraph` and `find_paths`:**
   - Weight edges by inverse identity frequency (e.g., $w(e) = 1 + \log_2 k_{\text{identity}}$) or penalize `many:many` (`unique: false` $\leftrightarrow$ `unique: false`) edges relative to unique-endpoint joins (`1:1`, `many:1`, `1:many`), so Steiner trees and $k$-shortest paths prefer specific domain relationships over ubiquitous partitioning keys.
   - Support an `allowed_multiplicities` or `exclude_identities` parameter on `find_connecting_subgraph` and `expand_subgraph`, matching `find_paths`.
3. **Composite-Scoping Representation (When Semantically Appropriate):**
   In multi-tenant schemas where entity keys are only unique *within* a tenant (`(tenant_id, employee_id)`), `tenant_id` participates as a component of composite `dataset_columns` rather than (or in addition to) a standalone join key, whereas standalone `tenant_id` represents a partitioning scope rather than a domain join path between two child facts.
