#Program ini memerlukan library Pandas (install: "pip install pandas") dan Yahoo Finance (install: "pip install yfinance")




#-------------------------------------------ACCOUNTING DATA MINER OLEH BADAR WIRYAWAN-------------------------------------------

import pandas as pd
import yfinance as yf

#-------------------------------------------ACCOUNTING DATA MINER OLEH BADAR WIRYAWAN-------------------------------------------

equity = input("Masukkan kode saham: ")
acc_data = input("Pilih informasi (Neraca = 1, Laba Rugi = 2, Arus Kas = 3): ")

#-------------------------------------------ACCOUNTING DATA MINER OLEH BADAR WIRYAWAN-------------------------------------------

def accounting_data_miner(Code=equity, Information=acc_data):
    
    stock_data = yf.Ticker(Code + ".JK")

    if Information == "1":
        data = stock_data.get_balance_sheet()
        tables = pd.DataFrame(data)
        reverse_tables = tables.loc[::-1]
        
        Ekspor = input("Apakah Anda akan mengekspor datanya (Y/N)?: ")
        if Ekspor == "Y":
            reverse_tables.to_csv(f"Laporan_Posisi_Keuangan_{Code}.csv")
        elif Ekspor == "N":
            print(reverse_tables)

            Konfirmasi_Ekspor = input("Apakah Anda akan mengekspornya kali ini (Y/N)?: ")

            if Konfirmasi_Ekspor == "Y":
                reverse_tables.to_csv(f"Laporan_Posisi_Keuangan_{Code}.csv")
            elif Konfirmasi_Ekspor == "N":
                print("Baiklah :)")

    elif Information == "2":
        data = stock_data.get_income_stmt()
        tables = pd.DataFrame(data)
        reverse_tables = tables.loc[::-1]

        Ekspor = input("Apakah Anda akan mengekspor datanya (Y/N)?: ")
        if Ekspor == "Y":
            reverse_tables.to_csv(f"Laporan_Laba_Rugi_{Code}.csv")
        elif Ekspor == "N":
            print(reverse_tables)

            Konfirmasi_Ekspor = input("Apakah Anda akan mengekspornya kali ini (Y/N)?: ")

            if Konfirmasi_Ekspor == "Y":
                reverse_tables.to_csv(f"Laporan_Laba_Rugi_{Code}.csv")
            elif Konfirmasi_Ekspor == "N":
                print("Baiklah :)")
    
    elif Information == "3":
        data = stock_data.get_cash_flow()
        tables = pd.DataFrame(data)
        reverse_tables = tables.loc[::-1]

        Ekspor = input("Apakah Anda akan mengekspor datanya (Y/N)?: ")
        if Ekspor == "Y":
            reverse_tables.to_csv(f"Laporan_Arus_Kas_{Code}.csv")
        elif Ekspor == "N":
            print(reverse_tables)

            Konfirmasi_Ekspor = input("Apakah Anda akan mengekspornya kali ini (Y/N)?: ")

            if Konfirmasi_Ekspor == "Y":
                reverse_tables.to_csv(f"Laporan_Arus_Kas_{Code}.csv")
            elif Konfirmasi_Ekspor == "N":
                print("Baiklah :)")

#-------------------------------------------ACCOUNTING DATA MINER OLEH BADAR WIRYAWAN-------------------------------------------

print(accounting_data_miner())

#-------------------------------------------ACCOUNTING DATA MINER OLEH BADAR WIRYAWAN-------------------------------------------