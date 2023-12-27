#Program ini memerlukan library Yahoo Finance (install: "pip install yfinance"),
#Investing.com (install: "pip install investpy"),
#dan Pandas (isntall: "pip install pandas").




#-----------------------------------------------------------------------COST OF CAPITAL AND VALUATION OLEH BADAR WIRYAWAN-----------------------------------------------------------------------

import yfinance as yf
import investpy as ip
import pandas as pd

#-----------------------------------------------------------------------COST OF CAPITAL AND VALUATION OLEH BADAR WIRYAWAN-----------------------------------------------------------------------

equity = input("Masukkan kode saham: ")
year = int(input("Masukkan tahun laporan: "))
select_valuation = input("Pilih valuasi (1 = Cost of Equity Capital, 2 = Cost of Debt, 3 = Weighted Average Cost of Capital): ")

#-----------------------------------------------------------------------COST OF CAPITAL AND VALUATION OLEH BADAR WIRYAWAN-----------------------------------------------------------------------

def cost_of_equity_capital(Tick = equity, Tahun = year):
    
    #GET STOCK BETA
    stock_data = yf.Ticker(ticker=Tick + ".JK")
    beta = stock_data.info["beta"]

    #GET RISK-FREE RATE 
    data01 = ip.economic_calendar(time_zone = "GMT +7:00", countries = ["indonesia"], categories = ["Central Banks"], from_date = f"01/12/{Tahun}", to_date = f"31/12/{Tahun}")
    table01 = pd.DataFrame(data01)
    to_delete = ["id", "date", "time", "zone", "currency", "importance"]
    table01_rev = table01.drop(to_delete, axis=1)
    get_index = table01_rev.index[table01_rev["event"]=="Interest Rate Decision"].tolist()
    suku_bunga = table01_rev.iloc[get_index[0], 1]
    get_number = float(suku_bunga[:4])
    risk_free_rate = get_number / 100

    #COMPUTE INDEX RETURN
    data02 = yf.download(tickers="^JKSE", start=f"{Tahun}-01-01", end=f"{Tahun+1}-01-01")
    table02 = pd.DataFrame(data02)
    start_close = table02["Close"].iloc[0]
    end_close = table02["Close"].iloc[-1]
    index_return = (end_close - start_close) / start_close

    #COST OF EQUITY
    Cost_of_Equity = risk_free_rate + (beta * (index_return - risk_free_rate))
    Cost_of_Equity_Percent = round(Cost_of_Equity * 100, 4)

    print(f"THE {Tahun} {Tick} COST OF EQUITY CAPITAL = {Cost_of_Equity_Percent}%")

#-----------------------------------------------------------------------COST OF CAPITAL AND VALUATION OLEH BADAR WIRYAWAN-----------------------------------------------------------------------

def cost_of_debt(Tick = equity, Tahun = year):

    #GET BALANCE SHEET AND INCOME STATEMENT
    balance_sheet = yf.Ticker(ticker=Tick + ".JK").get_balance_sheet()
    income_statement = yf.Ticker(ticker=Tick + ".JK").get_income_stmt()
    balance_sheet_table = pd.DataFrame(balance_sheet).loc[::-1]
    income_statement_table = pd.DataFrame(income_statement).loc[::-1]

    #COMPUTE PRETAX BORROWING RATE
    interest_expense = income_statement_table.at["InterestExpenseNonOperating", f"{Tahun}-12-31"]
    debt_and_lease = balance_sheet_table.at["CurrentDebtAndCapitalLeaseObligation", f"{Tahun}-12-31"] + balance_sheet_table.at["LongTermDebtAndCapitalLeaseObligation", f"{Tahun}-12-31"]    

    #TAX RATE
    tax_rate = 0.19

    #COST OF DEBT
    Cost_of_Debt = (interest_expense / debt_and_lease) * (1 - tax_rate)
    Cost_of_Debt_Percent = round(Cost_of_Debt * 100, 4)

    print(f"THE {Tahun} {Tick} COST OF DEBT = {Cost_of_Debt_Percent}%")

#-----------------------------------------------------------------------COST OF CAPITAL AND VALUATION OLEH BADAR WIRYAWAN-----------------------------------------------------------------------

