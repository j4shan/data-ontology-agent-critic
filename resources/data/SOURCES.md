# Data catalog

This file is the manifest for `resources/data/`. Earnings-call candidates are a provenance pool
for later ontology experiments. They are not Critic assessment domains, and they are not
reference catalogs, generated catalogs, or gold analytical knowledge graphs.

Question files paraphrase analyst questions. They do not store transcript text. Each industry
directory has `references.md`, which names the companies and earnings calls without links.

## Earnings-call industries

| Directory | Companies | Warehouse |
| --- | --- | --- |
| `semiconductors/` | Broadcom, Nvidia | — |
| `semiconductor-materials-equipment/` | Applied Materials, Lam Research | — |
| `systems-software/` | Microsoft, ServiceNow | — |
| `application-software/` | Salesforce, Oracle | — |
| `technology-hardware/` | Apple, Dell Technologies | `technology-hardware/warehouse/` (Device Inc) |
| `interactive-media/` | Alphabet, Meta Platforms | `interactive-media/warehouse/` (Social Inc) |
| `movies-entertainment/` | Walt Disney, Netflix | — |
| `integrated-telecom/` | AT&T, Verizon | — |
| `broadline-retail/` | Amazon, eBay | — |
| `home-improvement-retail/` | Home Depot, Lowe's | — |
| `automobile-manufacturers/` | General Motors, Tesla | `automobile-manufacturers/warehouse/` (Automaker Inc) |
| `restaurants/` | McDonald's, Starbucks | `restaurants/warehouse/` (Burger Inc) |
| `merchandise-retail/` | Costco, Walmart | `merchandise-retail/warehouse/` (Merchandise Inc) |
| `soft-drinks/` | Coca-Cola, PepsiCo | `soft-drinks/warehouse/` (Beverage Inc) |
| `packaged-foods/` | General Mills, Mondelez | `packaged-foods/warehouse/` (Food Inc) |
| `diversified-banks/` | Bank of America, JPMorgan Chase | `diversified-banks/warehouse/` (Bank Inc) |
| `investment-banking/` | Goldman Sachs, Morgan Stanley | — |
| `payments/` | Mastercard, Visa | — |
| `pc-insurance/` | Chubb, Progressive | — |
| `pharmaceuticals/` | Eli Lilly, Merck | — |
| `managed-care/` | Elevance Health, UnitedHealth Group | `managed-care/warehouse/` (Health Plan Inc) |
| `health-care-equipment/` | Intuitive Surgical, Stryker | `health-care-equipment/warehouse/` (Surgical Supply Inc) |
| `aerospace-defense/` | Lockheed Martin, RTX | — |
| `construction-machinery/` | Caterpillar, PACCAR | `construction-machinery/warehouse/` (Machinery Inc) |
| `rail-transportation/` | CSX, Union Pacific | `rail-transportation/warehouse/` (Railroad Inc) |
| `passenger-airlines/` | Delta Air Lines, United Airlines | `passenger-airlines/warehouse/` (Airline Inc) |
| `integrated-oil-gas/` | Chevron, Exxon Mobil | `integrated-oil-gas/warehouse/` (Energy Inc) |
| `specialty-chemicals/` | Ecolab, Sherwin-Williams | `specialty-chemicals/warehouse/` (Chemical Inc) |
| `data-center-reits/` | Digital Realty, Equinix | `data-center-reits/warehouse/` (Colocation Inc) |
| `electric-utilities/` | Duke Energy, Southern Company | `electric-utilities/warehouse/` (Utility Inc) |

Each company sheet is `{industry}/{ticker}/questions.md`. A warehouse is one schema version 3
catalog for that industry, owned by the naive name in the table. `coverage.md` is the GICS
membership list. `summary-report.md` is the question-count and warehouse summary.
`_batches/` holds the extraction tallies.

## Transcript sources

The four most recent dated transcripts were read for each company. Fiscal labels on the page
decide order when the URL date and the fiscal period disagree.

**The Motley Fool earnings-call transcript archive** is the primary source.

- Index: https://www.fool.com/earnings-call-transcripts/
- Article pattern: `https://www.fool.com/earnings/call-transcripts/{year}/{month}/{day}/{slug}/`
- Coverage used here: U.S. earnings calls, including S&P 500 names, with speaker-labeled Q&A.
- Access: public HTML pages. No account was required for the calls fetched in this pass.
- Fool pages are the source of record for a call when both Fool and a fallback carry it.

**MarketBeat earnings-report pages**, transcript body credited to Quartr, are the fallback.

- Company earnings index: `https://www.marketbeat.com/stocks/{EXCHANGE}/{TICKER}/earnings/`
- Report pattern: `https://www.marketbeat.com/earnings/reports/{YYYY-MM-DD}-{company-slug}-stock/`
- Use a MarketBeat page only when Fool has fewer than four recent calls for that company.

| Source | Why it is not the fetch path |
| --- | --- |
| Seeking Alpha | U.S. transcripts exist, and full text generally requires a paid subscription. |
| Koyfin | Free plan is a short recent window and is not a stable page-per-call archive. |
| Quartr | First-party audio and transcripts, primarily through an app rather than a stable public URL. |
| Company investor-relations sites | Prepared remarks, slides, and audio are common. Full analyst Q&A is inconsistent. |
| SEC EDGAR 8-K exhibits | Some issuers file prepared remarks or a transcript. Coverage of live analyst Q&A is uneven, so EDGAR is not the primary fetch. |
| Financial Modeling Prep, Alpha Vantage, and similar APIs | Transcript endpoints require an API key that this workspace does not have. |

Verbatim questions and prepared remarks stay on the source site.

## Assessment question sheets

Benchmark domain question sheets stay under `project_metadata/schema_candidates/`:

| Domain | Question sheet |
| --- | --- |
| `healthcare-payer` | `healthcare-payer/questions.md` |
| `telecom-mobile` | `telecom-mobile/questions.md` |
| `manufacturing-discrete` | `manufacturing-discrete/questions.md` |
| `retail-grocery` | `retail-grocery/questions.md` |
| `commerce-marketplace` | `commerce-marketplace/questions.md` |

## Published catalog assets

| Path | Content |
| --- | --- |
| `reference_catalogs/<domain>/` | Human-reviewed catalog gold for scoring generated catalogs. Each directory contains only that domain's YAML. |
| `generated_catalogs/<domain>/` | Committed actor output used as benchmark input, published only by the DDL collector after owner review. Each domain has `directory-manifest.yaml`, `yaml/` collection files, `decisions.md`, and `provenance.yaml`. No suite, case, or gold AKG is derived from generated catalogs. |

Neither directory has published catalog content yet. If a future suite introduces external or
vendored source data, record its origin, license, retrieval method, and content hashes here
before using it in a benchmark.
