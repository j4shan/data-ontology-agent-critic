# Greenbasket Markets

Greenbasket Markets is a regional grocery chain selling food and household goods under one banner. Locations form a hierarchy of that banner, then regions, then districts, then storefronts. A storefront is the shop a customer enters. It carries a format, a price zone, a primary distribution center, and a status of open, remodel, or closed.

Two labor rules govern every storefront. Each storefront employs many cashiers, and each cashier belongs to exactly one storefront. A cashier is a till operator and a one-to-one specialization of an employee, with a status of active, training, or inactive. Each storefront has exactly one store manager, and an employee manages at most one storefront. Every storefront also employs one or more employees, and every employee is assigned to one storefront. Shifts, labor roles, punches, scheduled shifts, and drawer sessions describe coverage and till accountability.

Each storefront has many POS workstations. A workstation has a lane type and at most one payment terminal. A POS transaction is one basket rung at one storefront, by one cashier, on one workstation, in one channel, on one calendar day and hour. It may name a loyalty account, and its status is completed, voided, or suspended. A POS transaction has many item lines and many tenders. A line records the item, the quantity sold, and the extended amount, and it may cite a promotion. A tender records one payment against that basket. Discounts, coupons, and tax attach to the line and leave the transaction as the basket grain.

Merchandise runs from department to category to subcategory to item. A department is a merchandise department, not a store labor department. Each department has many categories, each category has many subcategories, and each subcategory has many items. An item is the SKU a storefront sells or produces. It may name a brand, it names a unit of measure, and its type is grocery, fresh, general merchandise, or private label. Assortment lists an item at a storefront. Price is held by price zone and day, and cost may cite a vendor, a storefront, or both. Promotions contain offers, coupons may cite an offer, and redemptions record use on a line or a basket.

Loyalty sits beside the basket. A household groups shoppers, and a customer may belong to one household. A loyalty account joins a customer to a program, and point postings may cite the causing POS transaction. A household visit is a trip header for a storefront, a day, and a channel, and it is distinct from the POS transaction.

Planograms describe shelf presentation. Every storefront has one or more aisles, and every aisle has one or more fixtures. A planogram may target a subcategory. Each position places an item and may name a fixture, and every planogram has at least one position. Compliance records whether a storefront matched the plan on a day.

Distribution centers replenish the storefronts. A warehouse in this catalog is a distribution center, and each vendor has one or more sites. Purchase orders, invoices, distribution center shipments, and store receipts are headers with one or more item lines. Inventory may sit at a storefront or a distribution center location, and either reference may be empty. Forecasts, replenishment, vendor fill, movements, and shrink connect demand to receipts and loss.

Fresh production happens in the storefront. A recipe points at the finished fresh item, an ingredient points at the component item, and every recipe uses one or more ingredients. A production batch records what a storefront made on a day, and a waste event records what was discarded.

Store e-commerce pickup uses the storefront as the fulfillment node. An order belongs to one customer and one storefront, names a fulfillment type, and may name a delivery slot. Status runs through placed, picking, ready, delivered, or cancelled. Every order has many lines, and every line has at least one pick task. Slot capacity limits orders for a slot on a day. A delivery records the handoff when the order leaves the store.

The catalog names these populations and the rules that relate them. Statistics are not authored. The model carries no row counts, distinct counts, or other measurements of population size.

## Data ecosystem

The authored catalog `retail-grocery` contains 110 datasets (50 dimensions, 48 facts, 12 bridges) in the Snowflake database `RETAIL_GROCERY` on account `greenbasket.us-central-1`.

Each dataset is one ontology node. The grain column is the system of record for that dataset's logical identity and is marked `is_entity_universe: true`. Foreign-key columns realize the same logical identity with `is_entity_universe: false`, because the child dataset does not hold the complete population. Edges join those two realizations. Multiplicity and match existence are directional and follow the operating rules below. Row counts, distinct counts, and other data statistics are intentionally absent.

## Signature relationships

| Relationship | Identity | Parent to child | Child to parent | Rule |
| --- | --- | --- | --- | --- |
| `dim_store` to `dim_cashier` | `store_identity` | 1:many (always) | many:1 (always) | Each storefront includes one or more cashiers, and each cashier belongs to exactly one storefront. |
| `dim_employee` to `dim_store` | `employee_identity` | 1:1 (optional) | 1:1 (always) | Each storefront has exactly one manager, and an employee manages at most one storefront. |
| `dim_store` to `dim_workstation` | `store_identity` | 1:many (always) | many:1 (always) | Each storefront has one or more POS workstations, and each workstation belongs to exactly one storefront. |
| `dim_region` to `dim_district` | `region_identity` | 1:many (always) | many:1 (always) | Each region contains one or more districts, and each district belongs to exactly one region. |
| `dim_district` to `dim_store` | `district_identity` | 1:many (always) | many:1 (always) | Each district contains one or more storefronts, and each storefront belongs to exactly one district. |
| `fact_pos_transaction` to `fact_pos_line` | `pos_transaction_identity` | 1:many (always) | many:1 (always) | Each POS transaction has one or more item lines, and each line belongs to exactly one transaction. |
| `fact_pos_transaction` to `fact_pos_tender` | `pos_transaction_identity` | 1:many (always) | many:1 (always) | Each POS transaction has one or more tenders, and each tender belongs to exactly one transaction. |
| `dim_department` to `dim_category` | `department_identity` | 1:many (always) | many:1 (always) | Each merchandise department contains one or more categories, and each category belongs to exactly one department. |
| `dim_category` to `dim_subcategory` | `category_identity` | 1:many (always) | many:1 (always) | Each category contains one or more subcategories, and each subcategory belongs to exactly one category. |
| `fact_ecommerce_order` to `fact_ecommerce_order_line` | `ecommerce_order_identity` | 1:many (always) | many:1 (always) | Each e-commerce order has one or more lines, and each line belongs to exactly one order. |
| `dim_aisle` to `dim_fixture` | `aisle_identity` | 1:many (always) | many:1 (always) | Each aisle contains one or more fixtures, and each fixture belongs to exactly one aisle. |
| `dim_vendor` to `dim_vendor_site` | `vendor_identity` | 1:many (always) | many:1 (always) | Each vendor has one or more sites, and each site belongs to exactly one vendor. |

## Relationship rules

