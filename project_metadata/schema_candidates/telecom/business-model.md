# Northline Mobile

Northline Mobile is a national mobile network operator. The catalog is the warehouse-style ontology of its usage, online charging, mediation, roaming, and retail billing systems. Subscribers, subscriptions, cells, and rate plans are conformed dimensions. Call detail records, charging events, balance movements, and invoices are facts.

The usage landing zone follows 3GPP charging management. A charging data record is the formatted collection of one or more chargeable events that the network transfers to the billing domain. Voice, SMS, content, and packet-data records are separate facts because their measures differ. Packet-data volume is dominated by PGW and SMF records, including partial records for long sessions. An online charging event is finer than a closed CDR: reservations and debits are their own facts. Roaming usage that is exchanged with other operators lands on TAP-out and TAP-in facts. Cell counters are a 15-minute periodic snapshot, one row per cell per interval.

A billing account has one invoice in the statistics window. An invoice has many charge lines. A subscription has one service instance and one month-end bundle snapshot. Organization runs from the enterprise through legal entities, regions, and markets to cell sites and cells. The synthetic 30-day populations and the join fan-out derived from these rules are recorded beside the catalog, not inside the graph YAML.

## Data ecosystem

The authored catalog `telecom` contains 173 datasets (97 dimensions, 52 facts, 24 bridges) in the Snowflake database `TELECOM` on account `northline.us-east-1`.

Each dataset is one ontology node. The grain column is the system of record for that dataset's logical identity and is marked `is_entity_universe: true`. Foreign-key columns realize the same logical identity with `is_entity_universe: false`, because the child dataset does not hold the complete population. Edges join those two realizations. Multiplicity and match existence are directional and follow the operating rules below. Synthetic row counts and join fan-out for a 30-day window are in `statistics.md`. They are derived from authored populations and these multiplicity rules. The YAML nodes do not carry those statistics.

## Signature relationships

| Relationship | Identity | Parent to child | Child to parent | Rule |
| --- | --- | --- | --- | --- |
| `dim_region` to `dim_market` | `region_identity` | 1:many (always) | many:1 (always) | Many markets belong to one region, every market matches a region, and every region includes at least one market. Every region operates at least one market. |
| `dim_cell_site` to `dim_cell` | `cell_site_identity` | 1:many (always) | many:1 (always) | Many cells belong to one cell Site, every cell matches a cell Site, and every cell Site includes at least one cell. Every cell site has at least one cell. |
| `dim_employee` to `dim_market` | `employee_identity` | 1:1 (optional) | 1:1 (always) | Each market matches exactly one employee, each employee matches at most one market, and not every employee is matched. A market has one manager, and an employee manages at most one market. |
| `fact_charging_event` to `fact_balance_reservation` | `charging_event_identity` | 1:1 (optional) | 1:1 (always) | Each balance Reservation matches exactly one charging Event, each charging Event matches at most one balance Reservation, and not every charging Event is matched. A reservation matches one charging event, and some events do not reserve. |
| `fact_invoice` to `fact_invoice_line` | `invoice_identity` | 1:many (always) | many:1 (always) | Many invoice Lines belong to one invoice, every invoice Line matches a invoice, and every invoice includes at least one invoice Line. Every invoice has charge lines. |

## Relationship rules

