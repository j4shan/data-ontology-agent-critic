#!/usr/bin/env python3
"""Call the Data Ontology Graph service over its JSON-RPC 2.0 Unix-domain socket.

Standard library only; does not import actor code.

    graph_call.py METHOD [PARAMS_JSON] [--socket PATH] [--full]

The socket comes from --socket or $DOG_SOCKET. The client changes into the socket's directory and
connects by basename, so socket paths longer than the platform sun_path limit still work.
By default the result is printed in a compact projection that drops repeated snapshot headers and
nested dataset copies; --full prints the raw JSON-RPC result. In the compact projection,
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


def _endpoint(ep: dict) -> dict:
    return {
        "node_id": ep.get("node_id"),
        "qualified_name": ep.get("dataset", {}).get("descriptor", {}).get("qualified_name"),
        "identity_id": ep.get("identity_id"),
        "dataset_columns": ep.get("dataset_columns"),
        "entity_universe": ep.get("entity_universe"),
        "entity_expression": ep.get("entity_expression"),
        "entity_metadata": ep.get("entity_metadata"),
    }


def compact(method: str, result):
    if method == "graph.search":
        # Search rows are already compact: header-keyed subject and match tables per kind.
        return {
            "normalized_query": result["normalized_query"],
            "truncated": result["truncated"],
            "groups": result["groups"],
        }
    if method == "graph.get_hops":
        hops = [
            {
                "edge_id": h["edge_id"],
                "to_node_id": h["to_node_id"],
                "identity_id": h["identity_id"],
                "from_columns": h["from_endpoint"]["dataset_columns"],
                "to_columns": h["to_endpoint"]["dataset_columns"],
                "direction": h["direction"],
                "reverse_direction": h["reverse_direction"],
                **({"unknown_fields": h["unknown_fields"]} if h["unknown_fields"] else {}),
            }
            for h in result["hops"]
        ]
        return {"truncated": result["truncated"], "hops": hops}
    if method == "graph.get_relationship":
        return {**result, "endpoint_a": _endpoint(result["endpoint_a"]),
                "endpoint_b": _endpoint(result["endpoint_b"])}
    if method == "graph.find_paths":
        paths = [
                {
                    "length": p["length"],
                    "shape": " > ".join(h["direction"]["multiplicity"] for h in p["hops"]),
                    "fan_out_hops": sum(
                        h["direction"]["multiplicity"] in ("1:many", "many:many") for h in p["hops"]
                    ),
                    "unknown_hops": sum(bool(h["unknown_fields"]) for h in p["hops"]),
                    "hops": [
                        {
                            "edge_id": h["edge_id"],
                            "from": f'{h["from_node_id"]}[{",".join(h["from_endpoint"]["dataset_columns"])}]',
                            "to": f'{h["to_node_id"]}[{",".join(h["to_endpoint"]["dataset_columns"])}]',
                            "identity_id": h["identity_id"],
                            "direction": h["direction"],
                        }
                        for h in p["hops"]
                    ],
                }
                for p in result["paths"]
            ]
        # Fan-out-free chains first, then fewer unknown hops, then the service order.
        paths.sort(key=lambda p: (p["fan_out_hops"], p["unknown_hops"], p["length"]))
        return {"truncated": result["truncated"], "path_count": len(paths), "paths": paths}
    if method == "graph.expand_subgraph":
        return {
            "truncated": result["truncated"],
            "nodes": [
                {"distance": n["distance"], "node_id": n["dataset"]["node_id"],
                 "display_name": n["dataset"]["descriptor"]["display_name"],
                 "description": n["dataset"]["descriptor"]["description"]}
                for n in result["nodes"]
            ],
            "edges": [
                {"edge_id": e["edge_id"], "identity_id": e["identity_id"],
                 "a": f'{e["endpoint_a"]["node_id"]}[{",".join(e["endpoint_a"]["dataset_columns"])}]',
                 "b": f'{e["endpoint_b"]["node_id"]}[{",".join(e["endpoint_b"]["dataset_columns"])}]',
                 "a_to_b": e["a_to_b"], "b_to_a": e["b_to_a"]}
                for e in result["edges"]
            ],
        }
    if method == "graph.get_identity":
        return {**result, "definitions": [
            {"node_id": d["node_id"],
             "qualified_name": d["dataset"]["descriptor"]["qualified_name"],
             "dataset_columns": d["dataset_columns"], "entity_universe": d["entity_universe"]}
            for d in result["definitions"]]}
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("method")
    parser.add_argument("params", nargs="?", default="{}")
    parser.add_argument("--socket", default=os.environ.get("DOG_SOCKET"))
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()
    if not args.socket:
        parser.error("set --socket or DOG_SOCKET")
    method = args.method if args.method.startswith("graph.") else f"graph.{args.method}"
    response = call(Path(args.socket).expanduser().resolve(), method, json.loads(args.params))
    if "error" in response:
        print(json.dumps(response["error"], indent=1))
        sys.exit(1)
    result = response["result"]
    print(json.dumps(result if args.full else compact(method, result), indent=1))


if __name__ == "__main__":
    main()
