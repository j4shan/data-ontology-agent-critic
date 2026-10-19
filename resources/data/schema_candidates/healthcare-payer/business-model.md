# Harbor Medicare Services

Harbor Medicare Services is a fictional processor operating at Medicare Administrative Contractor scale. The catalog is the warehouse-style ontology of eligibility, claim submission, adjudication, remittance, pharmacy, premium billing, and benefit accumulation. Members, coverage spans, providers, plans, and code sets are conformed dimensions. Claims, service lines, remittance, and eligibility transactions are facts.

A claim is not one row. The X12 837 claim has a header and many service lines, and those grains stay in separate facts. Professional, institutional, and DME claims share the header and line facts and are distinguished by insurance line, bill type, and revenue code. Remittance follows the X12 835 shape: a remittance advice, many service lines, and adjustment rows for claim-adjustment reason codes. Eligibility is a 270 inquiry and a 271 response, one response per inquiry. Pharmacy claims are a separate NCPDP-style fact. Benefit accumulators land both as an adjudication ledger and as a month-end snapshot by member and accumulator type.

The 30-day populations are synthetic. The member count and the claim-header count are set so the window is consistent with published Medicare fee-for-service scale. Line, remittance, eligibility, and accumulator fan-out are authored on top of that anchor. Statistics sit beside the catalog.

## Data ecosystem

The authored catalog `healthcare-payer` contains 157 datasets (78 dimensions, 53 facts, 26 bridges) in the Snowflake database `HEALTHCARE_PAYER` on account `harbor.us-east-1`.

Each dataset is one ontology node. The grain column is the system of record for that dataset's logical identity and is marked `is_entity_universe: true`. Foreign-key columns realize the same logical identity with `is_entity_universe: false`, because the child dataset does not hold the complete population. Edges join those two realizations. Multiplicity and match existence are directional and follow the operating rules below. Synthetic row counts and join fan-out for a 30-day window are in `statistics.md`. They are derived from authored populations and these multiplicity rules. The YAML nodes do not carry those statistics.

## Signature relationships

| Relationship | Identity | Parent to child | Child to parent | Rule |
| --- | --- | --- | --- | --- |
| `fact_claim_header` to `fact_claim_line` | `claim_header_identity` | 1:many (always) | many:1 (always) | Many claim Lines belong to one claim Header, every claim Line matches a claim Header, and every claim Header includes at least one claim Line. Every claim header has service lines. |
| `fact_eligibility_inquiry` to `fact_eligibility_response` | `eligibility_inquiry_identity` | 1:1 (always) | 1:1 (always) | Each eligibility Response matches exactly one eligibility Inquiry, and each eligibility Inquiry matches exactly one eligibility Response. Each inquiry has one response, and each response has one inquiry. |
| `dim_member` to `dim_coverage` | `member_identity` | 1:many (always) | many:1 (always) | Many coverages belong to one member, every coverage matches a member, and every member includes at least one coverage. Every member has at least one coverage. |
| `fact_claim_line` to `fact_pricing_result` | `claim_line_identity` | 1:1 (always) | 1:1 (always) | Each pricing Result matches exactly one claim Line, and each claim Line matches exactly one pricing Result. Each service line has one pricing result. |

## Relationship rules

