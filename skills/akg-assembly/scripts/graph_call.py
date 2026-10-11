#!/usr/bin/env python3
"""Call the Data Ontology Graph service over its JSON-RPC 2.0 Unix-domain socket.

Standard library only; does not import actor code.

    graph_call.py METHOD [PARAMS_JSON] [--socket PATH] [--full [--records]]

The socket comes from --socket or $DOG_SOCKET. The client changes into the socket's directory and
connects by basename, so socket paths longer than the platform sun_path limit still work.
The service returns graph-object collections as {"header", "rows"} tables. By default the result
is printed in a compact projection that joins hop and path steps with their relationships and drops
dataset metadata; --full prints the raw JSON-RPC result, and --full --records converts each table
to a list of records (dotted column names become nested objects). In the compact projection,
find_paths results are re-sorted: paths with no fan-out hop (1:many or many:many) first, then
fewer hops with unknown claims, then shorter paths. Each path carries its direction `shape`.
"""
from __future__ import annotations

import argparse
import json
import os
import socket
import sys
from pathlib import Path


def call(socket_path: Path, method: str, params: dict) -> dict:
    request = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
    cwd = os.getcwd()
    os.chdir(socket_path.parent)
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as conn:
            conn.connect(socket_path.name)
            conn.sendall(json.dumps(request).encode() + b"\n")
            buf = b""
            while b"\n" not in buf:
                chunk = conn.recv(65536)
                if not chunk:
                    raise ConnectionError("service closed the connection")
                buf += chunk
    finally:
        os.chdir(cwd)
    return json.loads(buf.split(b"\n", 1)[0])


def to_records(table: dict) -> list[dict]:
    """Convert one {"header", "rows"} table to records, nesting dotted column names."""
    records = []
    for row in table["rows"]:
        if len(row) != len(table["header"]):
            raise ValueError(f"row has {len(row)} values for {len(table['header'])} columns")
        record: dict = {}
        for column, value in zip(table["header"], row):
            *parents, leaf = column.split(".")
            target = record
            for parent in parents:
                target = target.setdefault(parent, {})
            target[leaf] = value
        records.append(record)
    return records


def expand_tables(result):
    """Replace every table in a result with its records; other values are unchanged."""
    if isinstance(result, dict):
        if set(result) == {"header", "rows"}:
            return to_records(result)
        return {key: expand_tables(value) for key, value in result.items()}
    if isinstance(result, list):
        return [expand_tables(value) for value in result]
    return result


def _endpoint(result: dict, ref: dict, identity_id: str) -> dict:
    """Resolve an endpoint against the response's datasets and entity definitions."""
    dataset = next(d for d in result["datasets"] if d["node_id"] == ref["node_id"])
    definition = next(
        d for d in result["entity_definitions"]
        if (d["node_id"], d["identity_id"], d["dataset_columns"])
        == (ref["node_id"], identity_id, ref["dataset_columns"])
    )
    return {
        "node_id": ref["node_id"],
        "qualified_name": dataset["descriptor"]["qualified_name"],
        "dataset_columns": ref["dataset_columns"],
        "entity_universe": definition["entity_universe"],
        "entity_expression": definition["entity_expression"],
        "entity_metadata": definition["entity_metadata"],
    }


def _columns(relationship: dict, node_id: str) -> list[str]:
    for side in ("endpoint_a", "endpoint_b"):
        if relationship[side]["node_id"] == node_id:
            return relationship[side]["dataset_columns"]
    raise KeyError(node_id)


def _hop(relationships: dict, step: dict) -> dict:
    """A step joined with its relationship's identity and endpoint columns."""
    relationship = relationships[step["edge_id"]]
    return {
        "edge_id": step["edge_id"],
        "from": f'{step["from_node_id"]}[{",".join(_columns(relationship, step["from_node_id"]))}]',
        "to": f'{step["to_node_id"]}[{",".join(_columns(relationship, step["to_node_id"]))}]',
        "identity_id": relationship["identity_id"],
        "direction": step["direction"],
        "reverse_direction": step["reverse_direction"],
        **({"unknown_fields": step["unknown_fields"]} if step["unknown_fields"] else {}),
    }


