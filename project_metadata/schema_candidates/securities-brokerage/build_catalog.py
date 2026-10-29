"""Emit the `securities-brokerage` intermediary YAML, then apply the seeded forget pass.

Run from this directory:

    python3 build_catalog.py

The script writes `directory-manifest.yaml`, `yaml/`, and `forget-log.yaml`. The forget pass
removes a fixed share of non-essential descriptive metadata. Removed fields fall back to the
schema defaults (empty text, no synonyms). Names, keys, accessors, grains, and entity claims
are never forgotten.
"""

from __future__ import annotations

import random
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from catalog_source import DATASETS, IDENTITIES, ROOT as CATALOG  # noqa: E402

SCHEMA_VERSION = "4"
FORGET_SEED = 20261029
FORGET_RATE = 0.05
IDENTITY_FILE = "00_logical_identities.yaml"


class CatalogError(ValueError):
    pass


def _dump(document: dict) -> str:
    return yaml.safe_dump(document, sort_keys=False, allow_unicode=True, width=100)


def _qualified(dataset: dict) -> str:
    return f"{CATALOG}.{dataset['schema']}.{dataset['name']}"


def _node_id(dataset: dict) -> str:
    return f"{dataset['layer']['family']}:{_qualified(dataset)}"


LAYER_NAMES = {"sql-database": "oltp", "s3": "landing", "snowflake": "warehouse"}
LAYER_TAGS = {"sql-database": "operational", "s3": "landing", "snowflake": "analytical"}


def _collection(dataset: dict) -> str:
    return f"{LAYER_NAMES[dataset['layer']['family']]}_{dataset['schema']}.yaml"


def _accessor(dataset: dict) -> dict:
    layer = dataset["layer"]
    properties = dict(layer["properties"])
    if layer["family"] == "snowflake":
        properties.update(schema=dataset["schema"].upper(), object=dataset["name"].upper())
    elif layer["family"] == "s3":
        properties.update(prefix=dataset["file"]["prefix"], format=dataset["file"]["format"])
    else:
        properties.update(schema=dataset["schema"], object=dataset["name"])
    return {"schema_id": layer["schema_id"], "properties": properties}


def _column(column: dict) -> dict:
    payload = {"name": column["name"], "description": column["description"]}
    if column["value_description"]:
        payload["value_description"] = column["value_description"]
    if column["synonyms"]:
        payload["synonyms"] = column["synonyms"]
    return payload


def _definition(dataset: dict, key: dict) -> dict:
    columns = sorted(key["columns"])
    payload = {
        "identity_id": key["identity"],
        "dataset_columns": columns,
        "entity_universe": key["universe"],
        "unique": key["unique"],
        "total": key["total"],
        "conforms": key["conforms"],
        "entity_expression": [f"[{', '.join(columns)}]"],
        "entity_metadata": {"expression_context": dataset["layer"]["expression_context"]},
    }
    if key["description"]:
        payload["description"] = key["description"]
    return payload


def _grain(dataset: dict) -> dict:
    identity, columns = dataset["grain"]
    component: dict = {}
    if identity is not None:
        component["identity_id"] = identity
    component["dataset_columns"] = sorted(columns)
    description = dataset["grain_description"] or f"One row per {dataset['display_name'].lower()}."
    return {"description": description, "components": [component]}


def _node(dataset: dict) -> dict:
    return {
        "node_id": _node_id(dataset),
        "descriptor": {
            "qualified_name": _qualified(dataset),
            "display_name": dataset["display_name"],
            "description": dataset["description"],
            "synonyms": dataset["synonyms"],
            "tags": [
                LAYER_TAGS[dataset["layer"]["family"]],
                dataset["schema"],
                dataset["role"],
            ],
        },
        "accessor": _accessor(dataset),
        "grain": _grain(dataset),
        "columns": [_column(column) for column in dataset["columns"]],
        "entity_definitions": [_definition(dataset, key) for key in dataset["keys"]],
    }


def _validate() -> None:
    names = [_qualified(dataset) for dataset in DATASETS]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise CatalogError(f"duplicate datasets: {duplicates}")
    used: set[str] = set()
    complete: Counter[str] = Counter()
    for dataset in DATASETS:
        label = _qualified(dataset)
        column_names = [column["name"] for column in dataset["columns"]]
        if len(column_names) != len(set(column_names)):
            raise CatalogError(f"{label} repeats a column")
        keys = set()
        for key in dataset["keys"]:
            if key["identity"] not in IDENTITIES:
                raise CatalogError(f"{label} uses unknown identity {key['identity']}")
            missing = set(key["columns"]) - set(column_names)
            if missing:
                raise CatalogError(f"{label} key {key['identity']} names missing columns {sorted(missing)}")
            if key["universe"] == "complete":
                complete[key["identity"]] += 1
            used.add(key["identity"])
            keys.add((key["identity"], tuple(sorted(key["columns"]))))
        identity, columns = dataset["grain"]
        if set(columns) - set(column_names):
            raise CatalogError(f"{label} grain names missing columns")
        if identity is not None and (identity, tuple(sorted(columns))) not in keys:
            raise CatalogError(f"{label} grain identity {identity} has no matching entity definition")
    unused = sorted(set(IDENTITIES) - used)
    if unused:
        raise CatalogError(f"identities without a realization: {unused}")
    without_universe = sorted(identity for identity in IDENTITIES if complete[identity] == 0)
    if without_universe:
        raise CatalogError(f"identities without a complete realization: {without_universe}")