| Child dataset | Column | Universe dataset | Mapping | Parent match | Child match | Rule |
| --- | --- | --- | --- | --- | --- | --- |
| `dim_legal_entity` | `enterprise_id` | `dim_enterprise` | 1:N | 1:many / always | many:1 / always | Many legal Entities belong to one enterprise, every legal Entity matches a enterprise, and every enterprise includes at least one legal Entity. Every operating company sits under the one enterprise. |
| `dim_region` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many regions belong to one legal Entity, every region matches a legal Entity, and a legal Entity may include no region. |
| `dim_department` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many departments belong to one legal Entity, every department matches a legal Entity, and a legal Entity may include no department. |
| `dim_cost_center` | `department_id` | `dim_department` | 1:N | 1:many / always | many:1 / always | Many cost Centers belong to one department, every cost Center matches a department, and every department includes at least one cost Center. Every department owns at least one cost center. |
| `dim_cost_center` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many cost Centers belong to one legal Entity, every cost Center matches a legal Entity, and a legal Entity may include no cost Center. |
| `dim_employee` | `department_id` | `dim_department` | 1:N | 1:many / optional | many:1 / always | Many employees belong to one department, every employee matches a department, and a department may include no employee. |
| `dim_employee` | `cost_center_id` | `dim_cost_center` | 1:N | 1:many / optional | many:1 / always | Many employees belong to one cost Center, every employee matches a cost Center, and a cost Center may include no employee. |
| `dim_employee` | `market_id` | `dim_market` | 1:N | 1:many / optional | many:1 / always | Many employees belong to one market, every employee matches a market, and a market may include no employee. |
| `dim_market` | `region_id` | `dim_region` | 1:N | 1:many / always | many:1 / always | Many markets belong to one region, every market matches a region, and every region includes at least one market. Every region operates at least one market. |
| `dim_market` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many markets belong to one legal Entity, every market matches a legal Entity, and a legal Entity may include no market. |
| `dim_market` | `market_manager_employee_id` | `dim_employee` | 1:1 | 1:1 / optional | 1:1 / always | Each market matches exactly one employee, each employee matches at most one market, and not every employee is matched. A market has one manager, and an employee manages at most one market. |
| `dim_dealer` | `market_id` | `dim_market` | 1:N | 1:many / optional | many:1 / always | Many dealers belong to one market, every dealer matches a market, and a market may include no dealer. |
| `dim_dealer` | `channel_id` | `dim_channel` | 1:N | 1:many / optional | many:1 / always | Many dealers belong to one channel, every dealer matches a channel, and a channel may include no dealer. |
| `dim_workgroup` | `department_id` | `dim_department` | 1:N | 1:many / always | many:1 / always | Many workgroups belong to one department, every workgroup matches a department, and every department includes at least one workgroup. |
| `dim_gl_account` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many gL Accounts belong to one legal Entity, every gL Account matches a legal Entity, and a legal Entity may include no gL Account. |
| `dim_accounting_period` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many accounting Periods belong to one legal Entity, every accounting Period matches a legal Entity, and a legal Entity may include no accounting Period. |
| `dim_tax_jurisdiction` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Many tax Jurisdictions belong to one country, every tax Jurisdiction matches a country, and a country may include no tax Jurisdiction. |
| `dim_bank` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Many banks belong to one country, every bank matches a country, and a country may include no bank. |
| `dim_address` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Many addresses belong to one country, every address matches a country, and a country may include no address. |
| `dim_party` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Many parties belong to one country, every party matches a country, and a country may include no party. |
| `dim_party` | `address_id` | `dim_address` | 1:N | 1:many / optional | many:1 / optional | A party may match one address, and a address may include no party. A party may still be unidentified to a service address. |
| `dim_billing_account` | `party_id` | `dim_party` | 1:N | 1:many / optional | many:1 / always | Many billing Accounts belong to one party, every billing Account matches a party, and a party may include no billing Account. |
| `dim_billing_account` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many billing Accounts belong to one currency, every billing Account matches a currency, and a currency may include no billing Account. |
| `dim_billing_account` | `bill_cycle_id` | `dim_bill_cycle` | 1:N | 1:many / always | many:1 / always | Many billing Accounts belong to one bill Cycle, every billing Account matches a bill Cycle, and every bill Cycle includes at least one billing Account. Every bill cycle has accounts. |
| `dim_billing_account` | `market_id` | `dim_market` | 1:N | 1:many / always | many:1 / always | Many billing Accounts belong to one market, every billing Account matches a market, and every market includes at least one billing Account. Every market has billing accounts. |
| `dim_billing_account` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many billing Accounts belong to one legal Entity, every billing Account matches a legal Entity, and a legal Entity may include no billing Account. |
| `dim_billing_account` | `segment_id` | `dim_segment` | 1:N | 1:many / always | many:1 / always | Many billing Accounts belong to one customer Segment, every billing Account matches a customer Segment, and every customer Segment includes at least one billing Account. Every segment is in use. |
| `dim_billing_account` | `credit_class_id` | `dim_credit_class` | 1:N | 1:many / always | many:1 / always | Many billing Accounts belong to one credit Class, every billing Account matches a credit Class, and every credit Class includes at least one billing Account. |
| `dim_subscriber` | `billing_account_id` | `dim_billing_account` | 1:N | 1:many / always | many:1 / always | Many subscribers belong to one billing Account, every subscriber matches a billing Account, and every billing Account includes at least one subscriber. Every billing account has at least one subscriber. |
| `dim_subscriber` | `party_id` | `dim_party` | 1:N | 1:many / optional | many:1 / always | Many subscribers belong to one party, every subscriber matches a party, and a party may include no subscriber. |
| `dim_msisdn` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Many public Numbers belong to one country, every public Number matches a country, and a country may include no public Number. |
| `dim_subscription` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / always | many:1 / always | Many subscriptions belong to one subscriber, every subscription matches a subscriber, and every subscriber includes at least one subscription. Every subscriber has at least one subscription. |
| `dim_subscription` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / always | many:1 / always | Many subscriptions belong to one rate Plan, every subscription matches a rate Plan, and every rate Plan includes at least one subscription. Every rate plan has subscriptions. |
| `dim_subscription` | `market_id` | `dim_market` | 1:N | 1:many / optional | many:1 / always | Many subscriptions belong to one market, every subscription matches a market, and a market may include no subscription. |
| `dim_subscription` | `msisdn_id` | `dim_msisdn` | 1:1 | 1:1 / optional | 1:1 / always | Each subscription matches exactly one public Number, each public Number matches at most one subscription, and not every public Number is matched. Each subscription has one public number, and some numbers are spare. |
| `dim_plmn` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Many pLMNs belong to one country, every pLMN matches a country, and a country may include no pLMN. |
| `dim_imsi` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many iMSIs belong to one pLMN, every iMSI matches a pLMN, and a pLMN may include no iMSI. |
| `dim_sim` | `imsi_id` | `dim_imsi` | 1:1 | 1:1 / optional | 1:1 / always | Each sIM matches exactly one iMSI, each iMSI matches at most one sIM, and not every iMSI is matched. Each SIM carries one IMSI, and some IMSIs are unassigned. |
| `dim_sim` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / optional | A sIM may match one subscription, and a subscription may include no sIM. A SIM in stock is not on a subscription. |
| `dim_device_model` | `vendor_id` | `dim_vendor` | 1:N | 1:many / always | many:1 / always | Many device Models belong to one vendor, every device Model matches a vendor, and every vendor includes at least one device Model. Every vendor has at least one model. |
| `dim_device` | `device_model_id` | `dim_device_model` | 1:N | 1:many / always | many:1 / always | Many devices belong to one device Model, every device matches a device Model, and every device Model includes at least one device. Every model has devices. |
| `dim_device` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / optional | A device may match one subscriber, and a subscriber may include no device. A device in inventory has no subscriber. |
| `dim_contact` | `party_id` | `dim_party` | 1:N | 1:many / optional | many:1 / always | Many contacts belong to one party, every contact matches a party, and a party may include no contact. |
| `dim_product_spec` | `technology_id` | `dim_technology` | 1:N | 1:many / optional | many:1 / always | Many product Specs belong to one technology, every product Spec matches a technology, and a technology may include no product Spec. |
| `dim_product_offering` | `product_spec_id` | `dim_product_spec` | 1:N | 1:many / always | many:1 / always | Many product Offerings belong to one product Spec, every product Offering matches a product Spec, and every product Spec includes at least one product Offering. Every product spec is offered. |
| `dim_rate_plan` | `product_offering_id` | `dim_product_offering` | 1:N | 1:many / optional | many:1 / always | Many rate Plans belong to one product Offering, every rate Plan matches a product Offering, and a product Offering may include no rate Plan. |
| `dim_rate_plan` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many rate Plans belong to one currency, every rate Plan matches a currency, and a currency may include no rate Plan. |
| `dim_addon` | `product_offering_id` | `dim_product_offering` | 1:N | 1:many / optional | many:1 / always | Many add Ons belong to one product Offering, every add On matches a product Offering, and a product Offering may include no add On. |
| `dim_price` | `product_offering_id` | `dim_product_offering` | 1:N | 1:many / always | many:1 / always | Many prices belong to one product Offering, every price matches a product Offering, and every product Offering includes at least one price. Every offering has a price. |
| `dim_price` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many prices belong to one currency, every price matches a currency, and a currency may include no price. |
| `dim_discount` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / optional | many:1 / optional | A discount may match one rate Plan, and a rate Plan may include no discount. A discount may be account-specific rather than plan-wide. |
| `dim_tariff` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many tariffs belong to one currency, every tariff matches a currency, and a currency may include no tariff. |
| `dim_tariff` | `destination_zone_id` | `dim_destination_zone` | 1:N | 1:many / optional | many:1 / optional | A tariff may match one destination Zone, and a destination Zone may include no tariff. A tariff may be zone-independent. |
| `dim_tariff` | `charge_type_id` | `dim_charge_type` | 1:N | 1:many / always | many:1 / always | Many tariffs belong to one charge Type, every tariff matches a charge Type, and every charge Type includes at least one tariff. |
| `dim_tax_code` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / optional | A tax Code may match one gL Account, and a gL Account may include no tax Code. A memorandum tax code may have no ledger account. |
| `dim_roaming_partner` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many roaming Partners belong to one pLMN, every roaming Partner matches a pLMN, and a pLMN may include no roaming Partner. |
| `dim_roaming_partner` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Many roaming Partners belong to one country, every roaming Partner matches a country, and a country may include no roaming Partner. |
| `dim_tac` | `market_id` | `dim_market` | 1:N | 1:many / always | many:1 / always | Many tracking Areas belong to one market, every tracking Area matches a market, and every market includes at least one tracking Area. Every market has tracking areas. |
| `dim_location_area` | `market_id` | `dim_market` | 1:N | 1:many / always | many:1 / always | Many location Areas belong to one market, every location Area matches a market, and every market includes at least one location Area. |
| `dim_recording_entity` | `core_function_id` | `dim_core_function` | 1:N | 1:many / always | many:1 / always | Many recording Entities belong to one core Function, every recording Entity matches a core Function, and every core Function includes at least one recording Entity. |
| `dim_cell_site` | `market_id` | `dim_market` | 1:N | 1:many / always | many:1 / always | Many cell Sites belong to one market, every cell Site matches a market, and every market includes at least one cell Site. Every market has cell sites. |
| `dim_cell_site` | `region_id` | `dim_region` | 1:N | 1:many / optional | many:1 / always | Many cell Sites belong to one region, every cell Site matches a region, and a region may include no cell Site. |
| `dim_cell_site` | `address_id` | `dim_address` | 1:N | 1:many / optional | many:1 / always | Many cell Sites belong to one address, every cell Site matches a address, and a address may include no cell Site. |
| `dim_cell_site` | `site_type_id` | `dim_site_type` | 1:N | 1:many / always | many:1 / always | Many cell Sites belong to one site Type, every cell Site matches a site Type, and every site Type includes at least one cell Site. |
| `dim_cell` | `cell_site_id` | `dim_cell_site` | 1:N | 1:many / always | many:1 / always | Many cells belong to one cell Site, every cell matches a cell Site, and every cell Site includes at least one cell. Every cell site has at least one cell. |
| `dim_cell` | `technology_id` | `dim_technology` | 1:N | 1:many / always | many:1 / always | Many cells belong to one technology, every cell matches a technology, and every technology includes at least one cell. Every technology has cells. |
| `dim_cell` | `tac_id` | `dim_tac` | 1:N | 1:many / optional | many:1 / always | Many cells belong to one tracking Area, every cell matches a tracking Area, and a tracking Area may include no cell. |
| `dim_network_element` | `cell_site_id` | `dim_cell_site` | 1:N | 1:many / optional | many:1 / optional | A network Element may match one cell Site, and a cell Site may include no network Element. A core element is not tied to one site. |
| `dim_network_element` | `technology_id` | `dim_technology` | 1:N | 1:many / optional | many:1 / always | Many network Elements belong to one technology, every network Element matches a technology, and a technology may include no network Element. |
| `dim_network_element` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many network Elements belong to one pLMN, every network Element matches a pLMN, and a pLMN may include no network Element. |
| `dim_network_element` | `recording_entity_id` | `dim_recording_entity` | 1:N | 1:many / always | many:1 / always | Many network Elements belong to one recording Entity, every network Element matches a recording Entity, and every recording Entity includes at least one network Element. Every recording entity has elements. |
| `dim_network_element` | `vendor_id` | `dim_vendor` | 1:N | 1:many / always | many:1 / always | Many network Elements belong to one vendor, every network Element matches a vendor, and every vendor includes at least one network Element. |
| `dim_network_element` | `core_function_id` | `dim_core_function` | 1:N | 1:many / always | many:1 / always | Many network Elements belong to one core Function, every network Element matches a core Function, and every core Function includes at least one network Element. |
| `dim_slice` | `qos_id` | `dim_qos` | 1:N | 1:many / optional | many:1 / optional | A network Slice may match one qoS Profile, and a qoS Profile may include no network Slice. A slice may inherit QoS per session. |
| `dim_policy_rule` | `qos_id` | `dim_qos` | 1:N | 1:many / optional | many:1 / optional | A policy Rule may match one qoS Profile, and a qoS Profile may include no policy Rule. |
| `dim_policy_rule` | `slice_id` | `dim_slice` | 1:N | 1:many / optional | many:1 / optional | A policy Rule may match one network Slice, and a network Slice may include no policy Rule. |
| `dim_rating_group` | `charge_type_id` | `dim_charge_type` | 1:N | 1:many / always | many:1 / always | Many rating Groups belong to one charge Type, every rating Group matches a charge Type, and every charge Type includes at least one rating Group. |
| `dim_number_prefix` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Many number Prefixes belong to one country, every number Prefix matches a country, and a country may include no number Prefix. |
| `dim_number_prefix` | `destination_zone_id` | `dim_destination_zone` | 1:N | 1:many / optional | many:1 / optional | A number Prefix may match one destination Zone, and a destination Zone may include no number Prefix. |
| `dim_content_provider` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Many content Providers belong to one country, every content Provider matches a country, and a country may include no content Provider. |
| `dim_carrier` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Many interconnect Carriers belong to one country, every interconnect Carrier matches a country, and a country may include no interconnect Carrier. |
| `dim_interconnect_trunk` | `carrier_id` | `dim_carrier` | 1:N | 1:many / always | many:1 / always | Many interconnect Trunks belong to one interconnect Carrier, every interconnect Trunk matches a interconnect Carrier, and every interconnect Carrier includes at least one interconnect Trunk. Every carrier has a trunk. |
| `dim_interconnect_trunk` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many interconnect Trunks belong to one pLMN, every interconnect Trunk matches a pLMN, and a pLMN may include no interconnect Trunk. |
| `dim_agent` | `employee_id` | `dim_employee` | 1:1 | 1:1 / optional | 1:1 / always | Each care Agent matches exactly one employee, each employee matches at most one care Agent, and not every employee is matched. Each care agent is one employee, and most employees are not agents. |
| `dim_agent` | `department_id` | `dim_department` | 1:N | 1:many / optional | many:1 / always | Many care Agents belong to one department, every care Agent matches a department, and a department may include no care Agent. |
| `dim_queue` | `department_id` | `dim_department` | 1:N | 1:many / optional | many:1 / always | Many care Queues belong to one department, every care Queue matches a department, and a department may include no care Queue. |
| `dim_np_operator` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Many porting Operators belong to one country, every porting Operator matches a country, and a country may include no porting Operator. |
| `dim_service` | `subscription_id` | `dim_subscription` | 1:1 | 1:1 / always | 1:1 / always | Each service matches exactly one subscription, and each subscription matches exactly one service. Each subscription has one service instance, and each service instance has one subscription. |
| `dim_service` | `product_spec_id` | `dim_product_spec` | 1:N | 1:many / always | many:1 / always | Many services belong to one product Spec, every service matches a product Spec, and every product Spec includes at least one service. |
| `dim_resource` | `service_id` | `dim_service` | 1:N | 1:many / optional | many:1 / optional | A resource may match one service, and a service may include no resource. A spare resource is not on a service. |
| `dim_resource` | `sim_id` | `dim_sim` | 1:N | 1:many / optional | many:1 / optional | A resource may match one sIM, and a sIM may include no resource. |
| `dim_resource` | `device_id` | `dim_device` | 1:N | 1:many / optional | many:1 / optional | A resource may match one device, and a device may include no resource. |
| `dim_cost_element` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / always | Many cost Elements belong to one gL Account, every cost Element matches a gL Account, and a gL Account may include no cost Element. |
| `dim_campaign` | `channel_id` | `dim_channel` | 1:N | 1:many / always | many:1 / always | Many campaigns belong to one channel, every campaign matches a channel, and every channel includes at least one campaign. |
| `fact_data_cdr` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many data CDRs belong to one subscription, every data CDR matches a subscription, and a subscription may include no data CDR. Usage is rated on the subscription. |
| `fact_data_cdr` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / always | Many data CDRs belong to one subscriber, every data CDR matches a subscriber, and a subscriber may include no data CDR. |
| `fact_data_cdr` | `cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / always | Many data CDRs belong to one cell, every data CDR matches a cell, and a cell may include no data CDR. |
| `fact_data_cdr` | `cell_site_id` | `dim_cell_site` | 1:N | 1:many / optional | many:1 / always | Many data CDRs belong to one cell Site, every data CDR matches a cell Site, and a cell Site may include no data CDR. |
| `fact_data_cdr` | `technology_id` | `dim_technology` | 1:N | 1:many / always | many:1 / always | Many data CDRs belong to one technology, every data CDR matches a technology, and every technology includes at least one data CDR. |
| `fact_data_cdr` | `apn_id` | `dim_apn` | 1:N | 1:many / always | many:1 / always | Many data CDRs belong to one aPN DNN, every data CDR matches a aPN DNN, and every aPN DNN includes at least one data CDR. |
| `fact_data_cdr` | `qos_id` | `dim_qos` | 1:N | 1:many / optional | many:1 / always | Many data CDRs belong to one qoS Profile, every data CDR matches a qoS Profile, and a qoS Profile may include no data CDR. |
| `fact_data_cdr` | `rating_group_id` | `dim_rating_group` | 1:N | 1:many / optional | many:1 / always | Many data CDRs belong to one rating Group, every data CDR matches a rating Group, and a rating Group may include no data CDR. |
| `fact_data_cdr` | `record_type_id` | `dim_record_type` | 1:N | 1:many / always | many:1 / always | Many data CDRs belong to one record Type, every data CDR matches a record Type, and every record Type includes at least one data CDR. |
| `fact_data_cdr` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many data CDRs belong to one pLMN, every data CDR matches a pLMN, and a pLMN may include no data CDR. |
| `fact_data_cdr` | `roaming_partner_id` | `dim_roaming_partner` | 1:N | 1:many / optional | many:1 / optional | A data CDR may match one roaming Partner, and a roaming Partner may include no data CDR. Home data has no roaming partner. |
| `fact_data_cdr` | `network_element_id` | `dim_network_element` | 1:N | 1:many / optional | many:1 / always | Many data CDRs belong to one network Element, every data CDR matches a network Element, and a network Element may include no data CDR. |
| `fact_data_cdr` | `recording_entity_id` | `dim_recording_entity` | 1:N | 1:many / always | many:1 / always | Many data CDRs belong to one recording Entity, every data CDR matches a recording Entity, and every recording Entity includes at least one data CDR. |
| `fact_data_cdr` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many data CDRs belong to one calendar Day, every data CDR matches a calendar Day, and every calendar Day includes at least one data CDR. Every day in the window has data CDRs. |
| `fact_data_cdr` | `release_cause_id` | `dim_release_cause` | 1:N | 1:many / optional | many:1 / optional | A data CDR may match one release Cause, and a release Cause may include no data CDR. |
| `fact_data_cdr` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / optional | many:1 / always | Many data CDRs belong to one rate Plan, every data CDR matches a rate Plan, and a rate Plan may include no data CDR. |
| `fact_data_cdr` | `imsi_id` | `dim_imsi` | 1:N | 1:many / optional | many:1 / always | Many data CDRs belong to one iMSI, every data CDR matches a iMSI, and a iMSI may include no data CDR. |
| `fact_data_cdr` | `msisdn_id` | `dim_msisdn` | 1:N | 1:many / optional | many:1 / always | Many data CDRs belong to one public Number, every data CDR matches a public Number, and a public Number may include no data CDR. |
| `fact_data_cdr` | `slice_id` | `dim_slice` | 1:N | 1:many / optional | many:1 / optional | A data CDR may match one network Slice, and a network Slice may include no data CDR. 4G sessions have no slice. |
| `fact_data_cdr` | `mediation_file_id` | `fact_mediation_file` | 1:N | 1:many / always | many:1 / always | Many data CDRs belong to one mediation File, every data CDR matches a mediation File, and every mediation File includes at least one data CDR. Every mediation file in the window contains data CDRs. |
| `fact_voice_cdr` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many voice CDRs belong to one subscription, every voice CDR matches a subscription, and a subscription may include no voice CDR. |
| `fact_voice_cdr` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / always | Many voice CDRs belong to one subscriber, every voice CDR matches a subscriber, and a subscriber may include no voice CDR. |
| `fact_voice_cdr` | `cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / always | Many voice CDRs belong to one cell, every voice CDR matches a cell, and a cell may include no voice CDR. |
| `fact_voice_cdr` | `technology_id` | `dim_technology` | 1:N | 1:many / optional | many:1 / always | Many voice CDRs belong to one technology, every voice CDR matches a technology, and a technology may include no voice CDR. |
| `fact_voice_cdr` | `call_type_id` | `dim_call_type` | 1:N | 1:many / always | many:1 / always | Many voice CDRs belong to one call Type, every voice CDR matches a call Type, and every call Type includes at least one voice CDR. |
| `fact_voice_cdr` | `record_type_id` | `dim_record_type` | 1:N | 1:many / always | many:1 / always | Many voice CDRs belong to one record Type, every voice CDR matches a record Type, and every record Type includes at least one voice CDR. |
| `fact_voice_cdr` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many voice CDRs belong to one pLMN, every voice CDR matches a pLMN, and a pLMN may include no voice CDR. |
| `fact_voice_cdr` | `roaming_partner_id` | `dim_roaming_partner` | 1:N | 1:many / optional | many:1 / optional | A voice CDR may match one roaming Partner, and a roaming Partner may include no voice CDR. Home voice has no roaming partner. |
| `fact_voice_cdr` | `network_element_id` | `dim_network_element` | 1:N | 1:many / optional | many:1 / always | Many voice CDRs belong to one network Element, every voice CDR matches a network Element, and a network Element may include no voice CDR. |
| `fact_voice_cdr` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many voice CDRs belong to one calendar Day, every voice CDR matches a calendar Day, and every calendar Day includes at least one voice CDR. |
| `fact_voice_cdr` | `release_cause_id` | `dim_release_cause` | 1:N | 1:many / optional | many:1 / always | Many voice CDRs belong to one release Cause, every voice CDR matches a release Cause, and a release Cause may include no voice CDR. |
| `fact_voice_cdr` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / optional | many:1 / always | Many voice CDRs belong to one rate Plan, every voice CDR matches a rate Plan, and a rate Plan may include no voice CDR. |
| `fact_voice_cdr` | `msisdn_id` | `dim_msisdn` | 1:N | 1:many / optional | many:1 / always | Many voice CDRs belong to one public Number, every voice CDR matches a public Number, and a public Number may include no voice CDR. |
| `fact_voice_cdr` | `destination_zone_id` | `dim_destination_zone` | 1:N | 1:many / optional | many:1 / always | Many voice CDRs belong to one destination Zone, every voice CDR matches a destination Zone, and a destination Zone may include no voice CDR. |
| `fact_voice_cdr` | `number_prefix_id` | `dim_number_prefix` | 1:N | 1:many / optional | many:1 / optional | A voice CDR may match one number Prefix, and a number Prefix may include no voice CDR. |
| `fact_voice_cdr` | `time_band_id` | `dim_time_band` | 1:N | 1:many / always | many:1 / always | Many voice CDRs belong to one time Band, every voice CDR matches a time Band, and every time Band includes at least one voice CDR. |
| `fact_sms_cdr` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many sMS CDRs belong to one subscription, every sMS CDR matches a subscription, and a subscription may include no sMS CDR. |
| `fact_sms_cdr` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / always | Many sMS CDRs belong to one subscriber, every sMS CDR matches a subscriber, and a subscriber may include no sMS CDR. |
| `fact_sms_cdr` | `call_type_id` | `dim_call_type` | 1:N | 1:many / optional | many:1 / always | Many sMS CDRs belong to one call Type, every sMS CDR matches a call Type, and a call Type may include no sMS CDR. |
| `fact_sms_cdr` | `record_type_id` | `dim_record_type` | 1:N | 1:many / always | many:1 / always | Many sMS CDRs belong to one record Type, every sMS CDR matches a record Type, and every record Type includes at least one sMS CDR. |
| `fact_sms_cdr` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many sMS CDRs belong to one calendar Day, every sMS CDR matches a calendar Day, and every calendar Day includes at least one sMS CDR. |
| `fact_sms_cdr` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / optional | many:1 / always | Many sMS CDRs belong to one rate Plan, every sMS CDR matches a rate Plan, and a rate Plan may include no sMS CDR. |
| `fact_sms_cdr` | `msisdn_id` | `dim_msisdn` | 1:N | 1:many / optional | many:1 / always | Many sMS CDRs belong to one public Number, every sMS CDR matches a public Number, and a public Number may include no sMS CDR. |
| `fact_sms_cdr` | `destination_zone_id` | `dim_destination_zone` | 1:N | 1:many / optional | many:1 / always | Many sMS CDRs belong to one destination Zone, every sMS CDR matches a destination Zone, and a destination Zone may include no sMS CDR. |
| `fact_sms_cdr` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many sMS CDRs belong to one pLMN, every sMS CDR matches a pLMN, and a pLMN may include no sMS CDR. |
| `fact_content_cdr` | `content_provider_id` | `dim_content_provider` | 1:N | 1:many / always | many:1 / always | Many content CDRs belong to one content Provider, every content CDR matches a content Provider, and every content Provider includes at least one content CDR. Every content provider has events in the window. |
| `fact_content_cdr` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many content CDRs belong to one subscription, every content CDR matches a subscription, and a subscription may include no content CDR. |
| `fact_content_cdr` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many content CDRs belong to one calendar Day, every content CDR matches a calendar Day, and every calendar Day includes at least one content CDR. |
| `fact_content_cdr` | `charge_type_id` | `dim_charge_type` | 1:N | 1:many / optional | many:1 / always | Many content CDRs belong to one charge Type, every content CDR matches a charge Type, and a charge Type may include no content CDR. |
| `fact_content_cdr` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many content CDRs belong to one currency, every content CDR matches a currency, and a currency may include no content CDR. |
| `fact_mediation_file` | `network_element_id` | `dim_network_element` | 1:N | 1:many / always | many:1 / always | Many mediation Files belong to one network Element, every mediation File matches a network Element, and every network Element includes at least one mediation File. Every network element emits one file each day of the window. |
| `fact_mediation_file` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many mediation Files belong to one calendar Day, every mediation File matches a calendar Day, and every calendar Day includes at least one mediation File. Every day has mediation files. |
| `fact_mediation_file` | `file_format_id` | `dim_file_format` | 1:N | 1:many / always | many:1 / always | Many mediation Files belong to one file Format, every mediation File matches a file Format, and every file Format includes at least one mediation File. |
| `fact_mediation_file` | `recording_entity_id` | `dim_recording_entity` | 1:N | 1:many / always | many:1 / always | Many mediation Files belong to one recording Entity, every mediation File matches a recording Entity, and every recording Entity includes at least one mediation File. |
| `fact_charging_event` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many charging Events belong to one subscription, every charging Event matches a subscription, and a subscription may include no charging Event. |
| `fact_charging_event` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / always | Many charging Events belong to one subscriber, every charging Event matches a subscriber, and a subscriber may include no charging Event. |
| `fact_charging_event` | `record_type_id` | `dim_record_type` | 1:N | 1:many / always | many:1 / always | Many charging Events belong to one record Type, every charging Event matches a record Type, and every record Type includes at least one charging Event. |
| `fact_charging_event` | `rating_group_id` | `dim_rating_group` | 1:N | 1:many / always | many:1 / always | Many charging Events belong to one rating Group, every charging Event matches a rating Group, and every rating Group includes at least one charging Event. |
| `fact_charging_event` | `balance_type_id` | `dim_balance_type` | 1:N | 1:many / always | many:1 / always | Many charging Events belong to one balance Type, every charging Event matches a balance Type, and every balance Type includes at least one charging Event. |
| `fact_charging_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many charging Events belong to one calendar Day, every charging Event matches a calendar Day, and every calendar Day includes at least one charging Event. |
| `fact_charging_event` | `network_element_id` | `dim_network_element` | 1:N | 1:many / optional | many:1 / always | Many charging Events belong to one network Element, every charging Event matches a network Element, and a network Element may include no charging Event. |
| `fact_charging_event` | `qos_id` | `dim_qos` | 1:N | 1:many / optional | many:1 / always | Many charging Events belong to one qoS Profile, every charging Event matches a qoS Profile, and a qoS Profile may include no charging Event. |
| `fact_charging_event` | `apn_id` | `dim_apn` | 1:N | 1:many / optional | many:1 / always | Many charging Events belong to one aPN DNN, every charging Event matches a aPN DNN, and a aPN DNN may include no charging Event. |
| `fact_charging_event` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / optional | many:1 / always | Many charging Events belong to one rate Plan, every charging Event matches a rate Plan, and a rate Plan may include no charging Event. |
| `fact_charging_event` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many charging Events belong to one pLMN, every charging Event matches a pLMN, and a pLMN may include no charging Event. |
| `fact_balance_reservation` | `charging_event_id` | `fact_charging_event` | 1:1 | 1:1 / optional | 1:1 / always | Each balance Reservation matches exactly one charging Event, each charging Event matches at most one balance Reservation, and not every charging Event is matched. A reservation matches one charging event, and some events do not reserve. |
| `fact_balance_reservation` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many balance Reservations belong to one subscription, every balance Reservation matches a subscription, and a subscription may include no balance Reservation. |
| `fact_balance_reservation` | `balance_type_id` | `dim_balance_type` | 1:N | 1:many / always | many:1 / always | Many balance Reservations belong to one balance Type, every balance Reservation matches a balance Type, and every balance Type includes at least one balance Reservation. |
| `fact_balance_reservation` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many balance Reservations belong to one calendar Day, every balance Reservation matches a calendar Day, and every calendar Day includes at least one balance Reservation. |
| `fact_balance_debit` | `balance_reservation_id` | `fact_balance_reservation` | 1:1 | 1:1 / optional | 1:1 / always | Each balance Debit matches exactly one balance Reservation, each balance Reservation matches at most one balance Debit, and not every balance Reservation is matched. A debit matches one reservation, and some reservations expire unused. |
| `fact_balance_debit` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many balance Debits belong to one subscription, every balance Debit matches a subscription, and a subscription may include no balance Debit. |
| `fact_balance_debit` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many balance Debits belong to one calendar Day, every balance Debit matches a calendar Day, and every calendar Day includes at least one balance Debit. |
| `fact_balance_debit` | `balance_type_id` | `dim_balance_type` | 1:N | 1:many / always | many:1 / always | Many balance Debits belong to one balance Type, every balance Debit matches a balance Type, and every balance Type includes at least one balance Debit. |
| `fact_attach` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / always | Many attach Events belong to one subscriber, every attach Event matches a subscriber, and a subscriber may include no attach Event. |
| `fact_attach` | `cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / always | Many attach Events belong to one cell, every attach Event matches a cell, and a cell may include no attach Event. |
| `fact_attach` | `technology_id` | `dim_technology` | 1:N | 1:many / always | many:1 / always | Many attach Events belong to one technology, every attach Event matches a technology, and every technology includes at least one attach Event. |
| `fact_attach` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many attach Events belong to one pLMN, every attach Event matches a pLMN, and a pLMN may include no attach Event. |
| `fact_attach` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many attach Events belong to one calendar Day, every attach Event matches a calendar Day, and every calendar Day includes at least one attach Event. |
| `fact_attach` | `network_element_id` | `dim_network_element` | 1:N | 1:many / optional | many:1 / always | Many attach Events belong to one network Element, every attach Event matches a network Element, and a network Element may include no attach Event. |
| `fact_attach` | `imsi_id` | `dim_imsi` | 1:N | 1:many / optional | many:1 / always | Many attach Events belong to one iMSI, every attach Event matches a iMSI, and a iMSI may include no attach Event. |
| `fact_attach` | `msisdn_id` | `dim_msisdn` | 1:N | 1:many / optional | many:1 / always | Many attach Events belong to one public Number, every attach Event matches a public Number, and a public Number may include no attach Event. |
| `fact_rated_charge` | `data_cdr_id` | `fact_data_cdr` | 1:1 | 1:1 / optional | 1:1 / optional | A rated Charge may match one data CDR, and a data CDR may match one rated Charge. Data CDRs are one slice of rated usage. |
| `fact_rated_charge` | `voice_cdr_id` | `fact_voice_cdr` | 1:1 | 1:1 / optional | 1:1 / optional | A rated Charge may match one voice CDR, and a voice CDR may match one rated Charge. Voice CDRs are one slice of rated usage. |
| `fact_rated_charge` | `sms_cdr_id` | `fact_sms_cdr` | 1:1 | 1:1 / optional | 1:1 / optional | A rated Charge may match one sMS CDR, and a sMS CDR may match one rated Charge. SMS CDRs are one slice of rated usage. |
| `fact_rated_charge` | `content_cdr_id` | `fact_content_cdr` | 1:1 | 1:1 / optional | 1:1 / optional | A rated Charge may match one content CDR, and a content CDR may match one rated Charge. Content CDRs are one slice of rated usage. |
| `fact_rated_charge` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many rated Charges belong to one subscription, every rated Charge matches a subscription, and a subscription may include no rated Charge. |
| `fact_rated_charge` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / always | many:1 / always | Many rated Charges belong to one rate Plan, every rated Charge matches a rate Plan, and every rate Plan includes at least one rated Charge. |
| `fact_rated_charge` | `charge_type_id` | `dim_charge_type` | 1:N | 1:many / always | many:1 / always | Many rated Charges belong to one charge Type, every rated Charge matches a charge Type, and every charge Type includes at least one rated Charge. |
| `fact_rated_charge` | `tariff_id` | `dim_tariff` | 1:N | 1:many / optional | many:1 / optional | A rated Charge may match one tariff, and a tariff may include no rated Charge. Recurring charges are not usage-tariffed. |
| `fact_rated_charge` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many rated Charges belong to one currency, every rated Charge matches a currency, and a currency may include no rated Charge. |
| `fact_rated_charge` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many rated Charges belong to one calendar Day, every rated Charge matches a calendar Day, and every calendar Day includes at least one rated Charge. |
| `fact_rated_charge` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / always | Many rated Charges belong to one gL Account, every rated Charge matches a gL Account, and a gL Account may include no rated Charge. |
| `fact_rated_charge` | `tax_code_id` | `dim_tax_code` | 1:N | 1:many / optional | many:1 / optional | A rated Charge may match one tax Code, and a tax Code may include no rated Charge. |
| `fact_policy_event` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many policy Events belong to one subscription, every policy Event matches a subscription, and a subscription may include no policy Event. |
| `fact_policy_event` | `policy_rule_id` | `dim_policy_rule` | 1:N | 1:many / always | many:1 / always | Many policy Events belong to one policy Rule, every policy Event matches a policy Rule, and every policy Rule includes at least one policy Event. |
| `fact_policy_event` | `qos_id` | `dim_qos` | 1:N | 1:many / optional | many:1 / always | Many policy Events belong to one qoS Profile, every policy Event matches a qoS Profile, and a qoS Profile may include no policy Event. |
| `fact_policy_event` | `slice_id` | `dim_slice` | 1:N | 1:many / optional | many:1 / optional | A policy Event may match one network Slice, and a network Slice may include no policy Event. |
| `fact_policy_event` | `cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / optional | A policy Event may match one cell, and a cell may include no policy Event. |
| `fact_policy_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many policy Events belong to one calendar Day, every policy Event matches a calendar Day, and every calendar Day includes at least one policy Event. |
| `fact_policy_event` | `network_element_id` | `dim_network_element` | 1:N | 1:many / optional | many:1 / always | Many policy Events belong to one network Element, every policy Event matches a network Element, and a network Element may include no policy Event. |
| `fact_handover` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / always | Many handovers belong to one subscriber, every handover matches a subscriber, and a subscriber may include no handover. |
| `fact_handover` | `source_cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / always | Many handovers belong to one cell, every handover matches a cell, and a cell may include no handover. Cell the session left. |
| `fact_handover` | `handover_type_id` | `dim_handover_type` | 1:N | 1:many / always | many:1 / always | Many handovers belong to one handover Type, every handover matches a handover Type, and every handover Type includes at least one handover. |
| `fact_handover` | `technology_id` | `dim_technology` | 1:N | 1:many / optional | many:1 / always | Many handovers belong to one technology, every handover matches a technology, and a technology may include no handover. |
| `fact_handover` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many handovers belong to one calendar Day, every handover matches a calendar Day, and every calendar Day includes at least one handover. |
| `fact_handover` | `network_element_id` | `dim_network_element` | 1:N | 1:many / optional | many:1 / always | Many handovers belong to one network Element, every handover matches a network Element, and a network Element may include no handover. |
| `fact_handover_target` | `handover_id` | `fact_handover` | 1:1 | 1:1 / always | 1:1 / always | Each handover Target matches exactly one handover, and each handover matches exactly one handover Target. Each handover has one target-cell row, and each target row has one handover. |
| `fact_handover_target` | `target_cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / always | Many handover Targets belong to one cell, every handover Target matches a cell, and a cell may include no handover Target. Cell the session entered. |
| `fact_allowance_draw` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many allowance Draws belong to one subscription, every allowance Draw matches a subscription, and a subscription may include no allowance Draw. |
| `fact_allowance_draw` | `allowance_bucket_id` | `dim_allowance_bucket` | 1:N | 1:many / always | many:1 / always | Many allowance Draws belong to one allowance Bucket, every allowance Draw matches a allowance Bucket, and every allowance Bucket includes at least one allowance Draw. |
| `fact_allowance_draw` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many allowance Draws belong to one calendar Day, every allowance Draw matches a calendar Day, and every calendar Day includes at least one allowance Draw. |
| `fact_allowance_draw` | `rated_charge_id` | `fact_rated_charge` | 1:N | 1:many / optional | many:1 / optional | A allowance Draw may match one rated Charge, and a rated Charge may include no allowance Draw. A snapshot draw may not cite one charge. |
| `fact_location_update` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / always | Many location Updates belong to one subscriber, every location Update matches a subscriber, and a subscriber may include no location Update. |
| `fact_location_update` | `location_area_id` | `dim_location_area` | 1:N | 1:many / always | many:1 / always | Many location Updates belong to one location Area, every location Update matches a location Area, and every location Area includes at least one location Update. |
| `fact_location_update` | `cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / optional | A location Update may match one cell, and a cell may include no location Update. |
| `fact_location_update` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many location Updates belong to one calendar Day, every location Update matches a calendar Day, and every calendar Day includes at least one location Update. |
| `fact_location_update` | `technology_id` | `dim_technology` | 1:N | 1:many / optional | many:1 / always | Many location Updates belong to one technology, every location Update matches a technology, and a technology may include no location Update. |
| `fact_qos_change` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many qoS Changes belong to one subscription, every qoS Change matches a subscription, and a subscription may include no qoS Change. |
| `fact_qos_change` | `qos_id` | `dim_qos` | 1:N | 1:many / always | many:1 / always | Many qoS Changes belong to one qoS Profile, every qoS Change matches a qoS Profile, and every qoS Profile includes at least one qoS Change. |
| `fact_qos_change` | `cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / always | Many qoS Changes belong to one cell, every qoS Change matches a cell, and a cell may include no qoS Change. |
| `fact_qos_change` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many qoS Changes belong to one calendar Day, every qoS Change matches a calendar Day, and every calendar Day includes at least one qoS Change. |
| `fact_qos_change` | `policy_rule_id` | `dim_policy_rule` | 1:N | 1:many / optional | many:1 / optional | A qoS Change may match one policy Rule, and a policy Rule may include no qoS Change. |
| `fact_cell_counter` | `cell_id` | `dim_cell` | 1:N | 1:many / always | many:1 / always | Many cell Counters belong to one cell, every cell Counter matches a cell, and every cell includes at least one cell Counter. Every cell has a counter in every interval of the window. |
| `fact_cell_counter` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many cell Counters belong to one calendar Day, every cell Counter matches a calendar Day, and every calendar Day includes at least one cell Counter. |
| `fact_cell_counter` | `technology_id` | `dim_technology` | 1:N | 1:many / optional | many:1 / always | Many cell Counters belong to one technology, every cell Counter matches a technology, and a technology may include no cell Counter. |
| `fact_cell_counter` | `cell_site_id` | `dim_cell_site` | 1:N | 1:many / always | many:1 / always | Many cell Counters belong to one cell Site, every cell Counter matches a cell Site, and every cell Site includes at least one cell Counter. |
| `fact_tap_out` | `roaming_partner_id` | `dim_roaming_partner` | 1:N | 1:many / always | many:1 / always | Many tAP Out Records belong to one roaming Partner, every tAP Out Record matches a roaming Partner, and every roaming Partner includes at least one tAP Out Record. Every roaming partner receives outcollect records. |
| `fact_tap_out` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many tAP Out Records belong to one pLMN, every tAP Out Record matches a pLMN, and a pLMN may include no tAP Out Record. |
| `fact_tap_out` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many tAP Out Records belong to one subscription, every tAP Out Record matches a subscription, and a subscription may include no tAP Out Record. |
| `fact_tap_out` | `record_type_id` | `dim_record_type` | 1:N | 1:many / optional | many:1 / always | Many tAP Out Records belong to one record Type, every tAP Out Record matches a record Type, and a record Type may include no tAP Out Record. |
| `fact_tap_out` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many tAP Out Records belong to one calendar Day, every tAP Out Record matches a calendar Day, and every calendar Day includes at least one tAP Out Record. |
| `fact_tap_out` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many tAP Out Records belong to one currency, every tAP Out Record matches a currency, and a currency may include no tAP Out Record. |
| `fact_tap_out` | `voice_cdr_id` | `fact_voice_cdr` | 1:1 | 1:1 / optional | 1:1 / optional | A tAP Out Record may match one voice CDR, and a voice CDR may match one tAP Out Record. Voice outcollect is one slice of TAP-out. |
| `fact_tap_out` | `data_cdr_id` | `fact_data_cdr` | 1:1 | 1:1 / optional | 1:1 / optional | A tAP Out Record may match one data CDR, and a data CDR may match one tAP Out Record. Data outcollect is one slice of TAP-out. |
| `fact_tap_in` | `roaming_partner_id` | `dim_roaming_partner` | 1:N | 1:many / always | many:1 / always | Many tAP In Records belong to one roaming Partner, every tAP In Record matches a roaming Partner, and every roaming Partner includes at least one tAP In Record. Every partner sends incollect records. |
| `fact_tap_in` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many tAP In Records belong to one pLMN, every tAP In Record matches a pLMN, and a pLMN may include no tAP In Record. |
| `fact_tap_in` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many tAP In Records belong to one calendar Day, every tAP In Record matches a calendar Day, and every calendar Day includes at least one tAP In Record. |
| `fact_tap_in` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many tAP In Records belong to one currency, every tAP In Record matches a currency, and a currency may include no tAP In Record. |
| `fact_tap_in` | `record_type_id` | `dim_record_type` | 1:N | 1:many / optional | many:1 / always | Many tAP In Records belong to one record Type, every tAP In Record matches a record Type, and a record Type may include no tAP In Record. |
| `fact_invoice` | `billing_account_id` | `dim_billing_account` | 1:1 | 1:1 / always | 1:1 / always | Each invoice matches exactly one billing Account, and each billing Account matches exactly one invoice. The window closes exactly one invoice per billing account. |
| `fact_invoice` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many invoices belong to one currency, every invoice matches a currency, and a currency may include no invoice. |
| `fact_invoice` | `bill_cycle_id` | `dim_bill_cycle` | 1:N | 1:many / always | many:1 / always | Many invoices belong to one bill Cycle, every invoice matches a bill Cycle, and every bill Cycle includes at least one invoice. |
| `fact_invoice` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many invoices belong to one calendar Day, every invoice matches a calendar Day, and a calendar Day may include no invoice. |
| `fact_invoice` | `market_id` | `dim_market` | 1:N | 1:many / always | many:1 / always | Many invoices belong to one market, every invoice matches a market, and every market includes at least one invoice. |
| `fact_invoice` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many invoices belong to one legal Entity, every invoice matches a legal Entity, and a legal Entity may include no invoice. |
| `fact_invoice_line` | `invoice_id` | `fact_invoice` | 1:N | 1:many / always | many:1 / always | Many invoice Lines belong to one invoice, every invoice Line matches a invoice, and every invoice includes at least one invoice Line. Every invoice has charge lines. |
| `fact_invoice_line` | `charge_type_id` | `dim_charge_type` | 1:N | 1:many / always | many:1 / always | Many invoice Lines belong to one charge Type, every invoice Line matches a charge Type, and every charge Type includes at least one invoice Line. |
| `fact_invoice_line` | `tax_code_id` | `dim_tax_code` | 1:N | 1:many / optional | many:1 / optional | A invoice Line may match one tax Code, and a tax Code may include no invoice Line. |
| `fact_invoice_line` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many invoice Lines belong to one currency, every invoice Line matches a currency, and a currency may include no invoice Line. |
| `fact_invoice_line` | `rated_charge_id` | `fact_rated_charge` | 1:N | 1:many / optional | many:1 / optional | A invoice Line may match one rated Charge, and a rated Charge may include no invoice Line. Recurring fees are not tied to one rated CDR. |
| `fact_invoice_line` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / always | Many invoice Lines belong to one gL Account, every invoice Line matches a gL Account, and a gL Account may include no invoice Line. |
| `fact_invoice_line` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many invoice Lines belong to one calendar Day, every invoice Line matches a calendar Day, and a calendar Day may include no invoice Line. |
| `fact_tax_line` | `invoice_id` | `fact_invoice` | 1:N | 1:many / always | many:1 / always | Many tax Lines belong to one invoice, every tax Line matches a invoice, and every invoice includes at least one tax Line. Every invoice has at least one tax line. |
| `fact_tax_line` | `tax_code_id` | `dim_tax_code` | 1:N | 1:many / always | many:1 / always | Many tax Lines belong to one tax Code, every tax Line matches a tax Code, and every tax Code includes at least one tax Line. |
| `fact_tax_line` | `tax_jurisdiction_id` | `dim_tax_jurisdiction` | 1:N | 1:many / optional | many:1 / always | Many tax Lines belong to one tax Jurisdiction, every tax Line matches a tax Jurisdiction, and a tax Jurisdiction may include no tax Line. |
| `fact_tax_line` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many tax Lines belong to one currency, every tax Line matches a currency, and a currency may include no tax Line. |
| `fact_document` | `invoice_id` | `fact_invoice` | 1:1 | 1:1 / always | 1:1 / always | Each bill Document matches exactly one invoice, and each invoice matches exactly one bill Document. Each invoice has one rendered bill document. |
| `fact_document` | `document_type_id` | `dim_document_type` | 1:N | 1:many / optional | many:1 / always | Many bill Documents belong to one document Type, every bill Document matches a document Type, and a document Type may include no bill Document. |
| `fact_document` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many bill Documents belong to one calendar Day, every bill Document matches a calendar Day, and a calendar Day may include no bill Document. |
| `fact_payment` | `billing_account_id` | `dim_billing_account` | 1:N | 1:many / optional | many:1 / always | Many payments belong to one billing Account, every payment matches a billing Account, and a billing Account may include no payment. |
| `fact_payment` | `payment_method_id` | `dim_payment_method` | 1:N | 1:many / always | many:1 / always | Many payments belong to one payment Method, every payment matches a payment Method, and every payment Method includes at least one payment. |
| `fact_payment` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many payments belong to one currency, every payment matches a currency, and a currency may include no payment. |
| `fact_payment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many payments belong to one calendar Day, every payment matches a calendar Day, and every calendar Day includes at least one payment. |
| `fact_payment` | `bank_id` | `dim_bank` | 1:N | 1:many / optional | many:1 / optional | A payment may match one bank, and a bank may include no payment. |
| `fact_adjustment` | `billing_account_id` | `dim_billing_account` | 1:N | 1:many / optional | many:1 / always | Many adjustments belong to one billing Account, every adjustment matches a billing Account, and a billing Account may include no adjustment. |
| `fact_adjustment` | `adjustment_reason_id` | `dim_adjustment_reason` | 1:N | 1:many / always | many:1 / always | Many adjustments belong to one adjustment Reason, every adjustment matches a adjustment Reason, and every adjustment Reason includes at least one adjustment. |
| `fact_adjustment` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many adjustments belong to one currency, every adjustment matches a currency, and a currency may include no adjustment. |
| `fact_adjustment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many adjustments belong to one calendar Day, every adjustment matches a calendar Day, and a calendar Day may include no adjustment. |
| `fact_adjustment` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A adjustment may match one employee, and a employee may include no adjustment. |
| `fact_dunning_event` | `billing_account_id` | `dim_billing_account` | 1:N | 1:many / optional | many:1 / always | Many dunning Events belong to one billing Account, every dunning Event matches a billing Account, and a billing Account may include no dunning Event. |
| `fact_dunning_event` | `dunning_level_id` | `dim_dunning_level` | 1:N | 1:many / always | many:1 / always | Many dunning Events belong to one dunning Level, every dunning Event matches a dunning Level, and every dunning Level includes at least one dunning Event. |
| `fact_dunning_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many dunning Events belong to one calendar Day, every dunning Event matches a calendar Day, and a calendar Day may include no dunning Event. |
| `fact_credit_note` | `invoice_id` | `fact_invoice` | 1:N | 1:many / optional | many:1 / optional | A credit Note may match one invoice, and a invoice may include no credit Note. |
| `fact_credit_note` | `billing_account_id` | `dim_billing_account` | 1:N | 1:many / optional | many:1 / always | Many credit Notes belong to one billing Account, every credit Note matches a billing Account, and a billing Account may include no credit Note. |
| `fact_credit_note` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many credit Notes belong to one currency, every credit Note matches a currency, and a currency may include no credit Note. |
| `fact_credit_note` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many credit Notes belong to one calendar Day, every credit Note matches a calendar Day, and a calendar Day may include no credit Note. |
| `fact_topup` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many top Ups belong to one subscription, every top Up matches a subscription, and a subscription may include no top Up. |
| `fact_topup` | `payment_method_id` | `dim_payment_method` | 1:N | 1:many / optional | many:1 / always | Many top Ups belong to one payment Method, every top Up matches a payment Method, and a payment Method may include no top Up. |
| `fact_topup` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many top Ups belong to one currency, every top Up matches a currency, and a currency may include no top Up. |
| `fact_topup` | `channel_id` | `dim_channel` | 1:N | 1:many / always | many:1 / always | Many top Ups belong to one channel, every top Up matches a channel, and every channel includes at least one top Up. |
| `fact_topup` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many top Ups belong to one calendar Day, every top Up matches a calendar Day, and every calendar Day includes at least one top Up. |
| `fact_topup` | `dealer_id` | `dim_dealer` | 1:N | 1:many / optional | many:1 / optional | A top Up may match one dealer, and a dealer may include no top Up. |
| `fact_refund` | `payment_id` | `fact_payment` | 1:N | 1:many / optional | many:1 / optional | A refund may match one payment, and a payment may include no refund. |
| `fact_refund` | `billing_account_id` | `dim_billing_account` | 1:N | 1:many / optional | many:1 / always | Many refunds belong to one billing Account, every refund matches a billing Account, and a billing Account may include no refund. |
| `fact_refund` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many refunds belong to one currency, every refund matches a currency, and a currency may include no refund. |
| `fact_refund` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many refunds belong to one calendar Day, every refund matches a calendar Day, and a calendar Day may include no refund. |
| `fact_refund` | `adjustment_reason_id` | `dim_adjustment_reason` | 1:N | 1:many / optional | many:1 / always | Many refunds belong to one adjustment Reason, every refund matches a adjustment Reason, and a adjustment Reason may include no refund. |
| `fact_mediation_reject` | `mediation_rule_id` | `dim_mediation_rule` | 1:N | 1:many / always | many:1 / always | Many mediation Rejects belong to one mediation Rule, every mediation Reject matches a mediation Rule, and every mediation Rule includes at least one mediation Reject. |
| `fact_mediation_reject` | `record_type_id` | `dim_record_type` | 1:N | 1:many / optional | many:1 / always | Many mediation Rejects belong to one record Type, every mediation Reject matches a record Type, and a record Type may include no mediation Reject. |
| `fact_mediation_reject` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many mediation Rejects belong to one calendar Day, every mediation Reject matches a calendar Day, and every calendar Day includes at least one mediation Reject. |
| `fact_mediation_reject` | `recording_entity_id` | `dim_recording_entity` | 1:N | 1:many / optional | many:1 / always | Many mediation Rejects belong to one recording Entity, every mediation Reject matches a recording Entity, and a recording Entity may include no mediation Reject. |
| `fact_mediation_reject` | `data_cdr_id` | `fact_data_cdr` | 1:1 | 1:1 / optional | 1:1 / optional | A mediation Reject may match one data CDR, and a data CDR may match one mediation Reject. A reject may cite the data CDR it failed. |
| `fact_mediation_reject` | `voice_cdr_id` | `fact_voice_cdr` | 1:1 | 1:1 / optional | 1:1 / optional | A mediation Reject may match one voice CDR, and a voice CDR may match one mediation Reject. |
| `fact_mediation_reject` | `sms_cdr_id` | `fact_sms_cdr` | 1:1 | 1:1 / optional | 1:1 / optional | A mediation Reject may match one sMS CDR, and a sMS CDR may match one mediation Reject. |
| `fact_duplicate_suspect` | `record_type_id` | `dim_record_type` | 1:N | 1:many / optional | many:1 / always | Many duplicate Suspects belong to one record Type, every duplicate Suspect matches a record Type, and a record Type may include no duplicate Suspect. |
| `fact_duplicate_suspect` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many duplicate Suspects belong to one calendar Day, every duplicate Suspect matches a calendar Day, and a calendar Day may include no duplicate Suspect. |
| `fact_duplicate_suspect` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / optional | A duplicate Suspect may match one subscription, and a subscription may include no duplicate Suspect. |
| `fact_rerate` | `rated_charge_id` | `fact_rated_charge` | 1:N | 1:many / optional | many:1 / always | Many rerate Events belong to one rated Charge, every rerate Event matches a rated Charge, and a rated Charge may include no rerate Event. A rerate cites the charge it replaces. |
| `fact_rerate` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many rerate Events belong to one calendar Day, every rerate Event matches a calendar Day, and a calendar Day may include no rerate Event. |
| `fact_rerate` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A rerate Event may match one employee, and a employee may include no rerate Event. |
| `fact_number_port` | `msisdn_id` | `dim_msisdn` | 1:N | 1:many / optional | many:1 / always | Many number Ports belong to one public Number, every number Port matches a public Number, and a public Number may include no number Port. |
| `fact_number_port` | `np_operator_id` | `dim_np_operator` | 1:N | 1:many / always | many:1 / always | Many number Ports belong to one porting Operator, every number Port matches a porting Operator, and every porting Operator includes at least one number Port. |
| `fact_number_port` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / optional | A number Port may match one subscription, and a subscription may include no number Port. |
| `fact_number_port` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many number Ports belong to one calendar Day, every number Port matches a calendar Day, and a calendar Day may include no number Port. |
| `fact_sim_swap` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / always | Many sIM Swaps belong to one subscriber, every sIM Swap matches a subscriber, and a subscriber may include no sIM Swap. |
| `fact_sim_swap` | `sim_id` | `dim_sim` | 1:N | 1:many / optional | many:1 / always | Many sIM Swaps belong to one sIM, every sIM Swap matches a sIM, and a sIM may include no sIM Swap. |
| `fact_sim_swap` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A sIM Swap may match one employee, and a employee may include no sIM Swap. |
| `fact_sim_swap` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many sIM Swaps belong to one calendar Day, every sIM Swap matches a calendar Day, and a calendar Day may include no sIM Swap. |
| `fact_sim_swap` | `dealer_id` | `dim_dealer` | 1:N | 1:many / optional | many:1 / optional | A sIM Swap may match one dealer, and a dealer may include no sIM Swap. |
| `fact_outage_ticket` | `cell_site_id` | `dim_cell_site` | 1:N | 1:many / optional | many:1 / optional | A outage Ticket may match one cell Site, and a cell Site may include no outage Ticket. |
| `fact_outage_ticket` | `network_element_id` | `dim_network_element` | 1:N | 1:many / optional | many:1 / optional | A outage Ticket may match one network Element, and a network Element may include no outage Ticket. |
| `fact_outage_ticket` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many outage Tickets belong to one calendar Day, every outage Ticket matches a calendar Day, and a calendar Day may include no outage Ticket. |
| `fact_outage_ticket` | `trouble_code_id` | `dim_trouble_code` | 1:N | 1:many / optional | many:1 / always | Many outage Tickets belong to one trouble Code, every outage Ticket matches a trouble Code, and a trouble Code may include no outage Ticket. |
| `fact_network_alarm` | `network_element_id` | `dim_network_element` | 1:N | 1:many / optional | many:1 / always | Many network Alarms belong to one network Element, every network Alarm matches a network Element, and a network Element may include no network Alarm. |
| `fact_network_alarm` | `cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / optional | A network Alarm may match one cell, and a cell may include no network Alarm. |
| `fact_network_alarm` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many network Alarms belong to one calendar Day, every network Alarm matches a calendar Day, and every calendar Day includes at least one network Alarm. |
| `fact_network_alarm` | `alarm_severity_id` | `dim_alarm_severity` | 1:N | 1:many / always | many:1 / always | Many network Alarms belong to one alarm Severity, every network Alarm matches a alarm Severity, and every alarm Severity includes at least one network Alarm. |
| `fact_network_alarm` | `technology_id` | `dim_technology` | 1:N | 1:many / optional | many:1 / always | Many network Alarms belong to one technology, every network Alarm matches a technology, and a technology may include no network Alarm. |
| `fact_counter_breach` | `cell_counter_id` | `fact_cell_counter` | 1:N | 1:many / optional | many:1 / always | Many counter Breaches belong to one cell Counter, every counter Breach matches a cell Counter, and a cell Counter may include no counter Breach. |
| `fact_counter_breach` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many counter Breaches belong to one calendar Day, every counter Breach matches a calendar Day, and a calendar Day may include no counter Breach. |
| `fact_counter_breach` | `cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / always | Many counter Breaches belong to one cell, every counter Breach matches a cell, and a cell may include no counter Breach. |
| `fact_interaction` | `party_id` | `dim_party` | 1:N | 1:many / optional | many:1 / always | Many care Interactions belong to one party, every care Interaction matches a party, and a party may include no care Interaction. |
| `fact_interaction` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / optional | A care Interaction may match one subscriber, and a subscriber may include no care Interaction. |
| `fact_interaction` | `agent_id` | `dim_agent` | 1:N | 1:many / always | many:1 / always | Many care Interactions belong to one care Agent, every care Interaction matches a care Agent, and every care Agent includes at least one care Interaction. Every care agent handles interactions. |
| `fact_interaction` | `queue_id` | `dim_queue` | 1:N | 1:many / always | many:1 / always | Many care Interactions belong to one care Queue, every care Interaction matches a care Queue, and every care Queue includes at least one care Interaction. |
| `fact_interaction` | `channel_id` | `dim_channel` | 1:N | 1:many / optional | many:1 / always | Many care Interactions belong to one channel, every care Interaction matches a channel, and a channel may include no care Interaction. |
| `fact_interaction` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many care Interactions belong to one calendar Day, every care Interaction matches a calendar Day, and every calendar Day includes at least one care Interaction. |
| `fact_interaction` | `care_reason_id` | `dim_care_reason` | 1:N | 1:many / always | many:1 / always | Many care Interactions belong to one care Reason, every care Interaction matches a care Reason, and every care Reason includes at least one care Interaction. |
| `fact_trouble_ticket` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / always | Many trouble Tickets belong to one subscriber, every trouble Ticket matches a subscriber, and a subscriber may include no trouble Ticket. |
| `fact_trouble_ticket` | `trouble_code_id` | `dim_trouble_code` | 1:N | 1:many / always | many:1 / always | Many trouble Tickets belong to one trouble Code, every trouble Ticket matches a trouble Code, and every trouble Code includes at least one trouble Ticket. |
| `fact_trouble_ticket` | `channel_id` | `dim_channel` | 1:N | 1:many / optional | many:1 / always | Many trouble Tickets belong to one channel, every trouble Ticket matches a channel, and a channel may include no trouble Ticket. |
| `fact_trouble_ticket` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many trouble Tickets belong to one calendar Day, every trouble Ticket matches a calendar Day, and every calendar Day includes at least one trouble Ticket. |
| `fact_trouble_ticket` | `market_id` | `dim_market` | 1:N | 1:many / optional | many:1 / always | Many trouble Tickets belong to one market, every trouble Ticket matches a market, and a market may include no trouble Ticket. |
| `fact_trouble_ticket` | `agent_id` | `dim_agent` | 1:N | 1:many / optional | many:1 / optional | A trouble Ticket may match one care Agent, and a care Agent may include no trouble Ticket. |
| `fact_ticket_event` | `trouble_ticket_id` | `fact_trouble_ticket` | 1:N | 1:many / always | many:1 / always | Many ticket Events belong to one trouble Ticket, every ticket Event matches a trouble Ticket, and every trouble Ticket includes at least one ticket Event. Every ticket has events. |
| `fact_ticket_event` | `agent_id` | `dim_agent` | 1:N | 1:many / optional | many:1 / always | Many ticket Events belong to one care Agent, every ticket Event matches a care Agent, and a care Agent may include no ticket Event. |
| `fact_ticket_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many ticket Events belong to one calendar Day, every ticket Event matches a calendar Day, and a calendar Day may include no ticket Event. |
| `fact_dealer_sale` | `dealer_id` | `dim_dealer` | 1:N | 1:many / always | many:1 / always | Many dealer Sales belong to one dealer, every dealer Sale matches a dealer, and every dealer includes at least one dealer Sale. Every dealer records a sale in the window. |
| `fact_dealer_sale` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many dealer Sales belong to one subscription, every dealer Sale matches a subscription, and a subscription may include no dealer Sale. |
| `fact_dealer_sale` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / optional | many:1 / always | Many dealer Sales belong to one rate Plan, every dealer Sale matches a rate Plan, and a rate Plan may include no dealer Sale. |
| `fact_dealer_sale` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many dealer Sales belong to one calendar Day, every dealer Sale matches a calendar Day, and a calendar Day may include no dealer Sale. |
| `fact_dealer_sale` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A dealer Sale may match one employee, and a employee may include no dealer Sale. |
| `fact_dealer_sale` | `sale_type_id` | `dim_sale_type` | 1:N | 1:many / always | many:1 / always | Many dealer Sales belong to one sale Type, every dealer Sale matches a sale Type, and every sale Type includes at least one dealer Sale. |
| `fact_interconnect_invoice` | `carrier_id` | `dim_carrier` | 1:1 | 1:1 / always | 1:1 / always | Each interconnect Invoice matches exactly one interconnect Carrier, and each interconnect Carrier matches exactly one interconnect Invoice. Each interconnect carrier has one invoice in the window. |
| `fact_interconnect_invoice` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many interconnect Invoices belong to one currency, every interconnect Invoice matches a currency, and a currency may include no interconnect Invoice. |
| `fact_interconnect_invoice` | `accounting_period_id` | `dim_accounting_period` | 1:N | 1:many / always | many:1 / always | Many interconnect Invoices belong to one accounting Period, every interconnect Invoice matches a accounting Period, and every accounting Period includes at least one interconnect Invoice. |
| `fact_interconnect_invoice` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many interconnect Invoices belong to one calendar Day, every interconnect Invoice matches a calendar Day, and a calendar Day may include no interconnect Invoice. |
| `fact_settlement_line` | `roaming_partner_id` | `dim_roaming_partner` | 1:N | 1:many / always | many:1 / always | Many settlement Lines belong to one roaming Partner, every settlement Line matches a roaming Partner, and every roaming Partner includes at least one settlement Line. Every partner has settlement lines. |
| `fact_settlement_line` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many settlement Lines belong to one currency, every settlement Line matches a currency, and a currency may include no settlement Line. |
| `fact_settlement_line` | `accounting_period_id` | `dim_accounting_period` | 1:N | 1:many / always | many:1 / always | Many settlement Lines belong to one accounting Period, every settlement Line matches a accounting Period, and every accounting Period includes at least one settlement Line. |
| `fact_settlement_line` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many settlement Lines belong to one calendar Day, every settlement Line matches a calendar Day, and a calendar Day may include no settlement Line. |
| `fact_settlement_line` | `record_type_id` | `dim_record_type` | 1:N | 1:many / optional | many:1 / always | Many settlement Lines belong to one record Type, every settlement Line matches a record Type, and a record Type may include no settlement Line. |
| `fact_settlement_line` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many settlement Lines belong to one pLMN, every settlement Line matches a pLMN, and a pLMN may include no settlement Line. |
| `fact_journal_line` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / always | many:1 / always | Many journal Lines belong to one gL Account, every journal Line matches a gL Account, and every gL Account includes at least one journal Line. Every ledger account used by the operator is posted. |
| `fact_journal_line` | `accounting_period_id` | `dim_accounting_period` | 1:N | 1:many / always | many:1 / always | Many journal Lines belong to one accounting Period, every journal Line matches a accounting Period, and every accounting Period includes at least one journal Line. |
| `fact_journal_line` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many journal Lines belong to one currency, every journal Line matches a currency, and a currency may include no journal Line. |
| `fact_journal_line` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many journal Lines belong to one legal Entity, every journal Line matches a legal Entity, and a legal Entity may include no journal Line. |
| `fact_journal_line` | `cost_center_id` | `dim_cost_center` | 1:N | 1:many / optional | many:1 / optional | A journal Line may match one cost Center, and a cost Center may include no journal Line. |
| `fact_journal_line` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many journal Lines belong to one calendar Day, every journal Line matches a calendar Day, and every calendar Day includes at least one journal Line. |
| `fact_journal_line` | `journal_source_id` | `dim_journal_source` | 1:N | 1:many / always | many:1 / always | Many journal Lines belong to one journal Source, every journal Line matches a journal Source, and every journal Source includes at least one journal Line. |
| `fact_journal_line` | `cost_element_id` | `dim_cost_element` | 1:N | 1:many / optional | many:1 / optional | A journal Line may match one cost Element, and a cost Element may include no journal Line. |
| `fact_fraud_alert` | `fraud_rule_id` | `dim_fraud_rule` | 1:N | 1:many / always | many:1 / always | Many fraud Alerts belong to one fraud Rule, every fraud Alert matches a fraud Rule, and every fraud Rule includes at least one fraud Alert. |
| `fact_fraud_alert` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / always | Many fraud Alerts belong to one subscriber, every fraud Alert matches a subscriber, and a subscriber may include no fraud Alert. |
| `fact_fraud_alert` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many fraud Alerts belong to one calendar Day, every fraud Alert matches a calendar Day, and a calendar Day may include no fraud Alert. |
| `fact_fraud_alert` | `msisdn_id` | `dim_msisdn` | 1:N | 1:many / optional | many:1 / optional | A fraud Alert may match one public Number, and a public Number may include no fraud Alert. |
| `fact_barring_event` | `subscriber_id` | `dim_subscriber` | 1:N | 1:many / optional | many:1 / always | Many barring Events belong to one subscriber, every barring Event matches a subscriber, and a subscriber may include no barring Event. |
| `fact_barring_event` | `barring_id` | `dim_barring` | 1:N | 1:many / always | many:1 / always | Many barring Events belong to one barring Profile, every barring Event matches a barring Profile, and every barring Profile includes at least one barring Event. |
| `fact_barring_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many barring Events belong to one calendar Day, every barring Event matches a calendar Day, and a calendar Day may include no barring Event. |
| `fact_barring_event` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A barring Event may match one employee, and a employee may include no barring Event. |
| `fact_bundle_snapshot` | `subscription_id` | `dim_subscription` | 1:1 | 1:1 / always | 1:1 / always | Each bundle Snapshot matches exactly one subscription, and each subscription matches exactly one bundle Snapshot. Each subscription has one month-end bundle snapshot. |
| `fact_bundle_snapshot` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / optional | many:1 / always | Many bundle Snapshots belong to one rate Plan, every bundle Snapshot matches a rate Plan, and a rate Plan may include no bundle Snapshot. |
| `fact_bundle_snapshot` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many bundle Snapshots belong to one calendar Day, every bundle Snapshot matches a calendar Day, and a calendar Day may include no bundle Snapshot. |
| `fact_subscriber_snapshot` | `subscriber_id` | `dim_subscriber` | 1:1 | 1:1 / always | 1:1 / always | Each subscriber Snapshot matches exactly one subscriber, and each subscriber matches exactly one subscriber Snapshot. Each subscriber has one month-end snapshot. |
| `fact_subscriber_snapshot` | `segment_id` | `dim_segment` | 1:N | 1:many / optional | many:1 / always | Many subscriber Snapshots belong to one customer Segment, every subscriber Snapshot matches a customer Segment, and a customer Segment may include no subscriber Snapshot. |
| `fact_subscriber_snapshot` | `credit_class_id` | `dim_credit_class` | 1:N | 1:many / optional | many:1 / always | Many subscriber Snapshots belong to one credit Class, every subscriber Snapshot matches a credit Class, and a credit Class may include no subscriber Snapshot. |
| `fact_subscriber_snapshot` | `market_id` | `dim_market` | 1:N | 1:many / optional | many:1 / always | Many subscriber Snapshots belong to one market, every subscriber Snapshot matches a market, and a market may include no subscriber Snapshot. |
| `fact_subscriber_snapshot` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many subscriber Snapshots belong to one calendar Day, every subscriber Snapshot matches a calendar Day, and a calendar Day may include no subscriber Snapshot. |
| `fact_sla_breach` | `sla_id` | `dim_sla` | 1:N | 1:many / always | many:1 / always | Many sLA Breaches belong to one sLA, every sLA Breach matches a sLA, and every sLA includes at least one sLA Breach. |
| `fact_sla_breach` | `trouble_ticket_id` | `fact_trouble_ticket` | 1:N | 1:many / optional | many:1 / optional | A sLA Breach may match one trouble Ticket, and a trouble Ticket may include no sLA Breach. |
| `fact_sla_breach` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many sLA Breaches belong to one calendar Day, every sLA Breach matches a calendar Day, and a calendar Day may include no sLA Breach. |
| `fact_campaign_contact` | `campaign_id` | `dim_campaign` | 1:N | 1:many / always | many:1 / always | Many campaign Contacts belong to one campaign, every campaign Contact matches a campaign, and every campaign includes at least one campaign Contact. |
| `fact_campaign_contact` | `party_id` | `dim_party` | 1:N | 1:many / optional | many:1 / always | Many campaign Contacts belong to one party, every campaign Contact matches a party, and a party may include no campaign Contact. |
| `fact_campaign_contact` | `channel_id` | `dim_channel` | 1:N | 1:many / optional | many:1 / always | Many campaign Contacts belong to one channel, every campaign Contact matches a channel, and a channel may include no campaign Contact. |
| `fact_campaign_contact` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / always | many:1 / always | Many campaign Contacts belong to one calendar Day, every campaign Contact matches a calendar Day, and every calendar Day includes at least one campaign Contact. |
| `fact_campaign_contact` | `script_id` | `dim_script` | 1:N | 1:many / optional | many:1 / always | Many campaign Contacts belong to one care Script, every campaign Contact matches a care Script, and a care Script may include no campaign Contact. |
| `fact_promise_to_pay` | `billing_account_id` | `dim_billing_account` | 1:N | 1:many / optional | many:1 / always | Many promise To Pays belong to one billing Account, every promise To Pay matches a billing Account, and a billing Account may include no promise To Pay. |
| `fact_promise_to_pay` | `agent_id` | `dim_agent` | 1:N | 1:many / optional | many:1 / always | Many promise To Pays belong to one care Agent, every promise To Pay matches a care Agent, and a care Agent may include no promise To Pay. |
| `fact_promise_to_pay` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many promise To Pays belong to one calendar Day, every promise To Pay matches a calendar Day, and a calendar Day may include no promise To Pay. |
| `fact_collection_referral` | `collection_agency_id` | `dim_collection_agency` | 1:N | 1:many / always | many:1 / always | Many collection Referrals belong to one collection Agency, every collection Referral matches a collection Agency, and every collection Agency includes at least one collection Referral. |
| `fact_collection_referral` | `billing_account_id` | `dim_billing_account` | 1:N | 1:many / optional | many:1 / always | Many collection Referrals belong to one billing Account, every collection Referral matches a billing Account, and a billing Account may include no collection Referral. |
| `fact_collection_referral` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many collection Referrals belong to one calendar Day, every collection Referral matches a calendar Day, and a calendar Day may include no collection Referral. |
| `bridge_subscription_addon` | `subscription_id` | `dim_subscription` | 1:N | 1:many / optional | many:1 / always | Many subscription Add Ons belong to one subscription, every subscription Add On matches a subscription, and a subscription may include no subscription Add On. |
| `bridge_subscription_addon` | `addon_id` | `dim_addon` | 1:N | 1:many / always | many:1 / always | Many subscription Add Ons belong to one add On, every subscription Add On matches a add On, and every add On includes at least one subscription Add On. |
| `bridge_account_contact` | `billing_account_id` | `dim_billing_account` | 1:1 | 1:1 / always | 1:1 / always | Each account Contact matches exactly one billing Account, and each billing Account matches exactly one account Contact. Each billing account has one primary contact row. |
| `bridge_account_contact` | `contact_id` | `dim_contact` | 1:N | 1:many / optional | many:1 / always | Many account Contacts belong to one contact, every account Contact matches a contact, and a contact may include no account Contact. |
| `bridge_cell_neighbor` | `cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / always | Many cell Neighbors belong to one cell, every cell Neighbor matches a cell, and a cell may include no cell Neighbor. Source cell of the neighbor relation. |
| `bridge_neighbor_target` | `cell_neighbor_id` | `bridge_cell_neighbor` | 1:1 | 1:1 / always | 1:1 / always | Each neighbor Target matches exactly one cell Neighbor, and each cell Neighbor matches exactly one neighbor Target. Each neighbor relation has one target cell row. |
| `bridge_neighbor_target` | `neighbor_cell_id` | `dim_cell` | 1:N | 1:many / optional | many:1 / always | Many neighbor Targets belong to one cell, every neighbor Target matches a cell, and a cell may include no neighbor Target. Neighbor cell. |
| `bridge_plan_rating_group` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / always | many:1 / always | Many plan Rating Groups belong to one rate Plan, every plan Rating Group matches a rate Plan, and every rate Plan includes at least one plan Rating Group. |
| `bridge_plan_rating_group` | `rating_group_id` | `dim_rating_group` | 1:N | 1:many / always | many:1 / always | Many plan Rating Groups belong to one rating Group, every plan Rating Group matches a rating Group, and every rating Group includes at least one plan Rating Group. |
| `bridge_offering_price` | `product_offering_id` | `dim_product_offering` | 1:N | 1:many / always | many:1 / always | Many offering Prices belong to one product Offering, every offering Price matches a product Offering, and every product Offering includes at least one offering Price. |
| `bridge_offering_price` | `price_id` | `dim_price` | 1:1 | 1:1 / always | 1:1 / always | Each offering Price matches exactly one price, and each price matches exactly one offering Price. |
| `bridge_tariff_zone` | `tariff_id` | `dim_tariff` | 1:N | 1:many / always | many:1 / always | Many tariff Zones belong to one tariff, every tariff Zone matches a tariff, and every tariff includes at least one tariff Zone. |
| `bridge_tariff_zone` | `destination_zone_id` | `dim_destination_zone` | 1:N | 1:many / always | many:1 / always | Many tariff Zones belong to one destination Zone, every tariff Zone matches a destination Zone, and every destination Zone includes at least one tariff Zone. |
| `bridge_employee_queue` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many employee Queues belong to one employee, every employee Queue matches a employee, and a employee may include no employee Queue. |
| `bridge_employee_queue` | `queue_id` | `dim_queue` | 1:N | 1:many / always | many:1 / always | Many employee Queues belong to one care Queue, every employee Queue matches a care Queue, and every care Queue includes at least one employee Queue. |
| `bridge_partner_plmn` | `roaming_partner_id` | `dim_roaming_partner` | 1:N | 1:many / always | many:1 / always | Many partner PLMNs belong to one roaming Partner, every partner PLMN matches a roaming Partner, and every roaming Partner includes at least one partner PLMN. |
| `bridge_partner_plmn` | `plmn_id` | `dim_plmn` | 1:N | 1:many / optional | many:1 / always | Many partner PLMNs belong to one pLMN, every partner PLMN matches a pLMN, and a pLMN may include no partner PLMN. |
| `bridge_device_capability` | `device_model_id` | `dim_device_model` | 1:N | 1:many / always | many:1 / always | Many device Capabilities belong to one device Model, every device Capability matches a device Model, and every device Model includes at least one device Capability. |
| `bridge_device_capability` | `technology_id` | `dim_technology` | 1:N | 1:many / always | many:1 / always | Many device Capabilities belong to one technology, every device Capability matches a technology, and every technology includes at least one device Capability. |
| `bridge_subscriber_party` | `subscriber_id` | `dim_subscriber` | 1:1 | 1:1 / always | 1:1 / always | Each subscriber Party matches exactly one subscriber, and each subscriber matches exactly one subscriber Party. Each subscriber has one owning-party row. |
| `bridge_subscriber_party` | `party_id` | `dim_party` | 1:N | 1:many / optional | many:1 / always | Many subscriber Parties belong to one party, every subscriber Party matches a party, and a party may include no subscriber Party. |
| `bridge_trunk_prefix` | `interconnect_trunk_id` | `dim_interconnect_trunk` | 1:N | 1:many / always | many:1 / always | Many trunk Prefixes belong to one interconnect Trunk, every trunk Prefix matches a interconnect Trunk, and every interconnect Trunk includes at least one trunk Prefix. |
| `bridge_trunk_prefix` | `number_prefix_id` | `dim_number_prefix` | 1:N | 1:many / optional | many:1 / always | Many trunk Prefixes belong to one number Prefix, every trunk Prefix matches a number Prefix, and a number Prefix may include no trunk Prefix. |
| `bridge_agent_skill` | `agent_id` | `dim_agent` | 1:N | 1:many / optional | many:1 / always | Many agent Skills belong to one care Agent, every agent Skill matches a care Agent, and a care Agent may include no agent Skill. |
| `bridge_agent_skill` | `trouble_code_id` | `dim_trouble_code` | 1:N | 1:many / optional | many:1 / always | Many agent Skills belong to one trouble Code, every agent Skill matches a trouble Code, and a trouble Code may include no agent Skill. |
| `bridge_market_channel` | `market_id` | `dim_market` | 1:N | 1:many / always | many:1 / always | Many market Channels belong to one market, every market Channel matches a market, and every market includes at least one market Channel. |
| `bridge_market_channel` | `channel_id` | `dim_channel` | 1:N | 1:many / always | many:1 / always | Many market Channels belong to one channel, every market Channel matches a channel, and every channel includes at least one market Channel. |
| `bridge_dealer_plan` | `dealer_id` | `dim_dealer` | 1:N | 1:many / always | many:1 / always | Many dealer Plans belong to one dealer, every dealer Plan matches a dealer, and every dealer includes at least one dealer Plan. |
| `bridge_dealer_plan` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / optional | many:1 / always | Many dealer Plans belong to one rate Plan, every dealer Plan matches a rate Plan, and a rate Plan may include no dealer Plan. |
| `bridge_cell_spectrum` | `cell_id` | `dim_cell` | 1:N | 1:many / always | many:1 / always | Many cell Spectrums belong to one cell, every cell Spectrum matches a cell, and every cell includes at least one cell Spectrum. |
| `bridge_cell_spectrum` | `spectrum_band_id` | `dim_cell_band` | 1:N | 1:many / always | many:1 / always | Many cell Spectrums belong to one spectrum Band, every cell Spectrum matches a spectrum Band, and every spectrum Band includes at least one cell Spectrum. |
| `bridge_policy_apn` | `policy_rule_id` | `dim_policy_rule` | 1:N | 1:many / always | many:1 / always | Many policy APNs belong to one policy Rule, every policy APN matches a policy Rule, and every policy Rule includes at least one policy APN. |
| `bridge_policy_apn` | `apn_id` | `dim_apn` | 1:N | 1:many / optional | many:1 / always | Many policy APNs belong to one aPN DNN, every policy APN matches a aPN DNN, and a aPN DNN may include no policy APN. |
| `bridge_roaming_zone` | `roaming_partner_id` | `dim_roaming_partner` | 1:N | 1:many / always | many:1 / always | Many roaming Zones belong to one roaming Partner, every roaming Zone matches a roaming Partner, and every roaming Partner includes at least one roaming Zone. |
| `bridge_roaming_zone` | `destination_zone_id` | `dim_destination_zone` | 1:N | 1:many / optional | many:1 / always | Many roaming Zones belong to one destination Zone, every roaming Zone matches a destination Zone, and a destination Zone may include no roaming Zone. |
| `bridge_content_rating` | `content_provider_id` | `dim_content_provider` | 1:N | 1:many / always | many:1 / always | Many content Ratings belong to one content Provider, every content Rating matches a content Provider, and every content Provider includes at least one content Rating. |
| `bridge_content_rating` | `rating_group_id` | `dim_rating_group` | 1:N | 1:many / optional | many:1 / always | Many content Ratings belong to one rating Group, every content Rating matches a rating Group, and a rating Group may include no content Rating. |
| `bridge_prefix_zone` | `number_prefix_id` | `dim_number_prefix` | 1:1 | 1:1 / always | 1:1 / always | Each prefix Zone matches exactly one number Prefix, and each number Prefix matches exactly one prefix Zone. |
| `bridge_prefix_zone` | `destination_zone_id` | `dim_destination_zone` | 1:N | 1:many / always | many:1 / always | Many prefix Zones belong to one destination Zone, every prefix Zone matches a destination Zone, and every destination Zone includes at least one prefix Zone. |
| `bridge_party_address` | `party_id` | `dim_party` | 1:N | 1:many / optional | many:1 / always | Many party Addresses belong to one party, every party Address matches a party, and a party may include no party Address. |
| `bridge_party_address` | `address_id` | `dim_address` | 1:1 | 1:1 / always | 1:1 / always | Each party Address matches exactly one address, and each address matches exactly one party Address. Each address is linked once. |
| `bridge_workgroup_employee` | `employee_id` | `dim_employee` | 1:1 | 1:1 / always | 1:1 / always | Each workgroup Employee matches exactly one employee, and each employee matches exactly one workgroup Employee. |
| `bridge_workgroup_employee` | `workgroup_id` | `dim_workgroup` | 1:N | 1:many / always | many:1 / always | Many workgroup Employees belong to one workgroup, every workgroup Employee matches a workgroup, and every workgroup includes at least one workgroup Employee. |
| `bridge_campaign_plan` | `campaign_id` | `dim_campaign` | 1:N | 1:many / always | many:1 / always | Many campaign Plans belong to one campaign, every campaign Plan matches a campaign, and every campaign includes at least one campaign Plan. |
| `bridge_campaign_plan` | `rate_plan_id` | `dim_rate_plan` | 1:N | 1:many / optional | many:1 / always | Many campaign Plans belong to one rate Plan, every campaign Plan matches a rate Plan, and a rate Plan may include no campaign Plan. |
| `bridge_slice_qos` | `slice_id` | `dim_slice` | 1:N | 1:many / always | many:1 / always | Many slice QoSs belong to one network Slice, every slice QoS matches a network Slice, and every network Slice includes at least one slice QoS. |
| `bridge_slice_qos` | `qos_id` | `dim_qos` | 1:N | 1:many / optional | many:1 / always | Many slice QoSs belong to one qoS Profile, every slice QoS matches a qoS Profile, and a qoS Profile may include no slice QoS. |