| Child dataset | Column | Universe dataset | Mapping | Parent match | Child match | Rule |
| --- | --- | --- | --- | --- | --- | --- |
| `dim_region` | `banner_id` | `dim_banner` | 1:N | 1:many / always | many:1 / always | Each banner contains one or more regions, and each region belongs to exactly one banner. |
| `dim_district` | `region_id` | `dim_region` | 1:N | 1:many / always | many:1 / always | Each region contains one or more districts, and each district belongs to exactly one region. |
| `dim_store` | `district_id` | `dim_district` | 1:N | 1:many / always | many:1 / always | Each district contains one or more storefronts, and each storefront belongs to exactly one district. |
| `dim_store` | `banner_id` | `dim_banner` | 1:N | 1:many / optional | many:1 / always | Each storefront belongs to exactly one banner, and a banner may have no storefront on this reference. |
| `dim_store` | `store_format_id` | `dim_store_format` | 1:N | 1:many / optional | many:1 / always | Each storefront uses exactly one store format, and a format may be assigned to no storefront. |
| `dim_store` | `price_zone_id` | `dim_price_zone` | 1:N | 1:many / optional | many:1 / always | Each storefront belongs to exactly one price zone, and a price zone may contain no storefront. |
| `dim_store` | `manager_employee_id` | `dim_employee` | 1:1 | 1:1 / optional | 1:1 / always | Each storefront has exactly one manager, and an employee manages at most one storefront. |
| `dim_store` | `primary_warehouse_id` | `dim_warehouse` | 1:N | 1:many / optional | many:1 / always | Each storefront names exactly one primary distribution center, and a distribution center may be primary for no storefront. |
| `dim_category` | `department_id` | `dim_department` | 1:N | 1:many / always | many:1 / always | Each merchandise department contains one or more categories, and each category belongs to exactly one department. |
| `dim_subcategory` | `category_id` | `dim_category` | 1:N | 1:many / always | many:1 / always | Each category contains one or more subcategories, and each subcategory belongs to exactly one category. |
| `dim_item` | `subcategory_id` | `dim_subcategory` | 1:N | 1:many / always | many:1 / always | Each subcategory contains one or more items, and each item belongs to exactly one subcategory. |
| `dim_item` | `brand_id` | `dim_brand` | 1:N | 1:many / optional | many:1 / optional | An item may omit a brand, and a brand may be named on no item. |
| `dim_item` | `uom_id` | `dim_unit_of_measure` | 1:N | 1:many / optional | many:1 / always | Each item uses exactly one unit of measure, and a unit of measure may be unused. |
| `dim_vendor_site` | `vendor_id` | `dim_vendor` | 1:N | 1:many / always | many:1 / always | Each vendor has one or more sites, and each site belongs to exactly one vendor. |
| `dim_employee` | `store_id` | `dim_store` | 1:N | 1:many / always | many:1 / always | Every storefront employs one or more employees, and every employee is assigned to one storefront. |
| `dim_employee` | `department_id` | `dim_department` | 1:N | 1:many / optional | many:1 / optional | An employee may omit a merchandise department, and a merchandise department may have no employees. |
| `dim_cashier` | `employee_id` | `dim_employee` | 1:1 | 1:1 / optional | 1:1 / always | Each cashier is exactly one employee, and an employee is at most one cashier. |
| `dim_cashier` | `store_id` | `dim_store` | 1:N | 1:many / always | many:1 / always | Each storefront includes one or more cashiers, and each cashier belongs to exactly one storefront. |
| `dim_shift` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each shift belongs to exactly one storefront, and a storefront may define no shift. |
| `dim_workstation` | `store_id` | `dim_store` | 1:N | 1:many / always | many:1 / always | Each storefront has one or more POS workstations, and each workstation belongs to exactly one storefront. |
| `dim_workstation` | `lane_type_id` | `dim_lane_type` | 1:N | 1:many / optional | many:1 / always | Each workstation uses exactly one lane type, and a lane type may be unused. |
| `dim_payment_terminal` | `workstation_id` | `dim_workstation` | 1:1 | 1:1 / optional | 1:1 / always | Each payment terminal belongs to exactly one workstation, and a workstation has at most one payment terminal. |
| `dim_offer` | `promotion_id` | `dim_promotion` | 1:N | 1:many / always | many:1 / always | Each promotion includes one or more offers, and each offer belongs to exactly one promotion. |
| `dim_coupon` | `offer_id` | `dim_offer` | 1:N | 1:many / optional | many:1 / optional | A coupon may omit an offer, and an offer may have no coupon. |
| `dim_customer` | `household_id` | `dim_household` | 1:N | 1:many / optional | many:1 / optional | A customer may omit a household, and a household may have no customer on this reference. |
| `dim_loyalty_account` | `loyalty_program_id` | `dim_loyalty_program` | 1:N | 1:many / optional | many:1 / always | Each loyalty account belongs to exactly one program, and a program may have no account. |
| `dim_loyalty_account` | `customer_id` | `dim_customer` | 1:N | 1:many / optional | many:1 / always | Each loyalty account belongs to exactly one customer, and a customer may hold no loyalty account. |
| `dim_aisle` | `store_id` | `dim_store` | 1:N | 1:many / always | many:1 / always | Each storefront contains one or more aisles, and each aisle belongs to exactly one storefront. |
| `dim_fixture` | `aisle_id` | `dim_aisle` | 1:N | 1:many / always | many:1 / always | Each aisle contains one or more fixtures, and each fixture belongs to exactly one aisle. |
| `dim_planogram` | `subcategory_id` | `dim_subcategory` | 1:N | 1:many / optional | many:1 / optional | A planogram may omit a subcategory, and a subcategory may have no planogram. |
| `dim_dc_location` | `warehouse_id` | `dim_warehouse` | 1:N | 1:many / always | many:1 / always | Each distribution center has one or more locations, and each location belongs to exactly one distribution center. |
| `dim_recipe` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each recipe produces exactly one finished item, and an item may have no recipe. |
| `dim_ingredient` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each ingredient is exactly one item, and an item may have no ingredient row. |
| `dim_delivery_slot` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each delivery slot belongs to exactly one storefront, and a storefront may offer no slot. |
| `bridge_item_store` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each assortment row lists exactly one item, and an item may be listed at no storefront. |
| `bridge_item_store` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each assortment row names exactly one storefront, and a storefront may have no assortment row. |
| `bridge_item_vendor` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each source row names exactly one item, and an item may have no vendor source. |
| `bridge_item_vendor` | `vendor_id` | `dim_vendor` | 1:N | 1:many / optional | many:1 / always | Each source row names exactly one vendor, and a vendor may supply no item on this bridge. |
| `bridge_item_vendor` | `vendor_site_id` | `dim_vendor_site` | 1:N | 1:many / optional | many:1 / optional | A source row may omit a vendor site, and a vendor site may supply no item on this bridge. |
| `bridge_promotion_item` | `promotion_id` | `dim_promotion` | 1:N | 1:many / optional | many:1 / always | Each eligibility row names exactly one promotion, and a promotion may include no item on this bridge. |
| `bridge_promotion_item` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each eligibility row names exactly one item, and an item may be on no promotion. |
| `bridge_promotion_store` | `promotion_id` | `dim_promotion` | 1:N | 1:many / optional | many:1 / always | Each offer row names exactly one promotion, and a promotion may be offered at no storefront. |
| `bridge_promotion_store` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each offer row names exactly one storefront, and a storefront may run no promotion. |
| `bridge_planogram_position` | `planogram_id` | `dim_planogram` | 1:N | 1:many / always | many:1 / always | Each planogram has one or more positions, and each position belongs to exactly one planogram. |
| `bridge_planogram_position` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each position places exactly one item, and an item may occupy no planogram position. |
| `bridge_planogram_position` | `fixture_id` | `dim_fixture` | 1:N | 1:many / optional | many:1 / optional | A position may omit a fixture, and a fixture may hold no planogram position. |
| `bridge_coupon_item` | `coupon_id` | `dim_coupon` | 1:N | 1:many / optional | many:1 / always | Each link names exactly one coupon, and a coupon may apply to no item. |
| `bridge_coupon_item` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each link names exactly one item, and an item may be on no coupon. |
| `bridge_recipe_ingredient` | `recipe_id` | `dim_recipe` | 1:N | 1:many / always | many:1 / always | Each recipe uses one or more ingredients, and each use belongs to exactly one recipe. |
| `bridge_recipe_ingredient` | `ingredient_id` | `dim_ingredient` | 1:N | 1:many / optional | many:1 / always | Each use names exactly one ingredient, and an ingredient may be used by no recipe. |
| `bridge_employee_role` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Each assignment names exactly one employee, and an employee may hold no labor role. |
| `bridge_employee_role` | `labor_role_id` | `dim_labor_role` | 1:N | 1:many / optional | many:1 / always | Each assignment names exactly one labor role, and a labor role may be assigned to no employee. |
| `bridge_item_tax` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each applicability row names exactly one item, and an item may have no tax jurisdiction. |
| `bridge_item_tax` | `tax_jurisdiction_id` | `dim_tax_jurisdiction` | 1:N | 1:many / optional | many:1 / always | Each applicability row names exactly one jurisdiction, and a jurisdiction may tax no item. |
| `bridge_store_competitor` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each pairing names exactly one storefront, and a storefront may have no tracked competitor. |
| `bridge_store_competitor` | `competitor_id` | `dim_competitor` | 1:N | 1:many / optional | many:1 / always | Each pairing names exactly one competitor, and a competitor may be tracked for no storefront. |
| `bridge_customer_segment` | `customer_id` | `dim_customer` | 1:N | 1:many / optional | many:1 / always | Each membership names exactly one customer, and a customer may belong to no segment. |
| `bridge_customer_segment` | `segment_id` | `dim_customer_segment` | 1:N | 1:many / optional | many:1 / always | Each membership names exactly one segment, and a segment may have no member. |
| `bridge_offer_tender` | `offer_id` | `dim_offer` | 1:N | 1:many / optional | many:1 / always | Each eligibility row names exactly one offer, and an offer may accept no tender type. |
| `bridge_offer_tender` | `tender_type_id` | `dim_tender_type` | 1:N | 1:many / optional | many:1 / always | Each eligibility row names exactly one tender type, and a tender type may be accepted by no offer. |
| `fact_pos_transaction` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each transaction occurs at exactly one storefront, and a storefront may have no transaction. |
| `fact_pos_transaction` | `cashier_id` | `dim_cashier` | 1:N | 1:many / optional | many:1 / always | Each transaction is rung by exactly one cashier, and a cashier may ring no transaction. |
| `fact_pos_transaction` | `workstation_id` | `dim_workstation` | 1:N | 1:many / optional | many:1 / always | Each transaction is recorded on exactly one workstation, and a workstation may record no transaction. |
| `fact_pos_transaction` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each transaction occurs on exactly one calendar day, and a day may have no transaction. |
| `fact_pos_transaction` | `hour_id` | `dim_hour` | 1:N | 1:many / optional | many:1 / always | Each transaction occurs in exactly one hour, and an hour may have no transaction. |
| `fact_pos_transaction` | `channel_id` | `dim_channel` | 1:N | 1:many / optional | many:1 / always | Each transaction uses exactly one channel, and a channel may have no transaction. |
| `fact_pos_transaction` | `loyalty_account_id` | `dim_loyalty_account` | 1:N | 1:many / optional | many:1 / optional | A transaction may omit a loyalty account, and a loyalty account may appear on no transaction. |
| `fact_pos_line` | `pos_transaction_id` | `fact_pos_transaction` | 1:N | 1:many / always | many:1 / always | Each POS transaction has one or more item lines, and each line belongs to exactly one transaction. |
| `fact_pos_line` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each line sells exactly one item, and an item may appear on no line. |
| `fact_pos_line` | `uom_id` | `dim_unit_of_measure` | 1:N | 1:many / optional | many:1 / optional | A line may omit a selling unit of measure, and a unit of measure may appear on no line. |
| `fact_pos_line` | `promotion_id` | `dim_promotion` | 1:N | 1:many / optional | many:1 / optional | A line may omit a promotion, and a promotion may apply to no line. |
| `fact_pos_tender` | `pos_transaction_id` | `fact_pos_transaction` | 1:N | 1:many / always | many:1 / always | Each POS transaction has one or more tenders, and each tender belongs to exactly one transaction. |
| `fact_pos_tender` | `tender_type_id` | `dim_tender_type` | 1:N | 1:many / optional | many:1 / always | Each tender uses exactly one tender type, and a tender type may be used on no tender. |
| `fact_pos_discount` | `pos_line_id` | `fact_pos_line` | 1:N | 1:many / always | many:1 / always | Each POS line has one or more discounts, and each discount belongs to exactly one line. |
| `fact_pos_discount` | `offer_id` | `dim_offer` | 1:N | 1:many / optional | many:1 / optional | A discount may omit an offer, and an offer may grant no discount. |
| `fact_pos_discount` | `coupon_id` | `dim_coupon` | 1:N | 1:many / optional | many:1 / optional | A discount may omit a coupon, and a coupon may grant no discount. |
| `fact_transaction_tax` | `pos_line_id` | `fact_pos_line` | 1:N | 1:many / optional | many:1 / always | Each tax charge belongs to exactly one POS line, and a POS line may have no tax charge. |
| `fact_transaction_tax` | `tax_jurisdiction_id` | `dim_tax_jurisdiction` | 1:N | 1:many / optional | many:1 / always | Each tax charge names exactly one jurisdiction, and a jurisdiction may assess no charge. |
| `fact_cashier_drawer` | `cashier_id` | `dim_cashier` | 1:N | 1:many / optional | many:1 / always | Each drawer session is operated by exactly one cashier, and a cashier may have no drawer session. |
| `fact_cashier_drawer` | `workstation_id` | `dim_workstation` | 1:N | 1:many / optional | many:1 / always | Each drawer session uses exactly one workstation, and a workstation may have no drawer session. |
| `fact_cashier_drawer` | `shift_id` | `dim_shift` | 1:N | 1:many / optional | many:1 / always | Each drawer session belongs to exactly one shift, and a shift may have no drawer session. |
| `fact_cashier_drawer` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each drawer session occurs on exactly one day, and a day may have no drawer session. |
| `fact_labor_punch` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Each punch belongs to exactly one employee, and an employee may have no punch. |
| `fact_labor_punch` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each punch occurs at exactly one storefront, and a storefront may have no punch. |
| `fact_labor_punch` | `shift_id` | `dim_shift` | 1:N | 1:many / optional | many:1 / optional | A punch may omit a shift, and a shift may have no punch. |
| `fact_labor_punch` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each punch occurs on exactly one day, and a day may have no punch. |
| `fact_schedule_shift` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Each scheduled shift names exactly one employee, and an employee may have no scheduled shift. |
| `fact_schedule_shift` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each scheduled shift names exactly one storefront, and a storefront may have no scheduled shift. |
| `fact_schedule_shift` | `labor_role_id` | `dim_labor_role` | 1:N | 1:many / optional | many:1 / always | Each scheduled shift names exactly one labor role, and a labor role may be unscheduled. |
| `fact_schedule_shift` | `shift_id` | `dim_shift` | 1:N | 1:many / optional | many:1 / always | Each scheduled shift uses exactly one shift, and a shift may have no scheduled assignment. |
| `fact_schedule_shift` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each scheduled shift falls on exactly one day, and a day may have no scheduled shift. |
| `fact_retail_price` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each price names exactly one item, and an item may have no zone price. |
| `fact_retail_price` | `price_zone_id` | `dim_price_zone` | 1:N | 1:many / optional | many:1 / always | Each price names exactly one price zone, and a price zone may have no price row. |
| `fact_retail_price` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each price is effective on exactly one day, and a day may have no price row. |
| `fact_item_cost` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each cost names exactly one item, and an item may have no cost row. |
| `fact_item_cost` | `vendor_id` | `dim_vendor` | 1:N | 1:many / optional | many:1 / optional | A cost may omit a vendor, and a vendor may have no cost row. |
| `fact_item_cost` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / optional | A cost may omit a storefront, and a storefront may have no cost row. |
| `fact_inventory_position` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each position names exactly one item, and an item may have no position. |
| `fact_inventory_position` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / optional | A position may omit a storefront, and a storefront may have no inventory position. |
| `fact_inventory_position` | `dc_location_id` | `dim_dc_location` | 1:N | 1:many / optional | many:1 / optional | A position may omit a distribution-center location, and a location may have no inventory position. |
| `fact_inventory_movement` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each movement names exactly one item, and an item may have no movement. |
| `fact_inventory_movement` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / optional | A movement may omit a storefront, and a storefront may have no movement. |
| `fact_inventory_movement` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / always | Each movement names exactly one reason code, and a reason code may explain no movement. |
| `fact_inventory_movement` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each movement occurs on exactly one day, and a day may have no movement. |
| `fact_store_receipt` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each receipt arrives at exactly one storefront, and a storefront may have no receipt. |
| `fact_store_receipt` | `warehouse_id` | `dim_warehouse` | 1:N | 1:many / optional | many:1 / always | Each receipt comes from exactly one distribution center, and a distribution center may have no store receipt. |
| `fact_store_receipt` | `carrier_id` | `dim_carrier` | 1:N | 1:many / optional | many:1 / optional | A receipt may omit a carrier, and a carrier may deliver no store receipt. |
| `fact_store_receipt` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each receipt occurs on exactly one day, and a day may have no store receipt. |
| `fact_store_receipt_line` | `store_receipt_id` | `fact_store_receipt` | 1:N | 1:many / always | many:1 / always | Each store receipt has one or more lines, and each line belongs to exactly one receipt. |
| `fact_store_receipt_line` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each receipt line names exactly one item, and an item may appear on no receipt line. |
| `fact_dc_shipment` | `warehouse_id` | `dim_warehouse` | 1:N | 1:many / optional | many:1 / always | Each shipment leaves exactly one distribution center, and a distribution center may have no shipment. |
| `fact_dc_shipment` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each shipment is destined for exactly one storefront, and a storefront may have no shipment. |
| `fact_dc_shipment` | `carrier_id` | `dim_carrier` | 1:N | 1:many / optional | many:1 / optional | A shipment may omit a carrier, and a carrier may haul no shipment. |
| `fact_dc_shipment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each shipment is dispatched on exactly one day, and a day may have no shipment. |
| `fact_dc_shipment_line` | `dc_shipment_id` | `fact_dc_shipment` | 1:N | 1:many / always | many:1 / always | Each distribution-center shipment has one or more lines, and each line belongs to exactly one shipment. |
| `fact_dc_shipment_line` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each shipment line names exactly one item, and an item may appear on no shipment line. |
| `fact_dc_shipment_line` | `dc_location_id` | `dim_dc_location` | 1:N | 1:many / optional | many:1 / optional | A shipment line may omit a location, and a location may be picked on no shipment line. |
| `fact_purchase_order` | `vendor_id` | `dim_vendor` | 1:N | 1:many / optional | many:1 / always | Each purchase order names exactly one vendor, and a vendor may have no purchase order. |
| `fact_purchase_order` | `vendor_site_id` | `dim_vendor_site` | 1:N | 1:many / optional | many:1 / always | Each purchase order names exactly one vendor site, and a vendor site may have no purchase order. |
| `fact_purchase_order` | `warehouse_id` | `dim_warehouse` | 1:N | 1:many / optional | many:1 / always | Each purchase order is destined for exactly one distribution center, and a distribution center may have no purchase order. |
| `fact_purchase_order` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each purchase order uses exactly one currency, and a currency may be used on no purchase order. |
| `fact_purchase_order_line` | `purchase_order_id` | `fact_purchase_order` | 1:N | 1:many / always | many:1 / always | Each purchase order has one or more lines, and each line belongs to exactly one purchase order. |
| `fact_purchase_order_line` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each purchase-order line names exactly one item, and an item may appear on no purchase-order line. |
| `fact_purchase_order_line` | `uom_id` | `dim_unit_of_measure` | 1:N | 1:many / optional | many:1 / always | Each purchase-order line uses exactly one unit of measure, and a unit of measure may be unused on an order line. |
| `fact_vendor_invoice` | `vendor_id` | `dim_vendor` | 1:N | 1:many / optional | many:1 / always | Each invoice is issued by exactly one vendor, and a vendor may issue no invoice. |
| `fact_vendor_invoice` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each invoice uses exactly one currency, and a currency may be used on no invoice. |
| `fact_vendor_invoice` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each invoice is dated on exactly one day, and a day may have no invoice. |
| `fact_vendor_invoice_line` | `vendor_invoice_id` | `fact_vendor_invoice` | 1:N | 1:many / always | many:1 / always | Each vendor invoice has one or more lines, and each line belongs to exactly one invoice. |
| `fact_vendor_invoice_line` | `purchase_order_line_id` | `fact_purchase_order_line` | 1:N | 1:many / optional | many:1 / optional | An invoice line may omit a purchase-order line, and a purchase-order line may be unmatched by an invoice. |
| `fact_vendor_invoice_line` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / always | Each invoice line posts to exactly one general-ledger account, and an account may classify no invoice line. |
| `fact_promotion_redemption` | `promotion_id` | `dim_promotion` | 1:N | 1:many / optional | many:1 / always | Each redemption names exactly one promotion, and a promotion may have no redemption. |
| `fact_promotion_redemption` | `pos_line_id` | `fact_pos_line` | 1:N | 1:many / optional | many:1 / optional | A redemption may omit a POS line, and a POS line may have no promotion redemption. |
| `fact_promotion_redemption` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each redemption occurs at exactly one storefront, and a storefront may have no promotion redemption. |
| `fact_promotion_redemption` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each redemption occurs on exactly one day, and a day may have no promotion redemption. |
| `fact_coupon_redemption` | `coupon_id` | `dim_coupon` | 1:N | 1:many / optional | many:1 / always | Each redemption names exactly one coupon, and a coupon may have no redemption. |
| `fact_coupon_redemption` | `pos_transaction_id` | `fact_pos_transaction` | 1:N | 1:many / optional | many:1 / always | Each coupon redemption belongs to exactly one POS transaction, and a transaction may have no coupon redemption. |
| `fact_coupon_redemption` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each coupon redemption occurs at exactly one storefront, and a storefront may have no coupon redemption. |
| `fact_loyalty_accrual` | `loyalty_account_id` | `dim_loyalty_account` | 1:N | 1:many / optional | many:1 / always | Each accrual posts to exactly one loyalty account, and an account may have no accrual. |
| `fact_loyalty_accrual` | `pos_transaction_id` | `fact_pos_transaction` | 1:N | 1:many / optional | many:1 / optional | An accrual may omit a POS transaction, and a transaction may have no accrual. |
| `fact_loyalty_redemption` | `loyalty_account_id` | `dim_loyalty_account` | 1:N | 1:many / optional | many:1 / always | Each redemption draws from exactly one loyalty account, and an account may have no redemption. |
| `fact_loyalty_redemption` | `pos_transaction_id` | `fact_pos_transaction` | 1:N | 1:many / optional | many:1 / optional | A redemption may omit a POS transaction, and a transaction may have no loyalty redemption. |
| `fact_customer_return` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each return is accepted at exactly one storefront, and a storefront may have no return. |
| `fact_customer_return` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each return names exactly one item, and an item may have no return. |
| `fact_customer_return` | `pos_line_id` | `fact_pos_line` | 1:N | 1:many / optional | many:1 / optional | A return may omit the original POS line, and a POS line may have no return. |
| `fact_customer_return` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / always | Each return names exactly one reason code, and a reason code may explain no return. |
| `fact_customer_return` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each return occurs on exactly one day, and a day may have no return. |
| `fact_shrink_event` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each shrink event occurs at exactly one storefront, and a storefront may have no shrink event. |
| `fact_shrink_event` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each shrink event names exactly one item, and an item may have no shrink event. |
| `fact_shrink_event` | `shrink_reason_id` | `dim_shrink_reason` | 1:N | 1:many / optional | many:1 / always | Each shrink event names exactly one shrink reason, and a shrink reason may explain no event. |
| `fact_shrink_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each shrink event occurs on exactly one day, and a day may have no shrink event. |
| `fact_cycle_count` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / optional | A cycle count may omit a storefront, and a storefront may have no cycle count. |
| `fact_cycle_count` | `dc_location_id` | `dim_dc_location` | 1:N | 1:many / optional | many:1 / optional | A cycle count may omit a distribution-center location, and a location may have no cycle count. |
| `fact_cycle_count` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each cycle count names exactly one item, and an item may have no cycle count. |
| `fact_cycle_count` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Each cycle count is performed by exactly one employee, and an employee may perform no cycle count. |
| `fact_cycle_count` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each cycle count occurs on exactly one day, and a day may have no cycle count. |
| `fact_planogram_compliance` | `planogram_id` | `dim_planogram` | 1:N | 1:many / optional | many:1 / always | Each check evaluates exactly one planogram, and a planogram may have no compliance check. |
| `fact_planogram_compliance` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each check covers exactly one storefront, and a storefront may have no compliance check. |
| `fact_planogram_compliance` | `fixture_id` | `dim_fixture` | 1:N | 1:many / optional | many:1 / optional | A check may omit a fixture, and a fixture may have no compliance check. |
| `fact_planogram_compliance` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each check occurs on exactly one day, and a day may have no compliance check. |
| `fact_fresh_production` | `recipe_id` | `dim_recipe` | 1:N | 1:many / optional | many:1 / always | Each batch follows exactly one recipe, and a recipe may have no production batch. |
| `fact_fresh_production` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each batch is produced at exactly one storefront, and a storefront may have no production batch. |
| `fact_fresh_production` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each batch is produced on exactly one day, and a day may have no production batch. |
| `fact_markdown_event` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each markdown names exactly one item, and an item may have no markdown. |
| `fact_markdown_event` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each markdown occurs at exactly one storefront, and a storefront may have no markdown. |
| `fact_markdown_event` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / always | Each markdown names exactly one reason code, and a reason code may explain no markdown. |
| `fact_markdown_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each markdown occurs on exactly one day, and a day may have no markdown. |
| `fact_waste_event` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each waste event names exactly one item, and an item may have no waste event. |
| `fact_waste_event` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each waste event occurs at exactly one storefront, and a storefront may have no waste event. |
| `fact_waste_event` | `shrink_reason_id` | `dim_shrink_reason` | 1:N | 1:many / optional | many:1 / optional | A waste event may omit a shrink reason, and a shrink reason may explain no waste event. |
| `fact_waste_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each waste event occurs on exactly one day, and a day may have no waste event. |
| `fact_ecommerce_order` | `customer_id` | `dim_customer` | 1:N | 1:many / optional | many:1 / always | Each order is placed by exactly one customer, and a customer may place no order. |
| `fact_ecommerce_order` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each order is fulfilled by exactly one storefront, and a storefront may fulfill no order. |
| `fact_ecommerce_order` | `fulfillment_type_id` | `dim_fulfillment_type` | 1:N | 1:many / optional | many:1 / always | Each order uses exactly one fulfillment type, and a fulfillment type may be used on no order. |
| `fact_ecommerce_order` | `delivery_slot_id` | `dim_delivery_slot` | 1:N | 1:many / optional | many:1 / optional | An order may omit a delivery slot, and a delivery slot may be chosen on no order. |
| `fact_ecommerce_order` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each order is placed on exactly one day, and a day may have no order. |
| `fact_ecommerce_order_line` | `ecommerce_order_id` | `fact_ecommerce_order` | 1:N | 1:many / always | many:1 / always | Each e-commerce order has one or more lines, and each line belongs to exactly one order. |
| `fact_ecommerce_order_line` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each order line names exactly one item, and an item may appear on no order line. |
| `fact_pick_task` | `ecommerce_order_line_id` | `fact_ecommerce_order_line` | 1:N | 1:many / always | many:1 / always | Each e-commerce order line has one or more pick tasks, and each pick task belongs to exactly one order line. |
| `fact_pick_task` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A pick task may omit an employee, and an employee may have no pick task. |
| `fact_pick_task` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each pick task occurs at exactly one storefront, and a storefront may have no pick task. |
| `fact_delivery` | `ecommerce_order_id` | `fact_ecommerce_order` | 1:N | 1:many / optional | many:1 / always | Each delivery covers exactly one e-commerce order, and an order may have no delivery. |
| `fact_delivery` | `carrier_id` | `dim_carrier` | 1:N | 1:many / optional | many:1 / optional | A delivery may omit a carrier, and a carrier may haul no delivery. |
| `fact_delivery` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each delivery is dated on exactly one day, and a day may have no delivery. |
| `fact_slot_capacity` | `delivery_slot_id` | `dim_delivery_slot` | 1:N | 1:many / optional | many:1 / always | Each capacity row names exactly one delivery slot, and a slot may have no capacity row. |
| `fact_slot_capacity` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each capacity row names exactly one storefront, and a storefront may have no slot capacity. |
| `fact_slot_capacity` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each capacity row applies to exactly one day, and a day may have no slot capacity. |
| `fact_out_of_stock` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each observation names exactly one item, and an item may have no out-of-stock observation. |
| `fact_out_of_stock` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each observation names exactly one storefront, and a storefront may have no out-of-stock observation. |
| `fact_out_of_stock` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each observation occurs on exactly one day, and a day may have no out-of-stock observation. |
| `fact_out_of_stock` | `hour_id` | `dim_hour` | 1:N | 1:many / optional | many:1 / optional | An observation may omit an hour, and an hour may have no out-of-stock observation. |
| `fact_competitor_price` | `competitor_id` | `dim_competitor` | 1:N | 1:many / optional | many:1 / always | Each observation names exactly one competitor, and a competitor may have no price observation. |
| `fact_competitor_price` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each observation names exactly one item, and an item may have no competitor price. |
| `fact_competitor_price` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each observation is dated on exactly one day, and a day may have no competitor price. |
| `fact_demand_forecast` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each forecast names exactly one item, and an item may have no forecast. |
| `fact_demand_forecast` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each forecast names exactly one storefront, and a storefront may have no forecast. |
| `fact_demand_forecast` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each forecast applies to exactly one day, and a day may have no forecast. |
| `fact_replenishment_order` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each replenishment order names exactly one storefront, and a storefront may have no replenishment order. |
| `fact_replenishment_order` | `warehouse_id` | `dim_warehouse` | 1:N | 1:many / optional | many:1 / always | Each replenishment order names exactly one distribution center, and a distribution center may have no replenishment order. |
| `fact_replenishment_order` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each replenishment order names exactly one item, and an item may have no replenishment order. |
| `fact_replenishment_order` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each replenishment order is dated on exactly one day, and a day may have no replenishment order. |
| `fact_service_level` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Each observation names exactly one item, and an item may have no service-level observation. |
| `fact_service_level` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each observation names exactly one storefront, and a storefront may have no service-level observation. |
| `fact_service_level` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each observation occurs on exactly one day, and a day may have no service-level observation. |
| `fact_gift_card_txn` | `tender_type_id` | `dim_tender_type` | 1:N | 1:many / optional | many:1 / optional | A gift card transaction may omit a tender type, and a tender type may be used on no gift card transaction. |
| `fact_gift_card_txn` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each gift card transaction occurs at exactly one storefront, and a storefront may have no gift card transaction. |
| `fact_gift_card_txn` | `pos_transaction_id` | `fact_pos_transaction` | 1:N | 1:many / optional | many:1 / optional | A gift card transaction may omit a POS transaction, and a POS transaction may have no gift card activity. |
| `fact_cash_deposit` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each deposit comes from exactly one storefront, and a storefront may have no cash deposit. |
| `fact_cash_deposit` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each deposit occurs on exactly one day, and a day may have no cash deposit. |
| `fact_cash_deposit` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Each deposit is made by exactly one employee, and an employee may make no cash deposit. |
| `fact_utility_reading` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each reading belongs to exactly one storefront, and a storefront may have no utility reading. |
| `fact_utility_reading` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each reading is dated on exactly one day, and a day may have no utility reading. |
| `fact_customer_complaint` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each complaint concerns exactly one storefront, and a storefront may have no complaint. |
| `fact_customer_complaint` | `customer_id` | `dim_customer` | 1:N | 1:many / optional | many:1 / optional | A complaint may omit a customer, and a customer may file no complaint. |
| `fact_customer_complaint` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / always | Each complaint names exactly one reason code, and a reason code may explain no complaint. |
| `fact_customer_complaint` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each complaint is recorded on exactly one day, and a day may have no complaint. |
| `fact_vendor_fill` | `vendor_id` | `dim_vendor` | 1:N | 1:many / optional | many:1 / always | Each fill names exactly one vendor, and a vendor may have no fill. |
| `fact_vendor_fill` | `purchase_order_line_id` | `fact_purchase_order_line` | 1:N | 1:many / optional | many:1 / always | Each fill matches exactly one purchase-order line, and a purchase-order line may have no fill. |
| `fact_vendor_fill` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each fill is recorded on exactly one day, and a day may have no vendor fill. |
| `fact_space_audit` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each audit covers exactly one storefront, and a storefront may have no space audit. |
| `fact_space_audit` | `aisle_id` | `dim_aisle` | 1:N | 1:many / optional | many:1 / optional | An audit may omit an aisle, and an aisle may have no space audit. |
| `fact_space_audit` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Each audit is performed by exactly one employee, and an employee may perform no space audit. |
| `fact_space_audit` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each audit occurs on exactly one day, and a day may have no space audit. |
| `fact_household_visit` | `store_id` | `dim_store` | 1:N | 1:many / optional | many:1 / always | Each visit occurs at exactly one storefront, and a storefront may have no visit. |
| `fact_household_visit` | `household_id` | `dim_household` | 1:N | 1:many / optional | many:1 / optional | A visit may omit a household, and a household may have no visit. |
| `fact_household_visit` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each visit occurs on exactly one day, and a day may have no visit. |
| `fact_household_visit` | `channel_id` | `dim_channel` | 1:N | 1:many / optional | many:1 / always | Each visit uses exactly one channel, and a channel may have no visit. |

