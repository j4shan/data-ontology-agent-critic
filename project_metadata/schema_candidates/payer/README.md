# Harbor Medicare Services

## Introduction

Harbor Medicare Services processes Medicare-scale claims. The catalog `payer` is the ontology of eligibility, 837 submission, adjudication, 835 remittance, pharmacy, premium billing, and benefit accumulation: datasets in the Snowflake database `PAYER`.

A claim header and a claim line are different facts. A remittance advice, a remit line, and a remit adjustment are different facts. An eligibility inquiry has one response. Members, coverage, providers, plans, and code sets are the populations those facts join. The questions below use the authored identities and joins. Synthetic row counts and fan-out for a 30-day window are listed with the major fact tables.

The business narrative and the full relationship table are in `business-model.md`. Loadable YAML is in `yaml/`.

## BI questions

1. What did a member claim, on which plan and coverage, and which billing provider submitted it?
   `payer.claim.fact_claim_header` joins `dim_member`, `dim_coverage`, `dim_plan`, and `dim_provider` through `billing_provider_id`. Every header has service lines on `fact_claim_line`.

2. Which procedure, rendering provider, and charge apply to each service line?
   `fact_claim_line` joins `fact_claim_header` as `1:many` with a required match both ways. `procedure_id` joins `dim_procedure`. `rendering_provider_id` joins `dim_provider`. `charge_amount` is a measure of the line.

3. How was a service line priced, and how was it paid?
   `fact_pricing_result` joins `fact_claim_line` one-to-one in both directions. `fact_remit_line` may join the same service line, and every remit line joins `fact_remit_advice`. `fact_remit_adjustment` joins the remit line and `dim_carc`.

4. Which diagnoses were reported on a claim, and which of them feed an HCC?
   `fact_claim_diagnosis` joins `fact_claim_header` as `1:many` with a required match both ways, and joins `dim_diagnosis`. `bridge_diagnosis_hcc` joins `dim_diagnosis` and `dim_hcc`.

5. What eligibility inquiry did a provider send for a member, and what was the response?
   `fact_eligibility_inquiry` joins `dim_member` and `dim_provider`. `fact_eligibility_response` joins that inquiry one-to-one in both directions.

6. What did adjudication post to a member's deductible or out-of-pocket accumulator?
   `fact_accumulator_entry` joins `dim_member`, `dim_accumulator_type`, and `fact_claim_line`. `fact_accumulator_snapshot` is the month-end position, `1:many` from both the member and the accumulator type with a required match both ways.

7. Which pharmacy claim filled which NDC for a member, and which prescriber ordered it?
   `payer.pharmacy.fact_pharmacy_claim` joins `dim_member`, `dim_pharmacy`, `dim_ndc`, and `dim_prescriber`.

8. Which coverage spans does a member have, and which plan do they sit on?
   `dim_coverage` joins `dim_member` as `1:many` with a required match both ways, and joins `dim_plan`. `fact_enrollment_span` joins `dim_coverage` one-to-one in both directions.

9. Who is the member's attributed PCP, and what risk score was stored at month end?
   `fact_pcp_attribution` joins `dim_member` one-to-one and joins `dim_provider`. `fact_risk_score` joins `dim_member` one-to-one and joins `dim_risk_model`.

10. Which edits fired on a claim before pricing?
    `fact_claim_edit` joins `fact_claim_header` as `1:many` with a required match both ways, and joins `dim_edit_code`.

11. What premium was billed and what was paid?
    `fact_premium_bill` joins `dim_member` one-to-one. `fact_premium_payment` joins that bill.

12. Which trading partner submitted a claim batch?
    `fact_claim_header.edi_batch_id` joins `fact_edi_batch`. Every batch has claims. `fact_edi_batch` joins `dim_submitter` and `dim_trading_partner`.

## Major fact tables

High-volume landing zones for the 30-day synthetic window. The sum of all fact rows in the catalog, including smaller operational facts, is 5,145,930,000.

