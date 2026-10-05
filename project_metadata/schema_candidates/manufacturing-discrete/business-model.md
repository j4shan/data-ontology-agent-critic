# Alderford Pump Company

Alderford Pump Company is a discrete manufacturer of industrial centrifugal pumps for water, chemical, and process service. The company runs several plants and builds both make-to-stock catalog pumps and engineer-to-order machines whose materials, seals, and hydraulics are specified for a duty. This catalog is the warehouse-style ontology of that operating system: conformed dimensions, bridges, and event facts. Statistics are not authored.

Organization follows the public ISA-95 and IEC 62264 equipment hierarchy. The enterprise is the company. Legal entities own the plants. A plant is the site, also called a factory, where planning, production, stores, and shipping occur. One plant has many areas, and one plant has exactly one plant manager. An employee manages at most one plant. An area holds many production lines, a production line holds many work centers, and one work center has many work units. A work center is a resource, and a work unit is the machine or station that reports quantity. Departments, shifts, cost centers, and profit centers align people and money to those sites. Employees have a home plant and a department. A reporting line names the employee and a reporting-manager role, and that role is exactly one employee. A planner and a line supervisor are employees in one-to-one roles, and those roles do not cover every employee.

The product master treats an item as a material or a part, with a product family, a commodity, and a base unit of measure. Item type is make, buy, or phantom, and every item has at least one revision. Engineering documents and engineering changes control the revision. A bill of materials is a header for a parent item revision at a plant. One BOM has many components, each naming a component item and optionally the consuming operation. A routing header defines the process for an item revision at a plant, and one routing has many operations performed at work centers. Tools stay with a plant. Bridges record where an item is made, which skills a person or work center holds, which customers buy the item, and which supplier site can furnish it.

Planning uses a demand forecast and a master production schedule by item, plant, and day. Planned orders firm into production orders. A production order names the item revision and plant and may name the routing, the BOM, and the planner. Every production order has many operations. The shop records confirmations of good and scrap quantity, labor hours, material issues, and production receipts. Capacity load and kanban signals coordinate work centers and internal replenishment. Inventory sits in plant warehouses, and one warehouse has many storage locations. Balances, transactions, lots, serials, genealogy, and cycle counts describe what is on hand and how it moved. A transaction may be a receipt, issue, transfer, adjustment, or scrap.

Procurement runs from an employee requisition to a purchase order at a supplier site. One supplier has many sites. One purchase order has many lines, and every line includes at least one schedule, then goods receipt, supplier invoice, payment, and return. Order to cash starts with a quote. A sales order names the customer, ship-to, fulfilling plant, channel, currency, and payment term, and it may name a representative and an incoterm. One sales order has many lines, and each line has at least one promise-date schedule. Shipments, invoices, payments, and returns close the cycle. A customer has many ship-to addresses.

Quality records inspection results against a characteristic, with outcomes of pass, fail, or waiver. A nonconformance names a defect, and every nonconformance includes at least one disposition. Scrap and tool calibration complete that chain. Maintenance records assets, downtime, work orders, labor, and spare consumption. Cost records standard cost by item revision and plant, absorption to a production order, purchase-price variance, and freight. No row counts or distributions are authored.

## Data ecosystem

The authored catalog `manufacturing-discrete` contains 114 datasets (51 dimensions, 51 facts, 12 bridges) in the Snowflake database `MANUFACTURING_DISCRETE` on account `alderford.us-east-1`.

Each dataset is one ontology node. The grain column is the system of record for that dataset's logical identity and is marked `is_entity_universe: true`. Foreign-key columns realize the same logical identity with `is_entity_universe: false`, because the child dataset does not hold the complete population. Edges join those two realizations. Multiplicity and match existence are directional and follow the operating rules below. Row counts, distinct counts, and other data statistics are intentionally absent.

## Signature relationships

| Relationship | Identity | Parent to child | Child to parent | Rule |
| --- | --- | --- | --- | --- |
| `dim_plant` to `dim_area` | `plant_identity` | 1:many (always) | many:1 (always) | Many areas belong to one plant, every area matches a plant, and every plant includes at least one area. |
| `dim_area` to `dim_production_line` | `area_identity` | 1:many (always) | many:1 (always) | Many production lines belong to one area, every production line matches an area, and every area includes at least one production line. |
| `dim_production_line` to `dim_work_center` | `production_line_identity` | 1:many (always) | many:1 (always) | Many work centers belong to one production line, every work center matches a production line, and every production line includes at least one work center. |
| `dim_work_center` to `dim_work_unit` | `work_center_identity` | 1:many (always) | many:1 (always) | Many work units belong to one work center, every work unit matches a work center, and every work center includes at least one work unit. |
| `dim_employee` to `dim_plant` | `employee_identity` | 1:1 (optional) | 1:1 (always) | Each plant matches exactly one plant manager, each employee manages at most one plant, and not every employee is a plant manager. |
| `dim_bom_header` to `bridge_bom_component` | `bom_header_identity` | 1:many (always) | many:1 (always) | Many components belong to one bill of materials, every component matches a bill of materials, and every bill of materials includes at least one component. |
| `dim_routing_header` to `bridge_routing_operation` | `routing_identity` | 1:many (always) | many:1 (always) | Many routing operations belong to one routing, every routing operation matches a routing, and every routing includes at least one routing operation. |
| `fact_production_order` to `fact_production_order_operation` | `production_order_identity` | 1:many (always) | many:1 (always) | Many production order operations belong to one production order, every operation matches a production order, and every production order includes at least one operation. |
| `fact_sales_order` to `fact_sales_order_line` | `sales_order_identity` | 1:many (always) | many:1 (always) | Many sales order lines belong to one sales order, every line matches a sales order, and every sales order includes at least one line. |
| `fact_purchase_order` to `fact_purchase_order_line` | `purchase_order_identity` | 1:many (always) | many:1 (always) | Many purchase order lines belong to one purchase order, every line matches a purchase order, and every purchase order includes at least one line. |
| `dim_supplier` to `dim_supplier_site` | `supplier_identity` | 1:many (always) | many:1 (always) | Many supplier sites belong to one supplier, every supplier site matches a supplier, and every supplier includes at least one supplier site. |
| `dim_warehouse` to `dim_storage_location` | `warehouse_identity` | 1:many (always) | many:1 (always) | Many storage locations belong to one warehouse, every storage location matches a warehouse, and every warehouse includes at least one storage location. |

## Relationship rules