## Dataset inventory

### bridge

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `bridge_item_store` | bridge | `assortment_id` | Assortment listing of an item at a storefront. |
| `bridge_item_vendor` | bridge | `item_vendor_id` | Source relationship between an item, a vendor, and an optional vendor site. |
| `bridge_promotion_item` | bridge | `promotion_item_id` | Item eligible for a promotion. |
| `bridge_promotion_store` | bridge | `promotion_store_id` | Storefront where a promotion is offered. |
| `bridge_planogram_position` | bridge | `planogram_position_id` | Placement of an item on a planogram, optionally on a fixture. |
| `bridge_coupon_item` | bridge | `coupon_item_id` | Item a coupon can discount. |
| `bridge_recipe_ingredient` | bridge | `recipe_ingredient_id` | Ingredient used by a fresh recipe. |
| `bridge_employee_role` | bridge | `employee_role_id` | Labor role an employee is qualified to work. |
| `bridge_item_tax` | bridge | `item_tax_id` | Tax jurisdiction that applies to an item. |
| `bridge_store_competitor` | bridge | `store_competitor_id` | Competitor tracked against a storefront. |
| `bridge_customer_segment` | bridge | `customer_segment_id` | Membership of a customer in a segment. |
| `bridge_offer_tender` | bridge | `offer_tender_id` | Tender type an offer can be settled with. |

