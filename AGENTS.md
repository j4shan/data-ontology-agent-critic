# Agent instructions

## Independence from the actor

Critic evaluates an actor project, initially `../data-ontology-graph`. Do not import actor code,
copy actor internals into Critic, or reference actor graph identifiers (`node_id`, `edge_id`) in
suites, gold AKGs, or submissions. Use data-source terms: qualified dataset names and columns.
The actor location, artifact location, and socket path are always configurable inputs.

## Catalog asset isolation

Authored assets that belong to one BIRD Mini-Dev catalog must not share a file with another
catalog. `<database>` is the directory name under `resources/data/dev_databases/`.

- Reference YAML: `resources/data/reference_catalogs/<database>/`. The directory holds only that
  catalog's `.yaml` files, so it builds as a finalized actor YAML directory.
- Legacy overlay notes: `resources/data/legacy_overlays/<database>/`.
- Suites and gold AKGs are also organized per catalog.
- Never write into the vendored `resources/data/dev_databases/` or `resources/data/bird_minidev/`
  trees.
- Current catalogs are `financial` (first suite) and `student_club` (legacy notes only). Do not
  introduce `superhero` or `toxicology` assets.

## Cursor Cloud specific instructions

The image provides Python 3.12 and SQLite. Environment setup installs uv 0.12.19 onto `PATH` at
`/usr/local/bin`. This repository has no application server and no Python package yet, so setup
does not start a long-running process. There is no `pyproject.toml`, lockfile, or pytest suite
until framework code lands.

BIRD Mini-Dev SQLite catalogs and question files stay outside git. Provenance and hashes are in
`resources/data/SOURCES.md`. A checkout leaves `resources/data/dev_databases/` and
`resources/data/bird_minidev/` absent until a fetch script exists. The financial catalog's SQLite
accessor path is `resources/data/dev_databases/financial/financial.sqlite`.

Load the committed financial reference catalog and legacy overlay JSON with:

```bash
uv run --with pyyaml python - <<'PY'
import json
from pathlib import Path
import yaml

catalog = yaml.safe_load(
    Path("resources/data/reference_catalogs/financial/catalog.yaml").read_text()
)
names = [node["descriptor"]["qualified_name"] for node in catalog["nodes"]]
assert catalog["schema_version"] == "2"
assert len(names) == 8 and catalog["edges"]
for path in Path("resources/data/legacy_overlays").rglob("*.json"):
    json.loads(path.read_text())
print(catalog["schema_version"], len(names), len(catalog["edges"]))
PY
```