## Dataset inventory

### billing

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_invoice` | fact | `invoice_id` | One invoice for one billing account in the window. |
| `fact_invoice_line` | fact | `invoice_line_id` | One charge line on an invoice. |
| `fact_tax_line` | fact | `tax_line_id` | One tax amount on an invoice. |
| `fact_document` | fact | `document_id` | One rendered document for an invoice. |
| `fact_payment` | fact | `payment_id` | One payment posted to a billing account. |
| `fact_adjustment` | fact | `adjustment_id` | One adjustment on a billing account. |
| `fact_dunning_event` | fact | `dunning_event_id` | One collections action on a billing account. |
| `fact_credit_note` | fact | `credit_note_id` | One credit note against an invoice. |
| `fact_topup` | fact | `topup_id` | One prepaid top-up. |
| `fact_refund` | fact | `refund_id` | One refund of a payment. |
| `fact_bundle_snapshot` | fact | `bundle_snapshot_id` | Month-end allowance position of one subscription. |
| `fact_promise_to_pay` | fact | `promise_to_pay_id` | One promise-to-pay on a billing account. |
| `fact_collection_referral` | fact | `collection_referral_id` | One referral of an account to a collection agency. |

### bridge

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `bridge_subscription_addon` | bridge | `subscription_addon_id` | One add-on attached to a subscription. |
| `bridge_account_contact` | bridge | `account_contact_id` | One contact designated for a billing account. |
| `bridge_cell_neighbor` | bridge | `cell_neighbor_id` | One neighbor relation from a source cell. |
| `bridge_neighbor_target` | bridge | `neighbor_target_id` | Neighbor cell of one neighbor relation. |
| `bridge_plan_rating_group` | bridge | `plan_rating_group_id` | Rating groups valid on a rate plan. |
| `bridge_offering_price` | bridge | `offering_price_id` | Price assigned to a product offering. |
| `bridge_tariff_zone` | bridge | `tariff_zone_id` | Destination zone priced by a tariff. |
| `bridge_employee_queue` | bridge | `employee_queue_id` | Care queue an employee can serve. |
| `bridge_partner_plmn` | bridge | `partner_plmn_id` | PLMN operated by a roaming partner. |
| `bridge_device_capability` | bridge | `device_capability_id` | Technology a device model supports. |
| `bridge_subscriber_party` | bridge | `subscriber_party_id` | Party that owns a subscriber. |
| `bridge_trunk_prefix` | bridge | `trunk_prefix_id` | Number prefix routed over a trunk. |
| `bridge_agent_skill` | bridge | `agent_skill_id` | Trouble code a care agent can handle. |
| `bridge_market_channel` | bridge | `market_channel_id` | Channel enabled in a market. |
| `bridge_dealer_plan` | bridge | `dealer_plan_id` | Rate plan a dealer is allowed to sell. |
| `bridge_cell_spectrum` | bridge | `cell_spectrum_id` | Spectrum band configured on a cell. |
| `bridge_policy_apn` | bridge | `policy_apn_id` | APN a policy rule can govern. |
| `bridge_roaming_zone` | bridge | `roaming_zone_id` | Destination zone agreed with a roaming partner. |
| `bridge_content_rating` | bridge | `content_rating_id` | Rating group used for a content provider. |
| `bridge_prefix_zone` | bridge | `prefix_zone_id` | Destination zone of a number prefix. |
| `bridge_party_address` | bridge | `party_address_id` | Address linked to a party. |
| `bridge_workgroup_employee` | bridge | `workgroup_employee_id` | Membership of an employee in a workgroup. |
| `bridge_campaign_plan` | bridge | `campaign_plan_id` | Rate plan promoted by a campaign. |
| `bridge_slice_qos` | bridge | `slice_qos_id` | QoS profile allowed on a slice. |

### care

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_sla` | dimension | `sla_id` | Care or network service level. |
| `dim_script` | dimension | `script_id` | Script a care agent follows. |
| `dim_care_reason` | dimension | `care_reason_id` | Reason recorded on a care interaction. |
| `dim_fraud_rule` | dimension | `fraud_rule_id` | Rule that raises a fraud alert. |
| `dim_agent` | dimension | `agent_id` | Care employee who handles interactions. |
| `dim_queue` | dimension | `queue_id` | Queue that receives care interactions. |
| `dim_trouble_code` | dimension | `trouble_code_id` | Code that classifies a trouble ticket. |
| `dim_collection_agency` | dimension | `collection_agency_id` | External agency that can receive a referral. |
| `fact_interaction` | fact | `interaction_id` | One care contact with a party. |
| `fact_trouble_ticket` | fact | `trouble_ticket_id` | One customer trouble ticket. |
| `fact_ticket_event` | fact | `ticket_event_id` | One status or work event on a trouble ticket. |
| `fact_dealer_sale` | fact | `dealer_sale_id` | One sale recorded by a dealer. |
| `fact_fraud_alert` | fact | `fraud_alert_id` | One fraud alert on a subscriber. |
| `fact_barring_event` | fact | `barring_event_id` | One barring change on a subscriber. |
| `fact_sla_breach` | fact | `sla_breach_id` | One breach of a care or network SLA. |
| `fact_campaign_contact` | fact | `campaign_contact_id` | One outbound campaign contact. |