### calendar

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_calendar_day` | dimension | `calendar_day_id` | Civil date used to place operating events. |
| `dim_hour` | dimension | `hour_id` | Hour of the day used to place intraday events. |

### channel

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_channel` | dimension | `channel_id` | Selling channel such as in-store, pickup, or delivery. |
| `dim_fulfillment_type` | dimension | `fulfillment_type_id` | Way an e-commerce order is fulfilled from a storefront. |
| `dim_delivery_slot` | dimension | `delivery_slot_id` | Pickup or delivery window offered by a storefront. |

### customer

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_loyalty_program` | dimension | `loyalty_program_id` | Loyalty program a customer account can join. |
| `dim_customer` | dimension | `customer_id` | Shopper who may belong to a household and hold a loyalty account. |
| `dim_household` | dimension | `household_id` | Household that groups shoppers who share a home. |
| `dim_loyalty_account` | dimension | `loyalty_account_id` | Account that joins one customer to one loyalty program. |
| `dim_customer_segment` | dimension | `segment_id` | Named segment a customer can be a member of. |
| `fact_loyalty_accrual` | fact | `accrual_id` | Points posted to a loyalty account, optionally from a POS transaction. |
| `fact_loyalty_redemption` | fact | `loyalty_redemption_id` | Points redeemed from a loyalty account, optionally against a POS transaction. |
| `fact_household_visit` | fact | `visit_id` | Trip header for a visit to a storefront, distinct from the POS transaction. |

### ecommerce

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_ecommerce_order` | fact | `ecommerce_order_id` | Store e-commerce order fulfilled from a storefront. |
| `fact_ecommerce_order_line` | fact | `ecommerce_order_line_id` | Item line on a store e-commerce order. |
| `fact_pick_task` | fact | `pick_task_id` | Store pick of one e-commerce order line. |
| `fact_delivery` | fact | `delivery_id` | Handoff of an e-commerce order to a carrier or to the customer. |
| `fact_slot_capacity` | fact | `slot_capacity_id` | Order capacity a storefront offers for a delivery slot on a day. |