| Fact | Grain class | Rows | Why this is a landing zone |
| --- | --- | ---: | --- |
| `remit.fact_remit_adjustment` | transaction | 630,000,000 | Authored above the remit-line population because an 835 service line can carry more than one adjustment group. Coverage of remit lines is 70 percent. |
| `benefit.fact_accumulator_snapshot` | periodic_snapshot | 544,000,000 | 68 million members times 8 accumulator types = 544 million rows. This is a periodic snapshot, not a claim. |
| `remit.fact_remit_line` | transaction | 504,000,000 | Authored at 1.25 remit rows per adjudicated service line, on 96 percent of the 420 million service lines, grouped onto 12 million remittance advices. |
| `benefit.fact_accumulator_entry` | transaction | 420,000,000 | Authored at one ledger posting per service line, joined to 90 percent of lines. |
| `claim.fact_claim_line` | transaction | 420,000,000 | Authored at five lines per claim header. Headers are the CMS-scale 84 million claims in the window. |
| `claim.fact_pricing_result` | transaction | 420,000,000 | One-to-one with the 420 million service lines. |
| `eligibility.fact_eligibility_inquiry` | transaction | 336,000,000 | Authored at four inquiries per claim header. The multiple is synthetic. It is not a published HETS count. |
| `eligibility.fact_eligibility_response` | transaction | 336,000,000 | Equal to the inquiry population because every inquiry has one response. |
| `claim.fact_claim_diagnosis` | transaction | 252,000,000 | Authored at three diagnoses per claim header. |
| `claim.fact_claim_edit` | transaction | 210,000,000 | Authored at 2.5 edit results per claim header. |
| `claim.fact_claim_status` | transaction | 168,000,000 | Authored at two status events per claim header. |
| `pharmacy.fact_pharmacy_claim` | transaction | 136,000,000 | Authored at two fills per member per month across 68 million members. |
| `claim.fact_claim_header` | transaction | 84,000,000 | 84 million headers in 30 days annualize to 1.008 billion, consistent with CMS reporting more than one billion Medicare fee-for-service claims a year. |

## Synthetic join statistics

Synthetic closed-form population for the stated window. Dimension and fact row counts are authored from the cited industry anchors and from structural fan-out (every parent required by an always-match rule has at least one child). Distinct parent keys, unmatched parents, null foreign keys, and average children per matched parent are derived from multiplicity. Optional-child match rates default to 0.93 when a join does not set one. Optional-parent coverage defaults to the full parent population when matched children can reach it, and otherwise to one child per observed parent. A stated coverage or matched-row count overrides that default. This is not a sampled extract.

Outbound means a foreign key on the fact. Inbound means another dataset carries that fact's identity. The full population and every join are in `statistics.md` and `statistics.json`.

### `fact_remit_adjustment`

CAS adjustment segments land here, one row per reason on a paid or denied remit line.

Rows: `630,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 630,000,000 | 630,000,000 | 0 | 30 | 0 | 21,000,000.00 |
| `carc_id` | `dim_carc` | 630,000,000 | 630,000,000 | 0 | 300 | 0 | 2,100,000.00 |
| `rarc_id` | `dim_rarc` | 630,000,000 | 441,000,000 | 189,000,000 | 440 | 660 | 1,002,272.73 |
| `remit_line_id` | `fact_remit_line` | 630,000,000 | 630,000,000 | 0 | 352,800,000 | 151,200,000 | 1.79 |

Inbound:

None in this catalog.

### `fact_accumulator_snapshot`

Month-end benefit balances land here, one row per member per accumulator type.

Rows: `544,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `accumulator_type_id` | `dim_accumulator_type` | 544,000,000 | 544,000,000 | 0 | 8 | 0 | 68,000,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 544,000,000 | 544,000,000 | 0 | 30 | 0 | 18,133,333.33 |
| `member_id` | `dim_member` | 544,000,000 | 544,000,000 | 0 | 68,000,000 | 0 | 8.00 |
| `plan_id` | `dim_plan` | 544,000,000 | 544,000,000 | 0 | 40 | 0 | 13,600,000.00 |

Inbound:

