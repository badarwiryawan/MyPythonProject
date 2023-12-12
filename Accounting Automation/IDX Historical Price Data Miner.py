#Program ini memerlukan library Yahoo Finance (install: "pip install yfinance") dan Pandas (install: "pip install pandas").




#--------------------------IDX HISTORICAL PRICE DATA MINER OLEH BADAR WIRYAWAN--------------------------

import yfinance as yf
import pandas as pd

#--------------------------IDX HISTORICAL PRICE DATA MINER OLEH BADAR WIRYAWAN--------------------------

equity = input("Masukkan kode emiten: ")
start_time = input("Masukkan tanggal awal (YYYY-MM-DD): ")
end_time = input("Masukkan t + 1 tanggal akhir (YYYY-MM-DD): ")
timeframe = input("Masukkan timeframe (1 jam, 1 hari, 1 minggu, 1 bulan): ")

#--------------------------IDX HISTORICAL PRICE DATA MINER OLEH BADAR WIRYAWAN--------------------------

def historical_data_miner(Emiten = equity, 
                          Tanggal_awal = start_time, 
                          Tanggal_akhir = end_time, 
                          Jangka_waktu = timeframe):

    if timeframe == "1 jam":
        Jangka_waktu = "1h"
    elif timeframe == "1 hari":
        Jangka_waktu = "1d"
    elif timeframe == "1 minggu":
        Jangka_waktu = "1wk"
    elif timeframe == "1 bulan":
        Jangka_waktu == "1mo"

    data = yf.download(tickers = Emiten + ".JK", 
                       start = Tanggal_awal,  
                       end = Tanggal_akhir, 
                       interval = Jangka_waktu,)
    tables = pd.DataFrame(data)
    tables01 = tables.drop("Volume", axis = 1)

    Ekspor_hasil = input("Apakah Anda ingin mengekspor hasilnya (Y/N)?: ")
    if Ekspor_hasil == "Y":
        tables.to_csv(f"{equity}_Historical_Price_Data.csv")
    elif Ekspor_hasil == "N":
        print(tables01)

        Konfirmasi_ulang = input("Apakah Anda ingin mengekspor hasilnya kali ini (Y/N)?: ")
        if Konfirmasi_ulang == "Y":
            tables.to_csv(f"{equity}_Historical_Price_Data.csv")
        elif Konfirmasi_ulang == "N":
            print("Baiklah :)")

#--------------------------IDX HISTORICAL PRICE DATA MINER OLEH BADAR WIRYAWAN--------------------------

print(historical_data_miner())

#--------------------------IDX HISTORICAL PRICE DATA MINER OLEH BADAR WIRYAWAN--------------------------