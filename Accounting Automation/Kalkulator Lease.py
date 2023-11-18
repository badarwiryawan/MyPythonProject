#Program ini memerlukan library Pandas, install dengan "pip install pandas"




#-----------------------------------KALKULATOR LEASE OLEH BADAR WIRYAWAN---------------------------------------------

import pandas as pd

#-----------------------------------KALKULATOR LEASE OLEH BADAR WIRYAWAN---------------------------------------------

Pembayaran_sewa = float(input("Masukkan pembayaran sewa (tahun): "))
Bunga_sewa = float(input("Masukkan tingkat bunga sewa (tahun): "))
Periode = int(input("Masukkan lamanya sewa (tahun): "))

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

    Cetak_hasil = input("Apakah Anda ingin mencetak hasil (Y/N)?: ")
    if Cetak_hasil == "Y":
        data.to_csv("Kalkulasi_Lease.csv")
    elif Cetak_hasil == "N":
        print(data)

        Konfirmasi_cetak = input("Apakah Anda ingin mencetaknya kali ini (Y/N)?: ")
        if Konfirmasi_cetak == "Y":
            data.to_csv("Kalkulasi_Lease.csv")
        elif Konfirmasi_cetak == "N":
            print("Baiklah :)")

#-----------------------------------KALKULATOR LEASE OLEH BADAR WIRYAWAN---------------------------------------------

print(lease_schedule())

#-----------------------------------KALKULATOR LEASE OLEH BADAR WIRYAWAN---------------------------------------------