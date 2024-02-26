import pandas as pd
import yfinance as yf

#-------------------------------------------CASH CONVERSION CYCLE OLEH BADAR WIRYAWAN-------------------------------------------

equity = input("Masukkan kode saham: ")
Tahun = int(input("Masukkan tahun: "))

#-------------------------------------------CASH CONVERSION CYCLE OLEH BADAR WIRYAWAN-------------------------------------------
   
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

#-------------------------------------------CASH CONVERSION CYCLE OLEH BADAR WIRYAWAN-------------------------------------------

def cash_conversion_cycle(Tahun = Tahun):

    inventory = reverse_tables00.at["Inventory", f"{Tahun}-12-31"]
    accounts_receivable = reverse_tables00.at["AccountsReceivable", f"{Tahun}-12-31"]
    accounts_payable = reverse_tables00.at["AccountsPayable", f"{Tahun}-12-31"]
    revenue = reverse_tables01.at["TotalRevenue", f"{Tahun}-12-31"]
    cost_of_revenue = reverse_tables01.at["CostOfRevenue", f"{Tahun}-12-31"]

    day_inventory_outstanding = (inventory / cost_of_revenue) * 365
    day_receivables_outstanding = (accounts_receivable / revenue) * 365
    day_payables_outstanding = (accounts_payable / cost_of_revenue) * 365

    cash_conversion_cycle = day_inventory_outstanding + day_receivables_outstanding - day_payables_outstanding

    
    print(f"Cash Conversion Cycle {equity} pada {Tahun} adalah \033[1m{round(cash_conversion_cycle, 2)}\033[0m") 

print(cash_conversion_cycle())

#-------------------------------------------CASH CONVERSION CYCLE OLEH BADAR WIRYAWAN-------------------------------------------
