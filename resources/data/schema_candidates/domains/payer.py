"""Warehouse-style ontology for a Medicare-scale payer and claims processor."""

from domains.assemble import build_datasets, link as L, measure as M, spec

_NARRATIVE = """
Harbor Medicare Services is a fictional processor operating at Medicare Administrative Contractor scale. The catalog is the warehouse-style ontology of eligibility, claim submission, adjudication, remittance, pharmacy, premium billing, and benefit accumulation. Members, coverage spans, providers, plans, and code sets are conformed dimensions. Claims, service lines, remittance, and eligibility transactions are facts.

A claim is not one row. The X12 837 claim has a header and many service lines, and those grains stay in separate facts. Professional, institutional, and DME claims share the header and line facts and are distinguished by insurance line, bill type, and revenue code. Remittance follows the X12 835 shape: a remittance advice, many service lines, and adjustment rows for claim-adjustment reason codes. Eligibility is a 270 inquiry and a 271 response, one response per inquiry. Pharmacy claims are a separate NCPDP-style fact. Benefit accumulators land both as an adjudication ledger and as a month-end snapshot by member and accumulator type.

The 30-day populations are synthetic. The member count and the claim-header count are set so the window is consistent with published Medicare fee-for-service scale. Line, remittance, eligibility, and accumulator fan-out are authored on top of that anchor. Statistics sit beside the catalog.
"""

_PROVENANCE = """
Harbor Medicare Services is fictional. CMS reported in its fiscal year 2025 financial report that Medicare routinely processes over one billion fee-for-service claims a year and that enrollment is roughly 68 million people. The member dimension uses 68 million. The claim-header fact uses 84 million rows in a 30-day window, which annualizes to 1.008 billion claims. Service-line fan-out of five lines per header, remittance and adjustment multiples, eligibility at four inquiries per header, and the month-end accumulator snapshot of eight types per member are authored structural fan-outs, not additional CMS statistics. Header and line are separate facts because an 837 claim is one header and many service lines, which is also the Kimball rule that facts stay true to one grain. Remittance distinguishes the 835 advice, the service line, and the adjustment. Pharmacy is separate because NCPDP claim transactions are not 837 service lines. No payer platform DDL was copied.
"""

_QUESTIONS = """
1. What did a member claim, on which plan and coverage, and which billing provider submitted it?
   `healthcare-payer.claim.fact_claim_header` joins `dim_member`, `dim_coverage`, `dim_plan`, and `dim_provider` through `billing_provider_id`. Every header has service lines on `fact_claim_line`.

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
   `healthcare-payer.pharmacy.fact_pharmacy_claim` joins `dim_member`, `dim_pharmacy`, `dim_ndc`, and `dim_prescriber`.

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
"""


def _dim(subject, name, display, description, rows, links=(), measures=(), synonyms=()):
    return spec(subject, name, "dimension", display, description, rows, links, measures, synonyms)


def _fact(subject, name, display, description, rows, links=(), measures=(), volume_class="transaction", synonyms=()):
    return spec(
        subject, name, "fact", display, description, rows, links, measures, synonyms, volume_class=volume_class
    )


def _bridge(name, display, description, rows, links):
    return spec("bridge", name, "bridge", display, description, rows, links)