### finance

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_gl_account` | dimension | `gl_account_id` | General-ledger account that classifies a vendor invoice line. |
| `fact_cash_deposit` | fact | `cash_deposit_id` | Cash deposited from a storefront by an employee. |

### fresh

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_recipe` | dimension | `recipe_id` | Fresh recipe whose finished good is a sellable item. |
| `dim_ingredient` | dimension | `ingredient_id` | Component item that a fresh recipe can consume. |
| `fact_fresh_production` | fact | `production_batch_id` | Batch of a fresh recipe produced at a storefront. |
| `fact_waste_event` | fact | `waste_event_id` | Fresh or other product discarded at a storefront. |

### inventory

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_inventory_position` | fact | `inventory_position_id` | On-hand position of an item at a storefront or a distribution-center location. |
| `fact_inventory_movement` | fact | `movement_id` | Quantity movement of an item, optionally at a storefront. |
| `fact_shrink_event` | fact | `shrink_event_id` | Known loss of an item at a storefront. |
| `fact_cycle_count` | fact | `cycle_count_id` | Physical count of an item at a storefront or a distribution-center location. |
| `fact_out_of_stock` | fact | `out_of_stock_id` | Observation that an item was unavailable at a storefront. |

### merchandising

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_category` | dimension | `category_id` | Merchandise category inside a department. |
| `dim_subcategory` | dimension | `subcategory_id` | Merchandise subcategory inside a category. |
| `dim_brand` | dimension | `brand_id` | Brand that may be named on a sellable item. |
| `dim_unit_of_measure` | dimension | `uom_id` | Unit in which an item is stocked, ordered, or sold. |
| `dim_item` | dimension | `item_id` | Sellable or produced SKU classified under a subcategory. |

