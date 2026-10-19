"""Closed-form synthetic populations and inbound/outbound join statistics.

Row counts are authored. Distinct keys, nulls, and fan-out are derived from the
authored multiplicity so a 30-day window stays consistent with the join rules.
No row sample is generated.
"""

from __future__ import annotations

from domains.dsl import _KINDS


class PopulationError(ValueError):
    pass


def _matched_children(child_rows: int, kind: str, column: dict) -> tuple[int, float]:
    _child_mult, child_exist, _parent_mult, _parent_exist = _KINDS[kind]
    if child_exist == "always":
        return child_rows, 1.0
    if column.get("matched_rows") is not None:
        matched = int(column["matched_rows"])
        if matched < 0 or matched > child_rows:
            raise PopulationError(
                f"{column['name']} matched_rows {matched} outside 0..{child_rows}"
            )
        rate = (matched / child_rows) if child_rows else 0.0
        return matched, rate
    rate = 0.93 if column.get("match_rate") is None else float(column["match_rate"])
    if not 0 <= rate <= 1:
        raise PopulationError(f"{column['name']} match_rate {rate} outside 0..1")
    return int(round(child_rows * rate)), rate


def join_statistics(child_rows: int, parent_rows: int, kind: str, column: dict) -> dict:
    child_mult, child_exist, parent_mult, parent_exist = _KINDS[kind]
    matched, rate = _matched_children(child_rows, kind, column)
    if parent_exist == "always" and parent_mult == "1:many":
        if matched < parent_rows:
            raise PopulationError(
                f"{column['name']} {kind} matched {matched} < parent rows {parent_rows}"
            )
        distinct = parent_rows
    elif parent_mult == "1:1" and parent_exist == "always":
        if child_rows != parent_rows or matched != child_rows:
            raise PopulationError(f"{column['name']} 11! populations are not equal")
        distinct = parent_rows
    elif parent_mult == "1:1":
        if matched > parent_rows:
            raise PopulationError(
                f"{column['name']} 1:1 matched {matched} > parent rows {parent_rows}"
            )
        distinct = matched
    else:
        if matched == 0:
            distinct = 0
        elif column.get("coverage") is None:
            distinct = parent_rows if matched >= parent_rows else matched
        else:
            coverage = float(column["coverage"])
            if not 0 <= coverage <= 1:
                raise PopulationError(f"{column['name']} coverage {coverage} outside 0..1")
            distinct = int(round(parent_rows * coverage))
            distinct = min(parent_rows, matched, max(0, distinct))
            if coverage > 0 and matched > 0 and distinct == 0:
                distinct = 1
        if parent_exist == "always" and distinct != parent_rows:
            raise PopulationError(f"{column['name']} required parent is not fully covered")
    if distinct > matched:
        raise PopulationError(f"{column['name']} distinct parents exceed matched children")
    average = (matched / distinct) if distinct else 0.0
    return {
        "kind": kind,
        "child_to_parent_multiplicity": child_mult,
        "child_to_parent_existence": child_exist,
        "parent_to_child_multiplicity": parent_mult,
        "parent_to_child_existence": parent_exist,
        "child_rows": child_rows,
        "parent_rows": parent_rows,
        "matched_child_rows": matched,
        "null_child_rows": child_rows - matched,
        "child_match_rate": rate,
        "distinct_parent_keys": distinct,
        "unmatched_parent_rows": parent_rows - distinct,
        "parent_coverage": (distinct / parent_rows) if parent_rows else 0.0,
        "avg_children_per_matched_parent": average,
    }


def _kind_of(column: dict) -> str:
    for kind, values in _KINDS.items():
        if (
            column["to_universe_multiplicity"] == values[0]
            and column["to_universe_existence"] == values[1]
            and column["from_universe_multiplicity"] == values[2]
            and column["from_universe_existence"] == values[3]
        ):
            return kind
    raise PopulationError(f"{column['name']} has no known relationship kind")