### charging

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_charging_event` | fact | `charging_event_id` | One online charging event sent toward the charging function. |
| `fact_balance_reservation` | fact | `balance_reservation_id` | One quota reservation against a charging event. |
| `fact_balance_debit` | fact | `balance_debit_id` | One debit that consumes a reservation. |
| `fact_rated_charge` | fact | `rated_charge_id` | One rated usage charge produced from a mediated CDR. |
| `fact_policy_event` | fact | `policy_event_id` | One policy-control decision for a session. |
| `fact_allowance_draw` | fact | `allowance_draw_id` | One draw against an included allowance. |
| `fact_rerate` | fact | `rerate_id` | One rerate of a rated charge. |

### finance

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_gl_account` | dimension | `gl_account_id` | General-ledger account. |
| `dim_accounting_period` | dimension | `accounting_period_id` | Open accounting period covering the statistics window. |
| `dim_tax_jurisdiction` | dimension | `tax_jurisdiction_id` | Tax authority that can apply to a charge. |
| `dim_bank` | dimension | `bank_id` | Bank that settles a payment or interconnect invoice. |
| `dim_cost_element` | dimension | `cost_element_id` | Cost element inside a cost center. |
| `fact_journal_line` | fact | `journal_line_id` | One subledger journal line. |

### mediation

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_mediation_file` | fact | `mediation_file_id` | One CDR file emitted by a network element on one day. |
| `fact_mediation_reject` | fact | `mediation_reject_id` | One CDR rejected by mediation. |
| `fact_duplicate_suspect` | fact | `duplicate_suspect_id` | One CDR flagged as a possible duplicate. |

### network

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_plmn` | dimension | `plmn_id` | Public land mobile network, home or visited. |
| `dim_imsi` | dimension | `imsi_id` | International mobile subscriber identity. |
| `dim_roaming_partner` | dimension | `roaming_partner_id` | Operator that exchanges roaming usage. |
| `dim_tac` | dimension | `tac_id` | Tracking area that groups cells. |
| `dim_location_area` | dimension | `location_area_id` | Location area used by mobility updates. |
| `dim_recording_entity` | dimension | `recording_entity_id` | Network function that closes CDRs. |
| `dim_cell_site` | dimension | `cell_site_id` | Physical site that holds one or more cells. |
| `dim_cell` | dimension | `cell_id` | Sector or cell that serves a session. |
| `dim_network_element` | dimension | `network_element_id` | Switch, gateway, or function that records usage. |
| `dim_slice` | dimension | `slice_id` | 5G network slice. |
| `dim_mediation_rule` | dimension | `mediation_rule_id` | Rule that accepts or rejects a CDR. |
| `dim_policy_rule` | dimension | `policy_rule_id` | PCF or PCRF rule. |
| `dim_carrier` | dimension | `carrier_id` | Carrier that invoices interconnection. |
| `dim_interconnect_trunk` | dimension | `interconnect_trunk_id` | Trunk group toward an interconnect carrier. |
| `dim_resource` | dimension | `resource_id` | Network resource assigned to a service, SIM, or device. |
| `fact_cell_counter` | fact | `cell_counter_id` | One 15-minute counter snapshot for one cell. |
| `fact_outage_ticket` | fact | `outage_ticket_id` | One network outage ticket. |
| `fact_network_alarm` | fact | `network_alarm_id` | One alarm raised by a network element. |
| `fact_counter_breach` | fact | `counter_breach_id` | One threshold breach on a cell-counter snapshot. |