| Child dataset | Column | Universe dataset | Mapping | Parent match | Child match | Rule |
| --- | --- | --- | --- | --- | --- | --- |
| `dim_legal_entity` | `enterprise_id` | `dim_enterprise` | 1:N | 1:many / always | many:1 / always | Many legal Entities belong to one enterprise, every legal Entity matches a enterprise, and every enterprise includes at least one legal Entity. |
| `dim_jurisdiction` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many jurisdictions belong to one legal Entity, every jurisdiction matches a legal Entity, and a legal Entity may include no jurisdiction. |
| `dim_department` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many departments belong to one legal Entity, every department matches a legal Entity, and a legal Entity may include no department. |
| `dim_cost_center` | `department_id` | `dim_department` | 1:N | 1:many / always | many:1 / always | Many cost Centers belong to one department, every cost Center matches a department, and every department includes at least one cost Center. |
| `dim_employee` | `department_id` | `dim_department` | 1:N | 1:many / optional | many:1 / always | Many employees belong to one department, every employee matches a department, and a department may include no employee. |
| `dim_employee` | `cost_center_id` | `dim_cost_center` | 1:N | 1:many / optional | many:1 / always | Many employees belong to one cost Center, every employee matches a cost Center, and a cost Center may include no employee. |
| `dim_employee` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / optional | many:1 / always | Many employees belong to one jurisdiction, every employee matches a jurisdiction, and a jurisdiction may include no employee. |
| `dim_gl_account` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many gL Accounts belong to one legal Entity, every gL Account matches a legal Entity, and a legal Entity may include no gL Account. |
| `dim_locality` | `state_id` | `dim_state` | 1:N | 1:many / always | many:1 / always | Many payment Localities belong to one state, every payment Locality matches a state, and every state includes at least one payment Locality. |
| `dim_submitter` | `trading_partner_id` | `dim_trading_partner` | 1:N | 1:many / always | many:1 / always | Many submitters belong to one trading Partner, every submitter matches a trading Partner, and every trading Partner includes at least one submitter. Every trading partner has submitters. |
| `dim_address` | `state_id` | `dim_state` | 1:N | 1:many / optional | many:1 / always | Many addresses belong to one state, every address matches a state, and a state may include no address. |
| `dim_member` | `state_id` | `dim_state` | 1:N | 1:many / always | many:1 / always | Many members belong to one state, every member matches a state, and every state includes at least one member. Every state has members in this national book. |
| `dim_member` | `gender_id` | `dim_gender` | 1:N | 1:many / always | many:1 / always | Many members belong to one gender, every member matches a gender, and every gender includes at least one member. |
| `dim_member` | `language_id` | `dim_language` | 1:N | 1:many / optional | many:1 / always | Many members belong to one language, every member matches a language, and a language may include no member. |
| `dim_member` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / optional | many:1 / always | Many members belong to one jurisdiction, every member matches a jurisdiction, and a jurisdiction may include no member. |
| `dim_plan` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many plans belong to one legal Entity, every plan matches a legal Entity, and a legal Entity may include no plan. |
| `dim_plan` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / optional | many:1 / always | Many plans belong to one jurisdiction, every plan matches a jurisdiction, and a jurisdiction may include no plan. |
| `dim_plan` | `lob_id` | `dim_lob` | 1:N | 1:many / always | many:1 / always | Many plans belong to one line of Business, every plan matches a line of Business, and every line of Business includes at least one plan. |
| `dim_benefit` | `plan_id` | `dim_plan` | 1:N | 1:many / always | many:1 / always | Many benefits belong to one plan, every benefit matches a plan, and every plan includes at least one benefit. Every plan has benefits. |
| `dim_contract` | `plan_id` | `dim_plan` | 1:N | 1:many / always | many:1 / always | Many cMS Contracts belong to one plan, every cMS Contract matches a plan, and every plan includes at least one cMS Contract. Every plan has at least one contract row. |
| `dim_contract` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many cMS Contracts belong to one legal Entity, every cMS Contract matches a legal Entity, and a legal Entity may include no cMS Contract. |
| `dim_group` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many employer Groups belong to one plan, every employer Group matches a plan, and a plan may include no employer Group. |
| `dim_coverage` | `member_id` | `dim_member` | 1:N | 1:many / always | many:1 / always | Many coverages belong to one member, every coverage matches a member, and every member includes at least one coverage. Every member has at least one coverage. |
| `dim_coverage` | `plan_id` | `dim_plan` | 1:N | 1:many / always | many:1 / always | Many coverages belong to one plan, every coverage matches a plan, and every plan includes at least one coverage. Every plan has coverage. |
| `dim_coverage` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many coverages belong to one legal Entity, every coverage matches a legal Entity, and a legal Entity may include no coverage. |
| `dim_coverage` | `group_id` | `dim_group` | 1:N | 1:many / optional | many:1 / optional | A coverage may match one employer Group, and a employer Group may include no coverage. Individual coverage has no employer group. |
| `dim_provider` | `taxonomy_id` | `dim_taxonomy` | 1:N | 1:many / optional | many:1 / always | Many providers belong to one provider Taxonomy, every provider matches a provider Taxonomy, and a provider Taxonomy may include no provider. |
| `dim_provider` | `state_id` | `dim_state` | 1:N | 1:many / always | many:1 / always | Many providers belong to one state, every provider matches a state, and every state includes at least one provider. |
| `dim_provider` | `specialty_id` | `dim_specialty` | 1:N | 1:many / optional | many:1 / always | Many providers belong to one specialty, every provider matches a specialty, and a specialty may include no provider. |
| `dim_facility` | `state_id` | `dim_state` | 1:N | 1:many / optional | many:1 / always | Many facilities belong to one state, every facility matches a state, and a state may include no facility. |
| `dim_facility` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / optional | A facility may match one provider, and a provider may include no facility. A facility may not yet be tied to a billing NPI. |
| `dim_prescriber` | `taxonomy_id` | `dim_taxonomy` | 1:N | 1:many / optional | many:1 / always | Many prescribers belong to one provider Taxonomy, every prescriber matches a provider Taxonomy, and a provider Taxonomy may include no prescriber. |
| `dim_prescriber` | `state_id` | `dim_state` | 1:N | 1:many / optional | many:1 / always | Many prescribers belong to one state, every prescriber matches a state, and a state may include no prescriber. |
| `dim_pharmacy` | `state_id` | `dim_state` | 1:N | 1:many / always | many:1 / always | Many pharmacies belong to one state, every pharmacy matches a state, and every state includes at least one pharmacy. |
| `dim_pharmacy` | `network_id` | `dim_network` | 1:N | 1:many / optional | many:1 / always | Many pharmacies belong to one provider Network, every pharmacy matches a provider Network, and a provider Network may include no pharmacy. |
| `dim_ndc` | `drug_class_id` | `dim_drug_class` | 1:N | 1:many / optional | many:1 / always | Many nDCs belong to one drug Class, every nDC matches a drug Class, and a drug Class may include no nDC. |
| `dim_formulary` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many formularies belong to one plan, every formulary matches a plan, and a plan may include no formulary. |
| `dim_premium_schedule` | `plan_id` | `dim_plan` | 1:1 | 1:1 / always | 1:1 / always | Each premium Schedule matches exactly one plan, and each plan matches exactly one premium Schedule. Each plan has one premium schedule in the window. |
| `dim_fee_schedule` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / always | many:1 / always | Many fee Schedules belong to one jurisdiction, every fee Schedule matches a jurisdiction, and every jurisdiction includes at least one fee Schedule. |
| `dim_hcc` | `risk_model_id` | `dim_risk_model` | 1:N | 1:many / always | many:1 / always | Many hCCs belong to one risk Model, every hCC matches a risk Model, and every risk Model includes at least one hCC. |
| `dim_procedure` | `service_category_id` | `dim_service_category` | 1:N | 1:many / optional | many:1 / always | Many procedures belong to one service Category, every procedure matches a service Category, and a service Category may include no procedure. |
| `dim_agent` | `employee_id` | `dim_employee` | 1:1 | 1:1 / optional | 1:1 / always | Each service Agent matches exactly one employee, each employee matches at most one service Agent, and not every employee is matched. Each agent is one employee. |
| `dim_agent` | `call_queue_id` | `dim_call_queue` | 1:N | 1:many / optional | many:1 / always | Many service Agents belong to one call Queue, every service Agent matches a call Queue, and a call Queue may include no service Agent. |
| `fact_edi_batch` | `submitter_id` | `dim_submitter` | 1:N | 1:many / always | many:1 / always | Many eDI Batches belong to one submitter, every eDI Batch matches a submitter, and every submitter includes at least one eDI Batch. Every submitter sends batches in the window. |
| `fact_edi_batch` | `trading_partner_id` | `dim_trading_partner` | 1:N | 1:many / always | many:1 / always | Many eDI Batches belong to one trading Partner, every eDI Batch matches a trading Partner, and every trading Partner includes at least one eDI Batch. |
| `fact_edi_batch` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many eDI Batches belong to one calendar Day, every eDI Batch matches a calendar Day, and every calendar Day includes at least one eDI Batch. |
| `fact_claim_header` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many claim Headers belong to one member, every claim Header matches a member, and a member may include no claim Header. Not every member has a claim in the window. |
| `fact_claim_header` | `coverage_id` | `dim_coverage` | 1:N | 1:many / optional | many:1 / always | Many claim Headers belong to one coverage, every claim Header matches a coverage, and a coverage may include no claim Header. |
| `fact_claim_header` | `billing_provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many claim Headers belong to one provider, every claim Header matches a provider, and a provider may include no claim Header. Billing provider of the claim. |
| `fact_claim_header` | `facility_id` | `dim_facility` | 1:N | 1:many / optional | many:1 / optional | A claim Header may match one facility, and a facility may include no claim Header. Professional claims may omit a facility. |
| `fact_claim_header` | `plan_id` | `dim_plan` | 1:N | 1:many / always | many:1 / always | Many claim Headers belong to one plan, every claim Header matches a plan, and every plan includes at least one claim Header. |
| `fact_claim_header` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / always | many:1 / always | Many claim Headers belong to one jurisdiction, every claim Header matches a jurisdiction, and every jurisdiction includes at least one claim Header. |
| `fact_claim_header` | `insurance_line_id` | `dim_insurance_line` | 1:N | 1:many / always | many:1 / always | Many claim Headers belong to one insurance Line, every claim Header matches a insurance Line, and every insurance Line includes at least one claim Header. |
| `fact_claim_header` | `bill_type_id` | `dim_bill_type` | 1:N | 1:many / optional | many:1 / optional | A claim Header may match one bill Type, and a bill Type may include no claim Header. Professional claims have no institutional bill type. |
| `fact_claim_header` | `place_of_service_id` | `dim_place_of_service` | 1:N | 1:many / optional | many:1 / always | Many claim Headers belong to one place of Service, every claim Header matches a place of Service, and a place of Service may include no claim Header. |
| `fact_claim_header` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many claim Headers belong to one calendar Day, every claim Header matches a calendar Day, and every calendar Day includes at least one claim Header. Receipt day. Every day receives claims. |
| `fact_claim_header` | `drg_id` | `dim_drg` | 1:N | 1:many / optional | many:1 / optional | A claim Header may match one dRG, and a dRG may include no claim Header. A DRG is present on a subset of inpatient claims. |
| `fact_claim_header` | `submitter_id` | `dim_submitter` | 1:N | 1:many / optional | many:1 / always | Many claim Headers belong to one submitter, every claim Header matches a submitter, and a submitter may include no claim Header. |
| `fact_claim_header` | `trading_partner_id` | `dim_trading_partner` | 1:N | 1:many / optional | many:1 / always | Many claim Headers belong to one trading Partner, every claim Header matches a trading Partner, and a trading Partner may include no claim Header. |
| `fact_claim_header` | `claim_frequency_id` | `dim_claim_frequency` | 1:N | 1:many / always | many:1 / always | Many claim Headers belong to one claim Frequency, every claim Header matches a claim Frequency, and every claim Frequency includes at least one claim Header. |
| `fact_claim_header` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many claim Headers belong to one legal Entity, every claim Header matches a legal Entity, and a legal Entity may include no claim Header. |
| `fact_claim_header` | `principal_diagnosis_id` | `dim_diagnosis` | 1:N | 1:many / optional | many:1 / always | Many claim Headers belong to one diagnosis, every claim Header matches a diagnosis, and a diagnosis may include no claim Header. |
| `fact_claim_header` | `edi_batch_id` | `fact_edi_batch` | 1:N | 1:many / always | many:1 / always | Many claim Headers belong to one eDI Batch, every claim Header matches a eDI Batch, and every eDI Batch includes at least one claim Header. Every batch contains claims. |
| `fact_claim_header` | `filing_indicator_id` | `dim_filing_indicator` | 1:N | 1:many / optional | many:1 / always | Many claim Headers belong to one filing Indicator, every claim Header matches a filing Indicator, and a filing Indicator may include no claim Header. |
| `fact_claim_admission` | `claim_header_id` | `fact_claim_header` | 1:1 | 1:1 / optional | 1:1 / always | Each claim Admission matches exactly one claim Header, each claim Header matches at most one claim Admission, and not every claim Header is matched. An institutional claim has one admission row, and a professional claim has none. |
| `fact_claim_admission` | `admission_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many claim Admissions belong to one calendar Day, every claim Admission matches a calendar Day, and a calendar Day may include no claim Admission. Day of admission. |
| `fact_claim_admission` | `admission_type_id` | `dim_admission_type` | 1:N | 1:many / always | many:1 / always | Many claim Admissions belong to one admission Type, every claim Admission matches a admission Type, and every admission Type includes at least one claim Admission. |
| `fact_claim_line` | `claim_header_id` | `fact_claim_header` | 1:N | 1:many / always | many:1 / always | Many claim Lines belong to one claim Header, every claim Line matches a claim Header, and every claim Header includes at least one claim Line. Every claim header has service lines. |
| `fact_claim_line` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many claim Lines belong to one member, every claim Line matches a member, and a member may include no claim Line. |
| `fact_claim_line` | `rendering_provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many claim Lines belong to one provider, every claim Line matches a provider, and a provider may include no claim Line. Provider who rendered the service. Billing provider stays on the claim header. |
| `fact_claim_line` | `procedure_id` | `dim_procedure` | 1:N | 1:many / optional | many:1 / always | Many claim Lines belong to one procedure, every claim Line matches a procedure, and a procedure may include no claim Line. |
| `fact_claim_line` | `modifier_id` | `dim_modifier` | 1:N | 1:many / optional | many:1 / optional | A claim Line may match one procedure Modifier, and a procedure Modifier may include no claim Line. A line may have no modifier. |
| `fact_claim_line` | `revenue_code_id` | `dim_revenue_code` | 1:N | 1:many / optional | many:1 / optional | A claim Line may match one revenue Code, and a revenue Code may include no claim Line. Professional lines have no revenue code. |
| `fact_claim_line` | `place_of_service_id` | `dim_place_of_service` | 1:N | 1:many / optional | many:1 / always | Many claim Lines belong to one place of Service, every claim Line matches a place of Service, and a place of Service may include no claim Line. |
| `fact_claim_line` | `service_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many claim Lines belong to one calendar Day, every claim Line matches a calendar Day, and every calendar Day includes at least one claim Line. Every day is a date of service for some line. |
| `fact_claim_line` | `facility_id` | `dim_facility` | 1:N | 1:many / optional | many:1 / optional | A claim Line may match one facility, and a facility may include no claim Line. |
| `fact_claim_line` | `ndc_id` | `dim_ndc` | 1:N | 1:many / optional | many:1 / optional | A claim Line may match one nDC, and a nDC may include no claim Line. A drug line may cite an NDC. |
| `fact_claim_line` | `diagnosis_id` | `dim_diagnosis` | 1:N | 1:many / optional | many:1 / optional | A claim Line may match one diagnosis, and a diagnosis may include no claim Line. Line-level diagnosis pointer, when present. |
| `fact_claim_line` | `insurance_line_id` | `dim_insurance_line` | 1:N | 1:many / optional | many:1 / always | Many claim Lines belong to one insurance Line, every claim Line matches a insurance Line, and a insurance Line may include no claim Line. |
| `fact_claim_line` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many claim Lines belong to one plan, every claim Line matches a plan, and a plan may include no claim Line. |
| `fact_claim_line` | `fee_schedule_id` | `dim_fee_schedule` | 1:N | 1:many / optional | many:1 / optional | A claim Line may match one fee Schedule, and a fee Schedule may include no claim Line. |
| `fact_claim_diagnosis` | `claim_header_id` | `fact_claim_header` | 1:N | 1:many / always | many:1 / always | Many claim Diagnosises belong to one claim Header, every claim Diagnosis matches a claim Header, and every claim Header includes at least one claim Diagnosis. Every claim has at least one diagnosis row. |
| `fact_claim_diagnosis` | `diagnosis_id` | `dim_diagnosis` | 1:N | 1:many / optional | many:1 / always | Many claim Diagnosises belong to one diagnosis, every claim Diagnosis matches a diagnosis, and a diagnosis may include no claim Diagnosis. |
| `fact_claim_diagnosis` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many claim Diagnosises belong to one calendar Day, every claim Diagnosis matches a calendar Day, and a calendar Day may include no claim Diagnosis. |
| `fact_remit_advice` | `billing_provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many remit Advices belong to one provider, every remit Advice matches a provider, and a provider may include no remit Advice. |
| `fact_remit_advice` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many remit Advices belong to one calendar Day, every remit Advice matches a calendar Day, and every calendar Day includes at least one remit Advice. |
| `fact_remit_advice` | `payment_method_id` | `dim_payment_method` | 1:N | 1:many / always | many:1 / always | Many remit Advices belong to one payment Method, every remit Advice matches a payment Method, and every payment Method includes at least one remit Advice. |
| `fact_remit_advice` | `bank_id` | `dim_bank` | 1:N | 1:many / optional | many:1 / optional | A remit Advice may match one bank, and a bank may include no remit Advice. |
| `fact_remit_advice` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / optional | many:1 / always | Many remit Advices belong to one jurisdiction, every remit Advice matches a jurisdiction, and a jurisdiction may include no remit Advice. |
| `fact_remit_advice` | `trading_partner_id` | `dim_trading_partner` | 1:N | 1:many / optional | many:1 / always | Many remit Advices belong to one trading Partner, every remit Advice matches a trading Partner, and a trading Partner may include no remit Advice. |
| `fact_remit_line` | `remit_advice_id` | `fact_remit_advice` | 1:N | 1:many / always | many:1 / always | Many remit Lines belong to one remit Advice, every remit Line matches a remit Advice, and every remit Advice includes at least one remit Line. Every remittance advice has service lines. |
| `fact_remit_line` | `claim_line_id` | `fact_claim_line` | 1:N | 1:many / optional | many:1 / always | Many remit Lines belong to one claim Line, every remit Line matches a claim Line, and a claim Line may include no remit Line. Some service lines are still pended and have no remit line. |
| `fact_remit_line` | `claim_header_id` | `fact_claim_header` | 1:N | 1:many / optional | many:1 / always | Many remit Lines belong to one claim Header, every remit Line matches a claim Header, and a claim Header may include no remit Line. |
| `fact_remit_line` | `carc_id` | `dim_carc` | 1:N | 1:many / optional | many:1 / optional | A remit Line may match one cARC, and a cARC may include no remit Line. A paid line may have no adjustment reason. |
| `fact_remit_line` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many remit Lines belong to one member, every remit Line matches a member, and a member may include no remit Line. |
| `fact_remit_line` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many remit Lines belong to one provider, every remit Line matches a provider, and a provider may include no remit Line. |
| `fact_remit_line` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many remit Lines belong to one calendar Day, every remit Line matches a calendar Day, and every calendar Day includes at least one remit Line. |
| `fact_remit_adjustment` | `remit_line_id` | `fact_remit_line` | 1:N | 1:many / optional | many:1 / always | Many remit Adjustments belong to one remit Line, every remit Adjustment matches a remit Line, and a remit Line may include no remit Adjustment. Not every remit line carries an adjustment. |
| `fact_remit_adjustment` | `carc_id` | `dim_carc` | 1:N | 1:many / always | many:1 / always | Many remit Adjustments belong to one cARC, every remit Adjustment matches a cARC, and every cARC includes at least one remit Adjustment. |
| `fact_remit_adjustment` | `rarc_id` | `dim_rarc` | 1:N | 1:many / optional | many:1 / optional | A remit Adjustment may match one rARC, and a rARC may include no remit Adjustment. |
| `fact_remit_adjustment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many remit Adjustments belong to one calendar Day, every remit Adjustment matches a calendar Day, and every calendar Day includes at least one remit Adjustment. |
| `fact_eligibility_inquiry` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many eligibility Inquiries belong to one member, every eligibility Inquiry matches a member, and a member may include no eligibility Inquiry. |
| `fact_eligibility_inquiry` | `coverage_id` | `dim_coverage` | 1:N | 1:many / optional | many:1 / always | Many eligibility Inquiries belong to one coverage, every eligibility Inquiry matches a coverage, and a coverage may include no eligibility Inquiry. |
| `fact_eligibility_inquiry` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many eligibility Inquiries belong to one provider, every eligibility Inquiry matches a provider, and a provider may include no eligibility Inquiry. |
| `fact_eligibility_inquiry` | `trading_partner_id` | `dim_trading_partner` | 1:N | 1:many / always | many:1 / always | Many eligibility Inquiries belong to one trading Partner, every eligibility Inquiry matches a trading Partner, and every trading Partner includes at least one eligibility Inquiry. |
| `fact_eligibility_inquiry` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many eligibility Inquiries belong to one calendar Day, every eligibility Inquiry matches a calendar Day, and every calendar Day includes at least one eligibility Inquiry. |
| `fact_eligibility_inquiry` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many eligibility Inquiries belong to one plan, every eligibility Inquiry matches a plan, and a plan may include no eligibility Inquiry. |
| `fact_eligibility_inquiry` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / optional | many:1 / always | Many eligibility Inquiries belong to one jurisdiction, every eligibility Inquiry matches a jurisdiction, and a jurisdiction may include no eligibility Inquiry. |
| `fact_eligibility_response` | `eligibility_inquiry_id` | `fact_eligibility_inquiry` | 1:1 | 1:1 / always | 1:1 / always | Each eligibility Response matches exactly one eligibility Inquiry, and each eligibility Inquiry matches exactly one eligibility Response. Each inquiry has one response, and each response has one inquiry. |
| `fact_eligibility_response` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many eligibility Responses belong to one member, every eligibility Response matches a member, and a member may include no eligibility Response. |
| `fact_eligibility_response` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many eligibility Responses belong to one plan, every eligibility Response matches a plan, and a plan may include no eligibility Response. |
| `fact_eligibility_response` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many eligibility Responses belong to one calendar Day, every eligibility Response matches a calendar Day, and every calendar Day includes at least one eligibility Response. |
| `fact_claim_status` | `claim_header_id` | `fact_claim_header` | 1:N | 1:many / always | many:1 / always | Many claim Statuses belong to one claim Header, every claim Status matches a claim Header, and every claim Header includes at least one claim Status. Every header has status events. |
| `fact_claim_status` | `trading_partner_id` | `dim_trading_partner` | 1:N | 1:many / optional | many:1 / always | Many claim Statuses belong to one trading Partner, every claim Status matches a trading Partner, and a trading Partner may include no claim Status. |
| `fact_claim_status` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many claim Statuses belong to one calendar Day, every claim Status matches a calendar Day, and every calendar Day includes at least one claim Status. |
| `fact_claim_status` | `submitter_id` | `dim_submitter` | 1:N | 1:many / optional | many:1 / always | Many claim Statuses belong to one submitter, every claim Status matches a submitter, and a submitter may include no claim Status. |
| `fact_pharmacy_claim` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many pharmacy Claims belong to one member, every pharmacy Claim matches a member, and a member may include no pharmacy Claim. |
| `fact_pharmacy_claim` | `pharmacy_id` | `dim_pharmacy` | 1:N | 1:many / optional | many:1 / always | Many pharmacy Claims belong to one pharmacy, every pharmacy Claim matches a pharmacy, and a pharmacy may include no pharmacy Claim. |
| `fact_pharmacy_claim` | `prescriber_id` | `dim_prescriber` | 1:N | 1:many / optional | many:1 / always | Many pharmacy Claims belong to one prescriber, every pharmacy Claim matches a prescriber, and a prescriber may include no pharmacy Claim. |
| `fact_pharmacy_claim` | `ndc_id` | `dim_ndc` | 1:N | 1:many / optional | many:1 / always | Many pharmacy Claims belong to one nDC, every pharmacy Claim matches a nDC, and a nDC may include no pharmacy Claim. |
| `fact_pharmacy_claim` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many pharmacy Claims belong to one plan, every pharmacy Claim matches a plan, and a plan may include no pharmacy Claim. |
| `fact_pharmacy_claim` | `formulary_id` | `dim_formulary` | 1:N | 1:many / optional | many:1 / optional | A pharmacy Claim may match one formulary, and a formulary may include no pharmacy Claim. |
| `fact_pharmacy_claim` | `tier_id` | `dim_tier` | 1:N | 1:many / optional | many:1 / always | Many pharmacy Claims belong to one formulary Tier, every pharmacy Claim matches a formulary Tier, and a formulary Tier may include no pharmacy Claim. |
| `fact_pharmacy_claim` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many pharmacy Claims belong to one calendar Day, every pharmacy Claim matches a calendar Day, and every calendar Day includes at least one pharmacy Claim. |
| `fact_pharmacy_claim` | `insurance_line_id` | `dim_insurance_line` | 1:N | 1:many / optional | many:1 / always | Many pharmacy Claims belong to one insurance Line, every pharmacy Claim matches a insurance Line, and a insurance Line may include no pharmacy Claim. |
| `fact_accumulator_entry` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many accumulator Entries belong to one member, every accumulator Entry matches a member, and a member may include no accumulator Entry. |
| `fact_accumulator_entry` | `accumulator_type_id` | `dim_accumulator_type` | 1:N | 1:many / always | many:1 / always | Many accumulator Entries belong to one accumulator Type, every accumulator Entry matches a accumulator Type, and every accumulator Type includes at least one accumulator Entry. |
| `fact_accumulator_entry` | `claim_line_id` | `fact_claim_line` | 1:N | 1:many / optional | many:1 / always | Many accumulator Entries belong to one claim Line, every accumulator Entry matches a claim Line, and a claim Line may include no accumulator Entry. Each posting cites one service line. |
| `fact_accumulator_entry` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many accumulator Entries belong to one plan, every accumulator Entry matches a plan, and a plan may include no accumulator Entry. |
| `fact_accumulator_entry` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many accumulator Entries belong to one calendar Day, every accumulator Entry matches a calendar Day, and every calendar Day includes at least one accumulator Entry. |
| `fact_accumulator_snapshot` | `member_id` | `dim_member` | 1:N | 1:many / always | many:1 / always | Many accumulator Snapshots belong to one member, every accumulator Snapshot matches a member, and every member includes at least one accumulator Snapshot. Every member has a snapshot row for each accumulator type. |
| `fact_accumulator_snapshot` | `accumulator_type_id` | `dim_accumulator_type` | 1:N | 1:many / always | many:1 / always | Many accumulator Snapshots belong to one accumulator Type, every accumulator Snapshot matches a accumulator Type, and every accumulator Type includes at least one accumulator Snapshot. Every accumulator type is snapshotted. |
| `fact_accumulator_snapshot` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many accumulator Snapshots belong to one plan, every accumulator Snapshot matches a plan, and a plan may include no accumulator Snapshot. |
| `fact_accumulator_snapshot` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many accumulator Snapshots belong to one calendar Day, every accumulator Snapshot matches a calendar Day, and a calendar Day may include no accumulator Snapshot. |
| `fact_pricing_result` | `claim_line_id` | `fact_claim_line` | 1:1 | 1:1 / always | 1:1 / always | Each pricing Result matches exactly one claim Line, and each claim Line matches exactly one pricing Result. Each service line has one pricing result. |
| `fact_pricing_result` | `fee_schedule_id` | `dim_fee_schedule` | 1:N | 1:many / always | many:1 / always | Many pricing Results belong to one fee Schedule, every pricing Result matches a fee Schedule, and every fee Schedule includes at least one pricing Result. |
| `fact_pricing_result` | `procedure_id` | `dim_procedure` | 1:N | 1:many / optional | many:1 / always | Many pricing Results belong to one procedure, every pricing Result matches a procedure, and a procedure may include no pricing Result. |
| `fact_pricing_result` | `locality_id` | `dim_locality` | 1:N | 1:many / optional | many:1 / always | Many pricing Results belong to one payment Locality, every pricing Result matches a payment Locality, and a payment Locality may include no pricing Result. |
| `fact_pricing_result` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many pricing Results belong to one calendar Day, every pricing Result matches a calendar Day, and a calendar Day may include no pricing Result. |
| `fact_claim_edit` | `claim_header_id` | `fact_claim_header` | 1:N | 1:many / always | many:1 / always | Many claim Edits belong to one claim Header, every claim Edit matches a claim Header, and every claim Header includes at least one claim Edit. Every header receives edit results. |
| `fact_claim_edit` | `edit_code_id` | `dim_edit_code` | 1:N | 1:many / optional | many:1 / always | Many claim Edits belong to one edit Code, every claim Edit matches a edit Code, and a edit Code may include no claim Edit. |
| `fact_claim_edit` | `claim_line_id` | `fact_claim_line` | 1:N | 1:many / optional | many:1 / optional | A claim Edit may match one claim Line, and a claim Line may include no claim Edit. Header-level edits have no line. |
| `fact_claim_edit` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many claim Edits belong to one calendar Day, every claim Edit matches a calendar Day, and every calendar Day includes at least one claim Edit. |
| `fact_prior_auth` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many prior Authorizations belong to one member, every prior Authorization matches a member, and a member may include no prior Authorization. |
| `fact_prior_auth` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many prior Authorizations belong to one provider, every prior Authorization matches a provider, and a provider may include no prior Authorization. |
| `fact_prior_auth` | `auth_type_id` | `dim_auth_type` | 1:N | 1:many / always | many:1 / always | Many prior Authorizations belong to one authorization Type, every prior Authorization matches a authorization Type, and every authorization Type includes at least one prior Authorization. |
| `fact_prior_auth` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many prior Authorizations belong to one calendar Day, every prior Authorization matches a calendar Day, and a calendar Day may include no prior Authorization. |
| `fact_prior_auth` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many prior Authorizations belong to one plan, every prior Authorization matches a plan, and a plan may include no prior Authorization. |
| `fact_prior_auth` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A prior Authorization may match one employee, and a employee may include no prior Authorization. |
| `fact_auth_line` | `prior_auth_id` | `fact_prior_auth` | 1:N | 1:many / always | many:1 / always | Many authorization Lines belong to one prior Authorization, every authorization Line matches a prior Authorization, and every prior Authorization includes at least one authorization Line. Every authorization has lines. |
| `fact_auth_line` | `procedure_id` | `dim_procedure` | 1:N | 1:many / optional | many:1 / always | Many authorization Lines belong to one procedure, every authorization Line matches a procedure, and a procedure may include no authorization Line. |
| `fact_auth_line` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many authorization Lines belong to one calendar Day, every authorization Line matches a calendar Day, and a calendar Day may include no authorization Line. |
| `fact_auth_decision` | `prior_auth_id` | `fact_prior_auth` | 1:1 | 1:1 / always | 1:1 / always | Each authorization Decision matches exactly one prior Authorization, and each prior Authorization matches exactly one authorization Decision. Each authorization has one current decision. |
| `fact_auth_decision` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many authorization Decisions belong to one employee, every authorization Decision matches a employee, and a employee may include no authorization Decision. |
| `fact_auth_decision` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many authorization Decisions belong to one calendar Day, every authorization Decision matches a calendar Day, and a calendar Day may include no authorization Decision. |
| `fact_auth_decision` | `denial_reason_id` | `dim_denial_reason` | 1:N | 1:many / optional | many:1 / optional | A authorization Decision may match one denial Reason, and a denial Reason may include no authorization Decision. |
| `fact_cob_line` | `claim_line_id` | `fact_claim_line` | 1:N | 1:many / optional | many:1 / always | Many cOB Lines belong to one claim Line, every cOB Line matches a claim Line, and a claim Line may include no cOB Line. |
| `fact_cob_line` | `cob_type_id` | `dim_cob_type` | 1:N | 1:many / always | many:1 / always | Many cOB Lines belong to one cOB Type, every cOB Line matches a cOB Type, and every cOB Type includes at least one cOB Line. |
| `fact_cob_line` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many cOB Lines belong to one calendar Day, every cOB Line matches a calendar Day, and a calendar Day may include no cOB Line. |
| `fact_cob_line` | `trading_partner_id` | `dim_trading_partner` | 1:N | 1:many / optional | many:1 / optional | A cOB Line may match one trading Partner, and a trading Partner may include no cOB Line. |
| `fact_encounter` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many encounters belong to one member, every encounter matches a member, and a member may include no encounter. |
| `fact_encounter` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many encounters belong to one provider, every encounter matches a provider, and a provider may include no encounter. |
| `fact_encounter` | `facility_id` | `dim_facility` | 1:N | 1:many / optional | many:1 / optional | A encounter may match one facility, and a facility may include no encounter. |
| `fact_encounter` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many encounters belong to one plan, every encounter matches a plan, and a plan may include no encounter. |
| `fact_encounter` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many encounters belong to one calendar Day, every encounter matches a calendar Day, and every calendar Day includes at least one encounter. |
| `fact_encounter` | `place_of_service_id` | `dim_place_of_service` | 1:N | 1:many / optional | many:1 / always | Many encounters belong to one place of Service, every encounter matches a place of Service, and a place of Service may include no encounter. |
| `fact_premium_bill` | `member_id` | `dim_member` | 1:1 | 1:1 / always | 1:1 / always | Each premium Bill matches exactly one member, and each member matches exactly one premium Bill. Each member has one premium bill in the window. |
| `fact_premium_bill` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many premium Bills belong to one plan, every premium Bill matches a plan, and a plan may include no premium Bill. |
| `fact_premium_bill` | `premium_schedule_id` | `dim_premium_schedule` | 1:N | 1:many / optional | many:1 / always | Many premium Bills belong to one premium Schedule, every premium Bill matches a premium Schedule, and a premium Schedule may include no premium Bill. |
| `fact_premium_bill` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many premium Bills belong to one calendar Day, every premium Bill matches a calendar Day, and a calendar Day may include no premium Bill. |
| `fact_premium_payment` | `premium_bill_id` | `fact_premium_bill` | 1:N | 1:many / optional | many:1 / always | Many premium Payments belong to one premium Bill, every premium Payment matches a premium Bill, and a premium Bill may include no premium Payment. |
| `fact_premium_payment` | `payment_method_id` | `dim_payment_method` | 1:N | 1:many / always | many:1 / always | Many premium Payments belong to one payment Method, every premium Payment matches a payment Method, and every payment Method includes at least one premium Payment. |
| `fact_premium_payment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many premium Payments belong to one calendar Day, every premium Payment matches a calendar Day, and every calendar Day includes at least one premium Payment. |
| `fact_premium_payment` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many premium Payments belong to one member, every premium Payment matches a member, and a member may include no premium Payment. |
| `fact_capitation` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many capitation Payments belong to one provider, every capitation Payment matches a provider, and a provider may include no capitation Payment. |
| `fact_capitation` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many capitation Payments belong to one plan, every capitation Payment matches a plan, and a plan may include no capitation Payment. |
| `fact_capitation` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many capitation Payments belong to one calendar Day, every capitation Payment matches a calendar Day, and a calendar Day may include no capitation Payment. |
| `fact_capitation` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / optional | A capitation Payment may match one member, and a member may include no capitation Payment. Some capitation is paid per panel, not per member. |
| `fact_provider_payment` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many provider Payments belong to one provider, every provider Payment matches a provider, and a provider may include no provider Payment. |
| `fact_provider_payment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many provider Payments belong to one calendar Day, every provider Payment matches a calendar Day, and every calendar Day includes at least one provider Payment. |
| `fact_provider_payment` | `bank_id` | `dim_bank` | 1:N | 1:many / optional | many:1 / always | Many provider Payments belong to one bank, every provider Payment matches a bank, and a bank may include no provider Payment. |
| `fact_provider_payment` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / optional | many:1 / always | Many provider Payments belong to one jurisdiction, every provider Payment matches a jurisdiction, and a jurisdiction may include no provider Payment. |
| `fact_provider_payment` | `remit_advice_id` | `fact_remit_advice` | 1:N | 1:many / optional | many:1 / optional | A provider Payment may match one remit Advice, and a remit Advice may include no provider Payment. |
| `fact_appeal` | `claim_header_id` | `fact_claim_header` | 1:N | 1:many / optional | many:1 / always | Many appeals belong to one claim Header, every appeal matches a claim Header, and a claim Header may include no appeal. |
| `fact_appeal` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many appeals belong to one member, every appeal matches a member, and a member may include no appeal. |
| `fact_appeal` | `appeal_level_id` | `dim_appeal_level` | 1:N | 1:many / always | many:1 / always | Many appeals belong to one appeal Level, every appeal matches a appeal Level, and every appeal Level includes at least one appeal. |
| `fact_appeal` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many appeals belong to one calendar Day, every appeal matches a calendar Day, and a calendar Day may include no appeal. |
| `fact_appeal` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A appeal may match one employee, and a employee may include no appeal. |
| `fact_appeal_decision` | `appeal_id` | `fact_appeal` | 1:N | 1:many / optional | many:1 / always | Many appeal Decisions belong to one appeal, every appeal Decision matches a appeal, and a appeal may include no appeal Decision. |
| `fact_appeal_decision` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many appeal Decisions belong to one employee, every appeal Decision matches a employee, and a employee may include no appeal Decision. |
| `fact_appeal_decision` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many appeal Decisions belong to one calendar Day, every appeal Decision matches a calendar Day, and a calendar Day may include no appeal Decision. |
| `fact_appeal_decision` | `denial_reason_id` | `dim_denial_reason` | 1:N | 1:many / optional | many:1 / optional | A appeal Decision may match one denial Reason, and a denial Reason may include no appeal Decision. |
| `fact_medical_review` | `claim_line_id` | `fact_claim_line` | 1:N | 1:many / optional | many:1 / always | Many medical Reviews belong to one claim Line, every medical Review matches a claim Line, and a claim Line may include no medical Review. |
| `fact_medical_review` | `review_type_id` | `dim_review_type` | 1:N | 1:many / always | many:1 / always | Many medical Reviews belong to one review Type, every medical Review matches a review Type, and every review Type includes at least one medical Review. |
| `fact_medical_review` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many medical Reviews belong to one employee, every medical Review matches a employee, and a employee may include no medical Review. |
| `fact_medical_review` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many medical Reviews belong to one calendar Day, every medical Review matches a calendar Day, and a calendar Day may include no medical Review. |
| `fact_attachment` | `claim_header_id` | `fact_claim_header` | 1:N | 1:many / optional | many:1 / always | Many claim Attachments belong to one claim Header, every claim Attachment matches a claim Header, and a claim Header may include no claim Attachment. |
| `fact_attachment` | `document_type_id` | `dim_document_type` | 1:N | 1:many / always | many:1 / always | Many claim Attachments belong to one document Type, every claim Attachment matches a document Type, and every document Type includes at least one claim Attachment. |
| `fact_attachment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many claim Attachments belong to one calendar Day, every claim Attachment matches a calendar Day, and a calendar Day may include no claim Attachment. |
| `fact_referral` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many referrals belong to one member, every referral matches a member, and a member may include no referral. |
| `fact_referral` | `referring_provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many referrals belong to one provider, every referral matches a provider, and a provider may include no referral. Provider who referred. |
| `fact_referral` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many referrals belong to one calendar Day, every referral matches a calendar Day, and a calendar Day may include no referral. |
| `fact_referral` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many referrals belong to one plan, every referral matches a plan, and a plan may include no referral. |
| `fact_referral_target` | `referral_id` | `fact_referral` | 1:1 | 1:1 / always | 1:1 / always | Each referral Target matches exactly one referral, and each referral matches exactly one referral Target. Each referral has one target provider row. |
| `fact_referral_target` | `referred_provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many referral Targets belong to one provider, every referral Target matches a provider, and a provider may include no referral Target. Provider who received the referral. |
| `fact_pcp_attribution` | `member_id` | `dim_member` | 1:1 | 1:1 / always | 1:1 / always | Each pCP Attribution matches exactly one member, and each member matches exactly one pCP Attribution. Each member has one attribution row. |
| `fact_pcp_attribution` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many pCP Attributions belong to one provider, every pCP Attribution matches a provider, and a provider may include no pCP Attribution. |
| `fact_pcp_attribution` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many pCP Attributions belong to one plan, every pCP Attribution matches a plan, and a plan may include no pCP Attribution. |
| `fact_pcp_attribution` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many pCP Attributions belong to one calendar Day, every pCP Attribution matches a calendar Day, and a calendar Day may include no pCP Attribution. |
| `fact_risk_score` | `member_id` | `dim_member` | 1:1 | 1:1 / always | 1:1 / always | Each risk Score matches exactly one member, and each member matches exactly one risk Score. Each member has one risk score in the window. |
| `fact_risk_score` | `risk_model_id` | `dim_risk_model` | 1:N | 1:many / always | many:1 / always | Many risk Scores belong to one risk Model, every risk Score matches a risk Model, and every risk Model includes at least one risk Score. |
| `fact_risk_score` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many risk Scores belong to one plan, every risk Score matches a plan, and a plan may include no risk Score. |
| `fact_risk_score` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many risk Scores belong to one calendar Day, every risk Score matches a calendar Day, and a calendar Day may include no risk Score. |
| `fact_hcc_diagnosis` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many hCC Diagnosises belong to one member, every hCC Diagnosis matches a member, and a member may include no hCC Diagnosis. |
| `fact_hcc_diagnosis` | `diagnosis_id` | `dim_diagnosis` | 1:N | 1:many / optional | many:1 / always | Many hCC Diagnosises belong to one diagnosis, every hCC Diagnosis matches a diagnosis, and a diagnosis may include no hCC Diagnosis. |
| `fact_hcc_diagnosis` | `hcc_id` | `dim_hcc` | 1:N | 1:many / optional | many:1 / optional | A hCC Diagnosis may match one hCC, and a hCC may include no hCC Diagnosis. |
| `fact_hcc_diagnosis` | `risk_model_id` | `dim_risk_model` | 1:N | 1:many / optional | many:1 / always | Many hCC Diagnosises belong to one risk Model, every hCC Diagnosis matches a risk Model, and a risk Model may include no hCC Diagnosis. |
| `fact_hcc_diagnosis` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many hCC Diagnosises belong to one calendar Day, every hCC Diagnosis matches a calendar Day, and a calendar Day may include no hCC Diagnosis. |
| `fact_enrollment_span` | `coverage_id` | `dim_coverage` | 1:1 | 1:1 / always | 1:1 / always | Each enrollment Span matches exactly one coverage, and each coverage matches exactly one enrollment Span. Each coverage has one current enrollment span. |
| `fact_enrollment_span` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many enrollment Spans belong to one plan, every enrollment Span matches a plan, and a plan may include no enrollment Span. |
| `fact_enrollment_span` | `start_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / optional | A enrollment Span may match one calendar Day, and a calendar Day may include no enrollment Span. Spans that started before the window have no start day inside it. |
| `fact_disenrollment` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many disenrollments belong to one member, every disenrollment matches a member, and a member may include no disenrollment. |
| `fact_disenrollment` | `coverage_id` | `dim_coverage` | 1:N | 1:many / optional | many:1 / always | Many disenrollments belong to one coverage, every disenrollment matches a coverage, and a coverage may include no disenrollment. |
| `fact_disenrollment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many disenrollments belong to one calendar Day, every disenrollment matches a calendar Day, and a calendar Day may include no disenrollment. |
| `fact_disenrollment` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many disenrollments belong to one plan, every disenrollment matches a plan, and a plan may include no disenrollment. |
| `fact_premium_adjustment` | `premium_bill_id` | `fact_premium_bill` | 1:N | 1:many / optional | many:1 / always | Many premium Adjustments belong to one premium Bill, every premium Adjustment matches a premium Bill, and a premium Bill may include no premium Adjustment. |
| `fact_premium_adjustment` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many premium Adjustments belong to one member, every premium Adjustment matches a member, and a member may include no premium Adjustment. |
| `fact_premium_adjustment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many premium Adjustments belong to one calendar Day, every premium Adjustment matches a calendar Day, and a calendar Day may include no premium Adjustment. |
| `fact_low_income_subsidy` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many low Income Subsidies belong to one member, every low Income Subsidy matches a member, and a member may include no low Income Subsidy. |
| `fact_low_income_subsidy` | `lis_level_id` | `dim_lis_level` | 1:N | 1:many / always | many:1 / always | Many low Income Subsidies belong to one lIS Level, every low Income Subsidy matches a lIS Level, and every lIS Level includes at least one low Income Subsidy. |
| `fact_low_income_subsidy` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many low Income Subsidies belong to one calendar Day, every low Income Subsidy matches a calendar Day, and a calendar Day may include no low Income Subsidy. |
| `fact_call` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / optional | A service Call may match one member, and a member may include no service Call. |
| `fact_call` | `agent_id` | `dim_agent` | 1:N | 1:many / always | many:1 / always | Many service Calls belong to one service Agent, every service Call matches a service Agent, and every service Agent includes at least one service Call. Every agent takes calls. |
| `fact_call` | `call_queue_id` | `dim_call_queue` | 1:N | 1:many / always | many:1 / always | Many service Calls belong to one call Queue, every service Call matches a call Queue, and every call Queue includes at least one service Call. |
| `fact_call` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many service Calls belong to one calendar Day, every service Call matches a calendar Day, and every calendar Day includes at least one service Call. |
| `fact_call_event` | `call_id` | `fact_call` | 1:N | 1:many / always | many:1 / always | Many call Events belong to one service Call, every call Event matches a service Call, and every service Call includes at least one call Event. Every call has events. |
| `fact_call_event` | `agent_id` | `dim_agent` | 1:N | 1:many / optional | many:1 / always | Many call Events belong to one service Agent, every call Event matches a service Agent, and a service Agent may include no call Event. |
| `fact_call_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many call Events belong to one calendar Day, every call Event matches a calendar Day, and a calendar Day may include no call Event. |
| `fact_letter` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many letters belong to one member, every letter matches a member, and a member may include no letter. |
| `fact_letter` | `document_type_id` | `dim_document_type` | 1:N | 1:many / optional | many:1 / always | Many letters belong to one document Type, every letter matches a document Type, and a document Type may include no letter. |
| `fact_letter` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many letters belong to one calendar Day, every letter matches a calendar Day, and every calendar Day includes at least one letter. |
| `fact_portal_event` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many portal Events belong to one member, every portal Event matches a member, and a member may include no portal Event. |
| `fact_portal_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many portal Events belong to one calendar Day, every portal Event matches a calendar Day, and every calendar Day includes at least one portal Event. |
| `fact_audit_sample` | `audit_program_id` | `dim_audit_program` | 1:N | 1:many / always | many:1 / always | Many audit Samples belong to one audit Program, every audit Sample matches a audit Program, and every audit Program includes at least one audit Sample. |
| `fact_audit_sample` | `claim_header_id` | `fact_claim_header` | 1:N | 1:many / optional | many:1 / always | Many audit Samples belong to one claim Header, every audit Sample matches a claim Header, and a claim Header may include no audit Sample. |
| `fact_audit_sample` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many audit Samples belong to one calendar Day, every audit Sample matches a calendar Day, and a calendar Day may include no audit Sample. |
| `fact_fraud_lead` | `fraud_scheme_id` | `dim_fraud_scheme` | 1:N | 1:many / always | many:1 / always | Many fraud Leads belong to one fraud Scheme, every fraud Lead matches a fraud Scheme, and every fraud Scheme includes at least one fraud Lead. |
| `fact_fraud_lead` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / optional | A fraud Lead may match one provider, and a provider may include no fraud Lead. |
| `fact_fraud_lead` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / optional | A fraud Lead may match one member, and a member may include no fraud Lead. |
| `fact_fraud_lead` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many fraud Leads belong to one calendar Day, every fraud Lead matches a calendar Day, and a calendar Day may include no fraud Lead. |
| `fact_provider_enrollment` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many provider Enrollments belong to one provider, every provider Enrollment matches a provider, and a provider may include no provider Enrollment. |
| `fact_provider_enrollment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many provider Enrollments belong to one calendar Day, every provider Enrollment matches a calendar Day, and a calendar Day may include no provider Enrollment. |
| `fact_provider_enrollment` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / always | many:1 / always | Many provider Enrollments belong to one jurisdiction, every provider Enrollment matches a jurisdiction, and every jurisdiction includes at least one provider Enrollment. |
| `fact_provider_enrollment` | `enrollment_status_id` | `dim_enrollment_status` | 1:N | 1:many / always | many:1 / always | Many provider Enrollments belong to one enrollment Status, every provider Enrollment matches a enrollment Status, and every enrollment Status includes at least one provider Enrollment. |
| `fact_revalidation` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many revalidations belong to one provider, every revalidation matches a provider, and a provider may include no revalidation. |
| `fact_revalidation` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many revalidations belong to one calendar Day, every revalidation matches a calendar Day, and a calendar Day may include no revalidation. |
| `fact_revalidation` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / optional | many:1 / always | Many revalidations belong to one jurisdiction, every revalidation matches a jurisdiction, and a jurisdiction may include no revalidation. |
| `fact_claim_note` | `claim_header_id` | `fact_claim_header` | 1:N | 1:many / optional | many:1 / always | Many claim Notes belong to one claim Header, every claim Note matches a claim Header, and a claim Header may include no claim Note. |
| `fact_claim_note` | `note_type_id` | `dim_note_type` | 1:N | 1:many / always | many:1 / always | Many claim Notes belong to one note Type, every claim Note matches a note Type, and every note Type includes at least one claim Note. |
| `fact_claim_note` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A claim Note may match one employee, and a employee may include no claim Note. |
| `fact_claim_note` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many claim Notes belong to one calendar Day, every claim Note matches a calendar Day, and a calendar Day may include no claim Note. |
| `fact_interest_payment` | `claim_header_id` | `fact_claim_header` | 1:N | 1:many / optional | many:1 / always | Many interest Payments belong to one claim Header, every interest Payment matches a claim Header, and a claim Header may include no interest Payment. |
| `fact_interest_payment` | `interest_reason_id` | `dim_interest_reason` | 1:N | 1:many / always | many:1 / always | Many interest Payments belong to one interest Reason, every interest Payment matches a interest Reason, and every interest Reason includes at least one interest Payment. |
| `fact_interest_payment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many interest Payments belong to one calendar Day, every interest Payment matches a calendar Day, and a calendar Day may include no interest Payment. |
| `fact_interest_payment` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many interest Payments belong to one provider, every interest Payment matches a provider, and a provider may include no interest Payment. |
| `fact_withhold` | `provider_payment_id` | `fact_provider_payment` | 1:N | 1:many / optional | many:1 / always | Many withholds belong to one provider Payment, every withhold matches a provider Payment, and a provider Payment may include no withhold. |
| `fact_withhold` | `withhold_reason_id` | `dim_withhold_reason` | 1:N | 1:many / always | many:1 / always | Many withholds belong to one withhold Reason, every withhold matches a withhold Reason, and every withhold Reason includes at least one withhold. |
| `fact_withhold` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many withholds belong to one calendar Day, every withhold matches a calendar Day, and a calendar Day may include no withhold. |
| `fact_overpayment` | `claim_header_id` | `fact_claim_header` | 1:N | 1:many / optional | many:1 / always | Many overpayments belong to one claim Header, every overpayment matches a claim Header, and a claim Header may include no overpayment. |
| `fact_overpayment` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many overpayments belong to one provider, every overpayment matches a provider, and a provider may include no overpayment. |
| `fact_overpayment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many overpayments belong to one calendar Day, every overpayment matches a calendar Day, and a calendar Day may include no overpayment. |
| `fact_recovery` | `overpayment_id` | `fact_overpayment` | 1:N | 1:many / optional | many:1 / always | Many recoveries belong to one overpayment, every recovery matches a overpayment, and a overpayment may include no recovery. |
| `fact_recovery` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many recoveries belong to one calendar Day, every recovery matches a calendar Day, and a calendar Day may include no recovery. |
| `fact_recovery` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many recoveries belong to one provider, every recovery matches a provider, and a provider may include no recovery. |
| `fact_grievance` | `member_id` | `dim_member` | 1:N | 1:many / optional | many:1 / always | Many grievances belong to one member, every grievance matches a member, and a member may include no grievance. |
| `fact_grievance` | `plan_id` | `dim_plan` | 1:N | 1:many / optional | many:1 / always | Many grievances belong to one plan, every grievance matches a plan, and a plan may include no grievance. |
| `fact_grievance` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many grievances belong to one calendar Day, every grievance matches a calendar Day, and a calendar Day may include no grievance. |
| `fact_fee_schedule_rate` | `fee_schedule_id` | `dim_fee_schedule` | 1:N | 1:many / always | many:1 / always | Many fee Schedule Rates belong to one fee Schedule, every fee Schedule Rate matches a fee Schedule, and every fee Schedule includes at least one fee Schedule Rate. |
| `fact_fee_schedule_rate` | `procedure_id` | `dim_procedure` | 1:N | 1:many / optional | many:1 / always | Many fee Schedule Rates belong to one procedure, every fee Schedule Rate matches a procedure, and a procedure may include no fee Schedule Rate. |
| `fact_fee_schedule_rate` | `locality_id` | `dim_locality` | 1:N | 1:many / optional | many:1 / always | Many fee Schedule Rates belong to one payment Locality, every fee Schedule Rate matches a payment Locality, and a payment Locality may include no fee Schedule Rate. |
| `bridge_plan_benefit` | `plan_id` | `dim_plan` | 1:N | 1:many / always | many:1 / always | Many plan Benefits belong to one plan, every plan Benefit matches a plan, and every plan includes at least one plan Benefit. |
| `bridge_plan_benefit` | `benefit_id` | `dim_benefit` | 1:1 | 1:1 / always | 1:1 / always | Each plan Benefit matches exactly one benefit, and each benefit matches exactly one plan Benefit. |
| `bridge_provider_network` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many provider Networks belong to one provider, every provider Network matches a provider, and a provider may include no provider Network. |
| `bridge_provider_network` | `network_id` | `dim_network` | 1:N | 1:many / always | many:1 / always | Many provider Networks belong to one provider Network, every provider Network matches a provider Network, and every provider Network includes at least one provider Network. |
| `bridge_provider_specialty` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many provider Specialties belong to one provider, every provider Specialty matches a provider, and a provider may include no provider Specialty. |
| `bridge_provider_specialty` | `specialty_id` | `dim_specialty` | 1:N | 1:many / always | many:1 / always | Many provider Specialties belong to one specialty, every provider Specialty matches a specialty, and every specialty includes at least one provider Specialty. |
| `bridge_facility_network` | `facility_id` | `dim_facility` | 1:N | 1:many / optional | many:1 / always | Many facility Networks belong to one facility, every facility Network matches a facility, and a facility may include no facility Network. |
| `bridge_facility_network` | `network_id` | `dim_network` | 1:N | 1:many / always | many:1 / always | Many facility Networks belong to one provider Network, every facility Network matches a provider Network, and every provider Network includes at least one facility Network. |
| `bridge_member_language` | `member_id` | `dim_member` | 1:1 | 1:1 / always | 1:1 / always | Each member Language matches exactly one member, and each member matches exactly one member Language. |
| `bridge_member_language` | `language_id` | `dim_language` | 1:N | 1:many / always | many:1 / always | Many member Languages belong to one language, every member Language matches a language, and every language includes at least one member Language. |
| `bridge_coverage_rider` | `coverage_id` | `dim_coverage` | 1:N | 1:many / optional | many:1 / always | Many coverage Riders belong to one coverage, every coverage Rider matches a coverage, and a coverage may include no coverage Rider. |
| `bridge_coverage_rider` | `benefit_id` | `dim_benefit` | 1:N | 1:many / optional | many:1 / always | Many coverage Riders belong to one benefit, every coverage Rider matches a benefit, and a benefit may include no coverage Rider. |
| `bridge_formulary_drug` | `formulary_id` | `dim_formulary` | 1:N | 1:many / always | many:1 / always | Many formulary Drugs belong to one formulary, every formulary Drug matches a formulary, and every formulary includes at least one formulary Drug. |
| `bridge_formulary_drug` | `ndc_id` | `dim_ndc` | 1:N | 1:many / optional | many:1 / always | Many formulary Drugs belong to one nDC, every formulary Drug matches a nDC, and a nDC may include no formulary Drug. |
| `bridge_formulary_drug` | `tier_id` | `dim_tier` | 1:N | 1:many / always | many:1 / always | Many formulary Drugs belong to one formulary Tier, every formulary Drug matches a formulary Tier, and every formulary Tier includes at least one formulary Drug. |
| `bridge_plan_category` | `plan_id` | `dim_plan` | 1:N | 1:many / always | many:1 / always | Many plan Categories belong to one plan, every plan Category matches a plan, and every plan includes at least one plan Category. |
| `bridge_plan_category` | `service_category_id` | `dim_service_category` | 1:N | 1:many / optional | many:1 / always | Many plan Categories belong to one service Category, every plan Category matches a service Category, and a service Category may include no plan Category. |
| `bridge_group_benefit` | `group_id` | `dim_group` | 1:N | 1:many / always | many:1 / always | Many group Benefits belong to one employer Group, every group Benefit matches a employer Group, and every employer Group includes at least one group Benefit. |
| `bridge_group_benefit` | `benefit_id` | `dim_benefit` | 1:N | 1:many / optional | many:1 / always | Many group Benefits belong to one benefit, every group Benefit matches a benefit, and a benefit may include no group Benefit. |
| `bridge_jurisdiction_state` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / always | many:1 / always | Many jurisdiction States belong to one jurisdiction, every jurisdiction State matches a jurisdiction, and every jurisdiction includes at least one jurisdiction State. |
| `bridge_jurisdiction_state` | `state_id` | `dim_state` | 1:N | 1:many / optional | many:1 / always | Many jurisdiction States belong to one state, every jurisdiction State matches a state, and a state may include no jurisdiction State. |
| `bridge_diagnosis_hcc` | `diagnosis_id` | `dim_diagnosis` | 1:N | 1:many / optional | many:1 / always | Many diagnosis HCCs belong to one diagnosis, every diagnosis HCC matches a diagnosis, and a diagnosis may include no diagnosis HCC. |
| `bridge_diagnosis_hcc` | `hcc_id` | `dim_hcc` | 1:N | 1:many / always | many:1 / always | Many diagnosis HCCs belong to one hCC, every diagnosis HCC matches a hCC, and every hCC includes at least one diagnosis HCC. |
| `bridge_procedure_category` | `procedure_id` | `dim_procedure` | 1:1 | 1:1 / always | 1:1 / always | Each procedure Category matches exactly one procedure, and each procedure matches exactly one procedure Category. |
| `bridge_procedure_category` | `service_category_id` | `dim_service_category` | 1:N | 1:many / always | many:1 / always | Many procedure Categories belong to one service Category, every procedure Category matches a service Category, and every service Category includes at least one procedure Category. |
| `bridge_employee_jurisdiction` | `employee_id` | `dim_employee` | 1:1 | 1:1 / always | 1:1 / always | Each employee Jurisdiction matches exactly one employee, and each employee matches exactly one employee Jurisdiction. |
| `bridge_employee_jurisdiction` | `jurisdiction_id` | `dim_jurisdiction` | 1:N | 1:many / always | many:1 / always | Many employee Jurisdictions belong to one jurisdiction, every employee Jurisdiction matches a jurisdiction, and every jurisdiction includes at least one employee Jurisdiction. |
| `bridge_pharmacy_network` | `pharmacy_id` | `dim_pharmacy` | 1:N | 1:many / optional | many:1 / always | Many pharmacy Networks belong to one pharmacy, every pharmacy Network matches a pharmacy, and a pharmacy may include no pharmacy Network. |
| `bridge_pharmacy_network` | `network_id` | `dim_network` | 1:N | 1:many / always | many:1 / always | Many pharmacy Networks belong to one provider Network, every pharmacy Network matches a provider Network, and every provider Network includes at least one pharmacy Network. |
| `bridge_prescriber_specialty` | `prescriber_id` | `dim_prescriber` | 1:1 | 1:1 / always | 1:1 / always | Each prescriber Specialty matches exactly one prescriber, and each prescriber matches exactly one prescriber Specialty. |
| `bridge_prescriber_specialty` | `specialty_id` | `dim_specialty` | 1:N | 1:many / optional | many:1 / always | Many prescriber Specialties belong to one specialty, every prescriber Specialty matches a specialty, and a specialty may include no prescriber Specialty. |
| `bridge_cob_coverage` | `coverage_id` | `dim_coverage` | 1:N | 1:many / optional | many:1 / always | Many cOB Coverages belong to one coverage, every cOB Coverage matches a coverage, and a coverage may include no cOB Coverage. |
| `bridge_cob_coverage` | `cob_type_id` | `dim_cob_type` | 1:N | 1:many / always | many:1 / always | Many cOB Coverages belong to one cOB Type, every cOB Coverage matches a cOB Type, and every cOB Type includes at least one cOB Coverage. |
| `bridge_edit_line` | `edit_code_id` | `dim_edit_code` | 1:1 | 1:1 / always | 1:1 / always | Each edit Applicability matches exactly one edit Code, and each edit Code matches exactly one edit Applicability. |
| `bridge_edit_line` | `insurance_line_id` | `dim_insurance_line` | 1:N | 1:many / always | many:1 / always | Many edit Applicabilities belong to one insurance Line, every edit Applicability matches a insurance Line, and every insurance Line includes at least one edit Applicability. |
| `bridge_revenue_procedure` | `revenue_code_id` | `dim_revenue_code` | 1:N | 1:many / always | many:1 / always | Many revenue Procedures belong to one revenue Code, every revenue Procedure matches a revenue Code, and every revenue Code includes at least one revenue Procedure. |
| `bridge_revenue_procedure` | `procedure_id` | `dim_procedure` | 1:N | 1:many / optional | many:1 / always | Many revenue Procedures belong to one procedure, every revenue Procedure matches a procedure, and a procedure may include no revenue Procedure. |
| `bridge_drg_diagnosis` | `drg_id` | `dim_drg` | 1:N | 1:many / always | many:1 / always | Many dRG Diagnosises belong to one dRG, every dRG Diagnosis matches a dRG, and every dRG includes at least one dRG Diagnosis. |
| `bridge_drg_diagnosis` | `diagnosis_id` | `dim_diagnosis` | 1:N | 1:many / optional | many:1 / always | Many dRG Diagnosises belong to one diagnosis, every dRG Diagnosis matches a diagnosis, and a diagnosis may include no dRG Diagnosis. |
| `bridge_plan_formulary` | `plan_id` | `dim_plan` | 1:1 | 1:1 / always | 1:1 / always | Each plan Formulary matches exactly one plan, and each plan matches exactly one plan Formulary. |
| `bridge_plan_formulary` | `formulary_id` | `dim_formulary` | 1:N | 1:many / optional | many:1 / always | Many plan Formularies belong to one formulary, every plan Formulary matches a formulary, and a formulary may include no plan Formulary. |
| `bridge_network_plan` | `network_id` | `dim_network` | 1:N | 1:many / always | many:1 / always | Many network Plans belong to one provider Network, every network Plan matches a provider Network, and every provider Network includes at least one network Plan. |
| `bridge_network_plan` | `plan_id` | `dim_plan` | 1:N | 1:many / always | many:1 / always | Many network Plans belong to one plan, every network Plan matches a plan, and every plan includes at least one network Plan. |
| `bridge_facility_taxonomy` | `facility_id` | `dim_facility` | 1:1 | 1:1 / always | 1:1 / always | Each facility Taxonomy matches exactly one facility, and each facility matches exactly one facility Taxonomy. |
| `bridge_facility_taxonomy` | `taxonomy_id` | `dim_taxonomy` | 1:N | 1:many / optional | many:1 / always | Many facility Taxonomies belong to one provider Taxonomy, every facility Taxonomy matches a provider Taxonomy, and a provider Taxonomy may include no facility Taxonomy. |
| `bridge_state_locality` | `state_id` | `dim_state` | 1:N | 1:many / always | many:1 / always | Many state Localities belong to one state, every state Locality matches a state, and every state includes at least one state Locality. |
| `bridge_state_locality` | `locality_id` | `dim_locality` | 1:N | 1:many / optional | many:1 / always | Many state Localities belong to one payment Locality, every state Locality matches a payment Locality, and a payment Locality may include no state Locality. |
| `bridge_provider_facility` | `provider_id` | `dim_provider` | 1:N | 1:many / optional | many:1 / always | Many provider Facilities belong to one provider, every provider Facility matches a provider, and a provider may include no provider Facility. |
| `bridge_provider_facility` | `facility_id` | `dim_facility` | 1:N | 1:many / optional | many:1 / always | Many provider Facilities belong to one facility, every provider Facility matches a facility, and a facility may include no provider Facility. |
| `bridge_member_address` | `member_id` | `dim_member` | 1:1 | 1:1 / always | 1:1 / always | Each member Address matches exactly one member, and each member matches exactly one member Address. |
| `bridge_member_address` | `address_id` | `dim_address` | 1:1 | 1:1 / optional | 1:1 / always | Each member Address matches exactly one address, each address matches at most one member Address, and not every address is matched. Each member address row matches one address, and some addresses are not residential. |
| `bridge_contract_plan` | `contract_id` | `dim_contract` | 1:1 | 1:1 / always | 1:1 / always | Each contract Plan matches exactly one cMS Contract, and each cMS Contract matches exactly one contract Plan. |
| `bridge_contract_plan` | `plan_id` | `dim_plan` | 1:N | 1:many / always | many:1 / always | Many contract Plans belong to one plan, every contract Plan matches a plan, and every plan includes at least one contract Plan. |

## Dataset inventory

### appeal

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_appeal` | fact | `appeal_id` | One claim appeal. |
| `fact_appeal_decision` | fact | `appeal_decision_id` | One decision on an appeal. |

