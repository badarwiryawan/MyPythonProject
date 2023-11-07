#Program ini memerlukan library Pandas, install dengan command "pip install pandas"




#-------------------------------KALKULATOR VALUASI PENDEKATAN PENDAPATAN OLEH BADAR WIRYAWAN-----------------------------------------

import pandas as pd

Net_Income = float(input("Masukkan Pendapatan: "))
Increment = float(input("Masukkan Nominal Kenaikan Pendapatan: "))
Discount_Rate = float(input("Masukkan Tingkat Diskonto: "))
Periods = int(input("Masukkan Lamanya Tahun: "))

#-------------------------------KALKULATOR VALUASI PENDEKATAN PENDAPATAN OLEH BADAR WIRYAWAN-----------------------------------------

def pendekatan_discounted_cash_flow(Pendapatan=Net_Income, Inkremental=Increment, Tingkat_Diskonto=Discount_Rate, Periode=Periods):

    #PENAMBANGAN DATA DAFTAR PENDAPATAN

    Daftar_Pendapatan = []

    for a in range(Periode):
        Daftar_Pendapatan.append(Pendapatan)
        Pendapatan += Inkremental

    #PENAMBANGAN DATA DAFTAR PV FACTOR

    Daftar_PV_Factor = []

    for b in range(1, Periode+1):
        PV_Factor = 1 / ((1 + Tingkat_Diskonto) ** b)
        Daftar_PV_Factor.append(PV_Factor)

    #PENGHITUNGAN PENDAPATAN DISESUAIKAN (PRESENT VALUE)

    Daftar_Pendapatan_Adjusted = []

    for c, d in zip(range(0, Periode), range(0, Periode)):
        Pendapatan_Adj = round(Daftar_Pendapatan[c] * Daftar_PV_Factor[d], 4)
        Daftar_Pendapatan_Adjusted.append(Pendapatan_Adj)

    #PENGHITUNGAN PENDAPATAN KUMULATIF
    #Ini adalah nilai valuasi tahun ke-n

    Daftar_Pendapatan_Kumulatif = []

    Revenue = 0
    for e in Daftar_Pendapatan_Adjusted:
        Revenue += e
        Daftar_Pendapatan_Kumulatif.append(Revenue)
        
    #PENGINPUTAN DATA KE DALAM TABEL

    tables = {"Tahun": range(1, Periode+1), "Pendapatan": Daftar_Pendapatan, "PV Factor": Daftar_PV_Factor, "Pendapatan Disesuaikan": Daftar_Pendapatan_Adjusted, "Pendapatan Kumulatif": Daftar_Pendapatan_Kumulatif}
    data = pd.DataFrame(tables)

    #EXPORT KE FILE CSV

    Cetak = input("Ingin mencetak hasil (Y/N)?: ")

    if Cetak == "Y":
        data.to_csv("Kalkulasi_Pendekatan_Pendapatan.csv")
    elif Cetak == "N":
        print(data)

        Konfirmasi_Cetak = input("Apakah Anda ingin mencetaknya kali ini (Y/N)?: ")

        if Konfirmasi_Cetak == "Y":
            data.to_csv("Kalkulasi_Pendekatan_Pendapatan.csv")
        elif Konfirmasi_Cetak == "N":
            print("Baiklah :)")
 
#-------------------------------KALKULATOR VALUASI PENDEKATAN PENDAPATAN OLEH BADAR WIRYAWAN-----------------------------------------

print(pendekatan_discounted_cash_flow())

#-------------------------------KALKULATOR VALUASI PENDEKATAN PENDAPATAN OLEH BADAR WIRYAWAN-----------------------------------------
