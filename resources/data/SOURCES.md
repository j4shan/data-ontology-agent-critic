# Test data sources

No external or vendored test data source is currently active. The benchmark catalogs and question
sheets live under `project_metadata/schema_candidates/`:

| Domain | Question sheet |
| --- | --- |
| `healthcare-payer` | `healthcare-payer/questions.md` |
| `telecom-mobile` | `telecom-mobile/questions.md` |
| `manufacturing-discrete` | `manufacturing-discrete/questions.md` |
| `retail-grocery` | `retail-grocery/questions.md` |
| `commerce-marketplace` | `commerce-marketplace/questions.md` |

If a future suite introduces external source data, record its origin, license, retrieval method,
and content hashes here before using it in a benchmark.

## Published catalog assets

| Path | Content |
| --- | --- |
| `reference_catalogs/<domain>/` | Human-reviewed catalog gold for scoring generated catalogs. Each directory contains only that domain's YAML. |
| `generated_catalogs/<domain>/` | Committed actor output used as benchmark input, published only by the DDL collector after owner review. Each domain has `directory-manifest.yaml`, `yaml/` collection files, `decisions.md`, and `provenance.yaml`. No suite, case, or gold AKG is derived from generated catalogs. |

Neither directory has published catalog content yet.