def build_population(domain: dict, edges: list[dict]) -> dict:
    datasets = {item["name"]: item for item in domain["datasets"]}
    missing = [name for name, item in datasets.items() if "rows" not in item]
    if missing:
        raise PopulationError(f"{domain['key']} missing rows on {missing[:8]}")
    populations = []
    for item in domain["datasets"]:
        populations.append(
            {
                "dataset": item["name"],
                "subject": item["subject"],
                "role": item["role"],
                "volume_class": item.get("volume_class", ""),
                "rows": item["rows"],
                "display_name": item["display_name"],
                "description": item["description"],
            }
        )
    joins = []
    for edge in edges:
        column = edge["child_column"]
        stats = join_statistics(
            edge["child"]["rows"],
            edge["parent"]["rows"],
            _kind_of(column),
            column,
        )
        joins.append(
            {
                "child": edge["child"]["name"],
                "child_role": edge["child"]["role"],
                "column": column["name"],
                "parent": edge["parent"]["name"],
                "parent_role": edge["parent"]["role"],
                "identity": column["identity"],
                **stats,
            }
        )
    by_child: dict[str, list[dict]] = {}
    by_parent: dict[str, list[dict]] = {}
    for join in joins:
        by_child.setdefault(join["child"], []).append(join)
        by_parent.setdefault(join["parent"], []).append(join)
    major = []
    for entry in domain["major_facts"]:
        name = entry["dataset"]
        dataset = datasets[name]
        major.append(
            {
                **entry,
                "rows": dataset["rows"],
                "role": dataset["role"],
                "volume_class": dataset.get("volume_class", "transaction"),
                "subject": dataset["subject"],
                "outbound": by_child.get(name, []),
                "inbound": by_parent.get(name, []),
            }
        )
    fact_rows = sum(item["rows"] for item in populations if item["role"] == "fact")
    major.sort(key=lambda item: (-item["rows"], item["dataset"]))
    return {
        "key": domain["key"],
        "business_name": domain["business_name"],
        "window_days": domain["statistics_window_days"],
        "method": (
            "Synthetic closed-form population for the stated window. Dimension and fact "
            "row counts are authored from the cited industry anchors and from structural "
            "fan-out (every parent required by an always-match rule has at least one child). "
            "Distinct parent keys, unmatched parents, null foreign keys, and average children "
            "per matched parent are derived from multiplicity. Optional-child match rates "
            "default to 0.93 when a join does not set one. Optional-parent coverage defaults "
            "to the full parent population when matched children can reach it, and otherwise "
            "to one child per observed parent. A stated coverage or matched-row count overrides "
            "that default. This is not a sampled extract."
        ),
        "dataset_count": len(populations),
        "fact_row_total": fact_rows,
        "populations": populations,
        "joins": joins,
        "major_facts": major,
    }


def _int(value: int) -> str:
    return f"{value:,}"


def _num(value: float) -> str:
    return f"{value:,.2f}"


def _pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def _join_table(rows: list[dict], inbound: bool) -> list[str]:
    if not rows:
        return ["None in this catalog.", ""]
    if inbound:
        header = (
            "| Child dataset | Column | Child rows | Matched children | Null children | "
            "Distinct parent keys | Unmatched parents | Avg children per matched parent |"
        )
        rule = "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |"
    else:
        header = (
            "| Column | Universe dataset | Child rows | Matched children | Null children | "
            "Distinct parent keys | Unmatched parents | Avg children per matched parent |"
        )
        rule = "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |"
    lines = [header, rule]
    ordered = sorted(rows, key=lambda item: (-item["child_rows"], item["column"], item["child"]))
    for item in ordered:
        if inbound:
            left = f"`{item['child']}` | `{item['column']}`"
        else:
            left = f"`{item['column']}` | `{item['parent']}`"
        lines.append(
            f"| {left} | {_int(item['child_rows'])} | {_int(item['matched_child_rows'])} | "
            f"{_int(item['null_child_rows'])} | {_int(item['distinct_parent_keys'])} | "
            f"{_int(item['unmatched_parent_rows'])} | {_num(item['avg_children_per_matched_parent'])} |"
        )
    lines.append("")
    return lines