def _datasets() -> list[dict]:
    code_sets = [
        ("reference", "dim_currency", "Currency", "Currency of a financial fact.", 4, "USD, CAD, EUR, GBP"),
        ("reference", "dim_gender", "Gender", "Administrative gender code.", 4, "M, F, U, X"),
        ("reference", "dim_language", "Language", "Language of a member or letter.", 20, "en, es, zh, vi, ko, ru, ar, fr, pt, ht"),
        ("reference", "dim_relation", "Relationship", "Relationship of a person to the subscriber.", 12, "self, spouse, child, disabled-dependent, other"),
        ("reference", "dim_lob", "Line of Business", "Book of business.", 4, "FFS-A, FFS-B, MA, Part-D"),
        ("reference", "dim_insurance_line", "Insurance Line", "Medicare claim type.", 6, "inpatient, outpatient, professional, DME, home-health, hospice"),
        ("reference", "dim_cob_type", "COB Type", "Coordination-of-benefits type.", 6, "primary, secondary, tertiary, worker-comp, liability, none"),
        ("reference", "dim_payment_method", "Payment Method", "How a premium or provider payment was made.", 6, "EFT, check, card, benefit, withholding, offset"),
        ("reference", "dim_appeal_level", "Appeal Level", "Level of a claim appeal.", 5, "redetermination, reconsideration, ALJ, council, judicial"),
        ("reference", "dim_review_type", "Review Type", "Medical-review program.", 8, "prepay, postpay, TPE, probe, ADR, automated"),
        ("reference", "dim_auth_type", "Authorization Type", "Prior-authorization type.", 15, "inpatient, surgery, imaging, DME, drug, referral"),
        ("reference", "dim_service_category", "Service Category", "Benefit category of a procedure.", 80, "E&M, surgery, radiology, lab, anesthesia, therapy, drug"),
        ("reference", "dim_tier", "Formulary Tier", "Pharmacy formulary tier.", 6, "preferred-generic, generic, preferred-brand, nonpreferred, specialty, excluded"),
        ("reference", "dim_accumulator_type", "Accumulator Type", "Benefit accumulator bucket.", 8, "deductible, coinsurance, OOP, MOOP, copay, benefit-max, day-max, unit-max"),
        ("reference", "dim_discharge_status", "Discharge Status", "Patient discharge status.", 40, "home, SNF, transfer, expired, left-against-advice"),
        ("reference", "dim_admission_type", "Admission Type", "Institutional admission type.", 10, "emergency, urgent, elective, newborn, trauma"),
        ("reference", "dim_claim_frequency", "Claim Frequency", "Claim frequency code.", 8, "original, replacement, void, interim, final"),
        ("reference", "dim_filing_indicator", "Filing Indicator", "Claim filing indicator.", 12, "Medicare-A, Medicare-B, MA, Medicaid, commercial"),
        ("reference", "dim_place_of_service", "Place of Service", "CMS place-of-service code.", 50, "office, inpatient, outpatient, ER, ASC, home, telehealth, SNF"),
        ("reference", "dim_bill_type", "Bill Type", "Institutional bill type.", 100, "111, 131, 137, 211, 321, 721, 811"),
        ("reference", "dim_occurrence_code", "Occurrence Code", "Institutional occurrence code.", 80, "accident, admission, service"),
        ("reference", "dim_condition_code", "Condition Code", "Institutional condition code.", 120, "employment, ESRD, hospice, disaster"),
        ("reference", "dim_value_code", "Value Code", "Institutional value code.", 60, "covered-days, coinsurance, blood, rate"),
        ("reference", "dim_patient_status", "Patient Status", "Status of the patient on the claim.", 30, "discharged, still-patient, expired"),
        ("reference", "dim_modifier", "Procedure Modifier", "CPT or HCPCS modifier.", 400, "26, TC, 59, 25, LT, RT, GP, KX"),
        ("reference", "dim_revenue_code", "Revenue Code", "Institutional revenue code.", 500, "0100, 0250, 0300, 0450, 0510, 0636"),
        ("reference", "dim_denial_reason", "Denial Reason", "Payer denial category.", 200, "medical-necessity, timely-filing, duplicate, coverage, authorization"),
        ("reference", "dim_document_type", "Document Type", "Attachment or letter type.", 10, "ADR, EOB, letter, medical-record, invoice"),
        ("reference", "dim_enrollment_status", "Enrollment Status", "Status of a provider enrollment.", 6, "pending, approved, denied, revoked, deactivated, revalidation"),
        ("reference", "dim_note_type", "Note Type", "Type of a claim note.", 15, "adjudication, review, customer, system, appeal"),
        ("reference", "dim_interest_reason", "Interest Reason", "Why interest was paid on a claim.", 8, "late-clean-claim, court, settlement"),
        ("reference", "dim_withhold_reason", "Withhold Reason", "Why an amount was withheld.", 10, "IRS, offset, suspension, penalty"),
        ("reference", "dim_lis_level", "LIS Level", "Low-income subsidy level.", 5, "full, partial-1, partial-2, none, unknown"),
        ("reference", "dim_risk_model", "Risk Model", "Risk-adjustment model.", 4, "CMS-HCC-V24, CMS-HCC-V28, RxHCC, ESRD"),
        ("reference", "dim_edit_code", "Edit Code", "Pre-adjudication edit.", 1_500, "NCCI, MUE, LCD, duplicate, gender, age"),
        ("reference", "dim_call_queue", "Call Queue", "Member-services queue.", 20, "claims, eligibility, premium, pharmacy, appeals"),
        ("care", "dim_audit_program", "Audit Program", "Program that draws an audit sample.", 8, "CERT, UPIC, RAC, internal"),
        ("care", "dim_fraud_scheme", "Fraud Scheme", "Scheme classification of a fraud lead.", 40, "upcoding, unbundling, phantom, kickback, identity"),
        ("provider", "dim_taxonomy", "Provider Taxonomy", "NUCC taxonomy code.", 800, "207Q00000X, 207R00000X, 363L00000X, 261QE0002X"),
        ("provider", "dim_specialty", "Specialty", "Payer specialty grouping.", 180, "PCP, cardiology, orthopedics, oncology, radiology, pharmacy"),
        ("provider", "dim_network", "Provider Network", "Contracted network.", 25, "PPO, HMO, FFS-par, FFS-nonpar, pharmacy"),
        ("benefit", "dim_drug_class", "Drug Class", "Therapeutic class of an NDC.", 400, "statin, insulin, opioid, antibiotic, inhaler"),
        ("organization", "dim_state", "State", "US state or district.", 51, "AL, CA, FL, NY, TX, DC"),
        ("organization", "dim_bank", "Bank", "Bank used for provider or premium settlement.", 15, "treasury, commercial"),
    ]
    tables = []
    for subject, name, display, description, rows, codes in code_sets:
        tables.append(_dim(subject, name, display, description, rows, measures=[M("code", f"Code for the {display.lower()}.", codes)]))
    tables.extend(
        [
            _dim("organization", "dim_enterprise", "Enterprise", "The processor as one company.", 1, measures=[M("enterprise_name", "Registered name of the processor.")]),
            _dim("organization", "dim_legal_entity", "Legal Entity", "Legal entity that holds a Medicare contract.", 4, [L("enterprise_id", "dim_enterprise", "n1!")], [M("legal_entity_name", "Registered name.")]),
            _dim("organization", "dim_jurisdiction", "Jurisdiction", "Geographic jurisdiction the processor administers.", 12, [L("legal_entity_id", "dim_legal_entity", "n1")], [M("jurisdiction_name", "Name of the jurisdiction.")]),
            _dim("organization", "dim_department", "Department", "Internal department.", 60, [L("legal_entity_id", "dim_legal_entity", "n1")], [M("department_name", "Name of the department.")]),
            _dim("organization", "dim_cost_center", "Cost Center", "Cost center inside a department.", 180, [L("department_id", "dim_department", "n1!")], [M("cost_center_name", "Name of the cost center.")]),
            _dim("organization", "dim_employee", "Employee", "Employee of the processor.", 15_000, [L("department_id", "dim_department", "n1"), L("cost_center_id", "dim_cost_center", "n1"), L("jurisdiction_id", "dim_jurisdiction", "n1")], [M("employee_name", "Name of the employee.")]),
            _dim("organization", "dim_gl_account", "GL Account", "General-ledger account.", 600, [L("legal_entity_id", "dim_legal_entity", "n1")], [M("account_name", "Name of the account.")]),
            _dim("organization", "dim_accounting_period", "Accounting Period", "Accounting period of the statistics window.", 1, measures=[M("period_name", "Name of the period.")]),
            _dim("organization", "dim_calendar_day", "Calendar Day", "One day inside the 30-day statistics window.", 30, measures=[M("calendar_date", "Civil date.")]),
            _dim("organization", "dim_locality", "Payment Locality", "Medicare payment locality.", 120, [L("state_id", "dim_state", "n1!")], [M("locality_code", "Locality code.")]),
            _dim("organization", "dim_trading_partner", "Trading Partner", "Clearinghouse or submitter network.", 80, measures=[M("partner_name", "Name of the trading partner.")]),
            _dim("organization", "dim_submitter", "Submitter", "EDI submitter that sends claim batches.", 2_500, [L("trading_partner_id", "dim_trading_partner", "n1!", "Every trading partner has submitters.")], [M("submitter_name", "Name of the submitter.")]),
            _dim("member", "dim_address", "Address", "Postal address.", 70_000_000, [L("state_id", "dim_state", "n1")], [M("locality", "City or locality.")]),
            _dim("member", "dim_member", "Member", "Medicare beneficiary in the book of business.", 68_000_000, [L("state_id", "dim_state", "n1!", "Every state has members in this national book."), L("gender_id", "dim_gender", "n1!"), L("language_id", "dim_language", "n1"), L("jurisdiction_id", "dim_jurisdiction", "n1")], [M("member_number", "Medicare beneficiary identifier analogue.")], ["member", "beneficiary"]),
            _dim("benefit", "dim_plan", "Plan", "Benefit plan or contract.", 40, [L("legal_entity_id", "dim_legal_entity", "n1"), L("jurisdiction_id", "dim_jurisdiction", "n1"), L("lob_id", "dim_lob", "n1!")], [M("plan_name", "Name of the plan.")]),
            _dim("benefit", "dim_benefit", "Benefit", "Covered benefit inside a plan.", 600, [L("plan_id", "dim_plan", "n1!", "Every plan has benefits.")], [M("benefit_name", "Name of the benefit.")]),
            _dim("benefit", "dim_contract", "CMS Contract", "Contract identifier associated with a plan.", 120, [L("plan_id", "dim_plan", "n1!", "Every plan has at least one contract row."), L("legal_entity_id", "dim_legal_entity", "n1")], [M("contract_number", "Contract number.")]),
            _dim("member", "dim_group", "Employer Group", "Group that sponsors a subset of coverage.", 8_000, [L("plan_id", "dim_plan", "n1")], [M("group_name", "Name of the group.")]),
            _dim("member", "dim_coverage", "Coverage", "One coverage span key for a member on a plan.", 72_000_000, [L("member_id", "dim_member", "n1!", "Every member has at least one coverage."), L("plan_id", "dim_plan", "n1!", "Every plan has coverage."), L("legal_entity_id", "dim_legal_entity", "n1"), L("group_id", "dim_group", "n1?", "Individual coverage has no employer group.", match_rate=0.15)], [M("coverage_status", "Status of the coverage.", "active, terminated, pending")]),
            _dim("provider", "dim_provider", "Provider", "Billing or rendering provider identified by NPI.", 1_200_000, [L("taxonomy_id", "dim_taxonomy", "n1"), L("state_id", "dim_state", "n1!"), L("specialty_id", "dim_specialty", "n1")], [M("npi", "National provider identifier."), M("provider_name", "Name of the provider.")], ["provider", "billing provider"]),
            _dim("provider", "dim_facility", "Facility", "Service facility location.", 180_000, [L("state_id", "dim_state", "n1"), L("provider_id", "dim_provider", "n1?", "A facility may not yet be tied to a billing NPI.", match_rate=0.9)], [M("facility_name", "Name of the facility.")]),
            _dim("provider", "dim_prescriber", "Prescriber", "Prescriber on a pharmacy claim.", 400_000, [L("taxonomy_id", "dim_taxonomy", "n1"), L("state_id", "dim_state", "n1")], [M("npi", "Prescriber NPI.")]),
            _dim("pharmacy", "dim_pharmacy", "Pharmacy", "Dispensing pharmacy.", 60_000, [L("state_id", "dim_state", "n1!"), L("network_id", "dim_network", "n1")], [M("ncpdp_id", "NCPDP pharmacy identifier."), M("pharmacy_name", "Name of the pharmacy.")]),
            _dim("pharmacy", "dim_ndc", "NDC", "National drug code.", 50_000, [L("drug_class_id", "dim_drug_class", "n1")], [M("ndc_code", "11-digit NDC."), M("drug_name", "Drug name.")]),
            _dim("pharmacy", "dim_formulary", "Formulary", "Drug formulary.", 30, [L("plan_id", "dim_plan", "n1")], [M("formulary_name", "Name of the formulary.")]),
            _dim("benefit", "dim_premium_schedule", "Premium Schedule", "Premium amount schedule for a plan.", 40, [L("plan_id", "dim_plan", "11!", "Each plan has one premium schedule in the window.")], [M("monthly_amount", "Monthly premium amount.")]),
            _dim("benefit", "dim_fee_schedule", "Fee Schedule", "Fee schedule used to price a service.", 80, [L("jurisdiction_id", "dim_jurisdiction", "n1!")], [M("schedule_name", "Name of the fee schedule.")]),
            _dim("benefit", "dim_hcc", "HCC", "Hierarchical condition category.", 200, [L("risk_model_id", "dim_risk_model", "n1!")], [M("hcc_code", "HCC code.")]),
            _dim("reference", "dim_procedure", "Procedure", "CPT or HCPCS procedure code.", 12_000, [L("service_category_id", "dim_service_category", "n1")], [M("procedure_code", "Procedure code."), M("procedure_name", "Short description.")]),
            _dim("reference", "dim_diagnosis", "Diagnosis", "ICD-10-CM diagnosis code.", 72_000, measures=[M("diagnosis_code", "Diagnosis code without a decimal."), M("diagnosis_name", "Short description.")]),
            _dim("reference", "dim_drg", "DRG", "Diagnosis-related group.", 800, measures=[M("drg_code", "DRG code.")]),
            _dim("reference", "dim_carc", "CARC", "Claim adjustment reason code.", 300, measures=[M("carc_code", "CARC."), M("carc_text", "Reason text.")]),
            _dim("reference", "dim_rarc", "RARC", "Remittance advice remark code.", 1_100, measures=[M("rarc_code", "RARC.")]),
            _dim("care", "dim_agent", "Service Agent", "Member-services agent.", 4_000, [L("employee_id", "dim_employee", "11", "Each agent is one employee."), L("call_queue_id", "dim_call_queue", "n1")], [M("agent_name", "Name of the agent.")]),
            _fact(
                "edi",
                "fact_edi_batch",
                "EDI Batch",
                "One inbound claim batch from a submitter.",
                900_000,
                [
                    L("submitter_id", "dim_submitter", "n1!", "Every submitter sends batches in the window."),
                    L("trading_partner_id", "dim_trading_partner", "n1!"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                ],
                [M("transaction_count", "Claim transactions declared in the batch.")],
            ),
            _fact(
                "claim",
                "fact_claim_header",
                "Claim Header",
                "One 837 claim header.",
                84_000_000,
                [
                    L("member_id", "dim_member", "n1", "Not every member has a claim in the window.", coverage=0.80),
                    L("coverage_id", "dim_coverage", "n1", coverage=0.75),
                    L("billing_provider_id", "dim_provider", "n1", "Billing provider of the claim.", coverage=0.70),
                    L("facility_id", "dim_facility", "n1?", "Professional claims may omit a facility.", match_rate=0.42, coverage=0.8),
                    L("plan_id", "dim_plan", "n1!"),
                    L("jurisdiction_id", "dim_jurisdiction", "n1!"),
                    L("insurance_line_id", "dim_insurance_line", "n1!"),
                    L("bill_type_id", "dim_bill_type", "n1?", "Professional claims have no institutional bill type.", match_rate=0.42, coverage=0.7),
                    L("place_of_service_id", "dim_place_of_service", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1!", "Receipt day. Every day receives claims."),
                    L("drg_id", "dim_drg", "n1?", "A DRG is present on a subset of inpatient claims.", match_rate=0.12, coverage=0.6),
                    L("submitter_id", "dim_submitter", "n1"),
                    L("trading_partner_id", "dim_trading_partner", "n1"),
                    L("claim_frequency_id", "dim_claim_frequency", "n1!"),
                    L("legal_entity_id", "dim_legal_entity", "n1"),
                    L("principal_diagnosis_id", "dim_diagnosis", "n1", coverage=0.4),
                    L("edi_batch_id", "fact_edi_batch", "n1!", "Every batch contains claims."),
                    L("filing_indicator_id", "dim_filing_indicator", "n1"),
                ],
                [M("billed_amount", "Total billed amount on the header."), M("claim_status", "Processing status.", "received, pended, adjudicated, denied, void")],
                synonyms=["837 header", "claim"],
            ),
            _fact(
                "claim",
                "fact_claim_admission",
                "Claim Admission",
                "Admission day of an institutional claim. Professional claims have no admission row.",
                15_120_000,
                [
                    L("claim_header_id", "fact_claim_header", "11", "An institutional claim has one admission row, and a professional claim has none."),
                    L("admission_day_id", "dim_calendar_day", "n1", "Day of admission."),
                    L("admission_type_id", "dim_admission_type", "n1!"),
                ],
                [M("length_of_stay", "Days from admission through discharge when both are known.")],
            ),
            _fact(
                "claim",
                "fact_claim_line",
                "Claim Line",
                "One 837 service line.",
                420_000_000,
                [
                    L("claim_header_id", "fact_claim_header", "n1!", "Every claim header has service lines."),
                    L("member_id", "dim_member", "n1", coverage=0.80),
                    L("rendering_provider_id", "dim_provider", "n1", "Provider who rendered the service. Billing provider stays on the claim header.", coverage=0.55),
                    L("procedure_id", "dim_procedure", "n1", coverage=0.40),
                    L("modifier_id", "dim_modifier", "n1?", "A line may have no modifier.", match_rate=0.35, coverage=0.5),
                    L("revenue_code_id", "dim_revenue_code", "n1?", "Professional lines have no revenue code.", match_rate=0.42, coverage=0.6),
                    L("place_of_service_id", "dim_place_of_service", "n1"),
                    L("service_day_id", "dim_calendar_day", "n1!", "Every day is a date of service for some line."),
                    L("facility_id", "dim_facility", "n1?", match_rate=0.42),
                    L("ndc_id", "dim_ndc", "n1?", "A drug line may cite an NDC.", match_rate=0.08, coverage=0.15),
                    L("diagnosis_id", "dim_diagnosis", "n1?", "Line-level diagnosis pointer, when present.", match_rate=0.7, coverage=0.25),
                    L("insurance_line_id", "dim_insurance_line", "n1"),
                    L("plan_id", "dim_plan", "n1"),
                    L("fee_schedule_id", "dim_fee_schedule", "n1?", match_rate=0.8),
                ],
                [M("charge_amount", "Billed charge on the line."), M("unit_count", "Service units on the line.")],
                synonyms=["service line", "837 line"],
            ),
            _fact(
                "claim",
                "fact_claim_diagnosis",
                "Claim Diagnosis",
                "One diagnosis reported on a claim header.",
                252_000_000,
                [
                    L("claim_header_id", "fact_claim_header", "n1!", "Every claim has at least one diagnosis row."),
                    L("diagnosis_id", "dim_diagnosis", "n1", coverage=0.35),
                    L("calendar_day_id", "dim_calendar_day", "n1"),
                ],
                [M("diagnosis_sequence", "Sequence of the diagnosis on the claim.")],
            ),
            _fact(
                "remit",
                "fact_remit_advice",
                "Remit Advice",
                "One 835 remittance advice.",
                12_000_000,
                [
                    L("billing_provider_id", "dim_provider", "n1", coverage=0.65),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("payment_method_id", "dim_payment_method", "n1!"),
                    L("bank_id", "dim_bank", "n1?", match_rate=0.9),
                    L("jurisdiction_id", "dim_jurisdiction", "n1"),
                    L("trading_partner_id", "dim_trading_partner", "n1"),
                ],
                [M("payment_amount", "Total payment on the advice.")],
            ),
            _fact(
                "remit",
                "fact_remit_line",
                "Remit Line",
                "One 835 service payment line.",
                504_000_000,
                [
                    L("remit_advice_id", "fact_remit_advice", "n1!", "Every remittance advice has service lines."),
                    L("claim_line_id", "fact_claim_line", "n1", "Some service lines are still pended and have no remit line.", coverage=0.96),
                    L("claim_header_id", "fact_claim_header", "n1", coverage=0.98),
                    L("carc_id", "dim_carc", "n1?", "A paid line may have no adjustment reason.", match_rate=0.55, coverage=0.8),
                    L("member_id", "dim_member", "n1", coverage=0.8),
                    L("provider_id", "dim_provider", "n1", coverage=0.65),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                ],
                [M("paid_amount", "Amount paid on the remit line."), M("allowed_amount", "Allowed amount on the remit line.")],
            ),
            _fact(
                "remit",
                "fact_remit_adjustment",
                "Remit Adjustment",
                "One CAS adjustment on a remit line.",
                630_000_000,
                [
                    L("remit_line_id", "fact_remit_line", "n1", "Not every remit line carries an adjustment.", coverage=0.70),
                    L("carc_id", "dim_carc", "n1!"),
                    L("rarc_id", "dim_rarc", "n1?", match_rate=0.7, coverage=0.4),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                ],
                [M("adjustment_amount", "Adjustment amount.")],
            ),
            _fact(
                "eligibility",
                "fact_eligibility_inquiry",
                "Eligibility Inquiry",
                "One X12 270 eligibility inquiry.",
                336_000_000,
                [
                    L("member_id", "dim_member", "n1", coverage=0.90),
                    L("coverage_id", "dim_coverage", "n1", coverage=0.85),
                    L("provider_id", "dim_provider", "n1", coverage=0.50),
                    L("trading_partner_id", "dim_trading_partner", "n1!"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("plan_id", "dim_plan", "n1"),
                    L("jurisdiction_id", "dim_jurisdiction", "n1"),
                ],
                [M("inquiry_type", "Kind of eligibility question.", "coverage, benefit, copay, deductible")],
            ),
            _fact(
                "eligibility",
                "fact_eligibility_response",
                "Eligibility Response",
                "One X12 271 response to an eligibility inquiry.",
                336_000_000,
                [
                    L("eligibility_inquiry_id", "fact_eligibility_inquiry", "11!", "Each inquiry has one response, and each response has one inquiry."),
                    L("member_id", "dim_member", "n1", coverage=0.90),
                    L("plan_id", "dim_plan", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                ],
                [M("response_status", "Eligibility response status.", "active, inactive, rejected")],
            ),
            _fact(
                "claim",
                "fact_claim_status",
                "Claim Status",
                "One claim-status event for a header.",
                168_000_000,
                [
                    L("claim_header_id", "fact_claim_header", "n1!", "Every header has status events."),
                    L("trading_partner_id", "dim_trading_partner", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("submitter_id", "dim_submitter", "n1"),
                ],
                [M("status_code", "Claim status category.", "received, accepted, rejected, pended, finalized, paid")],
            ),
            _fact(
                "pharmacy",
                "fact_pharmacy_claim",
                "Pharmacy Claim",
                "One NCPDP pharmacy claim.",
                136_000_000,
                [
                    L("member_id", "dim_member", "n1", coverage=0.45),
                    L("pharmacy_id", "dim_pharmacy", "n1", coverage=0.92),
                    L("prescriber_id", "dim_prescriber", "n1", coverage=0.60),
                    L("ndc_id", "dim_ndc", "n1", coverage=0.25),
                    L("plan_id", "dim_plan", "n1"),
                    L("formulary_id", "dim_formulary", "n1?", match_rate=0.8),
                    L("tier_id", "dim_tier", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("insurance_line_id", "dim_insurance_line", "n1"),
                ],
                [M("ingredient_cost", "Ingredient cost."), M("dispensing_fee", "Dispensing fee."), M("quantity", "Quantity dispensed.")],
            ),
            _fact(
                "benefit",
                "fact_accumulator_entry",
                "Accumulator Entry",
                "One benefit-accumulator posting from adjudication.",
                420_000_000,
                [
                    L("member_id", "dim_member", "n1", coverage=0.80),
                    L("accumulator_type_id", "dim_accumulator_type", "n1!"),
                    L("claim_line_id", "fact_claim_line", "n1", "Each posting cites one service line.", coverage=0.90),
                    L("plan_id", "dim_plan", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                ],
                [M("applied_amount", "Amount applied to the accumulator.")],
            ),
            _fact(
                "benefit",
                "fact_accumulator_snapshot",
                "Accumulator Snapshot",
                "Month-end accumulator balance for one member and one accumulator type.",
                544_000_000,
                [
                    L("member_id", "dim_member", "n1!", "Every member has a snapshot row for each accumulator type."),
                    L("accumulator_type_id", "dim_accumulator_type", "n1!", "Every accumulator type is snapshotted."),
                    L("plan_id", "dim_plan", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1"),
                ],
                [M("balance_amount", "Balance at month end.")],
                volume_class="periodic_snapshot",
            ),
            _fact(
                "claim",
                "fact_pricing_result",
                "Pricing Result",
                "One fee-schedule pricing result for a service line.",
                420_000_000,
                [
                    L("claim_line_id", "fact_claim_line", "11!", "Each service line has one pricing result."),
                    L("fee_schedule_id", "dim_fee_schedule", "n1!"),
                    L("procedure_id", "dim_procedure", "n1", coverage=0.40),
                    L("locality_id", "dim_locality", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1"),
                ],
                [M("allowed_amount", "Priced allowed amount.")],
            ),
            _fact(
                "claim",
                "fact_claim_edit",
                "Claim Edit",
                "One pre-adjudication edit result on a claim header.",
                210_000_000,
                [
                    L("claim_header_id", "fact_claim_header", "n1!", "Every header receives edit results."),
                    L("edit_code_id", "dim_edit_code", "n1", coverage=0.75),
                    L("claim_line_id", "fact_claim_line", "n1?", "Header-level edits have no line.", match_rate=0.8),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                ],
                [M("edit_disposition", "What the edit did.", "informational, pend, deny")],
            ),
            _fact("um", "fact_prior_auth", "Prior Authorization", "One prior authorization.", 2_400_000, [L("member_id", "dim_member", "n1", coverage=0.03), L("provider_id", "dim_provider", "n1", coverage=0.1), L("auth_type_id", "dim_auth_type", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1"), L("plan_id", "dim_plan", "n1"), L("employee_id", "dim_employee", "n1?", match_rate=0.4)], [M("auth_status", "Status of the authorization.", "pended, approved, denied, void")]),
            _fact("um", "fact_auth_line", "Authorization Line", "One service line requested on a prior authorization.", 6_000_000, [L("prior_auth_id", "fact_prior_auth", "n1!", "Every authorization has lines."), L("procedure_id", "dim_procedure", "n1", coverage=0.1), L("calendar_day_id", "dim_calendar_day", "n1")], [M("requested_units", "Units requested.")]),
            _fact("um", "fact_auth_decision", "Authorization Decision", "One decision on a prior authorization.", 2_400_000, [L("prior_auth_id", "fact_prior_auth", "11!", "Each authorization has one current decision."), L("employee_id", "dim_employee", "n1"), L("calendar_day_id", "dim_calendar_day", "n1"), L("denial_reason_id", "dim_denial_reason", "n1?", match_rate=0.2)], [M("decision", "Decision.", "approved, denied, partial")]),
            _fact("remit", "fact_cob_line", "COB Line", "One coordination-of-benefits amount on a service line.", 36_000_000, [L("claim_line_id", "fact_claim_line", "n1", coverage=0.08), L("cob_type_id", "dim_cob_type", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1"), L("trading_partner_id", "dim_trading_partner", "n1?", match_rate=0.5)], [M("other_paid_amount", "Amount paid by the other payer.")]),
            _fact("claim", "fact_encounter", "Encounter", "One Medicare Advantage encounter submission.", 50_000_000, [L("member_id", "dim_member", "n1", coverage=0.30), L("provider_id", "dim_provider", "n1", coverage=0.2), L("facility_id", "dim_facility", "n1?", match_rate=0.4), L("plan_id", "dim_plan", "n1"), L("calendar_day_id", "dim_calendar_day", "n1!"), L("place_of_service_id", "dim_place_of_service", "n1")], [M("encounter_status", "Submission status.", "accepted, rejected, void")]),
            _fact("premium", "fact_premium_bill", "Premium Bill", "One monthly premium bill for a member.", 68_000_000, [L("member_id", "dim_member", "11!", "Each member has one premium bill in the window."), L("plan_id", "dim_plan", "n1"), L("premium_schedule_id", "dim_premium_schedule", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("billed_amount", "Premium billed.")], volume_class="periodic_snapshot"),
            _fact("premium", "fact_premium_payment", "Premium Payment", "One premium payment.", 60_000_000, [L("premium_bill_id", "fact_premium_bill", "n1", coverage=0.88), L("payment_method_id", "dim_payment_method", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1!"), L("member_id", "dim_member", "n1", coverage=0.85)], [M("paid_amount", "Premium paid.")]),
            _fact("premium", "fact_capitation", "Capitation Payment", "One capitation payment line.", 8_000_000, [L("provider_id", "dim_provider", "n1", coverage=0.05), L("plan_id", "dim_plan", "n1"), L("calendar_day_id", "dim_calendar_day", "n1"), L("member_id", "dim_member", "n1?", "Some capitation is paid per panel, not per member.", match_rate=0.7)], [M("capitation_amount", "Capitation amount.")]),
            _fact("remit", "fact_provider_payment", "Provider Payment", "One EFT or check to a provider.", 12_000_000, [L("provider_id", "dim_provider", "n1", coverage=0.4), L("calendar_day_id", "dim_calendar_day", "n1!"), L("bank_id", "dim_bank", "n1"), L("jurisdiction_id", "dim_jurisdiction", "n1"), L("remit_advice_id", "fact_remit_advice", "n1?", match_rate=0.9)], [M("payment_amount", "Amount of the payment instrument.")]),
            _fact("appeal", "fact_appeal", "Appeal", "One claim appeal.", 180_000, [L("claim_header_id", "fact_claim_header", "n1"), L("member_id", "dim_member", "n1"), L("appeal_level_id", "dim_appeal_level", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1"), L("employee_id", "dim_employee", "n1?", match_rate=0.8)], [M("appeal_status", "Status of the appeal.", "open, upheld, overturned, dismissed")]),
            _fact("appeal", "fact_appeal_decision", "Appeal Decision", "One decision on an appeal.", 150_000, [L("appeal_id", "fact_appeal", "n1", coverage=0.83), L("employee_id", "dim_employee", "n1"), L("calendar_day_id", "dim_calendar_day", "n1"), L("denial_reason_id", "dim_denial_reason", "n1?", match_rate=0.4)], [M("decision", "Decision.", "upheld, overturned, partial")]),
            _fact("claim", "fact_medical_review", "Medical Review", "One medical-review action on a service line.", 900_000, [L("claim_line_id", "fact_claim_line", "n1", coverage=0.002), L("review_type_id", "dim_review_type", "n1!"), L("employee_id", "dim_employee", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("review_outcome", "Outcome.", "pay, deny, pend, education")]),
            _fact("claim", "fact_attachment", "Claim Attachment", "One attachment linked to a claim header.", 2_500_000, [L("claim_header_id", "fact_claim_header", "n1", coverage=0.02), L("document_type_id", "dim_document_type", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("page_count", "Pages in the attachment.")]),
            _fact("um", "fact_referral", "Referral", "One referral from one provider to another.", 1_100_000, [L("member_id", "dim_member", "n1"), L("referring_provider_id", "dim_provider", "n1", "Provider who referred.", coverage=0.05), L("calendar_day_id", "dim_calendar_day", "n1"), L("plan_id", "dim_plan", "n1")], [M("referral_status", "Status.", "open, used, expired, denied")]),
            _fact("um", "fact_referral_target", "Referral Target", "Provider who received one referral.", 1_100_000, [L("referral_id", "fact_referral", "11!", "Each referral has one target provider row."), L("referred_provider_id", "dim_provider", "n1", "Provider who received the referral.", coverage=0.08)], [M("target_status", "Whether the target accepted the referral.", "pending, accepted, declined")]),
            _fact("member", "fact_pcp_attribution", "PCP Attribution", "Month-end primary-care attribution of a member.", 68_000_000, [L("member_id", "dim_member", "11!", "Each member has one attribution row."), L("provider_id", "dim_provider", "n1", coverage=0.15), L("plan_id", "dim_plan", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("attribution_method", "How the PCP was chosen.", "election, claims, default")], volume_class="periodic_snapshot"),
            _fact("member", "fact_risk_score", "Risk Score", "Month-end risk score of a member.", 68_000_000, [L("member_id", "dim_member", "11!", "Each member has one risk score in the window."), L("risk_model_id", "dim_risk_model", "n1!"), L("plan_id", "dim_plan", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("risk_score", "Risk score value.")], volume_class="periodic_snapshot"),
            _fact("member", "fact_hcc_diagnosis", "HCC Diagnosis", "One diagnosis captured for risk adjustment.", 96_000_000, [L("member_id", "dim_member", "n1", coverage=0.40), L("diagnosis_id", "dim_diagnosis", "n1", coverage=0.08), L("hcc_id", "dim_hcc", "n1?", match_rate=0.7), L("risk_model_id", "dim_risk_model", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("source", "Where the diagnosis was captured.", "claim, encounter, chart")]),
            _fact("member", "fact_enrollment_span", "Enrollment Span", "One current enrollment span for a coverage.", 72_000_000, [L("coverage_id", "dim_coverage", "11!", "Each coverage has one current enrollment span."), L("plan_id", "dim_plan", "n1"), L("start_day_id", "dim_calendar_day", "n1?", "Spans that started before the window have no start day inside it.", match_rate=0.04)], [M("span_status", "Status of the span.", "active, ended")], volume_class="accumulating_snapshot"),
            _fact("member", "fact_disenrollment", "Disenrollment", "One disenrollment event.", 1_200_000, [L("member_id", "dim_member", "n1"), L("coverage_id", "dim_coverage", "n1"), L("calendar_day_id", "dim_calendar_day", "n1"), L("plan_id", "dim_plan", "n1")], [M("disenroll_reason", "Reason.", "death, move, voluntary, other-coverage")]),
            _fact("premium", "fact_premium_adjustment", "Premium Adjustment", "One adjustment to a premium bill.", 800_000, [L("premium_bill_id", "fact_premium_bill", "n1"), L("member_id", "dim_member", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("adjustment_amount", "Signed premium adjustment.")]),
            _fact("premium", "fact_low_income_subsidy", "Low Income Subsidy", "One low-income subsidy determination.", 6_000_000, [L("member_id", "dim_member", "n1", coverage=0.08), L("lis_level_id", "dim_lis_level", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("subsidy_amount", "Monthly subsidy amount.")]),
            _fact("care", "fact_call", "Service Call", "One member-services call.", 8_000_000, [L("member_id", "dim_member", "n1?", match_rate=0.85, coverage=0.1), L("agent_id", "dim_agent", "n1!", "Every agent takes calls."), L("call_queue_id", "dim_call_queue", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1!")], [M("handle_seconds", "Handle time.")]),
            _fact("care", "fact_call_event", "Call Event", "One event inside a service call.", 24_000_000, [L("call_id", "fact_call", "n1!", "Every call has events."), L("agent_id", "dim_agent", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("event_type", "Kind of call event.", "answer, transfer, hold, disposition")]),
            _fact("care", "fact_letter", "Letter", "One letter sent to a member.", 5_000_000, [L("member_id", "dim_member", "n1", coverage=0.06), L("document_type_id", "dim_document_type", "n1"), L("calendar_day_id", "dim_calendar_day", "n1!")], [M("mail_status", "Mail status.", "queued, sent, returned")]),
            _fact("care", "fact_portal_event", "Portal Event", "One authenticated member-portal event.", 45_000_000, [L("member_id", "dim_member", "n1", coverage=0.25), L("calendar_day_id", "dim_calendar_day", "n1!")], [M("event_name", "Portal action.", "login, claim-view, id-card, payment")]),
            _fact("care", "fact_audit_sample", "Audit Sample", "One claim drawn into an audit sample.", 50_000, [L("audit_program_id", "dim_audit_program", "n1!"), L("claim_header_id", "fact_claim_header", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("sample_weight", "Weight of the sample row.")]),
            _fact("care", "fact_fraud_lead", "Fraud Lead", "One fraud lead.", 30_000, [L("fraud_scheme_id", "dim_fraud_scheme", "n1!"), L("provider_id", "dim_provider", "n1?", match_rate=0.7), L("member_id", "dim_member", "n1?", match_rate=0.4), L("calendar_day_id", "dim_calendar_day", "n1")], [M("lead_status", "Status.", "open, referred, closed")]),
            _fact("provider", "fact_provider_enrollment", "Provider Enrollment", "One provider enrollment application.", 40_000, [L("provider_id", "dim_provider", "n1"), L("calendar_day_id", "dim_calendar_day", "n1"), L("jurisdiction_id", "dim_jurisdiction", "n1!"), L("enrollment_status_id", "dim_enrollment_status", "n1!")], [M("application_source", "How the application arrived.", "PECOS, paper")]),
            _fact("provider", "fact_revalidation", "Revalidation", "One provider revalidation.", 20_000, [L("provider_id", "dim_provider", "n1"), L("calendar_day_id", "dim_calendar_day", "n1"), L("jurisdiction_id", "dim_jurisdiction", "n1")], [M("revalidation_result", "Result.", "approved, deactivated, pending")]),
            _fact("claim", "fact_claim_note", "Claim Note", "One note on a claim header.", 10_000_000, [L("claim_header_id", "fact_claim_header", "n1", coverage=0.08), L("note_type_id", "dim_note_type", "n1!"), L("employee_id", "dim_employee", "n1?", match_rate=0.6), L("calendar_day_id", "dim_calendar_day", "n1")], [M("note_text", "Short note.")]),
            _fact("remit", "fact_interest_payment", "Interest Payment", "One interest payment on a late claim.", 200_000, [L("claim_header_id", "fact_claim_header", "n1"), L("interest_reason_id", "dim_interest_reason", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1"), L("provider_id", "dim_provider", "n1")], [M("interest_amount", "Interest amount.")]),
            _fact("remit", "fact_withhold", "Withhold", "One withhold against a provider payment.", 100_000, [L("provider_payment_id", "fact_provider_payment", "n1"), L("withhold_reason_id", "dim_withhold_reason", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("withhold_amount", "Amount withheld.")]),
            _fact("remit", "fact_overpayment", "Overpayment", "One identified overpayment.", 400_000, [L("claim_header_id", "fact_claim_header", "n1"), L("provider_id", "dim_provider", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("overpaid_amount", "Overpaid amount.")]),
            _fact("remit", "fact_recovery", "Recovery", "One recovery against an overpayment.", 250_000, [L("overpayment_id", "fact_overpayment", "n1", coverage=0.6), L("calendar_day_id", "dim_calendar_day", "n1"), L("provider_id", "dim_provider", "n1")], [M("recovered_amount", "Amount recovered.")]),
            _fact("care", "fact_grievance", "Grievance", "One member grievance.", 90_000, [L("member_id", "dim_member", "n1"), L("plan_id", "dim_plan", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("grievance_category", "Category.", "access, quality, billing, privacy")]),
            _fact("benefit", "fact_fee_schedule_rate", "Fee Schedule Rate", "One procedure rate on a fee schedule.", 2_000_000, [L("fee_schedule_id", "dim_fee_schedule", "n1!"), L("procedure_id", "dim_procedure", "n1", coverage=0.5), L("locality_id", "dim_locality", "n1")], [M("rate_amount", "Allowed rate.")]),
            _bridge("bridge_plan_benefit", "Plan Benefit", "Benefit packaged on a plan.", 600, [L("plan_id", "dim_plan", "n1!"), L("benefit_id", "dim_benefit", "11!")]),
            _bridge("bridge_provider_network", "Provider Network Participation", "Network participation of a provider.", 2_000_000, [L("provider_id", "dim_provider", "n1", coverage=0.8), L("network_id", "dim_network", "n1!")]),
            _bridge("bridge_provider_specialty", "Provider Specialty", "Specialty attested by a provider.", 1_500_000, [L("provider_id", "dim_provider", "n1", coverage=0.9), L("specialty_id", "dim_specialty", "n1!")]),
            _bridge("bridge_facility_network", "Facility Network", "Network participation of a facility.", 200_000, [L("facility_id", "dim_facility", "n1"), L("network_id", "dim_network", "n1!")]),
            _bridge("bridge_member_language", "Member Language", "Preferred language of a member.", 68_000_000, [L("member_id", "dim_member", "11!"), L("language_id", "dim_language", "n1!")]),
            _bridge("bridge_coverage_rider", "Coverage Rider", "Optional rider on a coverage.", 4_000_000, [L("coverage_id", "dim_coverage", "n1", coverage=0.05), L("benefit_id", "dim_benefit", "n1")]),
            _bridge("bridge_formulary_drug", "Formulary Drug", "NDC placed on a formulary tier.", 400_000, [L("formulary_id", "dim_formulary", "n1!"), L("ndc_id", "dim_ndc", "n1", coverage=0.5), L("tier_id", "dim_tier", "n1!")]),
            _bridge("bridge_plan_category", "Plan Category", "Service category covered by a plan.", 800, [L("plan_id", "dim_plan", "n1!"), L("service_category_id", "dim_service_category", "n1")]),
            _bridge("bridge_group_benefit", "Group Benefit", "Benefit variation for an employer group.", 20_000, [L("group_id", "dim_group", "n1!"), L("benefit_id", "dim_benefit", "n1")]),
            _bridge("bridge_jurisdiction_state", "Jurisdiction State", "State included in a jurisdiction.", 60, [L("jurisdiction_id", "dim_jurisdiction", "n1!"), L("state_id", "dim_state", "n1")]),
            _bridge("bridge_diagnosis_hcc", "Diagnosis HCC", "HCC mapping of a diagnosis.", 80_000, [L("diagnosis_id", "dim_diagnosis", "n1", coverage=0.4), L("hcc_id", "dim_hcc", "n1!")]),
            _bridge("bridge_procedure_category", "Procedure Category", "Service category of a procedure.", 12_000, [L("procedure_id", "dim_procedure", "11!"), L("service_category_id", "dim_service_category", "n1!")]),
            _bridge("bridge_employee_jurisdiction", "Employee Jurisdiction", "Jurisdiction an employee can work.", 15_000, [L("employee_id", "dim_employee", "11!"), L("jurisdiction_id", "dim_jurisdiction", "n1!")]),
            _bridge("bridge_pharmacy_network", "Pharmacy Network", "Network participation of a pharmacy.", 80_000, [L("pharmacy_id", "dim_pharmacy", "n1"), L("network_id", "dim_network", "n1!")]),
            _bridge("bridge_prescriber_specialty", "Prescriber Specialty", "Specialty of a prescriber.", 400_000, [L("prescriber_id", "dim_prescriber", "11!"), L("specialty_id", "dim_specialty", "n1")]),
            _bridge("bridge_cob_coverage", "COB Coverage", "Other coverage recorded for coordination of benefits.", 2_000_000, [L("coverage_id", "dim_coverage", "n1", coverage=0.02), L("cob_type_id", "dim_cob_type", "n1!")]),
            _bridge("bridge_edit_line", "Edit Applicability", "Insurance line an edit code applies to.", 1_500, [L("edit_code_id", "dim_edit_code", "11!"), L("insurance_line_id", "dim_insurance_line", "n1!")]),
            _bridge("bridge_revenue_procedure", "Revenue Procedure", "Procedure commonly billed with a revenue code.", 8_000, [L("revenue_code_id", "dim_revenue_code", "n1!"), L("procedure_id", "dim_procedure", "n1")]),
            _bridge("bridge_drg_diagnosis", "DRG Diagnosis", "Diagnosis associated with a DRG.", 5_000, [L("drg_id", "dim_drg", "n1!"), L("diagnosis_id", "dim_diagnosis", "n1")]),
            _bridge("bridge_plan_formulary", "Plan Formulary", "Formulary adopted by a plan.", 40, [L("plan_id", "dim_plan", "11!"), L("formulary_id", "dim_formulary", "n1")]),
            _bridge("bridge_network_plan", "Network Plan", "Network offered on a plan.", 80, [L("network_id", "dim_network", "n1!"), L("plan_id", "dim_plan", "n1!")]),
            _bridge("bridge_facility_taxonomy", "Facility Taxonomy", "Taxonomy of a facility.", 180_000, [L("facility_id", "dim_facility", "11!"), L("taxonomy_id", "dim_taxonomy", "n1")]),
            _bridge("bridge_state_locality", "State Locality", "Locality inside a state.", 200, [L("state_id", "dim_state", "n1!"), L("locality_id", "dim_locality", "n1")]),
            _bridge("bridge_provider_facility", "Provider Facility", "Facility where a provider practices.", 250_000, [L("provider_id", "dim_provider", "n1", coverage=0.15), L("facility_id", "dim_facility", "n1")]),
            _bridge("bridge_member_address", "Member Address", "Residential address of a member.", 68_000_000, [L("member_id", "dim_member", "11!"), L("address_id", "dim_address", "11", "Each member address row matches one address, and some addresses are not residential.")]),
            _bridge("bridge_contract_plan", "Contract Plan", "Already represented on the contract dimension; this bridge records historical contract-to-plan assignment inside the window.", 120, [L("contract_id", "dim_contract", "11!"), L("plan_id", "dim_plan", "n1!")]),
        ]
    )
    return build_datasets(tables)


DATASETS = _datasets()

DOMAIN = {
    "key": "healthcare-payer",
    "business_name": "Harbor Medicare Services",
    "database": "HEALTHCARE_PAYER",
    "account": "harbor.us-east-1",
    "root": "healthcare-payer",
    "narrative": _NARRATIVE.strip(),
    "provenance": _PROVENANCE.strip(),
    "statistics_window_days": 30,
    "identity_synonyms": {
        "member_identity": ["beneficiary", "enrollee"],
        "provider_identity": ["NPI", "billing provider"],
        "claim_header_identity": ["837 claim", "claim"],
        "claim_line_identity": ["service line"],
    },
    "readme_intro": """
Harbor Medicare Services processes Medicare-scale claims. The catalog `healthcare-payer` is the ontology of eligibility, 837 submission, adjudication, 835 remittance, pharmacy, premium billing, and benefit accumulation: datasets in the Snowflake database `HEALTHCARE_PAYER`.

A claim header and a claim line are different facts. A remittance advice, a remit line, and a remit adjustment are different facts. An eligibility inquiry has one response. Members, coverage, providers, plans, and code sets are the populations those facts join. The questions below use the authored identities and joins. Synthetic row counts and fan-out for a 30-day window are listed with the major fact tables.
""".strip(),
    "readme_questions": _QUESTIONS.strip(),
    "signatures": [
        {
            "child": "fact_claim_line",
            "parent": "fact_claim_header",
            "identity": "claim_header_identity",
            "parent_multiplicity": "1:many",
            "parent_existence": "always",
            "child_multiplicity": "many:1",
            "child_existence": "always",
        },
        {
            "child": "fact_eligibility_response",
            "parent": "fact_eligibility_inquiry",
            "identity": "eligibility_inquiry_identity",
            "parent_multiplicity": "1:1",
            "parent_existence": "always",
            "child_multiplicity": "1:1",
            "child_existence": "always",
        },
        {
            "child": "dim_coverage",
            "parent": "dim_member",
            "identity": "member_identity",
            "parent_multiplicity": "1:many",
            "parent_existence": "always",
            "child_multiplicity": "many:1",
            "child_existence": "always",
        },
        {
            "child": "fact_pricing_result",
            "parent": "fact_claim_line",
            "identity": "claim_line_identity",
            "parent_multiplicity": "1:1",
            "parent_existence": "always",
            "child_multiplicity": "1:1",
            "child_existence": "always",
        },
    ],
    "major_facts": [
        {
            "dataset": "fact_remit_adjustment",
            "landing": "CAS adjustment segments land here, one row per reason on a paid or denied remit line.",
            "basis": "Authored above the remit-line population because an 835 service line can carry more than one adjustment group. Coverage of remit lines is 70 percent.",
        },
        {
            "dataset": "fact_accumulator_snapshot",
            "landing": "Month-end benefit balances land here, one row per member per accumulator type.",
            "basis": "68 million members times 8 accumulator types = 544 million rows. This is a periodic snapshot, not a claim.",
        },
        {
            "dataset": "fact_remit_line",
            "landing": "835 service-payment lines land here. This is the payment event grain.",
            "basis": "Authored at 1.25 remit rows per adjudicated service line, on 96 percent of the 420 million service lines, grouped onto 12 million remittance advices.",
        },
        {
            "dataset": "fact_claim_line",
            "landing": "837 service lines are the atomic medical-claim landing zone.",
            "basis": "Authored at five lines per claim header. Headers are the CMS-scale 84 million claims in the window.",
        },
        {
            "dataset": "fact_pricing_result",
            "landing": "Fee-schedule pricing results land here, one per service line.",
            "basis": "One-to-one with the 420 million service lines.",
        },
        {
            "dataset": "fact_accumulator_entry",
            "landing": "Adjudication postings to deductibles and out-of-pocket accumulators land here.",
            "basis": "Authored at one ledger posting per service line, joined to 90 percent of lines.",
        },
        {
            "dataset": "fact_eligibility_inquiry",
            "landing": "X12 270 eligibility inquiries land here.",
            "basis": "Authored at four inquiries per claim header. The multiple is synthetic. It is not a published HETS count.",
        },
        {
            "dataset": "fact_eligibility_response",
            "landing": "X12 271 eligibility responses land here, one per inquiry.",
            "basis": "Equal to the inquiry population because every inquiry has one response.",
        },
        {
            "dataset": "fact_claim_diagnosis",
            "landing": "Claim diagnosis rows land here for reporting and risk inputs.",
            "basis": "Authored at three diagnoses per claim header.",
        },
        {
            "dataset": "fact_claim_edit",
            "landing": "Pre-adjudication edit results land here.",
            "basis": "Authored at 2.5 edit results per claim header.",
        },
        {
            "dataset": "fact_claim_status",
            "landing": "Claim-status events land here as the header moves through receipt, acceptance, and finalization.",
            "basis": "Authored at two status events per claim header.",
        },
        {
            "dataset": "fact_pharmacy_claim",
            "landing": "NCPDP pharmacy claims land here, separate from 837 service lines.",
            "basis": "Authored at two fills per member per month across 68 million members.",
        },
        {
            "dataset": "fact_claim_header",
            "landing": "837 claim headers land here. Volume concentrates on the lines, but the header is the claim grain those lines require.",
            "basis": "84 million headers in 30 days annualize to 1.008 billion, consistent with CMS reporting more than one billion Medicare fee-for-service claims a year.",
        },
    ],
    "datasets": DATASETS,
}
