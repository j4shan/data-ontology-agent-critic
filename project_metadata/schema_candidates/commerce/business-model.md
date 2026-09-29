# Meridian Marketplace

Meridian Marketplace is a multi-seller marketplace that sells to business buyers and to consumers. One marketplace hosts many sellers. Each seller is the merchant for its offers, and the marketplace supplies the shared buying experience, checkout, and settlement. A buyer is either a business account purchasing under negotiated terms or a consumer account purchasing from a published listing. Both audiences use the same commercial documents.

Each seller has exactly one account manager. That manager is an employee, and an employee manages at most one seller. Each seller operates one or more seller storefronts. A storefront sells in one currency and publishes one or more listings. A listing is the offer a buyer can purchase: it names a variant, belongs to one storefront, and may point at a catalog. On the buying side, each buyer account has one or more buyer users. A consumer profile matches one buyer user when a personal profile is kept, and a buyer user may have no consumer profile. Addresses support bill-to, ship-to, and return roles.

The catalog separates the item a seller presents from the unit that is stocked and sold. A product may name a brand. Each product has one or more variants, and each variant uses one unit of measure. Categories classify products through an assignment, so a category does not point at itself. Attributes, media, and harmonized-system codes describe the goods and support customs when a shipment crosses a border. A bundle is a parent variant with one or more component variants on separate component rows. A compatibility group collects variants that can be used together, and each membership row names one variant.

Business buying depends on contracts and price lists. A contract binds one seller, one buyer account, and one currency, and every contract prices one or more variants. A price list is a seller schedule of variant prices in one currency, and every price list includes one or more variants. A quote states a quoted quantity and a quoted price for a buyer account before an order exists. Promotions and coupons can target variants. A consumer can buy an active listing without a contract, while a business order can cite the contract. The two paths share variants, listings, and orders.

The commercial documents are the cart, the quote, the order, the shipment, the payment, the seller settlement, and the return. A cart belongs to a buyer account. An empty cart is valid, so a cart may have no lines, while each cart line belongs to exactly one cart. Checkout may start from a cart. An order names a buyer account, a seller, the marketplace, a currency, a channel, a calendar day, and a ship-to address. A bill-to address is an optional one-to-one record on the order, and a contract is optional. Every order has one or more order lines naming a variant and a storefront. Allocation and backorder record how unmet demand is sourced.

A shipment belongs to one order and may name a carrier service, a warehouse, a fulfillment center, and a ship date. Every shipment has one or more shipment lines, scan events, and packages. Payment authorization may precede the order. Capture collects funds, and refunds and chargebacks adjust a capture. Seller settlement is what the marketplace owes the seller. Every settlement has one or more settlement lines, with commission, fees, and payout explaining the proceeds. Invoices and buyer payments record what the buyer owes, including subscription billing when an account holds a plan. A return request has one or more return lines, and each line is inspected.

Support cases, reviews, questions, advertising, search, and fraud decisions sit beside that spine. A review stores the rating selected by the reviewer on the published scale. Search stores the raw text the buyer submitted. None of these rows summarize a population. Quantities, prices, and amounts are attributes of a single document. Statistics are not authored.

## Data ecosystem

The authored catalog `commerce` contains 113 datasets (52 dimensions, 49 facts, 12 bridges) in the Snowflake database `COMMERCE` on account `meridian.us-west-2`.

Each dataset is one ontology node. The grain column is the system of record for that dataset's logical identity and is marked `is_entity_universe: true`. Foreign-key columns realize the same logical identity with `is_entity_universe: false`, because the child dataset does not hold the complete population. Edges join those two realizations. Multiplicity and match existence are directional and follow the operating rules below. Row counts, distinct counts, and other data statistics are intentionally absent.

## Signature relationships

| Relationship | Identity | Parent to child | Child to parent | Rule |
| --- | --- | --- | --- | --- |
| `dim_marketplace` to `dim_seller` | `marketplace_identity` | 1:many (always) | many:1 (always) | Every marketplace includes one or more sellers, and each seller belongs to exactly one marketplace. |
| `dim_employee` to `dim_seller` | `employee_identity` | 1:1 (optional) | 1:1 (always) | Each seller has exactly one account manager, and an employee manages at most one seller. |
| `dim_seller` to `dim_seller_storefront` | `seller_identity` | 1:many (always) | many:1 (always) | Each seller includes one or more storefronts, and each storefront belongs to exactly one seller. |
| `dim_seller_storefront` to `fact_listing` | `seller_storefront_identity` | 1:many (always) | many:1 (always) | Each storefront includes one or more listings, and each listing belongs to exactly one storefront. |
| `dim_product` to `dim_variant` | `product_identity` | 1:many (always) | many:1 (always) | Every product includes one or more variants, and each variant belongs to exactly one product. |
| `fact_order` to `fact_order_line` | `order_identity` | 1:many (always) | many:1 (always) | Every order includes one or more order lines, and each order line belongs to exactly one order. |
| `fact_cart` to `fact_cart_line` | `cart_identity` | 1:many (optional) | many:1 (always) | Each cart line belongs to exactly one cart, and a cart may have no cart lines. |
| `fact_shipment` to `fact_shipment_line` | `shipment_identity` | 1:many (always) | many:1 (always) | Every shipment includes one or more shipment lines, and each shipment line belongs to exactly one shipment. |
| `fact_shipment` to `fact_shipment_event` | `shipment_identity` | 1:many (always) | many:1 (always) | Every shipment includes one or more shipment events, and each shipment event belongs to exactly one shipment. |
| `fact_seller_settlement` to `fact_settlement_line` | `seller_settlement_identity` | 1:many (always) | many:1 (always) | Every seller settlement includes one or more settlement lines, and each settlement line belongs to exactly one seller settlement. |
| `dim_buyer_account` to `dim_buyer_user` | `buyer_account_identity` | 1:many (always) | many:1 (always) | Every buyer account includes one or more buyer users, and each buyer user belongs to exactly one buyer account. |
| `dim_buyer_account` to `fact_order` | `buyer_account_identity` | 1:many (optional) | many:1 (always) | Each order belongs to exactly one buyer account, and a buyer account may have no orders. |

## Relationship rules

