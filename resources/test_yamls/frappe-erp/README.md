# ERPNext and Frappe HRMS

`frappe-erp` is a schema version 4 catalog of ERPNext and Frappe HRMS on MariaDB, plus the Frappe User DocType. Each main DocType is one dataset. The catalog is the high fan-out candidate: Frappe stores `owner` and `modified_by` on every non-single table, and both columns realize `user_identity`.

The actor loaded `yaml/` with `load_intermediary_directory`. The directory is valid: schema version 4, 693 nodes, 700 logical identities, 14,223 columns, and 4,979 entity definitions.

## Sources

DocType JSON is read from the `develop` checkouts under `/tmp/schema-scan`. ERPNext and HRMS contribute every `doctype/<name>/<name>.json`. Frappe contributes only `frappe/core/doctype/user/user.json`, so `user_identity` has one complete population.

| Project | Path | Commit |
| --- | --- | --- |
| ERPNext | `/tmp/schema-scan/erpnext` | `49d50fb7e54656be5fa99c8a406be837556cf622` |
| Frappe HRMS | `/tmp/schema-scan/hrms` | `1d62bdbd2f9a67978c3ac9729999555bfe838263` |
| Frappe (User only) | `/tmp/schema-scan/frappe` | `58a298d5499cc966dee85546056841bb9744afbd` |

That is 536 ERPNext DocTypes, 158 HRMS DocTypes, and User. Two DocTypes have no stored columns and are omitted: `Authorization Control` (empty) and `Pegged Currencies` (a Section Break and a Table only). The child table `Pegged Currency Details` remains a dataset. 693 datasets are emitted.

## Counts

| Measure | Count |
| --- | ---: |
| Datasets | 693 |
| Non-single datasets | 658 |
| Single datasets | 35 |
| Columns | 14,223 |
| Logical identities | 700 |
| Entity definitions | 4,979 |

Datasets are partitioned by the DocType module. User is the only dataset in `framework.yaml`.

| File | Datasets | File | Datasets |
| --- | ---: | --- | ---: |
| `accounts.yaml` | 190 | `projects.yaml` | 15 |
| `hr.yaml` | 115 | `subcontracting.yaml` | 13 |
| `stock.yaml` | 78 | `support.yaml` | 11 |
| `manufacturing.yaml` | 51 | `maintenance.yaml` | 5 |
| `payroll.yaml` | 43 | `regional.yaml` | 5 |
| `setup.yaml` | 39 | `telephony.yaml` | 5 |
| `crm.yaml` | 28 | `utilities.yaml` | 4 |
| `assets.yaml` | 26 | `bulk_transaction.yaml` | 2 |
| `selling.yaml` | 20 | `communication.yaml` | 2 |
| `buying.yaml` | 19 | `edi.yaml` | 2 |
| `quality_management.yaml` | 16 | `portal.yaml` | 2 |
| `erpnext_integrations.yaml` | 1 | `framework.yaml` | 1 |

Qualified names are `frappe-erp.<module>.<doctype_snake>`. The MariaDB object is `tab<DocType name>`, on host `mariadb.frappe.internal`, database `frappe`, dialect `mariadb`, schema equal to the module slug.

## user_identity

`user_identity` is realized on 659 datasets. It is realized on 658 of 658 non-single datasets, which is 100 percent. Every non-single dataset defines it on `owner` and on `modified_by`. `frappe-erp.framework.user` also defines it on `name`, and that definition is the complete population. One single dataset, `frappe-erp.hr.shift_assignment_tool`, defines it on `approver`.

## company_identity

`company_identity` is realized on 207 datasets, 29.9 percent of 693. It is realized on 197 non-single datasets, 29.9 percent of 658. `frappe-erp.setup.company` defines it on `name`, and that definition is the complete population. Every other definition is a stored Link whose options are `Company`, including `company`, `parent_company`, `represents_company`, and the other company links that ERPNext and HRMS actually declare. There is no `tenant_id` column.

## Top 15 identities by dataset count

| Identity | Datasets |
| --- | ---: |
| `user_identity` | 659 |
| `company_identity` | 207 |
| `item_identity` | 100 |
| `account_identity` | 94 |
| `currency_identity` | 86 |
| `uom_identity` | 78 |
| `warehouse_identity` | 77 |
| `cost_center_identity` | 75 |
| `employee_identity` | 74 |
| `doctype_identity` | 67 |
| `project_identity` | 67 |
| `department_identity` | 58 |
| `customer_identity` | 44 |
| `supplier_identity` | 40 |
| `designation_identity` | 30 |

