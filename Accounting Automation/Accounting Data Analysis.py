#This program needs Yahoo Finance (install: "pip install yfinance") and Pandas (install: "pip install pandas") Library.




#-------------------------------------------ACCOUNTING DATA ANALYSIS BY BADAR WIRYAWAN-----------------------------------------------

import pandas as pd
import yfinance as yf

#-------------------------------------------ACCOUNTING DATA ANALYSIS BY BADAR WIRYAWAN-----------------------------------------------

equity = input("Insert IDX Stock Ticker: ")
year = int(input("Insert The Report Year: "))
data_to_analysis = input("Select Analysis (1 = Profitability, 2 = Liquidity, 3 = Altman Z-Score): ")

#-------------------------------------------ACCOUNTING DATA ANALYSIS BY BADAR WIRYAWAN-----------------------------------------------
   
stock_data = yf.Ticker(equity + ".JK")

data00 = stock_data.get_balance_sheet()
data01 = stock_data.get_income_stmt()
#data02 = stock_data.get_cash_flow()
tables00 = pd.DataFrame(data00)
tables01 = pd.DataFrame(data01)
#tables02 = pd.DataFrame(data02)
reverse_tables00 = tables00.loc[::-1]
reverse_tables01 = tables01.loc[::-1]
#reverse_tables02 = tables02.loc[::-1]

#-------------------------------------------ACCOUNTING DATA ANALYSIS BY BADAR WIRYAWAN-----------------------------------------------

def profitability_analysis(Year = year):

    #Return on Assets
    Net_income = reverse_tables01.at["NetIncome", f"{Year}-12-31"]
    Total_asset = reverse_tables00.at["TotalAssets", f"{Year}-12-31"]
    ROA = round((Net_income / Total_asset) * 100, 4)

    print(f"{equity} Return on Assets = {ROA}%")

    #Return on Equity
    Net_income = reverse_tables01.at["NetIncome", f"{Year}-12-31"]
    Stockholders_equity = reverse_tables00.at["TotalEquityGrossMinorityInterest", f"{Year}-12-31"]
    ROE = round((Net_income / Stockholders_equity) * 100, 4)

    print(f"{equity} Return on Equity = {ROE}%")

def liquidity_analysis(Year = year):

    #Current Ratio
    Current_asset = reverse_tables00.at["CurrentAssets", f"{Year}-12-31"]
    Current_liabilities = reverse_tables00.at["CurrentLiabilities", f"{Year}-12-31"]
    CR = round(Current_asset / Current_liabilities, 4)

    print(f"{equity} Current Ratio = {CR}")

    #Quick Ratio
    Current_asset_exclude_inventory = reverse_tables00.at["CashCashEquivalentsAndShortTermInvestments", f"{Year}-12-31"] + reverse_tables00.at["AccountsReceivable", f"{Year}-12-31"]
    Current_liabilities = reverse_tables00.at["CurrentLiabilities", f"{Year}-12-31"]
    QR = round(Current_asset_exclude_inventory / Current_liabilities, 4)

    print(f"{equity} Quick Ratio = {QR}")

def altman_score(Ticker = equity, Year = year):

    data_stock = yf.download(tickers=Ticker+".JK", start=f"{Year}-12-24", end=f"{Year+1}-01-01")
    table_stock = pd.DataFrame(data_stock)
    latest_close = table_stock["Close"].iloc[-1]

    first_common_factor = 1 / reverse_tables00.at["TotalAssets", f"{Year}-12-31"] 
    working_capital = 1.2 * reverse_tables00.at["WorkingCapital", f"{Year}-12-31"]
    retained_earnings = 1.4 * reverse_tables00.at["RetainedEarnings", f"{Year}-12-31"]
    the_EBIT = 3.3 * reverse_tables01.at["EBIT", f"{Year}-12-31"]
    second_common_factor = 1 / reverse_tables00.at["TotalLiabilitiesNetMinorityInterest", f"{Year}-12-31"]
    market_cap = 0.6 * reverse_tables00.at["OrdinarySharesNumber", f"{Year}-12-31"] * latest_close 
    revenue = 0.99 * reverse_tables01.at["OperatingRevenue", f"{Year}-12-31"]

    altman_z_score = (first_common_factor * (working_capital + retained_earnings + the_EBIT)) + (second_common_factor * (market_cap + revenue))

    if altman_z_score > 3.00:
        print(f"Altman Z-Score = {altman_z_score}")
        print("Company is healthy and there's low bankruptcy potential in the short term.")
    elif 2.99 > altman_z_score > 1.80:
        print(f"Altman Z-Score = {altman_z_score}")
        print("Gray area-company is exposed to some risk of bankruptcy; caution is advised.")
    elif 1.80 > altman_z_score:
        print(f"Altman Z-Score = {altman_z_score}")
        print("Company is in financial distress and there's high bankruptcy potential in short term.")

#-------------------------------------------ACCOUNTING DATA ANALYSIS BY BADAR WIRYAWAN-----------------------------------------------

if data_to_analysis == "1":
    print("\n")
    print(f"THE {str(year)} {equity} PROFITABILITY ANALYSIS")
    print(" ")
    print(profitability_analysis())

elif data_to_analysis == "2":
    print("\n")
    print(f"THE {str(year)} {equity} LIQUIDITY ANALYSIS")
    print(" ")
    print(liquidity_analysis())

elif data_to_analysis == "3":
    print("\n")
    print(f"THE {str(year)} {equity} ALTMAN Z-SCORE")
    print(" ")
    print(altman_score())

#-------------------------------------------ACCOUNTING DATA ANALYSIS BY BADAR WIRYAWAN-----------------------------------------------