### benefit

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_drug_class` | dimension | `drug_class_id` | Therapeutic class of an NDC. |
| `dim_plan` | dimension | `plan_id` | Benefit plan or contract. |
| `dim_benefit` | dimension | `benefit_id` | Covered benefit inside a plan. |
| `dim_contract` | dimension | `contract_id` | Contract identifier associated with a plan. |
| `dim_premium_schedule` | dimension | `premium_schedule_id` | Premium amount schedule for a plan. |
| `dim_fee_schedule` | dimension | `fee_schedule_id` | Fee schedule used to price a service. |
| `dim_hcc` | dimension | `hcc_id` | Hierarchical condition category. |
| `fact_accumulator_entry` | fact | `accumulator_entry_id` | One benefit-accumulator posting from adjudication. |
| `fact_accumulator_snapshot` | fact | `accumulator_snapshot_id` | Month-end accumulator balance for one member and one accumulator type. |
| `fact_fee_schedule_rate` | fact | `fee_schedule_rate_id` | One procedure rate on a fee schedule. |

### bridge

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `bridge_plan_benefit` | bridge | `plan_benefit_id` | Benefit packaged on a plan. |
| `bridge_provider_network` | bridge | `provider_network_id` | Network participation of a provider. |
| `bridge_provider_specialty` | bridge | `provider_specialty_id` | Specialty attested by a provider. |
| `bridge_facility_network` | bridge | `facility_network_id` | Network participation of a facility. |
| `bridge_member_language` | bridge | `member_language_id` | Preferred language of a member. |
| `bridge_coverage_rider` | bridge | `coverage_rider_id` | Optional rider on a coverage. |
| `bridge_formulary_drug` | bridge | `formulary_drug_id` | NDC placed on a formulary tier. |
| `bridge_plan_category` | bridge | `plan_category_id` | Service category covered by a plan. |
| `bridge_group_benefit` | bridge | `group_benefit_id` | Benefit variation for an employer group. |
| `bridge_jurisdiction_state` | bridge | `jurisdiction_state_id` | State included in a jurisdiction. |
| `bridge_diagnosis_hcc` | bridge | `diagnosis_hcc_id` | HCC mapping of a diagnosis. |
| `bridge_procedure_category` | bridge | `procedure_category_id` | Service category of a procedure. |
| `bridge_employee_jurisdiction` | bridge | `employee_jurisdiction_id` | Jurisdiction an employee can work. |
| `bridge_pharmacy_network` | bridge | `pharmacy_network_id` | Network participation of a pharmacy. |
| `bridge_prescriber_specialty` | bridge | `prescriber_specialty_id` | Specialty of a prescriber. |
| `bridge_cob_coverage` | bridge | `cob_coverage_id` | Other coverage recorded for coordination of benefits. |
| `bridge_edit_line` | bridge | `edit_line_id` | Insurance line an edit code applies to. |
| `bridge_revenue_procedure` | bridge | `revenue_procedure_id` | Procedure commonly billed with a revenue code. |
| `bridge_drg_diagnosis` | bridge | `drg_diagnosis_id` | Diagnosis associated with a DRG. |
| `bridge_plan_formulary` | bridge | `plan_formulary_id` | Formulary adopted by a plan. |
| `bridge_network_plan` | bridge | `network_plan_id` | Network offered on a plan. |
| `bridge_facility_taxonomy` | bridge | `facility_taxonomy_id` | Taxonomy of a facility. |
| `bridge_state_locality` | bridge | `state_locality_id` | Locality inside a state. |
| `bridge_provider_facility` | bridge | `provider_facility_id` | Facility where a provider practices. |
| `bridge_member_address` | bridge | `member_address_id` | Residential address of a member. |
| `bridge_contract_plan` | bridge | `contract_plan_id` | Already represented on the contract dimension; this bridge records historical contract-to-plan assignment inside the window. |

### care

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_audit_program` | dimension | `audit_program_id` | Program that draws an audit sample. |
| `dim_fraud_scheme` | dimension | `fraud_scheme_id` | Scheme classification of a fraud lead. |
| `dim_agent` | dimension | `agent_id` | Member-services agent. |
| `fact_call` | fact | `call_id` | One member-services call. |
| `fact_call_event` | fact | `call_event_id` | One event inside a service call. |
| `fact_letter` | fact | `letter_id` | One letter sent to a member. |
| `fact_portal_event` | fact | `portal_event_id` | One authenticated member-portal event. |
| `fact_audit_sample` | fact | `audit_sample_id` | One claim drawn into an audit sample. |
| `fact_fraud_lead` | fact | `fraud_lead_id` | One fraud lead. |
| `fact_grievance` | fact | `grievance_id` | One member grievance. |

