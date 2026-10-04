# Alderford Pump Company

## Introduction

Alderford Pump Company builds industrial centrifugal pumps at several plants, both as catalog make-to-stock machines and as engineer-to-order units. The catalog `manufacturing-discrete` is the ontology of that operating system: 113 datasets in the Snowflake database `MANUFACTURING_DISCRETE`, grouped as organization, product, party, inventory, quality, maintenance, finance, commercial, execution, procurement, and bridge.

The equipment hierarchy follows the ISA-95 shape. One enterprise has many legal entities, a plant belongs to one legal entity, and each plant has exactly one plant manager. Every plant has at least one area, every area has at least one production line, every line has at least one work center, and every work center has at least one work unit. Product structure is an item, its revisions, a bill of materials, and a routing. Execution, procurement, order-to-cash, quality, maintenance, and cost are event facts that reference those populations.

Each grain column is the complete population of its logical identity (`is_entity_universe: true`). A foreign key on another dataset is the same identity with `is_entity_universe: false`. The edge states directional multiplicity and whether a match is required. The questions below use only those authored identities, grains, and joins. Each question has one universe dataset per identity and one column set on each join, so the datasets and the relationship path are fixed by the metadata. Measure columns such as quantity and amount are attributes of a single fact row. The catalog does not store row counts or distributions.

The business narrative and the full relationship table are in `business-model.md`. Loadable YAML is in `yaml/`.

## BI questions

1. Who manages each plant, and which plants does a given employee manage?
   `manufacturing-discrete.organization.dim_plant.plant_manager_employee_id` joins `manufacturing-discrete.organization.dim_employee.employee_id` one-to-one. Every plant has a manager. An employee manages at most one plant.

2. What is the equipment hierarchy under a plant?
   `dim_plant` to `dim_area` to `dim_production_line` to `dim_work_center` to `dim_work_unit`, each hop `1:many` with a required match in both directions. Every plant, area, line, and work center has at least one child.

3. Which employees report to which manager?
   `manufacturing-discrete.bridge.bridge_employee_reporting` names `employee_id` and `reporting_manager_id`. `manufacturing-discrete.organization.dim_reporting_manager` joins that role to exactly one employee. The report and the manager are different columns, so the two roles stay distinct.

4. Which items are made or stocked at a plant, and what is each item's family, commodity, and base unit?
   `manufacturing-discrete.bridge.bridge_item_plant` joins `dim_item` and `dim_plant`. `dim_item` joins `dim_product_family`, `dim_commodity`, and `dim_unit_of_measure`. Every item has at least one revision on `dim_item_revision`.

5. What components, and which operation consumes them, are on the bill of materials for an item revision at a plant?
   `dim_bom_header` identifies the parent revision and plant. `bridge_bom_component` is `1:many` from that header and always matches a component item. The consuming operation is optional.

6. Which work centers perform the operations on a routing?
   `dim_routing_header` identifies the item revision and plant. `bridge_routing_operation` is `1:many` from that routing and joins `dim_operation` and `dim_work_center`.

7. For a production order, which operations were confirmed, in what good and scrap quantity, by whom, and on which work unit?
   `manufacturing-discrete.execution.fact_production_order` joins its item revision, plant, and optional routing and BOM. Every order has operations on `fact_production_order_operation`. `fact_operation_confirmation` records `good_quantity` and `scrap_quantity` and may name the work unit, shift, and employee.

8. How many labor hours did each employee book to a production-order operation, work center, and shift?
   `manufacturing-discrete.execution.fact_labor_ticket` is one ticket. It always joins `dim_employee`, `dim_work_center`, `dim_shift`, and `dim_calendar_day`. The production-order operation is optional, so indirect time stays on the ticket.

9. What quantity of each item was issued to a production order, and what quantity was received back into a location and lot?
   `fact_material_issue` joins the production order, item, and storage location, with an optional lot. `fact_production_receipt` joins the same order and the item revision, storage location, and optional lot.

10. What did each customer order, for which ship-to and promise date, and what shipped?
    `manufacturing-discrete.commercial.fact_sales_order` always joins `dim_customer` and `dim_customer_ship_to`. Every order has lines on `fact_sales_order_line`, and every line has promise schedules on `fact_sales_order_schedule`. `fact_shipment_line` may join the sales-order line, so a line can ship in more than one shipment.

11. What has been purchased from each supplier site, and what has been received?
    `fact_purchase_order` joins `dim_supplier` and `dim_supplier_site`. Every supplier has at least one site. Every purchase order has lines, and every line has at least one schedule. `fact_goods_receipt` joins the purchase-order line and the receiving storage location.

12. Which supplier sites are approved to furnish an item?
    `manufacturing-discrete.bridge.bridge_supplier_item` joins `dim_supplier`, `dim_item`, and optionally `dim_supplier_site`.

13. Where is on-hand inventory, and how did a lot become another lot?
    `fact_inventory_balance` is one balance of an item in a storage location and inventory status, with an optional lot. A genealogy link on `fact_lot_genealogy` names the parent lot. The child lot is a separate row on `fact_lot_descendant`, joined one-to-one to that link. Source and destination locations of a movement are also separate: `from_storage_location_id` stays on `fact_inventory_transaction`, and the destination is `fact_inventory_destination`.

14. Which nonconformances are open against an item revision, and what disposition did each receive?
    `manufacturing-discrete.quality.fact_nonconformance` joins the item revision, plant, and defect code. Every nonconformance has at least one row on `fact_ncr_disposition`, joined to `dim_disposition_code` and the deciding employee.

15. What standard cost and purchase-price variance apply to an item revision?
    `manufacturing-discrete.finance.fact_standard_cost` joins the item revision and plant. `fact_purchase_price_variance` joins the purchase-order line, the item revision, and the variance account.
