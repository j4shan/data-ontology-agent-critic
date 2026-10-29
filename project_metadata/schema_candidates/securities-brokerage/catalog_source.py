"""Authoring source for the `securities-brokerage` catalog.

The operational layer follows the TPC-E brokerage schema and the warehouse layer follows the
TPC-DI target schema. Both are extended with order management, money movement, margin,
compliance, workforce, and analytic marts. `build_catalog.py` turns these definitions into
schema version 4 intermediary YAML.
"""

from __future__ import annotations

ROOT = "securities-brokerage"

OLTP = {
    "schema_id": "accessor.sql-database.v1",
    "family": "sql-database",
    "expression_context": "PostgreSQL column reference",
    "properties": {"host": "oltp.halyard.internal", "database": "brokerage", "dialect": "postgresql"},
}
WAREHOUSE = {
    "schema_id": "accessor.snowflake.v1",
    "family": "snowflake",
    "expression_context": "Snowflake column reference",
    "properties": {"account": "halyard.us-east-1", "database": "SECURITIES_BROKERAGE"},
}


def c(name: str, description: str, value_description: str = "", synonyms: tuple[str, ...] = ()) -> dict:
    return {"name": name, "description": description, "value_description": value_description, "synonyms": list(synonyms)}


def k(
    identity: str,
    *columns: str,
    universe: str = "partial",
    unique: object = False,
    total: object = True,
    conforms: object = True,
    description: str = "",
) -> dict:
    return {
        "identity": identity,
        "columns": list(columns),
        "universe": universe,
        "unique": unique,
        "total": total,
        "conforms": conforms,
        "description": description,
    }


def pk(identity: str, *columns: str, description: str = "") -> dict:
    """The dataset is the system of record for this entity."""
    return k(identity, *columns, universe="complete", unique=True, total=True, conforms=True, description=description)


DATASETS: list[dict] = []


def ds(
    layer: dict,
    schema: str,
    name: str,
    display_name: str,
    description: str,
    columns: list[dict],
    keys: list[dict],
    grain: tuple | str,
    role: str,
    synonyms: tuple[str, ...] = (),
    grain_description: str = "",
) -> None:
    DATASETS.append(
        {
            "layer": layer,
            "schema": schema,
            "name": name,
            "display_name": display_name,
            "description": description,
            "columns": columns,
            "keys": keys,
            "grain": grain,
            "role": role,
            "synonyms": list(synonyms),
            "grain_description": grain_description,
        }
    )


IDENTITIES: dict[str, tuple[str, str, tuple[str, ...]]] = {
    # name, description, synonyms
    "zip_code_identity": ("Postal code", "A US postal code with its town and division.", ("ZIP", "zip code")),
    "address_identity": ("Postal address", "A street address shared by customers, companies, exchanges, and branches.", ()),
    "status_type_identity": ("Status type", "A lifecycle status code shared by trades, accounts, customers, brokers, companies, and securities.", ()),
    "tax_rate_identity": ("Tax rate", "A national or local tax rate that applies to customer trading gains.", ()),
    "trade_type_identity": ("Trade type", "A trade type: market or limit, buy or sell, or stop-loss.", ("order type",)),
    "customer_tier_identity": ("Customer tier", "A pricing tier that sets charges and commission rates.", ("pricing tier",)),
    "exchange_identity": ("Exchange", "A listing exchange for securities.", ("listing venue",)),
    "sector_identity": ("Sector", "An industry sector.", ()),
    "industry_identity": ("Industry", "An industry within a sector.", ()),
    "company_identity": ("Company", "A public company that issues securities.", ("issuer",)),
    "security_identity": ("Security", "A listed security, keyed by its trading symbol.", ("instrument", "symbol", "ticker")),
    "news_item_identity": ("News item", "A news article that may mention one or more companies.", ()),
    "customer_identity": ("Customer", "A person who holds one or more brokerage accounts.", ("client", "account holder")),
    "account_identity": ("Brokerage account", "A customer brokerage account that holds cash and positions.", ("account",)),
    "position_identity": ("Position", "The current position of one account in one security.", ("holding summary",)),
    "watch_list_identity": ("Watch list", "A customer's list of securities to follow.", ()),
    "broker_identity": ("Broker", "A registered representative who services accounts and handles trades.", ("registered representative", "RR")),
    "trade_identity": ("Trade", "A customer trade, from submission through settlement.", ("order ticket",)),
    "order_identity": ("Order", "A customer order in the order management system.", ()),
    "execution_identity": ("Execution", "A fill of an order at a venue.", ("fill",)),
    "route_identity": ("Order route", "One routing of an order to an execution venue.", ()),
    "venue_identity": ("Execution venue", "A market center that executes routed orders, keyed by its MIC.", ("market center", "MIC")),
    "corporate_action_identity": ("Corporate action", "A split, dividend, merger, or spin-off that affects a security.", ()),
    "entitlement_identity": ("Corporate action entitlement", "One account's entitlement from one corporate action.", ()),
    "margin_call_identity": ("Margin call", "A demand for funds or securities to meet a margin requirement.", ()),
    "bank_link_identity": ("Bank link", "A verified external bank account linked to a customer.", ()),
    "transfer_identity": ("Funding transfer", "A cash deposit or withdrawal between a brokerage account and a bank.", ("money movement",)),
    "acats_transfer_identity": ("ACATS transfer", "A transfer of account assets between brokerage firms through ACATS.", ()),
    "kyc_review_identity": ("KYC review", "A know-your-customer review of one customer.", ()),
    "aml_alert_identity": ("AML alert", "An anti-money-laundering monitoring alert.", ()),
    "aml_case_identity": ("AML case", "An investigation case that groups AML alerts.", ()),
    "surveillance_alert_identity": ("Trade surveillance alert", "A market-abuse surveillance alert on trading activity.", ()),
    "complaint_identity": ("Customer complaint", "A written customer complaint.", ()),
    "cat_event_identity": ("CAT reportable event", "An order event reported to the Consolidated Audit Trail.", ()),
    "branch_identity": ("Branch", "A branch office of the firm.", ("office",)),
    "employee_identity": ("Employee", "A firm employee, including brokers and their managers.", ("associated person",)),
    "statement_identity": ("Account statement", "A periodic account statement.", ()),
    "session_identity": ("Digital session", "A customer login session on web or mobile.", ()),
    "interaction_identity": ("Service interaction", "A customer service contact.", ()),
    "date_key_identity": ("Calendar date key", "A warehouse surrogate key for one calendar day.", ("SK_DateID",)),
    "time_key_identity": ("Time-of-day key", "A warehouse surrogate key for one second of the day.", ("SK_TimeID",)),
    "calendar_month_identity": ("Calendar month", "A calendar month in YYYYMM form.", ()),
    "customer_version_identity": ("Customer version", "A warehouse surrogate key for one historical version of a customer.", ("SK_CustomerID",)),
    "account_version_identity": ("Account version", "A warehouse surrogate key for one historical version of an account.", ("SK_AccountID",)),
    "broker_version_identity": ("Broker version", "A warehouse surrogate key for one version of a broker.", ("SK_BrokerID",)),
    "company_version_identity": ("Company version", "A warehouse surrogate key for one historical version of a company.", ("SK_CompanyID",)),
    "security_version_identity": ("Security version", "A warehouse surrogate key for one historical version of a security.", ("SK_SecurityID",)),
    "prospect_identity": ("Marketing prospect", "A person in a purchased marketing list, keyed by the agency identifier.", ("lead",)),
    "customer_segment_identity": ("Customer segment", "A marketing and service segment for customers.", ()),
    "account_day_identity": ("Account day", "One account version on one business day.", ("account snapshot",)),
}

SCD2_COLUMNS = [
    c("is_current", "Whether this row is the current version.", "TRUE for the one current version; FALSE for history."),
    c("batch_id", "Warehouse load batch that created this version.", "1 is the historical load; 2 and later are incremental loads."),
    c("effective_date", "First date this version is valid."),
    c("end_date", "Last date this version is valid.", "9999-12-31 for the current version."),
]

# ---------------------------------------------------------------------------------------------
# Operational layer: reference data (TPC-E fixed tables)
# ---------------------------------------------------------------------------------------------

ds(OLTP, "reference", "zip_code", "Zip code", "US postal codes with town and state or division.",
   [c("zc_code", "Postal code.", synonyms=("zip",)), c("zc_town", "Town name."), c("zc_div", "State or division abbreviation.")],
   [pk("zip_code_identity", "zc_code")], ("zip_code_identity", ["zc_code"]), "reference")

ds(OLTP, "reference", "address", "Address", "Street addresses for customers, companies, exchanges, and branches.",
   [c("ad_id", "Address identifier."), c("ad_line1", "First address line."), c("ad_line2", "Second address line."),
    c("ad_zc_code", "Postal code of the address."), c("ad_ctry", "Country name.")],
   [pk("address_identity", "ad_id"), k("zip_code_identity", "ad_zc_code")], ("address_identity", ["ad_id"]), "reference")

ds(OLTP, "reference", "status_type", "Status type", "Lifecycle status codes used across trading and master data.",
   [c("st_id", "Status code.", "ACTV active, CMPT completed, CNCL canceled, PNDG pending, SBMT submitted, INAC inactive."),
    c("st_name", "Status name.")],
   [pk("status_type_identity", "st_id")], ("status_type_identity", ["st_id"]), "reference")

ds(OLTP, "reference", "taxrate", "Tax rate", "National and local tax rates applied to customer trading gains.",
   [c("tx_id", "Tax rate code.", "Codes starting with US are national US rates; others are state or country rates."),
    c("tx_name", "Tax rate name."), c("tx_rate", "Tax rate as a fraction.", "0.00000 to 1.00000")],
   [pk("tax_rate_identity", "tx_id")], ("tax_rate_identity", ["tx_id"]), "reference")

ds(OLTP, "reference", "trade_type", "Trade type", "Trade types with their side and market-versus-limit flags.",
   [c("tt_id", "Trade type code.", "TMB market buy, TMS market sell, TLB limit buy, TLS limit sell, TSL stop loss."),
    c("tt_name", "Trade type name."), c("tt_is_sell", "Whether the type sells.", "1 sell, 0 buy"),
    c("tt_is_mrkt", "Whether the type executes at market.", "1 market, 0 limit or stop")],
   [pk("trade_type_identity", "tt_id")], ("trade_type_identity", ["tt_id"]), "reference")

