"""Load each candidate with the Data Ontology Graph service and record evidence."""

from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

DOG_SRC = Path("/agent/repos/data-ontology-graph/src")
sys.path.insert(0, str(DOG_SRC))
os.environ["PYTHONPATH"] = str(DOG_SRC) + os.pathsep + os.environ.get("PYTHONPATH", "")

from data_ontology_graph.builder import build_snapshot_from_yaml, detect_contradictions
from data_ontology_graph.rpc.client import call

ROOT = Path(__file__).resolve().parent
ARTIFACTS = Path("/opt/cursor/artifacts")
PYTHON = "python3"
CASES = {
    "manufacturing-discrete": {
        "search": "plant manager",
        "dataset": "sf:manufacturing-discrete.organization.dim_plant",
        "hops_from": "sf:manufacturing-discrete.organization.dim_plant",
        "expected_hops": [
            ("sf:manufacturing-discrete.organization.dim_area", "1:many", "always"),
        ],
        "path": (
            "sf:manufacturing-discrete.organization.dim_plant",
            "sf:manufacturing-discrete.organization.dim_work_unit",
        ),
    },
    "retail-grocery": {
        "search": "cashier",
        "dataset": "sf:retail-grocery.organization.dim_store",
        "hops_from": "sf:retail-grocery.organization.dim_store",
        "expected_hops": [
            ("sf:retail-grocery.storefront.dim_cashier", "1:many", "always"),
            ("sf:retail-grocery.organization.dim_employee", "1:1", "always"),
        ],
        "path": (
            "sf:retail-grocery.storefront.dim_cashier",
            "sf:retail-grocery.pos.fact_pos_line",
        ),
    },
    "commerce-marketplace": {
        "search": "storefront",
        "dataset": "sf:commerce-marketplace.party.dim_seller",
        "hops_from": "sf:commerce-marketplace.party.dim_seller",
        "expected_hops": [
            ("sf:commerce-marketplace.party.dim_seller_storefront", "1:many", "always"),
            ("sf:commerce-marketplace.party.dim_employee", "1:1", "always"),
        ],
        "path": (
            "sf:commerce-marketplace.party.dim_seller_storefront",
            "sf:commerce-marketplace.order.fact_order_line",
        ),
    },
    "telecom-mobile": {
        "search": "subscriber",
        "dataset": "sf:telecom-mobile.party.dim_subscriber",
        "hops_from": "sf:telecom-mobile.organization.dim_market",
        "expected_hops": [
            ("sf:telecom-mobile.network.dim_cell_site", "1:many", "always"),
            ("sf:telecom-mobile.organization.dim_employee", "1:1", "always"),
        ],
        "path": (
            "sf:telecom-mobile.party.dim_subscriber",
            "sf:telecom-mobile.usage.fact_voice_cdr",
        ),
    },
    "healthcare-payer": {
        "search": "provider",
        "dataset": "sf:healthcare-payer.provider.dim_provider",
        "hops_from": "sf:healthcare-payer.claim.fact_claim_header",
        "expected_hops": [
            ("sf:healthcare-payer.claim.fact_claim_line", "1:many", "always"),
            ("sf:healthcare-payer.claim.fact_claim_diagnosis", "1:many", "always"),
        ],
        "path": (
            "sf:healthcare-payer.provider.dim_provider",
            "sf:healthcare-payer.claim.fact_claim_line",
        ),
    },
}


def _wait_for_socket(path: Path, timeout: float = 20) -> None:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if path.exists():
            try:
                with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
                    client.settimeout(1)
                    client.connect(str(path))
                return
            except OSError:
                pass
        time.sleep(0.2)
    raise TimeoutError(f"socket not ready: {path}")


def _start_server(domain: str, artifact: Path, sock: Path) -> None:
    session = f"dog-{domain}"
    if sock.exists():
        sock.unlink()
    command = (
        f"PYTHONPATH={DOG_SRC} {PYTHON} -m data_ontology_graph.rpc.server "
        f"--snapshot-dir {artifact} --socket {sock}"
    )
    subprocess.run(
        ["tmux", "-f", "/exec-daemon/tmux.portal.conf", "kill-session", "-t", session],
        check=False,
        capture_output=True,
    )
    subprocess.check_call(
        [
            "tmux",
            "-f",
            "/exec-daemon/tmux.portal.conf",
            "new-session",
            "-d",
            "-s",
            session,
            command,
        ]
    )
    _wait_for_socket(sock)


def _universe_report(snapshot) -> dict:
    coverage: dict[str, list[bool]] = defaultdict(list)
    for node in snapshot.nodes:
        for definition in node.entity_definitions:
            coverage[definition.identity_id].append(definition.is_entity_universe)
    incomplete = sorted(
        identity
        for identity, flags in coverage.items()
        if sum(1 for flag in flags if flag) != 1
    )
    return {
        "identity_count": len(coverage),
        "identities_missing_single_universe": incomplete,
    }