def weighted_average_cost_of_capital(Tick = equity, Tahun = year):

    #GET INFLATION
    inflation_data = ip.economic_calendar(time_zone = "GMT +7:00", countries = ["indonesia"], categories = ["Central Banks"], from_date = f"01/01/{Tahun+1}", to_date = f"31/01/{Tahun+1}")
    inflation_table = pd.DataFrame(inflation_data)
    to_delete = ["id", "date", "time", "zone", "currency", "importance"]
    inflation_table_rev = inflation_table.drop(to_delete, axis=1)
    get_index = inflation_table_rev.index[inflation_table_rev["event"]=="Inflation (YoY)  (Dec)"].tolist()
    tingkat_inflasi = inflation_table_rev.iloc[get_index[0], 1]
    get_number = float(tingkat_inflasi[:4])
    inflation_rate = get_number / 100

    #GET INTEREST RATE
    interest_rate_data = ip.economic_calendar(time_zone = "GMT +7:00", countries = ["indonesia"], categories = ["Central Banks"], from_date = f"01/12/{Tahun}", to_date = f"31/12/{Tahun}")
    interest_table = pd.DataFrame(interest_rate_data)
    to_delete = ["id", "date", "time", "zone", "currency", "importance"]
    interest_table_rev = interest_table.drop(to_delete, axis=1)
    get_index = interest_table_rev.index[interest_table_rev["event"]=="Interest Rate Decision"].tolist()
    suku_bunga = interest_table_rev.iloc[get_index[0], 1]
    get_number = float(suku_bunga[:4])
    risk_free_rate = get_number / 100

    #INTRINSIC VALUE OF COMPANY
    balance_sheet = yf.Ticker(ticker=Tick + ".JK").get_balance_sheet()
    balance_sheet_table = pd.DataFrame(balance_sheet).loc[::-1]
    intrinsic_value_debt = (1 + risk_free_rate - inflation_rate) * balance_sheet_table.at["TotalLiabilitiesNetMinorityInterest", f"{Tahun}-12-31"]
    intrinsic_value_equity = (1 + risk_free_rate - inflation_rate) * balance_sheet_table.at["TotalEquityGrossMinorityInterest", f"{Tahun}-12-31"]

    #COST OF DEBT
    balance_sheet = yf.Ticker(ticker=Tick + ".JK").get_balance_sheet()
    income_statement = yf.Ticker(ticker=Tick + ".JK").get_income_stmt()
    balance_sheet_table = pd.DataFrame(balance_sheet).loc[::-1]
    income_statement_table = pd.DataFrame(income_statement).loc[::-1]
    interest_expense = income_statement_table.at["InterestExpenseNonOperating", f"{Tahun}-12-31"]
    debt_and_lease = balance_sheet_table.at["CurrentDebtAndCapitalLeaseObligation", f"{Tahun}-12-31"] + balance_sheet_table.at["LongTermDebtAndCapitalLeaseObligation", f"{Tahun}-12-31"]    
    tax_rate = 0.19
    Cost_of_Debt = (interest_expense / debt_and_lease) * (1 - tax_rate)

    #COST OF EQUITY
    stock_data = yf.Ticker(ticker=Tick + ".JK")
    beta = stock_data.info["beta"]
    data01 = ip.economic_calendar(time_zone = "GMT +7:00", countries = ["indonesia"], categories = ["Central Banks"], from_date = f"01/12/{Tahun}", to_date = f"31/12/{Tahun}")
    table01 = pd.DataFrame(data01)
    to_delete = ["id", "date", "time", "zone", "currency", "importance"]
    table01_rev = table01.drop(to_delete, axis=1)
    get_index = table01_rev.index[table01_rev["event"]=="Interest Rate Decision"].tolist()
    suku_bunga = table01_rev.iloc[get_index[0], 1]
    get_number = float(suku_bunga[:4])
    risk_free_rate = get_number / 100
    data02 = yf.download(tickers="^JKSE", start=f"{Tahun}-01-01", end=f"{Tahun+1}-01-01")
    table02 = pd.DataFrame(data02)
    start_close = table02["Close"].iloc[0]
    end_close = table02["Close"].iloc[-1]
    index_return = (end_close - start_close) / start_close
    Cost_of_Equity = risk_free_rate + (beta * (index_return - risk_free_rate))

    #WACC
    wacc = (Cost_of_Debt * (intrinsic_value_debt / (intrinsic_value_debt + intrinsic_value_equity))) + (Cost_of_Equity * (intrinsic_value_equity / (intrinsic_value_debt + intrinsic_value_equity)))
    wacc_in_percent = round(wacc * 100, 4)

    print(f"THE {Tahun} {Tick} WEIGHTED AVERAGE COST OF CAPITAL = {wacc_in_percent}%")

#-----------------------------------------------------------------------COST OF CAPITAL AND VALUATION OLEH BADAR WIRYAWAN-----------------------------------------------------------------------

if select_valuation == "1":
    print(cost_of_equity_capital())
elif select_valuation == "2":
    print(cost_of_debt())
elif select_valuation == "3":
    print(weighted_average_cost_of_capital())

#-----------------------------------------------------------------------COST OF CAPITAL AND VALUATION OLEH BADAR WIRYAWAN-----------------------------------------------------------------------