### organization

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_enterprise` | dimension | `enterprise_id` | The mobile operator as one company. |
| `dim_legal_entity` | dimension | `legal_entity_id` | Incorporated carrier entity that owns markets and the ledger. |
| `dim_region` | dimension | `region_id` | Operating region inside a legal entity. |
| `dim_department` | dimension | `department_id` | Organizational department. |
| `dim_cost_center` | dimension | `cost_center_id` | Cost center that collects labor and network cost. |
| `dim_employee` | dimension | `employee_id` | Employee of the operator. |
| `dim_market` | dimension | `market_id` | Geographic market that contains cell sites and accounts. |
| `dim_dealer` | dimension | `dealer_id` | Retail dealer that can sell a subscription. |
| `dim_workgroup` | dimension | `workgroup_id` | Care or field workgroup inside a department. |

### party

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_address` | dimension | `address_id` | Postal or site address. |
| `dim_party` | dimension | `party_id` | Person or organization that can hold an account. |
| `dim_billing_account` | dimension | `billing_account_id` | Account that receives one invoice in the window. |
| `dim_subscriber` | dimension | `subscriber_id` | Person or device identity that uses the network. |
| `dim_msisdn` | dimension | `msisdn_id` | MSISDN that can be assigned to a subscription. |
| `dim_subscription` | dimension | `subscription_id` | Contracted service that rates usage. |
| `dim_sim` | dimension | `sim_id` | SIM or eSIM profile. |
| `dim_device` | dimension | `device_id` | Handset or module seen on the network. |
| `dim_contact` | dimension | `contact_id` | Phone, email, or postal contact for a party. |
| `dim_np_operator` | dimension | `np_operator_id` | Operator on the other side of a number port. |
| `fact_number_port` | fact | `number_port_id` | One number-portability event. |
| `fact_sim_swap` | fact | `sim_swap_id` | One SIM replacement on a subscriber. |
| `fact_subscriber_snapshot` | fact | `subscriber_snapshot_id` | Month-end status of one subscriber. |

