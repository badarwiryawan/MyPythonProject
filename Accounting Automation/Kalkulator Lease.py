#Program ini memerlukan library Pandas, install dengan "pip install pandas"




#-----------------------------------KALKULATOR LEASE OLEH BADAR WIRYAWAN---------------------------------------------

import pandas as pd
import locale
import datetime
from datetime import datetime

#-----------------------------------KALKULATOR LEASE OLEH BADAR WIRYAWAN---------------------------------------------

Pembayaran_sewa = float(input("Masukkan pembayaran sewa (tahun): "))
Bunga_sewa = float(input("Masukkan tingkat bunga sewa (tahun): "))
Periode = int(input("Masukkan lamanya sewa (tahun): "))

locale.setlocale(locale.LC_ALL, "id_ID")

#-----------------------------------KALKULATOR LEASE OLEH BADAR WIRYAWAN---------------------------------------------

def lease_schedule(Lease_payment = Pembayaran_sewa, Lease_rate = Bunga_sewa, Periods = Periode):

    #KOLOM 01

    daftar_tahun = []

    for a in range(Periods + 1):
        daftar_tahun.append(a)

    #KOLOM 02

    daftar_pembayaran = [0]

    for b in range(Periods):
        pembayaran = Lease_payment
        daftar_pembayaran.append(pembayaran)

    #KOLOM 03, 04, 05

    daftar_beban_bunga = [0]
    daftar_pengurangan_utang_sewa = [0]
    daftar_utang_sewa = []

    PV_Annuity_Factor = (1 - (1 / (1 + Lease_rate) ** Periods)) / Lease_rate
    Utang_sewa_awal = Lease_payment * PV_Annuity_Factor
    daftar_utang_sewa.append(Utang_sewa_awal)
    
    for c in range(Periods):
        beban_bunga = daftar_utang_sewa[c] * Lease_rate
        daftar_beban_bunga.append(beban_bunga)

        pengurangan_utang_sewa = daftar_pembayaran[c + 1] - daftar_beban_bunga[c + 1]
        daftar_pengurangan_utang_sewa.append(pengurangan_utang_sewa)

        utang_sewa = daftar_utang_sewa[c] - daftar_pengurangan_utang_sewa[c + 1] 
        daftar_utang_sewa.append(utang_sewa)

    #KOLOM 06, 07, 08

    daftar_beban_amortisasi = [0]
    daftar_hak_guna_aset = [Utang_sewa_awal]
    daftar_akumulasi_amortisasi = [0]

    for d in range(Periods):
        beban_amortisasi = (Utang_sewa_awal - 0) / Periods
        daftar_beban_amortisasi.append(beban_amortisasi)

    for e in range(Periods):
        hak_guna_aset_baru = daftar_hak_guna_aset[e] - daftar_beban_amortisasi[e + 1]
        daftar_hak_guna_aset.append(hak_guna_aset_baru)  

    for f in range(Periods):
        akumulasi_amortisasi = daftar_akumulasi_amortisasi[f] + daftar_beban_amortisasi[f + 1]
        daftar_akumulasi_amortisasi.append(akumulasi_amortisasi) 

    tables = {"TAHUN": daftar_tahun,
              "PEMBAYARAN KAS": daftar_pembayaran,
              "BEBAN BUNGA": daftar_beban_bunga,
              "PENGURANGAN UTANG SEWA": daftar_pengurangan_utang_sewa,
              "UTANG SEWA": daftar_utang_sewa,
              "BEBAN AMORTISASI": daftar_beban_amortisasi,
              "HAK GUNA ASET": daftar_hak_guna_aset,
              "AKUMULASI AMORTISASI": daftar_akumulasi_amortisasi
              }
    data = pd.DataFrame(tables)

    Cetak_hasil = input("Apakah Anda ingin mencetak hasilnya (Y/N)?: ")
    today_date = datetime.now().date()

    if Cetak_hasil == "Y":
        data.to_csv(f"Kalkulasi_Lease_{str(today_date)}.csv")
    elif Cetak_hasil == "N":
        print(data)

        Jurnal_transaksi = input("Apakah Anda ingin melihat jurnal transaksinya (Y/N)?: ")
        if Jurnal_transaksi == "Y":
            rupiah_hak_guna_aset = locale.currency(daftar_hak_guna_aset[0], grouping=True)
            rupiah_utang_sewa = locale.currency(daftar_utang_sewa[0], grouping=True)

            daftar_rupiah_pengurangan_utang_sewa = []
            daftar_rupiah_beban_bunga = []
            daftar_rupiah_beban_amortisasi = []
            daftar_rupiah_pembayaran = []

            for g in range(0, Periods + 1):
                rupiah_pengurangan_utang_sewa = locale.currency(daftar_pengurangan_utang_sewa[g], grouping=True)
                rupiah_beban_bunga = locale.currency(daftar_beban_bunga[g], grouping=True)
                rupiah_beban_amortisasi = locale.currency(daftar_beban_amortisasi[g], grouping=True)
                rupiah_pembayaran = locale.currency(daftar_pembayaran[g], grouping=True)
                daftar_rupiah_pengurangan_utang_sewa.append(rupiah_pengurangan_utang_sewa)
                daftar_rupiah_beban_bunga.append(rupiah_beban_bunga)
                daftar_rupiah_beban_amortisasi.append(rupiah_beban_amortisasi)
                daftar_rupiah_pembayaran.append(rupiah_pembayaran)

            print("Hak Guna Aset" + " " * 26 + f"{rupiah_hak_guna_aset}")
            print(" " * 4 + "Utang Sewa" + " " * 32 + f"{rupiah_utang_sewa}")
            print("(" + "\033[3m" + "Pencatatan Hak Sewa" + "\033[0m" + ")")
            print(" ")
            for h in range(1, Periods + 1):
                print("Utang Sewa" + " " * 29 + f"{daftar_rupiah_pengurangan_utang_sewa[h]}" )
                print("Beban Bunga" + " " * 28 + f"{daftar_rupiah_beban_bunga[h]}")
                print("Beban Amortisasi Hak Guna Aset" + " " * 9 + f"{daftar_rupiah_beban_amortisasi[h]}")
                print(" " * 4 + "Akumulasi Amortisasi Hak Guna Aset" + " " * 8 + f"{daftar_rupiah_beban_amortisasi[h]}")
                print(" " * 4 + "Kas" + " " * 39 + f"{daftar_rupiah_pembayaran[h]}" )
                print("(" + "\033[3m" + f"Pembayaran Pokok, Bunga, dan Pencatatan Amortisasi ke-{h}" + "\033[0m" + ")")
                print(" ")
        
        elif Jurnal_transaksi == "N":
            print("Baiklah :)")


#-----------------------------------KALKULATOR LEASE OLEH BADAR WIRYAWAN---------------------------------------------

print(lease_schedule())

#-----------------------------------KALKULATOR LEASE OLEH BADAR WIRYAWAN---------------------------------------------