ds(OLTP, "reference", "customer_tier", "Customer tier", "Pricing tiers that set charges and commission schedules.",
   [c("tier", "Tier number.", "1 highest-value customers with lowest fees, 2 standard, 3 basic."),
    c("tier_name", "Tier name."), c("min_household_assets", "Minimum household assets for the tier.", "USD")],
   [pk("customer_tier_identity", "tier")], ("customer_tier_identity", ["tier"]), "reference")

ds(OLTP, "reference", "charge", "Trade charge", "Flat charge per trade by trade type and customer tier.",
   [c("ch_tt_id", "Trade type the charge applies to."), c("ch_c_tier", "Customer tier the charge applies to."),
    c("ch_chrg", "Flat charge per trade.", "USD")],
   [k("trade_type_identity", "ch_tt_id", universe="complete"), k("customer_tier_identity", "ch_c_tier", universe="complete")],
   (None, ["ch_c_tier", "ch_tt_id"]), "reference",
   grain_description="One row per trade type and customer tier.")

ds(OLTP, "reference", "commission_rate", "Commission rate", "Commission rate schedule by tier, trade type, exchange, and quantity band.",
   [c("cr_c_tier", "Customer tier."), c("cr_tt_id", "Trade type."), c("cr_ex_id", "Exchange of the traded security."),
    c("cr_from_qty", "Lowest quantity of the band.", "shares"), c("cr_to_qty", "Highest quantity of the band.", "shares"),
    c("cr_rate", "Commission as a percentage of trade value.", "percent, 0.00 to 100.00")],
   [k("customer_tier_identity", "cr_c_tier", universe="complete"), k("trade_type_identity", "cr_tt_id", universe="complete"), k("exchange_identity", "cr_ex_id", universe="complete")],
   (None, ["cr_c_tier", "cr_ex_id", "cr_from_qty", "cr_tt_id"]), "reference",
   grain_description="One row per tier, trade type, exchange, and starting quantity.")

ds(OLTP, "reference", "exchange", "Exchange", "Listing exchanges with trading hours.",
   [c("ex_id", "Exchange code.", "NYSE, NASDAQ, AMEX, PCX"), c("ex_name", "Exchange name."),
    c("ex_num_symb", "Number of securities listed."), c("ex_open", "Opening time.", "minutes after midnight, exchange local time"),
    c("ex_close", "Closing time.", "minutes after midnight, exchange local time"), c("ex_desc", "Exchange description."),
    c("ex_ad_id", "Exchange address.")],
   [pk("exchange_identity", "ex_id"), k("address_identity", "ex_ad_id", unique=True)], ("exchange_identity", ["ex_id"]), "reference")

ds(OLTP, "reference", "sector", "Sector", "Industry sectors.",
   [c("sc_id", "Sector code."), c("sc_name", "Sector name.")],
   [pk("sector_identity", "sc_id")], ("sector_identity", ["sc_id"]), "reference")

ds(OLTP, "reference", "industry", "Industry", "Industries within sectors.",
   [c("in_id", "Industry code."), c("in_name", "Industry name."), c("in_sc_id", "Sector of the industry.")],
   [pk("industry_identity", "in_id"), k("sector_identity", "in_sc_id", universe="complete")], ("industry_identity", ["in_id"]), "reference")

# ---------------------------------------------------------------------------------------------
# Operational layer: market data (TPC-E market tables)
# ---------------------------------------------------------------------------------------------

ds(OLTP, "market", "company", "Company", "Public companies that issue listed securities.",
   [c("co_id", "Company identifier."), c("co_st_id", "Company status.", "ACTV or INAC"), c("co_name", "Company name."),
    c("co_in_id", "Industry of the company."), c("co_sp_rate", "S&P credit rating.", "AAA through D, with + and - modifiers"),
    c("co_ceo", "Chief executive officer name."), c("co_ad_id", "Headquarters address."), c("co_desc", "Company description."),
    c("co_open_date", "Date the company was founded.")],
   [pk("company_identity", "co_id"), k("status_type_identity", "co_st_id"), k("industry_identity", "co_in_id"),
    k("address_identity", "co_ad_id", unique=True)],
   ("company_identity", ["co_id"]), "master", synonyms=("issuer",))

ds(OLTP, "market", "company_competitor", "Company competitor", "Competitor pairs within an industry.",
   [c("cp_co_id", "The company."), c("cp_comp_co_id", "A competitor of the company."), c("cp_in_id", "Industry in which they compete.")],
   [k("company_identity", "cp_co_id", description="The company whose competitor is listed."),
    k("company_identity", "cp_comp_co_id", description="The competing company."),
    k("industry_identity", "cp_in_id")],
   (None, ["cp_co_id", "cp_comp_co_id", "cp_in_id"]), "bridge",
   grain_description="One row per company, competitor, and industry.")

ds(OLTP, "market", "security", "Security", "Listed securities with issue, exchange, and 52-week statistics.",
   [c("s_symb", "Trading symbol.", synonyms=("ticker",)), c("s_issue", "Issue type.", "COMMON, PREF_A, PREF_B, PREF_C, PREF_D"),
    c("s_st_id", "Security status.", "ACTV or INAC"), c("s_name", "Security name."), c("s_ex_id", "Listing exchange."),
    c("s_co_id", "Issuing company."), c("s_num_out", "Shares outstanding."), c("s_start_date", "First trade date."),
    c("s_exch_date", "First trade date on the current exchange."), c("s_pe", "Price-to-earnings ratio."),
    c("s_52wk_high", "52-week high price.", "USD"), c("s_52wk_high_date", "Date of the 52-week high."),
    c("s_52wk_low", "52-week low price.", "USD"), c("s_52wk_low_date", "Date of the 52-week low."),
    c("s_dividend", "Annual dividend per share.", "USD"), c("s_yield", "Dividend yield.", "percent")],
   [pk("security_identity", "s_symb"), k("status_type_identity", "s_st_id"), k("exchange_identity", "s_ex_id"),
    k("company_identity", "s_co_id", universe="complete")],
   ("security_identity", ["s_symb"]), "master", synonyms=("instrument", "stock"))

ds(OLTP, "market", "daily_market", "Daily market", "Daily price and volume for each security.",
   [c("dm_date", "Trading date."), c("dm_s_symb", "Security symbol."), c("dm_close", "Closing price.", "USD"),
    c("dm_high", "Day high price.", "USD"), c("dm_low", "Day low price.", "USD"), c("dm_vol", "Shares traded.")],
   [k("security_identity", "dm_s_symb", universe="complete")], (None, ["dm_date", "dm_s_symb"]), "fact",
   synonyms=("end of day prices", "EOD"), grain_description="One row per security per trading day.")

ds(OLTP, "market", "last_trade", "Last trade", "Most recent trade price and volume for each security.",
   [c("lt_s_symb", "Security symbol."), c("lt_dts", "Timestamp of the last trade."), c("lt_price", "Last trade price.", "USD"),
    c("lt_open_price", "Opening price for the day.", "USD"), c("lt_vol", "Shares traded today.")],
   [k("security_identity", "lt_s_symb", universe="complete", unique=True, description="The security whose last trade this is.")],
   ("security_identity", ["lt_s_symb"]), "fact", synonyms=("quote", "ticker tape"))

ds(OLTP, "market", "financial", "Company financial", "Quarterly financial statements for each company.",
   [c("fi_co_id", "Company."), c("fi_year", "Fiscal year."), c("fi_qtr", "Fiscal quarter.", "1 to 4"),
    c("fi_qtr_start_date", "First day of the quarter."), c("fi_revenue", "Revenue.", "USD"), c("fi_net_earn", "Net earnings.", "USD"),
    c("fi_basic_eps", "Basic earnings per share.", "USD"), c("fi_dilut_eps", "Diluted earnings per share.", "USD"),
    c("fi_margin", "Profit margin.", "fraction"), c("fi_inventory", "Inventory value.", "USD"), c("fi_assets", "Total assets.", "USD"),
    c("fi_liability", "Total liabilities.", "USD"), c("fi_out_basic", "Basic shares outstanding."),
    c("fi_out_dilut", "Diluted shares outstanding.")],
   [k("company_identity", "fi_co_id", universe="complete")], (None, ["fi_co_id", "fi_qtr", "fi_year"]), "fact",
   synonyms=("fundamentals", "quarterly results"), grain_description="One row per company per fiscal quarter.")

ds(OLTP, "market", "news_item", "News item", "News articles about companies.",
   [c("ni_id", "News item identifier."), c("ni_headline", "Headline."), c("ni_summary", "Summary."),
    c("ni_item", "Article body."), c("ni_dts", "Publication timestamp."), c("ni_source", "News source."),
    c("ni_author", "Author.")],
   [pk("news_item_identity", "ni_id")], ("news_item_identity", ["ni_id"]), "master")

ds(OLTP, "market", "news_xref", "News cross-reference", "Companies mentioned by each news item.",
   [c("nx_ni_id", "News item."), c("nx_co_id", "Company mentioned.")],
   [k("news_item_identity", "nx_ni_id", universe="complete"), k("company_identity", "nx_co_id")],
   (None, ["nx_co_id", "nx_ni_id"]), "bridge", grain_description="One row per news item and company.")

# ---------------------------------------------------------------------------------------------
# Operational layer: customers, accounts, and brokers (TPC-E customer and broker tables)
# ---------------------------------------------------------------------------------------------

ds(OLTP, "customer", "customer", "Customer", "Brokerage customers with identity, tier, and contact details.",
   [c("c_id", "Customer identifier."), c("c_tax_id", "Customer tax identifier.", synonyms=("SSN", "TIN")),
    c("c_st_id", "Customer status.", "ACTV or INAC"), c("c_l_name", "Last name."), c("c_f_name", "First name."),
    c("c_m_name", "Middle initial."), c("c_gndr", "Gender.", "M, F, or null when not given"), c("c_tier", "Pricing tier."),
    c("c_dob", "Date of birth."), c("c_ad_id", "Home address."), c("c_ctry_1", "Phone country code."),
    c("c_area_1", "Phone area code."), c("c_local_1", "Local phone number."), c("c_email_1", "Primary email address."),
    c("c_email_2", "Alternate email address.")],
   [pk("customer_identity", "c_id"), k("status_type_identity", "c_st_id"), k("customer_tier_identity", "c_tier", universe="complete"),
    k("address_identity", "c_ad_id", unique=True)],
   ("customer_identity", ["c_id"]), "master", synonyms=("client",))

