# Earnings-call candidate coverage

Provenance is analyst questions on recent earnings calls, not an appointed business domain.
Membership is the S&P 500 list of companies (Wikipedia table of GICS sector and sub-industry,
checked 2026-10-05). Each row is one GICS sub-industry with two current constituents.

These directories are a candidate pool. They are not Critic assessment domains, and they do not
contain reference catalogs, generated catalogs, or gold analytical knowledge graphs.

Status values: `selected` (pair locked, transcripts not read), `extracting`, `questions-ready`,
`partial` (fewer than four calls or a thin Q&A), `blocked`.

| # | GICS sector | GICS sub-industry | Ticker | Company | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Information Technology | Semiconductors | NVDA | Nvidia | extracting |
| 1 | Information Technology | Semiconductors | AVGO | Broadcom | extracting |
| 2 | Information Technology | Semiconductor Materials & Equipment | AMAT | Applied Materials | extracting |
| 2 | Information Technology | Semiconductor Materials & Equipment | LRCX | Lam Research | extracting |
| 3 | Information Technology | Systems Software | MSFT | Microsoft | extracting |
| 3 | Information Technology | Systems Software | NOW | ServiceNow | extracting |
| 4 | Information Technology | Application Software | CRM | Salesforce | extracting |
| 4 | Information Technology | Application Software | ORCL | Oracle | extracting |
| 5 | Information Technology | Technology Hardware, Storage & Peripherals | AAPL | Apple | extracting |
| 5 | Information Technology | Technology Hardware, Storage & Peripherals | DELL | Dell Technologies | extracting |
| 6 | Communication Services | Interactive Media & Services | GOOGL | Alphabet | extracting |
| 6 | Communication Services | Interactive Media & Services | META | Meta Platforms | extracting |
| 7 | Communication Services | Movies & Entertainment | NFLX | Netflix | extracting |
| 7 | Communication Services | Movies & Entertainment | DIS | Walt Disney | extracting |
| 8 | Communication Services | Integrated Telecommunication Services | T | AT&T | extracting |
| 8 | Communication Services | Integrated Telecommunication Services | VZ | Verizon | extracting |
| 9 | Consumer Discretionary | Broadline Retail | AMZN | Amazon | extracting |
| 9 | Consumer Discretionary | Broadline Retail | EBAY | eBay | extracting |
| 10 | Consumer Discretionary | Home Improvement Retail | HD | Home Depot | extracting |
| 10 | Consumer Discretionary | Home Improvement Retail | LOW | Lowe's | extracting |
| 11 | Consumer Discretionary | Automobile Manufacturers | TSLA | Tesla | extracting |
| 11 | Consumer Discretionary | Automobile Manufacturers | GM | General Motors | extracting |
| 12 | Consumer Discretionary | Restaurants | MCD | McDonald's | extracting |
| 12 | Consumer Discretionary | Restaurants | SBUX | Starbucks | extracting |
| 13 | Consumer Staples | Consumer Staples Merchandise Retail | WMT | Walmart | extracting |
| 13 | Consumer Staples | Consumer Staples Merchandise Retail | COST | Costco | extracting |
| 14 | Consumer Staples | Soft Drinks & Non-alcoholic Beverages | KO | Coca-Cola | extracting |
| 14 | Consumer Staples | Soft Drinks & Non-alcoholic Beverages | PEP | PepsiCo | extracting |
| 15 | Consumer Staples | Packaged Foods & Meats | MDLZ | Mondelez | extracting |
| 15 | Consumer Staples | Packaged Foods & Meats | GIS | General Mills | extracting |
| 16 | Financials | Diversified Banks | JPM | JPMorgan Chase | extracting |
| 16 | Financials | Diversified Banks | BAC | Bank of America | extracting |
| 17 | Financials | Investment Banking & Brokerage | GS | Goldman Sachs | extracting |
| 17 | Financials | Investment Banking & Brokerage | MS | Morgan Stanley | extracting |
| 18 | Financials | Transaction & Payment Processing Services | V | Visa | extracting |
| 18 | Financials | Transaction & Payment Processing Services | MA | Mastercard | extracting |
| 19 | Financials | Property & Casualty Insurance | PGR | Progressive | extracting |
| 19 | Financials | Property & Casualty Insurance | CB | Chubb | extracting |
| 20 | Health Care | Pharmaceuticals | LLY | Eli Lilly | extracting |
| 20 | Health Care | Pharmaceuticals | MRK | Merck | extracting |
| 21 | Health Care | Managed Health Care | UNH | UnitedHealth Group | extracting |
| 21 | Health Care | Managed Health Care | ELV | Elevance Health | extracting |
| 22 | Health Care | Health Care Equipment | SYK | Stryker | extracting |
| 22 | Health Care | Health Care Equipment | ISRG | Intuitive Surgical | extracting |
| 23 | Industrials | Aerospace & Defense | RTX | RTX | extracting |
| 23 | Industrials | Aerospace & Defense | LMT | Lockheed Martin | extracting |
| 24 | Industrials | Construction Machinery & Heavy Transportation Equipment | CAT | Caterpillar | extracting |
| 24 | Industrials | Construction Machinery & Heavy Transportation Equipment | PCAR | PACCAR | extracting |
| 25 | Industrials | Rail Transportation | UNP | Union Pacific | extracting |
| 25 | Industrials | Rail Transportation | CSX | CSX | extracting |
| 26 | Industrials | Passenger Airlines | DAL | Delta Air Lines | extracting |
| 26 | Industrials | Passenger Airlines | UAL | United Airlines | extracting |
| 27 | Energy | Integrated Oil & Gas | XOM | Exxon Mobil | extracting |
| 27 | Energy | Integrated Oil & Gas | CVX | Chevron | extracting |
| 28 | Materials | Specialty Chemicals | SHW | Sherwin-Williams | extracting |
| 28 | Materials | Specialty Chemicals | ECL | Ecolab | extracting |
| 29 | Real Estate | Data Center REITs | EQIX | Equinix | extracting |
| 29 | Real Estate | Data Center REITs | DLR | Digital Realty | extracting |
| 30 | Utilities | Electric Utilities | SO | Southern Company | extracting |
| 30 | Utilities | Electric Utilities | DUK | Duke Energy | extracting |

Question files, once extracted, live at `{sub-industry-slug}/{ticker}/questions.md` under this
directory. Slugs are lowercase hyphenated sub-industry names.