| Child dataset | Column | Universe dataset | Mapping | Parent match | Child match | Rule |
| --- | --- | --- | --- | --- | --- | --- |
| `dim_legal_entity` | `enterprise_id` | `dim_enterprise` | 1:N | 1:many / always | many:1 / always | Many legal entities belong to one enterprise, every legal entity matches an enterprise, and every enterprise includes at least one legal entity. |
| `dim_plant` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many plants belong to one legal entity, every plant matches a legal entity, and a legal entity may include no plant. |
| `dim_plant` | `plant_manager_employee_id` | `dim_employee` | 1:1 | 1:1 / optional | 1:1 / always | Each plant matches exactly one plant manager, each employee manages at most one plant, and not every employee is a plant manager. |
| `dim_area` | `plant_id` | `dim_plant` | 1:N | 1:many / always | many:1 / always | Many areas belong to one plant, every area matches a plant, and every plant includes at least one area. |
| `dim_production_line` | `area_id` | `dim_area` | 1:N | 1:many / always | many:1 / always | Many production lines belong to one area, every production line matches an area, and every area includes at least one production line. |
| `dim_production_line` | `supervisor_employee_id` | `dim_employee` | 1:1 | 1:1 / optional | 1:1 / always | Each production line matches exactly one supervisor, each employee supervises at most one production line, and not every employee is a line supervisor. |
| `dim_work_center` | `production_line_id` | `dim_production_line` | 1:N | 1:many / always | many:1 / always | Many work centers belong to one production line, every work center matches a production line, and every production line includes at least one work center. |
| `dim_work_center` | `department_id` | `dim_department` | 1:N | 1:many / optional | many:1 / always | Many work centers belong to one department, every work center matches a department, and a department may include no work center. |
| `dim_work_center` | `cost_center_id` | `dim_cost_center` | 1:N | 1:many / optional | many:1 / always | Many work centers belong to one cost center, every work center matches a cost center, and a cost center may include no work center. |
| `dim_work_unit` | `work_center_id` | `dim_work_center` | 1:N | 1:many / always | many:1 / always | Many work units belong to one work center, every work unit matches a work center, and every work center includes at least one work unit. |
| `dim_department` | `plant_id` | `dim_plant` | 1:N | 1:many / always | many:1 / always | Many departments belong to one plant, every department matches a plant, and every plant includes at least one department. |
| `dim_cost_center` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many cost centers belong to one legal entity, every cost center matches a legal entity, and a legal entity may include no cost center. |
| `dim_cost_center` | `profit_center_id` | `dim_profit_center` | 1:N | 1:many / optional | many:1 / always | Many cost centers belong to one profit center, every cost center matches a profit center, and a profit center may include no cost center. |
| `dim_profit_center` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many profit centers belong to one legal entity, every profit center matches a legal entity, and a legal entity may include no profit center. |
| `dim_employee` | `department_id` | `dim_department` | 1:N | 1:many / optional | many:1 / always | Many employees belong to one department, every employee matches a department, and a department may include no employee. |
| `dim_employee` | `home_plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many employees belong to one home plant, every employee matches a home plant, and a plant may include no employee. |
| `dim_shift` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many shifts belong to one plant, every shift matches a plant, and a plant may include no shift. |
| `dim_planner` | `employee_id` | `dim_employee` | 1:1 | 1:1 / optional | 1:1 / always | Each planner matches exactly one employee, each employee holds at most one planner assignment, and not every employee is a planner. |
| `dim_planner` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many planners belong to one plant, every planner matches a plant, and a plant may include no planner. |
| `dim_item` | `product_family_id` | `dim_product_family` | 1:N | 1:many / optional | many:1 / always | Many items belong to one product family, every item matches a product family, and a product family may include no item. |
| `dim_item` | `commodity_id` | `dim_commodity` | 1:N | 1:many / optional | many:1 / always | Many items belong to one commodity, every item matches a commodity, and a commodity may include no item. |
| `dim_item` | `base_uom_id` | `dim_unit_of_measure` | 1:N | 1:many / optional | many:1 / always | Many items share one base unit of measure, every item matches a unit of measure, and a unit of measure may include no item. |
| `dim_item_revision` | `item_id` | `dim_item` | 1:N | 1:many / always | many:1 / always | Many revisions belong to one item, every revision matches an item, and every item includes at least one revision. |
| `dim_bom_header` | `parent_item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many bills of materials belong to one parent item revision, every bill of materials matches a parent revision, and an item revision may include no bill of materials. |
| `dim_bom_header` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many bills of materials belong to one plant, every bill of materials matches a plant, and a plant may include no bill of materials. |
| `dim_routing_header` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many routings belong to one item revision, every routing matches an item revision, and an item revision may include no routing. |
| `dim_routing_header` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many routings belong to one plant, every routing matches a plant, and a plant may include no routing. |
| `dim_tool` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many tools belong to one plant, every tool matches a plant, and a plant may include no tool. |
| `dim_engineering_document` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / optional | An engineering document may match one item revision, and an item revision may include no engineering document. |
| `dim_supplier` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many suppliers share one default currency, every supplier matches a currency, and a currency may include no supplier. |
| `dim_supplier_site` | `supplier_id` | `dim_supplier` | 1:N | 1:many / always | many:1 / always | Many supplier sites belong to one supplier, every supplier site matches a supplier, and every supplier includes at least one supplier site. |
| `dim_customer` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many customers share one default currency, every customer matches a currency, and a currency may include no customer. |
| `dim_customer` | `sales_channel_id` | `dim_sales_channel` | 1:N | 1:many / optional | many:1 / optional | A customer may match one sales channel, and a sales channel may include no customer. |
| `dim_customer_ship_to` | `customer_id` | `dim_customer` | 1:N | 1:many / always | many:1 / always | Many ship-to addresses belong to one customer, every ship-to matches a customer, and every customer includes at least one ship-to. |
| `dim_warehouse` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many warehouses belong to one plant, every warehouse matches a plant, and a plant may include no warehouse. |
| `dim_storage_location` | `warehouse_id` | `dim_warehouse` | 1:N | 1:many / always | many:1 / always | Many storage locations belong to one warehouse, every storage location matches a warehouse, and every warehouse includes at least one storage location. |
| `dim_lot` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many lots belong to one item, every lot matches an item, and an item may include no lot. |
| `dim_lot` | `supplier_id` | `dim_supplier` | 1:N | 1:many / optional | many:1 / optional | A lot may match one supplier, and a supplier may include no lot. |
| `dim_serial` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many serials belong to one item, every serial matches an item, and an item may include no serial. |
| `dim_serial` | `lot_id` | `dim_lot` | 1:N | 1:many / optional | many:1 / optional | A serial may match one lot, and a lot may include no serial. |
| `dim_inspection_plan` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many inspection plans belong to one item revision, every inspection plan matches an item revision, and an item revision may include no inspection plan. |
| `dim_asset` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many assets belong to one plant, every asset matches a plant, and a plant may include no asset. |
| `dim_asset` | `work_center_id` | `dim_work_center` | 1:N | 1:many / optional | many:1 / optional | An asset may match one work center, and a work center may include no asset. |
| `dim_asset` | `cost_center_id` | `dim_cost_center` | 1:N | 1:many / optional | many:1 / always | Many assets belong to one cost center, every asset matches a cost center, and a cost center may include no asset. |
| `dim_maintenance_crew` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many maintenance crews belong to one plant, every maintenance crew matches a plant, and a plant may include no maintenance crew. |
| `dim_gl_account` | `legal_entity_id` | `dim_legal_entity` | 1:N | 1:many / optional | many:1 / always | Many general-ledger accounts belong to one legal entity, every account matches a legal entity, and a legal entity may include no account. |
| `dim_sales_representative` | `employee_id` | `dim_employee` | 1:1 | 1:1 / optional | 1:1 / always | Each sales representative matches exactly one employee, each employee holds at most one sales representative role, and not every employee is a sales representative. |
| `bridge_employee_skill` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many skill assignments belong to one employee, every assignment matches an employee, and an employee may include no skill assignment. |
| `bridge_employee_skill` | `skill_id` | `dim_labor_skill` | 1:N | 1:many / optional | many:1 / always | Many skill assignments belong to one labor skill, every assignment matches a labor skill, and a labor skill may include no assignment. |
| `dim_reporting_manager` | `employee_id` | `dim_employee` | 1:1 | 1:1 / optional | 1:1 / always | Each reporting-manager role matches exactly one employee, an employee holds at most one reporting-manager role, and not every employee is a reporting manager. |
| `bridge_employee_reporting` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many reporting rows name one employee as the report, every reporting row matches that employee, and an employee may include no reporting row. |
| `bridge_employee_reporting` | `reporting_manager_id` | `dim_reporting_manager` | 1:N | 1:many / optional | many:1 / always | Many reporting rows name one reporting manager, every reporting row matches that role, and a reporting manager may include no reporting row. |
| `bridge_item_plant` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many item-plant rows belong to one item, every row matches an item, and an item may include no plant assignment. |
| `bridge_item_plant` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many item-plant rows belong to one plant, every row matches a plant, and a plant may include no item assignment. |
| `bridge_work_center_skill` | `work_center_id` | `dim_work_center` | 1:N | 1:many / optional | many:1 / always | Many skill requirements belong to one work center, every requirement matches a work center, and a work center may include no skill requirement. |
| `bridge_work_center_skill` | `skill_id` | `dim_labor_skill` | 1:N | 1:many / optional | many:1 / always | Many skill requirements belong to one labor skill, every requirement matches a labor skill, and a labor skill may include no work-center requirement. |
| `bridge_bom_component` | `bom_header_id` | `dim_bom_header` | 1:N | 1:many / always | many:1 / always | Many components belong to one bill of materials, every component matches a bill of materials, and every bill of materials includes at least one component. |
| `bridge_bom_component` | `component_item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many component rows belong to one item, every component row matches an item, and an item may include no component row. |
| `bridge_bom_component` | `operation_id` | `dim_operation` | 1:N | 1:many / optional | many:1 / optional | A component row may match one operation, and an operation may include no component row. |
| `bridge_routing_operation` | `routing_id` | `dim_routing_header` | 1:N | 1:many / always | many:1 / always | Many routing operations belong to one routing, every routing operation matches a routing, and every routing includes at least one routing operation. |
| `bridge_routing_operation` | `operation_id` | `dim_operation` | 1:N | 1:many / optional | many:1 / always | Many routing operations belong to one operation, every routing operation matches an operation, and an operation may include no routing operation. |
| `bridge_routing_operation` | `work_center_id` | `dim_work_center` | 1:N | 1:many / optional | many:1 / always | Many routing operations belong to one work center, every routing operation matches a work center, and a work center may include no routing operation. |
| `bridge_item_customer` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many item-customer rows belong to one item, every row matches an item, and an item may include no customer link. |
| `bridge_item_customer` | `customer_id` | `dim_customer` | 1:N | 1:many / optional | many:1 / always | Many item-customer rows belong to one customer, every row matches a customer, and a customer may include no item link. |
| `bridge_supplier_item` | `supplier_id` | `dim_supplier` | 1:N | 1:many / optional | many:1 / always | Many supplier-item rows belong to one supplier, every row matches a supplier, and a supplier may include no item source. |
| `bridge_supplier_item` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many supplier-item rows belong to one item, every row matches an item, and an item may include no supplier source. |
| `bridge_supplier_item` | `supplier_site_id` | `dim_supplier_site` | 1:N | 1:many / optional | many:1 / optional | A supplier-item row may match one supplier site, and a supplier site may include no supplier-item row. |
| `bridge_asset_spare` | `asset_id` | `dim_asset` | 1:N | 1:many / optional | many:1 / always | Many spare links belong to one asset, every spare link matches an asset, and an asset may include no spare link. |
| `bridge_asset_spare` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many spare links belong to one item, every spare link matches an item, and an item may include no spare link. |
| `bridge_employee_work_center` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many qualifications belong to one employee, every qualification matches an employee, and an employee may include no qualification. |
| `bridge_employee_work_center` | `work_center_id` | `dim_work_center` | 1:N | 1:many / optional | many:1 / always | Many qualifications belong to one work center, every qualification matches a work center, and a work center may include no qualification. |
| `bridge_characteristic_item` | `characteristic_id` | `dim_quality_characteristic` | 1:N | 1:many / optional | many:1 / always | Many applicability rows belong to one characteristic, every row matches a characteristic, and a characteristic may include no applicability row. |
| `bridge_characteristic_item` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many applicability rows belong to one item revision, every row matches an item revision, and an item revision may include no applicability row. |
| `bridge_engineering_change_revision` | `engineering_change_id` | `dim_engineering_change` | 1:N | 1:many / optional | many:1 / always | Many revision links belong to one engineering change, every link matches an engineering change, and an engineering change may include no revision link. |
| `bridge_engineering_change_revision` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many revision links belong to one item revision, every link matches an item revision, and an item revision may include no engineering change. |
| `fact_sales_quote` | `customer_id` | `dim_customer` | 1:N | 1:many / optional | many:1 / always | Many quotes belong to one customer, every quote matches a customer, and a customer may include no quote. |
| `fact_sales_quote` | `sales_rep_id` | `dim_sales_representative` | 1:N | 1:many / optional | many:1 / optional | A quote may match one sales representative, and a sales representative may include no quote. |
| `fact_sales_quote` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many quotes belong to one calendar day, every quote matches a calendar day, and a calendar day may include no quote. |
| `fact_sales_quote_line` | `quote_id` | `fact_sales_quote` | 1:N | 1:many / always | many:1 / always | Many quote lines belong to one quote, every quote line matches a quote, and every quote includes at least one quote line. |
| `fact_sales_quote_line` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many quote lines belong to one item revision, every quote line matches an item revision, and an item revision may include no quote line. |
| `fact_sales_order` | `customer_id` | `dim_customer` | 1:N | 1:many / optional | many:1 / always | Many sales orders belong to one customer, every sales order matches a customer, and a customer may include no sales order. |
| `fact_sales_order` | `ship_to_id` | `dim_customer_ship_to` | 1:N | 1:many / optional | many:1 / always | Many sales orders belong to one ship-to, every sales order matches a ship-to, and a ship-to may include no sales order. |
| `fact_sales_order` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many sales orders belong to one plant, every sales order matches a plant, and a plant may include no sales order. |
| `fact_sales_order` | `sales_channel_id` | `dim_sales_channel` | 1:N | 1:many / optional | many:1 / always | Many sales orders belong to one sales channel, every sales order matches a sales channel, and a sales channel may include no sales order. |
| `fact_sales_order` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many sales orders share one currency, every sales order matches a currency, and a currency may include no sales order. |
| `fact_sales_order` | `payment_term_id` | `dim_payment_term` | 1:N | 1:many / optional | many:1 / always | Many sales orders share one payment term, every sales order matches a payment term, and a payment term may include no sales order. |
| `fact_sales_order` | `sales_rep_id` | `dim_sales_representative` | 1:N | 1:many / optional | many:1 / optional | A sales order may match one sales representative, and a sales representative may include no sales order. |
| `fact_sales_order` | `incoterm_id` | `dim_incoterm` | 1:N | 1:many / optional | many:1 / optional | A sales order may match one incoterm, and an incoterm may include no sales order. |
| `fact_sales_order` | `order_date_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many sales orders belong to one order date, every sales order matches a calendar day, and a calendar day may include no sales order. |
| `fact_sales_order_line` | `sales_order_id` | `fact_sales_order` | 1:N | 1:many / always | many:1 / always | Many sales order lines belong to one sales order, every line matches a sales order, and every sales order includes at least one line. |
| `fact_sales_order_line` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many sales order lines belong to one item revision, every line matches an item revision, and an item revision may include no sales order line. |
| `fact_sales_order_line` | `uom_id` | `dim_unit_of_measure` | 1:N | 1:many / optional | many:1 / always | Many sales order lines share one unit of measure, every line matches a unit of measure, and a unit of measure may include no sales order line. |
| `fact_sales_order_schedule` | `sales_order_line_id` | `fact_sales_order_line` | 1:N | 1:many / always | many:1 / always | Many schedules belong to one sales order line, every schedule matches a sales order line, and every sales order line includes at least one schedule. |
| `fact_sales_order_schedule` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many schedules belong to one plant, every schedule matches a plant, and a plant may include no schedule. |
| `fact_sales_order_schedule` | `ship_to_id` | `dim_customer_ship_to` | 1:N | 1:many / optional | many:1 / always | Many schedules belong to one ship-to, every schedule matches a ship-to, and a ship-to may include no schedule. |
| `fact_sales_order_schedule` | `promise_date_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many schedules belong to one promise date, every schedule matches a calendar day, and a calendar day may include no schedule. |
| `fact_shipment` | `carrier_id` | `dim_carrier` | 1:N | 1:many / optional | many:1 / always | Many shipments belong to one carrier, every shipment matches a carrier, and a carrier may include no shipment. |
| `fact_shipment` | `ship_to_id` | `dim_customer_ship_to` | 1:N | 1:many / optional | many:1 / always | Many shipments belong to one ship-to, every shipment matches a ship-to, and a ship-to may include no shipment. |
| `fact_shipment` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many shipments belong to one plant, every shipment matches a plant, and a plant may include no shipment. |
| `fact_shipment` | `ship_date_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many shipments belong to one ship date, every shipment matches a calendar day, and a calendar day may include no shipment. |
| `fact_shipment_line` | `shipment_id` | `fact_shipment` | 1:N | 1:many / always | many:1 / always | Many shipment lines belong to one shipment, every shipment line matches a shipment, and every shipment includes at least one shipment line. |
| `fact_shipment_line` | `sales_order_line_id` | `fact_sales_order_line` | 1:N | 1:many / optional | many:1 / optional | A shipment line may match one sales order line, and a sales order line may include no shipment line. |
| `fact_shipment_line` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many shipment lines belong to one item revision, every shipment line matches an item revision, and an item revision may include no shipment line. |
| `fact_shipment_line` | `lot_id` | `dim_lot` | 1:N | 1:many / optional | many:1 / optional | A shipment line may match one lot, and a lot may include no shipment line. |
| `fact_customer_invoice` | `customer_id` | `dim_customer` | 1:N | 1:many / optional | many:1 / always | Many customer invoices belong to one customer, every customer invoice matches a customer, and a customer may include no customer invoice. |
| `fact_customer_invoice` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many customer invoices share one currency, every customer invoice matches a currency, and a currency may include no customer invoice. |
| `fact_customer_invoice` | `invoice_date_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many customer invoices belong to one invoice date, every customer invoice matches a calendar day, and a calendar day may include no customer invoice. |
| `fact_customer_invoice_line` | `invoice_id` | `fact_customer_invoice` | 1:N | 1:many / always | many:1 / always | Many customer invoice lines belong to one customer invoice, every line matches a customer invoice, and every customer invoice includes at least one line. |
| `fact_customer_invoice_line` | `shipment_line_id` | `fact_shipment_line` | 1:N | 1:many / optional | many:1 / optional | A customer invoice line may match one shipment line, and a shipment line may include no customer invoice line. |
| `fact_customer_invoice_line` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / always | Many customer invoice lines belong to one general-ledger account, every line matches an account, and an account may include no customer invoice line. |
| `fact_customer_payment` | `customer_id` | `dim_customer` | 1:N | 1:many / optional | many:1 / always | Many customer payments belong to one customer, every payment matches a customer, and a customer may include no payment. |
| `fact_customer_payment` | `invoice_id` | `fact_customer_invoice` | 1:N | 1:many / optional | many:1 / optional | A customer payment may match one customer invoice, and a customer invoice may include no payment. |
| `fact_customer_payment` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many customer payments share one currency, every payment matches a currency, and a currency may include no customer payment. |
| `fact_customer_payment` | `payment_date_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many customer payments belong to one payment date, every payment matches a calendar day, and a calendar day may include no customer payment. |
| `fact_customer_return` | `customer_id` | `dim_customer` | 1:N | 1:many / optional | many:1 / always | Many customer returns belong to one customer, every return matches a customer, and a customer may include no return. |
| `fact_customer_return` | `sales_order_line_id` | `fact_sales_order_line` | 1:N | 1:many / optional | many:1 / optional | A customer return may match one sales order line, and a sales order line may include no customer return. |
| `fact_customer_return` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / always | Many customer returns belong to one reason code, every return matches a reason code, and a reason code may include no customer return. |
| `fact_customer_return` | `receipt_date_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many customer returns belong to one receipt date, every return matches a calendar day, and a calendar day may include no customer return. |
| `fact_demand_forecast` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many forecasts belong to one item, every forecast matches an item, and an item may include no forecast. |
| `fact_demand_forecast` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many forecasts belong to one plant, every forecast matches a plant, and a plant may include no forecast. |
| `fact_demand_forecast` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many forecasts belong to one calendar day, every forecast matches a calendar day, and a calendar day may include no forecast. |
| `fact_master_production_schedule` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many schedule rows belong to one item, every schedule row matches an item, and an item may include no master schedule row. |
| `fact_master_production_schedule` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many schedule rows belong to one plant, every schedule row matches a plant, and a plant may include no master schedule row. |
| `fact_master_production_schedule` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many schedule rows belong to one calendar day, every schedule row matches a calendar day, and a calendar day may include no master schedule row. |
| `fact_planned_order` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many planned orders belong to one item revision, every planned order matches an item revision, and an item revision may include no planned order. |
| `fact_planned_order` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many planned orders belong to one plant, every planned order matches a plant, and a plant may include no planned order. |
| `fact_planned_order` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many planned orders belong to one calendar day, every planned order matches a calendar day, and a calendar day may include no planned order. |
| `fact_production_order` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many production orders belong to one item revision, every production order matches an item revision, and an item revision may include no production order. |
| `fact_production_order` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many production orders belong to one plant, every production order matches a plant, and a plant may include no production order. |
| `fact_production_order` | `routing_id` | `dim_routing_header` | 1:N | 1:many / optional | many:1 / optional | A production order may match one routing, and a routing may include no production order. |
| `fact_production_order` | `bom_header_id` | `dim_bom_header` | 1:N | 1:many / optional | many:1 / optional | A production order may match one bill of materials, and a bill of materials may include no production order. |
| `fact_production_order` | `planner_id` | `dim_planner` | 1:N | 1:many / optional | many:1 / optional | A production order may match one planner, and a planner may include no production order. |
| `fact_production_order_operation` | `production_order_id` | `fact_production_order` | 1:N | 1:many / always | many:1 / always | Many production order operations belong to one production order, every operation matches a production order, and every production order includes at least one operation. |
| `fact_production_order_operation` | `operation_id` | `dim_operation` | 1:N | 1:many / optional | many:1 / always | Many production order operations belong to one operation, every production order operation matches an operation, and an operation may include no production order operation. |
| `fact_production_order_operation` | `work_center_id` | `dim_work_center` | 1:N | 1:many / optional | many:1 / always | Many production order operations belong to one work center, every production order operation matches a work center, and a work center may include no production order operation. |
| `fact_production_order_operation` | `routing_operation_id` | `bridge_routing_operation` | 1:N | 1:many / optional | many:1 / optional | A production order operation may match one routing operation, and a routing operation may include no production order operation. |
| `fact_operation_confirmation` | `production_order_operation_id` | `fact_production_order_operation` | 1:N | 1:many / optional | many:1 / always | Many confirmations belong to one production order operation, every confirmation matches a production order operation, and a production order operation may include no confirmation. |
| `fact_operation_confirmation` | `work_unit_id` | `dim_work_unit` | 1:N | 1:many / optional | many:1 / optional | A confirmation may match one work unit, and a work unit may include no confirmation. |
| `fact_operation_confirmation` | `shift_id` | `dim_shift` | 1:N | 1:many / optional | many:1 / optional | A confirmation may match one shift, and a shift may include no confirmation. |
| `fact_operation_confirmation` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / optional | A confirmation may match one employee, and an employee may include no confirmation. |
| `fact_operation_confirmation` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many confirmations belong to one calendar day, every confirmation matches a calendar day, and a calendar day may include no confirmation. |
| `fact_labor_ticket` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many labor tickets belong to one employee, every labor ticket matches an employee, and an employee may include no labor ticket. |
| `fact_labor_ticket` | `production_order_operation_id` | `fact_production_order_operation` | 1:N | 1:many / optional | many:1 / optional | A labor ticket may match one production order operation, and a production order operation may include no labor ticket. |
| `fact_labor_ticket` | `work_center_id` | `dim_work_center` | 1:N | 1:many / optional | many:1 / always | Many labor tickets belong to one work center, every labor ticket matches a work center, and a work center may include no labor ticket. |
| `fact_labor_ticket` | `shift_id` | `dim_shift` | 1:N | 1:many / optional | many:1 / always | Many labor tickets belong to one shift, every labor ticket matches a shift, and a shift may include no labor ticket. |
| `fact_labor_ticket` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many labor tickets belong to one calendar day, every labor ticket matches a calendar day, and a calendar day may include no labor ticket. |
| `fact_material_issue` | `production_order_id` | `fact_production_order` | 1:N | 1:many / optional | many:1 / always | Many material issues belong to one production order, every material issue matches a production order, and a production order may include no material issue. |
| `fact_material_issue` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many material issues belong to one item, every material issue matches an item, and an item may include no material issue. |
| `fact_material_issue` | `storage_location_id` | `dim_storage_location` | 1:N | 1:many / optional | many:1 / always | Many material issues belong to one storage location, every material issue matches a storage location, and a storage location may include no material issue. |
| `fact_material_issue` | `lot_id` | `dim_lot` | 1:N | 1:many / optional | many:1 / optional | A material issue may match one lot, and a lot may include no material issue. |
| `fact_production_receipt` | `production_order_id` | `fact_production_order` | 1:N | 1:many / optional | many:1 / always | Many production receipts belong to one production order, every production receipt matches a production order, and a production order may include no production receipt. |
| `fact_production_receipt` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many production receipts belong to one item revision, every production receipt matches an item revision, and an item revision may include no production receipt. |
| `fact_production_receipt` | `storage_location_id` | `dim_storage_location` | 1:N | 1:many / optional | many:1 / always | Many production receipts belong to one storage location, every production receipt matches a storage location, and a storage location may include no production receipt. |
| `fact_production_receipt` | `lot_id` | `dim_lot` | 1:N | 1:many / optional | many:1 / optional | A production receipt may match one lot, and a lot may include no production receipt. |
| `fact_capacity_load` | `work_center_id` | `dim_work_center` | 1:N | 1:many / optional | many:1 / always | Many capacity loads belong to one work center, every capacity load matches a work center, and a work center may include no capacity load. |
| `fact_capacity_load` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many capacity loads belong to one calendar day, every capacity load matches a calendar day, and a calendar day may include no capacity load. |
| `fact_capacity_load` | `shift_id` | `dim_shift` | 1:N | 1:many / optional | many:1 / optional | A capacity load may match one shift, and a shift may include no capacity load. |
| `fact_kanban_signal` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many kanban signals belong to one item, every kanban signal matches an item, and an item may include no kanban signal. |
| `fact_kanban_signal` | `storage_location_id` | `dim_storage_location` | 1:N | 1:many / optional | many:1 / always | Many kanban signals belong to one storage location, every kanban signal matches a storage location, and a storage location may include no kanban signal. |
| `fact_kanban_signal` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many kanban signals belong to one plant, every kanban signal matches a plant, and a plant may include no kanban signal. |
| `fact_inventory_balance` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many balances belong to one item, every balance matches an item, and an item may include no balance. |
| `fact_inventory_balance` | `storage_location_id` | `dim_storage_location` | 1:N | 1:many / optional | many:1 / always | Many balances belong to one storage location, every balance matches a storage location, and a storage location may include no balance. |
| `fact_inventory_balance` | `inventory_status_id` | `dim_inventory_status` | 1:N | 1:many / optional | many:1 / always | Many balances belong to one inventory status, every balance matches an inventory status, and an inventory status may include no balance. |
| `fact_inventory_balance` | `lot_id` | `dim_lot` | 1:N | 1:many / optional | many:1 / optional | A balance may match one lot, and a lot may include no balance. |
| `fact_inventory_transaction` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many inventory transactions belong to one item, every transaction matches an item, and an item may include no inventory transaction. |
| `fact_inventory_transaction` | `from_storage_location_id` | `dim_storage_location` | 1:N | 1:many / optional | many:1 / optional | An inventory transaction may match one source storage location, and a storage location may include no transaction as a source. |
| `fact_inventory_transaction` | `inventory_status_id` | `dim_inventory_status` | 1:N | 1:many / optional | many:1 / optional | An inventory transaction may match one inventory status, and an inventory status may include no inventory transaction. |
| `fact_inventory_transaction` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / optional | An inventory transaction may match one reason code, and a reason code may include no inventory transaction. |
| `fact_inventory_transaction` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many inventory transactions belong to one calendar day, every transaction matches a calendar day, and a calendar day may include no inventory transaction. |
| `fact_inventory_destination` | `inventory_txn_id` | `fact_inventory_transaction` | 1:N | 1:many / optional | many:1 / always | Many destinations may belong to one inventory transaction, every destination matches a transaction, and a transaction may include no destination. |
| `fact_inventory_destination` | `storage_location_id` | `dim_storage_location` | 1:N | 1:many / optional | many:1 / always | Many destinations belong to one storage location, every destination matches a storage location, and a storage location may include no destination. |
| `fact_lot_genealogy` | `parent_lot_id` | `dim_lot` | 1:N | 1:many / optional | many:1 / always | Many genealogy links name one lot as the parent, every genealogy link matches that parent lot, and a lot may include no genealogy link as a parent. |
| `fact_lot_genealogy` | `production_order_id` | `fact_production_order` | 1:N | 1:many / optional | many:1 / optional | A genealogy link may match one production order, and a production order may include no genealogy link. |
| `fact_lot_descendant` | `genealogy_id` | `fact_lot_genealogy` | 1:1 | 1:1 / always | 1:1 / always | Each genealogy link matches exactly one child lot, and each child-lot row matches exactly one genealogy link. |
| `fact_lot_descendant` | `child_lot_id` | `dim_lot` | 1:N | 1:many / optional | many:1 / always | Many child-lot rows name one lot, every child-lot row matches that lot, and a lot may include no child-lot row. |
| `fact_cycle_count` | `storage_location_id` | `dim_storage_location` | 1:N | 1:many / optional | many:1 / always | Many cycle counts belong to one storage location, every cycle count matches a storage location, and a storage location may include no cycle count. |
| `fact_cycle_count` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many cycle counts belong to one item, every cycle count matches an item, and an item may include no cycle count. |
| `fact_cycle_count` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many cycle counts belong to one employee, every cycle count matches an employee, and an employee may include no cycle count. |
| `fact_cycle_count` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many cycle counts belong to one calendar day, every cycle count matches a calendar day, and a calendar day may include no cycle count. |
| `fact_serial_history` | `serial_id` | `dim_serial` | 1:N | 1:many / optional | many:1 / always | Many serial events belong to one serial, every serial event matches a serial, and a serial may include no serial event. |
| `fact_serial_history` | `production_order_id` | `fact_production_order` | 1:N | 1:many / optional | many:1 / optional | A serial event may match one production order, and a production order may include no serial event. |
| `fact_serial_history` | `shipment_line_id` | `fact_shipment_line` | 1:N | 1:many / optional | many:1 / optional | A serial event may match one shipment line, and a shipment line may include no serial event. |
| `fact_purchase_requisition` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many requisitions belong to one item revision, every requisition matches an item revision, and an item revision may include no requisition. |
| `fact_purchase_requisition` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many requisitions belong to one plant, every requisition matches a plant, and a plant may include no requisition. |
| `fact_purchase_requisition` | `requester_employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many requisitions belong to one requesting employee, every requisition matches an employee, and an employee may include no requisition. |
| `fact_purchase_requisition` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many requisitions belong to one calendar day, every requisition matches a calendar day, and a calendar day may include no requisition. |
| `fact_purchase_order` | `supplier_id` | `dim_supplier` | 1:N | 1:many / optional | many:1 / always | Many purchase orders belong to one supplier, every purchase order matches a supplier, and a supplier may include no purchase order. |
| `fact_purchase_order` | `supplier_site_id` | `dim_supplier_site` | 1:N | 1:many / optional | many:1 / always | Many purchase orders belong to one supplier site, every purchase order matches a supplier site, and a supplier site may include no purchase order. |
| `fact_purchase_order` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many purchase orders belong to one plant, every purchase order matches a plant, and a plant may include no purchase order. |
| `fact_purchase_order` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many purchase orders share one currency, every purchase order matches a currency, and a currency may include no purchase order. |
| `fact_purchase_order` | `payment_term_id` | `dim_payment_term` | 1:N | 1:many / optional | many:1 / always | Many purchase orders share one payment term, every purchase order matches a payment term, and a payment term may include no purchase order. |
| `fact_purchase_order` | `buyer_employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many purchase orders belong to one buyer, every purchase order matches an employee, and an employee may include no purchase order as buyer. |
| `fact_purchase_order_line` | `purchase_order_id` | `fact_purchase_order` | 1:N | 1:many / always | many:1 / always | Many purchase order lines belong to one purchase order, every line matches a purchase order, and every purchase order includes at least one line. |
| `fact_purchase_order_line` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many purchase order lines belong to one item revision, every line matches an item revision, and an item revision may include no purchase order line. |
| `fact_purchase_order_line` | `uom_id` | `dim_unit_of_measure` | 1:N | 1:many / optional | many:1 / always | Many purchase order lines share one unit of measure, every line matches a unit of measure, and a unit of measure may include no purchase order line. |
| `fact_po_schedule` | `purchase_order_line_id` | `fact_purchase_order_line` | 1:N | 1:many / always | many:1 / always | Many purchase order schedules belong to one purchase order line, every schedule matches a purchase order line, and every purchase order line includes at least one schedule. |
| `fact_po_schedule` | `storage_location_id` | `dim_storage_location` | 1:N | 1:many / optional | many:1 / optional | A purchase order schedule may match one storage location, and a storage location may include no purchase order schedule. |
| `fact_po_schedule` | `due_date_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many purchase order schedules belong to one due date, every schedule matches a calendar day, and a calendar day may include no purchase order schedule. |
| `fact_goods_receipt` | `purchase_order_line_id` | `fact_purchase_order_line` | 1:N | 1:many / optional | many:1 / always | Many goods receipts belong to one purchase order line, every goods receipt matches a purchase order line, and a purchase order line may include no goods receipt. |
| `fact_goods_receipt` | `storage_location_id` | `dim_storage_location` | 1:N | 1:many / optional | many:1 / always | Many goods receipts belong to one storage location, every goods receipt matches a storage location, and a storage location may include no goods receipt. |
| `fact_goods_receipt` | `lot_id` | `dim_lot` | 1:N | 1:many / optional | many:1 / optional | A goods receipt may match one lot, and a lot may include no goods receipt. |
| `fact_goods_receipt` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many goods receipts belong to one calendar day, every goods receipt matches a calendar day, and a calendar day may include no goods receipt. |
| `fact_supplier_invoice` | `supplier_id` | `dim_supplier` | 1:N | 1:many / optional | many:1 / always | Many supplier invoices belong to one supplier, every supplier invoice matches a supplier, and a supplier may include no supplier invoice. |
| `fact_supplier_invoice` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many supplier invoices share one currency, every supplier invoice matches a currency, and a currency may include no supplier invoice. |
| `fact_supplier_invoice` | `invoice_date_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many supplier invoices belong to one invoice date, every supplier invoice matches a calendar day, and a calendar day may include no supplier invoice. |
| `fact_supplier_invoice_line` | `supplier_invoice_id` | `fact_supplier_invoice` | 1:N | 1:many / always | many:1 / always | Many supplier invoice lines belong to one supplier invoice, every line matches a supplier invoice, and every supplier invoice includes at least one line. |
| `fact_supplier_invoice_line` | `purchase_order_line_id` | `fact_purchase_order_line` | 1:N | 1:many / optional | many:1 / optional | A supplier invoice line may match one purchase order line, and a purchase order line may include no supplier invoice line. |
| `fact_supplier_invoice_line` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / always | Many supplier invoice lines belong to one general-ledger account, every line matches an account, and an account may include no supplier invoice line. |
| `fact_supplier_payment` | `supplier_id` | `dim_supplier` | 1:N | 1:many / optional | many:1 / always | Many supplier payments belong to one supplier, every payment matches a supplier, and a supplier may include no supplier payment. |
| `fact_supplier_payment` | `supplier_invoice_id` | `fact_supplier_invoice` | 1:N | 1:many / optional | many:1 / optional | A supplier payment may match one supplier invoice, and a supplier invoice may include no payment. |
| `fact_supplier_payment` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many supplier payments share one currency, every payment matches a currency, and a currency may include no supplier payment. |
| `fact_supplier_payment` | `payment_date_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many supplier payments belong to one payment date, every payment matches a calendar day, and a calendar day may include no supplier payment. |
| `fact_supplier_return` | `supplier_id` | `dim_supplier` | 1:N | 1:many / optional | many:1 / always | Many supplier returns belong to one supplier, every return matches a supplier, and a supplier may include no supplier return. |
| `fact_supplier_return` | `purchase_order_line_id` | `fact_purchase_order_line` | 1:N | 1:many / optional | many:1 / optional | A supplier return may match one purchase order line, and a purchase order line may include no supplier return. |
| `fact_supplier_return` | `reason_code_id` | `dim_reason_code` | 1:N | 1:many / optional | many:1 / always | Many supplier returns belong to one reason code, every return matches a reason code, and a reason code may include no supplier return. |
| `fact_inspection_result` | `inspection_plan_id` | `dim_inspection_plan` | 1:N | 1:many / optional | many:1 / always | Many inspection results belong to one inspection plan, every result matches an inspection plan, and an inspection plan may include no result. |
| `fact_inspection_result` | `production_order_operation_id` | `fact_production_order_operation` | 1:N | 1:many / optional | many:1 / optional | An inspection result may match one production order operation, and a production order operation may include no inspection result. |
| `fact_inspection_result` | `characteristic_id` | `dim_quality_characteristic` | 1:N | 1:many / optional | many:1 / always | Many inspection results belong to one characteristic, every result matches a characteristic, and a characteristic may include no inspection result. |
| `fact_inspection_result` | `lot_id` | `dim_lot` | 1:N | 1:many / optional | many:1 / optional | An inspection result may match one lot, and a lot may include no inspection result. |
| `fact_nonconformance` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many nonconformances belong to one item revision, every nonconformance matches an item revision, and an item revision may include no nonconformance. |
| `fact_nonconformance` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many nonconformances belong to one plant, every nonconformance matches a plant, and a plant may include no nonconformance. |
| `fact_nonconformance` | `defect_code_id` | `dim_defect_code` | 1:N | 1:many / optional | many:1 / always | Many nonconformances belong to one defect code, every nonconformance matches a defect code, and a defect code may include no nonconformance. |
| `fact_nonconformance` | `production_order_id` | `fact_production_order` | 1:N | 1:many / optional | many:1 / optional | A nonconformance may match one production order, and a production order may include no nonconformance. |
| `fact_nonconformance` | `lot_id` | `dim_lot` | 1:N | 1:many / optional | many:1 / optional | A nonconformance may match one lot, and a lot may include no nonconformance. |
| `fact_ncr_disposition` | `nonconformance_id` | `fact_nonconformance` | 1:N | 1:many / always | many:1 / always | Many dispositions belong to one nonconformance, every disposition matches a nonconformance, and every nonconformance includes at least one disposition. |
| `fact_ncr_disposition` | `disposition_code_id` | `dim_disposition_code` | 1:N | 1:many / optional | many:1 / always | Many dispositions belong to one disposition code, every disposition matches a disposition code, and a disposition code may include no disposition. |
| `fact_ncr_disposition` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many dispositions belong to one employee, every disposition matches an employee, and an employee may include no disposition. |
| `fact_scrap_event` | `production_order_operation_id` | `fact_production_order_operation` | 1:N | 1:many / optional | many:1 / optional | A scrap event may match one production order operation, and a production order operation may include no scrap event. |
| `fact_scrap_event` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many scrap events belong to one item, every scrap event matches an item, and an item may include no scrap event. |
| `fact_scrap_event` | `defect_code_id` | `dim_defect_code` | 1:N | 1:many / optional | many:1 / optional | A scrap event may match one defect code, and a defect code may include no scrap event. |
| `fact_scrap_event` | `storage_location_id` | `dim_storage_location` | 1:N | 1:many / optional | many:1 / optional | A scrap event may match one storage location, and a storage location may include no scrap event. |
| `fact_calibration_result` | `tool_id` | `dim_tool` | 1:N | 1:many / optional | many:1 / always | Many calibration results belong to one tool, every calibration result matches a tool, and a tool may include no calibration result. |
| `fact_calibration_result` | `characteristic_id` | `dim_quality_characteristic` | 1:N | 1:many / optional | many:1 / optional | A calibration result may match one characteristic, and a characteristic may include no calibration result. |
| `fact_calibration_result` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many calibration results belong to one calendar day, every calibration result matches a calendar day, and a calendar day may include no calibration result. |
| `fact_downtime_event` | `work_center_id` | `dim_work_center` | 1:N | 1:many / optional | many:1 / always | Many downtime events belong to one work center, every downtime event matches a work center, and a work center may include no downtime event. |
| `fact_downtime_event` | `asset_id` | `dim_asset` | 1:N | 1:many / optional | many:1 / optional | A downtime event may match one asset, and an asset may include no downtime event. |
| `fact_downtime_event` | `failure_code_id` | `dim_failure_code` | 1:N | 1:many / optional | many:1 / optional | A downtime event may match one failure code, and a failure code may include no downtime event. |
| `fact_downtime_event` | `shift_id` | `dim_shift` | 1:N | 1:many / optional | many:1 / optional | A downtime event may match one shift, and a shift may include no downtime event. |
| `fact_downtime_event` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many downtime events belong to one calendar day, every downtime event matches a calendar day, and a calendar day may include no downtime event. |
| `fact_maintenance_work_order` | `asset_id` | `dim_asset` | 1:N | 1:many / optional | many:1 / always | Many maintenance work orders belong to one asset, every work order matches an asset, and an asset may include no maintenance work order. |
| `fact_maintenance_work_order` | `maintenance_crew_id` | `dim_maintenance_crew` | 1:N | 1:many / optional | many:1 / optional | A maintenance work order may match one maintenance crew, and a maintenance crew may include no maintenance work order. |
| `fact_maintenance_work_order` | `failure_code_id` | `dim_failure_code` | 1:N | 1:many / optional | many:1 / optional | A maintenance work order may match one failure code, and a failure code may include no maintenance work order. |
| `fact_maintenance_work_order` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many maintenance work orders belong to one plant, every work order matches a plant, and a plant may include no maintenance work order. |
| `fact_maintenance_labor` | `maintenance_work_order_id` | `fact_maintenance_work_order` | 1:N | 1:many / always | many:1 / always | Many labor postings belong to one maintenance work order, every posting matches a maintenance work order, and every maintenance work order includes at least one labor posting. |
| `fact_maintenance_labor` | `employee_id` | `dim_employee` | 1:N | 1:many / optional | many:1 / always | Many maintenance labor postings belong to one employee, every posting matches an employee, and an employee may include no maintenance labor posting. |
| `fact_maintenance_labor` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many maintenance labor postings belong to one calendar day, every posting matches a calendar day, and a calendar day may include no maintenance labor posting. |
| `fact_spare_consumption` | `maintenance_work_order_id` | `fact_maintenance_work_order` | 1:N | 1:many / optional | many:1 / always | Many spare consumptions belong to one maintenance work order, every consumption matches a maintenance work order, and a maintenance work order may include no spare consumption. |
| `fact_spare_consumption` | `item_id` | `dim_item` | 1:N | 1:many / optional | many:1 / always | Many spare consumptions belong to one item, every consumption matches an item, and an item may include no spare consumption. |
| `fact_spare_consumption` | `storage_location_id` | `dim_storage_location` | 1:N | 1:many / optional | many:1 / optional | A spare consumption may match one storage location, and a storage location may include no spare consumption. |
| `fact_standard_cost` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many standard costs belong to one item revision, every standard cost matches an item revision, and an item revision may include no standard cost. |
| `fact_standard_cost` | `plant_id` | `dim_plant` | 1:N | 1:many / optional | many:1 / always | Many standard costs belong to one plant, every standard cost matches a plant, and a plant may include no standard cost. |
| `fact_standard_cost` | `cost_center_id` | `dim_cost_center` | 1:N | 1:many / optional | many:1 / optional | A standard cost may match one cost center, and a cost center may include no standard cost. |
| `fact_standard_cost` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / optional | A standard cost may match one general-ledger account, and an account may include no standard cost. |
| `fact_cost_absorption` | `production_order_id` | `fact_production_order` | 1:N | 1:many / optional | many:1 / always | Many absorptions belong to one production order, every absorption matches a production order, and a production order may include no absorption. |
| `fact_cost_absorption` | `cost_center_id` | `dim_cost_center` | 1:N | 1:many / optional | many:1 / always | Many absorptions belong to one cost center, every absorption matches a cost center, and a cost center may include no absorption. |
| `fact_cost_absorption` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / always | Many absorptions belong to one general-ledger account, every absorption matches an account, and an account may include no absorption. |
| `fact_cost_absorption` | `calendar_day_id` | `dim_calendar_day` | 1:N | 1:many / optional | many:1 / always | Many absorptions belong to one calendar day, every absorption matches a calendar day, and a calendar day may include no absorption. |
| `fact_purchase_price_variance` | `purchase_order_line_id` | `fact_purchase_order_line` | 1:N | 1:many / optional | many:1 / always | Many variances belong to one purchase order line, every variance matches a purchase order line, and a purchase order line may include no variance. |
| `fact_purchase_price_variance` | `item_revision_id` | `dim_item_revision` | 1:N | 1:many / optional | many:1 / always | Many variances belong to one item revision, every variance matches an item revision, and an item revision may include no variance. |
| `fact_purchase_price_variance` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / always | Many variances belong to one general-ledger account, every variance matches an account, and an account may include no variance. |
| `fact_freight_charge` | `shipment_id` | `fact_shipment` | 1:N | 1:many / optional | many:1 / optional | A freight charge may match one shipment, and a shipment may include no freight charge. |
| `fact_freight_charge` | `carrier_id` | `dim_carrier` | 1:N | 1:many / optional | many:1 / always | Many freight charges belong to one carrier, every freight charge matches a carrier, and a carrier may include no freight charge. |
| `fact_freight_charge` | `gl_account_id` | `dim_gl_account` | 1:N | 1:many / optional | many:1 / always | Many freight charges belong to one general-ledger account, every freight charge matches an account, and an account may include no freight charge. |
| `fact_freight_charge` | `currency_id` | `dim_currency` | 1:N | 1:many / optional | many:1 / always | Many freight charges share one currency, every freight charge matches a currency, and a currency may include no freight charge. |