def compact(method: str, result):
    if method == "graph.search":
        # Search rows are already compact: header-keyed subject and match tables per kind.
        return {
            "normalized_query": result["normalized_query"],
            "truncated": result["truncated"],
            "groups": result["groups"],
        }
    result = expand_tables(result)
    relationships = {r["edge_id"]: r for r in result.get("relationships", [])}
    if method == "graph.get_hops":
        return {"truncated": result["truncated"],
                "hops": [_hop(relationships, step) for step in result["hops"]]}
    if method == "graph.get_relationship":
        compacted = {key: value for key, value in result.items()
                     if key not in ("datasets", "entity_definitions")}
        for side in ("endpoint_a", "endpoint_b"):
            compacted[side] = _endpoint(result, result[side], result["identity_id"])
        return compacted
    if method == "graph.find_paths":
        grouped: list[list[dict]] = []
        for step in result["hops"]:
            if step["path"] == len(grouped):
                grouped.append([])
            grouped[step["path"]].append(step)
        paths = []
        for steps in grouped:
            directions = [step["direction"]["multiplicity"] for step in steps]
            paths.append({
                "length": len(steps),
                "shape": " > ".join(directions),
                "fan_out_hops": sum(m in ("1:many", "many:many") for m in directions),
                "unknown_hops": sum(bool(step["unknown_fields"]) for step in steps),
                "hops": [_hop(relationships, step) for step in steps],
            })
        # Fan-out-free chains first, then fewer unknown hops, then the service order.
        paths.sort(key=lambda p: (p["fan_out_hops"], p["unknown_hops"], p["length"]))
        return {"truncated": result["truncated"], "path_count": len(paths), "paths": paths}
    if method == "graph.expand_subgraph":
        return {
            "truncated": result["truncated"],
            "nodes": [
                {"distance": d["distance"], "node_id": d["node_id"],
                 "display_name": d["descriptor"]["display_name"],
                 "description": d["descriptor"]["description"]}
                for d in result["datasets"]
            ],
            "edges": [
                {"edge_id": edge_id, "identity_id": e["identity_id"],
                 "a": f'{e["endpoint_a"]["node_id"]}[{",".join(e["endpoint_a"]["dataset_columns"])}]',
                 "b": f'{e["endpoint_b"]["node_id"]}[{",".join(e["endpoint_b"]["dataset_columns"])}]',
                 "a_to_b": e["a_to_b"], "b_to_a": e["b_to_a"]}
                for edge_id, e in relationships.items()
            ],
        }
    if method == "graph.get_identity":
        names = {d["node_id"]: d["descriptor"]["qualified_name"] for d in result["datasets"]}
        return {**{k: v for k, v in result.items() if k not in ("datasets", "entity_definitions")},
                "definitions": [
                    {"node_id": d["node_id"], "qualified_name": names[d["node_id"]],
                     "dataset_columns": d["dataset_columns"],
                     "entity_universe": d["entity_universe"]}
                    for d in result["entity_definitions"]]}
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("method")
    parser.add_argument("params", nargs="?", default="{}")
    parser.add_argument("--socket", default=os.environ.get("DOG_SOCKET"))
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--records", action="store_true",
                        help="with --full, convert each table to a list of records")
    args = parser.parse_args()
    if not args.socket:
        parser.error("set --socket or DOG_SOCKET")
    method = args.method if args.method.startswith("graph.") else f"graph.{args.method}"
    response = call(Path(args.socket).expanduser().resolve(), method, json.loads(args.params))
    if "error" in response:
        print(json.dumps(response["error"], indent=1))
        sys.exit(1)
    result = response["result"]
    if args.full:
        output = expand_tables(result) if args.records else result
    else:
        output = compact(method, result)
    print(json.dumps(output, indent=1))


if __name__ == "__main__":
    main()
