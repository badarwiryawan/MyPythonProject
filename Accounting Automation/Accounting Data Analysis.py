#This program needs Yahoo Finance (install: "pip install yfinance") and Pandas (install: "pip install pandas") Library.




#-------------------------------------------ACCOUNTING DATA ANALYSIS BY BADAR WIRYAWAN-----------------------------------------------

import pandas as pd
import yfinance as yf

#-------------------------------------------ACCOUNTING DATA ANALYSIS BY BADAR WIRYAWAN-----------------------------------------------

equity = input("Insert IDX Stock Ticker: ")
year = int(input("Insert The Report Year: "))
data_to_analysis = input("Select Analysis (1 = Profitability, 2 = Liquidity): ")

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

#-------------------------------------------ACCOUNTING DATA ANALYSIS BY BADAR WIRYAWAN-----------------------------------------------
