# ERPNext and Frappe HRMS

`frappe-erp` is a schema version 4 catalog of the ERPNext and Frappe HRMS tables on MariaDB,
plus the Frappe `tabUser` table. Each dataset is one DocType table.

## Source

| Project | Commit |
| --- | --- |
| ERPNext | `49d50fb7e54656be5fa99c8a406be837556cf622` |
| Frappe HRMS | `1d62bdbd2f9a67978c3ac9729999555bfe838263` |
| Frappe (User DocType only) | `58a298d5499cc966dee85546056841bb9744afbd` |

The sources declare 694 ERPNext and HRMS DocTypes. 42 of them have no table of their own and
are not in the catalog: 37 single DocTypes, which store their values as rows of `tabSingles`,
and 7 virtual DocTypes, 2 of which are also single.

## Counts

| Measure | Count |
| --- | ---: |
| Datasets | 653 |
| Columns | 13,662 |
| Logical identities | 693 |
| Entity definitions | 4,844 |

| File | Datasets | File | Datasets |
| --- | ---: | --- | ---: |
| `accounts.yaml` | 176 | `subcontracting.yaml` | 13 |
| `hr.yaml` | 111 | `support.yaml` | 10 |
| `stock.yaml` | 73 | `maintenance.yaml` | 5 |
| `manufacturing.yaml` | 48 | `regional.yaml` | 5 |
| `payroll.yaml` | 41 | `telephony.yaml` | 5 |
| `setup.yaml` | 38 | `communication.yaml` | 2 |
| `assets.yaml` | 26 | `edi.yaml` | 2 |
| `crm.yaml` | 26 | `portal.yaml` | 2 |
| `buying.yaml` | 18 | `utilities.yaml` | 2 |
| `selling.yaml` | 18 | `bulk_transaction.yaml` | 1 |
| `quality_management.yaml` | 16 | `framework.yaml` | 1 |
| `projects.yaml` | 14 | | |

`forget-log.yaml` lists 6,403 of 65,535 eligible values that are absent from `yaml/`, with
their original values.

## Files

| Path | Contents |
| --- | --- |
| `directory-manifest.yaml` | Directory manifest for `yaml/`. |
| `yaml/00_logical_identities.yaml` | Logical identities. |
| `yaml/<module>.yaml` | Datasets of one Frappe module. |
| `forget-log.yaml` | Values absent from `yaml/` and their originals. |
| `questions.md` | Ten finance, inventory, and HR questions. |