| Child dataset | Column | Universe dataset | Mapping | Parent match | Child match | Rule |
| --- | --- | --- | --- | --- | --- | --- |
| `dim_region` | `country_id` | `dim_country` | 1:N | 1:many / always | many:1 / always | Every country includes one or more regions, and each region belongs to exactly one country. |
| `dim_seller` | `marketplace_id` | `dim_marketplace` | 1:N | 1:many / always | many:1 / always | Every marketplace includes one or more sellers, and each seller belongs to exactly one marketplace. |
| `dim_seller` | `seller_tier_id` | `dim_seller_tier` | 1:N | 1:many / optional | many:1 / always | Each seller is assigned exactly one seller tier, and a seller tier may have no sellers. |
| `dim_seller` | `account_manager_employee_id` | `dim_employee` | 1:1 | 1:1 / optional | 1:1 / always | Each seller has exactly one account manager, and an employee manages at most one seller. |
| `dim_seller` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Each seller belongs to exactly one country, and a country may have no sellers. |
| `dim_seller_storefront` | `seller_id` | `dim_seller` | 1:N | 1:many / always | many:1 / always | Each seller includes one or more storefronts, and each storefront belongs to exactly one seller. |
| `dim_seller_storefront` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each storefront uses exactly one currency, and a currency may have no storefronts. |
| `dim_buyer_account` | `buyer_segment_id` | `dim_buyer_segment` | 1:N | 1:many / optional | many:1 / optional | A buyer account may have no buyer segment, and a buyer segment may have no buyer accounts. |
| `dim_buyer_account` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Each buyer account belongs to exactly one country, and a country may have no buyer accounts. |
| `dim_buyer_user` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / always | many:1 / always | Every buyer account includes one or more buyer users, and each buyer user belongs to exactly one buyer account. |
| `dim_address` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / optional | An address may have no buyer account, and a buyer account may have no addresses. |
| `dim_address` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Each address belongs to exactly one country, and a country may have no addresses. |
| `dim_address` | `region_id` | `dim_region` | 1:N | 1:many / optional | many:1 / optional | An address may have no region, and a region may have no addresses. |
| `dim_catalog` | `seller_id` | `dim_seller` | 1:N | 1:many / always | many:1 / always | Every seller includes one or more catalogs, and each catalog belongs to exactly one seller. |
| `dim_product` | `brand_id` | `dim_brand` | 1:N | 1:many / optional | many:1 / optional | A product may have no brand, and a brand may have no products. |
| `dim_product` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each product belongs to exactly one seller, and a seller may have no products. |
| `dim_variant` | `product_id` | `dim_product` | 1:N | 1:many / always | many:1 / always | Every product includes one or more variants, and each variant belongs to exactly one product. |
| `dim_variant` | `uom_id` | `dim_uom` | 1:N | 1:many / optional | many:1 / always | Each variant uses exactly one unit of measure, and a unit of measure may have no variants. |
| `dim_media_asset` | `product_id` | `dim_product` | 1:N | 1:many / optional | many:1 / optional | A media asset may have no product, and a product may have no media assets. |
| `dim_price_list` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each price list belongs to exactly one seller, and a seller may have no price lists. |
| `dim_price_list` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each price list uses exactly one currency, and a currency may have no price lists. |
| `dim_contract` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each contract belongs to exactly one seller, and a seller may have no contracts. |
| `dim_contract` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / always | Each contract belongs to exactly one buyer account, and a buyer account may have no contracts. |
| `dim_contract` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each contract uses exactly one currency, and a currency may have no contracts. |
| `dim_payment_method` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / always | Each payment method belongs to exactly one buyer account, and a buyer account may have no payment methods. |
| `dim_payment_method` | `payment_provider_id` | `dim_payment_provider` | 1:N | 1:many / optional | many:1 / always | Each payment method uses exactly one payment provider, and a payment provider may have no payment methods. |
| `dim_shipping_method` | `carrier_id` | `dim_carrier` | 1:N | 1:many / optional | many:1 / optional | A shipping method may have no carrier, and a carrier may have no shipping methods. |
| `dim_carrier_service` | `carrier_id` | `dim_carrier` | 1:N | 1:many / always | many:1 / always | Every carrier includes one or more carrier services, and each carrier service belongs to exactly one carrier. |
| `dim_seller_warehouse` | `seller_id` | `dim_seller` | 1:N | 1:many / always | many:1 / always | Every seller includes one or more warehouses, and each warehouse belongs to exactly one seller. |
| `dim_seller_warehouse` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Each warehouse belongs to exactly one country, and a country may have no warehouses. |
| `dim_fulfillment_center` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Each fulfillment center belongs to exactly one country, and a country may have no fulfillment centers. |
| `dim_fulfillment_center` | `region_id` | `dim_region` | 1:N | 1:many / optional | many:1 / optional | A fulfillment center may have no region, and a region may have no fulfillment centers. |
| `dim_promotion` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / optional | A promotion may have no seller, and a seller may have no promotions. |
| `dim_coupon` | `promotion_id` | `dim_promotion` | 1:N | 1:many / optional | many:1 / optional | A coupon may have no promotion, and a promotion may have no coupons. |
| `dim_campaign` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each campaign belongs to exactly one seller, and a seller may have no campaigns. |
| `dim_subscription_plan` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / optional | A subscription plan may have no seller, and a seller may have no subscription plans. |
| `dim_fee_schedule` | `seller_tier_id` | `dim_seller_tier` | 1:N | 1:many / optional | many:1 / always | Each fee schedule belongs to exactly one seller tier, and a seller tier may have no fee schedules. |
| `dim_return_policy` | `seller_id` | `dim_seller` | 1:N | 1:many / always | many:1 / always | Every seller includes one or more return policies, and each return policy belongs to exactly one seller. |
| `dim_consumer` | `buyer_user_id` | `dim_buyer_user` | 1:1 | 1:1 / optional | 1:1 / always | Each consumer profile matches exactly one buyer user, and a buyer user has at most one consumer profile. |
| `bridge_product_category` | `product_id` | `dim_product` | 1:N | 1:many / optional | many:1 / always | Each assignment belongs to exactly one product, and a product may have no category assignments. |
| `bridge_product_category` | `category_id` | `dim_category` | 1:N | 1:many / optional | many:1 / always | Each assignment belongs to exactly one category, and a category may have no product assignments. |
| `bridge_variant_attribute` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each assignment belongs to exactly one variant, and a variant may have no attribute assignments. |
| `bridge_variant_attribute` | `attribute_id` | `dim_attribute` | 1:N | 1:many / optional | many:1 / always | Each assignment belongs to exactly one attribute, and an attribute may have no variant assignments. |
| `bridge_catalog_product` | `catalog_id` | `dim_catalog` | 1:N | 1:many / always | many:1 / always | Every catalog includes one or more products, and each placement belongs to exactly one catalog. |
| `bridge_catalog_product` | `product_id` | `dim_product` | 1:N | 1:many / optional | many:1 / always | Each placement belongs to exactly one product, and a product may have no catalog placements. |
| `bridge_price_list_variant` | `price_list_id` | `dim_price_list` | 1:N | 1:many / always | many:1 / always | Every price list includes one or more variants, and each price row belongs to exactly one price list. |
| `bridge_price_list_variant` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each price row belongs to exactly one variant, and a variant may have no price list rows. |
| `bridge_contract_price` | `contract_id` | `dim_contract` | 1:N | 1:many / always | many:1 / always | Every contract includes one or more priced variants, and each contract price belongs to exactly one contract. |
| `bridge_contract_price` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each contract price belongs to exactly one variant, and a variant may have no contract prices. |
| `bridge_promotion_variant` | `promotion_id` | `dim_promotion` | 1:N | 1:many / optional | many:1 / always | Each promotion target belongs to exactly one promotion, and a promotion may have no variant targets. |
| `bridge_promotion_variant` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each promotion target belongs to exactly one variant, and a variant may have no promotion targets. |
| `bridge_seller_category` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each authorization belongs to exactly one seller, and a seller may have no category authorizations. |
| `bridge_seller_category` | `category_id` | `dim_category` | 1:N | 1:many / optional | many:1 / always | Each authorization belongs to exactly one category, and a category may have no seller authorizations. |
| `bridge_buyer_address` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / always | Each buyer address link belongs to exactly one buyer account, and a buyer account may have no address links. |
| `bridge_buyer_address` | `address_id` | `dim_address` | 1:N | 1:many / optional | many:1 / always | Each buyer address link belongs to exactly one address, and an address may have no buyer links. |
| `dim_bundle` | `parent_variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each bundle names exactly one parent variant, and a variant may be the parent of no bundle. |
| `bridge_bundle_component` | `bundle_id` | `dim_bundle` | 1:N | 1:many / always | many:1 / always | Every bundle includes one or more components, and each component belongs to exactly one bundle. |
| `bridge_bundle_component` | `component_variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each bundle component names exactly one component variant, and a variant may have no bundle rows as the component. |
| `bridge_campaign_placement` | `campaign_id` | `dim_campaign` | 1:N | 1:many / always | many:1 / always | Every campaign includes one or more placements, and each booking belongs to exactly one campaign. |
| `bridge_campaign_placement` | `ad_placement_id` | `dim_ad_placement` | 1:N | 1:many / optional | many:1 / always | Each booking belongs to exactly one ad placement, and an ad placement may have no campaign bookings. |
| `bridge_product_compatibility` | `compatibility_group_id` | `dim_compatibility_group` | 1:N | 1:many / always | many:1 / always | Every compatibility group includes one or more variants, and each membership belongs to exactly one group. |
| `bridge_product_compatibility` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each membership names exactly one variant, and a variant may belong to no compatibility group. |
| `bridge_coupon_variant` | `coupon_id` | `dim_coupon` | 1:N | 1:many / optional | many:1 / always | Each coupon target belongs to exactly one coupon, and a coupon may have no variant targets. |
| `bridge_coupon_variant` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each coupon target belongs to exactly one variant, and a variant may have no coupon targets. |
| `fact_listing` | `seller_storefront_id` | `dim_seller_storefront` | 1:N | 1:many / always | many:1 / always | Each storefront includes one or more listings, and each listing belongs to exactly one storefront. |
| `fact_listing` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each listing offers exactly one variant, and a variant may have no listings. |
| `fact_listing` | `catalog_id` | `dim_catalog` | 1:N | 1:many / optional | many:1 / optional | A listing may have no catalog, and a catalog may have no listings. |
| `fact_inventory_position` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each inventory position belongs to exactly one variant, and a variant may have no inventory positions. |
| `fact_inventory_position` | `seller_warehouse_id` | `dim_seller_warehouse` | 1:N | 1:many / optional | many:1 / optional | An inventory position may have no seller warehouse, and a seller warehouse may have no inventory positions. |
| `fact_inventory_position` | `fulfillment_center_id` | `dim_fulfillment_center` | 1:N | 1:many / optional | many:1 / optional | An inventory position may have no fulfillment center, and a fulfillment center may have no inventory positions. |
| `fact_inventory_reservation` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each reservation belongs to exactly one variant, and a variant may have no reservations. |
| `fact_inventory_reservation` | `order_line_id` | `fact_order_line` | 1:N | 1:many / optional | many:1 / optional | A reservation may have no order line, and an order line may have no reservations. |
| `fact_inventory_reservation` | `seller_warehouse_id` | `dim_seller_warehouse` | 1:N | 1:many / optional | many:1 / optional | A reservation may have no seller warehouse, and a seller warehouse may have no reservations. |
| `fact_cart` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / always | Each cart belongs to exactly one buyer account, and a buyer account may have no carts. |
| `fact_cart` | `buyer_user_id` | `dim_buyer_user` | 1:N | 1:many / optional | many:1 / optional | A cart may have no buyer user, and a buyer user may have no carts. |
| `fact_cart` | `channel_id` | `dim_channel` | 1:N | 1:many / optional | many:1 / always | Each cart belongs to exactly one channel, and a channel may have no carts. |
| `fact_cart` | `device_id` | `dim_device` | 1:N | 1:many / optional | many:1 / optional | A cart may have no device, and a device may have no carts. |
| `fact_cart_line` | `cart_id` | `fact_cart` | 1:N | 1:many / optional | many:1 / always | Each cart line belongs to exactly one cart, and a cart may have no cart lines. |
| `fact_cart_line` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each cart line belongs to exactly one variant, and a variant may have no cart lines. |
| `fact_cart_line` | `listing_id` | `fact_listing` | 1:N | 1:many / optional | many:1 / optional | A cart line may have no listing, and a listing may have no cart lines. |
| `fact_checkout` | `cart_id` | `fact_cart` | 1:N | 1:many / optional | many:1 / optional | A checkout may have no cart, and a cart may have no checkouts. |
| `fact_checkout` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / always | Each checkout belongs to exactly one buyer account, and a buyer account may have no checkouts. |
| `fact_checkout` | `address_id` | `dim_address` | 1:N | 1:many / optional | many:1 / optional | A checkout may have no address, and an address may have no checkouts. |
| `fact_checkout` | `shipping_method_id` | `dim_shipping_method` | 1:N | 1:many / optional | many:1 / optional | A checkout may have no shipping method, and a shipping method may have no checkouts. |
| `fact_order` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / always | Each order belongs to exactly one buyer account, and a buyer account may have no orders. |
| `fact_order` | `buyer_user_id` | `dim_buyer_user` | 1:N | 1:many / optional | many:1 / optional | An order may have no buyer user, and a buyer user may have no orders. |
| `fact_order` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each order belongs to exactly one seller, and a seller may have no orders. |
| `fact_order` | `marketplace_id` | `dim_marketplace` | 1:N | 1:many / optional | many:1 / always | Each order belongs to exactly one marketplace, and a marketplace may have no orders. |
| `fact_order` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each order uses exactly one currency, and a currency may have no orders. |
| `fact_order` | `ship_to_address_id` | `dim_address` | 1:N | 1:many / optional | many:1 / always | Each order ships to exactly one address, and an address may have no orders shipped to it. |
| `fact_order` | `channel_id` | `dim_channel` | 1:N | 1:many / optional | many:1 / always | Each order belongs to exactly one channel, and a channel may have no orders. |
| `fact_order` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each order belongs to exactly one calendar day, and a calendar day may have no orders. |
| `fact_order` | `contract_id` | `dim_contract` | 1:N | 1:many / optional | many:1 / optional | An order may have no contract, and a contract may have no orders. |
| `fact_order_bill_to` | `order_id` | `fact_order` | 1:1 | 1:1 / optional | 1:1 / always | Each bill-to record matches exactly one order, an order has at most one bill-to record, and an order may have no bill-to record. |
| `fact_order_bill_to` | `address_id` | `dim_address` | 1:N | 1:many / optional | many:1 / always | Each bill-to record names exactly one address, and an address may have no bill-to records. |
| `fact_order_line` | `order_id` | `fact_order` | 1:N | 1:many / always | many:1 / always | Every order includes one or more order lines, and each order line belongs to exactly one order. |
| `fact_order_line` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each order line belongs to exactly one variant, and a variant may have no order lines. |
| `fact_order_line` | `listing_id` | `fact_listing` | 1:N | 1:many / optional | many:1 / optional | An order line may have no listing, and a listing may have no order lines. |
| `fact_order_line` | `seller_storefront_id` | `dim_seller_storefront` | 1:N | 1:many / optional | many:1 / always | Each order line belongs to exactly one storefront, and a storefront may have no order lines. |
| `fact_order_allocation` | `order_line_id` | `fact_order_line` | 1:N | 1:many / always | many:1 / always | Every order line includes one or more allocations, and each allocation belongs to exactly one order line. |
| `fact_order_allocation` | `seller_warehouse_id` | `dim_seller_warehouse` | 1:N | 1:many / optional | many:1 / optional | An allocation may have no seller warehouse, and a seller warehouse may have no allocations. |
| `fact_order_allocation` | `fulfillment_center_id` | `dim_fulfillment_center` | 1:N | 1:many / optional | many:1 / optional | An allocation may have no fulfillment center, and a fulfillment center may have no allocations. |
| `fact_shipment` | `order_id` | `fact_order` | 1:N | 1:many / optional | many:1 / always | Each shipment belongs to exactly one order, and an order may have no shipments. |
| `fact_shipment` | `carrier_service_id` | `dim_carrier_service` | 1:N | 1:many / optional | many:1 / optional | A shipment may have no carrier service, and a carrier service may have no shipments. |
| `fact_shipment` | `fulfillment_center_id` | `dim_fulfillment_center` | 1:N | 1:many / optional | many:1 / optional | A shipment may have no fulfillment center, and a fulfillment center may have no shipments. |
| `fact_shipment` | `seller_warehouse_id` | `dim_seller_warehouse` | 1:N | 1:many / optional | many:1 / optional | A shipment may have no seller warehouse, and a seller warehouse may have no shipments. |
| `fact_shipment` | `ship_date_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / optional | A shipment may have no ship date, and a calendar day may have no shipments dated on it. |
| `fact_shipment_line` | `shipment_id` | `fact_shipment` | 1:N | 1:many / always | many:1 / always | Every shipment includes one or more shipment lines, and each shipment line belongs to exactly one shipment. |
| `fact_shipment_line` | `order_line_id` | `fact_order_line` | 1:N | 1:many / optional | many:1 / always | Each shipment line belongs to exactly one order line, and an order line may have no shipment lines. |
| `fact_shipment_event` | `shipment_id` | `fact_shipment` | 1:N | 1:many / always | many:1 / always | Every shipment includes one or more shipment events, and each shipment event belongs to exactly one shipment. |
| `fact_shipment_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each shipment event belongs to exactly one calendar day, and a calendar day may have no shipment events. |
| `fact_delivery` | `shipment_id` | `fact_shipment` | 1:N | 1:many / optional | many:1 / always | Each delivery belongs to exactly one shipment, and a shipment may have no deliveries. |
| `fact_delivery` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / optional | A delivery may have no calendar day, and a calendar day may have no deliveries. |
| `fact_payment_authorization` | `order_id` | `fact_order` | 1:N | 1:many / optional | many:1 / optional | An authorization may have no order, and an order may have no authorizations. |
| `fact_payment_authorization` | `payment_method_id` | `dim_payment_method` | 1:N | 1:many / optional | many:1 / always | Each authorization belongs to exactly one payment method, and a payment method may have no authorizations. |
| `fact_payment_authorization` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each authorization uses exactly one currency, and a currency may have no authorizations. |
| `fact_payment_authorization` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each authorization belongs to exactly one calendar day, and a calendar day may have no authorizations. |
| `fact_payment_capture` | `authorization_id` | `fact_payment_authorization` | 1:N | 1:many / optional | many:1 / optional | A capture may have no authorization, and an authorization may have no captures. |
| `fact_payment_capture` | `order_id` | `fact_order` | 1:N | 1:many / optional | many:1 / always | Each capture belongs to exactly one order, and an order may have no captures. |
| `fact_payment_capture` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each capture uses exactly one currency, and a currency may have no captures. |
| `fact_refund` | `capture_id` | `fact_payment_capture` | 1:N | 1:many / optional | many:1 / optional | A refund may have no capture, and a capture may have no refunds. |
| `fact_refund` | `order_id` | `fact_order` | 1:N | 1:many / optional | many:1 / always | Each refund belongs to exactly one order, and an order may have no refunds. |
| `fact_refund` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / always | Each refund cites exactly one reason code, and a reason code may have no refunds. |
| `fact_refund` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each refund uses exactly one currency, and a currency may have no refunds. |
| `fact_chargeback` | `capture_id` | `fact_payment_capture` | 1:N | 1:many / optional | many:1 / always | Each chargeback belongs to exactly one capture, and a capture may have no chargebacks. |
| `fact_chargeback` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / always | Each chargeback cites exactly one reason code, and a reason code may have no chargebacks. |
| `fact_chargeback` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each chargeback uses exactly one currency, and a currency may have no chargebacks. |
| `fact_seller_settlement` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each seller settlement belongs to exactly one seller, and a seller may have no settlements. |
| `fact_seller_settlement` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each seller settlement uses exactly one currency, and a currency may have no settlements. |
| `fact_seller_settlement` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each seller settlement belongs to exactly one calendar day, and a calendar day may have no settlements. |
| `fact_settlement_line` | `seller_settlement_id` | `fact_seller_settlement` | 1:N | 1:many / always | many:1 / always | Every seller settlement includes one or more settlement lines, and each settlement line belongs to exactly one seller settlement. |
| `fact_settlement_line` | `order_line_id` | `fact_order_line` | 1:N | 1:many / optional | many:1 / optional | A settlement line may have no order line, and an order line may have no settlement lines. |
| `fact_settlement_line` | `fee_schedule_id` | `dim_fee_schedule` | 1:N | 1:many / optional | many:1 / optional | A settlement line may have no fee schedule, and a fee schedule may have no settlement lines. |
| `fact_commission` | `order_line_id` | `fact_order_line` | 1:N | 1:many / optional | many:1 / always | Each commission belongs to exactly one order line, and an order line may have no commissions. |
| `fact_commission` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each commission belongs to exactly one seller, and a seller may have no commissions. |
| `fact_commission` | `fee_schedule_id` | `dim_fee_schedule` | 1:N | 1:many / optional | many:1 / optional | A commission may have no fee schedule, and a fee schedule may have no commissions. |
| `fact_fee_assessment` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each fee assessment belongs to exactly one seller, and a seller may have no fee assessments. |
| `fact_fee_assessment` | `fee_schedule_id` | `dim_fee_schedule` | 1:N | 1:many / optional | many:1 / always | Each fee assessment belongs to exactly one fee schedule, and a fee schedule may have no fee assessments. |
| `fact_fee_assessment` | `seller_settlement_id` | `fact_seller_settlement` | 1:N | 1:many / optional | many:1 / optional | A fee assessment may have no seller settlement, and a seller settlement may have no fee assessments. |
| `fact_fee_assessment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each fee assessment belongs to exactly one calendar day, and a calendar day may have no fee assessments. |
| `fact_invoice` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / always | Each invoice belongs to exactly one buyer account, and a buyer account may have no invoices. |
| `fact_invoice` | `order_id` | `fact_order` | 1:N | 1:many / optional | many:1 / optional | An invoice may have no order, and an order may have no invoices. |
| `fact_invoice` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each invoice uses exactly one currency, and a currency may have no invoices. |
| `fact_invoice` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each invoice belongs to exactly one calendar day, and a calendar day may have no invoices. |
| `fact_invoice_line` | `invoice_id` | `fact_invoice` | 1:N | 1:many / always | many:1 / always | Every invoice includes one or more invoice lines, and each invoice line belongs to exactly one invoice. |
| `fact_invoice_line` | `order_line_id` | `fact_order_line` | 1:N | 1:many / optional | many:1 / optional | An invoice line may have no order line, and an order line may have no invoice lines. |
| `fact_invoice_line` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / always | Each invoice line belongs to exactly one ledger account, and a ledger account may have no invoice lines. |
| `fact_buyer_payment` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / always | Each buyer payment belongs to exactly one buyer account, and a buyer account may have no buyer payments. |
| `fact_buyer_payment` | `invoice_id` | `fact_invoice` | 1:N | 1:many / optional | many:1 / optional | A buyer payment may have no invoice, and an invoice may have no buyer payments. |
| `fact_buyer_payment` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each buyer payment uses exactly one currency, and a currency may have no buyer payments. |
| `fact_buyer_payment` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each buyer payment belongs to exactly one calendar day, and a calendar day may have no buyer payments. |
| `fact_return_request` | `order_id` | `fact_order` | 1:N | 1:many / optional | many:1 / always | Each return request belongs to exactly one order, and an order may have no return requests. |
| `fact_return_request` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / always | Each return request belongs to exactly one buyer account, and a buyer account may have no return requests. |
| `fact_return_request` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / always | Each return request cites exactly one reason code, and a reason code may have no return requests. |
| `fact_return_request` | `return_policy_id` | `dim_return_policy` | 1:N | 1:many / optional | many:1 / optional | A return request may have no return policy, and a return policy may have no return requests. |
| `fact_return_line` | `return_request_id` | `fact_return_request` | 1:N | 1:many / always | many:1 / always | Every return request includes one or more return lines, and each return line belongs to exactly one return request. |
| `fact_return_line` | `order_line_id` | `fact_order_line` | 1:N | 1:many / optional | many:1 / always | Each return line belongs to exactly one order line, and an order line may have no return lines. |
| `fact_return_inspection` | `return_line_id` | `fact_return_line` | 1:N | 1:many / always | many:1 / always | Every return line includes one or more inspections, and each inspection belongs to exactly one return line. |
| `fact_return_inspection` | `fulfillment_center_id` | `dim_fulfillment_center` | 1:N | 1:many / optional | many:1 / optional | An inspection may have no fulfillment center, and a fulfillment center may have no inspections. |
| `fact_review` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each review belongs to exactly one variant, and a variant may have no reviews. |
| `fact_review` | `buyer_user_id` | `dim_buyer_user` | 1:N | 1:many / optional | many:1 / optional | A review may have no buyer user, and a buyer user may have no reviews. |
| `fact_review` | `review_topic_id` | `dim_review_topic` | 1:N | 1:many / optional | many:1 / optional | A review may have no review topic, and a review topic may have no reviews. |
| `fact_review` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each review belongs to exactly one calendar day, and a calendar day may have no reviews. |
| `fact_question` | `product_id` | `dim_product` | 1:N | 1:many / optional | many:1 / always | Each question belongs to exactly one product, and a product may have no questions. |
| `fact_question` | `buyer_user_id` | `dim_buyer_user` | 1:N | 1:many / optional | many:1 / optional | A question may have no buyer user, and a buyer user may have no questions. |
| `fact_question` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each question belongs to exactly one calendar day, and a calendar day may have no questions. |
| `fact_support_case` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / optional | A support case may have no buyer account, and a buyer account may have no support cases. |
| `fact_support_case` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / optional | A support case may have no seller, and a seller may have no support cases. |
| `fact_support_case` | `support_queue_id` | `dim_support_queue` | 1:N | 1:many / optional | many:1 / always | Each support case belongs to exactly one support queue, and a support queue may have no cases. |
| `fact_support_case` | `order_id` | `fact_order` | 1:N | 1:many / optional | many:1 / optional | A support case may have no order, and an order may have no support cases. |
| `fact_support_case` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / optional | A support case may have no reason code, and a reason code may have no support cases. |
| `fact_support_message` | `support_case_id` | `fact_support_case` | 1:N | 1:many / always | many:1 / always | Every support case includes one or more messages, and each message belongs to exactly one support case. |
| `fact_support_message` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A support message may have no employee, and an employee may have no support messages. |
| `fact_support_message` | `buyer_user_id` | `dim_buyer_user` | 1:N | 1:many / optional | many:1 / optional | A support message may have no buyer user, and a buyer user may have no support messages. |
| `fact_ad_impression` | `campaign_id` | `dim_campaign` | 1:N | 1:many / optional | many:1 / always | Each impression belongs to exactly one campaign, and a campaign may have no impressions. |
| `fact_ad_impression` | `ad_placement_id` | `dim_ad_placement` | 1:N | 1:many / optional | many:1 / always | Each impression belongs to exactly one ad placement, and an ad placement may have no impressions. |
| `fact_ad_impression` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each impression belongs to exactly one calendar day, and a calendar day may have no impressions. |
| `fact_ad_impression` | `device_id` | `dim_device` | 1:N | 1:many / optional | many:1 / optional | An impression may have no device, and a device may have no impressions. |
| `fact_ad_click` | `impression_id` | `fact_ad_impression` | 1:N | 1:many / optional | many:1 / optional | A click may have no impression, and an impression may have no clicks. |
| `fact_ad_click` | `campaign_id` | `dim_campaign` | 1:N | 1:many / optional | many:1 / always | Each click belongs to exactly one campaign, and a campaign may have no clicks. |
| `fact_ad_click` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each click belongs to exactly one calendar day, and a calendar day may have no clicks. |
| `fact_search_event` | `buyer_user_id` | `dim_buyer_user` | 1:N | 1:many / optional | many:1 / optional | A search event may have no buyer user, and a buyer user may have no search events. |
| `fact_search_event` | `channel_id` | `dim_channel` | 1:N | 1:many / optional | many:1 / always | Each search event belongs to exactly one channel, and a channel may have no search events. |
| `fact_search_event` | `device_id` | `dim_device` | 1:N | 1:many / optional | many:1 / optional | A search event may have no device, and a device may have no search events. |
| `fact_search_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each search event belongs to exactly one calendar day, and a calendar day may have no search events. |
| `fact_page_view` | `product_id` | `dim_product` | 1:N | 1:many / optional | many:1 / optional | A page view may have no product, and a product may have no page views. |
| `fact_page_view` | `listing_id` | `fact_listing` | 1:N | 1:many / optional | many:1 / optional | A page view may have no listing, and a listing may have no page views. |
| `fact_page_view` | `channel_id` | `dim_channel` | 1:N | 1:many / optional | many:1 / always | Each page view belongs to exactly one channel, and a channel may have no page views. |
| `fact_page_view` | `device_id` | `dim_device` | 1:N | 1:many / optional | many:1 / optional | A page view may have no device, and a device may have no page views. |
| `fact_page_view` | `traffic_source_id` | `dim_traffic_source` | 1:N | 1:many / optional | many:1 / optional | A page view may have no traffic source, and a traffic source may have no page views. |
| `fact_page_view` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each page view belongs to exactly one calendar day, and a calendar day may have no page views. |
| `fact_subscription` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / always | Each subscription belongs to exactly one buyer account, and a buyer account may have no subscriptions. |
| `fact_subscription` | `plan_id` | `dim_subscription_plan` | 1:N | 1:many / optional | many:1 / always | Each subscription belongs to exactly one plan, and a plan may have no subscriptions. |
| `fact_subscription` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / optional | A subscription may have no variant, and a variant may have no subscriptions. |
| `fact_subscription_invoice` | `subscription_id` | `fact_subscription` | 1:N | 1:many / always | many:1 / always | Every subscription includes one or more subscription invoices, and each subscription invoice belongs to exactly one subscription. |
| `fact_subscription_invoice` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each subscription invoice uses exactly one currency, and a currency may have no subscription invoices. |
| `fact_subscription_invoice` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each subscription invoice belongs to exactly one calendar day, and a calendar day may have no subscription invoices. |
| `fact_fraud_decision` | `order_id` | `fact_order` | 1:N | 1:many / optional | many:1 / optional | A fraud decision may have no order, and an order may have no fraud decisions. |
| `fact_fraud_decision` | `checkout_id` | `fact_checkout` | 1:N | 1:many / optional | many:1 / optional | A fraud decision may have no checkout, and a checkout may have no fraud decisions. |
| `fact_fraud_decision` | `fraud_rule_id` | `dim_fraud_rule` | 1:N | 1:many / optional | many:1 / optional | A fraud decision may have no fraud rule, and a fraud rule may have no decisions. |
| `fact_fraud_decision` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each fraud decision belongs to exactly one calendar day, and a calendar day may have no fraud decisions. |
| `fact_price_change` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each price change belongs to exactly one variant, and a variant may have no price changes. |
| `fact_price_change` | `price_list_id` | `dim_price_list` | 1:N | 1:many / optional | many:1 / optional | A price change may have no price list, and a price list may have no price changes. |
| `fact_price_change` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each price change belongs to exactly one calendar day, and a calendar day may have no price changes. |
| `fact_quote` | `buyer_account_id` | `dim_buyer_account` | 1:N | 1:many / optional | many:1 / always | Each quote belongs to exactly one buyer account, and a buyer account may have no quotes. |
| `fact_quote` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each quote belongs to exactly one seller, and a seller may have no quotes. |
| `fact_quote` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A quote may have no employee, and an employee may have no quotes. |
| `fact_quote` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each quote uses exactly one currency, and a currency may have no quotes. |
| `fact_quote` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each quote belongs to exactly one calendar day, and a calendar day may have no quotes. |
| `fact_quote_line` | `quote_id` | `fact_quote` | 1:N | 1:many / always | many:1 / always | Every quote includes one or more quote lines, and each quote line belongs to exactly one quote. |
| `fact_quote_line` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each quote line belongs to exactly one variant, and a variant may have no quote lines. |
| `fact_backorder` | `order_line_id` | `fact_order_line` | 1:N | 1:many / optional | many:1 / always | Each backorder belongs to exactly one order line, and an order line may have no backorders. |
| `fact_backorder` | `variant_id` | `dim_variant` | 1:N | 1:many / optional | many:1 / always | Each backorder belongs to exactly one variant, and a variant may have no backorders. |
| `fact_sla_breach` | `order_id` | `fact_order` | 1:N | 1:many / optional | many:1 / optional | A service breach may have no order, and an order may have no service breaches. |
| `fact_sla_breach` | `shipment_id` | `fact_shipment` | 1:N | 1:many / optional | many:1 / optional | A service breach may have no shipment, and a shipment may have no service breaches. |
| `fact_sla_breach` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each service breach belongs to exactly one seller, and a seller may have no service breaches. |
| `fact_sla_breach` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each service breach belongs to exactly one calendar day, and a calendar day may have no service breaches. |
| `fact_customs_declaration` | `shipment_id` | `fact_shipment` | 1:N | 1:many / optional | many:1 / always | Each customs declaration belongs to exactly one shipment, and a shipment may have no customs declarations. |
| `fact_customs_declaration` | `hs_code_id` | `dim_hs_code` | 1:N | 1:many / optional | many:1 / optional | A customs declaration may have no harmonized-system code, and a harmonized-system code may have no declarations. |
| `fact_customs_declaration` | `country_id` | `dim_country` | 1:N | 1:many / optional | many:1 / always | Each customs declaration belongs to exactly one country, and a country may have no customs declarations. |
| `fact_listing_suppression` | `listing_id` | `fact_listing` | 1:N | 1:many / optional | many:1 / always | Each suppression belongs to exactly one listing, and a listing may have no suppressions. |
| `fact_listing_suppression` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / always | Each suppression cites exactly one reason code, and a reason code may have no suppressions. |
| `fact_listing_suppression` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each suppression belongs to exactly one calendar day, and a calendar day may have no suppressions. |
| `fact_package` | `shipment_id` | `fact_shipment` | 1:N | 1:many / always | many:1 / always | Every shipment includes one or more packages, and each package belongs to exactly one shipment. |
| `fact_package` | `package_type_id` | `dim_package_type` | 1:N | 1:many / optional | many:1 / always | Each package uses exactly one package type, and a package type may have no packages. |
| `fact_payout` | `seller_settlement_id` | `fact_seller_settlement` | 1:N | 1:many / optional | many:1 / always | Each payout belongs to exactly one seller settlement, and a seller settlement may have no payouts. |
| `fact_payout` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / always | Each payout belongs to exactly one seller, and a seller may have no payouts. |
| `fact_payout` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Each payout uses exactly one currency, and a currency may have no payouts. |
| `fact_payout` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each payout belongs to exactly one calendar day, and a calendar day may have no payouts. |
| `fact_answer` | `question_id` | `fact_question` | 1:N | 1:many / always | many:1 / always | Every question includes one or more answers, and each answer belongs to exactly one question. |
| `fact_answer` | `seller_id` | `dim_seller` | 1:N | 1:many / optional | many:1 / optional | An answer may have no seller, and a seller may have no answers. |
| `fact_answer` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | An answer may have no employee, and an employee may have no answers. |
| `fact_answer` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Each answer belongs to exactly one calendar day, and a calendar day may have no answers. |

