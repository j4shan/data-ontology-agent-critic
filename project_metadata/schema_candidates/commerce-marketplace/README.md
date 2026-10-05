# Meridian Marketplace

## Introduction

Meridian Marketplace is a multi-seller marketplace for business buyers and consumers. The catalog `commerce-marketplace` is the ontology of that marketplace: 113 datasets in the Snowflake database `COMMERCE_MARKETPLACE`. One marketplace has many sellers. Each seller has exactly one account manager and at least one seller storefront. Each storefront publishes at least one listing. A product has at least one variant, and a listing offers one variant on one storefront.

Buyers are accounts with one or more users. Commercial documents are the cart, quote, order, shipment, payment, seller settlement, and return. A cart may be empty. An order always has lines. A shipment always has lines, scan events, and packages. A seller settlement always has settlement lines. Contracts and price lists carry business prices. Bill-to and ship-to are different datasets, so the two addresses do not share one join column.

Each grain column is the complete population of its logical identity (`is_entity_universe: true`). A foreign key elsewhere is the same identity with `is_entity_universe: false`. The questions below use only those authored identities, grains, and joins. Each question has one universe dataset per identity and one column set on each join, so the datasets and the relationship path are fixed by the metadata. Quantity, price, and amount columns are attributes of a single fact row. The catalog does not store row counts or distributions.

The business narrative and the full relationship table are in `business-model.md`. Loadable YAML is in `yaml/`.

## BI questions

1. Who is each seller's account manager, and which storefronts does that seller operate?
   `commerce-marketplace.party.dim_seller.account_manager_employee_id` joins `dim_employee` one-to-one. Every seller has one manager, and an employee manages at most one seller. `dim_seller_storefront.seller_id` joins `dim_seller` as `1:many` with a required match both ways.

2. What does each storefront list, for which variant and product?
   `commerce-marketplace.listing.fact_listing` is `1:many` from `dim_seller_storefront` and always joins `dim_variant`. Every product on `dim_product` has at least one variant. A listing may also name a catalog.

3. What is in a buyer's cart, and which checkout followed it?
   `fact_cart` always joins `dim_buyer_account`. `fact_cart_line` always joins the cart and a variant. A cart may have no lines. `fact_checkout` may join the cart, the buyer account, an address, and a shipping method.

4. What did a buyer account order from a seller, on which storefront, and under which contract?
   `commerce-marketplace.order.fact_order` always joins `dim_buyer_account`, `dim_seller`, `dim_marketplace`, `dim_currency`, the ship-to address, the channel, and the order day. The contract is optional. Every order has lines on `fact_order_line`, and each line joins `dim_variant` and `dim_seller_storefront`. A buyer account may have no orders. Every buyer account has at least one user on `dim_buyer_user`.

5. Where is an order billed, as distinct from where it ships?
   Ship-to is `fact_order.ship_to_address_id`, required, joined to `dim_address`. Bill-to is a separate one-to-one row on `fact_order_bill_to`. An order has at most one bill-to record and may have none.

6. How was each order line allocated, and what remains on backorder?
   `fact_order_allocation` is `1:many` from `fact_order_line` and may name a seller warehouse or a fulfillment center. `fact_backorder` joins the order line and the variant.

7. What shipped for an order, and which scans and packages belong to that shipment?
   `fact_shipment` joins `fact_order` and may name a carrier service, a fulfillment center, a seller warehouse, and a ship date. Every shipment has lines on `fact_shipment_line`, events on `fact_shipment_event`, and packages on `fact_package`. `fact_shipment_line` joins the order line.

8. Was payment authorized, captured, refunded, or charged back?
   `fact_payment_authorization` joins `dim_payment_method` and may join the order. `fact_payment_capture` joins the order and may join the authorization. `fact_refund` joins the order and a reason code. `fact_chargeback` joins the capture.

9. What did the marketplace settle to a seller, and which order lines, fees, and payouts make up that settlement?
   `fact_seller_settlement` joins `dim_seller`, currency, and day. Every settlement has lines on `commerce-marketplace.settlement.fact_settlement_line`. `fact_commission` joins the order line and the seller. `fact_payout` joins the settlement and the seller.

10. Which contract price or price-list price applies to a variant for a buyer and seller?
    `dim_contract` joins one seller, one buyer account, and one currency. Every contract has prices on `bridge_contract_price`. `dim_price_list` joins the seller and currency, and every price list has variant prices on `bridge_price_list_variant`. An order may cite the contract. The two price populations stay on different bridges.

11. What are the components of a bundle, and which variants are compatible?
    `dim_bundle` names one parent variant. `bridge_bundle_component` is `1:many` from that bundle and names one component variant per row. `dim_compatibility_group` has members on `bridge_product_compatibility`, one variant per membership row.

12. What was returned, and what did inspection decide?
    `fact_return_request` joins the order, buyer account, and reason code, and may join the seller's return policy. Every seller has a return policy. Every request has lines on `fact_return_line`. Every return line has an inspection on `fact_return_inspection`.

13. Which listings were suppressed, and which fraud decision applied to an order or checkout?
    `fact_listing_suppression` joins `fact_listing` and `dim_reason_code`. `fact_fraud_decision` may join the order, the checkout, and `dim_fraud_rule`.