`currency_identity` and `doctype_identity` are among these because many Link fields point at the Frappe Currency and DocType masters. Those masters are outside this catalog, so their definitions stay `partial`. The same is true of Address, Contact, Role, and the other Frappe DocTypes that ERPNext links to. User is the only Frappe DocType included as a dataset.

## Memory loss

Optional inferred values were dropped with the `memory-loss-v1` rates and domain `frappe-erp`. A draw depends on the domain and the field path. Names, accessors, column names, logical-entity ids and names, and entity-definition `identity_id` and `dataset_columns` stay. Forgotten claims are `unknown`. A complete definition never keeps `conforms: false`; that draw is `unknown` instead. When the whole grain is forgotten, the value is the scalar `unknown` and its component fields are not forgotten a second time.

7,060 of 74,042 eligible values were forgotten. Every rate kind had eligible values, and every kind lost at least one.

| Kind | Rate | Eligible | Forgotten |
| --- | ---: | ---: | ---: |
| description | 0.08 | 21,211 | 1,691 |
| synonyms | 0.15 | 6,151 | 940 |
| tags | 0.15 | 693 | 107 |
| value_description | 0.12 | 14,223 | 1,770 |
| entity_expression | 0.10 | 4,979 | 493 |
| entity_metadata | 0.10 | 4,979 | 491 |
| grain_component_description | 0.08 | 616 | 65 |
| grain | 0.06 | 658 | 42 |
| grain_component_identity | 0.05 | 616 | 41 |
| claim | 0.07 | 19,916 | 1,420 |

`forget-log.yaml` records the seed, the domain, the rate table, the counts, and every forgotten path with its kind and original value. It is not builder input and it lives outside `yaml/`.

## Modeling rules

A dataset is one main DocType JSON, plus User. Non-single tables add the framework columns `name`, `owner`, `creation`, `modified`, `modified_by`, `docstatus`, and `idx` after the authored fields. Child tables (`istable`) also add `parent`, `parentfield`, and `parenttype`. Single DocTypes have no framework columns; the grain is `unknown`. Virtual DocTypes use the same single versus non-single rules.

Stored fieldtypes are kept, including Link, Dynamic Link, Data, Select, numeric and date types, Check, text, Attach, Code, Read Only, JSON, Phone, Duration, and Rating. Layout and no-value types are omitted: Section Break, Column Break, Tab Break, HTML, Button, Fold, Heading, Table, Table MultiSelect, Image, Attachment Gallery, and Vue Component. Virtual fields are omitted. `dataset_columns` lists are sorted ascending. Column inventory follows the DocType, then the framework columns.

`name` on a non-single DocType realizes `<snake>_identity` with `unique` true, `total` true, `conforms` true, and `entity_universe` complete. A Link to DocType X realizes `<snake of X>_identity` with `unique` taken from the field's `unique` flag, `total` true when `reqd` is set, `conforms` true, and `entity_universe` partial. `owner` and `modified_by` realize `user_identity` with `unique` false, `total` true, `conforms` true, and `entity_universe` partial. Select, Data, and Check columns have no entity definition unless the column is `name`.

When a child table is the target of exactly one Table field, `parent` realizes that parent's identity (`unique` false, `total` true, `conforms` true, partial). `frappe-erp.selling.sales_order_item` does this for Sales Order. Shared children such as `frappe-erp.selling.sales_team` keep `parent` as a column with no entity definition. A Dynamic Link keeps its column. It gets an entity definition only when the paired options field is a literal constant DocType. None of the 87 Dynamic Link fields in these sources are constant, so `party` on `frappe-erp.accounts.gl_entry` stays a column.

The grain of a non-single dataset is `name` and that DocType's identity. The grain description says one row per document. Each entity expression is a single label such as `[column]`, with expression context `MariaDB column reference`. The logical-entity name is the DocType name. Its description says what the identity is. Node ids are `sql-database:frappe-erp.<module>.<doctype_snake>`. Tags carry the module and `erpnext`, `hrms`, or `framework`. User is tagged `core` and `framework`.

## Files

| Path | Contents |
| --- | --- |
| `directory-manifest.yaml` | Schema version 4 manifest. Paths are relative to `yaml/`. |
| `yaml/00_logical_identities.yaml` | `schema_version` and `logical_identities` only. |
| `yaml/<module>.yaml` | `schema_version` and `nodes` for one module. |
| `forget-log.yaml` | Memory-loss answer key. Not builder input. |
| `questions.md` | Ten finance, inventory, and HR questions over qualified dataset names and columns. |