## Dataset inventory

### advertising

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_campaign` | dimension | `campaign_id` | Advertising campaign owned by a seller. |
| `dim_ad_placement` | dimension | `ad_placement_id` | Placement where a campaign can show an advertisement. |
| `fact_ad_impression` | fact | `impression_id` | Impression of a campaign on an ad placement. |
| `fact_ad_click` | fact | `click_id` | Click recorded for a campaign. |

### bridge

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `bridge_product_category` | bridge | `product_category_id` | Assignment of a product to a category. |
| `bridge_variant_attribute` | bridge | `variant_attribute_id` | Assignment of an attribute to a variant. |
| `bridge_catalog_product` | bridge | `catalog_product_id` | Placement of a product in a seller catalog. |
| `bridge_price_list_variant` | bridge | `price_list_variant_id` | Price of a variant on a seller price list. |
| `bridge_contract_price` | bridge | `contract_price_id` | Negotiated price of a variant on a contract. |
| `bridge_promotion_variant` | bridge | `promotion_variant_id` | Variant targeted by a promotion. |
| `bridge_seller_category` | bridge | `seller_category_id` | Authorization for a seller to sell in a category. |
| `bridge_buyer_address` | bridge | `buyer_address_id` | Link between a buyer account and an address. |
| `bridge_bundle_component` | bridge | `bundle_component_id` | Component variant required by a bundle. |
| `bridge_campaign_placement` | bridge | `campaign_placement_id` | Placement booked for an advertising campaign. |
| `bridge_product_compatibility` | bridge | `compatibility_id` | Membership of one variant in a compatibility group. |
| `bridge_coupon_variant` | bridge | `coupon_variant_id` | Variant that a coupon can discount. |

### calendar

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_calendar_day` | dimension | `calendar_day_id` | Calendar day used to date commerce documents. |

