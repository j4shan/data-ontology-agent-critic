# Proposal: track the three intermediary collections in separate files

This proposal asks the Data Ontology Graph intermediary to record where `logical_identities`, `nodes`, and `edges` live when a catalog is a directory. It does not change the assembled document those files produce. Critic does not apply this change to the Data Ontology Graph repository.

## Current contract

Schema version 2 defines one assembled document:

| Field | Role |
| --- | --- |
| `schema_version` | Constant `"2"` |
| `logical_identities` | Map of business identities |
| `nodes` | Dataset list |
| `edges` | Relationship list |

A single file may contain all three collections. A directory may also be loaded: every `.yaml` file is merged, and any file may contain any mix of the three keys. The merge checks duplicate identity ids and duplicate `node_id` values. It does not record which file owns which collection, and it accepts a file that mixes identities, nodes, and edges.

The catalogs in this scratchpad already keep the collections apart:

| Collection | File |
| --- | --- |
| `logical_identities` | `yaml/00_logical_identities.yaml` |
| `nodes` | One subject file, such as `yaml/organization.yaml` |
| `edges` | `yaml/99_relationships.yaml` |

That split is an authoring choice. The schema does not require it.

## Proposed directory contract

Directory input gains a manifest, `directory-manifest.yaml`, stored beside `yaml/` rather than inside it. The current builder rejects any non-collection file inside the YAML directory, so the manifest stays outside that directory until the builder learns this contract.

The manifest names the file or files for each of the three collections. A collection file contains `schema_version` and exactly one of `logical_identities`, `nodes`, or `edges`.

| Collection | Files | File contents |
| --- | --- | --- |
| `logical_identities` | Exactly one | `schema_version` and `logical_identities` |
| `nodes` | One or more | `schema_version` and `nodes` |
| `edges` | Exactly one | `schema_version` and `edges` |

Nodes stay a single list in the assembled document. Subject files are partitions of that list, and the manifest is the list of those partitions. Identities and edges are not partitioned.

Proposed manifest shape, validated by `intermediary-directory.schema.json`:

```yaml
schema_version: "2"
logical_identities: 00_logical_identities.yaml
nodes:
  - organization.yaml
  - product.yaml
edges: 99_relationships.yaml
```

Paths are relative to the YAML directory. The manifest lists every collection file once. A path that appears twice, points outside the directory, or names a file whose collection does not match the manifest key is invalid.

## Builder behavior

Single-file input stays an assembled `IntermediaryDefinition` for backward compatibility.

Directory input reads the manifest first, then loads only the listed files:

1. Reject a collection file that contains more than one of `logical_identities`, `nodes`, and `edges`.
2. Reject a YAML file in the directory that the manifest does not list.
3. Reject a listed file that is missing.
4. Keep the existing rules for conflicting `schema_version`, duplicate identity ids, and duplicate `node_id` values.
5. Assemble the three collections and validate the result with the existing `IntermediaryDefinition` schema.

No relationship is inferred. The manifest tracks file ownership. It does not add or remove identities, nodes, or edges.

## Examples

Manifests for the scratchpad catalogs are in `manifests/`. They match the files already present under each catalog's `yaml/` directory. They are not builder input.

## Out of scope

This proposal does not change single-file input, add statistics, or change entity definitions,
multiplicity, or match existence.