None in this catalog.

### `fact_remit_line`

835 service-payment lines land here. This is the payment event grain.

Rows: `504,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 504,000,000 | 504,000,000 | 0 | 30 | 0 | 16,800,000.00 |
| `carc_id` | `dim_carc` | 504,000,000 | 277,200,000 | 226,800,000 | 240 | 60 | 1,155,000.00 |
| `claim_header_id` | `fact_claim_header` | 504,000,000 | 504,000,000 | 0 | 82,320,000 | 1,680,000 | 6.12 |
| `claim_line_id` | `fact_claim_line` | 504,000,000 | 504,000,000 | 0 | 403,200,000 | 16,800,000 | 1.25 |
| `member_id` | `dim_member` | 504,000,000 | 504,000,000 | 0 | 54,400,000 | 13,600,000 | 9.26 |
| `provider_id` | `dim_provider` | 504,000,000 | 504,000,000 | 0 | 780,000 | 420,000 | 646.15 |
| `remit_advice_id` | `fact_remit_advice` | 504,000,000 | 504,000,000 | 0 | 12,000,000 | 0 | 42.00 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_remit_adjustment` | `remit_line_id` | 630,000,000 | 630,000,000 | 0 | 352,800,000 | 151,200,000 | 1.79 |

### `fact_accumulator_entry`

Adjudication postings to deductibles and out-of-pocket accumulators land here.

Rows: `420,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `accumulator_type_id` | `dim_accumulator_type` | 420,000,000 | 420,000,000 | 0 | 8 | 0 | 52,500,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 420,000,000 | 420,000,000 | 0 | 30 | 0 | 14,000,000.00 |
| `claim_line_id` | `fact_claim_line` | 420,000,000 | 420,000,000 | 0 | 378,000,000 | 42,000,000 | 1.11 |
| `member_id` | `dim_member` | 420,000,000 | 420,000,000 | 0 | 54,400,000 | 13,600,000 | 7.72 |
| `plan_id` | `dim_plan` | 420,000,000 | 420,000,000 | 0 | 40 | 0 | 10,500,000.00 |

Inbound:

None in this catalog.

### `fact_claim_line`

837 service lines are the atomic medical-claim landing zone.

Rows: `420,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `claim_header_id` | `fact_claim_header` | 420,000,000 | 420,000,000 | 0 | 84,000,000 | 0 | 5.00 |
| `diagnosis_id` | `dim_diagnosis` | 420,000,000 | 294,000,000 | 126,000,000 | 18,000 | 54,000 | 16,333.33 |
| `facility_id` | `dim_facility` | 420,000,000 | 176,400,000 | 243,600,000 | 180,000 | 0 | 980.00 |
| `fee_schedule_id` | `dim_fee_schedule` | 420,000,000 | 336,000,000 | 84,000,000 | 80 | 0 | 4,200,000.00 |
| `insurance_line_id` | `dim_insurance_line` | 420,000,000 | 420,000,000 | 0 | 6 | 0 | 70,000,000.00 |
| `member_id` | `dim_member` | 420,000,000 | 420,000,000 | 0 | 54,400,000 | 13,600,000 | 7.72 |
| `modifier_id` | `dim_modifier` | 420,000,000 | 147,000,000 | 273,000,000 | 200 | 200 | 735,000.00 |
| `ndc_id` | `dim_ndc` | 420,000,000 | 33,600,000 | 386,400,000 | 7,500 | 42,500 | 4,480.00 |
| `place_of_service_id` | `dim_place_of_service` | 420,000,000 | 420,000,000 | 0 | 50 | 0 | 8,400,000.00 |
| `plan_id` | `dim_plan` | 420,000,000 | 420,000,000 | 0 | 40 | 0 | 10,500,000.00 |
| `procedure_id` | `dim_procedure` | 420,000,000 | 420,000,000 | 0 | 4,800 | 7,200 | 87,500.00 |
| `rendering_provider_id` | `dim_provider` | 420,000,000 | 420,000,000 | 0 | 660,000 | 540,000 | 636.36 |
| `revenue_code_id` | `dim_revenue_code` | 420,000,000 | 176,400,000 | 243,600,000 | 300 | 200 | 588,000.00 |
| `service_day_id` | `dim_calendar_day` | 420,000,000 | 420,000,000 | 0 | 30 | 0 | 14,000,000.00 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_remit_line` | `claim_line_id` | 504,000,000 | 504,000,000 | 0 | 403,200,000 | 16,800,000 | 1.25 |
| `fact_accumulator_entry` | `claim_line_id` | 420,000,000 | 420,000,000 | 0 | 378,000,000 | 42,000,000 | 1.11 |
| `fact_pricing_result` | `claim_line_id` | 420,000,000 | 420,000,000 | 0 | 420,000,000 | 0 | 1.00 |
| `fact_claim_edit` | `claim_line_id` | 210,000,000 | 168,000,000 | 42,000,000 | 168,000,000 | 252,000,000 | 1.00 |
| `fact_cob_line` | `claim_line_id` | 36,000,000 | 36,000,000 | 0 | 33,600,000 | 386,400,000 | 1.07 |
| `fact_medical_review` | `claim_line_id` | 900,000 | 900,000 | 0 | 840,000 | 419,160,000 | 1.07 |

### `fact_pricing_result`

Fee-schedule pricing results land here, one per service line.

Rows: `420,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 420,000,000 | 420,000,000 | 0 | 30 | 0 | 14,000,000.00 |
| `claim_line_id` | `fact_claim_line` | 420,000,000 | 420,000,000 | 0 | 420,000,000 | 0 | 1.00 |
| `fee_schedule_id` | `dim_fee_schedule` | 420,000,000 | 420,000,000 | 0 | 80 | 0 | 5,250,000.00 |
| `locality_id` | `dim_locality` | 420,000,000 | 420,000,000 | 0 | 120 | 0 | 3,500,000.00 |
| `procedure_id` | `dim_procedure` | 420,000,000 | 420,000,000 | 0 | 4,800 | 7,200 | 87,500.00 |

