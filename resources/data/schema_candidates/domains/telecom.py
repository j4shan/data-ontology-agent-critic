"""Warehouse-style ontology for Northline Mobile usage, charging, and billing."""

from domains.assemble import build_datasets, link as L, measure as M, spec

_NARRATIVE = """
Northline Mobile is a national mobile network operator. The catalog is the warehouse-style ontology of its usage, online charging, mediation, roaming, and retail billing systems. Subscribers, subscriptions, cells, and rate plans are conformed dimensions. Call detail records, charging events, balance movements, and invoices are facts.

The usage landing zone follows 3GPP charging management. A charging data record is the formatted collection of one or more chargeable events that the network transfers to the billing domain. Voice, SMS, content, and packet-data records are separate facts because their measures differ. Packet-data volume is dominated by PGW and SMF records, including partial records for long sessions. An online charging event is finer than a closed CDR: reservations and debits are their own facts. Roaming usage that is exchanged with other operators lands on TAP-out and TAP-in facts. Cell counters are a 15-minute periodic snapshot, one row per cell per interval.

A billing account has one invoice in the statistics window. An invoice has many charge lines. A subscription has one service instance and one month-end bundle snapshot. Organization runs from the enterprise through legal entities, regions, and markets to cell sites and cells. The synthetic 30-day populations and the join fan-out derived from these rules are recorded beside the catalog, not inside the graph YAML.
"""

_PROVENANCE = """
Northline Mobile is a fictional operator. The mediated-CDR total of 2.1 billion rows in a 30-day window is the volume reported for one national operator's mediation pipeline (2.1 billion call detail records a month, covering voice, SMS, and data). CDR parameters, partial records, and the split between a CDR and a charging event follow 3GPP TS 32.298, TS 32.297, and TS 32.240. Shared business entities follow the TM Forum Information Framework (SID) at the level of party, product, service, and usage, without copying the SID model. Roaming interchange follows the GSMA TAP3 pattern of an outcollect and incollect usage record. Cell-counter grain is the Kimball periodic snapshot: one measurement per cell per 15-minute interval. The 85,000 cells and 28,000 sites are a synthetic national macro footprint, not an operator inventory. Online-charging volume is authored at three charging events per mediated CDR. No vendor DDL was copied.
"""

_QUESTIONS = """
1. Which subscription, subscriber, cell, and rate plan produced each data CDR, and how much volume did it carry?
   `telecom-mobile.usage.fact_data_cdr` joins `dim_subscription`, `dim_subscriber`, `dim_cell`, `dim_rate_plan`, and `dim_calendar_day`. `uplink_bytes` and `downlink_bytes` are measures of that CDR row.

2. Which voice CDRs were roaming, and which roaming partner and visited PLMN applied?
   `fact_voice_cdr.roaming_partner_id` is optional. When it is present it joins `dim_roaming_partner`. `visited_plmn_id` joins `dim_plmn`. Home usage leaves the roaming partner empty.

3. How many online charging events, reservations, and debits did a subscription generate?
   `telecom-mobile.charging.fact_charging_event` joins `dim_subscription`. `fact_balance_reservation` joins one charging event, one-to-one, and not every charging event has a reservation. `fact_balance_debit` joins one reservation the same way.

4. What rated charge was produced from a mediated CDR, and which invoice line billed it?
   `fact_rated_charge` may join `fact_data_cdr`, `fact_voice_cdr`, `fact_sms_cdr`, or `fact_content_cdr` one-to-one. `fact_invoice_line.rated_charge_id` may join that rated charge. Every invoice line joins `fact_invoice`.

5. Which cell sites sit in a market, and which cells belong to each site?
   `dim_cell_site.market_id` joins `dim_market` as `1:many` with a required match both ways. `dim_cell.cell_site_id` joins `dim_cell_site` the same way.

6. Who manages each market?
   `dim_market.market_manager_employee_id` joins `dim_employee` one-to-one. Every market has one manager. An employee manages at most one market.

7. What is on a billing account's invoice for the window?
   `fact_invoice` joins `dim_billing_account` one-to-one in both directions: every account has one invoice, and every invoice has one account. `fact_invoice_line` is `1:many` from that invoice with a required match both ways. `fact_document` joins the invoice one-to-one as the bill document.

8. Which TAP-out records were raised for roaming usage?
   `telecom-mobile.roaming.fact_tap_out` joins `dim_roaming_partner` with a required match both ways, and may join the voice CDR or the data CDR that was outcollected.

9. What allowance did a subscription draw, and which rated charge caused the draw?
   `fact_allowance_draw` joins `dim_subscription` and `dim_allowance_bucket`. The rated charge is optional.

10. Which mediation file did a network element emit each day, and which data CDRs were rejected?
    `fact_mediation_file` joins `dim_network_element` and `dim_calendar_day` as `1:many` with a required match both ways. `fact_mediation_reject` may join a data, voice, or SMS CDR.

11. How did a subscriber move between cells?
    `fact_handover.source_cell_id` joins `dim_cell`. The cell entered is `fact_handover_target.target_cell_id`, and that target row joins the handover one-to-one. Source and target stay on different datasets so each join to `dim_cell` is a single column.

12. Which dealer sold a subscription, and which add-ons are attached to it?
    `fact_dealer_sale` joins `dim_dealer` with a required match both ways, and joins `dim_subscription`. `bridge_subscription_addon` joins `dim_subscription` and `dim_addon`.
"""


def _dim(subject, name, display, description, rows, links=(), measures=(), synonyms=()):
    return spec(subject, name, "dimension", display, description, rows, links, measures, synonyms)


def _fact(subject, name, display, description, rows, links=(), measures=(), volume_class="transaction", synonyms=()):
    return spec(
        subject,
        name,
        "fact",
        display,
        description,
        rows,
        links,
        measures,
        synonyms,
        volume_class=volume_class,
    )


def _bridge(name, display, description, rows, links, measures=()):
    return spec("bridge", name, "bridge", display, description, rows, links, measures)