## Dataset inventory

### bridge

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `bridge_employee_skill` | bridge | `employee_skill_id` | Skill held by an employee. |
| `bridge_employee_reporting` | bridge | `reporting_id` | Reporting line from an employee to a manager. |
| `bridge_item_plant` | bridge | `item_plant_id` | Authorization to stock or build an item at a plant. |
| `bridge_work_center_skill` | bridge | `work_center_skill_id` | Skill required to run a work center. |
| `bridge_bom_component` | bridge | `bom_component_id` | Component item consumed by a bill of materials. |
| `bridge_routing_operation` | bridge | `routing_operation_id` | Operation step on a routing, performed at a work center. |
| `bridge_item_customer` | bridge | `item_customer_id` | Commercial link between an item and a customer that buys it. |
| `bridge_supplier_item` | bridge | `supplier_item_id` | Source relationship between a supplier and an item. |
| `bridge_asset_spare` | bridge | `asset_spare_id` | Spare item that can be consumed by an asset. |
| `bridge_employee_work_center` | bridge | `qualification_id` | Qualification of an employee to work at a work center. |
| `bridge_characteristic_item` | bridge | `characteristic_applicability_id` | Applicability of a quality characteristic to an item revision. |
| `bridge_engineering_change_revision` | bridge | `engineering_change_revision_id` | Item revision an engineering change authorizes. |