Inbound:

None in this catalog.

### `fact_eligibility_inquiry`

X12 270 eligibility inquiries land here.

Rows: `336,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 336,000,000 | 336,000,000 | 0 | 30 | 0 | 11,200,000.00 |
| `coverage_id` | `dim_coverage` | 336,000,000 | 336,000,000 | 0 | 61,200,000 | 10,800,000 | 5.49 |
| `jurisdiction_id` | `dim_jurisdiction` | 336,000,000 | 336,000,000 | 0 | 12 | 0 | 28,000,000.00 |
| `member_id` | `dim_member` | 336,000,000 | 336,000,000 | 0 | 61,200,000 | 6,800,000 | 5.49 |
| `plan_id` | `dim_plan` | 336,000,000 | 336,000,000 | 0 | 40 | 0 | 8,400,000.00 |
| `provider_id` | `dim_provider` | 336,000,000 | 336,000,000 | 0 | 600,000 | 600,000 | 560.00 |
| `trading_partner_id` | `dim_trading_partner` | 336,000,000 | 336,000,000 | 0 | 80 | 0 | 4,200,000.00 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_eligibility_response` | `eligibility_inquiry_id` | 336,000,000 | 336,000,000 | 0 | 336,000,000 | 0 | 1.00 |

### `fact_eligibility_response`

X12 271 eligibility responses land here, one per inquiry.

Rows: `336,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 336,000,000 | 336,000,000 | 0 | 30 | 0 | 11,200,000.00 |
| `eligibility_inquiry_id` | `fact_eligibility_inquiry` | 336,000,000 | 336,000,000 | 0 | 336,000,000 | 0 | 1.00 |
| `member_id` | `dim_member` | 336,000,000 | 336,000,000 | 0 | 61,200,000 | 6,800,000 | 5.49 |
| `plan_id` | `dim_plan` | 336,000,000 | 336,000,000 | 0 | 40 | 0 | 8,400,000.00 |

Inbound:

None in this catalog.

### `fact_claim_diagnosis`

Claim diagnosis rows land here for reporting and risk inputs.

Rows: `252,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 252,000,000 | 252,000,000 | 0 | 30 | 0 | 8,400,000.00 |
| `claim_header_id` | `fact_claim_header` | 252,000,000 | 252,000,000 | 0 | 84,000,000 | 0 | 3.00 |
| `diagnosis_id` | `dim_diagnosis` | 252,000,000 | 252,000,000 | 0 | 25,200 | 46,800 | 10,000.00 |