### claim

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_claim_header` | fact | `claim_header_id` | One 837 claim header. |
| `fact_claim_admission` | fact | `claim_admission_id` | Admission day of an institutional claim. Professional claims have no admission row. |
| `fact_claim_line` | fact | `claim_line_id` | One 837 service line. |
| `fact_claim_diagnosis` | fact | `claim_diagnosis_id` | One diagnosis reported on a claim header. |
| `fact_claim_status` | fact | `claim_status_id` | One claim-status event for a header. |
| `fact_pricing_result` | fact | `pricing_result_id` | One fee-schedule pricing result for a service line. |
| `fact_claim_edit` | fact | `claim_edit_id` | One pre-adjudication edit result on a claim header. |
| `fact_encounter` | fact | `encounter_id` | One Medicare Advantage encounter submission. |
| `fact_medical_review` | fact | `medical_review_id` | One medical-review action on a service line. |
| `fact_attachment` | fact | `attachment_id` | One attachment linked to a claim header. |
| `fact_claim_note` | fact | `claim_note_id` | One note on a claim header. |

### edi

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_edi_batch` | fact | `edi_batch_id` | One inbound claim batch from a submitter. |

### eligibility

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_eligibility_inquiry` | fact | `eligibility_inquiry_id` | One X12 270 eligibility inquiry. |
| `fact_eligibility_response` | fact | `eligibility_response_id` | One X12 271 response to an eligibility inquiry. |

### member

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_address` | dimension | `address_id` | Postal address. |
| `dim_member` | dimension | `member_id` | Medicare beneficiary in the book of business. |
| `dim_group` | dimension | `group_id` | Group that sponsors a subset of coverage. |
| `dim_coverage` | dimension | `coverage_id` | One coverage span key for a member on a plan. |
| `fact_pcp_attribution` | fact | `pcp_attribution_id` | Month-end primary-care attribution of a member. |
| `fact_risk_score` | fact | `risk_score_id` | Month-end risk score of a member. |
| `fact_hcc_diagnosis` | fact | `hcc_diagnosis_id` | One diagnosis captured for risk adjustment. |
| `fact_enrollment_span` | fact | `enrollment_span_id` | One current enrollment span for a coverage. |
| `fact_disenrollment` | fact | `disenrollment_id` | One disenrollment event. |