ds(OLTP, "customer", "customer_taxrate", "Customer tax rate", "Tax rates that apply to each customer.",
   [c("cx_tx_id", "Tax rate."), c("cx_c_id", "Customer.")],
   [k("tax_rate_identity", "cx_tx_id"), k("customer_identity", "cx_c_id", universe="complete")],
   (None, ["cx_c_id", "cx_tx_id"]), "bridge",
   grain_description="One row per customer and tax rate; each customer has one national and one local rate.")

ds(OLTP, "customer", "customer_account", "Customer account", "Brokerage accounts with owner, broker, tax status, and cash balance.",
   [c("ca_id", "Account identifier."), c("ca_b_id", "Servicing broker."), c("ca_c_id", "Account owner."),
    c("ca_name", "Account nickname."), c("ca_tax_st", "Tax status.", "0 non-taxable, 1 taxable at trade, 2 taxable at year end"),
    c("ca_bal", "Cash balance.", "USD")],
   [pk("account_identity", "ca_id"), k("broker_identity", "ca_b_id", universe="complete"), k("customer_identity", "ca_c_id", universe="complete")],
   ("account_identity", ["ca_id"]), "master", synonyms=("brokerage account",))

ds(OLTP, "customer", "account_permission", "Account permission", "People permitted to act on an account, including the owner.",
   [c("ap_ca_id", "Account."), c("ap_acl", "Access control list.", "4-character permission mask"),
    c("ap_tax_id", "Tax identifier of the permitted person."), c("ap_l_name", "Last name."), c("ap_f_name", "First name.")],
   [k("account_identity", "ap_ca_id", universe="complete")], (None, ["ap_ca_id", "ap_tax_id"]), "bridge",
   synonyms=("authorized trader", "power of attorney"), grain_description="One row per account and permitted person.")

ds(OLTP, "customer", "watch_list", "Watch list", "Customer watch lists.",
   [c("wl_id", "Watch list identifier."), c("wl_c_id", "Owning customer.")],
   [pk("watch_list_identity", "wl_id"), k("customer_identity", "wl_c_id", universe="complete", unique=True)],
   ("watch_list_identity", ["wl_id"]), "master")

ds(OLTP, "customer", "watch_item", "Watch item", "Securities on each watch list.",
   [c("wi_wl_id", "Watch list."), c("wi_s_symb", "Watched security.")],
   [k("watch_list_identity", "wi_wl_id"), k("security_identity", "wi_s_symb")],
   (None, ["wi_s_symb", "wi_wl_id"]), "bridge", grain_description="One row per watch list and security.")

ds(OLTP, "customer", "broker", "Broker", "Brokers with their running trade and commission totals.",
   [c("b_id", "Broker identifier."), c("b_st_id", "Broker status.", "ACTV or INAC"), c("b_name", "Broker name."),
    c("b_num_trades", "Number of trades completed."), c("b_comm_total", "Commission earned to date.", "USD"),
    c("b_employee_id", "Employee record of the broker."), c("b_branch_id", "Home branch of the broker.")],
   [pk("broker_identity", "b_id"), k("status_type_identity", "b_st_id"),
    k("employee_identity", "b_employee_id", unique=True), k("branch_identity", "b_branch_id")],
   ("broker_identity", ["b_id"]), "master", synonyms=("registered representative", "financial advisor"))

# ---------------------------------------------------------------------------------------------
# Operational layer: trading (TPC-E trade tables)
# ---------------------------------------------------------------------------------------------

ds(OLTP, "trading", "trade", "Trade", "Customer trades with type, price, fees, and status.",
   [c("t_id", "Trade identifier."), c("t_dts", "Timestamp of the latest status change."), c("t_st_id", "Trade status.",
     "SBMT submitted, PNDG pending limit, CMPT completed, CNCL canceled"),
    c("t_tt_id", "Trade type."), c("t_is_cash", "Whether the trade is a cash trade.", "1 cash, 0 margin"),
    c("t_s_symb", "Traded security."), c("t_qty", "Shares traded."), c("t_bid_price", "Requested price.", "USD per share"),
    c("t_ca_id", "Account that placed the trade."), c("t_exec_name", "Name of the person who executed the trade."),
    c("t_trade_price", "Execution price.", "USD per share; null until completed"), c("t_chrg", "Flat charge.", "USD"),
    c("t_comm", "Commission.", "USD"), c("t_tax", "Tax withheld.", "USD"),
    c("t_lifo", "Whether holdings are relieved last-in first-out.", "1 LIFO, 0 FIFO")],
   [pk("trade_identity", "t_id"), k("status_type_identity", "t_st_id"), k("trade_type_identity", "t_tt_id"),
    k("security_identity", "t_s_symb"), k("account_identity", "t_ca_id")],
   ("trade_identity", ["t_id"]), "fact", synonyms=("order", "ticket"))

ds(OLTP, "trading", "trade_history", "Trade history", "Status history of each trade.",
   [c("th_t_id", "Trade."), c("th_dts", "Timestamp of the status change."), c("th_st_id", "Status entered.")],
   [k("trade_identity", "th_t_id", universe="complete"), k("status_type_identity", "th_st_id")],
   (None, ["th_st_id", "th_t_id"]), "fact", grain_description="One row per trade and status entered.")

ds(OLTP, "trading", "trade_request", "Trade request", "Pending limit and stop orders waiting for a trigger price.",
   [c("tr_t_id", "Pending trade."), c("tr_tt_id", "Trade type."), c("tr_s_symb", "Security."), c("tr_qty", "Shares requested."),
    c("tr_bid_price", "Trigger price.", "USD per share"), c("tr_b_id", "Broker handling the request.")],
   [k("trade_identity", "tr_t_id", unique=True, description="The pending trade waiting for its trigger."),
    k("trade_type_identity", "tr_tt_id"), k("security_identity", "tr_s_symb"), k("broker_identity", "tr_b_id")],
   ("trade_identity", ["tr_t_id"]), "fact", synonyms=("pending order", "limit book"))

ds(OLTP, "trading", "settlement", "Settlement", "Cash settlement of completed trades.",
   [c("se_t_id", "Settled trade."), c("se_cash_type", "Settlement type.", "Cash Account or Margin"),
    c("se_cash_due_date", "Settlement due date.", "trade date plus one business day under T+1"),
    c("se_amt", "Settlement amount.", "USD; positive is a credit to the account")],
   [k("trade_identity", "se_t_id", unique=True)], ("trade_identity", ["se_t_id"]), "fact")

ds(OLTP, "trading", "cash_transaction", "Cash transaction", "Cash ledger entries for completed cash trades.",
   [c("ct_t_id", "Trade that created the entry."), c("ct_dts", "Entry timestamp."), c("ct_amt", "Amount.", "USD"),
    c("ct_name", "Entry description.")],
   [k("trade_identity", "ct_t_id", unique=True)], ("trade_identity", ["ct_t_id"]), "fact", synonyms=("cash ledger",))

ds(OLTP, "trading", "holding", "Holding", "Open tax lots, one per opening trade.",
   [c("h_t_id", "Trade that opened the lot."), c("h_ca_id", "Account."), c("h_s_symb", "Security."),
    c("h_dts", "Lot open timestamp."), c("h_price", "Lot cost per share.", "USD"),
    c("h_qty", "Remaining shares.", "negative for a short lot")],
   [k("trade_identity", "h_t_id", unique=True, description="The trade that opened the lot."),
    k("account_identity", "h_ca_id"), k("security_identity", "h_s_symb"),
    k("position_identity", "h_ca_id", "h_s_symb", universe="complete", description="The account position the lot belongs to.")],
   ("trade_identity", ["h_t_id"]), "fact", synonyms=("tax lot", "lot"))

ds(OLTP, "trading", "holding_history", "Holding history", "Changes to tax lots caused by later trades.",
   [c("hh_h_t_id", "Trade that opened the lot."), c("hh_t_id", "Trade that changed the lot."),
    c("hh_before_qty", "Lot quantity before the change."), c("hh_after_qty", "Lot quantity after the change.")],
   [k("trade_identity", "hh_h_t_id", description="The trade that opened the lot."),
    k("trade_identity", "hh_t_id", description="The trade that changed the lot.")],
   (None, ["hh_h_t_id", "hh_t_id"]), "fact", grain_description="One row per lot and the trade that changed it.")

ds(OLTP, "trading", "holding_summary", "Holding summary", "Net position per account and security.",
   [c("hs_ca_id", "Account."), c("hs_s_symb", "Security."), c("hs_qty", "Net shares held.")],
   [pk("position_identity", "hs_ca_id", "hs_s_symb", description="The account position."),
    k("account_identity", "hs_ca_id"), k("security_identity", "hs_s_symb")],
   ("position_identity", ["hs_ca_id", "hs_s_symb"]), "fact", synonyms=("position",))

# ---------------------------------------------------------------------------------------------
# Operational layer: order management and routing (extension beyond TPC-E)
# ---------------------------------------------------------------------------------------------

ds(OLTP, "oms", "customer_order", "Customer order", "Customer orders as received by the order management system.",
   [c("ord_id", "Order identifier."), c("ord_ca_id", "Account that placed the order."), c("ord_s_symb", "Security."),
    c("ord_side", "Order side.", "B buy, S sell, SS sell short, BC buy to cover"),
    c("ord_type", "Order type.", "MKT market, LMT limit, STP stop, STL stop limit"),
    c("ord_tif", "Time in force.", "DAY, GTC good till canceled, IOC immediate or cancel, FOK fill or kill"),
    c("ord_qty", "Shares ordered."), c("ord_limit_price", "Limit price.", "USD; null for market and stop orders"),
    c("ord_stop_price", "Stop trigger price.", "USD; null unless a stop type"),
    c("ord_status", "Order status.", "NEW, PARTIAL, FILLED, CANCELED, REJECTED, EXPIRED"),
    c("ord_channel", "Entry channel.", "WEB, MOBILE, API, BROKER, IVR"), c("ord_created_ts", "Order receipt timestamp."),
    c("ord_entered_by_b_id", "Broker who entered the order.", "null for self-directed orders"),
    c("ord_t_id", "Trade booked from the order.", "null until the first fill is booked")],
   [pk("order_identity", "ord_id"), k("account_identity", "ord_ca_id"), k("security_identity", "ord_s_symb"),
    k("broker_identity", "ord_entered_by_b_id", total=False, description="The broker who entered the order for the customer."),
    k("trade_identity", "ord_t_id", universe="complete", unique=True, total=False, description="The trade booked from the order.")],
   ("order_identity", ["ord_id"]), "fact", synonyms=("parent order",))

