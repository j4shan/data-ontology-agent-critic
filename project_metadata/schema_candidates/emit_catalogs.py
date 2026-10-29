"""Emit business-model notes and synthetic statistics from domain modules."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

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

    for item in domain.get("composite_identities", []):
        identity = item["identity"]
        if identity in universe:
            raise CatalogError(f"{identity} is both a universe and a composite identity")
        if len(item["members"]) < 2:
            raise CatalogError(f"{identity} needs at least two member datasets")
        for dataset_name, columns in item["members"].items():
            dataset = next((d for d in datasets if d["name"] == dataset_name), None)
            if dataset is None:
                raise CatalogError(f"{identity} names unknown dataset {dataset_name}")
            names = {column["name"] for column in dataset["columns"]}
            if len(columns) < 2 or not set(columns) <= names:
                raise CatalogError(f"{identity} needs two or more existing columns on {dataset_name}")
        for pair in item["links"]:
            if pair["a"] not in item["members"] or pair["b"] not in item["members"]:
                raise CatalogError(f"{identity} link {pair['a']}-{pair['b']} names a non-member")
            for multiplicity, existence in (pair["a_to_b"], pair["b_to_a"]):
                if multiplicity not in _MULTIPLICITY or existence not in _EXISTENCE:
                    raise CatalogError(f"{identity} link {pair['a']}-{pair['b']} bad direction")
            if not pair.get("rule"):
                raise CatalogError(f"{identity} link {pair['a']}-{pair['b']} missing rule")

    return {"universe": universe, "edges": edges}


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
                "They are derived from authored populations and these multiplicity rules."
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
    if domain.get("composite_identities"):
        lines.extend(["", "## Composite identities", ""])
        lines.append(
            "These business entities are identified by columns that also realize other "
            "identities. No dataset holds their complete population, so every realization is "
            "partial. Edges join only the datasets the business compares at that key."
        )
        lines.append("")
        lines.append("| Identity | Datasets and columns | Compared pair | A to B | B to A | Rule |")
        lines.append("| --- | --- | --- | --- | --- | --- |")
        for item in domain["composite_identities"]:
            members = "; ".join(
                f"`{name}` ({', '.join(columns)})" for name, columns in item["members"].items()
            )
            for pair in item["links"]:
                lines.append(
                    f"| `{item['identity']}` | {members} | `{pair['a']}` to `{pair['b']}` | "
                    f"{pair['a_to_b'][0]} ({pair['a_to_b'][1]}) | "
                    f"{pair['b_to_a'][0]} ({pair['b_to_a'][1]}) | {pair['rule']} |"
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
                "The business narrative and the full relationship table are in `business-model.md`.",
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
        "edges": len(checked["edges"])
        + sum(len(item["links"]) for item in domain.get("composite_identities", [])),
        "identities": len(checked["universe"]) + len(domain.get("composite_identities", [])),
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