### product

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_cell_band` | dimension | `cell_band_id` | Radio band a cell can use. |
| `dim_vendor` | dimension | `vendor_id` | Network or device vendor. |
| `dim_device_model` | dimension | `device_model_id` | Handset or CPE model. |
| `dim_product_spec` | dimension | `product_spec_id` | Technical product specification. |
| `dim_product_offering` | dimension | `product_offering_id` | Sellable offering built on a product spec. |
| `dim_rate_plan` | dimension | `rate_plan_id` | Price plan assigned to subscriptions. |
| `dim_addon` | dimension | `addon_id` | Optional product attached to a subscription. |
| `dim_price` | dimension | `price_id` | Price point of an offering. |
| `dim_discount` | dimension | `discount_id` | Discount that can apply to a rate plan. |
| `dim_tariff` | dimension | `tariff_id` | Usage tariff for a zone and charge type. |
| `dim_tax_code` | dimension | `tax_code_id` | Tax treatment of a charge. |
| `dim_rating_group` | dimension | `rating_group_id` | Online-charging rating group. |
| `dim_content_provider` | dimension | `content_provider_id` | Provider of a charged content event. |
| `dim_service` | dimension | `service_id` | Customer-facing service instance for a subscription. |
| `dim_campaign` | dimension | `campaign_id` | Acquisition or retention campaign. |

### reference

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_channel` | dimension | `channel_id` | Sales or care channel. |
| `dim_currency` | dimension | `currency_id` | ISO currency used for charges and invoices. |
| `dim_technology` | dimension | `technology_id` | Radio access technology. |
| `dim_call_type` | dimension | `call_type_id` | Usage class on a CDR. |
| `dim_record_type` | dimension | `record_type_id` | 3GPP CDR or event type. |
| `dim_time_band` | dimension | `time_band_id` | Peak or off-peak band used by a tariff. |
| `dim_charge_type` | dimension | `charge_type_id` | Class of a rated or invoice charge. |
| `dim_balance_type` | dimension | `balance_type_id` | Prepaid or allowance balance that charging can touch. |
| `dim_dunning_level` | dimension | `dunning_level_id` | Collections stage of a billing account. |
| `dim_payment_method` | dimension | `payment_method_id` | How a payment or top-up was tendered. |
| `dim_adjustment_reason` | dimension | `adjustment_reason_id` | Why a balance or invoice was adjusted. |
| `dim_barring` | dimension | `barring_id` | Service bar that can be applied to a subscription. |
| `dim_handover_type` | dimension | `handover_type_id` | Mobility procedure that moved a session. |
| `dim_language` | dimension | `language_id` | Language of a bill or care contact. |
| `dim_segment` | dimension | `segment_id` | Marketing segment of a billing account. |
| `dim_credit_class` | dimension | `credit_class_id` | Credit treatment of a billing account. |
| `dim_bill_cycle` | dimension | `bill_cycle_id` | Monthly cycle that closes an account. |
| `dim_file_format` | dimension | `file_format_id` | CDR file format on the billing-domain transfer. |
| `dim_alarm_severity` | dimension | `alarm_severity_id` | Severity of a network alarm. |
| `dim_core_function` | dimension | `core_function_id` | 3GPP core function of a network element. |
| `dim_site_type` | dimension | `site_type_id` | Construction type of a cell site. |
| `dim_unit` | dimension | `unit_id` | Unit of a usage measure. |
| `dim_account_status` | dimension | `account_status_id` | Status of a billing account. |
| `dim_subscription_status` | dimension | `subscription_status_id` | Status of a subscription. |
| `dim_sale_type` | dimension | `sale_type_id` | How a dealer sale was classified. |
| `dim_journal_source` | dimension | `journal_source_id` | Subledger that produced a journal line. |
| `dim_document_type` | dimension | `document_type_id` | Kind of customer document. |
| `dim_qos` | dimension | `qos_id` | QoS profile applied to a session. |
| `dim_apn` | dimension | `apn_id` | Access point name or data network name. |
| `dim_destination_zone` | dimension | `destination_zone_id` | Rating zone for a called number or roaming partner. |
| `dim_allowance_bucket` | dimension | `allowance_bucket_id` | Included usage bucket on a plan. |
| `dim_country` | dimension | `country_id` | Country of an address, number, or partner. |
| `dim_calendar_day` | dimension | `calendar_day_id` | One day inside the 30-day statistics window. |
| `dim_release_cause` | dimension | `release_cause_id` | Cause that closed a session or call. |
| `dim_number_prefix` | dimension | `number_prefix_id` | Dialed or called-party prefix. |