ds(OLTP, "oms", "execution_venue", "Execution venue", "Market centers that execute routed orders.",
   [c("venue_mic", "ISO 10383 market identifier code.", synonyms=("MIC",)), c("venue_name", "Venue name."),
    c("venue_type", "Venue type.", "EXCHANGE, ATS, WHOLESALER, INTERNAL"),
    c("listing_ex_id", "Listing exchange operated by the venue.", "null for venues that do not list securities")],
   [pk("venue_identity", "venue_mic"), k("exchange_identity", "listing_ex_id", unique=True, total=False)],
   ("venue_identity", ["venue_mic"]), "reference", synonyms=("market center",))

ds(OLTP, "oms", "order_route", "Order route", "Each routing of an order, or a slice of it, to a venue.",
   [c("route_id", "Route identifier."), c("route_ord_id", "Routed order."), c("route_venue_mic", "Destination venue."),
    c("route_qty", "Shares routed."), c("route_ts", "Routing timestamp."),
    c("route_status", "Route outcome.", "ACK, FILLED, PARTIAL, CANCELED, REJECTED"),
    c("route_payment_per_share", "Payment for order flow received.", "USD per share; 0 when none")],
   [pk("route_identity", "route_id"), k("order_identity", "route_ord_id"), k("venue_identity", "route_venue_mic")],
   ("route_identity", ["route_id"]), "fact", synonyms=("child order",))

ds(OLTP, "oms", "order_execution", "Order execution", "Fills reported by venues against routed orders.",
   [c("exec_id", "Execution identifier."), c("exec_route_id", "Route that was filled."), c("exec_ord_id", "Order that was filled."),
    c("exec_venue_mic", "Executing venue."), c("exec_qty", "Shares filled."), c("exec_price", "Fill price.", "USD per share"),
    c("exec_ts", "Fill timestamp."), c("exec_liquidity", "Liquidity flag.", "A added, R removed, X routed out"),
    c("nbbo_bid_at_receipt", "National best bid when the order was received.", "USD"),
    c("nbbo_ask_at_receipt", "National best offer when the order was received.", "USD")],
   [pk("execution_identity", "exec_id"), k("route_identity", "exec_route_id"), k("order_identity", "exec_ord_id"),
    k("venue_identity", "exec_venue_mic")],
   ("execution_identity", ["exec_id"]), "fact", synonyms=("fill",))

ds(OLTP, "oms", "order_event", "Order event", "Lifecycle audit events of each order.",
   [c("ord_id", "Order."), c("event_seq", "Event sequence within the order."),
    c("event_type", "Event type.", "NEW, ROUTE, FILL, MODIFY, CANCEL_REQUEST, CANCEL, REJECT, EXPIRE"),
    c("event_ts", "Event timestamp."), c("actor", "Who caused the event.", "CUSTOMER, BROKER, SYSTEM, VENUE")],
   [k("order_identity", "ord_id", universe="complete")], (None, ["event_seq", "ord_id"]), "fact",
   grain_description="One row per order event.")

ds(OLTP, "oms", "market_calendar", "Market calendar", "Trading days and early closes per exchange.",
   [c("ex_id", "Exchange."), c("cal_date", "Calendar date."), c("is_trading_day", "Whether the exchange is open."),
    c("close_minute", "Closing time.", "minutes after midnight; earlier on half days")],
   [k("exchange_identity", "ex_id")], (None, ["cal_date", "ex_id"]), "reference",
   grain_description="One row per exchange per calendar date.")

# ---------------------------------------------------------------------------------------------
# Operational layer: security reference extensions and corporate actions
# ---------------------------------------------------------------------------------------------

ds(OLTP, "market", "security_identifier", "Security identifier", "External identifiers of each security over time.",
   [c("s_symb", "Security symbol."), c("id_scheme", "Identifier scheme.", "CUSIP, ISIN, FIGI, SEDOL"),
    c("id_value", "Identifier value."), c("valid_from", "First date the identifier applies."),
    c("valid_to", "Last date the identifier applies.", "null while current")],
   [k("security_identity", "s_symb", universe="complete")], (None, ["id_scheme", "id_value"]), "reference",
   synonyms=("CUSIP", "ISIN", "xref"), grain_description="One row per identifier scheme and value.")

ds(OLTP, "market", "corporate_action", "Corporate action", "Splits, dividends, mergers, and spin-offs.",
   [c("action_id", "Corporate action identifier."), c("s_symb", "Affected security."),
    c("action_type", "Action type.", "CASH_DIV, STOCK_DIV, SPLIT, REVERSE_SPLIT, MERGER, SPINOFF"),
    c("announce_date", "Announcement date."), c("ex_date", "Ex-date."), c("record_date", "Record date."),
    c("pay_date", "Payable date."), c("cash_rate", "Cash per share.", "USD; null for non-cash actions"),
    c("ratio_new", "New shares in the ratio."), c("ratio_old", "Old shares in the ratio."),
    c("successor_s_symb", "Security received.", "null unless a merger or spin-off")],
   [pk("corporate_action_identity", "action_id"),
    k("security_identity", "s_symb", description="The security the action applies to."),
    k("security_identity", "successor_s_symb", total=False, description="The security delivered by a merger or spin-off.")],
   ("corporate_action_identity", ["action_id"]), "fact", synonyms=("corporate event",))

ds(OLTP, "market", "ca_entitlement", "Corporate action entitlement", "Per-account entitlements computed on the record date.",
   [c("entitlement_id", "Entitlement identifier."), c("action_id", "Corporate action."), c("ca_id", "Entitled account."),
    c("s_symb", "Security held on the record date."), c("eligible_qty", "Shares held on the record date."),
    c("gross_cash", "Gross cash entitled.", "USD"), c("withholding", "Tax withheld.", "USD"),
    c("new_shares", "Shares delivered."), c("paid_ts", "Timestamp the entitlement was paid.", "null until paid")],
   [pk("entitlement_identity", "entitlement_id"), k("corporate_action_identity", "action_id"),
    k("account_identity", "ca_id"), k("security_identity", "s_symb"),
    k("position_identity", "ca_id", "s_symb", conforms="unknown",
      description="The position held on the record date; it may since have been closed.")],
   ("entitlement_identity", ["entitlement_id"]), "fact", synonyms=("dividend payment",))

# ---------------------------------------------------------------------------------------------
# Operational layer: margin and risk
# ---------------------------------------------------------------------------------------------

ds(OLTP, "risk", "margin_account", "Margin account", "Margin agreement terms for accounts approved for margin.",
   [c("ca_id", "Margin-approved account."), c("agreement_date", "Margin agreement signing date."),
    c("house_maint_pct", "House maintenance requirement.", "percent of long market value, at least 25"),
    c("options_level", "Options approval level.", "0 none to 4 uncovered"),
    c("pattern_day_trader", "Whether the account is flagged as a pattern day trader.")],
   [k("account_identity", "ca_id", unique=True)], ("account_identity", ["ca_id"]), "master")

ds(OLTP, "risk", "margin_call", "Margin call", "Margin calls issued to accounts.",
   [c("call_id", "Margin call identifier."), c("ca_id", "Account called."),
    c("call_type", "Call type.", "REGT Regulation T, MAINT maintenance, HOUSE house, DAY_TRADE day trading"),
    c("issued_date", "Issue date."), c("due_date", "Due date."), c("call_amount", "Amount due.", "USD"),
    c("status", "Call status.", "OPEN, MET, LIQUIDATED, EXTENDED"), c("met_date", "Date the call was met.")],
   [pk("margin_call_identity", "call_id"), k("account_identity", "ca_id")],
   ("margin_call_identity", ["call_id"]), "fact")

ds(OLTP, "risk", "account_risk_daily", "Account risk daily", "End-of-day margin and risk measures per margin account.",
   [c("ca_id", "Account."), c("as_of_date", "Business date."), c("equity", "Account equity.", "USD"),
    c("debit_balance", "Margin debit balance.", "USD"), c("sma", "Special memorandum account balance.", "USD"),
    c("maint_excess", "Equity above the maintenance requirement.", "USD; negative means a call"),
    c("var_1d_99", "One-day 99 percent value at risk.", "USD"), c("top_s_symb", "Largest position by market value.")],
   [k("account_identity", "ca_id"), k("security_identity", "top_s_symb", total=False)],
   (None, ["as_of_date", "ca_id"]), "fact", grain_description="One row per margin account per business date.")

# ---------------------------------------------------------------------------------------------
# Operational layer: money movement
# ---------------------------------------------------------------------------------------------

ds(OLTP, "cashier", "bank_link", "Bank link", "External bank accounts linked by customers.",
   [c("bank_link_id", "Bank link identifier."), c("c_id", "Customer."), c("routing_number", "ABA routing number."),
    c("account_last4", "Last four digits of the bank account."), c("bank_account_type", "Bank account type.", "CHECKING or SAVINGS"),
    c("verified_ts", "Verification timestamp.", "null until verified"), c("link_status", "Link status.", "PENDING, ACTIVE, REMOVED")],
   [pk("bank_link_identity", "bank_link_id"), k("customer_identity", "c_id")],
   ("bank_link_identity", ["bank_link_id"]), "master")

ds(OLTP, "cashier", "funding_transfer", "Funding transfer", "Deposits and withdrawals between accounts and banks.",
   [c("transfer_id", "Transfer identifier."), c("ca_id", "Brokerage account."), c("bank_link_id", "Bank link used.",
     "null for checks and incoming wires"), c("direction", "Direction.", "IN deposit, OUT withdrawal"),
    c("method", "Method.", "ACH, WIRE, CHECK, JOURNAL"), c("amount", "Amount.", "USD"),
    c("initiated_ts", "Initiation timestamp."), c("settled_ts", "Settlement timestamp.", "null while pending"),
    c("status", "Transfer status.", "PENDING, SETTLED, RETURNED, CANCELED")],
   [pk("transfer_identity", "transfer_id"), k("account_identity", "ca_id"),
    k("bank_link_identity", "bank_link_id", total=False)],
   ("transfer_identity", ["transfer_id"]), "fact", synonyms=("deposit", "withdrawal", "money movement"))

ds(OLTP, "cashier", "acats_transfer", "ACATS transfer", "Full and partial account transfers with other firms.",
   [c("acats_id", "ACATS control number."), c("ca_id", "Account at this firm."),
    c("direction", "Direction.", "IN transfer to this firm, OUT transfer away"),
    c("contra_dtc_number", "DTC participant number of the other firm."), c("transfer_type", "Transfer type.", "FULL or PARTIAL"),
    c("requested_date", "Request date."), c("completed_date", "Completion date.", "null while open"),
    c("status", "Status.", "REQUEST, REVIEW, SETTLE_PREP, SETTLED, REJECTED")],
   [pk("acats_transfer_identity", "acats_id"), k("account_identity", "ca_id")],
   ("acats_transfer_identity", ["acats_id"]), "fact", synonyms=("account transfer",))