### cart

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_cart` | fact | `cart_id` | Shopping cart owned by a buyer account. |
| `fact_cart_line` | fact | `cart_line_id` | Line on a cart for a variant the buyer intends to purchase. |

### catalog

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_catalog` | dimension | `catalog_id` | Assortment of products published by a seller. |
| `dim_category` | dimension | `category_id` | Product category that classifies products without a parent category link. |
| `dim_brand` | dimension | `brand_id` | Brand that may be named on a product. |
| `dim_product` | dimension | `product_id` | Commercial item a seller presents in the catalog. |
| `dim_variant` | dimension | `variant_id` | Sellable unit of a product that inventory and orders move. |
| `dim_attribute` | dimension | `attribute_id` | Descriptive attribute that can be assigned to a variant. |
| `dim_media_asset` | dimension | `media_asset_id` | Media file that may illustrate a product. |
| `dim_uom` | dimension | `uom_id` | Unit in which a variant is stocked and sold. |
| `dim_hs_code` | dimension | `hs_code_id` | Harmonized-system code available for a customs declaration. |
| `dim_bundle` | dimension | `bundle_id` | Sellable bundle whose parent is one variant. |
| `dim_compatibility_group` | dimension | `compatibility_group_id` | Set of variants that can be used together. |

### channel

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_channel` | dimension | `channel_id` | Selling channel through which a buyer acts. |
| `dim_device` | dimension | `device_id` | Device class a buyer may use. |
| `dim_locale` | dimension | `locale_id` | Locale available for marketplace presentation. |
| `dim_traffic_source` | dimension | `traffic_source_id` | Source that may refer a buyer to a page view. |

### checkout

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_checkout` | fact | `checkout_id` | Attempt to convert a cart into an order. |