def _documents() -> tuple[dict, dict[str, dict]]:
    identities = {}
    for identity_id in sorted(IDENTITIES):
        name, description, synonyms = IDENTITIES[identity_id]
        payload = {"name": name, "description": description}
        if synonyms:
            payload["synonyms"] = list(synonyms)
        identities[identity_id] = payload
    by_file: dict[str, list[dict]] = defaultdict(list)
    for dataset in sorted(DATASETS, key=_qualified):
        by_file[_collection(dataset)].append(_node(dataset))
    nodes = {
        name: {"schema_version": SCHEMA_VERSION, "nodes": by_file[name]} for name in sorted(by_file)
    }
    return {"schema_version": SCHEMA_VERSION, "logical_identities": identities}, nodes


def _forgettable(identity_doc: dict, node_docs: dict[str, dict]) -> list[tuple[str, str, dict, str]]:
    """Every non-empty descriptive field: (file, location, owning mapping, field name)."""
    slots = []
    for identity_id, payload in identity_doc["logical_identities"].items():
        for field in ("description", "synonyms"):
            if payload.get(field):
                slots.append((IDENTITY_FILE, f"logical_identities.{identity_id}", payload, field))
    for file_name, document in node_docs.items():
        for node in document["nodes"]:
            base = node["node_id"]
            for field in ("description", "synonyms"):
                if node["descriptor"].get(field):
                    slots.append((file_name, f"{base}.descriptor", node["descriptor"], field))
            if node["grain"].get("description"):
                slots.append((file_name, f"{base}.grain", node["grain"], "description"))
            for column in node["columns"]:
                for field in ("description", "value_description", "synonyms"):
                    if column.get(field):
                        slots.append((file_name, f"{base}.columns.{column['name']}", column, field))
            for definition in node["entity_definitions"]:
                if definition.get("description"):
                    location = f"{base}.entity_definitions.{definition['identity_id']}[{', '.join(definition['dataset_columns'])}]"
                    slots.append((file_name, location, definition, "description"))
    return slots


def _forget(identity_doc: dict, node_docs: dict[str, dict]) -> dict:
    slots = _forgettable(identity_doc, node_docs)
    rng = random.Random(FORGET_SEED)
    chosen = sorted(rng.sample(range(len(slots)), round(len(slots) * FORGET_RATE)))
    entries = []
    for index in chosen:
        file_name, location, owner, field = slots[index]
        entries.append({"file": file_name, "location": location, "field": field, "original": owner.pop(field)})
    by_field = Counter(f"{_kind(entry)}.{entry['field']}" for entry in entries)
    return {
        "seed": FORGET_SEED,
        "rate": FORGET_RATE,
        "eligible_fields": len(slots),
        "forgotten_fields": len(entries),
        "forgotten_by_kind": dict(sorted(by_field.items())),
        "entries": entries,
    }


def _kind(entry: dict) -> str:
    location = entry["location"]
    for kind in ("descriptor", "grain", "columns", "entity_definitions"):
        if f".{kind}" in location:
            return kind
    return "logical_identity"


def _relationship_counts() -> dict[str, int]:
    """Pairs of realizations per identity; the actor derives one relationship per pair."""
    realizations: Counter[str] = Counter()
    for dataset in DATASETS:
        for key in dataset["keys"]:
            realizations[key["identity"]] += 1
    return {identity: len(list(combinations(range(count), 2))) for identity, count in realizations.items()}


def main() -> None:
    _validate()
    identity_doc, node_docs = _documents()
    log = _forget(identity_doc, node_docs)

    yaml_dir = ROOT / "yaml"
    yaml_dir.mkdir(exist_ok=True)
    for stale in yaml_dir.glob("*.yaml"):
        stale.unlink()
    (yaml_dir / IDENTITY_FILE).write_text(_dump(identity_doc), encoding="utf-8")
    for file_name, document in node_docs.items():
        (yaml_dir / file_name).write_text(_dump(document), encoding="utf-8")
    manifest = {"schema_version": SCHEMA_VERSION, "logical_identities": IDENTITY_FILE, "nodes": sorted(node_docs)}
    (ROOT / "directory-manifest.yaml").write_text(_dump(manifest), encoding="utf-8")
    (ROOT / "forget-log.yaml").write_text(_dump(log), encoding="utf-8")

    pairs = _relationship_counts()
    roles = Counter(dataset["role"] for dataset in DATASETS)
    layers = Counter(dataset["layer"]["family"] for dataset in DATASETS)
    definitions = sum(len(dataset["keys"]) for dataset in DATASETS)
    columns = sum(len(dataset["columns"]) for dataset in DATASETS)
    print(f"datasets: {len(DATASETS)} ({dict(layers)}) roles: {dict(sorted(roles.items()))}")
    print(f"columns: {columns} entity definitions: {definitions} logical entities: {len(IDENTITIES)}")
    print(f"derived relationship pairs: {sum(pairs.values())}")
    print("largest identities:", sorted(pairs.items(), key=lambda item: -item[1])[:8])
    print(f"forgotten: {log['forgotten_fields']} of {log['eligible_fields']} -> {log['forgotten_by_kind']}")


if __name__ == "__main__":
    main()