ds(OLTP, "cashier", "acats_asset", "ACATS asset", "Securities and cash lines of each ACATS transfer.",
   [c("acats_id", "ACATS transfer."), c("line_no", "Asset line."), c("s_symb", "Security transferred.", "null for cash lines"),
    c("qty", "Shares transferred."), c("cash_amount", "Cash transferred.", "USD")],
   [k("acats_transfer_identity", "acats_id"), k("security_identity", "s_symb", total=False, conforms="unknown",
     description="Securities from other firms may not be listed on a supported exchange.")],
   (None, ["acats_id", "line_no"]), "fact", grain_description="One row per transfer asset line.")

# ---------------------------------------------------------------------------------------------
# Operational layer: compliance
# ---------------------------------------------------------------------------------------------

ds(OLTP, "compliance", "kyc_review", "KYC review", "Know-your-customer and customer due diligence reviews.",
   [c("review_id", "Review identifier."), c("c_id", "Customer reviewed."),
    c("review_type", "Review type.", "ONBOARDING, PERIODIC, EVENT_DRIVEN"),
    c("risk_rating", "Assigned risk rating.", "LOW, MEDIUM, HIGH"), c("reviewed_date", "Review date."),
    c("reviewer_employee_id", "Reviewing employee."), c("outcome", "Outcome.", "APPROVED, RESTRICTED, EXITED")],
   [pk("kyc_review_identity", "review_id"), k("customer_identity", "c_id"), k("employee_identity", "reviewer_employee_id")],
   ("kyc_review_identity", ["review_id"]), "fact", synonyms=("CDD", "due diligence"))

ds(OLTP, "compliance", "aml_case", "AML case", "Anti-money-laundering investigation cases.",
   [c("case_id", "Case identifier."), c("opened_date", "Open date."), c("closed_date", "Close date.", "null while open"),
    c("assigned_employee_id", "Investigator."), c("disposition", "Disposition.", "NO_ACTION, SAR_FILED, ACCOUNT_CLOSED"),
    c("sar_filed_date", "Date a suspicious activity report was filed.", "null when none was filed")],
   [pk("aml_case_identity", "case_id"), k("employee_identity", "assigned_employee_id")],
   ("aml_case_identity", ["case_id"]), "fact")

ds(OLTP, "compliance", "aml_alert", "AML alert", "Transaction monitoring alerts.",
   [c("alert_id", "Alert identifier."), c("c_id", "Customer alerted."), c("ca_id", "Account alerted.", "null for customer-level rules"),
    c("rule_code", "Monitoring rule.", "STRUCTURING, RAPID_MOVEMENT, HIGH_RISK_GEO, LOW_PRICED_SECURITIES"),
    c("alert_date", "Alert date."), c("score", "Risk score.", "0 to 100"),
    c("status", "Status.", "OPEN, CLOSED_NO_ACTION, ESCALATED"), c("case_id", "Case the alert was escalated to.", "null unless escalated")],
   [pk("aml_alert_identity", "alert_id"), k("customer_identity", "c_id"), k("account_identity", "ca_id", total=False),
    k("aml_case_identity", "case_id", total=False)],
   ("aml_alert_identity", ["alert_id"]), "fact")

ds(OLTP, "compliance", "surveillance_alert", "Trade surveillance alert", "Market-abuse alerts on customer trading.",
   [c("alert_id", "Alert identifier."), c("ca_id", "Account."), c("s_symb", "Security."),
    c("t_id", "Trade that triggered the alert.", "null for pattern alerts over many trades"),
    c("pattern", "Pattern detected.", "WASH_TRADE, SPOOFING, LAYERING, MARKING_THE_CLOSE, FRONT_RUNNING, INSIDER"),
    c("alert_date", "Alert date."), c("status", "Status.", "OPEN, CLOSED_NO_ACTION, ESCALATED, REPORTED"),
    c("reviewer_employee_id", "Reviewing analyst.")],
   [pk("surveillance_alert_identity", "alert_id"), k("account_identity", "ca_id"), k("security_identity", "s_symb"),
    k("trade_identity", "t_id", total=False), k("employee_identity", "reviewer_employee_id", total=False)],
   ("surveillance_alert_identity", ["alert_id"]), "fact")

ds(OLTP, "compliance", "complaint", "Customer complaint", "Written customer complaints, as reported under FINRA Rule 4530.",
   [c("complaint_id", "Complaint identifier."), c("c_id", "Complaining customer."), c("ca_id", "Account concerned.", "null when not account-specific"),
    c("b_id", "Broker named.", "null when no broker is named"), c("received_date", "Receipt date."),
    c("category", "Problem category.", "UNSUITABLE, UNAUTHORIZED_TRADING, SERVICE, FEES, PLATFORM_OUTAGE, MISREPRESENTATION"),
    c("status", "Status.", "OPEN, RESOLVED, ARBITRATION"), c("resolved_date", "Resolution date.")],
   [pk("complaint_identity", "complaint_id"), k("customer_identity", "c_id"), k("account_identity", "ca_id", total=False),
    k("broker_identity", "b_id", total=False)],
   ("complaint_identity", ["complaint_id"]), "fact")

ds(OLTP, "compliance", "cat_event", "CAT reportable event", "Order events submitted to the Consolidated Audit Trail.",
   [c("cat_event_id", "Firm-assigned event identifier."), c("ord_id", "Order reported."),
    c("cat_event_type", "CAT event type.", "MENO new order, MEOR order route, MEOM modification, MEOC cancel, MEOF fulfillment"),
    c("event_ts", "Event timestamp."), c("submitted_date", "Submission date."),
    c("cat_status", "Feedback status.", "ACCEPTED, REJECTED, REPAIRED"), c("error_code", "CAT error code.", "null when accepted")],
   [pk("cat_event_identity", "cat_event_id"), k("order_identity", "ord_id")],
   ("cat_event_identity", ["cat_event_id"]), "fact", synonyms=("CAT submission",))

# ---------------------------------------------------------------------------------------------
# Operational layer: workforce and servicing
# ---------------------------------------------------------------------------------------------

ds(OLTP, "firm", "branch", "Branch", "Branch offices.",
   [c("branch_id", "Branch identifier."), c("branch_name", "Branch name."), c("region", "Sales region.", "EAST, CENTRAL, WEST"),
    c("ad_id", "Branch address."), c("opened_date", "Open date.")],
   [pk("branch_identity", "branch_id"), k("address_identity", "ad_id", unique=True)],
   ("branch_identity", ["branch_id"]), "master", synonyms=("office",))

ds(OLTP, "firm", "employee", "Employee", "Firm employees with their manager and registration number.",
   [c("employee_id", "Employee identifier."), c("branch_id", "Home branch."), c("manager_employee_id", "Direct manager.", "null for the top of the hierarchy"),
    c("job_role", "Role.", "BROKER, BRANCH_MANAGER, COMPLIANCE, OPERATIONS, SERVICE"), c("hire_date", "Hire date."),
    c("term_date", "Termination date.", "null while employed"), c("crd_number", "FINRA CRD number.", "null when unregistered")],
   [pk("employee_identity", "employee_id"), k("branch_identity", "branch_id", universe="complete"),
    k("employee_identity", "manager_employee_id", total=False, description="The employee's direct manager.")],
   ("employee_identity", ["employee_id"]), "master", synonyms=("staff",))

ds(OLTP, "firm", "registration", "Registration", "Securities licenses and state registrations of employees.",
   [c("employee_id", "Registered employee."), c("license", "License.", "S7, S63, S65, S66, S24"),
    c("state", "State of registration."), c("granted_date", "Grant date."), c("lapsed_date", "Lapse date.", "null while active")],
   [k("employee_identity", "employee_id")], (None, ["employee_id", "license", "state"]), "reference",
   grain_description="One row per employee, license, and state.")

ds(OLTP, "service", "statement", "Account statement", "Periodic account statements and delivery status.",
   [c("statement_id", "Statement identifier."), c("ca_id", "Account."), c("period_end_date", "Statement period end."),
    c("delivery_channel", "Delivery channel.", "EDELIVERY or PAPER"), c("delivered_ts", "Delivery timestamp.")],
   [pk("statement_identity", "statement_id"), k("account_identity", "ca_id")],
   ("statement_identity", ["statement_id"]), "fact")

ds(OLTP, "service", "digital_session", "Digital session", "Customer web and mobile sessions.",
   [c("session_id", "Session identifier."), c("c_id", "Customer."), c("device_type", "Device.", "WEB, IOS, ANDROID"),
    c("started_ts", "Login timestamp."), c("ended_ts", "Logout or timeout timestamp."),
    c("orders_placed", "Orders placed in the session.")],
   [pk("session_identity", "session_id"), k("customer_identity", "c_id")],
   ("session_identity", ["session_id"]), "fact", synonyms=("login",))

ds(OLTP, "service", "service_interaction", "Service interaction", "Customer service contacts.",
   [c("interaction_id", "Interaction identifier."), c("c_id", "Customer."), c("employee_id", "Handling employee.", "null for chatbot contacts"),
    c("channel", "Channel.", "PHONE, CHAT, EMAIL, BRANCH"), c("contact_ts", "Contact timestamp."),
    c("reason_code", "Reason.", "PASSWORD, TRANSFER, TRADE_QUESTION, TAX_FORM, COMPLAINT"),
    c("complaint_id", "Complaint logged from the contact.", "null when none was logged")],
   [pk("interaction_identity", "interaction_id"), k("customer_identity", "c_id"),
    k("employee_identity", "employee_id", total=False), k("complaint_identity", "complaint_id", unique=True, total=False)],
   ("interaction_identity", ["interaction_id"]), "fact", synonyms=("call", "contact"))

# ---------------------------------------------------------------------------------------------
# Warehouse layer: TPC-DI dimensions
# ---------------------------------------------------------------------------------------------

def date_key(column: str, description: str = "", total: object = True) -> dict:
    return k("date_key_identity", column, total=total, description=description)


def time_key(column: str, description: str = "", total: object = True) -> dict:
    return k("time_key_identity", column, total=total, description=description)