### organization

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_state` | dimension | `state_id` | US state or district. |
| `dim_bank` | dimension | `bank_id` | Bank used for provider or premium settlement. |
| `dim_enterprise` | dimension | `enterprise_id` | The processor as one company. |
| `dim_legal_entity` | dimension | `legal_entity_id` | Legal entity that holds a Medicare contract. |
| `dim_jurisdiction` | dimension | `jurisdiction_id` | Geographic jurisdiction the processor administers. |
| `dim_department` | dimension | `department_id` | Internal department. |
| `dim_cost_center` | dimension | `cost_center_id` | Cost center inside a department. |
| `dim_employee` | dimension | `employee_id` | Employee of the processor. |
| `dim_gl_account` | dimension | `gl_account_id` | General-ledger account. |
| `dim_accounting_period` | dimension | `accounting_period_id` | Accounting period of the statistics window. |
| `dim_calendar_day` | dimension | `calendar_day_id` | One day inside the 30-day statistics window. |
| `dim_locality` | dimension | `locality_id` | Medicare payment locality. |
| `dim_trading_partner` | dimension | `trading_partner_id` | Clearinghouse or submitter network. |
| `dim_submitter` | dimension | `submitter_id` | EDI submitter that sends claim batches. |

### pharmacy

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_pharmacy` | dimension | `pharmacy_id` | Dispensing pharmacy. |
| `dim_ndc` | dimension | `ndc_id` | National drug code. |
| `dim_formulary` | dimension | `formulary_id` | Drug formulary. |
| `fact_pharmacy_claim` | fact | `pharmacy_claim_id` | One NCPDP pharmacy claim. |