### commercial

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_price_list` | dimension | `price_list_id` | Seller schedule of variant prices in one currency. |
| `dim_contract` | dimension | `contract_id` | Negotiated agreement between one seller and one buyer account. |
| `dim_currency` | dimension | `currency_id` | Currency used to price and settle commerce documents. |
| `dim_payment_method` | dimension | `payment_method_id` | Instrument a buyer account uses to pay through a provider. |
| `dim_payment_provider` | dimension | `payment_provider_id` | Provider that processes buyer payment methods. |
| `dim_incoterm` | dimension | `incoterm_id` | Trade term available for cross-border commerce. |

### content

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_review` | fact | `review_id` | Review a buyer wrote for a variant. |
| `fact_question` | fact | `question_id` | Question a buyer asked about a product. |
| `fact_answer` | fact | `answer_id` | Answer posted to a product question. |

### finance

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_gl_account` | dimension | `gl_account_id` | General-ledger account used on an invoice line. |
| `dim_fee_schedule` | dimension | `fee_schedule_id` | Fee schedule that applies to one seller tier. |

### fulfillment

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_shipping_method` | dimension | `shipping_method_id` | Buyer-facing shipping choice that may name a carrier. |
| `dim_carrier` | dimension | `carrier_id` | Carrier that moves shipments for the marketplace. |
| `dim_carrier_service` | dimension | `carrier_service_id` | Service level offered by a carrier. |
| `dim_seller_warehouse` | dimension | `seller_warehouse_id` | Warehouse a seller uses to hold inventory. |
| `dim_fulfillment_center` | dimension | `fulfillment_center_id` | Marketplace fulfillment center that can ship seller goods. |
| `dim_package_type` | dimension | `package_type_id` | Package type used when a shipment is packed. |
| `fact_shipment` | fact | `shipment_id` | Shipment of goods for one order. |
| `fact_shipment_line` | fact | `shipment_line_id` | Order-line quantity included on a shipment. |
| `fact_shipment_event` | fact | `shipment_event_id` | Scan event recorded against a shipment. |
| `fact_delivery` | fact | `delivery_id` | Delivery confirmation for a shipment. |
| `fact_package` | fact | `package_id` | Package packed for a shipment. |