### roaming

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_tap_out` | fact | `tap_out_id` | One outcollect roaming record sent to a partner. |
| `fact_tap_in` | fact | `tap_in_id` | One incollect roaming record received from a partner. |
| `fact_interconnect_invoice` | fact | `interconnect_invoice_id` | One interconnect invoice from a carrier. |
| `fact_settlement_line` | fact | `settlement_line_id` | One roaming settlement line with a partner. |

### usage

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_data_cdr` | fact | `data_cdr_id` | One closed or partial packet-data CDR transferred to billing. |
| `fact_voice_cdr` | fact | `voice_cdr_id` | One voice call detail record. |
| `fact_sms_cdr` | fact | `sms_cdr_id` | One short-message CDR. |
| `fact_content_cdr` | fact | `content_cdr_id` | One content or premium event CDR. |
| `fact_attach` | fact | `attach_id` | One registration or attach of a subscriber to the network. |
| `fact_handover` | fact | `handover_id` | One mobility handover between cells. |
| `fact_handover_target` | fact | `handover_target_id` | Target cell of one handover. Kept as its own dataset so source and target do not share one join to the cell population. |
| `fact_location_update` | fact | `location_update_id` | One location-update or tracking-area update. |
| `fact_qos_change` | fact | `qos_change_id` | One mid-session QoS change. |

## Provenance

Northline Mobile is a fictional operator. The mediated-CDR total of 2.1 billion rows in a 30-day window is the volume reported for one national operator's mediation pipeline (2.1 billion call detail records a month, covering voice, SMS, and data). CDR parameters, partial records, and the split between a CDR and a charging event follow 3GPP TS 32.298, TS 32.297, and TS 32.240. Shared business entities follow the TM Forum Information Framework (SID) at the level of party, product, service, and usage, without copying the SID model. Roaming interchange follows the GSMA TAP3 pattern of an outcollect and incollect usage record. Cell-counter grain is the Kimball periodic snapshot: one measurement per cell per 15-minute interval. The 85,000 cells and 28,000 sites are a synthetic national macro footprint, not an operator inventory. Online-charging volume is authored at three charging events per mediated CDR. No vendor DDL was copied.