Inbound:

None in this catalog.

### `fact_claim_edit`

Pre-adjudication edit results land here.

Rows: `210,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 210,000,000 | 210,000,000 | 0 | 30 | 0 | 7,000,000.00 |
| `claim_header_id` | `fact_claim_header` | 210,000,000 | 210,000,000 | 0 | 84,000,000 | 0 | 2.50 |
| `claim_line_id` | `fact_claim_line` | 210,000,000 | 168,000,000 | 42,000,000 | 168,000,000 | 252,000,000 | 1.00 |
| `edit_code_id` | `dim_edit_code` | 210,000,000 | 210,000,000 | 0 | 1,125 | 375 | 186,666.67 |

Inbound:

None in this catalog.

### `fact_claim_status`

Claim-status events land here as the header moves through receipt, acceptance, and finalization.

Rows: `168,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 168,000,000 | 168,000,000 | 0 | 30 | 0 | 5,600,000.00 |
| `claim_header_id` | `fact_claim_header` | 168,000,000 | 168,000,000 | 0 | 84,000,000 | 0 | 2.00 |
| `submitter_id` | `dim_submitter` | 168,000,000 | 168,000,000 | 0 | 2,500 | 0 | 67,200.00 |
| `trading_partner_id` | `dim_trading_partner` | 168,000,000 | 168,000,000 | 0 | 80 | 0 | 2,100,000.00 |

Inbound:

None in this catalog.

### `fact_pharmacy_claim`

NCPDP pharmacy claims land here, separate from 837 service lines.

