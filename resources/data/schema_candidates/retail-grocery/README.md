# Greenbasket Markets

## Introduction

Greenbasket Markets is a regional grocery chain. The catalog `retail-grocery` is the ontology of that chain: 110 datasets in the Snowflake database `RETAIL_GROCERY`. Locations run from one banner to regions, districts, and storefronts. Merchandise runs from department to category, subcategory, and item. Store operations cover cashiers, the store manager, POS workstations, baskets, replenishment, fresh production, loyalty, and store e-commerce.

Two labor rules are fixed in the metadata. Every storefront includes one or more cashiers, and each cashier belongs to exactly one storefront. Every storefront has exactly one manager, and an employee manages at most one storefront. A cashier is also exactly one employee. A POS transaction is one basket at one storefront, rung by one cashier on one workstation, and every basket has at least one item line and one tender.

Each grain column is the complete population of its logical identity (`is_entity_universe: true`). A foreign key elsewhere is the same identity with `is_entity_universe: false`. The questions below use only those authored identities, grains, and joins. Each question has one universe dataset per identity and one column set on each join, so the datasets and the relationship path are fixed by the metadata. Quantity and amount columns are attributes of a single fact row. The catalog does not store row counts or distributions.

The business narrative and the full relationship table are in `business-model.md`. Loadable YAML is in `yaml/`.

## BI questions

1. Which cashiers work at each storefront, and who is that storefront's manager?
   `retail-grocery.storefront.dim_cashier.store_id` joins `retail-grocery.organization.dim_store.store_id` as `1:many` with a required match both ways. `dim_cashier.employee_id` joins `dim_employee` one-to-one. `dim_store.manager_employee_id` joins `dim_employee` one-to-one, required from the storefront and optional across employees.

2. Which storefronts sit in each district, region, and banner?
   `dim_banner` to `dim_region` to `dim_district` to `dim_store`. Region, district, and storefront hops are `1:many` with a required child. A storefront also names its banner, format, price zone, and primary distribution center directly.

3. What quantity and extended amount of each item did a storefront sell, by day, hour, cashier, and workstation?
   `retail-grocery.pos.fact_pos_line` holds `sold_quantity` and `extended_amount` and always joins `fact_pos_transaction` and `dim_item`. The transaction joins `dim_store`, `dim_cashier`, `dim_workstation`, `dim_calendar_day`, and `dim_hour`. Line grain stays the line. The basket grain stays the transaction.

4. How was each basket paid?
   `retail-grocery.pos.fact_pos_tender` is `1:many` from `fact_pos_transaction` and always joins `dim_tender_type`. Every transaction has at least one tender. `tender_amount` is an attribute of the tender row.

5. Which promotion, offer, or coupon discounted a line, and what tax was charged?
   `fact_pos_discount` is `1:many` from `fact_pos_line` and may name an offer or a coupon. `fact_transaction_tax` joins the line and `dim_tax_jurisdiction`.

6. What is the merchandise hierarchy of an item, and where is it listed?
   `dim_department` to `dim_category` to `dim_subcategory` to `dim_item`, each hop `1:many` and required. `retail-grocery.bridge.bridge_item_store` is the assortment of an item at a storefront. `fact_retail_price` joins the item, price zone, and day.

7. Which items are on a planogram, and did the storefront match that plan?
   `dim_store` to `dim_aisle` to `dim_fixture` is required `1:many`. `bridge_planogram_position` places an item on a planogram and may name a fixture. `fact_planogram_compliance` joins the planogram, storefront, and day.

8. What did a household's loyalty account earn or redeem on a basket?
   `dim_loyalty_account` joins one customer and one program. `fact_loyalty_accrual` and `fact_loyalty_redemption` join that account and may join the POS transaction. A customer may join `dim_household`. `fact_household_visit` is a separate trip header, not the basket.

9. What did a distribution center ship to a storefront, and what did the storefront receive?
   `fact_dc_shipment` joins `dim_warehouse` and `dim_store`. Every shipment has lines on `fact_dc_shipment_line`. `fact_store_receipt` joins the storefront and warehouse, and every receipt has lines on `fact_store_receipt_line`.

10. What is on order from a vendor site, and how much of each purchase-order line was filled?
    Every vendor has at least one site on `dim_vendor_site`. `fact_purchase_order` joins the vendor, site, and warehouse. Every order has lines. `fact_vendor_fill` joins the purchase-order line and records `filled_quantity`.

11. Where was an item out of stock, shrunk, or wasted, and why?
    `fact_out_of_stock` joins item, storefront, and day. `fact_shrink_event` joins item, storefront, and `dim_shrink_reason`. `fact_waste_event` joins the same item and storefront. Fresh production is separate: `dim_recipe` points at the finished item, `bridge_recipe_ingredient` lists ingredients, and `fact_fresh_production` is one batch at a storefront on a day.

12. What e-commerce orders were placed for pickup or delivery at a storefront, and were the lines picked?
    `fact_ecommerce_order` joins `dim_customer`, `dim_store`, and `dim_fulfillment_type`, and may name a delivery slot. Every order has lines on `fact_ecommerce_order_line`. Every line has at least one `fact_pick_task`. `fact_delivery` joins the order when it leaves the storefront.
