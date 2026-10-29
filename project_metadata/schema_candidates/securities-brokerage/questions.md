# Halyard Securities

Catalog: `securities-brokerage`

These questions are analytical decisions for ontology assessment. Each asks for a comparison, concentration, gap, trend, or exception across a population. Many of them cross the operational, landing, and warehouse layers, or join on a durable key in one layer and a version surrogate key in another.

## Best execution analyst

This role reviews where non-directed orders are routed and whether customers receive the price available at receipt. It owns orders, routes, venue executions, the Rule 605 execution-quality mart, and the Rule 606 routing mart. Missing a pattern leaves order flow at a venue that pays for it but fills worse than the alternatives.

| request_desc | impact | question | core_datasets |
| --- | --- | --- | --- |
| Compare price improvement by venue for the same order type and size bucket. | Flow stays at a venue that pays more but fills worse. | Which venues deliver less price improvement per share than other venues on the same order type and size bucket, and how much flow do they receive? | Execution quality; Venue dimension; Customer order; Order execution; Security dimension; Date dimension |
| Reconcile payment for order flow received with routing share by venue and month. | The Rule 606 report misstates the financial relationship with a venue. | For each month and order class, which venues' share of routed orders is out of line with their share of net payment received? | Order routing month; Order route; Execution venue; Month dimension; Customer order |
| Find orders that were routed several times before any fill. | Latency and missed fills are treated as venue issues when the router causes them. | Which securities, order types, and times of day concentrate orders that took three or more routes before their first execution? | Customer order; Order route; Order execution; Order event; Security; Time dimension |
| Track fill rates for marketable limit orders around the open and the close. | Customers miss fills in the busiest minutes, and nobody looks at the router logic for them. | How does the fill rate of marketable limit orders trend across the first and last 15 minutes of each trading day, by venue? | Execution quality; Customer order; Order execution; Execution venue; Market calendar; Time dimension |
| Find order events whose CAT submission was rejected or repaired. | CAT error rates rise above regulatory thresholds without anyone seeing which events fail. | Which order event types, channels, and venues concentrate CAT events that were rejected or repaired? | CAT reportable event; Customer order; Order event; Order route; Execution venue |

## Margin and credit risk analyst

This role sets house margin requirements and watches concentrated and under-margined accounts. It owns margin accounts, calls, daily risk, and the margin exposure mart. Missing a concentration lets one security's drop turn into unsecured debit balances.

| request_desc | impact | question | core_datasets |
| --- | --- | --- | --- |
| Find securities that are the largest position in many margin accounts with thin excess equity. | One price drop issues calls across many accounts at once. | Which securities are the top position in the most margin accounts whose house excess is under 10 percent of equity, and what is their combined debit? | Margin exposure daily; Security dimension; Account dimension; Account risk daily; Margin account |
| Compare margin calls that were met with those that ended in liquidation, by call type and broker. | Calls are extended for accounts that end in liquidation anyway. | Which call types, brokers, and branches concentrate margin calls that ended in liquidation rather than being met? | Margin call; Customer account; Broker; Branch; Margin account |
| Relate daily value at risk to the next day's realized loss. | The VaR model understates loss for a group of accounts and nobody recalibrates it. | For which account tiers and options levels does realized loss on the next business day exceed the prior day's 99 percent VaR more often than 1 percent of days? | Account risk daily; Account daily snapshot; Margin account; Customer account; Customer |
| Find fully paid lending loans on positions that are now short of the lent quantity. | Lent shares exceed the position, and the firm has an unsecured obligation. | Which open securities loans exceed the current net position of the account in that security? | Securities loan; Holding summary; Customer account; Security |

## Broker and branch performance analyst

This role manages the book of business of brokers and branches. It owns the broker month mart, account servicing, complaints, and registrations. Missing an outlier keeps an unproductive or risky broker in place.

| request_desc | impact | question | core_datasets |
| --- | --- | --- | --- |
| Compare broker production with complaints naming the broker. | High producers with unsuitable trading complaints keep their books. | Which brokers rank in the top quartile of commission and also in the top quartile of complaints per serviced account? | Broker month; Complaint fact; Broker dimension; Customer complaint; Broker |
| Find accounts lost when a broker left the firm. | Assets follow a departing broker and nobody acts on the remaining accounts. | For brokers whose employee record terminated, what share of their accounts transferred out by ACATS within 90 days, by branch? | Employee; Broker; Customer account; ACATS transfer; Branch; Broker month |
| Find brokers trading in states where they are not registered. | The firm executes for an unregistered representative. | Which brokers entered orders for customers whose home state is not among the broker's active registrations? | Customer order; Broker; Employee; Registration; Customer; Address; Zip code |
| Track assets under care by branch region. | A region's decline is masked by one large branch. | How does assets under care per broker trend by branch region across the last 12 months? | Broker month; Branch dimension; Branch; Month dimension |

## Customer growth and retention analyst

This role manages acquisition, segment migration, and churn. It owns the customer month mart, net new assets, prospects, digital engagement, and service contacts. Missing a churn signal lets assets leave without an intervention.