ds(WAREHOUSE, "dw", "dim_date", "Date dimension", "Calendar and fiscal attributes of each day.",
   [c("sk_date_id", "Date surrogate key.", "YYYYMMDD"), c("date_value", "Calendar date."), c("date_desc", "Long date description."),
    c("calendar_year_id", "Calendar year."), c("calendar_qtr_id", "Calendar quarter.", "YYYYQ"),
    c("calendar_month_id", "Calendar month.", "YYYYMM"), c("calendar_week_id", "Calendar week.", "YYYYWW"),
    c("day_of_week_num", "Day of week.", "1 Monday to 7 Sunday"), c("fiscal_year_id", "Fiscal year."),
    c("fiscal_qtr_id", "Fiscal quarter.", "YYYYQ"), c("holiday_flag", "Whether the day is a market holiday.")],
   [pk("date_key_identity", "sk_date_id"),
    k("calendar_month_identity", "calendar_month_id", universe="complete", description="The calendar month containing the day.")],
   ("date_key_identity", ["sk_date_id"]), "dimension", synonyms=("calendar",))

ds(WAREHOUSE, "dw", "dim_time", "Time dimension", "Attributes of each second of the day.",
   [c("sk_time_id", "Time surrogate key.", "HHMMSS"), c("time_value", "Time of day."), c("hour_id", "Hour.", "0 to 23"),
    c("minute_id", "Minute.", "0 to 59"), c("second_id", "Second.", "0 to 59"),
    c("market_hours_flag", "Whether the second is within regular market hours.", "09:30:00 to 15:59:59 Eastern"),
    c("office_hours_flag", "Whether the second is within office hours.")],
   [pk("time_key_identity", "sk_time_id")], ("time_key_identity", ["sk_time_id"]), "dimension")

ds(WAREHOUSE, "dw", "dim_customer", "Customer dimension", "Customer history with tax rates and purchased marketing attributes.",
   [c("sk_customer_id", "Customer version surrogate key."), c("customer_id", "Operational customer identifier."),
    c("tax_id", "Customer tax identifier."), c("status", "Customer status name.", "Active or Inactive"),
    c("last_name", "Last name."), c("first_name", "First name."), c("gender", "Gender.", "M, F, or U unknown"),
    c("tier", "Pricing tier.", "1, 2, 3, or null"), c("dob", "Date of birth."), c("postal_code", "Postal code."),
    c("city", "City."), c("state_prov", "State or province."), c("country", "Country."), c("email1", "Primary email."),
    c("national_tax_rate_desc", "National tax rate name."), c("national_tax_rate", "National tax rate.", "fraction"),
    c("local_tax_rate_desc", "Local tax rate name."), c("local_tax_rate", "Local tax rate.", "fraction"),
    c("agency_id", "Marketing agency identifier matched from the prospect list.", "null when the customer is not on the list"),
    c("credit_rating", "Credit rating from the prospect list."), c("net_worth", "Estimated net worth.", "USD"),
    c("marketing_nameplate", "Marketing segments derived from prospect attributes.",
      "plus-separated tags such as HighValue+Expenses+Boomer"), *SCD2_COLUMNS],
   [pk("customer_version_identity", "sk_customer_id"),
    k("customer_identity", "customer_id", description="The customer this row is a version of."),
    k("customer_tier_identity", "tier", total=False),
    k("prospect_identity", "agency_id", total=False, conforms="unknown",
      description="Prospect match by agency identifier; the prospect file is replaced on every load.")],
   ("customer_version_identity", ["sk_customer_id"]), "dimension", synonyms=("DimCustomer",),
   grain_description="One row per customer version; Type 2 history.")

ds(WAREHOUSE, "dw", "dim_account", "Account dimension", "Account history with its broker and owner versions.",
   [c("sk_account_id", "Account version surrogate key."), c("account_id", "Operational account identifier."),
    c("sk_broker_id", "Broker version servicing the account."), c("sk_customer_id", "Customer version owning the account."),
    c("status", "Account status name.", "Active or Inactive"), c("account_desc", "Account nickname."),
    c("tax_status", "Tax status.", "0 non-taxable, 1 taxable at trade, 2 taxable at year end"), *SCD2_COLUMNS],
   [pk("account_version_identity", "sk_account_id"),
    k("account_identity", "account_id", description="The account this row is a version of."),
    k("broker_version_identity", "sk_broker_id"), k("customer_version_identity", "sk_customer_id")],
   ("account_version_identity", ["sk_account_id"]), "dimension", synonyms=("DimAccount",),
   grain_description="One row per account version; Type 2 history.")

ds(WAREHOUSE, "dw", "dim_broker", "Broker dimension", "Brokers from the HR feed with branch and manager.",
   [c("sk_broker_id", "Broker surrogate key."), c("broker_id", "Operational broker identifier."),
    c("manager_employee_id", "Manager's employee identifier."), c("first_name", "First name."), c("last_name", "Last name."),
    c("middle_initial", "Middle initial."), c("branch", "Branch name."), c("office", "Office name."), c("phone", "Phone."),
    *SCD2_COLUMNS],
   [pk("broker_version_identity", "sk_broker_id"), k("broker_identity", "broker_id", unique=True),
    k("employee_identity", "manager_employee_id", total=False, description="The broker's manager.")],
   ("broker_version_identity", ["sk_broker_id"]), "dimension", synonyms=("DimBroker",))

ds(WAREHOUSE, "dw", "dim_company", "Company dimension", "Company history from the FINWIRE feed.",
   [c("sk_company_id", "Company version surrogate key."), c("company_id", "Company identifier (CIK)."),
    c("status", "Company status name."), c("name", "Company name."), c("industry", "Industry name."),
    c("sp_rating", "S&P rating."), c("is_low_grade", "Whether the rating is below investment grade.", "TRUE when the rating does not start with A or BBB"),
    c("ceo", "Chief executive officer."), c("postal_code", "Postal code."), c("city", "City."), c("state_prov", "State or province."),
    c("country", "Country."), c("description", "Company description."), c("founding_date", "Founding date."), *SCD2_COLUMNS],
   [pk("company_version_identity", "sk_company_id"),
    k("company_identity", "company_id", description="The company this row is a version of.")],
   ("company_version_identity", ["sk_company_id"]), "dimension", synonyms=("DimCompany",),
   grain_description="One row per company version; Type 2 history.")

ds(WAREHOUSE, "dw", "dim_security", "Security dimension", "Security history from the FINWIRE feed.",
   [c("sk_security_id", "Security version surrogate key."), c("symbol", "Trading symbol."), c("issue", "Issue type."),
    c("status", "Security status name."), c("name", "Security name."), c("exchange_id", "Listing exchange."),
    c("sk_company_id", "Issuing company version."), c("shares_outstanding", "Shares outstanding."),
    c("first_trade", "First trade date."), c("first_trade_on_exchange", "First trade date on the exchange."),
    c("dividend", "Annual dividend.", "USD per share"), *SCD2_COLUMNS],
   [pk("security_version_identity", "sk_security_id"),
    k("security_identity", "symbol", description="The security this row is a version of."),
    k("exchange_identity", "exchange_id"), k("company_version_identity", "sk_company_id")],
   ("security_version_identity", ["sk_security_id"]), "dimension", synonyms=("DimSecurity",),
   grain_description="One row per security version; Type 2 history.")

ds(WAREHOUSE, "dw", "dim_trade", "Trade dimension", "Trades with create and close dates and fees (TPC-DI DimTrade).",
   [c("trade_id", "Operational trade identifier."), c("sk_broker_id", "Broker version.", "null when no broker handled the trade"),
    c("sk_create_date_id", "Date the trade was created."), c("sk_create_time_id", "Time the trade was created."),
    c("sk_close_date_id", "Date the trade completed or was canceled.", "null while open"),
    c("sk_close_time_id", "Time the trade completed or was canceled.", "null while open"),
    c("status", "Trade status name.", "Submitted, Pending, Completed, Canceled"),
    c("type", "Trade type name.", "Market Buy, Market Sell, Limit Buy, Limit Sell, Stop Loss"),
    c("cash_flag", "Whether the trade is a cash trade."), c("sk_security_id", "Security version."),
    c("sk_company_id", "Company version of the issuer."), c("quantity", "Shares."), c("bid_price", "Requested price.", "USD"),
    c("sk_customer_id", "Customer version."), c("sk_account_id", "Account version."), c("executed_by", "Executor name."),
    c("trade_price", "Execution price.", "USD"), c("fee", "Flat fee.", "USD"), c("commission", "Commission.", "USD"),
    c("tax", "Tax.", "USD"), c("batch_id", "Load batch.")],
   [k("trade_identity", "trade_id", unique=True, description="The operational trade."),
    k("broker_version_identity", "sk_broker_id", total=False),
    date_key("sk_create_date_id", "The day the trade was created."), time_key("sk_create_time_id", "The second the trade was created."),
    date_key("sk_close_date_id", "The day the trade closed.", total=False),
    time_key("sk_close_time_id", "The second the trade closed.", total=False),
    k("security_version_identity", "sk_security_id"), k("company_version_identity", "sk_company_id"),
    k("customer_version_identity", "sk_customer_id"), k("account_version_identity", "sk_account_id")],
   ("trade_identity", ["trade_id"]), "fact", synonyms=("DimTrade", "fact trade"))

ds(WAREHOUSE, "dw", "status_type", "Status type", "Warehouse copy of status codes.",
   [c("st_id", "Status code."), c("st_name", "Status name.")],
   [k("status_type_identity", "st_id", unique=True)], ("status_type_identity", ["st_id"]), "reference")

ds(WAREHOUSE, "dw", "trade_type", "Trade type", "Warehouse copy of trade types.",
   [c("tt_id", "Trade type code."), c("tt_name", "Trade type name."), c("tt_is_sell", "Sell flag."), c("tt_is_mrkt", "Market flag.")],
   [k("trade_type_identity", "tt_id", unique=True)], ("trade_type_identity", ["tt_id"]), "reference")

ds(WAREHOUSE, "dw", "tax_rate", "Tax rate", "Warehouse copy of tax rates.",
   [c("tx_id", "Tax rate code."), c("tx_name", "Tax rate name."), c("tx_rate", "Rate.", "fraction")],
   [k("tax_rate_identity", "tx_id", unique=True)], ("tax_rate_identity", ["tx_id"]), "reference")

ds(WAREHOUSE, "dw", "industry", "Industry", "Warehouse copy of industries with their sector.",
   [c("in_id", "Industry code."), c("in_name", "Industry name."), c("in_sc_id", "Sector code.")],
   [k("industry_identity", "in_id", unique=True), k("sector_identity", "in_sc_id", universe="complete")],
   ("industry_identity", ["in_id"]), "reference")