### organization

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_banner` | dimension | `banner_id` | Single consumer-facing banner under which Greenbasket storefronts trade. |
| `dim_region` | dimension | `region_id` | Geographic region that groups districts inside the banner. |
| `dim_district` | dimension | `district_id` | Field district that groups storefronts inside a region. |
| `dim_store_format` | dimension | `store_format_id` | Operating format of a storefront, such as a supermarket or a small market. |
| `dim_price_zone` | dimension | `price_zone_id` | Pricing zone that groups storefronts sharing a retail price file. |
| `dim_store` | dimension | `store_id` | Storefront shop where customers buy merchandise and pick up e-commerce orders. |
| `dim_department` | dimension | `department_id` | Merchandise department that groups categories, separate from any store labor department. |
| `dim_employee` | dimension | `employee_id` | Person employed by a storefront, including the store manager. |

### party

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_vendor` | dimension | `vendor_id` | Supplier that sells merchandise to Greenbasket. |
| `dim_vendor_site` | dimension | `vendor_site_id` | Ship-from or order site that belongs to a vendor. |

### planning

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_demand_forecast` | fact | `forecast_id` | Forecast quantity of an item at a storefront on a day. |

### pos

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_pos_transaction` | fact | `pos_transaction_id` | Basket rung at a storefront by a cashier on a workstation. |
| `fact_pos_line` | fact | `pos_line_id` | Item line on a POS transaction. |
| `fact_pos_tender` | fact | `pos_tender_id` | Tender applied to a POS transaction. |
| `fact_pos_discount` | fact | `pos_discount_id` | Discount taken against a POS line. |
| `fact_transaction_tax` | fact | `transaction_tax_id` | Tax amount charged on a POS line for a jurisdiction. |
| `fact_customer_return` | fact | `customer_return_id` | Quantity of an item returned at a storefront. |

