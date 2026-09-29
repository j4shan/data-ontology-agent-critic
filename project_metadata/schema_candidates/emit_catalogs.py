"""Emit ontology-graph YAML catalogs and business-model notes from domain modules."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from domains.commerce import DOMAIN as COMMERCE  # noqa: E402
from domains.manufacturing import DOMAIN as MANUFACTURING  # noqa: E402
from domains.payer import DOMAIN as PAYER  # noqa: E402
from domains.retail import DOMAIN as RETAIL  # noqa: E402
from domains.telecom import DOMAIN as TELECOM  # noqa: E402
from population_stats import build_population, render_readme_statistics, render_statistics_markdown  # noqa: E402

DOMAINS = (MANUFACTURING, RETAIL, COMMERCE, TELECOM, PAYER)
_MULTIPLICITY = {"1:1", "1:many", "many:1", "many:many", "unknown"}
_EXISTENCE = {"always", "optional", "unknown"}


class CatalogError(ValueError):
    pass


def _identity_label(identity_id: str) -> str:
    stem = identity_id.removesuffix("_identity").replace("_", " ")
    return f"{stem[:1].upper()}{stem[1:]} identity"


def _dump(document: dict) -> str:
    return yaml.safe_dump(
        document,
        sort_keys=False,
        allow_unicode=True,
        width=100,
    )


def _validate(domain: dict) -> dict:
    datasets = domain["datasets"]
    names = [item["name"] for item in datasets]
    if len(names) != len(set(names)):
        duplicates = sorted({name for name in names if names.count(name) > 1})
        raise CatalogError(f"{domain['key']} duplicate datasets: {duplicates}")
    count = len(datasets)
    if count < 100 or count >= 300:
        raise CatalogError(f"{domain['key']} dataset count {count} is outside 100..299")

    universe: dict[str, tuple[str, str]] = {}
    references: list[tuple[dict, dict]] = []
    for dataset in datasets:
        columns = dataset["columns"]
        column_names = [column["name"] for column in columns]
        if len(column_names) != len(set(column_names)):
            raise CatalogError(f"{dataset['name']} has duplicate columns")
        universes = [column for column in columns if column.get("universe")]
        if len(universes) != 1:
            raise CatalogError(f"{dataset['name']} must declare exactly one universe key")
        grain = universes[0]
        if not grain["identity"].endswith("_identity"):
            raise CatalogError(f"{dataset['name']} identity must end with _identity")
        identity = grain["identity"]
        if identity in universe:
            other = universe[identity]
            raise CatalogError(
                f"{identity} is the universe of both {other[0]} and {dataset['name']}"
            )
        universe[identity] = (dataset["name"], grain["name"])
        for column in columns:
            if column.get("identity") and not column.get("universe"):
                references.append((dataset, column))
                for field, allowed in (
                    ("to_universe_multiplicity", _MULTIPLICITY),
                    ("from_universe_multiplicity", _MULTIPLICITY),
                    ("to_universe_existence", _EXISTENCE),
                    ("from_universe_existence", _EXISTENCE),
                ):
                    if column[field] not in allowed:
                        raise CatalogError(f"{dataset['name']}.{column['name']} bad {field}")
                if not column.get("business_rule"):
                    raise CatalogError(f"{dataset['name']}.{column['name']} missing business rule")

    for dataset, column in references:
        if column["identity"] not in universe:
            raise CatalogError(
                f"{dataset['name']}.{column['name']} references unknown {column['identity']}"
            )
        parent_name, _parent_column = universe[column["identity"]]
        if parent_name == dataset["name"]:
            raise CatalogError(
                f"{dataset['name']}.{column['name']} self-references {column['identity']}"
            )

    edges = []
    seen = set()
    for dataset, column in references:
        parent_name, parent_column = universe[column["identity"]]
        parent = next(item for item in datasets if item["name"] == parent_name)
        key = (
            dataset["name"],
            column["name"],
            column["identity"],
            parent_name,
            parent_column,
        )
        if key in seen:
            raise CatalogError(f"duplicate edge {key}")
        seen.add(key)
        edges.append(
            {
                "child": dataset,
                "child_column": column,
                "parent": parent,
                "parent_column": parent_column,
            }
        )

    for signature in domain.get("signatures", []):
        matches = [
            edge
            for edge in edges
            if edge["child"]["name"] == signature["child"]
            and edge["parent"]["name"] == signature["parent"]
            and edge["child_column"]["identity"] == signature["identity"]
            and edge["child_column"]["from_universe_multiplicity"] == signature["parent_multiplicity"]
            and edge["child_column"]["from_universe_existence"] == signature["parent_existence"]
            and edge["child_column"]["to_universe_multiplicity"] == signature["child_multiplicity"]
            and edge["child_column"]["to_universe_existence"] == signature["child_existence"]
        ]
        if not matches:
            raise CatalogError(f"{domain['key']} missing signature relationship {signature}")

    return {"universe": universe, "edges": edges}


def _node(domain: dict, dataset: dict) -> dict:
    grain = next(column for column in dataset["columns"] if column.get("universe"))
    root = domain["root"]
    qualified = f"{root}.{dataset['subject']}.{dataset['name']}"
    columns = []
    for column in dataset["columns"]:
        payload = {"name": column["name"], "description": column["description"]}
        if column.get("value_description"):
            payload["value_description"] = column["value_description"]
        columns.append(payload)
    entity_definitions = []
    for column in dataset["columns"]:
        if not column.get("identity"):
            continue
        metadata = {
            "expression_context": "SQL column reference",
            "population_role": "universe" if column.get("universe") else "reference",
        }
        if column.get("mapping"):
            metadata["mapping"] = column["mapping"]
        rule = column.get("business_rule") or (
            f"Complete authored population of {dataset['display_name'].lower()}."
        )
        metadata["business_rule"] = rule
        entity_definitions.append(
            {
                "identity_id": column["identity"],
                "dataset_columns": [column["name"]],
                "is_entity_universe": bool(column.get("universe")),
                "entity_expression": [f"[{column['name']}]"],
                "entity_metadata": metadata,
            }
        )
    node = {
        "node_id": f"sf:{qualified}",
        "descriptor": {
            "qualified_name": qualified,
            "display_name": dataset["display_name"],
            "description": dataset["description"],
            "synonyms": dataset["synonyms"],
            "tags": [dataset["role"], dataset["subject"]],
        },
        "accessor": {
            "schema_id": "accessor.snowflake.v1",
            "properties": {
                "account": domain["account"],
                "database": domain["database"],
                "schema": dataset["subject"].upper(),
                "object": dataset["name"].upper(),
                "format": "table",
            },
        },
        "grain": {
            "description": f"One row is one {dataset['display_name'].lower()}.",
            "components": [
                {
                    "identity_id": grain["identity"],
                    "dataset_columns": [grain["name"]],
                    "description": grain["description"],
                }
            ],
        },
        "columns": columns,
        "entity_definitions": entity_definitions,
    }
    return node


def _edge(domain: dict, edge: dict) -> dict:
    child = edge["child"]
    parent = edge["parent"]
    column = edge["child_column"]
    child_qualified = f"{domain['root']}.{child['subject']}.{child['name']}"
    parent_qualified = f"{domain['root']}.{parent['subject']}.{parent['name']}"
    return {
        "endpoint_a": {
            "node_id": f"sf:{child_qualified}",
            "identity_id": column["identity"],
            "dataset_columns": [column["name"]],
        },
        "endpoint_b": {
            "node_id": f"sf:{parent_qualified}",
            "identity_id": column["identity"],
            "dataset_columns": [edge["parent_column"]],
        },
        "a_to_b": {
            "multiplicity": column["to_universe_multiplicity"],
            "match_existence": column["to_universe_existence"],
        },
        "b_to_a": {
            "multiplicity": column["from_universe_multiplicity"],
            "match_existence": column["from_universe_existence"],
        },
    }


def _business_markdown(domain: dict, edges: list[dict]) -> str:
    by_subject: dict[str, list[dict]] = defaultdict(list)
    for dataset in domain["datasets"]:
        by_subject[dataset["subject"]].append(dataset)
    role_counts = defaultdict(int)
    for dataset in domain["datasets"]:
        role_counts[dataset["role"]] += 1
    lines = [
        f"# {domain['business_name']}",
        "",
        domain["narrative"].strip(),
        "",
        "## Data ecosystem",
        "",
        (
            f"The authored catalog `{domain['root']}` contains {len(domain['datasets'])} datasets "
            f"({role_counts['dimension']} dimensions, {role_counts['fact']} facts, "
            f"{role_counts['bridge']} bridges) in the Snowflake database `{domain['database']}` "
            f"on account `{domain['account']}`."
        ),
        "",
        (
            "Each dataset is one ontology node. The grain column is the system of record for that "
            "dataset's logical identity and is marked `is_entity_universe: true`. Foreign-key "
            "columns realize the same logical identity with `is_entity_universe: false`, because "
            "the child dataset does not hold the complete population. Edges join those two "
            "realizations. Multiplicity and match existence are directional and follow the "
            "operating rules below. "
            + (
                "Synthetic row counts and join fan-out for a "
                f"{domain['statistics_window_days']}-day window are in `statistics.md`. "
                "They are derived from authored populations and these multiplicity rules. "
                "The YAML nodes do not carry those statistics."
                if domain.get("statistics_window_days")
                else "Row counts, distinct counts, and other data statistics are intentionally absent."
            )
        ),
        "",
        "## Signature relationships",
        "",
        "| Relationship | Identity | Parent to child | Child to parent | Rule |",
        "| --- | --- | --- | --- | --- |",
    ]
    for signature in domain.get("signatures", []):
        match = next(
            edge
            for edge in edges
            if edge["parent"]["name"] == signature["parent"]
            and edge["child"]["name"] == signature["child"]
            and edge["child_column"]["identity"] == signature["identity"]
        )
        rule = " ".join(match["child_column"]["business_rule"].replace("|", "/").split())
        lines.append(
            f"| `{signature['parent']}` to `{signature['child']}` | `{signature['identity']}` | "
            f"{signature['parent_multiplicity']} ({signature['parent_existence']}) | "
            f"{signature['child_multiplicity']} ({signature['child_existence']}) | {rule} |"
        )
    lines.extend(["", "## Relationship rules", ""])
    lines.append("| Child dataset | Column | Universe dataset | Mapping | Parent match | Child match | Rule |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    for edge in edges:
        column = edge["child_column"]
        rule = " ".join(column["business_rule"].replace("|", "/").split())
        lines.append(
            f"| `{edge['child']['name']}` | `{column['name']}` | `{edge['parent']['name']}` | "
            f"{column['mapping']} | {column['from_universe_multiplicity']} / "
            f"{column['from_universe_existence']} | {column['to_universe_multiplicity']} / "
            f"{column['to_universe_existence']} | {rule} |"
        )
    lines.extend(["", "## Dataset inventory", ""])
    for subject in sorted(by_subject):
        lines.append(f"### {subject}")
        lines.append("")
        lines.append("| Dataset | Role | Grain | Description |")
        lines.append("| --- | --- | --- | --- |")
        for dataset in by_subject[subject]:
            grain = next(column for column in dataset["columns"] if column.get("universe"))
            description = dataset["description"].replace("|", "/")
            lines.append(
                f"| `{dataset['name']}` | {dataset['role']} | `{grain['name']}` | {description} |"
            )
        lines.append("")
    lines.extend(["## Provenance", "", domain["provenance"].strip(), ""])
    return "\n".join(lines)


def emit(domain: dict) -> dict:
    checked = _validate(domain)
    target = ROOT / domain["key"]
    yaml_dir = target / "yaml"
    if yaml_dir.exists():
        for stale in yaml_dir.glob("*.yaml"):
            stale.unlink()
    yaml_dir.mkdir(parents=True, exist_ok=True)

    synonyms = domain.get("identity_synonyms", {})
    identities = {}
    for identity, (dataset_name, _column) in sorted(checked["universe"].items()):
        dataset = next(item for item in domain["datasets"] if item["name"] == dataset_name)
        payload = {
            "name": _identity_label(identity),
            "description": (
                f"Identifies a {dataset['display_name'].lower()} in the "
                f"{domain['business_name']} data ecosystem."
            ),
        }
        if identity in synonyms:
            payload["synonyms"] = synonyms[identity]
        identities[identity] = payload
    (yaml_dir / "00_logical_identities.yaml").write_text(
        _dump({"schema_version": "2", "logical_identities": identities}),
        encoding="utf-8",
    )

    by_subject: dict[str, list[dict]] = defaultdict(list)
    for dataset in domain["datasets"]:
        by_subject[dataset["subject"]].append(dataset)
    for subject in sorted(by_subject):
        document = {
            "schema_version": "2",
            "nodes": [_node(domain, dataset) for dataset in by_subject[subject]],
        }
        (yaml_dir / f"{subject}.yaml").write_text(_dump(document), encoding="utf-8")

    edge_document = {
        "schema_version": "2",
        "edges": [_edge(domain, edge) for edge in checked["edges"]],
    }
    (yaml_dir / "99_relationships.yaml").write_text(_dump(edge_document), encoding="utf-8")
    (target / "business-model.md").write_text(
        _business_markdown(domain, checked["edges"]),
        encoding="utf-8",
    )
    if domain.get("statistics_window_days"):
        report = build_population(domain, checked["edges"])
        (target / "statistics.json").write_text(
            json.dumps(report, indent=2) + "\n",
            encoding="utf-8",
        )
        (target / "statistics.md").write_text(
            render_statistics_markdown(report),
            encoding="utf-8",
        )
        readme = "\n".join(
            [
                f"# {domain['business_name']}",
                "",
                "## Introduction",
                "",
                domain["readme_intro"].strip(),
                "",
                "The business narrative and the full relationship table are in `business-model.md`. Loadable YAML is in `yaml/`.",
                "",
                "## BI questions",
                "",
                domain["readme_questions"].strip(),
                "",
                render_readme_statistics(report).rstrip(),
                "",
            ]
        )
        (target / "README.md").write_text(readme, encoding="utf-8")
    return {
        "key": domain["key"],
        "datasets": len(domain["datasets"]),
        "edges": len(checked["edges"]),
        "identities": len(checked["universe"]),
        "yaml_dir": str(yaml_dir),
    }


def main() -> None:
    for domain in DOMAINS:
        summary = emit(domain)
        print(
            f"{summary['key']}: {summary['datasets']} datasets, "
            f"{summary['identities']} identities, {summary['edges']} relationships"
        )


if __name__ == "__main__":
    main()