### commercial

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_sales_channel` | dimension | `sales_channel_id` | Route to market through which a customer or order is sold. |
| `dim_incoterm` | dimension | `incoterm_id` | Trade term that allocates delivery cost and risk on an order. |
| `dim_reason_code` | dimension | `reason_code_id` | Coded reason for a return, adjustment, or inventory exception. |
| `dim_sales_representative` | dimension | `sales_rep_id` | Employee who sells to customers. |
| `fact_sales_quote` | fact | `quote_id` | Offer of price and quantity presented to a customer. |
| `fact_sales_quote_line` | fact | `quote_line_id` | Item revision and quantity offered on a sales quote. |
| `fact_sales_order` | fact | `sales_order_id` | Customer commitment to buy pumps or parts from a fulfilling plant. |
| `fact_sales_order_line` | fact | `sales_order_line_id` | Ordered quantity of an item revision on a sales order. |
| `fact_sales_order_schedule` | fact | `schedule_id` | Promised delivery of a sales order line to a ship-to. |
| `fact_shipment` | fact | `shipment_id` | Outbound shipment from a plant to a ship-to on a carrier. |
| `fact_shipment_line` | fact | `shipment_line_id` | Quantity of an item revision placed on a shipment. |
| `fact_customer_invoice` | fact | `invoice_id` | Invoice issued to a customer for goods or services. |
| `fact_customer_invoice_line` | fact | `customer_invoice_line_id` | Amount billed on a customer invoice, optionally against a shipment line. |
| `fact_customer_payment` | fact | `customer_payment_id` | Cash received from a customer, optionally applied to an invoice. |
| `fact_customer_return` | fact | `customer_return_id` | Goods returned by a customer, optionally against a sales order line. |

### execution

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_demand_forecast` | fact | `forecast_id` | Forecast quantity of an item at a plant on a day. |
| `fact_master_production_schedule` | fact | `mps_id` | Scheduled build quantity of an item at a plant on a day. |
| `fact_planned_order` | fact | `planned_order_id` | Planning suggestion to make an item revision at a plant. |
| `fact_production_order` | fact | `production_order_id` | Released or planned authority to make an item revision at a plant. |
| `fact_production_order_operation` | fact | `production_order_operation_id` | Operation step released on a production order. |
| `fact_operation_confirmation` | fact | `confirmation_id` | Reported good and scrap quantity against a production order operation. |
| `fact_labor_ticket` | fact | `labor_ticket_id` | Hours an employee charged to a work center and optionally to an order operation. |
| `fact_material_issue` | fact | `material_issue_id` | Quantity of an item issued from a storage location to a production order. |
| `fact_production_receipt` | fact | `production_receipt_id` | Quantity of an item revision received from a production order into stock. |
| `fact_capacity_load` | fact | `capacity_load_id` | Hours of load placed on a work center for a day. |
| `fact_kanban_signal` | fact | `kanban_signal_id` | Replenishment signal for an item at a storage location in a plant. |