### price

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_retail_price` | fact | `price_id` | Retail price of an item in a price zone on a day. |
| `fact_item_cost` | fact | `item_cost_id` | Unit cost of an item, optionally for a vendor and a storefront. |
| `fact_markdown_event` | fact | `markdown_id` | Markdown taken on an item at a storefront. |
| `fact_competitor_price` | fact | `competitor_price_id` | Observed competitor price of an item on a day. |

### promotion

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_promotion` | dimension | `promotion_id` | Merchandising promotion that groups one or more offers. |
| `dim_offer` | dimension | `offer_id` | Customer offer that belongs to a promotion. |
| `dim_coupon` | dimension | `coupon_id` | Coupon a shopper can present, optionally tied to an offer. |
| `fact_promotion_redemption` | fact | `redemption_id` | Use of a promotion at a storefront, optionally against a POS line. |
| `fact_coupon_redemption` | fact | `coupon_redemption_id` | Coupon presented on a POS transaction at a storefront. |

### reference

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_reason_code` | dimension | `reason_code_id` | Coded reason used for movements, returns, markdowns, and complaints. |
| `dim_shrink_reason` | dimension | `shrink_reason_id` | Reason inventory or fresh product was lost or discarded. |
| `dim_tax_jurisdiction` | dimension | `tax_jurisdiction_id` | Tax authority that can apply to an item or a basket line. |
| `dim_competitor` | dimension | `competitor_id` | Competing retailer whose prices or proximity are tracked. |
| `dim_currency` | dimension | `currency_id` | Currency used on purchase orders and vendor invoices. |
| `dim_season` | dimension | `season_id` | Merchandising season used to describe seasonal selling. |

### service

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_service_level` | fact | `service_level_id` | In-stock observation for an item at a storefront on a day. |
| `fact_customer_complaint` | fact | `complaint_id` | Complaint recorded against a storefront. |