def exercise(domain: str) -> dict:
    spec = CASES[domain]
    yaml_dir = ROOT / domain / "yaml"
    artifact = Path(f"/tmp/dog-artifacts/{domain}")
    sock = Path(f"/tmp/dog-{domain}.sock")
    snapshot, report, _ = build_snapshot_from_yaml(yaml_dir)
    contradictions = detect_contradictions(list(snapshot.edges))
    universe = _universe_report(snapshot)
    publish = subprocess.run(
        [
            PYTHON,
            "-m",
            "data_ontology_graph.builder.publish",
            "--yaml-dir",
            str(yaml_dir),
            "--artifact-dir",
            str(artifact),
        ],
        check=True,
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONPATH": str(DOG_SRC)},
    )
    _start_server(domain, artifact, sock)
    info = call(sock, "graph.snapshot_info", {})
    search = call(sock, "graph.search", {"query": spec["search"], "limit": 10})
    dataset = call(sock, "graph.get_dataset", {"node_id": spec["dataset"]})
    hops = call(sock, "graph.get_hops", {"node_id": spec["hops_from"]})
    paths = call(
        sock,
        "graph.find_paths",
        {
            "from_node_id": spec["path"][0],
            "to_node_id": spec["path"][1],
            "max_hops": 4,
            "limit": 5,
        },
    )
    hop_rows = hops["result"]
    expectations = []
    for target, multiplicity, existence in spec["expected_hops"]:
        match = next((row for row in hop_rows if row["to_node_id"] == target), None)
        expectations.append(
            {
                "to_node_id": target,
                "found": match is not None,
                "multiplicity": None if match is None else match["direction"]["multiplicity"],
                "match_existence": None if match is None else match["direction"]["match_existence"],
                "expected_multiplicity": multiplicity,
                "expected_existence": existence,
            }
        )
    store_definitions = dataset["result"]["entity_definitions"]
    return {
        "domain": domain,
        "build": {
            "node_count": report.node_count,
            "edge_count": report.edge_count,
            "contradictions": len(contradictions),
            **universe,
        },
        "publish_stdout": publish.stdout.strip(),
        "snapshot_info": info["result"],
        "search_query": spec["search"],
        "search_hit_count": len(search["result"]["hits"]),
        "search_labels": [hit["subject"]["label"] for hit in search["result"]["hits"][:8]],
        "dataset_node": dataset["result"]["node_id"],
        "universe_flags": [
            {
                "identity_id": item["identity_id"],
                "columns": item["dataset_columns"],
                "is_entity_universe": item["is_entity_universe"],
            }
            for item in store_definitions
        ],
        "hop_checks": expectations,
        "hop_count": len(hop_rows),
        "path_count": len(paths["result"]["paths"]),
        "shortest_path": paths["result"]["paths"][0]["hops"] if paths["result"]["paths"] else [],
        "errors": [
            info.get("error"),
            search.get("error"),
            dataset.get("error"),
            hops.get("error"),
            paths.get("error"),
        ],
    }


def _check_statistics() -> list[str]:
    failures = []
    telecom = json.loads((ROOT / "telecom-mobile" / "statistics.json").read_text(encoding="utf-8"))
    payer = json.loads((ROOT / "healthcare-payer" / "statistics.json").read_text(encoding="utf-8"))
    by_name = {item["dataset"]: item for item in telecom["populations"]}
    mediated = (
        by_name["fact_data_cdr"]["rows"]
        + by_name["fact_voice_cdr"]["rows"]
        + by_name["fact_sms_cdr"]["rows"]
        + by_name["fact_content_cdr"]["rows"]
    )
    if mediated != 2_100_000_000:
        failures.append("telecom-mobile mediated CDR total")
    if by_name["fact_cell_counter"]["rows"] != 85_000 * 96 * 30:
        failures.append("telecom-mobile cell counter grid")
    if by_name["fact_charging_event"]["rows"] != 6_300_000_000:
        failures.append("telecom-mobile charging events")
    payer_rows = {item["dataset"]: item["rows"] for item in payer["populations"]}
    if payer_rows["dim_member"] != 68_000_000 or payer_rows["fact_claim_header"] != 84_000_000:
        failures.append("healthcare-payer CMS-scale anchors")
    if payer_rows["fact_claim_line"] != 420_000_000:
        failures.append("healthcare-payer claim line fan-out")
    line = next(item for item in payer["major_facts"] if item["dataset"] == "fact_claim_line")
    header_join = next(item for item in line["outbound"] if item["column"] == "claim_header_id")
    if header_join["distinct_parent_keys"] != 84_000_000 or header_join["avg_children_per_matched_parent"] != 5:
        failures.append("healthcare-payer header-to-line join")
    if not line["inbound"]:
        failures.append("healthcare-payer claim line inbound")
    voice = next(item for item in telecom["major_facts"] if item["dataset"] == "fact_voice_cdr")
    if not voice["outbound"] or not voice["inbound"]:
        failures.append("telecom-mobile voice joins")
    return failures


def main() -> None:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    stat_failures = _check_statistics()
    results = [exercise(domain) for domain in CASES]
    destination = ARTIFACTS / "dog-service-exercise.json"
    destination.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    failures = list(stat_failures)
    for result in results:
        build = result["build"]
        if build["node_count"] < 100 or build["contradictions"] or build["identities_missing_single_universe"]:
            failures.append(result["domain"] + " build")
        if result["snapshot_info"]["node_count"] != build["node_count"]:
            failures.append(result["domain"] + " snapshot")
        if any(result["errors"]):
            failures.append(result["domain"] + " rpc")
        if result["search_hit_count"] < 1 or result["path_count"] < 1:
            failures.append(result["domain"] + " navigation")
        for hop in result["hop_checks"]:
            if (
                not hop["found"]
                or hop["multiplicity"] != hop["expected_multiplicity"]
                or hop["match_existence"] != hop["expected_existence"]
            ):
                failures.append(result["domain"] + " hop " + hop["to_node_id"])
    print(json.dumps({"failures": failures, "domains": [item["domain"] for item in results]}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