### premium

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_premium_bill` | fact | `premium_bill_id` | One monthly premium bill for a member. |
| `fact_premium_payment` | fact | `premium_payment_id` | One premium payment. |
| `fact_capitation` | fact | `capitation_id` | One capitation payment line. |
| `fact_premium_adjustment` | fact | `premium_adjustment_id` | One adjustment to a premium bill. |
| `fact_low_income_subsidy` | fact | `low_income_subsidy_id` | One low-income subsidy determination. |

### provider

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_taxonomy` | dimension | `taxonomy_id` | NUCC taxonomy code. |
| `dim_specialty` | dimension | `specialty_id` | Payer specialty grouping. |
| `dim_network` | dimension | `network_id` | Contracted network. |
| `dim_provider` | dimension | `provider_id` | Billing or rendering provider identified by NPI. |
| `dim_facility` | dimension | `facility_id` | Service facility location. |
| `dim_prescriber` | dimension | `prescriber_id` | Prescriber on a pharmacy claim. |
| `fact_provider_enrollment` | fact | `provider_enrollment_id` | One provider enrollment application. |
| `fact_revalidation` | fact | `revalidation_id` | One provider revalidation. |

### reference

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_currency` | dimension | `currency_id` | Currency of a financial fact. |
| `dim_gender` | dimension | `gender_id` | Administrative gender code. |
| `dim_language` | dimension | `language_id` | Language of a member or letter. |
| `dim_relation` | dimension | `relation_id` | Relationship of a person to the subscriber. |
| `dim_lob` | dimension | `lob_id` | Book of business. |
| `dim_insurance_line` | dimension | `insurance_line_id` | Medicare claim type. |
| `dim_cob_type` | dimension | `cob_type_id` | Coordination-of-benefits type. |
| `dim_payment_method` | dimension | `payment_method_id` | How a premium or provider payment was made. |
| `dim_appeal_level` | dimension | `appeal_level_id` | Level of a claim appeal. |
| `dim_review_type` | dimension | `review_type_id` | Medical-review program. |
| `dim_auth_type` | dimension | `auth_type_id` | Prior-authorization type. |
| `dim_service_category` | dimension | `service_category_id` | Benefit category of a procedure. |
| `dim_tier` | dimension | `tier_id` | Pharmacy formulary tier. |
| `dim_accumulator_type` | dimension | `accumulator_type_id` | Benefit accumulator bucket. |
| `dim_discharge_status` | dimension | `discharge_status_id` | Patient discharge status. |
| `dim_admission_type` | dimension | `admission_type_id` | Institutional admission type. |
| `dim_claim_frequency` | dimension | `claim_frequency_id` | Claim frequency code. |
| `dim_filing_indicator` | dimension | `filing_indicator_id` | Claim filing indicator. |
| `dim_place_of_service` | dimension | `place_of_service_id` | CMS place-of-service code. |
| `dim_bill_type` | dimension | `bill_type_id` | Institutional bill type. |
| `dim_occurrence_code` | dimension | `occurrence_code_id` | Institutional occurrence code. |
| `dim_condition_code` | dimension | `condition_code_id` | Institutional condition code. |
| `dim_value_code` | dimension | `value_code_id` | Institutional value code. |
| `dim_patient_status` | dimension | `patient_status_id` | Status of the patient on the claim. |
| `dim_modifier` | dimension | `modifier_id` | CPT or HCPCS modifier. |
| `dim_revenue_code` | dimension | `revenue_code_id` | Institutional revenue code. |
| `dim_denial_reason` | dimension | `denial_reason_id` | Payer denial category. |
| `dim_document_type` | dimension | `document_type_id` | Attachment or letter type. |
| `dim_enrollment_status` | dimension | `enrollment_status_id` | Status of a provider enrollment. |
| `dim_note_type` | dimension | `note_type_id` | Type of a claim note. |
| `dim_interest_reason` | dimension | `interest_reason_id` | Why interest was paid on a claim. |
| `dim_withhold_reason` | dimension | `withhold_reason_id` | Why an amount was withheld. |
| `dim_lis_level` | dimension | `lis_level_id` | Low-income subsidy level. |
| `dim_risk_model` | dimension | `risk_model_id` | Risk-adjustment model. |
| `dim_edit_code` | dimension | `edit_code_id` | Pre-adjudication edit. |
| `dim_call_queue` | dimension | `call_queue_id` | Member-services queue. |
| `dim_procedure` | dimension | `procedure_id` | CPT or HCPCS procedure code. |
| `dim_diagnosis` | dimension | `diagnosis_id` | ICD-10-CM diagnosis code. |
| `dim_drg` | dimension | `drg_id` | Diagnosis-related group. |
| `dim_carc` | dimension | `carc_id` | Claim adjustment reason code. |
| `dim_rarc` | dimension | `rarc_id` | Remittance advice remark code. |

### remit

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_remit_advice` | fact | `remit_advice_id` | One 835 remittance advice. |
| `fact_remit_line` | fact | `remit_line_id` | One 835 service payment line. |
| `fact_remit_adjustment` | fact | `remit_adjustment_id` | One CAS adjustment on a remit line. |
| `fact_cob_line` | fact | `cob_line_id` | One coordination-of-benefits amount on a service line. |
| `fact_provider_payment` | fact | `provider_payment_id` | One EFT or check to a provider. |
| `fact_interest_payment` | fact | `interest_payment_id` | One interest payment on a late claim. |
| `fact_withhold` | fact | `withhold_id` | One withhold against a provider payment. |
| `fact_overpayment` | fact | `overpayment_id` | One identified overpayment. |
| `fact_recovery` | fact | `recovery_id` | One recovery against an overpayment. |

### um

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_prior_auth` | fact | `prior_auth_id` | One prior authorization. |
| `fact_auth_line` | fact | `auth_line_id` | One service line requested on a prior authorization. |
| `fact_auth_decision` | fact | `auth_decision_id` | One decision on a prior authorization. |
| `fact_referral` | fact | `referral_id` | One referral from one provider to another. |
| `fact_referral_target` | fact | `referral_target_id` | Provider who received one referral. |

## Provenance

Harbor Medicare Services is fictional. CMS reported in its fiscal year 2025 financial report that Medicare routinely processes over one billion fee-for-service claims a year and that enrollment is roughly 68 million people. The member dimension uses 68 million. The claim-header fact uses 84 million rows in a 30-day window, which annualizes to 1.008 billion claims. Service-line fan-out of five lines per header, remittance and adjustment multiples, eligibility at four inquiries per header, and the month-end accumulator snapshot of eight types per member are authored structural fan-outs, not additional CMS statistics. Header and line are separate facts because an 837 claim is one header and many service lines, which is also the Kimball rule that facts stay true to one grain. Remittance distinguishes the 835 advice, the service line, and the adjustment. Pharmacy is separate because NCPDP claim transactions are not 837 service lines. No payer platform DDL was copied.