### space

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_aisle` | dimension | `aisle_id` | Selling aisle inside a storefront. |
| `dim_fixture` | dimension | `fixture_id` | Shelf or display fixture installed in an aisle. |
| `dim_planogram` | dimension | `planogram_id` | Plan for how a subcategory should be presented on fixtures. |
| `fact_planogram_compliance` | fact | `compliance_id` | Check of whether a storefront matched a planogram. |
| `fact_space_audit` | fact | `space_audit_id` | Audit of store space, optionally of one aisle, performed by an employee. |

### storefront

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_cashier` | dimension | `cashier_id` | Till operator employed by exactly one storefront. |
| `dim_labor_role` | dimension | `labor_role_id` | Job role a store employee can be scheduled to work. |
| `dim_shift` | dimension | `shift_id` | Named work shift offered by a storefront. |
| `dim_lane_type` | dimension | `lane_type_id` | Kind of checkout lane, such as a staffed belt or self-checkout. |
| `dim_workstation` | dimension | `workstation_id` | POS workstation installed in a storefront. |
| `dim_payment_terminal` | dimension | `payment_terminal_id` | Payment terminal bound to one POS workstation. |
| `fact_cashier_drawer` | fact | `drawer_session_id` | Cash drawer session worked by a cashier on a workstation. |
| `fact_labor_punch` | fact | `punch_id` | Time punch for an employee at a storefront. |
| `fact_schedule_shift` | fact | `scheduled_shift_id` | Shift an employee is scheduled to work at a storefront. |
| `fact_utility_reading` | fact | `utility_reading_id` | Utility usage recorded for a storefront on a day. |

### supply

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_warehouse` | dimension | `warehouse_id` | Distribution center that replenishes storefronts. |
| `dim_dc_location` | dimension | `dc_location_id` | Storage location inside a distribution center. |
| `dim_carrier` | dimension | `carrier_id` | Carrier that hauls store deliveries or e-commerce orders. |
| `fact_store_receipt` | fact | `store_receipt_id` | Receipt of a distribution-center shipment at a storefront. |
| `fact_store_receipt_line` | fact | `store_receipt_line_id` | Item quantity received on a store receipt. |
| `fact_dc_shipment` | fact | `dc_shipment_id` | Shipment from a distribution center to a storefront. |
| `fact_dc_shipment_line` | fact | `dc_shipment_line_id` | Item quantity shipped on a distribution-center shipment. |
| `fact_purchase_order` | fact | `purchase_order_id` | Order placed with a vendor site for delivery to a distribution center. |
| `fact_purchase_order_line` | fact | `purchase_order_line_id` | Item quantity ordered on a purchase order. |
| `fact_vendor_invoice` | fact | `vendor_invoice_id` | Invoice presented by a vendor. |
| `fact_vendor_invoice_line` | fact | `vendor_invoice_line_id` | Charge line on a vendor invoice. |
| `fact_replenishment_order` | fact | `replenishment_order_id` | Storefront request that a distribution center replenish an item. |
| `fact_vendor_fill` | fact | `vendor_fill_id` | Quantity a vendor filled against a purchase-order line. |

### tender

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_tender_type` | dimension | `tender_type_id` | Form of payment a basket or gift card transaction can use. |
| `fact_gift_card_txn` | fact | `gift_card_txn_id` | Issue, redemption, or reload of a gift card at a storefront. |

## Provenance

Original grocery operating ontology informed by publicly described retail concepts (store, workstation, tender, item, promotion) such as those discussed around the NRF ARTS operational model and a Kimball-style retail bus. Not a copy of a vendor schema. No synthetic statistics.