def render_statistics_markdown(report: dict) -> str:
    lines = [
        f"# {report['business_name']} synthetic statistics",
        "",
        report["method"],
        "",
        (
            f"Window: {report['window_days']} days. Datasets: {report['dataset_count']}. "
            f"Sum of fact-table rows in the window: {_int(report['fact_row_total'])}."
        ),
        "",
        "## Major fact tables",
        "",
        "These are the event and periodic-snapshot facts where high-volume data lands.",
        "",
        "| Fact | Grain class | Rows in window | Basis |",
        "| --- | --- | ---: | --- |",
    ]
    for fact in report["major_facts"]:
        basis = " ".join(fact["basis"].replace("|", "/").split())
        lines.append(
            f"| `{fact['dataset']}` | {fact['volume_class']} | {_int(fact['rows'])} | {basis} |"
        )
    lines.extend(["", "## Join statistics for major facts", ""])
    for fact in report["major_facts"]:
        lines.append(f"### `{fact['dataset']}`")
        lines.append("")
        lines.append(fact["landing"].strip())
        lines.append("")
        lines.append(
            f"Population `{_int(fact['rows'])}` rows. "
            f"Outbound joins are foreign keys on this fact. "
            f"Inbound joins are other datasets that reference this fact."
        )
        lines.append("")
        lines.append("#### Outbound")
        lines.append("")
        lines.extend(_join_table(fact["outbound"], inbound=False))
        lines.append("#### Inbound")
        lines.append("")
        lines.extend(_join_table(fact["inbound"], inbound=True))
    lines.extend(["## Dataset populations", ""])
    lines.append("| Dataset | Role | Volume class | Rows |")
    lines.append("| --- | --- | --- | ---: |")
    for item in sorted(report["populations"], key=lambda row: (-row["rows"], row["dataset"])):
        lines.append(
            f"| `{item['dataset']}` | {item['role']} | {item['volume_class'] or '—'} | {_int(item['rows'])} |"
        )
    lines.extend(["", "## All joins", ""])
    lines.append(
        "| Child | Column | Parent | Matched children | Null children | Distinct parent keys | "
        "Unmatched parents | Parent coverage | Avg children per matched parent |"
    )
    lines.append("| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |")
    for item in sorted(report["joins"], key=lambda row: (row["child"], row["column"])):
        lines.append(
            f"| `{item['child']}` | `{item['column']}` | `{item['parent']}` | "
            f"{_int(item['matched_child_rows'])} | {_int(item['null_child_rows'])} | "
            f"{_int(item['distinct_parent_keys'])} | {_int(item['unmatched_parent_rows'])} | "
            f"{_pct(item['parent_coverage'])} | {_num(item['avg_children_per_matched_parent'])} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_readme_statistics(report: dict) -> str:
    lines = [
        "## Major fact tables",
        "",
        (
            f"High-volume landing zones for the {report['window_days']}-day synthetic window. "
            f"The sum of all fact rows in the catalog, including smaller operational facts, is "
            f"{_int(report['fact_row_total'])}."
        ),
        "",
        "| Fact | Grain class | Rows | Why this is a landing zone |",
        "| --- | --- | ---: | --- |",
    ]
    for fact in report["major_facts"]:
        basis = " ".join(fact["basis"].replace("|", "/").split())
        lines.append(
            f"| `{fact['subject']}.{fact['dataset']}` | {fact['volume_class']} | "
            f"{_int(fact['rows'])} | {basis} |"
        )
    lines.extend(
        [
            "",
            "## Synthetic join statistics",
            "",
            report["method"],
            "",
            (
                "Outbound means a foreign key on the fact. Inbound means another dataset carries "
                "that fact's identity. The full population and every join are in `statistics.md` "
                "and `statistics.json`."
            ),
            "",
        ]
    )
    for fact in report["major_facts"]:
        lines.append(f"### `{fact['dataset']}`")
        lines.append("")
        lines.append(fact["landing"].strip())
        lines.append("")
        lines.append(f"Rows: `{_int(fact['rows'])}`.")
        lines.append("")
        lines.append("Outbound:")
        lines.append("")
        lines.extend(_join_table(fact["outbound"], inbound=False))
        lines.append("Inbound:")
        lines.append("")
        lines.extend(_join_table(fact["inbound"], inbound=True))
    return "\n".join(lines)