Rows: `136,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 136,000,000 | 136,000,000 | 0 | 30 | 0 | 4,533,333.33 |
| `formulary_id` | `dim_formulary` | 136,000,000 | 108,800,000 | 27,200,000 | 30 | 0 | 3,626,666.67 |
| `insurance_line_id` | `dim_insurance_line` | 136,000,000 | 136,000,000 | 0 | 6 | 0 | 22,666,666.67 |
| `member_id` | `dim_member` | 136,000,000 | 136,000,000 | 0 | 30,600,000 | 37,400,000 | 4.44 |
| `ndc_id` | `dim_ndc` | 136,000,000 | 136,000,000 | 0 | 12,500 | 37,500 | 10,880.00 |
| `pharmacy_id` | `dim_pharmacy` | 136,000,000 | 136,000,000 | 0 | 55,200 | 4,800 | 2,463.77 |
| `plan_id` | `dim_plan` | 136,000,000 | 136,000,000 | 0 | 40 | 0 | 3,400,000.00 |
| `prescriber_id` | `dim_prescriber` | 136,000,000 | 136,000,000 | 0 | 240,000 | 160,000 | 566.67 |
| `tier_id` | `dim_tier` | 136,000,000 | 136,000,000 | 0 | 6 | 0 | 22,666,666.67 |

Inbound:

None in this catalog.

### `fact_claim_header`

837 claim headers land here. Volume concentrates on the lines, but the header is the claim grain those lines require.

Rows: `84,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `bill_type_id` | `dim_bill_type` | 84,000,000 | 35,280,000 | 48,720,000 | 70 | 30 | 504,000.00 |
| `billing_provider_id` | `dim_provider` | 84,000,000 | 84,000,000 | 0 | 840,000 | 360,000 | 100.00 |
| `calendar_day_id` | `dim_calendar_day` | 84,000,000 | 84,000,000 | 0 | 30 | 0 | 2,800,000.00 |
| `claim_frequency_id` | `dim_claim_frequency` | 84,000,000 | 84,000,000 | 0 | 8 | 0 | 10,500,000.00 |
| `coverage_id` | `dim_coverage` | 84,000,000 | 84,000,000 | 0 | 54,000,000 | 18,000,000 | 1.56 |
| `drg_id` | `dim_drg` | 84,000,000 | 10,080,000 | 73,920,000 | 480 | 320 | 21,000.00 |
| `edi_batch_id` | `fact_edi_batch` | 84,000,000 | 84,000,000 | 0 | 900,000 | 0 | 93.33 |
| `facility_id` | `dim_facility` | 84,000,000 | 35,280,000 | 48,720,000 | 144,000 | 36,000 | 245.00 |
| `filing_indicator_id` | `dim_filing_indicator` | 84,000,000 | 84,000,000 | 0 | 12 | 0 | 7,000,000.00 |
| `insurance_line_id` | `dim_insurance_line` | 84,000,000 | 84,000,000 | 0 | 6 | 0 | 14,000,000.00 |
| `jurisdiction_id` | `dim_jurisdiction` | 84,000,000 | 84,000,000 | 0 | 12 | 0 | 7,000,000.00 |
| `legal_entity_id` | `dim_legal_entity` | 84,000,000 | 84,000,000 | 0 | 4 | 0 | 21,000,000.00 |
| `member_id` | `dim_member` | 84,000,000 | 84,000,000 | 0 | 54,400,000 | 13,600,000 | 1.54 |
| `place_of_service_id` | `dim_place_of_service` | 84,000,000 | 84,000,000 | 0 | 50 | 0 | 1,680,000.00 |
| `plan_id` | `dim_plan` | 84,000,000 | 84,000,000 | 0 | 40 | 0 | 2,100,000.00 |
| `principal_diagnosis_id` | `dim_diagnosis` | 84,000,000 | 84,000,000 | 0 | 28,800 | 43,200 | 2,916.67 |
| `submitter_id` | `dim_submitter` | 84,000,000 | 84,000,000 | 0 | 2,500 | 0 | 33,600.00 |
| `trading_partner_id` | `dim_trading_partner` | 84,000,000 | 84,000,000 | 0 | 80 | 0 | 1,050,000.00 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_remit_line` | `claim_header_id` | 504,000,000 | 504,000,000 | 0 | 82,320,000 | 1,680,000 | 6.12 |
| `fact_claim_line` | `claim_header_id` | 420,000,000 | 420,000,000 | 0 | 84,000,000 | 0 | 5.00 |
| `fact_claim_diagnosis` | `claim_header_id` | 252,000,000 | 252,000,000 | 0 | 84,000,000 | 0 | 3.00 |
| `fact_claim_edit` | `claim_header_id` | 210,000,000 | 210,000,000 | 0 | 84,000,000 | 0 | 2.50 |
| `fact_claim_status` | `claim_header_id` | 168,000,000 | 168,000,000 | 0 | 84,000,000 | 0 | 2.00 |
| `fact_claim_admission` | `claim_header_id` | 15,120,000 | 15,120,000 | 0 | 15,120,000 | 68,880,000 | 1.00 |
| `fact_claim_note` | `claim_header_id` | 10,000,000 | 10,000,000 | 0 | 6,720,000 | 77,280,000 | 1.49 |
| `fact_attachment` | `claim_header_id` | 2,500,000 | 2,500,000 | 0 | 1,680,000 | 82,320,000 | 1.49 |
| `fact_overpayment` | `claim_header_id` | 400,000 | 400,000 | 0 | 400,000 | 83,600,000 | 1.00 |
| `fact_interest_payment` | `claim_header_id` | 200,000 | 200,000 | 0 | 200,000 | 83,800,000 | 1.00 |
| `fact_appeal` | `claim_header_id` | 180,000 | 180,000 | 0 | 180,000 | 83,820,000 | 1.00 |
| `fact_audit_sample` | `claim_header_id` | 50,000 | 50,000 | 0 | 50,000 | 83,950,000 | 1.00 |
