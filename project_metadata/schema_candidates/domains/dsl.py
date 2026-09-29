"""Compact constructors for ontology catalog datasets.

Relationship kinds, read from the child dataset toward the population universe:

- n1: many children share one parent; every child matches; a parent may have no children.
- n1!: same as n1, and every parent row has at least one child.
- n1?: the child reference may be absent; a parent may have no children.
- 11: one child matches one parent; every child matches; a parent may have no child.
- 11!: one-to-one in both directions, and both sides always match.
- 11?: one-to-one, and either side may be unmatched.
"""

from __future__ import annotations

_KINDS = {
    "n1": ("many:1", "always", "1:many", "optional"),
    "n1!": ("many:1", "always", "1:many", "always"),
    "n1?": ("many:1", "optional", "1:many", "optional"),
    "11": ("1:1", "always", "1:1", "optional"),
    "11!": ("1:1", "always", "1:1", "always"),
    "11?": ("1:1", "optional", "1:1", "optional"),
}


def pk(name: str, identity: str, description: str, *, rule: str = "") -> dict:
    return {
        "name": name,
        "description": description,
        "identity": identity,
        "universe": True,
        "business_rule": rule,
    }


def col(name: str, description: str, *, value_description: str = "") -> dict:
    column = {"name": name, "description": description}
    if value_description:
        column["value_description"] = value_description
    return column


def status(name: str, description: str, codes: str) -> dict:
    return col(name, description, value_description=codes)


def ref(name: str, identity: str, description: str, rule: str, kind: str = "n1") -> dict:
    if kind not in _KINDS:
        raise ValueError(f"unknown relationship kind {kind!r} on {name}")
    child_mult, child_exist, parent_mult, parent_exist = _KINDS[kind]
    if parent_mult == "1:many":
        mapping = "1:N"
    elif parent_mult == "1:1":
        mapping = "1:1"
    else:
        mapping = parent_mult
    return {
        "name": name,
        "description": description,
        "identity": identity,
        "universe": False,
        "to_universe_multiplicity": child_mult,
        "to_universe_existence": child_exist,
        "from_universe_multiplicity": parent_mult,
        "from_universe_existence": parent_exist,
        "mapping": mapping,
        "business_rule": rule,
    }


def table(
    subject: str,
    name: str,
    role: str,
    display: str,
    description: str,
    columns: list[dict],
    synonyms: list[str] | None = None,
) -> dict:
    if role not in {"dimension", "fact", "bridge"}:
        raise ValueError(f"{name} has role {role!r}")
    return {
        "subject": subject,
        "name": name,
        "role": role,
        "display_name": display,
        "description": description,
        "columns": columns,
        "synonyms": list(synonyms or []),
    }