def _datasets() -> list[dict]:
    code_sets = [
        ("reference", "dim_channel", "Channel", "Sales or care channel.", 8, "retail, digital, telesales, dealer, care, chat, app, uSSD"),
        ("reference", "dim_currency", "Currency", "ISO currency used for charges and invoices.", 12, "USD, EUR, GBP, CAD, MXN, BRL, JPY, AUD, CHF, INR, ZAR, AED"),
        ("reference", "dim_technology", "Technology", "Radio access technology.", 6, "2G, 3G, 4G, 5G-NSA, 5G-SA, WiFi"),
        ("reference", "dim_call_type", "Call Type", "Usage class on a CDR.", 12, "MOC, MTC, emergency, CF, SMS-MO, SMS-MT, MMS, data, video, USSD, content, supplemental"),
        ("reference", "dim_record_type", "Record Type", "3GPP CDR or event type.", 24, "MOC, MTC, SMS-MO, SMS-MT, SGW, PGW, SMF, CHF, IMS, MMS, TAP, content"),
        ("reference", "dim_time_band", "Time Band", "Peak or off-peak band used by a tariff.", 8, "peak, off-peak, weekend, night, holiday, flat, promo, special"),
        ("reference", "dim_charge_type", "Charge Type", "Class of a rated or invoice charge.", 16, "usage, recurring, one-time, roaming, content, discount, tax, adjustment"),
        ("reference", "dim_balance_type", "Balance Type", "Prepaid or allowance balance that charging can touch.", 10, "monetary, voice, sms, data, roaming, promo, credit, deposit, reward, tax"),
        ("reference", "dim_dunning_level", "Dunning Level", "Collections stage of a billing account.", 5, "reminder, notice, restrict, suspend, writeoff"),
        ("reference", "dim_payment_method", "Payment Method", "How a payment or top-up was tendered.", 8, "card, ACH, cash, voucher, wallet, direct-debit, benefit, adjustment"),
        ("reference", "dim_adjustment_reason", "Adjustment Reason", "Why a balance or invoice was adjusted.", 40, "goodwill, rating-error, roaming-dispute, tax, fraud, rebate, writeoff, duplicate"),
        ("reference", "dim_barring", "Barring Profile", "Service bar that can be applied to a subscription.", 15, "outgoing, premium, roaming, data, international, content, all"),
        ("reference", "dim_handover_type", "Handover Type", "Mobility procedure that moved a session.", 8, "intra-eNB, X2, S1, intra-gNB, Xn, N2, inter-RAT, SRVCC"),
        ("reference", "dim_language", "Language", "Language of a bill or care contact.", 20, "en, es, fr, de, pt, zh, ar, hi, vi, ko"),
        ("reference", "dim_segment", "Customer Segment", "Marketing segment of a billing account.", 12, "consumer, youth, family, smb, enterprise, prepaid, IoT, MVNO, government, staff"),
        ("reference", "dim_credit_class", "Credit Class", "Credit treatment of a billing account.", 8, "prime, standard, subprime, deposit, prepaid, suspended, written-off, staff"),
        ("reference", "dim_bill_cycle", "Bill Cycle", "Monthly cycle that closes an account.", 6, "cycle-01, cycle-05, cycle-10, cycle-15, cycle-20, cycle-25"),
        ("reference", "dim_file_format", "File Format", "CDR file format on the billing-domain transfer.", 4, "BER, XML, CSV, TAP3"),
        ("reference", "dim_alarm_severity", "Alarm Severity", "Severity of a network alarm.", 5, "critical, major, minor, warning, cleared"),
        ("reference", "dim_core_function", "Core Function", "3GPP core function of a network element.", 10, "MSC, SGSN, MME, SGW, PGW, AMF, SMF, UPF, PCF, CHF"),
        ("reference", "dim_site_type", "Site Type", "Construction type of a cell site.", 5, "macro, micro, pico, indoor, rooftop"),
        ("reference", "dim_unit", "Unit", "Unit of a usage measure.", 10, "second, byte, message, event, currency, percent"),
        ("reference", "dim_account_status", "Account Status", "Status of a billing account.", 6, "active, prospect, suspended, closed, collections, fraud"),
        ("reference", "dim_subscription_status", "Subscription Status", "Status of a subscription.", 8, "pending, active, barred, suspended, porting, closed, prepaid, test"),
        ("reference", "dim_sale_type", "Sale Type", "How a dealer sale was classified.", 6, "new, upgrade, add-on, prepaid, MNP, device"),
        ("reference", "dim_journal_source", "Journal Source", "Subledger that produced a journal line.", 8, "billing, rating, roaming, cash, tax, fixed-asset, inventory, manual"),
        ("reference", "dim_document_type", "Document Type", "Kind of customer document.", 12, "invoice, credit-note, dunning, contract, receipt, tax-statement"),
        ("reference", "dim_qos", "QoS Profile", "QoS profile applied to a session.", 30, "conversational, streaming, interactive, background, mission-critical, IMS-voice"),
        ("reference", "dim_apn", "APN DNN", "Access point name or data network name.", 80, "internet, ims, mms, enterprise, iot, tethering"),
        ("reference", "dim_destination_zone", "Destination Zone", "Rating zone for a called number or roaming partner.", 90, "home, on-net, off-net, national, international, satellite, premium"),
        ("reference", "dim_allowance_bucket", "Allowance Bucket", "Included usage bucket on a plan.", 40, "voice-national, sms, data-home, data-roam, hotspot, video"),
        ("care", "dim_sla", "SLA", "Care or network service level.", 20, "care-24h, care-4h, network-critical, network-major"),
        ("care", "dim_script", "Care Script", "Script a care agent follows.", 30, "billing, coverage, device, port-in, retention"),
        ("care", "dim_care_reason", "Care Reason", "Reason recorded on a care interaction.", 50, "bill-explain, payment, coverage, device, complaint, retention"),
        ("product", "dim_cell_band", "Spectrum Band", "Radio band a cell can use.", 16, "n71, n41, n77, b2, b4, b12, b66, GSM850"),
    ]
    tables = []
    for subject, name, display, description, rows, codes in code_sets:
        tables.append(
            _dim(
                subject,
                name,
                display,
                description,
                rows,
                measures=[M("code", f"Code for the {display.lower()}.", codes)],
            )
        )
    tables.extend(
        [
            _dim("organization", "dim_enterprise", "Enterprise", "The mobile operator as one company.", 1, measures=[M("enterprise_name", "Registered name of the operator.")]),
            _dim("organization", "dim_legal_entity", "Legal Entity", "Incorporated carrier entity that owns markets and the ledger.", 4, [L("enterprise_id", "dim_enterprise", "n1!", "Every operating company sits under the one enterprise.")], [M("legal_entity_name", "Registered name of the legal entity.")]),
            _dim("organization", "dim_region", "Region", "Operating region inside a legal entity.", 6, [L("legal_entity_id", "dim_legal_entity", "n1")], [M("region_name", "Name of the region.")]),
            _dim("organization", "dim_department", "Department", "Organizational department.", 80, [L("legal_entity_id", "dim_legal_entity", "n1")], [M("department_name", "Name of the department.")]),
            _dim("organization", "dim_cost_center", "Cost Center", "Cost center that collects labor and network cost.", 240, [L("department_id", "dim_department", "n1!", "Every department owns at least one cost center."), L("legal_entity_id", "dim_legal_entity", "n1")], [M("cost_center_name", "Name of the cost center.")]),
            _dim("organization", "dim_employee", "Employee", "Employee of the operator.", 42_000, [L("department_id", "dim_department", "n1"), L("cost_center_id", "dim_cost_center", "n1"), L("market_id", "dim_market", "n1")], [M("employee_name", "Name of the employee.")], ["employee", "worker"]),
            _dim("organization", "dim_market", "Market", "Geographic market that contains cell sites and accounts.", 18, [L("region_id", "dim_region", "n1!", "Every region operates at least one market."), L("legal_entity_id", "dim_legal_entity", "n1"), L("market_manager_employee_id", "dim_employee", "11", "A market has one manager, and an employee manages at most one market.")], [M("market_name", "Name of the market.")]),
            _dim("organization", "dim_dealer", "Dealer", "Retail dealer that can sell a subscription.", 1_200, [L("market_id", "dim_market", "n1"), L("channel_id", "dim_channel", "n1")], [M("dealer_name", "Trade name of the dealer.")]),
            _dim("organization", "dim_workgroup", "Workgroup", "Care or field workgroup inside a department.", 120, [L("department_id", "dim_department", "n1!")], [M("workgroup_name", "Name of the workgroup.")]),
            _dim("finance", "dim_gl_account", "GL Account", "General-ledger account.", 800, [L("legal_entity_id", "dim_legal_entity", "n1")], [M("account_name", "Name of the ledger account.")]),
            _dim("finance", "dim_accounting_period", "Accounting Period", "Open accounting period covering the statistics window.", 1, [L("legal_entity_id", "dim_legal_entity", "n1")], [M("period_name", "Name of the accounting period.")]),
            _dim("finance", "dim_tax_jurisdiction", "Tax Jurisdiction", "Tax authority that can apply to a charge.", 60, [L("country_id", "dim_country", "n1")], [M("jurisdiction_name", "Name of the tax jurisdiction.")]),
            _dim("finance", "dim_bank", "Bank", "Bank that settles a payment or interconnect invoice.", 25, [L("country_id", "dim_country", "n1")], [M("bank_name", "Name of the bank.")]),
            _dim("reference", "dim_country", "Country", "Country of an address, number, or partner.", 240, measures=[M("iso_code", "ISO country code."), M("country_name", "Name of the country.")]),
            _dim("reference", "dim_calendar_day", "Calendar Day", "One day inside the 30-day statistics window.", 30, measures=[M("calendar_date", "Civil date of the day.")]),
            _dim("party", "dim_address", "Address", "Postal or site address.", 18_000_000, [L("country_id", "dim_country", "n1")], [M("locality", "City or locality of the address.")]),
            _dim("party", "dim_party", "Party", "Person or organization that can hold an account.", 22_000_000, [L("country_id", "dim_country", "n1"), L("address_id", "dim_address", "n1?", "A party may still be unidentified to a service address.", match_rate=0.9)], [M("party_name", "Name of the party.")]),
            _dim("party", "dim_billing_account", "Billing Account", "Account that receives one invoice in the window.", 16_000_000, [L("party_id", "dim_party", "n1"), L("currency_id", "dim_currency", "n1"), L("bill_cycle_id", "dim_bill_cycle", "n1!", "Every bill cycle has accounts."), L("market_id", "dim_market", "n1!", "Every market has billing accounts."), L("legal_entity_id", "dim_legal_entity", "n1"), L("segment_id", "dim_segment", "n1!", "Every segment is in use."), L("credit_class_id", "dim_credit_class", "n1!")], [M("account_number", "Business number of the billing account.")]),
            _dim("party", "dim_subscriber", "Subscriber", "Person or device identity that uses the network.", 20_000_000, [L("billing_account_id", "dim_billing_account", "n1!", "Every billing account has at least one subscriber."), L("party_id", "dim_party", "n1")], [M("subscriber_name", "Name shown on the subscription.")], ["subscriber", "mobile subscriber"]),
            _dim("party", "dim_msisdn", "Public Number", "MSISDN that can be assigned to a subscription.", 27_000_000, [L("country_id", "dim_country", "n1")], [M("e164", "E.164 rendering of the number.")]),
            _dim("party", "dim_subscription", "Subscription", "Contracted service that rates usage.", 25_000_000, [L("subscriber_id", "dim_subscriber", "n1!", "Every subscriber has at least one subscription."), L("rate_plan_id", "dim_rate_plan", "n1!", "Every rate plan has subscriptions."), L("market_id", "dim_market", "n1"), L("msisdn_id", "dim_msisdn", "11", "Each subscription has one public number, and some numbers are spare.")], [M("activated_on", "Date the subscription activated.")]),
            _dim("network", "dim_plmn", "PLMN", "Public land mobile network, home or visited.", 900, [L("country_id", "dim_country", "n1")], [M("mcc_mnc", "Mobile country and network code."), M("home_role", "Whether the PLMN is home or visited.", "home, partner, other")]),
            _dim("network", "dim_imsi", "IMSI", "International mobile subscriber identity.", 26_000_000, [L("plmn_id", "dim_plmn", "n1")], [M("imsi_value", "IMSI digits.")]),
            _dim("party", "dim_sim", "SIM", "SIM or eSIM profile.", 24_000_000, [L("imsi_id", "dim_imsi", "11", "Each SIM carries one IMSI, and some IMSIs are unassigned."), L("subscription_id", "dim_subscription", "n1?", "A SIM in stock is not on a subscription.", match_rate=0.96)]),
            _dim("product", "dim_vendor", "Vendor", "Network or device vendor.", 40, measures=[M("vendor_name", "Name of the vendor.")]),
            _dim("product", "dim_device_model", "Device Model", "Handset or CPE model.", 1_800, [L("vendor_id", "dim_vendor", "n1!", "Every vendor has at least one model.")], [M("model_name", "Commercial name of the model.")]),
            _dim("party", "dim_device", "Device", "Handset or module seen on the network.", 23_000_000, [L("device_model_id", "dim_device_model", "n1!", "Every model has devices."), L("subscriber_id", "dim_subscriber", "n1?", "A device in inventory has no subscriber.", match_rate=0.85)]),
            _dim("party", "dim_contact", "Contact", "Phone, email, or postal contact for a party.", 20_500_000, [L("party_id", "dim_party", "n1")], [M("contact_value", "Contact address or number.")]),
            _dim("product", "dim_product_spec", "Product Spec", "Technical product specification.", 220, [L("technology_id", "dim_technology", "n1")], [M("spec_name", "Name of the specification.")]),
            _dim("product", "dim_product_offering", "Product Offering", "Sellable offering built on a product spec.", 500, [L("product_spec_id", "dim_product_spec", "n1!", "Every product spec is offered.")], [M("offering_name", "Commercial name of the offering.")]),
            _dim("product", "dim_rate_plan", "Rate Plan", "Price plan assigned to subscriptions.", 420, [L("product_offering_id", "dim_product_offering", "n1"), L("currency_id", "dim_currency", "n1")], [M("plan_name", "Name of the rate plan.")]),
            _dim("product", "dim_addon", "Add On", "Optional product attached to a subscription.", 260, [L("product_offering_id", "dim_product_offering", "n1")], [M("addon_name", "Name of the add-on.")]),
            _dim("product", "dim_price", "Price", "Price point of an offering.", 2_400, [L("product_offering_id", "dim_product_offering", "n1!", "Every offering has a price."), L("currency_id", "dim_currency", "n1")], [M("amount", "List amount of the price.")]),
            _dim("product", "dim_discount", "Discount", "Discount that can apply to a rate plan.", 180, [L("rate_plan_id", "dim_rate_plan", "n1?", "A discount may be account-specific rather than plan-wide.", match_rate=0.8)], [M("discount_name", "Name of the discount.")]),
            _dim("product", "dim_tariff", "Tariff", "Usage tariff for a zone and charge type.", 1_100, [L("currency_id", "dim_currency", "n1"), L("destination_zone_id", "dim_destination_zone", "n1?", "A tariff may be zone-independent.", match_rate=0.9), L("charge_type_id", "dim_charge_type", "n1!")], [M("rate_amount", "Rate amount per unit.")]),
            _dim("product", "dim_tax_code", "Tax Code", "Tax treatment of a charge.", 40, [L("gl_account_id", "dim_gl_account", "n1?", "A memorandum tax code may have no ledger account.", match_rate=0.9)], [M("tax_name", "Name of the tax code.")]),
            _dim("network", "dim_roaming_partner", "Roaming Partner", "Operator that exchanges roaming usage.", 640, [L("plmn_id", "dim_plmn", "n1"), L("country_id", "dim_country", "n1")], [M("partner_name", "Name of the roaming partner.")]),
            _dim("network", "dim_tac", "Tracking Area", "Tracking area that groups cells.", 400, [L("market_id", "dim_market", "n1!", "Every market has tracking areas.")], [M("tac_code", "Tracking area code.")]),
            _dim("network", "dim_location_area", "Location Area", "Location area used by mobility updates.", 3_200, [L("market_id", "dim_market", "n1!")], [M("lac_code", "Location area code.")]),
            _dim("network", "dim_recording_entity", "Recording Entity", "Network function that closes CDRs.", 400, [L("core_function_id", "dim_core_function", "n1!")], [M("entity_name", "Name of the recording entity.")]),
            _dim("network", "dim_cell_site", "Cell Site", "Physical site that holds one or more cells.", 28_000, [L("market_id", "dim_market", "n1!", "Every market has cell sites."), L("region_id", "dim_region", "n1"), L("address_id", "dim_address", "n1"), L("site_type_id", "dim_site_type", "n1!")], [M("site_name", "Name of the cell site.")]),
            _dim("network", "dim_cell", "Cell", "Sector or cell that serves a session.", 85_000, [L("cell_site_id", "dim_cell_site", "n1!", "Every cell site has at least one cell."), L("technology_id", "dim_technology", "n1!", "Every technology has cells."), L("tac_id", "dim_tac", "n1")], [M("cell_name", "Name of the cell."), M("eci", "E-UTRAN or NR cell identity.")], ["cell", "sector"]),
            _dim("network", "dim_network_element", "Network Element", "Switch, gateway, or function that records usage.", 12_000, [L("cell_site_id", "dim_cell_site", "n1?", "A core element is not tied to one site.", match_rate=0.7), L("technology_id", "dim_technology", "n1"), L("plmn_id", "dim_plmn", "n1"), L("recording_entity_id", "dim_recording_entity", "n1!", "Every recording entity has elements."), L("vendor_id", "dim_vendor", "n1!"), L("core_function_id", "dim_core_function", "n1!")], [M("element_name", "Name of the network element.")]),
            _dim("network", "dim_slice", "Network Slice", "5G network slice.", 12, [L("qos_id", "dim_qos", "n1?", "A slice may inherit QoS per session.", match_rate=0.8)], [M("slice_name", "Name of the slice.")]),
            _dim("network", "dim_mediation_rule", "Mediation Rule", "Rule that accepts or rejects a CDR.", 150, measures=[M("rule_name", "Name of the mediation rule.")]),
            _dim("network", "dim_policy_rule", "Policy Rule", "PCF or PCRF rule.", 60, [L("qos_id", "dim_qos", "n1?", match_rate=0.7), L("slice_id", "dim_slice", "n1?", match_rate=0.4)], [M("rule_name", "Name of the policy rule.")]),
            _dim("product", "dim_rating_group", "Rating Group", "Online-charging rating group.", 200, [L("charge_type_id", "dim_charge_type", "n1!")], [M("group_code", "Rating group code.")]),
            _dim("reference", "dim_release_cause", "Release Cause", "Cause that closed a session or call.", 180, measures=[M("cause_code", "Protocol cause code.")]),
            _dim("reference", "dim_number_prefix", "Number Prefix", "Dialed or called-party prefix.", 5_000, [L("country_id", "dim_country", "n1"), L("destination_zone_id", "dim_destination_zone", "n1?", match_rate=0.95, coverage=0.8)], [M("prefix", "Digit prefix.")]),
            _dim("product", "dim_content_provider", "Content Provider", "Provider of a charged content event.", 350, [L("country_id", "dim_country", "n1")], [M("provider_name", "Name of the content provider.")]),
            _dim("network", "dim_carrier", "Interconnect Carrier", "Carrier that invoices interconnection.", 80, [L("country_id", "dim_country", "n1")], [M("carrier_name", "Name of the carrier.")]),
            _dim("network", "dim_interconnect_trunk", "Interconnect Trunk", "Trunk group toward an interconnect carrier.", 2_200, [L("carrier_id", "dim_carrier", "n1!", "Every carrier has a trunk."), L("plmn_id", "dim_plmn", "n1")], [M("trunk_name", "Name of the trunk group.")]),
            _dim("care", "dim_fraud_rule", "Fraud Rule", "Rule that raises a fraud alert.", 90, measures=[M("rule_name", "Name of the fraud rule.")]),
            _dim("care", "dim_agent", "Care Agent", "Care employee who handles interactions.", 6_000, [L("employee_id", "dim_employee", "11", "Each care agent is one employee, and most employees are not agents."), L("department_id", "dim_department", "n1")], [M("agent_name", "Name of the care agent.")]),
            _dim("care", "dim_queue", "Care Queue", "Queue that receives care interactions.", 40, [L("department_id", "dim_department", "n1")], [M("queue_name", "Name of the queue.")]),
            _dim("care", "dim_trouble_code", "Trouble Code", "Code that classifies a trouble ticket.", 300, measures=[M("code", "Trouble code.")]),
            _dim("party", "dim_np_operator", "Porting Operator", "Operator on the other side of a number port.", 40, [L("country_id", "dim_country", "n1")], [M("operator_name", "Name of the porting operator.")]),
            _dim("product", "dim_service", "Service", "Customer-facing service instance for a subscription.", 25_000_000, [L("subscription_id", "dim_subscription", "11!", "Each subscription has one service instance, and each service instance has one subscription."), L("product_spec_id", "dim_product_spec", "n1!")], [M("service_status", "Status of the service.", "designed, active, suspended, ceased")]),
            _dim("network", "dim_resource", "Resource", "Network resource assigned to a service, SIM, or device.", 30_000_000, [L("service_id", "dim_service", "n1?", "A spare resource is not on a service.", match_rate=0.8), L("sim_id", "dim_sim", "n1?", match_rate=0.5), L("device_id", "dim_device", "n1?", match_rate=0.4)]),
            _dim("finance", "dim_cost_element", "Cost Element", "Cost element inside a cost center.", 60, [L("gl_account_id", "dim_gl_account", "n1")], [M("element_name", "Name of the cost element.")]),
            _dim("care", "dim_collection_agency", "Collection Agency", "External agency that can receive a referral.", 8, measures=[M("agency_name", "Name of the collection agency.")]),
            _dim("product", "dim_campaign", "Campaign", "Acquisition or retention campaign.", 60, [L("channel_id", "dim_channel", "n1!")], [M("campaign_name", "Name of the campaign.")]),
            _fact(
                "usage",
                "fact_data_cdr",
                "Data CDR",
                "One closed or partial packet-data CDR transferred to billing.",
                1_400_000_000,
                [
                    L("subscription_id", "dim_subscription", "n1", "Usage is rated on the subscription.", coverage=0.94),
                    L("subscriber_id", "dim_subscriber", "n1", coverage=0.94),
                    L("cell_id", "dim_cell", "n1", coverage=0.99),
                    L("cell_site_id", "dim_cell_site", "n1", coverage=0.99),
                    L("technology_id", "dim_technology", "n1!"),
                    L("apn_id", "dim_apn", "n1!"),
                    L("qos_id", "dim_qos", "n1"),
                    L("rating_group_id", "dim_rating_group", "n1"),
                    L("record_type_id", "dim_record_type", "n1!"),
                    L("plmn_id", "dim_plmn", "n1", coverage=0.2),
                    L("roaming_partner_id", "dim_roaming_partner", "n1?", "Home data has no roaming partner.", match_rate=0.12, coverage=0.4),
                    L("network_element_id", "dim_network_element", "n1"),
                    L("recording_entity_id", "dim_recording_entity", "n1!"),
                    L("calendar_day_id", "dim_calendar_day", "n1!", "Every day in the window has data CDRs."),
                    L("release_cause_id", "dim_release_cause", "n1?", match_rate=0.8, coverage=0.7),
                    L("rate_plan_id", "dim_rate_plan", "n1"),
                    L("imsi_id", "dim_imsi", "n1", coverage=0.9),
                    L("msisdn_id", "dim_msisdn", "n1", coverage=0.9),
                    L("slice_id", "dim_slice", "n1?", "4G sessions have no slice.", match_rate=0.35),
                    L("mediation_file_id", "fact_mediation_file", "n1!", "Every mediation file in the window contains data CDRs."),
                ],
                [M("uplink_bytes", "Uplink volume on the CDR."), M("downlink_bytes", "Downlink volume on the CDR."), M("duration_seconds", "Recorded duration of the CDR.")],
                synonyms=["PGW CDR", "SMF CDR", "data record"],
            ),
            _fact(
                "usage",
                "fact_voice_cdr",
                "Voice CDR",
                "One voice call detail record.",
                520_000_000,
                [
                    L("subscription_id", "dim_subscription", "n1", coverage=0.62),
                    L("subscriber_id", "dim_subscriber", "n1", coverage=0.62),
                    L("cell_id", "dim_cell", "n1", coverage=0.9),
                    L("technology_id", "dim_technology", "n1"),
                    L("call_type_id", "dim_call_type", "n1!"),
                    L("record_type_id", "dim_record_type", "n1!"),
                    L("plmn_id", "dim_plmn", "n1", coverage=0.25),
                    L("roaming_partner_id", "dim_roaming_partner", "n1?", "Home voice has no roaming partner.", match_rate=0.08, coverage=0.35),
                    L("network_element_id", "dim_network_element", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("release_cause_id", "dim_release_cause", "n1", coverage=0.6),
                    L("rate_plan_id", "dim_rate_plan", "n1"),
                    L("msisdn_id", "dim_msisdn", "n1", coverage=0.62),
                    L("destination_zone_id", "dim_destination_zone", "n1"),
                    L("number_prefix_id", "dim_number_prefix", "n1?", match_rate=0.9, coverage=0.5),
                    L("time_band_id", "dim_time_band", "n1!"),
                ],
                [M("duration_seconds", "Conversation duration."), M("setup_seconds", "Setup time before answer.")],
            ),
            _fact(
                "usage",
                "fact_sms_cdr",
                "SMS CDR",
                "One short-message CDR.",
                150_000_000,
                [
                    L("subscription_id", "dim_subscription", "n1", coverage=0.4),
                    L("subscriber_id", "dim_subscriber", "n1", coverage=0.4),
                    L("call_type_id", "dim_call_type", "n1"),
                    L("record_type_id", "dim_record_type", "n1!"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("rate_plan_id", "dim_rate_plan", "n1"),
                    L("msisdn_id", "dim_msisdn", "n1", coverage=0.4),
                    L("destination_zone_id", "dim_destination_zone", "n1"),
                    L("plmn_id", "dim_plmn", "n1", coverage=0.15),
                ],
                [M("message_count", "Messages represented by the CDR, usually one.")],
            ),
            _fact(
                "usage",
                "fact_content_cdr",
                "Content CDR",
                "One content or premium event CDR.",
                30_000_000,
                [
                    L("content_provider_id", "dim_content_provider", "n1!", "Every content provider has events in the window."),
                    L("subscription_id", "dim_subscription", "n1", coverage=0.15),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("charge_type_id", "dim_charge_type", "n1"),
                    L("currency_id", "dim_currency", "n1"),
                ],
                [M("content_amount", "Gross content charge.")],
            ),
            _fact(
                "mediation",
                "fact_mediation_file",
                "Mediation File",
                "One CDR file emitted by a network element on one day.",
                360_000,
                [
                    L("network_element_id", "dim_network_element", "n1!", "Every network element emits one file each day of the window."),
                    L("calendar_day_id", "dim_calendar_day", "n1!", "Every day has mediation files."),
                    L("file_format_id", "dim_file_format", "n1!"),
                    L("recording_entity_id", "dim_recording_entity", "n1!"),
                ],
                [M("file_name", "Transfer file name."), M("record_count", "CDR records declared in the file header.")],
                volume_class="transaction",
            ),
            _fact(
                "charging",
                "fact_charging_event",
                "Charging Event",
                "One online charging event sent toward the charging function.",
                6_300_000_000,
                [
                    L("subscription_id", "dim_subscription", "n1", coverage=0.97),
                    L("subscriber_id", "dim_subscriber", "n1", coverage=0.97),
                    L("record_type_id", "dim_record_type", "n1!"),
                    L("rating_group_id", "dim_rating_group", "n1!"),
                    L("balance_type_id", "dim_balance_type", "n1!"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("network_element_id", "dim_network_element", "n1"),
                    L("qos_id", "dim_qos", "n1"),
                    L("apn_id", "dim_apn", "n1"),
                    L("rate_plan_id", "dim_rate_plan", "n1"),
                    L("plmn_id", "dim_plmn", "n1", coverage=0.2),
                ],
                [M("requested_units", "Units requested on the event."), M("used_units", "Units reported used on the event.")],
                synonyms=["CHF event", "online charging event"],
            ),
            _fact(
                "charging",
                "fact_balance_reservation",
                "Balance Reservation",
                "One quota reservation against a charging event.",
                4_200_000_000,
                [
                    L("charging_event_id", "fact_charging_event", "11", "A reservation matches one charging event, and some events do not reserve."),
                    L("subscription_id", "dim_subscription", "n1", coverage=0.95),
                    L("balance_type_id", "dim_balance_type", "n1!"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                ],
                [M("reserved_units", "Units reserved.")],
            ),
            _fact(
                "charging",
                "fact_balance_debit",
                "Balance Debit",
                "One debit that consumes a reservation.",
                3_150_000_000,
                [
                    L("balance_reservation_id", "fact_balance_reservation", "11", "A debit matches one reservation, and some reservations expire unused."),
                    L("subscription_id", "dim_subscription", "n1", coverage=0.93),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("balance_type_id", "dim_balance_type", "n1!"),
                ],
                [M("debited_units", "Units debited.")],
            ),
            _fact(
                "usage",
                "fact_attach",
                "Attach Event",
                "One registration or attach of a subscriber to the network.",
                2_400_000_000,
                [
                    L("subscriber_id", "dim_subscriber", "n1", coverage=0.98),
                    L("cell_id", "dim_cell", "n1", coverage=0.99),
                    L("technology_id", "dim_technology", "n1!"),
                    L("plmn_id", "dim_plmn", "n1", coverage=0.15),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("network_element_id", "dim_network_element", "n1"),
                    L("imsi_id", "dim_imsi", "n1", coverage=0.95),
                    L("msisdn_id", "dim_msisdn", "n1", coverage=0.95),
                ],
                [M("attach_result", "Result of the attach.", "success, reject, timeout")],
            ),
            _fact(
                "charging",
                "fact_rated_charge",
                "Rated Charge",
                "One rated usage charge produced from a mediated CDR.",
                2_100_000_000,
                [
                    L("data_cdr_id", "fact_data_cdr", "11?", "Data CDRs are one slice of rated usage.", matched_rows=1_400_000_000),
                    L("voice_cdr_id", "fact_voice_cdr", "11?", "Voice CDRs are one slice of rated usage.", matched_rows=520_000_000),
                    L("sms_cdr_id", "fact_sms_cdr", "11?", "SMS CDRs are one slice of rated usage.", matched_rows=150_000_000),
                    L("content_cdr_id", "fact_content_cdr", "11?", "Content CDRs are one slice of rated usage.", matched_rows=30_000_000),
                    L("subscription_id", "dim_subscription", "n1", coverage=0.96),
                    L("rate_plan_id", "dim_rate_plan", "n1!"),
                    L("charge_type_id", "dim_charge_type", "n1!"),
                    L("tariff_id", "dim_tariff", "n1?", "Recurring charges are not usage-tariffed.", match_rate=0.97),
                    L("currency_id", "dim_currency", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("gl_account_id", "dim_gl_account", "n1"),
                    L("tax_code_id", "dim_tax_code", "n1?", match_rate=0.9),
                ],
                [M("charge_amount", "Rated amount before tax.")],
            ),
            _fact(
                "charging",
                "fact_policy_event",
                "Policy Event",
                "One policy-control decision for a session.",
                1_800_000_000,
                [
                    L("subscription_id", "dim_subscription", "n1", coverage=0.9),
                    L("policy_rule_id", "dim_policy_rule", "n1!"),
                    L("qos_id", "dim_qos", "n1"),
                    L("slice_id", "dim_slice", "n1?", match_rate=0.4),
                    L("cell_id", "dim_cell", "n1?", match_rate=0.8, coverage=0.9),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("network_element_id", "dim_network_element", "n1"),
                ],
                [M("decision", "Policy decision.", "allow, restrict, redirect, terminate")],
            ),
            _fact(
                "usage",
                "fact_handover",
                "Handover",
                "One mobility handover between cells.",
                960_000_000,
                [
                    L("subscriber_id", "dim_subscriber", "n1", coverage=0.8),
                    L("source_cell_id", "dim_cell", "n1", "Cell the session left.", coverage=0.95),
                    L("handover_type_id", "dim_handover_type", "n1!"),
                    L("technology_id", "dim_technology", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("network_element_id", "dim_network_element", "n1"),
                ],
                [M("success_flag", "Whether the handover completed.", "success, failure")],
            ),
            _fact(
                "usage",
                "fact_handover_target",
                "Handover Target",
                "Target cell of one handover. Kept as its own dataset so source and target do not share one join to the cell population.",
                960_000_000,
                [
                    L("handover_id", "fact_handover", "11!", "Each handover has one target-cell row, and each target row has one handover."),
                    L("target_cell_id", "dim_cell", "n1", "Cell the session entered.", coverage=0.95),
                ],
                [M("target_technology", "Technology of the target cell.", "2G, 3G, 4G, 5G")],
            ),
            _fact(
                "charging",
                "fact_allowance_draw",
                "Allowance Draw",
                "One draw against an included allowance.",
                900_000_000,
                [
                    L("subscription_id", "dim_subscription", "n1", coverage=0.7),
                    L("allowance_bucket_id", "dim_allowance_bucket", "n1!"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("rated_charge_id", "fact_rated_charge", "n1?", "A snapshot draw may not cite one charge.", match_rate=0.8),
                ],
                [M("drawn_units", "Units drawn from the allowance.")],
            ),
            _fact(
                "usage",
                "fact_location_update",
                "Location Update",
                "One location-update or tracking-area update.",
                600_000_000,
                [
                    L("subscriber_id", "dim_subscriber", "n1", coverage=0.85),
                    L("location_area_id", "dim_location_area", "n1!"),
                    L("cell_id", "dim_cell", "n1?", match_rate=0.7, coverage=0.8),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("technology_id", "dim_technology", "n1"),
                ],
                [M("update_result", "Result of the update.", "success, reject")],
            ),
            _fact(
                "usage",
                "fact_qos_change",
                "QoS Change",
                "One mid-session QoS change.",
                300_000_000,
                [
                    L("subscription_id", "dim_subscription", "n1", coverage=0.5),
                    L("qos_id", "dim_qos", "n1!"),
                    L("cell_id", "dim_cell", "n1", coverage=0.8),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("policy_rule_id", "dim_policy_rule", "n1?", match_rate=0.6),
                ],
                [M("bitrate_kbps", "Granted bitrate after the change.")],
            ),
            _fact(
                "network",
                "fact_cell_counter",
                "Cell Counter",
                "One 15-minute counter snapshot for one cell.",
                244_800_000,
                [
                    L("cell_id", "dim_cell", "n1!", "Every cell has a counter in every interval of the window."),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("technology_id", "dim_technology", "n1"),
                    L("cell_site_id", "dim_cell_site", "n1!"),
                ],
                [M("quarter_index", "Interval index 0 through 95 inside the day."), M("prb_utilization", "Average PRB utilization in the interval."), M("active_users", "Average active users in the interval.")],
                volume_class="periodic_snapshot",
            ),
            _fact(
                "roaming",
                "fact_tap_out",
                "TAP Out Record",
                "One outcollect roaming record sent to a partner.",
                126_000_000,
                [
                    L("roaming_partner_id", "dim_roaming_partner", "n1!", "Every roaming partner receives outcollect records."),
                    L("plmn_id", "dim_plmn", "n1"),
                    L("subscription_id", "dim_subscription", "n1", coverage=0.2),
                    L("record_type_id", "dim_record_type", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("currency_id", "dim_currency", "n1"),
                    L("voice_cdr_id", "fact_voice_cdr", "11?", "Voice outcollect is one slice of TAP-out.", matched_rows=36_000_000),
                    L("data_cdr_id", "fact_data_cdr", "11?", "Data outcollect is one slice of TAP-out.", matched_rows=90_000_000),
                ],
                [M("charge_amount", "Outcollect charge in the tap currency.")],
            ),
            _fact(
                "roaming",
                "fact_tap_in",
                "TAP In Record",
                "One incollect roaming record received from a partner.",
                40_000_000,
                [
                    L("roaming_partner_id", "dim_roaming_partner", "n1!", "Every partner sends incollect records."),
                    L("plmn_id", "dim_plmn", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1!"),
                    L("currency_id", "dim_currency", "n1"),
                    L("record_type_id", "dim_record_type", "n1"),
                ],
                [M("charge_amount", "Incollect charge.")],
            ),
            _fact(
                "billing",
                "fact_invoice",
                "Invoice",
                "One invoice for one billing account in the window.",
                16_000_000,
                [
                    L("billing_account_id", "dim_billing_account", "11!", "The window closes exactly one invoice per billing account."),
                    L("currency_id", "dim_currency", "n1"),
                    L("bill_cycle_id", "dim_bill_cycle", "n1!"),
                    L("calendar_day_id", "dim_calendar_day", "n1"),
                    L("market_id", "dim_market", "n1!"),
                    L("legal_entity_id", "dim_legal_entity", "n1"),
                ],
                [M("invoice_amount", "Total invoice amount."), M("invoice_status", "Status of the invoice.", "issued, settled, adjusted, void")],
            ),
            _fact(
                "billing",
                "fact_invoice_line",
                "Invoice Line",
                "One charge line on an invoice.",
                128_000_000,
                [
                    L("invoice_id", "fact_invoice", "n1!", "Every invoice has charge lines."),
                    L("charge_type_id", "dim_charge_type", "n1!"),
                    L("tax_code_id", "dim_tax_code", "n1?", match_rate=0.75),
                    L("currency_id", "dim_currency", "n1"),
                    L("rated_charge_id", "fact_rated_charge", "n1?", "Recurring fees are not tied to one rated CDR.", match_rate=0.7),
                    L("gl_account_id", "dim_gl_account", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1"),
                ],
                [M("line_amount", "Amount of the invoice line.")],
            ),
            _fact(
                "billing",
                "fact_tax_line",
                "Tax Line",
                "One tax amount on an invoice.",
                32_000_000,
                [
                    L("invoice_id", "fact_invoice", "n1!", "Every invoice has at least one tax line."),
                    L("tax_code_id", "dim_tax_code", "n1!"),
                    L("tax_jurisdiction_id", "dim_tax_jurisdiction", "n1"),
                    L("currency_id", "dim_currency", "n1"),
                ],
                [M("tax_amount", "Tax amount.")],
            ),
            _fact(
                "billing",
                "fact_document",
                "Bill Document",
                "One rendered document for an invoice.",
                16_000_000,
                [
                    L("invoice_id", "fact_invoice", "11!", "Each invoice has one rendered bill document."),
                    L("document_type_id", "dim_document_type", "n1"),
                    L("calendar_day_id", "dim_calendar_day", "n1"),
                ],
                [M("document_uri", "Location of the rendered document.")],
            ),
            _fact("billing", "fact_payment", "Payment", "One payment posted to a billing account.", 14_500_000, [L("billing_account_id", "dim_billing_account", "n1", coverage=0.7), L("payment_method_id", "dim_payment_method", "n1!"), L("currency_id", "dim_currency", "n1"), L("calendar_day_id", "dim_calendar_day", "n1!"), L("bank_id", "dim_bank", "n1?", match_rate=0.8)], [M("payment_amount", "Amount of the payment.")]),
            _fact("billing", "fact_adjustment", "Adjustment", "One adjustment on a billing account.", 3_200_000, [L("billing_account_id", "dim_billing_account", "n1", coverage=0.15), L("adjustment_reason_id", "dim_adjustment_reason", "n1!"), L("currency_id", "dim_currency", "n1"), L("calendar_day_id", "dim_calendar_day", "n1"), L("employee_id", "dim_employee", "n1?", match_rate=0.5)], [M("adjustment_amount", "Signed adjustment amount.")]),
            _fact("billing", "fact_dunning_event", "Dunning Event", "One collections action on a billing account.", 1_800_000, [L("billing_account_id", "dim_billing_account", "n1", coverage=0.08), L("dunning_level_id", "dim_dunning_level", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("action_name", "Collections action taken.")]),
            _fact("billing", "fact_credit_note", "Credit Note", "One credit note against an invoice.", 400_000, [L("invoice_id", "fact_invoice", "n1?", match_rate=0.9), L("billing_account_id", "dim_billing_account", "n1"), L("currency_id", "dim_currency", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("credit_amount", "Amount credited.")]),
            _fact("billing", "fact_topup", "Top Up", "One prepaid top-up.", 6_000_000, [L("subscription_id", "dim_subscription", "n1", coverage=0.12), L("payment_method_id", "dim_payment_method", "n1"), L("currency_id", "dim_currency", "n1"), L("channel_id", "dim_channel", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1!"), L("dealer_id", "dim_dealer", "n1?", match_rate=0.4)], [M("topup_amount", "Amount of the top-up.")]),
            _fact("billing", "fact_refund", "Refund", "One refund of a payment.", 220_000, [L("payment_id", "fact_payment", "n1?", match_rate=0.95), L("billing_account_id", "dim_billing_account", "n1"), L("currency_id", "dim_currency", "n1"), L("calendar_day_id", "dim_calendar_day", "n1"), L("adjustment_reason_id", "dim_adjustment_reason", "n1")], [M("refund_amount", "Amount refunded.")]),
            _fact("mediation", "fact_mediation_reject", "Mediation Reject", "One CDR rejected by mediation.", 8_400_000, [L("mediation_rule_id", "dim_mediation_rule", "n1!"), L("record_type_id", "dim_record_type", "n1"), L("calendar_day_id", "dim_calendar_day", "n1!"), L("recording_entity_id", "dim_recording_entity", "n1"), L("data_cdr_id", "fact_data_cdr", "11?", "A reject may cite the data CDR it failed.", matched_rows=5_600_000), L("voice_cdr_id", "fact_voice_cdr", "11?", matched_rows=2_000_000), L("sms_cdr_id", "fact_sms_cdr", "11?", matched_rows=800_000)], [M("reject_reason", "Mediation reject reason.")]),
            _fact("mediation", "fact_duplicate_suspect", "Duplicate Suspect", "One CDR flagged as a possible duplicate.", 2_100_000, [L("record_type_id", "dim_record_type", "n1"), L("calendar_day_id", "dim_calendar_day", "n1"), L("subscription_id", "dim_subscription", "n1?", match_rate=0.9)], [M("duplicate_score", "Score that ranked the suspect.")]),
            _fact("charging", "fact_rerate", "Rerate Event", "One rerate of a rated charge.", 21_000_000, [L("rated_charge_id", "fact_rated_charge", "n1", "A rerate cites the charge it replaces.", coverage=0.01), L("calendar_day_id", "dim_calendar_day", "n1"), L("employee_id", "dim_employee", "n1?", match_rate=0.2)], [M("rerate_amount", "Replacement charge amount.")]),
            _fact("party", "fact_number_port", "Number Port", "One number-portability event.", 180_000, [L("msisdn_id", "dim_msisdn", "n1"), L("np_operator_id", "dim_np_operator", "n1!"), L("subscription_id", "dim_subscription", "n1?", match_rate=0.8), L("calendar_day_id", "dim_calendar_day", "n1")], [M("port_direction", "Direction of the port.", "in, out")]),
            _fact("party", "fact_sim_swap", "SIM Swap", "One SIM replacement on a subscriber.", 250_000, [L("subscriber_id", "dim_subscriber", "n1"), L("sim_id", "dim_sim", "n1"), L("employee_id", "dim_employee", "n1?", match_rate=0.7), L("calendar_day_id", "dim_calendar_day", "n1"), L("dealer_id", "dim_dealer", "n1?", match_rate=0.4)], [M("swap_reason", "Reason for the swap.", "lost, upgrade, fraud, defect")]),
            _fact("network", "fact_outage_ticket", "Outage Ticket", "One network outage ticket.", 4_000, [L("cell_site_id", "dim_cell_site", "n1?", match_rate=0.8), L("network_element_id", "dim_network_element", "n1?", match_rate=0.6), L("calendar_day_id", "dim_calendar_day", "n1"), L("trouble_code_id", "dim_trouble_code", "n1")], [M("impacted_cells", "Count of cells listed on the ticket.")]),
            _fact("network", "fact_network_alarm", "Network Alarm", "One alarm raised by a network element.", 1_800_000, [L("network_element_id", "dim_network_element", "n1", coverage=0.55), L("cell_id", "dim_cell", "n1?", match_rate=0.4, coverage=0.2), L("calendar_day_id", "dim_calendar_day", "n1!"), L("alarm_severity_id", "dim_alarm_severity", "n1!"), L("technology_id", "dim_technology", "n1")], [M("alarm_code", "Vendor alarm code.")]),
            _fact("network", "fact_counter_breach", "Counter Breach", "One threshold breach on a cell-counter snapshot.", 500_000, [L("cell_counter_id", "fact_cell_counter", "n1", coverage=0.002), L("calendar_day_id", "dim_calendar_day", "n1"), L("cell_id", "dim_cell", "n1", coverage=0.1)], [M("metric_name", "Counter that breached."), M("observed_value", "Observed counter value.")]),
            _fact("care", "fact_interaction", "Care Interaction", "One care contact with a party.", 9_500_000, [L("party_id", "dim_party", "n1", coverage=0.3), L("subscriber_id", "dim_subscriber", "n1?", match_rate=0.8), L("agent_id", "dim_agent", "n1!", "Every care agent handles interactions."), L("queue_id", "dim_queue", "n1!"), L("channel_id", "dim_channel", "n1"), L("calendar_day_id", "dim_calendar_day", "n1!"), L("care_reason_id", "dim_care_reason", "n1!")], [M("handle_seconds", "Handle time of the interaction.")]),
            _fact("care", "fact_trouble_ticket", "Trouble Ticket", "One customer trouble ticket.", 1_200_000, [L("subscriber_id", "dim_subscriber", "n1", coverage=0.05), L("trouble_code_id", "dim_trouble_code", "n1!"), L("channel_id", "dim_channel", "n1"), L("calendar_day_id", "dim_calendar_day", "n1!"), L("market_id", "dim_market", "n1"), L("agent_id", "dim_agent", "n1?", match_rate=0.9)], [M("ticket_status", "Status of the ticket.", "open, pending, resolved, closed")]),
            _fact("care", "fact_ticket_event", "Ticket Event", "One status or work event on a trouble ticket.", 4_800_000, [L("trouble_ticket_id", "fact_trouble_ticket", "n1!", "Every ticket has events."), L("agent_id", "dim_agent", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("event_type", "Kind of ticket event.", "create, assign, note, resolve, reopen")]),
            _fact("care", "fact_dealer_sale", "Dealer Sale", "One sale recorded by a dealer.", 420_000, [L("dealer_id", "dim_dealer", "n1!", "Every dealer records a sale in the window."), L("subscription_id", "dim_subscription", "n1"), L("rate_plan_id", "dim_rate_plan", "n1"), L("calendar_day_id", "dim_calendar_day", "n1"), L("employee_id", "dim_employee", "n1?", match_rate=0.3), L("sale_type_id", "dim_sale_type", "n1!")], [M("sale_amount", "Amount of the sale.")]),
            _fact("roaming", "fact_interconnect_invoice", "Interconnect Invoice", "One interconnect invoice from a carrier.", 80, [L("carrier_id", "dim_carrier", "11!", "Each interconnect carrier has one invoice in the window."), L("currency_id", "dim_currency", "n1"), L("accounting_period_id", "dim_accounting_period", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("invoice_amount", "Interconnect invoice amount.")]),
            _fact("roaming", "fact_settlement_line", "Settlement Line", "One roaming settlement line with a partner.", 2_400_000, [L("roaming_partner_id", "dim_roaming_partner", "n1!", "Every partner has settlement lines."), L("currency_id", "dim_currency", "n1"), L("accounting_period_id", "dim_accounting_period", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1"), L("record_type_id", "dim_record_type", "n1"), L("plmn_id", "dim_plmn", "n1")], [M("settlement_amount", "Settlement amount.")]),
            _fact("finance", "fact_journal_line", "Journal Line", "One subledger journal line.", 6_000_000, [L("gl_account_id", "dim_gl_account", "n1!", "Every ledger account used by the operator is posted."), L("accounting_period_id", "dim_accounting_period", "n1!"), L("currency_id", "dim_currency", "n1"), L("legal_entity_id", "dim_legal_entity", "n1"), L("cost_center_id", "dim_cost_center", "n1?", match_rate=0.8), L("calendar_day_id", "dim_calendar_day", "n1!"), L("journal_source_id", "dim_journal_source", "n1!"), L("cost_element_id", "dim_cost_element", "n1?", match_rate=0.5)], [M("entered_amount", "Entered amount of the journal line.")]),
            _fact("care", "fact_fraud_alert", "Fraud Alert", "One fraud alert on a subscriber.", 350_000, [L("fraud_rule_id", "dim_fraud_rule", "n1!"), L("subscriber_id", "dim_subscriber", "n1", coverage=0.015), L("calendar_day_id", "dim_calendar_day", "n1"), L("msisdn_id", "dim_msisdn", "n1?", match_rate=0.9)], [M("alert_score", "Score of the fraud alert.")]),
            _fact("care", "fact_barring_event", "Barring Event", "One barring change on a subscriber.", 80_000, [L("subscriber_id", "dim_subscriber", "n1"), L("barring_id", "dim_barring", "n1!"), L("calendar_day_id", "dim_calendar_day", "n1"), L("employee_id", "dim_employee", "n1?", match_rate=0.6)], [M("barring_action", "Action applied.", "apply, remove")]),
            _fact("billing", "fact_bundle_snapshot", "Bundle Snapshot", "Month-end allowance position of one subscription.", 25_000_000, [L("subscription_id", "dim_subscription", "11!", "Each subscription has one month-end bundle snapshot."), L("rate_plan_id", "dim_rate_plan", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("remaining_data_mb", "Remaining included data at snapshot.")], volume_class="periodic_snapshot"),
            _fact("party", "fact_subscriber_snapshot", "Subscriber Snapshot", "Month-end status of one subscriber.", 20_000_000, [L("subscriber_id", "dim_subscriber", "11!", "Each subscriber has one month-end snapshot."), L("segment_id", "dim_segment", "n1"), L("credit_class_id", "dim_credit_class", "n1"), L("market_id", "dim_market", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("status_code", "Snapshot status.", "active, barred, suspended, closed")], volume_class="periodic_snapshot"),
            _fact("care", "fact_sla_breach", "SLA Breach", "One breach of a care or network SLA.", 15_000, [L("sla_id", "dim_sla", "n1!"), L("trouble_ticket_id", "fact_trouble_ticket", "n1?", match_rate=0.7), L("calendar_day_id", "dim_calendar_day", "n1")], [M("breach_minutes", "Minutes past the SLA.")]),
            _fact("care", "fact_campaign_contact", "Campaign Contact", "One outbound campaign contact.", 4_000_000, [L("campaign_id", "dim_campaign", "n1!"), L("party_id", "dim_party", "n1", coverage=0.15), L("channel_id", "dim_channel", "n1"), L("calendar_day_id", "dim_calendar_day", "n1!"), L("script_id", "dim_script", "n1")], [M("contact_result", "Result of the contact.", "answered, no-answer, converted, refused")]),
            _fact("billing", "fact_promise_to_pay", "Promise To Pay", "One promise-to-pay on a billing account.", 260_000, [L("billing_account_id", "dim_billing_account", "n1"), L("agent_id", "dim_agent", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("promised_amount", "Amount the account promised to pay.")]),
            _fact("billing", "fact_collection_referral", "Collection Referral", "One referral of an account to a collection agency.", 40_000, [L("collection_agency_id", "dim_collection_agency", "n1!"), L("billing_account_id", "dim_billing_account", "n1"), L("calendar_day_id", "dim_calendar_day", "n1")], [M("referred_amount", "Amount referred.")]),
            _bridge("bridge_subscription_addon", "Subscription Add On", "One add-on attached to a subscription.", 18_000_000, [L("subscription_id", "dim_subscription", "n1", coverage=0.5), L("addon_id", "dim_addon", "n1!")]),
            _bridge("bridge_account_contact", "Account Contact", "One contact designated for a billing account.", 16_000_000, [L("billing_account_id", "dim_billing_account", "11!", "Each billing account has one primary contact row."), L("contact_id", "dim_contact", "n1")]),
            _bridge("bridge_cell_neighbor", "Cell Neighbor", "One neighbor relation from a source cell.", 340_000, [L("cell_id", "dim_cell", "n1", "Source cell of the neighbor relation.", coverage=1.0)]),
            _bridge("bridge_neighbor_target", "Neighbor Target", "Neighbor cell of one neighbor relation.", 340_000, [L("cell_neighbor_id", "bridge_cell_neighbor", "11!", "Each neighbor relation has one target cell row."), L("neighbor_cell_id", "dim_cell", "n1", "Neighbor cell.", coverage=1.0)]),
            _bridge("bridge_plan_rating_group", "Plan Rating Group", "Rating groups valid on a rate plan.", 2_000, [L("rate_plan_id", "dim_rate_plan", "n1!"), L("rating_group_id", "dim_rating_group", "n1!")]),
            _bridge("bridge_offering_price", "Offering Price", "Price assigned to a product offering.", 2_400, [L("product_offering_id", "dim_product_offering", "n1!"), L("price_id", "dim_price", "11!")]),
            _bridge("bridge_tariff_zone", "Tariff Zone", "Destination zone priced by a tariff.", 4_000, [L("tariff_id", "dim_tariff", "n1!"), L("destination_zone_id", "dim_destination_zone", "n1!")]),
            _bridge("bridge_employee_queue", "Employee Queue", "Care queue an employee can serve.", 8_000, [L("employee_id", "dim_employee", "n1"), L("queue_id", "dim_queue", "n1!")]),
            _bridge("bridge_partner_plmn", "Partner PLMN", "PLMN operated by a roaming partner.", 900, [L("roaming_partner_id", "dim_roaming_partner", "n1!"), L("plmn_id", "dim_plmn", "n1")]),
            _bridge("bridge_device_capability", "Device Capability", "Technology a device model supports.", 8_000, [L("device_model_id", "dim_device_model", "n1!"), L("technology_id", "dim_technology", "n1!")]),
            _bridge("bridge_subscriber_party", "Subscriber Party", "Party that owns a subscriber.", 20_000_000, [L("subscriber_id", "dim_subscriber", "11!", "Each subscriber has one owning-party row."), L("party_id", "dim_party", "n1")]),
            _bridge("bridge_trunk_prefix", "Trunk Prefix", "Number prefix routed over a trunk.", 6_000, [L("interconnect_trunk_id", "dim_interconnect_trunk", "n1!"), L("number_prefix_id", "dim_number_prefix", "n1")]),
            _bridge("bridge_agent_skill", "Agent Skill", "Trouble code a care agent can handle.", 7_000, [L("agent_id", "dim_agent", "n1"), L("trouble_code_id", "dim_trouble_code", "n1")]),
            _bridge("bridge_market_channel", "Market Channel", "Channel enabled in a market.", 48, [L("market_id", "dim_market", "n1!"), L("channel_id", "dim_channel", "n1!")]),
            _bridge("bridge_dealer_plan", "Dealer Plan", "Rate plan a dealer is allowed to sell.", 3_600, [L("dealer_id", "dim_dealer", "n1!"), L("rate_plan_id", "dim_rate_plan", "n1")]),
            _bridge("bridge_cell_spectrum", "Cell Spectrum", "Spectrum band configured on a cell.", 200_000, [L("cell_id", "dim_cell", "n1!"), L("spectrum_band_id", "dim_cell_band", "n1!")]),
            _bridge("bridge_policy_apn", "Policy APN", "APN a policy rule can govern.", 400, [L("policy_rule_id", "dim_policy_rule", "n1!"), L("apn_id", "dim_apn", "n1")]),
            _bridge("bridge_roaming_zone", "Roaming Zone", "Destination zone agreed with a roaming partner.", 1_200, [L("roaming_partner_id", "dim_roaming_partner", "n1!"), L("destination_zone_id", "dim_destination_zone", "n1")]),
            _bridge("bridge_content_rating", "Content Rating", "Rating group used for a content provider.", 700, [L("content_provider_id", "dim_content_provider", "n1!"), L("rating_group_id", "dim_rating_group", "n1")]),
            _bridge("bridge_prefix_zone", "Prefix Zone", "Destination zone of a number prefix.", 5_000, [L("number_prefix_id", "dim_number_prefix", "11!"), L("destination_zone_id", "dim_destination_zone", "n1!")]),
            _bridge("bridge_party_address", "Party Address", "Address linked to a party.", 18_000_000, [L("party_id", "dim_party", "n1", coverage=0.8), L("address_id", "dim_address", "11!", "Each address is linked once.")]),
            _bridge("bridge_workgroup_employee", "Workgroup Employee", "Membership of an employee in a workgroup.", 42_000, [L("employee_id", "dim_employee", "11!"), L("workgroup_id", "dim_workgroup", "n1!")]),
            _bridge("bridge_campaign_plan", "Campaign Plan", "Rate plan promoted by a campaign.", 180, [L("campaign_id", "dim_campaign", "n1!"), L("rate_plan_id", "dim_rate_plan", "n1")]),
            _bridge("bridge_slice_qos", "Slice QoS", "QoS profile allowed on a slice.", 36, [L("slice_id", "dim_slice", "n1!"), L("qos_id", "dim_qos", "n1")]),
        ]
    )
    return build_datasets(tables)


DATASETS = _datasets()

DOMAIN = {
    "key": "telecom-mobile",
    "business_name": "Northline Mobile",
    "database": "TELECOM_MOBILE",
    "account": "northline.us-east-1",
    "root": "telecom-mobile",
    "narrative": _NARRATIVE.strip(),
    "provenance": _PROVENANCE.strip(),
    "statistics_window_days": 30,
    "identity_synonyms": {
        "subscriber_identity": ["mobile subscriber", "end user"],
        "cell_identity": ["sector", "cell"],
        "msisdn_identity": ["public number", "directory number"],
        "billing_account_identity": ["account"],
    },
    "readme_intro": """
Northline Mobile operates a national mobile network. The catalog `telecom-mobile` is the ontology of usage mediation, online charging, roaming interchange, and retail billing: datasets in the Snowflake database `TELECOM_MOBILE`.

A subscription belongs to a subscriber and a billing account. Packet, voice, message, and content usage land as separate CDR facts. Online charging events, reservations, and debits are finer than a closed CDR. TAP-out and TAP-in hold roaming interchange. Cell counters are one row per cell per 15-minute interval. The questions below use the authored identities and joins. Synthetic row counts and fan-out for a 30-day window are listed with the major fact tables.
""".strip(),
    "readme_questions": _QUESTIONS.strip(),
    "signatures": [
        {
            "child": "dim_market",
            "parent": "dim_region",
            "identity": "region_identity",
            "parent_multiplicity": "1:many",
            "parent_existence": "always",
            "child_multiplicity": "many:1",
            "child_existence": "always",
        },
        {
            "child": "dim_cell",
            "parent": "dim_cell_site",
            "identity": "cell_site_identity",
            "parent_multiplicity": "1:many",
            "parent_existence": "always",
            "child_multiplicity": "many:1",
            "child_existence": "always",
        },
        {
            "child": "dim_market",
            "parent": "dim_employee",
            "identity": "employee_identity",
            "parent_multiplicity": "1:1",
            "parent_existence": "optional",
            "child_multiplicity": "1:1",
            "child_existence": "always",
        },
        {
            "child": "fact_balance_reservation",
            "parent": "fact_charging_event",
            "identity": "charging_event_identity",
            "parent_multiplicity": "1:1",
            "parent_existence": "optional",
            "child_multiplicity": "1:1",
            "child_existence": "always",
        },
        {
            "child": "fact_invoice_line",
            "parent": "fact_invoice",
            "identity": "invoice_identity",
            "parent_multiplicity": "1:many",
            "parent_existence": "always",
            "child_multiplicity": "many:1",
            "child_existence": "always",
        },
    ],
    "major_facts": [
        {
            "dataset": "fact_charging_event",
            "landing": "Online charging events are the finest usage landing zone. 3GPP treats a charging event as one chargeable-event report toward the charging function, which is finer than a closed CDR.",
            "basis": "Authored at three events per mediated CDR. The mediated total is the published 2.1 billion CDRs per month, so the event fact is 6.3 billion rows.",
        },
        {
            "dataset": "fact_balance_reservation",
            "landing": "Quota reservations are the online-charging landing zone for held balance.",
            "basis": "Authored as two reservations for every three charging events. Some charging events do not reserve.",
        },
        {
            "dataset": "fact_balance_debit",
            "landing": "Balance debits are the landing zone for committed online-charging usage.",
            "basis": "Authored as three debits for every four reservations. Unused reservations expire without a debit.",
        },
        {
            "dataset": "fact_attach",
            "landing": "Network attach and registration events land here, separate from billable CDRs.",
            "basis": "Synthetic mobility volume for a 25 million subscription national network over 30 days.",
        },
        {
            "dataset": "fact_rated_charge",
            "landing": "Rating output lands here, one charge per mediated CDR, before invoice assembly.",
            "basis": "Equal to the 2.1 billion mediated CDRs. Optional one-to-one links partition that population across data, voice, SMS, and content CDRs.",
        },
        {
            "dataset": "fact_policy_event",
            "landing": "Policy-control decisions land here for session authorization and QoS.",
            "basis": "Synthetic session-control volume, below the charging-event grain and above closed CDRs.",
        },
        {
            "dataset": "fact_data_cdr",
            "landing": "Packet-data CDRs, including partial PGW and SMF records, are the largest mediated-CDR landing zone.",
            "basis": "1.4 billion of the published 2.1 billion monthly CDRs. Partial records are why data outnumbers voice.",
        },
        {
            "dataset": "fact_handover",
            "landing": "Mobility handovers land here, with separate source and target cell identities.",
            "basis": "Synthetic radio-mobility volume for the 85,000-cell footprint.",
        },
        {
            "dataset": "fact_allowance_draw",
            "landing": "Included-allowance consumption lands here, optionally tied to a rated charge.",
            "basis": "Synthetic draw volume for subscriptions that hold an allowance bucket.",
        },
        {
            "dataset": "fact_location_update",
            "landing": "Location and tracking-area updates land here.",
            "basis": "Synthetic mobility signaling volume, lower than handover volume.",
        },
        {
            "dataset": "fact_voice_cdr",
            "landing": "Voice call detail records land here.",
            "basis": "520 million of the published 2.1 billion monthly CDRs.",
        },
        {
            "dataset": "fact_qos_change",
            "landing": "Mid-session QoS changes land here.",
            "basis": "Synthetic bearer-modification volume.",
        },
        {
            "dataset": "fact_cell_counter",
            "landing": "Radio performance counters land here at 15-minute grain.",
            "basis": "85,000 cells times 96 intervals times 30 days = 244,800,000 rows. This is a periodic snapshot, not a CDR.",
        },
        {
            "dataset": "fact_sms_cdr",
            "landing": "Short-message CDRs land here.",
            "basis": "150 million of the published 2.1 billion monthly CDRs.",
        },
        {
            "dataset": "fact_tap_out",
            "landing": "Outbound roaming usage exchanged with partners lands here.",
            "basis": "Authored as 6 percent of mediated CDRs (126 million), the outcollect slice of the 2.1 billion.",
        },
        {
            "dataset": "fact_invoice_line",
            "landing": "Billable charge lines for the cycle land here, after rating.",
            "basis": "16 million invoices times an authored average of 8 lines.",
        },
    ],
    "datasets": DATASETS,
}
