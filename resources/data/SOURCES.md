# Test data sources

Vendored sources are local only and are not committed. This file records where each came from and
the SHA-256 of the files the `financial` suite depends on.

## BIRD Mini-Dev

| Local path | Origin | Committed |
| --- | --- | --- |
| `dev_databases/<database>/` | BIRD Mini-Dev SQLite databases and `database_description/` CSVs, moved from `data-ontology-graph/resources/data/dev_databases/` on 2026-09-25. | No |
| `bird_minidev/mini_dev_sqlite.json` | BIRD Mini-Dev SQLite question set, 500 questions (32 `financial`), copied from `text-to-sql-agent/resources/MINIDE/`. | No |
| `bird_minidev/mini_dev_sqlite_gold.sql` | BIRD Mini-Dev SQLite gold SQL, same origin. | No |

Upstream release: BIRD Mini-Dev (<https://github.com/bird-bench/mini_dev>).

### `financial` hashes

```
d15d89cdb068a202b6f2b99342af44dffc1d52545b39ceaf62efdc0ba570101e  dev_databases/financial/financial.sqlite
98f9b72619c30593fadc013efc668d081193f34f2bda1353214c48c8013f03b3  dev_databases/financial/database_description/account.csv
1dd79bf48c7696a5e6c3fc4835c9994b129f58307ad75c2f874f9cd1078fe300  dev_databases/financial/database_description/card.csv
d1ef6f74b4730737517307c2f3b219496af264d83fe3e34f435c078b368dd800  dev_databases/financial/database_description/client.csv
3b7ade14650a78e7122fdf4f423c4dae241e923d73039c65e5e85b7ac7919ffe  dev_databases/financial/database_description/disp.csv
6da804294fe9e7f9f8285759b842e39e0c5c8cb10390a93d5e292c2cb28fdc48  dev_databases/financial/database_description/district.csv
e6f4c7393d3973c9647913206ec4da2b9480bca4a8fb1ed45f4d42c433112756  dev_databases/financial/database_description/loan.csv
d01db89f3121b96a8c5876108d835ad0ab8d8bd5e132d9d823d384ae12706476  dev_databases/financial/database_description/order.csv
59efafabbb4347853f29ebfc14fdd18633f724a669e7e26cb7b2ecd628d6c4a2  dev_databases/financial/database_description/trans.csv
def4b2b43a9b06955193418f24c9be170eb6d83763ab702311790e0cdda8c791  bird_minidev/mini_dev_sqlite.json
9089b50f2cfea1a7223f5f5019f0677bd9c6ddd61065dd00b6f0238549394976  bird_minidev/mini_dev_sqlite_gold.sql
```

## Authored assets (committed)

| Path | Content |
| --- | --- |
| `reference_catalogs/<database>/catalog.yaml` | Reviewed finalized YAML for the actor's builder. Each directory holds only that catalog's YAML, so it builds as a finalized directory. |
| `legacy_overlays/<database>/` | Pre-YAML overlay and annotation JSON from the actor repository. Authoring notes only; the actor builder does not accept them. |