ds(WAREHOUSE, "dw", "prospect", "Prospect", "Purchased marketing prospect list, replaced on every load.",
   [c("agency_id", "Agency identifier of the prospect."), c("sk_record_date_id", "Date the record was first loaded."),
    c("sk_update_date_id", "Date the record last changed."), c("batch_id", "Load batch."),
    c("is_customer", "Whether the prospect matches a current customer.", "matched on name, address, and postal code"),
    c("last_name", "Last name."), c("first_name", "First name."), c("gender", "Gender."), c("postal_code", "Postal code."),
    c("city", "City."), c("state", "State."), c("income", "Annual income.", "USD"), c("number_cars", "Cars owned."),
    c("number_children", "Children."), c("marital_status", "Marital status.", "S, M, D, W, or U"), c("age", "Age."),
    c("credit_rating", "Credit score."), c("own_or_rent_flag", "Home ownership.", "O own, R rent, U unknown"),
    c("net_worth", "Estimated net worth.", "USD"), c("marketing_nameplate", "Derived marketing segments.")],
   [pk("prospect_identity", "agency_id"), date_key("sk_record_date_id", "The day the record was first loaded."),
    date_key("sk_update_date_id", "The day the record last changed.")],
   ("prospect_identity", ["agency_id"]), "dimension", synonyms=("lead", "marketing list"))

ds(WAREHOUSE, "dw", "financial", "Financial", "Quarterly company financials from the FINWIRE feed.",
   [c("sk_company_id", "Company version."), c("fi_year", "Fiscal year."), c("fi_qtr", "Fiscal quarter."),
    c("fi_qtr_start_date", "Quarter start date."), c("fi_revenue", "Revenue.", "USD"), c("fi_net_earn", "Net earnings.", "USD"),
    c("fi_basic_eps", "Basic EPS.", "USD"), c("fi_dilut_eps", "Diluted EPS.", "USD"), c("fi_margin", "Margin."),
    c("fi_assets", "Assets.", "USD"), c("fi_liability", "Liabilities.", "USD"),
    c("fi_out_basic", "Basic shares outstanding."), c("fi_out_dilut", "Diluted shares outstanding.")],
   [k("company_version_identity", "sk_company_id")], (None, ["fi_qtr", "fi_year", "sk_company_id"]), "fact",
   grain_description="One row per company version per fiscal quarter.")

# ---------------------------------------------------------------------------------------------
# Warehouse layer: TPC-DI facts
# ---------------------------------------------------------------------------------------------

ds(WAREHOUSE, "dw", "fact_cash_balances", "Cash balances fact", "End-of-day cash balance per account.",
   [c("sk_customer_id", "Customer version."), c("sk_account_id", "Account version."), c("sk_date_id", "Business date."),
    c("cash", "Cash balance at end of day.", "USD"), c("batch_id", "Load batch.")],
   [k("customer_version_identity", "sk_customer_id"), k("account_version_identity", "sk_account_id"),
    date_key("sk_date_id"), k("account_day_identity", "sk_account_id", "sk_date_id", unique=True)],
   ("account_day_identity", ["sk_account_id", "sk_date_id"]), "fact", synonyms=("FactCashBalances",),
   grain_description="One row per account per day with cash activity.")

ds(WAREHOUSE, "dw", "fact_holdings", "Holdings fact", "Holding changes with the trade that caused them.",
   [c("trade_id", "Trade that opened the lot."), c("current_trade_id", "Trade that changed the lot."),
    c("sk_customer_id", "Customer version."), c("sk_account_id", "Account version."), c("sk_security_id", "Security version."),
    c("sk_company_id", "Issuer version."), c("sk_date_id", "Date of the change."), c("sk_time_id", "Time of the change."),
    c("current_price", "Trade price of the change.", "USD"), c("current_holding", "Lot quantity after the change."),
    c("batch_id", "Load batch.")],
   [k("trade_identity", "trade_id", description="The trade that opened the lot."),
    k("trade_identity", "current_trade_id", unique=True, description="The trade that changed the lot."),
    k("customer_version_identity", "sk_customer_id"), k("account_version_identity", "sk_account_id"),
    k("security_version_identity", "sk_security_id"), k("company_version_identity", "sk_company_id"),
    date_key("sk_date_id"), time_key("sk_time_id")],
   ("trade_identity", ["current_trade_id"]), "fact", synonyms=("FactHoldings",))

ds(WAREHOUSE, "dw", "fact_market_history", "Market history fact", "Daily market statistics per security with 52-week extremes.",
   [c("sk_security_id", "Security version."), c("sk_company_id", "Issuer version."), c("sk_date_id", "Trading date."),
    c("pe_ratio", "Price over trailing four-quarter EPS."), c("yield", "Dividend over close price.", "percent"),
    c("fifty_two_week_high", "52-week high.", "USD"), c("sk_fifty_two_week_high_date", "Date of the 52-week high."),
    c("fifty_two_week_low", "52-week low.", "USD"), c("sk_fifty_two_week_low_date", "Date of the 52-week low."),
    c("close_price", "Close.", "USD"), c("day_high", "Day high.", "USD"), c("day_low", "Day low.", "USD"),
    c("volume", "Shares traded."), c("batch_id", "Load batch.")],
   [k("security_version_identity", "sk_security_id"), k("company_version_identity", "sk_company_id"),
    date_key("sk_date_id", "The trading day."), date_key("sk_fifty_two_week_high_date", "The day of the 52-week high."),
    date_key("sk_fifty_two_week_low_date", "The day of the 52-week low.")],
   (None, ["sk_date_id", "sk_security_id"]), "fact", synonyms=("FactMarketHistory",),
   grain_description="One row per security version per trading day.")

ds(WAREHOUSE, "dw", "fact_watches", "Watches fact", "When customers added and removed securities from watch lists.",
   [c("sk_customer_id", "Customer version."), c("sk_security_id", "Security version."),
    c("sk_date_id_date_placed", "Date the watch was placed."), c("sk_date_id_date_removed", "Date the watch was removed.", "null while active"),
    c("batch_id", "Load batch.")],
   [k("customer_version_identity", "sk_customer_id"), k("security_version_identity", "sk_security_id"),
    date_key("sk_date_id_date_placed", "The day the watch was placed."),
    date_key("sk_date_id_date_removed", "The day the watch was removed.", total=False)],
   (None, ["sk_customer_id", "sk_security_id"]), "fact", synonyms=("FactWatches",),
   grain_description="One row per customer version and security version watched.")

# ---------------------------------------------------------------------------------------------
# Warehouse layer: analytic marts (extension beyond TPC-DI)
# ---------------------------------------------------------------------------------------------

def account_day(*, universe: str = "partial") -> list[dict]:
    if universe == "complete":
        day = pk("account_day_identity", "sk_account_id", "sk_date_id")
    else:
        day = k("account_day_identity", "sk_account_id", "sk_date_id", unique=True)
    return [day, k("account_version_identity", "sk_account_id"), date_key("sk_date_id")]


ds(WAREHOUSE, "mart", "dim_month", "Month dimension", "Calendar months with trading-day counts.",
   [c("calendar_month_id", "Calendar month.", "YYYYMM"), c("month_name", "Month name."), c("calendar_qtr_id", "Calendar quarter.", "YYYYQ"),
    c("trading_days", "Trading days in the month."), c("sk_month_end_date_id", "Last calendar day of the month.")],
   [pk("calendar_month_identity", "calendar_month_id"), date_key("sk_month_end_date_id", "The last day of the month.")],
   ("calendar_month_identity", ["calendar_month_id"]), "dimension")

ds(WAREHOUSE, "mart", "dim_customer_segment", "Customer segment dimension", "Asset-based service segments.",
   [c("segment_code", "Segment code.", "SELF_DIRECTED, ACTIVE_TRADER, EMERGING, AFFLUENT, HNW high net worth"),
    c("segment_name", "Segment name."), c("min_assets", "Lower asset bound.", "USD"),
    c("max_assets", "Upper asset bound.", "USD; null for the top segment"),
    c("service_model", "Service model.", "DIGITAL, TEAM, DEDICATED_BROKER")],
   [pk("customer_segment_identity", "segment_code")], ("customer_segment_identity", ["segment_code"]), "dimension")

ds(WAREHOUSE, "mart", "dim_venue", "Venue dimension", "Warehouse copy of execution venues.",
   [c("venue_mic", "Market identifier code."), c("venue_name", "Venue name."), c("venue_type", "Venue type."),
    c("is_wholesaler", "Whether the venue is an off-exchange wholesaler.")],
   [k("venue_identity", "venue_mic", unique=True)], ("venue_identity", ["venue_mic"]), "dimension")

ds(WAREHOUSE, "mart", "dim_branch", "Branch dimension", "Warehouse copy of branches.",
   [c("branch_id", "Branch identifier."), c("branch_name", "Branch name."), c("region", "Sales region.")],
   [k("branch_identity", "branch_id", unique=True)], ("branch_identity", ["branch_id"]), "dimension")

ds(WAREHOUSE, "mart", "fact_account_daily", "Account daily snapshot", "End-of-day balances and performance for every open account.",
   [c("sk_account_id", "Account version."), c("sk_date_id", "Business date."), c("sk_customer_id", "Owner version."),
    c("long_market_value", "Market value of long positions.", "USD"), c("short_market_value", "Market value of short positions.", "USD"),
    c("cash_balance", "Cash balance.", "USD"), c("margin_debit", "Margin debit balance.", "USD"),
    c("total_equity", "Account equity.", "USD"), c("net_deposits", "Deposits minus withdrawals that day.", "USD"),
    c("realized_pl", "Realized profit and loss that day.", "USD"), c("unrealized_pl", "Change in unrealized profit and loss.", "USD"),
    c("trade_count", "Completed trades that day.")],
   [*account_day(universe="complete"), k("customer_version_identity", "sk_customer_id")],
   ("account_day_identity", ["sk_account_id", "sk_date_id"]), "fact", synonyms=("AUM snapshot", "account balance"))