### finance

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_gl_account` | dimension | `gl_account_id` | Ledger account owned by a legal entity. |
| `dim_payment_term` | dimension | `payment_term_id` | Commercial term that states when an invoice is due. |
| `fact_standard_cost` | fact | `standard_cost_id` | Standard cost amount of an item revision at a plant. |
| `fact_cost_absorption` | fact | `absorption_id` | Amount absorbed from a cost center to a production order. |
| `fact_purchase_price_variance` | fact | `ppv_id` | Variance between purchase price and standard for a purchase order line. |
| `fact_freight_charge` | fact | `freight_charge_id` | Freight amount charged by a carrier, optionally against a shipment. |

### inventory

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_warehouse` | dimension | `warehouse_id` | Building or yard that stores inventory at a plant. |
| `dim_storage_location` | dimension | `storage_location_id` | Bin, rack, or floor location inside a warehouse. |
| `dim_inventory_status` | dimension | `inventory_status_id` | Usability state of stock, such as available, hold, or inspection. |
| `dim_lot` | dimension | `lot_id` | Traceable batch of an item, optionally received from a supplier. |
| `dim_serial` | dimension | `serial_id` | Uniquely identified unit of an item, optionally tied to a lot. |
| `fact_inventory_balance` | fact | `balance_id` | On-hand quantity of an item in a storage location and inventory status. |
| `fact_inventory_transaction` | fact | `inventory_txn_id` | Movement or adjustment of an item quantity on a day. |
| `fact_inventory_destination` | fact | `inventory_destination_id` | Storage location that received quantity from an inventory transaction. |
| `fact_lot_genealogy` | fact | `genealogy_id` | Parent lot consumed by a genealogy link. The child lot is a separate descendant row. |
| `fact_lot_descendant` | fact | `lot_descendant_id` | Child lot created by one genealogy link. |
| `fact_cycle_count` | fact | `cycle_count_id` | Quantity an employee counted for an item in a storage location. |
| `fact_serial_history` | fact | `serial_event_id` | Lifecycle event recorded against a serial. |