| request_desc | impact | question | core_datasets |
| --- | --- | --- | --- |
| Find the engagement pattern that precedes an ACATS transfer out. | Retention offers go to customers who were never leaving. | How do sessions, service contacts, and trades change over the three months before a customer's first outgoing ACATS transfer, compared with customers who stayed? | Customer month; Digital engagement daily; Service interaction; ACATS transfer; Customer account; Customer |
| Compare net new assets by segment and funding method. | Growth targets credit the wrong channel. | Which segments and transfer methods account for net new assets, and how does the mix trend by month? | Net new assets; Funding transfer; ACATS transfer; Customer month; Customer segment dimension; Month dimension |
| Measure prospect conversion by marketing nameplate. | Purchased lists are renewed for segments that never convert. | Which marketing nameplates have the highest share of prospects that later appear as customers, and how much do those customers hold after a year? | Prospect; Prospect feed; Customer dimension; Customer month |
| Find customers who moved between segments and why. | Service models are assigned from a stale segment. | Which customers changed segment in the last quarter, and how much of the change came from market movement rather than flows? | Customer month; Customer segment dimension; Net new assets; Account daily snapshot |

## AML and surveillance analyst

This role investigates money laundering and market abuse. It owns AML alerts and cases, surveillance alerts, KYC reviews, and money movement. Missing a pattern leaves a suspicious account open and unreported.

| request_desc | impact | question | core_datasets |
| --- | --- | --- | --- |
| Find accounts with rapid deposit-trade-withdraw cycles in low-priced securities. | Layering through the brokerage goes undetected. | Which accounts deposited, traded low-priced securities, and withdrew most of the deposit within five business days, more than twice in a quarter? | Funding transfer; Trade; Security; Daily market; Customer account; AML alert |
| Compare alert-to-case escalation rates by monitoring rule. | Analysts spend time on rules that never escalate while a productive rule is under-tuned. | Which AML rules have the lowest share of alerts escalated to cases, and the highest share of cases that end in a SAR? | AML alert fact; AML alert; AML case; KYC review |
| Find surveillance alerts on trades placed shortly before a news item about the issuer. | Possible insider trading is closed as noise. | Which trades flagged for insider or front-running patterns were placed within two days before a news item naming the issuing company? | Trade surveillance alert; Trade; Security; Company; News cross-reference; News item |
| Find high-risk customers overdue for periodic review. | The firm misses its due diligence schedule for its riskiest customers. | Which customers rated high risk have no KYC review in the last 12 months but have AML alerts in that period? | KYC review; Customer; AML alert; Customer account |
| Track time to close surveillance alerts by pattern. | A backlog in one pattern grows unseen. | How does the time from alert to close trend by pattern and reviewer across the year? | Surveillance alert fact; Trade surveillance alert; Employee; Date dimension |

## Finance and revenue analyst

This role reports revenue by source and account economics. It owns the revenue mart, trade fees, cash sweep, lending, and corporate actions. Missing a shift overstates the durability of a revenue line.

| request_desc | impact | question | core_datasets |
| --- | --- | --- | --- |
| Break revenue into trading, margin interest, sweep, payment for order flow, and lending by tier. | Pricing changes target the wrong tier. | How does revenue per account by source compare across customer tiers and segments by quarter? | Revenue daily; Account dimension; Customer dimension; Customer tier; Customer segment dimension; Date dimension |
| Reconcile booked commissions with the commission schedule. | Customers are over- or under-charged and nobody sees it until a complaint. | Which completed trades carry a commission that differs from the rate implied by the customer's tier, trade type, exchange, and quantity band? | Trade; Commission rate; Customer account; Customer; Security; Exchange; Trade charge |
| Compare the sweep spread with cash balances by program bank. | Sweep economics are booked from a stale rate table. | Which program banks earn the widest spread between bank and client rates, and how much client cash do they hold each month? | Cash sweep balance; Customer account; Cash balances fact |
| Measure cash paid on corporate actions against entitlements. | Dividends are paid short and customers notice before finance does. | Which corporate actions paid less cash than the sum of their account entitlements, and by how much? | Corporate action impact; Corporate action entitlement; Corporate action; Security |
| Find realized losses disallowed under the wash-sale rule by tier. | Year-end tax forms surprise customers and drive complaints. | Which tiers and securities concentrate disallowed wash-sale losses, and how many of those accounts later filed a fees or tax complaint? | Realized gain; Tax form; Customer complaint; Customer account; Customer |

## Data integration engineer

This role owns the nightly load from the operational system and the landing files into the warehouse. It owns the landing feeds, the TPC-DI dimensions and facts, DImessages, and Audit. Missing a gap makes every downstream report wrong in the same way.

| request_desc | impact | question | core_datasets |
| --- | --- | --- | --- |
| Reconcile completed operational trades with the warehouse trade dimension. | Revenue and holdings in the warehouse miss trades that the OLTP system booked. | Which completed operational trades are missing from the trade dimension or have a different trade price, by trade date and batch? | Trade; Trade feed; Trade dimension; Date dimension; Data integration messages |
| Find FINWIRE security records whose issuer does not resolve to a company. | Securities load without a company version and fall out of every issuer report. | Which FINWIRE security records name an issuer by company name that does not match any FINWIRE company record posted before it? | FINWIRE security records; FINWIRE company records; Security dimension; Company dimension |
| Compare audit expectations with loaded row counts per batch. | A short batch is accepted and the warehouse silently drops a day. | For each batch, which audited attributes differ from the counts actually loaded into the customer, account, trade, and cash balance tables? | Audit; Data integration messages; CustomerMgmt feed; Trade feed; Customer dimension; Account dimension; Cash balances fact |
| Find customer versions whose account versions point at a superseded customer version. | Account history attributes trades to an outdated customer record. | Which current account versions reference a customer version that is no longer current? | Account dimension; Customer dimension; CustomerMgmt feed |
| Compare operational positions with warehouse holdings. | Customers see different positions in statements and analytics. | Which account and security positions in the operational position summary differ from the net of the latest warehouse holdings facts? | Holding summary; Holding; Holdings fact; Account dimension; Security dimension |
