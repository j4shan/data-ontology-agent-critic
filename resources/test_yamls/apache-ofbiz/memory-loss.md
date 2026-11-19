# Apache OFBiz memory loss

This catalog was degraded by the `memory-loss-v1` process: a sample of eligible values was removed
from `yaml/`, and each removed value is listed with its original in `forget-log.yaml`. A forgotten
claim reads `unknown`; a forgotten description, synonym list, tag list, expression, or metadata
entry is absent.

Every forgotten value that shapes a relationship has since been restored. `forget-log.yaml` now
lists only the values that are still forgotten. The log as generated is in commit `88ef491`.

## Memory loss by kind

| Kind | Rate | Eligible | Forgotten as generated | Restored | Still forgotten |
| --- | ---: | ---: | ---: | ---: | ---: |
| `description` | 0.08 | 14,123 | 1,157 | 261 | 896 |
| `synonyms` | 0.15 | 1,640 | 241 | 0 | 241 |
| `tags` | 0.15 | 835 | 119 | 0 | 119 |
| `value_description` | 0.12 | 8,694 | 1,065 | 0 | 1,065 |
| `entity_expression` | 0.10 | 2,991 | 306 | 306 | 0 |
| `entity_metadata` | 0.10 | 2,991 | 325 | 325 | 0 |
| `grain_component_description` | 0.08 | 768 | 58 | 0 | 58 |
| `grain` | 0.06 | 835 | 67 | 0 | 67 |
| `grain_component_identity` | 0.05 | 768 | 37 | 0 | 37 |
| `claim` | 0.07 | 10,548 | 760 | 760 | 0 |
| **Total** | | **44,193** | **4,135** | **1,652** | **2,483** |

## Restored: relationship evidence

Relationships between entity definitions of the same logical entity are derived from the two
endpoint definitions, so every forgotten entity-definition field was restored:

| Field | Restored | Role in a relationship |
| --- | ---: | --- |
| `unique` | 224 | Multiplicity. |
| `total` | 120 | Match existence. |
| `conforms` | 201 | Match existence. |
| `entity_universe` | 215 | Match existence, through key containment. |
| `description` | 261 | Effective endpoint description, which distinguishes roles. |
| `entity_expression` | 306 | Agent-facing labels of the endpoint realization. |
| `entity_metadata` | 325 | Context for interpreting the endpoint realization. |

Every forgotten `claim` value was an entity-definition claim, so no claims remain forgotten. No
forgotten column description was the effective description of a single-column definition
without its own description, so no column values were restored.

Cross-entity relationships in `yaml/00_entity_relationships.yaml` were never degraded. Their
descriptions, `multiplicity`, and `match_existence` are complete as stated.

## Still forgotten

| Location | Kind | Count |
| --- | --- | ---: |
| Column | `description` | 687 |
| Column | `value_description` | 1,065 |
| Dataset descriptor | `description` | 59 |
| Dataset descriptor | `synonyms` | 108 |
| Dataset descriptor | `tags` | 119 |
| Grain | `grain` | 67 |
| Grain | `description` | 77 |
| Grain component | `grain_component_description` | 58 |
| Grain component | `grain_component_identity` | 37 |
| Logical identity | `description` | 73 |
| Logical identity | `synonyms` | 133 |

A grain component's identity names the logical entity a record boundary is keyed by. It is not
an entity definition, so it creates no relationship and stays forgotten.