### inventory

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_inventory_position` | fact | `inventory_position_id` | Available units of a variant at a warehouse or fulfillment center. |
| `fact_inventory_reservation` | fact | `reservation_id` | Units of a variant reserved, optionally for an order line. |

### invoice

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_invoice` | fact | `invoice_id` | Invoice issued to a buyer account. |
| `fact_invoice_line` | fact | `invoice_line_id` | Line on a buyer invoice posted to a ledger account. |
| `fact_buyer_payment` | fact | `buyer_payment_id` | Payment received from a buyer account. |

### listing

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_listing` | fact | `listing_id` | Offer a storefront publishes for one variant. |
| `fact_listing_suppression` | fact | `suppression_id` | Suppression applied to a listing for a stated reason. |

### order

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_order` | fact | `order_id` | Commercial commitment by a buyer account to purchase from a seller. |
| `fact_order_bill_to` | fact | `order_bill_to_id` | Optional billing address recorded for one order. |
| `fact_order_line` | fact | `order_line_id` | Variant quantity purchased on an order from one storefront. |
| `fact_order_allocation` | fact | `allocation_id` | Quantity of an order line allocated to a warehouse or fulfillment center. |
| `fact_backorder` | fact | `backorder_id` | Unfilled demand recorded against an order line. |

### organization

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_marketplace` | dimension | `marketplace_id` | Marketplace that hosts sellers and sells to business buyers and consumers. |
| `dim_country` | dimension | `country_id` | Country used for seller, buyer, warehouse, and customs geography. |
| `dim_region` | dimension | `region_id` | Region contained by one country. |
| `dim_support_queue` | dimension | `support_queue_id` | Queue that receives marketplace support cases. |

### party

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_employee` | dimension | `employee_id` | Marketplace employee who can manage a seller account. |
| `dim_seller_tier` | dimension | `seller_tier_id` | Commercial tier that groups sellers for fee treatment. |
| `dim_seller` | dimension | `seller_id` | Merchant that sells on the marketplace through one or more storefronts. |
| `dim_seller_storefront` | dimension | `seller_storefront_id` | Shop operated by a seller to publish listings in one currency. |
| `dim_buyer_segment` | dimension | `buyer_segment_id` | Segment used to classify buyer accounts. |
| `dim_buyer_account` | dimension | `buyer_account_id` | Account that purchases as a business or as a consumer. |
| `dim_buyer_user` | dimension | `buyer_user_id` | Person who acts for a buyer account. |
| `dim_address` | dimension | `address_id` | Address used for billing, shipping, or returns. |
| `dim_consumer` | dimension | `consumer_id` | Consumer profile that extends one buyer user. |

