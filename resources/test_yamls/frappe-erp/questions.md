# ERPNext and Frappe HRMS

Catalog: `frappe-erp`

These questions are for a finance, inventory, or HR analyst. Each one asks for a comparison, a concentration, or an exception. Dataset names are qualified names. Columns are the physical columns on those datasets.

## 1. Overdue receivables

Open invoices that age past their terms tie up cash and get missed when collection follows the largest customer instead of the oldest balance.

Which customer groups and companies concentrate sales invoices whose `outstanding_amount` is still open after `due_date`, and how does that balance compare with `grand_total`?

| Dataset | Columns |
| --- | --- |
| `frappe-erp.accounts.sales_invoice` | `customer`, `company`, `posting_date`, `due_date`, `grand_total`, `outstanding_amount`, `status` |
| `frappe-erp.selling.customer` | `customer_name`, `customer_group`, `territory`, `disabled` |

## 2. Payables and suppliers on hold

A supplier on hold can still carry an old unpaid balance, and a release date can hide which invoices are actually blocked.

Which suppliers have purchase invoices with a remaining `outstanding_amount` after `due_date`, and which of those suppliers are `on_hold`?

| Dataset | Columns |
| --- | --- |
| `frappe-erp.accounts.purchase_invoice` | `supplier`, `company`, `posting_date`, `due_date`, `grand_total`, `outstanding_amount`, `status` |
| `frappe-erp.buying.supplier` | `supplier_name`, `supplier_group`, `on_hold`, `hold_type`, `release_date`, `disabled` |

## 3. Receipts that never clear an invoice

Unallocated cash looks like collections until someone tries to match it to an invoice. A growing remainder means the allocation step is being skipped.

Which companies, parties, and months have payment entries whose `unallocated_amount` stays a large share of `paid_amount`?

| Dataset | Columns |
| --- | --- |
| `frappe-erp.accounts.payment_entry` | `payment_type`, `posting_date`, `company`, `party_type`, `party`, `paid_amount`, `unallocated_amount` |
| `frappe-erp.accounts.sales_invoice` | `customer`, `company`, `outstanding_amount`, `posting_date`, `due_date` |

## 4. Cancelled ledger lines in expense accounts

Cancellation that still leaves `is_cancelled` rows in the ledger changes profit if a report adds them back in. Expense accounts are where that shows up first.

Which expense accounts and cost centers get the largest `debit` and `credit` from general ledger rows with `is_cancelled` set, compared with rows that are not cancelled?

| Dataset | Columns |
| --- | --- |
| `frappe-erp.accounts.gl_entry` | `account`, `debit`, `credit`, `posting_date`, `company`, `cost_center`, `voucher_type`, `is_cancelled`, `party_type`, `party` |
| `frappe-erp.accounts.account` | `account_name`, `root_type`, `account_type`, `company`, `is_group` |

## 5. Budget against the ledger

A budget that only warns, and never stops, lets a cost center overspend for the whole year. The ledger is the actual; the budget row is the limit.

Which cost centers and accounts have general-ledger spend above `budget_amount` for the budget's fiscal range, and which of those budgets are set to warn or ignore rather than stop?

| Dataset | Columns |
| --- | --- |
| `frappe-erp.accounts.budget` | `budget_against`, `company`, `cost_center`, `account`, `budget_amount`, `from_fiscal_year`, `to_fiscal_year`, `action_if_annual_budget_exceeded` |
| `frappe-erp.accounts.gl_entry` | `account`, `cost_center`, `company`, `debit`, `credit`, `posting_date`, `is_cancelled` |

## 6. Stock that is already promised away

A bin can show quantity on hand while `projected_qty` is already negative because of reservations. Picking against that bin creates backorders.

Which items and warehouses have `projected_qty` below zero, how much of that gap is `reserved_qty` rather than `actual_qty`, and which item groups account for the reserved value?

| Dataset | Columns |
| --- | --- |
| `frappe-erp.stock.bin` | `item_code`, `warehouse`, `actual_qty`, `reserved_qty`, `ordered_qty`, `projected_qty`, `valuation_rate`, `company` |
| `frappe-erp.stock.item` | `item_code`, `item_name`, `item_group`, `is_stock_item`, `disabled`, `has_batch_no` |
| `frappe-erp.stock.stock_ledger_entry` | `item_code`, `warehouse`, `actual_qty`, `qty_after_transaction`, `posting_date`, `voucher_type`, `company` |

## 7. Expired batches that still have quantity

Shipping an expired batch is a quality failure. A batch can stay in stock after `expiry_date` when receipts and issues never drew it down.

Which items and batches have `expiry_date` in the past and `batch_qty` still above zero, and which item groups hold the most of that quantity?

| Dataset | Columns |
| --- | --- |
| `frappe-erp.stock.batch` | `batch_id`, `item`, `expiry_date`, `batch_qty`, `manufacturing_date`, `disabled` |
| `frappe-erp.stock.item` | `item_name`, `item_group`, `has_batch_no`, `end_of_life`, `disabled` |

## 8. Work orders past the delivery date

A work order that has moved material and still has not finished by `expected_delivery_date` blocks both the sales order and the warehouse.

Which production items and companies have work orders whose `produced_qty` is still below `qty` after `expected_delivery_date`, and how much material was already transferred?

| Dataset | Columns |
| --- | --- |
| `frappe-erp.manufacturing.work_order` | `production_item`, `bom_no`, `qty`, `produced_qty`, `material_transferred_for_manufacturing`, `status`, `company`, `planned_start_date`, `expected_delivery_date` |
| `frappe-erp.manufacturing.bom` | `item`, `is_active`, `is_default`, `company`, `quantity` |

## 9. Attendance and leave after an employee leaves

Payroll and headcount stay wrong when a leaver is still marked present, or when a leave application runs past `relieving_date`.

Which departments have employees whose `status` is Left and who still have attendance or leave on or after `relieving_date`?

| Dataset | Columns |
| --- | --- |
| `frappe-erp.setup.employee` | `employee_name`, `status`, `department`, `designation`, `reports_to`, `company`, `date_of_joining`, `relieving_date` |
| `frappe-erp.hr.attendance` | `employee`, `attendance_date`, `status`, `department`, `company`, `working_hours`, `late_entry` |
| `frappe-erp.hr.leave_application` | `employee`, `leave_type`, `from_date`, `to_date`, `total_leave_days`, `status`, `company` |

## 10. Expense claims cut at approval

A wide gap between the claimed amount and the sanctioned amount means either the policy is unclear or approvers are cutting one department harder than the others.

Which companies and employee departments have expense claims where `total_sanctioned_amount` is far below `total_claimed_amount`, and how does that gap line up with `approval_status`?

| Dataset | Columns |
| --- | --- |
| `frappe-erp.hr.expense_claim` | `employee`, `company`, `posting_date`, `approval_status`, `status`, `total_claimed_amount`, `total_sanctioned_amount` |
| `frappe-erp.setup.employee` | `department`, `designation`, `reports_to`, `company`, `status` |
