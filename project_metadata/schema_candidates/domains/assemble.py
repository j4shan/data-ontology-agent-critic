"""Turn compact dataset specs into catalog datasets with consistent join rules."""

from __future__ import annotations

from domains.dsl import col, pk, ref, status, table

_IRREGULAR = {
    "address": "addresses",
    "facility": "facilities",
    "taxonomy": "taxonomies",
}


def singular(display: str) -> str:
    return display[:1].lower() + display[1:]


def plural(display: str) -> str:
    text = singular(display)
    if text in _IRREGULAR:
        return _IRREGULAR[text]
    if text.endswith(("s", "x", "z", "ch", "sh")):
        return text + "es"
    if text.endswith("y") and len(text) > 1 and text[-2] not in "aeiou":
        return text[:-1] + "ies"
    return text + "s"


def _rule(child: str, parent: str, kind: str, because: str) -> str:
    child_one = singular(child)
    parent_one = singular(parent)
    child_many = plural(child)
    parent_many = plural(parent)
    if kind == "n1":
        sentence = (
            f"Many {child_many} belong to one {parent_one}, every {child_one} matches a "
            f"{parent_one}, and a {parent_one} may include no {child_one}."
        )
    elif kind == "n1!":
        sentence = (
            f"Many {child_many} belong to one {parent_one}, every {child_one} matches a "
            f"{parent_one}, and every {parent_one} includes at least one {child_one}."
        )
    elif kind == "n1?":
        sentence = (
            f"A {child_one} may match one {parent_one}, and a {parent_one} may include no "
            f"{child_one}."
        )
    elif kind == "11":
        sentence = (
            f"Each {child_one} matches exactly one {parent_one}, each {parent_one} matches "
            f"at most one {child_one}, and not every {parent_one} is matched."
        )
    elif kind == "11!":
        sentence = (
            f"Each {child_one} matches exactly one {parent_one}, and each {parent_one} "
            f"matches exactly one {child_one}."
        )
    elif kind == "11?":
        sentence = (
            f"A {child_one} may match one {parent_one}, and a {parent_one} may match one "
            f"{child_one}."
        )
    else:
        raise ValueError(f"unknown kind {kind}")
    if because:
        sentence = f"{sentence} {because.strip()}"
    return sentence


def link(
    column: str,
    parent: str,
    kind: str = "n1",
    because: str = "",
    *,
    coverage: float | None = None,
    match_rate: float | None = None,
    matched_rows: int | None = None,
) -> dict:
    return {
        "column": column,
        "parent": parent,
        "kind": kind,
        "because": because,
        "coverage": coverage,
        "match_rate": match_rate,
        "matched_rows": matched_rows,
    }


def measure(name: str, description: str, codes: str = "") -> dict:
    return {"name": name, "description": description, "codes": codes}


def spec(
    subject: str,
    name: str,
    role: str,
    display: str,
    description: str,
    rows: int,
    links: tuple | list = (),
    measures: tuple | list = (),
    synonyms: tuple | list = (),
    volume_class: str = "",
    grain_rule: str = "",
) -> dict:
    return {
        "subject": subject,
        "name": name,
        "role": role,
        "display": display,
        "description": description,
        "rows": rows,
        "links": list(links),
        "measures": list(measures),
        "synonyms": list(synonyms),
        "volume_class": volume_class,
        "grain_rule": grain_rule,
    }


def _stem(name: str) -> str:
    for prefix in ("dim_", "fact_", "bridge_"):
        if name.startswith(prefix):
            return name[len(prefix) :]
    raise ValueError(f"{name} must start with dim_, fact_, or bridge_")


def build_datasets(specs: list[dict]) -> list[dict]:
    by_name = {item["name"]: item for item in specs}
    if len(by_name) != len(specs):
        raise ValueError("duplicate dataset name in spec")
    displays = {item["name"]: item["display"] for item in specs}
    datasets = []
    for item in specs:
        stem = _stem(item["name"])
        identity = f"{stem}_identity"
        columns = [
            pk(
                f"{stem}_id",
                identity,
                f"Identifier of one {singular(item['display'])}.",
                rule=item.get("grain_rule", ""),
            )
        ]
        seen = {columns[0]["name"]}
        for fk in item["links"]:
            parent = by_name[fk["parent"]]
            parent_stem = _stem(parent["name"])
            if fk["column"] in seen:
                raise ValueError(f"{item['name']} duplicate column {fk['column']}")
            seen.add(fk["column"])
            if fk["parent"] == item["name"]:
                raise ValueError(f"{item['name']} self-references")
            kind = fk["kind"]
            child_rows = item["rows"]
            parent_rows = parent["rows"]
            if kind == "n1!" and child_rows < parent_rows:
                raise ValueError(
                    f"{item['name']} -> {parent['name']} n1! has {child_rows} < {parent_rows}"
                )
            if kind == "11!" and child_rows != parent_rows:
                raise ValueError(
                    f"{item['name']} -> {parent['name']} 11! rows {child_rows} != {parent_rows}"
                )
            if kind == "11" and child_rows > parent_rows:
                raise ValueError(
                    f"{item['name']} -> {parent['name']} 11 has {child_rows} > {parent_rows}"
                )
            if fk["coverage"] is not None and kind in {"n1!", "11!"}:
                raise ValueError(f"{item['name']}.{fk['column']} coverage on required parent")
            if (fk["match_rate"] is not None or fk["matched_rows"] is not None) and kind in {
                "n1",
                "n1!",
                "11",
                "11!",
            }:
                raise ValueError(f"{item['name']}.{fk['column']} match override on required child")
            because = fk["because"]
            columns.append(
                ref(
                    fk["column"],
                    f"{parent_stem}_identity",
                    because or f"Reference to the {singular(displays[parent['name']])}.",
                    _rule(item["display"], parent["display"], kind, because),
                    kind,
                    coverage=fk["coverage"],
                    match_rate=fk["match_rate"],
                    matched_rows=fk["matched_rows"],
                )
            )
        for measure_item in item["measures"]:
            if measure_item["name"] in seen:
                raise ValueError(f"{item['name']} duplicate column {measure_item['name']}")
            seen.add(measure_item["name"])
            if measure_item["codes"]:
                columns.append(
                    status(measure_item["name"], measure_item["description"], measure_item["codes"])
                )
            else:
                columns.append(col(measure_item["name"], measure_item["description"]))
        datasets.append(
            table(
                item["subject"],
                item["name"],
                item["role"],
                item["display"],
                item["description"],
                columns,
                item["synonyms"],
                rows=item["rows"],
                volume_class=item["volume_class"]
                or ("transaction" if item["role"] == "fact" else ""),
            )
        )
    return datasets