### payment

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_payment_authorization` | fact | `authorization_id` | Authorization of a payment method, optionally before an order exists. |
| `fact_payment_capture` | fact | `capture_id` | Capture of funds for an order. |
| `fact_refund` | fact | `refund_id` | Refund of captured funds for an order. |
| `fact_chargeback` | fact | `chargeback_id` | Chargeback raised against a payment capture. |
| `fact_payout` | fact | `payout_id` | Payout of a seller settlement to the seller. |

### policy

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_return_policy` | dimension | `return_policy_id` | Return policy published by a seller. |

### pricing

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_price_change` | fact | `price_change_id` | Recorded change to the price of a variant. |

### promotion

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_promotion` | dimension | `promotion_id` | Promotion that may be funded by a seller. |
| `dim_coupon` | dimension | `coupon_id` | Coupon that may be issued under a promotion. |

### quote

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_quote` | fact | `quote_id` | Quote a seller offers to a buyer account. |
| `fact_quote_line` | fact | `quote_line_id` | Variant quantity and price offered on a quote. |

### reference

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_reason_code` | dimension | `reason_code_id` | Reason code used on refunds, returns, and suppressions. |
| `dim_review_topic` | dimension | `review_topic_id` | Topic a product review may address. |

### returns

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_return_request` | fact | `return_request_id` | Request to return goods from an order. |
| `fact_return_line` | fact | `return_line_id` | Order-line quantity included on a return request. |
| `fact_return_inspection` | fact | `return_inspection_id` | Inspection result recorded for a return line. |

### service

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_support_case` | fact | `support_case_id` | Support case routed to a marketplace queue. |
| `fact_support_message` | fact | `support_message_id` | Message posted on a support case. |
| `fact_sla_breach` | fact | `sla_breach_id` | Service breach recorded against a seller. |

