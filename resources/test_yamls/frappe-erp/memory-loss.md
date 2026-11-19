# Frappe ERP memory loss

This catalog was degraded by the `memory-loss-v1` process: a sample of eligible values was removed
from `yaml/`, and each removed value is listed with its original in `forget-log.yaml`. A forgotten
claim reads `unknown`; a forgotten description, synonym list, tag list, expression, or metadata
entry is absent.

Every forgotten value that shapes a relationship has since been restored. `forget-log.yaml` now
lists only the values that are still forgotten. The log as generated is in commit `88ef491`.

## Memory loss by kind

| Kind | Rate | Eligible | Forgotten as generated | Restored | Still forgotten |
| --- | ---: | ---: | ---: | ---: | ---: |
| `description` | 0.08 | 20,464 | 1,644 | 390 | 1,254 |
| `synonyms` | 0.15 | 6,022 | 920 | 0 | 920 |
| `tags` | 0.15 | 653 | 104 | 0 | 104 |
| `value_description` | 0.12 | 13,662 | 1,712 | 0 | 1,712 |
| `entity_expression` | 0.10 | 4,844 | 478 | 478 | 0 |
| `entity_metadata` | 0.10 | 4,844 | 475 | 475 | 0 |
| `grain_component_description` | 0.08 | 612 | 65 | 0 | 65 |
| `grain` | 0.06 | 653 | 41 | 0 | 41 |
| `grain_component_identity` | 0.05 | 612 | 40 | 0 | 40 |
| `claim` | 0.07 | 17,351 | 1,236 | 1,236 | 0 |
| **Total** | | **69,717** | **6,715** | **2,579** | **4,136** |

## Restored: relationship evidence

Relationships between entity definitions of the same logical entity are derived from the two
endpoint definitions, so every forgotten entity-definition field was restored:

| Field | Restored | Role in a relationship |
| --- | ---: | --- |
| `unique` | 360 | Multiplicity. |
| `total` | 203 | Match existence. |
| `conforms` | 347 | Match existence. |
| `entity_universe` | 326 | Match existence, through key containment. |
| `description` | 390 | Effective endpoint description, which distinguishes roles. |
| `entity_expression` | 478 | Agent-facing labels of the endpoint realization. |
| `entity_metadata` | 475 | Context for interpreting the endpoint realization. |

Every forgotten `claim` value was an entity-definition claim, so no claims remain forgotten. No
forgotten column description was the effective description of a single-column definition
without its own description, so no column values were restored.

Cross-entity relationships in `yaml/00_entity_relationships.yaml` were never degraded. Their
descriptions, `multiplicity`, and `match_existence` are complete as stated.

## Still forgotten

| Location | Kind | Count |
| --- | --- | ---: |
| Column | `description` | 1,096 |
| Column | `synonyms` | 830 |
| Column | `value_description` | 1,712 |
| Dataset descriptor | `description` | 67 |
| Dataset descriptor | `synonyms` | 90 |
| Dataset descriptor | `tags` | 104 |
| Grain | `grain` | 41 |
| Grain | `description` | 37 |
| Grain component | `grain_component_description` | 65 |
| Grain component | `grain_component_identity` | 40 |
| Logical identity | `description` | 54 |

A grain component's identity names the logical entity a record boundary is keyed by. It is not
an entity definition, so it creates no relationship and stays forgotten.
