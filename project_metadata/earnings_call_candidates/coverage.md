# Earnings-call candidate coverage

Provenance is analyst questions on recent earnings calls, not an appointed business domain.
Membership is the S&P 500 list of companies (Wikipedia table of GICS sector and sub-industry,
checked 2026-10-05). Each row is one GICS sub-industry with two current constituents.

These directories are a candidate pool. They are not Critic assessment domains, and they do not
contain reference catalogs, generated catalogs, or gold analytical knowledge graphs.

Status values: `selected` (pair locked, transcripts not read), `extracting`, `questions-ready`,
`partial` (fewer than four calls or a thin Q&A), `blocked`.

Every pair below is `questions-ready`: four recent calls were read and analyst questions were
paraphrased into `{slug}/{ticker}/questions.md`. Schema YAML has not been started. See
`summary-report.md` for counts and the simulation shortlist.

| # | GICS sector | GICS sub-industry | Ticker | Company | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Information Technology | Semiconductors | NVDA | Nvidia | questions-ready |
| 1 | Information Technology | Semiconductors | AVGO | Broadcom | questions-ready |
| 2 | Information Technology | Semiconductor Materials & Equipment | AMAT | Applied Materials | questions-ready |
| 2 | Information Technology | Semiconductor Materials & Equipment | LRCX | Lam Research | questions-ready |
| 3 | Information Technology | Systems Software | MSFT | Microsoft | questions-ready |
| 3 | Information Technology | Systems Software | NOW | ServiceNow | questions-ready |
| 4 | Information Technology | Application Software | CRM | Salesforce | questions-ready |
| 4 | Information Technology | Application Software | ORCL | Oracle | questions-ready |
| 5 | Information Technology | Technology Hardware, Storage & Peripherals | AAPL | Apple | questions-ready |
| 5 | Information Technology | Technology Hardware, Storage & Peripherals | DELL | Dell Technologies | questions-ready |
| 6 | Communication Services | Interactive Media & Services | GOOGL | Alphabet | questions-ready |
| 6 | Communication Services | Interactive Media & Services | META | Meta Platforms | questions-ready |
| 7 | Communication Services | Movies & Entertainment | NFLX | Netflix | questions-ready |
| 7 | Communication Services | Movies & Entertainment | DIS | Walt Disney | questions-ready |
| 8 | Communication Services | Integrated Telecommunication Services | T | AT&T | questions-ready |
| 8 | Communication Services | Integrated Telecommunication Services | VZ | Verizon | questions-ready |
| 9 | Consumer Discretionary | Broadline Retail | AMZN | Amazon | questions-ready |
| 9 | Consumer Discretionary | Broadline Retail | EBAY | eBay | questions-ready |
| 10 | Consumer Discretionary | Home Improvement Retail | HD | Home Depot | questions-ready |
| 10 | Consumer Discretionary | Home Improvement Retail | LOW | Lowe's | questions-ready |
| 11 | Consumer Discretionary | Automobile Manufacturers | TSLA | Tesla | questions-ready |
| 11 | Consumer Discretionary | Automobile Manufacturers | GM | General Motors | questions-ready |
| 12 | Consumer Discretionary | Restaurants | MCD | McDonald's | questions-ready |
| 12 | Consumer Discretionary | Restaurants | SBUX | Starbucks | questions-ready |
| 13 | Consumer Staples | Consumer Staples Merchandise Retail | WMT | Walmart | questions-ready |
| 13 | Consumer Staples | Consumer Staples Merchandise Retail | COST | Costco | questions-ready |
| 14 | Consumer Staples | Soft Drinks & Non-alcoholic Beverages | KO | Coca-Cola | questions-ready |
| 14 | Consumer Staples | Soft Drinks & Non-alcoholic Beverages | PEP | PepsiCo | questions-ready |
| 15 | Consumer Staples | Packaged Foods & Meats | MDLZ | Mondelez | questions-ready |
| 15 | Consumer Staples | Packaged Foods & Meats | GIS | General Mills | questions-ready |
| 16 | Financials | Diversified Banks | JPM | JPMorgan Chase | questions-ready |
| 16 | Financials | Diversified Banks | BAC | Bank of America | questions-ready |
| 17 | Financials | Investment Banking & Brokerage | GS | Goldman Sachs | questions-ready |
| 17 | Financials | Investment Banking & Brokerage | MS | Morgan Stanley | questions-ready |
| 18 | Financials | Transaction & Payment Processing Services | V | Visa | questions-ready |
| 18 | Financials | Transaction & Payment Processing Services | MA | Mastercard | questions-ready |
| 19 | Financials | Property & Casualty Insurance | PGR | Progressive | questions-ready |
| 19 | Financials | Property & Casualty Insurance | CB | Chubb | questions-ready |
| 20 | Health Care | Pharmaceuticals | LLY | Eli Lilly | questions-ready |
| 20 | Health Care | Pharmaceuticals | MRK | Merck | questions-ready |
| 21 | Health Care | Managed Health Care | UNH | UnitedHealth Group | questions-ready |
| 21 | Health Care | Managed Health Care | ELV | Elevance Health | questions-ready |
| 22 | Health Care | Health Care Equipment | SYK | Stryker | questions-ready |
| 22 | Health Care | Health Care Equipment | ISRG | Intuitive Surgical | questions-ready |
| 23 | Industrials | Aerospace & Defense | RTX | RTX | questions-ready |
| 23 | Industrials | Aerospace & Defense | LMT | Lockheed Martin | questions-ready |
| 24 | Industrials | Construction Machinery & Heavy Transportation Equipment | CAT | Caterpillar | questions-ready |
| 24 | Industrials | Construction Machinery & Heavy Transportation Equipment | PCAR | PACCAR | questions-ready |
| 25 | Industrials | Rail Transportation | UNP | Union Pacific | questions-ready |
| 25 | Industrials | Rail Transportation | CSX | CSX | questions-ready |
| 26 | Industrials | Passenger Airlines | DAL | Delta Air Lines | questions-ready |
| 26 | Industrials | Passenger Airlines | UAL | United Airlines | questions-ready |
| 27 | Energy | Integrated Oil & Gas | XOM | Exxon Mobil | questions-ready |
| 27 | Energy | Integrated Oil & Gas | CVX | Chevron | questions-ready |
| 28 | Materials | Specialty Chemicals | SHW | Sherwin-Williams | questions-ready |
| 28 | Materials | Specialty Chemicals | ECL | Ecolab | questions-ready |
| 29 | Real Estate | Data Center REITs | EQIX | Equinix | questions-ready |
| 29 | Real Estate | Data Center REITs | DLR | Digital Realty | questions-ready |
| 30 | Utilities | Electric Utilities | SO | Southern Company | questions-ready |
| 30 | Utilities | Electric Utilities | DUK | Duke Energy | questions-ready |

Question files, once extracted, live at `{sub-industry-slug}/{ticker}/questions.md` under this
directory. Slugs are lowercase hyphenated sub-industry names.