### maintenance

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_asset` | dimension | `asset_id` | Maintainable equipment installed at a plant. |
| `dim_failure_code` | dimension | `failure_code_id` | Coded reason equipment stopped or required repair. |
| `dim_maintenance_crew` | dimension | `maintenance_crew_id` | Crew that performs maintenance at a plant. |
| `fact_downtime_event` | fact | `downtime_id` | Minutes a work center was down, optionally tied to an asset and failure. |
| `fact_maintenance_work_order` | fact | `maintenance_work_order_id` | Work order opened to repair or service an asset at a plant. |
| `fact_maintenance_labor` | fact | `maintenance_labor_id` | Hours an employee charged to a maintenance work order. |
| `fact_spare_consumption` | fact | `spare_consumption_id` | Quantity of an item consumed by a maintenance work order. |

### organization

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_enterprise` | dimension | `enterprise_id` | The company that owns every legal entity and plant. |
| `dim_legal_entity` | dimension | `legal_entity_id` | Incorporated owner of plants, cost centers, and ledger accounts. |
| `dim_plant` | dimension | `plant_id` | Manufacturing site where product is planned, made, stored, and shipped. |
| `dim_area` | dimension | `area_id` | Production area inside a plant, such as machining, assembly, or test. |
| `dim_production_line` | dimension | `production_line_id` | Line of resources that performs a stage of work inside an area. |
| `dim_work_center` | dimension | `work_center_id` | Resource that provides a class of capacity on a production line. |
| `dim_work_unit` | dimension | `work_unit_id` | Individual machine, bench, or station that reports production. |
| `dim_department` | dimension | `department_id` | Organizational unit at a plant that employs people and owns work centers. |
| `dim_cost_center` | dimension | `cost_center_id` | Responsibility center that collects manufacturing cost for a legal entity. |
| `dim_profit_center` | dimension | `profit_center_id` | Organizational unit that reports margin for a legal entity. |
| `dim_employee` | dimension | `employee_id` | Person employed by Alderford who can be assigned to work, supervision, or buying. |
| `dim_labor_skill` | dimension | `skill_id` | Named skill that qualifies a person or a work center for an operation. |
| `dim_shift` | dimension | `shift_id` | Named working shift at a plant. |
| `dim_calendar_day` | dimension | `calendar_day_id` | Civil day used to date plans, orders, movements, and cost postings. |
| `dim_planner` | dimension | `planner_id` | Employee authorized to plan supply for a plant. |
| `dim_reporting_manager` | dimension | `reporting_manager_id` | Employee designated as the manager on reporting lines. |