ds(WAREHOUSE, "mart", "fact_revenue_daily", "Revenue daily", "Firm revenue attributed to each account each day.",
   [c("sk_account_id", "Account version."), c("sk_date_id", "Business date."), c("sk_broker_id", "Servicing broker version."),
    c("commission_revenue", "Commissions.", "USD"), c("fee_revenue", "Flat charges and account fees.", "USD"),
    c("margin_interest", "Margin interest accrued.", "USD"), c("pfof_revenue", "Payment for order flow attributed.", "USD"),
    c("sweep_revenue", "Cash sweep net interest.", "USD"), c("sec_lending_revenue", "Fully paid securities lending revenue.", "USD")],
   [*account_day(), k("broker_version_identity", "sk_broker_id")],
   ("account_day_identity", ["sk_account_id", "sk_date_id"]), "fact", synonyms=("revenue attribution",),
   grain_description="One row per account per day with revenue.")

ds(WAREHOUSE, "mart", "fact_margin_exposure_daily", "Margin exposure daily", "Daily margin requirement and call exposure per margin account.",
   [c("sk_account_id", "Account version."), c("sk_date_id", "Business date."), c("debit_balance", "Debit balance.", "USD"),
    c("maint_requirement", "Maintenance requirement.", "USD"), c("house_excess", "Equity above the house requirement.", "USD"),
    c("open_call_amount", "Open margin calls.", "USD"), c("top_sk_security_id", "Largest position by market value."),
    c("top_position_pct", "Largest position as a share of long market value.", "percent")],
   [*account_day(), k("security_version_identity", "top_sk_security_id", total=False)],
   ("account_day_identity", ["sk_account_id", "sk_date_id"]), "fact",
   grain_description="One row per margin account per day.")

ds(WAREHOUSE, "mart", "fact_customer_month", "Customer month", "Monthly customer value, activity, and retention.",
   [c("customer_id", "Durable customer identifier."), c("calendar_month_id", "Month."),
    c("segment_code", "Segment at month end."), c("tenure_months", "Months since the first account opened."),
    c("accounts_open", "Open accounts at month end."), c("assets_end", "Total equity at month end.", "USD"),
    c("net_new_assets", "Net new assets in the month.", "USD"), c("trades", "Completed trades."),
    c("revenue", "Attributed revenue.", "USD"), c("digital_sessions", "Digital sessions."),
    c("is_active", "Whether the customer traded or logged in during the month."),
    c("is_churned", "Whether the customer closed all accounts or transferred out by ACATS during the month.")],
   [k("customer_identity", "customer_id", description="The durable customer, not a version."),
    k("calendar_month_identity", "calendar_month_id"), k("customer_segment_identity", "segment_code")],
   (None, ["calendar_month_id", "customer_id"]), "fact", synonyms=("customer scorecard", "retention"),
   grain_description="One row per customer per month while the customer has an open account.")

ds(WAREHOUSE, "mart", "fact_broker_month", "Broker month", "Monthly book of business and production per broker.",
   [c("broker_id", "Durable broker identifier."), c("calendar_month_id", "Month."), c("branch_id", "Branch at month end."),
    c("accounts_serviced", "Accounts serviced at month end."), c("assets_under_care", "Equity of serviced accounts.", "USD"),
    c("trades", "Trades in serviced accounts."), c("commission", "Commission credited.", "USD"),
    c("new_accounts", "Accounts opened."), c("lost_accounts", "Accounts closed or transferred away."),
    c("complaints", "Complaints naming the broker.")],
   [k("broker_identity", "broker_id"), k("calendar_month_identity", "calendar_month_id"), k("branch_identity", "branch_id")],
   (None, ["broker_id", "calendar_month_id"]), "fact", synonyms=("rep production", "broker scorecard"),
   grain_description="One row per broker per month.")

ds(WAREHOUSE, "mart", "fact_execution_quality", "Execution quality", "Order-level execution quality measured against the NBBO at receipt (SEC Rule 605 basis).",
   [c("ord_id", "Order."), c("sk_security_id", "Security version."), c("sk_date_id", "Order date."),
    c("primary_venue_mic", "Venue that filled the most shares."), c("order_type", "Order type.", "MKT, LMT, STP, STL"),
    c("size_bucket", "Order size bucket.", "Rule 605 buckets: under 100, 100 to 499, 500 to 1999, 2000 to 4999, 5000 to 9999 shares"),
    c("arrival_mid", "NBBO midpoint at receipt.", "USD"), c("avg_fill_price", "Volume-weighted fill price.", "USD"),
    c("price_improvement_per_share", "Improvement versus the NBBO.", "USD per share; negative is disimprovement"),
    c("effective_spread_bps", "Effective spread.", "basis points"), c("fill_rate", "Filled shares over ordered shares.", "0 to 1"),
    c("ms_to_first_fill", "Latency to first fill.", "milliseconds; null when unfilled")],
   [k("order_identity", "ord_id", unique=True), k("security_version_identity", "sk_security_id"), date_key("sk_date_id"),
    k("venue_identity", "primary_venue_mic", total=False)],
   ("order_identity", ["ord_id"]), "fact", synonyms=("best execution", "Rule 605"))

ds(WAREHOUSE, "mart", "fact_routing_month", "Order routing month", "Monthly routing of non-directed orders by venue (SEC Rule 606 basis).",
   [c("calendar_month_id", "Month."), c("venue_mic", "Venue."), c("order_type_class", "Order class.", "MARKET, MARKETABLE_LIMIT, NON_MARKETABLE_LIMIT, OTHER"),
    c("orders_routed", "Non-directed orders routed."), c("pct_of_orders", "Share of the class routed to the venue.", "percent"),
    c("net_payment_usd", "Net payment received from the venue.", "USD"),
    c("payment_per_hundred_shares", "Net payment per hundred shares.", "cents")],
   [k("calendar_month_identity", "calendar_month_id"), k("venue_identity", "venue_mic")],
   (None, ["calendar_month_id", "order_type_class", "venue_mic"]), "fact", synonyms=("Rule 606", "PFOF report"),
   grain_description="One row per month, venue, and order class.")

ds(WAREHOUSE, "mart", "fact_net_new_assets", "Net new assets", "Asset flows into and out of accounts from transfers and ACATS.",
   [c("flow_source", "Source system.", "TRANSFER or ACATS"), c("source_id", "Identifier in the source system."),
    c("sk_account_id", "Account version."), c("sk_date_id", "Settlement date."),
    c("flow_type", "Flow type.", "ACH_IN, ACH_OUT, WIRE_IN, WIRE_OUT, CHECK_IN, ACATS_IN, ACATS_OUT, JOURNAL"),
    c("amount", "Flow value.", "USD; negative for outflows; ACATS securities at prior close"),
    c("transfer_id", "Funding transfer.", "null for ACATS flows"), c("acats_id", "ACATS transfer.", "null for funding transfers")],
   [k("account_version_identity", "sk_account_id"), date_key("sk_date_id"),
    k("transfer_identity", "transfer_id", unique=True, total=False), k("acats_transfer_identity", "acats_id", unique=True, total=False)],
   (None, ["flow_source", "source_id"]), "fact", synonyms=("NNA", "asset flows"),
   grain_description="One row per settled transfer or ACATS transfer.")

ds(WAREHOUSE, "mart", "fact_digital_engagement_daily", "Digital engagement daily", "Daily digital activity per customer.",
   [c("sk_customer_id", "Customer version."), c("sk_date_id", "Date."), c("sessions", "Sessions."),
    c("session_minutes", "Minutes in session."), c("orders_placed", "Orders placed digitally."),
    c("research_views", "Research and quote page views.")],
   [k("customer_version_identity", "sk_customer_id"), date_key("sk_date_id")],
   (None, ["sk_customer_id", "sk_date_id"]), "fact", grain_description="One row per customer version per day with a session.")

ds(WAREHOUSE, "mart", "fact_surveillance_alert", "Surveillance alert fact", "Surveillance alerts with time to disposition.",
   [c("alert_id", "Alert."), c("sk_account_id", "Account version."), c("sk_security_id", "Security version."),
    c("sk_alert_date_id", "Alert date."), c("sk_closed_date_id", "Close date.", "null while open"),
    c("pattern", "Pattern."), c("disposition", "Disposition."), c("days_open", "Days from alert to close.")],
   [k("surveillance_alert_identity", "alert_id", unique=True), k("account_version_identity", "sk_account_id"),
    k("security_version_identity", "sk_security_id"), date_key("sk_alert_date_id", "The day of the alert."),
    date_key("sk_closed_date_id", "The day the alert closed.", total=False)],
   ("surveillance_alert_identity", ["alert_id"]), "fact")

ds(WAREHOUSE, "mart", "fact_aml_alert", "AML alert fact", "AML alerts with escalation and SAR outcome.",
   [c("alert_id", "Alert."), c("sk_customer_id", "Customer version."), c("sk_date_id", "Alert date."),
    c("rule_code", "Monitoring rule."), c("score", "Risk score."), c("is_escalated", "Whether a case was opened."),
    c("is_sar_filed", "Whether the case ended in a SAR filing.")],
   [k("aml_alert_identity", "alert_id", unique=True), k("customer_version_identity", "sk_customer_id"), date_key("sk_date_id")],
   ("aml_alert_identity", ["alert_id"]), "fact")

ds(WAREHOUSE, "mart", "fact_complaint", "Complaint fact", "Complaints with resolution time.",
   [c("complaint_id", "Complaint."), c("sk_customer_id", "Customer version."), c("sk_broker_id", "Broker version named.", "null when none"),
    c("sk_received_date_id", "Receipt date."), c("sk_resolved_date_id", "Resolution date.", "null while open"),
    c("category", "Problem category."), c("days_to_resolve", "Days from receipt to resolution.")],
   [k("complaint_identity", "complaint_id", unique=True), k("customer_version_identity", "sk_customer_id"),
    k("broker_version_identity", "sk_broker_id", total=False), date_key("sk_received_date_id", "The day the complaint arrived."),
    date_key("sk_resolved_date_id", "The day the complaint was resolved.", total=False)],
   ("complaint_identity", ["complaint_id"]), "fact")

ds(WAREHOUSE, "mart", "fact_corporate_action_impact", "Corporate action impact", "Accounts and value affected by each corporate action.",
   [c("action_id", "Corporate action."), c("sk_security_id", "Security version."), c("sk_ex_date_id", "Ex-date."),
    c("accounts_entitled", "Accounts with an entitlement."), c("shares_eligible", "Shares held on the record date."),
    c("cash_paid", "Cash paid.", "USD"), c("shares_delivered", "Shares delivered.")],
   [k("corporate_action_identity", "action_id", unique=True), k("security_version_identity", "sk_security_id"),
    date_key("sk_ex_date_id", "The ex-date.")],
   ("corporate_action_identity", ["action_id"]), "fact")