### settlement

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_seller_settlement` | fact | `seller_settlement_id` | Settlement of proceeds owed to a seller. |
| `fact_settlement_line` | fact | `settlement_line_id` | Line that builds the net amount of a seller settlement. |
| `fact_commission` | fact | `commission_id` | Commission assessed on an order line for a seller. |
| `fact_fee_assessment` | fact | `fee_assessment_id` | Fee charged to a seller under a fee schedule. |

### subscription

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_subscription_plan` | dimension | `plan_id` | Plan a buyer account may subscribe to, optionally from a seller. |
| `fact_subscription` | fact | `subscription_id` | Subscription a buyer account holds to a plan. |
| `fact_subscription_invoice` | fact | `subscription_invoice_id` | Invoice generated for a subscription. |

### trade

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_customs_declaration` | fact | `customs_declaration_id` | Customs declaration filed for a shipment. |

### traffic

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_search_event` | fact | `search_event_id` | Search a buyer submitted on a channel. |
| `fact_page_view` | fact | `page_view_id` | Page view of a product or listing on a channel. |

### trust

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_fraud_rule` | dimension | `fraud_rule_id` | Rule that a fraud decision may cite. |
| `fact_fraud_decision` | fact | `fraud_decision_id` | Fraud decision on a checkout or an order. |

## Provenance

This is an original marketplace operating ontology informed by publicly described commerce concepts (seller, catalog, listing, cart, order, payment capture, shipment, settlement). It is not a copy of Shopify, Amazon, or any vendor schema. No synthetic statistics are included.