### party

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_currency` | dimension | `currency_id` | Currency used to price purchases, sales, and freight. |
| `dim_supplier` | dimension | `supplier_id` | External party that sells materials or services to Alderford. |
| `dim_supplier_site` | dimension | `supplier_site_id` | Order or ship-from location of a supplier. |
| `dim_customer` | dimension | `customer_id` | External party that buys pumps or spare parts from Alderford. |
| `dim_customer_ship_to` | dimension | `ship_to_id` | Destination address that can receive a customer shipment. |
| `dim_carrier` | dimension | `carrier_id` | Transportation company that can haul a shipment. |

### procurement

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `fact_purchase_requisition` | fact | `requisition_id` | Internal request to buy an item revision for a plant. |
| `fact_purchase_order` | fact | `purchase_order_id` | Order placed with a supplier site to supply a plant. |
| `fact_purchase_order_line` | fact | `purchase_order_line_id` | Ordered quantity of an item revision on a purchase order. |
| `fact_po_schedule` | fact | `po_schedule_id` | Due date for a portion of a purchase order line. |
| `fact_goods_receipt` | fact | `goods_receipt_id` | Quantity received against a purchase order line into a storage location. |
| `fact_supplier_invoice` | fact | `supplier_invoice_id` | Invoice received from a supplier. |
| `fact_supplier_invoice_line` | fact | `supplier_invoice_line_id` | Amount on a supplier invoice, optionally matched to a purchase order line. |
| `fact_supplier_payment` | fact | `supplier_payment_id` | Cash paid to a supplier, optionally applied to a supplier invoice. |
| `fact_supplier_return` | fact | `supplier_return_id` | Goods returned to a supplier, optionally against a purchase order line. |

### product

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_product_family` | dimension | `product_family_id` | Commercial family that groups related pump items. |
| `dim_commodity` | dimension | `commodity_id` | Purchasing commodity used to classify materials and parts. |
| `dim_unit_of_measure` | dimension | `uom_id` | Unit in which an item quantity is stocked, ordered, or shipped. |
| `dim_item` | dimension | `item_id` | Material or part that Alderford makes, buys, or uses as a phantom. |
| `dim_item_revision` | dimension | `item_revision_id` | Controlled engineering revision of an item. |
| `dim_bom_header` | dimension | `bom_header_id` | Bill of materials for a parent item revision at a plant. |
| `dim_routing_header` | dimension | `routing_id` | Manufacturing routing for an item revision at a plant. |
| `dim_operation` | dimension | `operation_id` | Standard manufacturing operation that can appear on a routing. |
| `dim_tool` | dimension | `tool_id` | Gauge, fixture, or tool kept at a plant and subject to calibration. |
| `dim_engineering_document` | dimension | `document_id` | Controlled document that may describe an item revision. |
| `dim_engineering_change` | dimension | `engineering_change_id` | Change order that authorizes a revision to product definition. |

