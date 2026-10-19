# Warehouse model learnings

Joined from the Checkpoint A reviews and the review of the eleven models written before the four-checkpoint plan. These are the rules used for the Muse Wonder rebuilds.

## Grain

- A fact grain is the combination that makes one row: fiscal period, scenario, and the business keys.
- Say that combination in `grain.description`. Each grain component matches an entity definition, with column names in ascending order.
- A surrogate such as `volume_id` may exist on the row. It is not the grain. "One row is one volume" does not say which quarter, commodity, and region that row is.
- The dimension that owns an identity is a complete population. A fact that references it is partial.

## Measures

- Do not store an analyst conclusion as a column. Names ending in `_flag`, and descriptions such as "whether this row is marked," record a judgment instead of a measure.
- Classifications belong on dimension codes.
- A measure description names the unit: carloads, revenue ton-miles, dollars, barrels, megawatt-hours, impressions, member-months.
- Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity.
- A rate needs its denominator at a grain that can join. Yield needs revenue ton-miles. Airline unit cost needs available seat-miles. Average check needs a check count. Price mix needs unit cases and net revenue. Member margin needs member-months.
- An enterprise total — earnings, cash, free cash flow, operating ratio, rate base, openings to a company goal — is grained at the enterprise or the reporting segment. Do not hang it on a cost bucket, a play, a hub, or a capital program, and do not repeat one company-wide total on every child row.

## Dimensions

- One code list holds one axis. Do not put values that can be true at once in a mutually exclusive list.
- Do not put a parent and its children in the same list. Merchandise is not a peer of coal. A reporting segment is not a peer of a product. A warehouse club is not a peer of Sam's Club and of international.
- Split route to market from buyer segment, rate class from sales-pipeline stage, query intent from how the answer is displayed, and a plant from the technology inside it.
- `guidance_horizon` does not belong on the fiscal quarter. A quarter can be a reported result and, in another row, a guide. That distinction is a scenario dimension with `reported` and `guide`.

## Both companies

- One imaginary owner still has to answer both companies' questions. A mapped heading is not coverage when the columns cannot express the distinction the question asks.
- Do not put both companies' reportable-segment names in one mutually exclusive list.
- Where the operating processes differ, give each process its own fact or a process-type dimension. Examples that failed this test: McDonald's franchise economics used for Starbucks licenses, Equinix cabinets used for Digital Realty megawatts, Apple device families used for Dell servers, Stryker franchises used for Intuitive procedures, Caterpillar machines used for PACCAR trucks, Coca-Cola unit cases used for PepsiCo snacks, and GM dealer wholesale used for Tesla direct delivery.
- Two similar operators, such as two class-I railroads, do not need a company dimension. A company or reporting-unit dimension is required when a row cannot otherwise be traced to the business that produced it.

## Coverage and size

- Every numbered question from both `questions.md` files appears once in a slice `coverage.md`. The company is part of that mapping, either in the heading or in a company section, because both companies reuse quarter and number.
- Every mapped column exists in the YAML.
- Reusable facts beat one fact per question. The dataset floor for these warehouses is 70.
- A clean graph build — zero unknown fields and zero contradictory edges — does not mean the grain, the code lists, or the two-company fit are right.
