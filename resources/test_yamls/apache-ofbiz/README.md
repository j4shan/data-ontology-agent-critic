# Apache OFBiz

`apache-ofbiz` is a schema version 4 catalog of the Apache OFBiz tables on PostgreSQL. Each
dataset is one OFBiz entity table in the `public` schema of the `ofbiz` database, or of the
`ofbiztenant` database for the 6 tenant entities. Column names are the physical column names.

## Source

Apache OFBiz framework commit `5dd66dd617a1fc7435e893a209d9b7ca97827394`, 23 `entitymodel` files.
The test entity model, the entity model template, and the 270 view-entities are not in the
catalog.

## Counts

| Measure | Count |
| --- | ---: |
| Datasets | 835 |
| Columns | 8,694 |
| Logical identities | 835 |
| Entity definitions | 2,030 |

| File | Datasets | File | Datasets |
| --- | ---: | --- | ---: |
| `product.yaml` | 169 | `entity.yaml` | 10 |
| `accounting.yaml` | 147 | `service.yaml` | 10 |
| `order.yaml` | 112 | `manufacturing.yaml` | 8 |
| `party.yaml` | 84 | `entityext.yaml` | 7 |
| `content.yaml` | 64 | `catalina.yaml` | 1 |
| `common.yaml` | 48 | `webtools.yaml` | 1 |
| `humanres.yaml` | 41 | | |
| `workeffort.yaml` | 41 | | |
| `shipment.yaml` | 35 | | |
| `marketing.yaml` | 32 | | |
| `webapp.yaml` | 14 | | |
| `security.yaml` | 11 | | |

`forget-log.yaml` lists 3,534 of 36,936 eligible values that are absent from `yaml/`, with
their original values.

## Files

| Path | Contents |
| --- | --- |
| `directory-manifest.yaml` | Directory manifest for `yaml/`. |
| `yaml/00_logical_identities.yaml` | Logical identities. |
| `yaml/<group>.yaml` | Datasets of one OFBiz entity group. |
| `forget-log.yaml` | Values absent from `yaml/` and their originals. |
| `questions.md` | Ten operator questions over orders, inventory, accounting, manufacturing, and shipments. |