### quality

| Dataset | Role | Grain | Description |
| --- | --- | --- | --- |
| `dim_quality_characteristic` | dimension | `characteristic_id` | Measurable characteristic inspected on a pump, part, or tool. |
| `dim_defect_code` | dimension | `defect_code_id` | Coded reason a part or assembly fails to conform. |
| `dim_disposition_code` | dimension | `disposition_code_id` | Coded decision applied to nonconforming material. |
| `dim_inspection_plan` | dimension | `inspection_plan_id` | Plan that states how an item revision is inspected. |
| `fact_inspection_result` | fact | `inspection_result_id` | Measured result of a characteristic against an inspection plan. |
| `fact_nonconformance` | fact | `nonconformance_id` | Recorded failure of an item revision to meet requirements at a plant. |
| `fact_ncr_disposition` | fact | `disposition_id` | Disposition decision recorded against a nonconformance. |
| `fact_scrap_event` | fact | `scrap_event_id` | Quantity of an item scrapped, optionally from a production order operation. |
| `fact_calibration_result` | fact | `calibration_id` | Result of calibrating a tool on a day. |

## Provenance

This model is an original warehouse-style ontology informed by the publicly described ISA-95 and IEC 62264 equipment hierarchy and by APICS/ASCM manufacturing entities such as the item, bill of material, routing, production order, and inventory transaction. It is not a copy of SAP, Oracle, or any vendor DDL. No synthetic row statistics are included.
