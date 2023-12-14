#Program ini memerlukan library Pandas, install dengan "pip install pandas"
#Hanya dapat digunakan di obligasi premium atau diskon.



#---------------------------------------------------------KALKULATOR AMORTISASI OBLIGASI METODE BUNGA EFEKTIF OLEH BADAR WIRYAWAN------------------------------------------------------------------------

import pandas as pd
import datetime
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "id_ID")

Nilai_Nominal = float(input("Masukkan nilai nominal obligasi: "))
Bunga_Nominal = float(input("Masukkan bunga nominal obligasi: "))
Bunga_Efektif = float(input("Masukkan bunga efektif: "))
Pembayaran = int(input("Masukkan banyaknya pembayaran per tahun: "))
Tempo = int(input("Masukkan tempo obligasi (tahun): "))

#---------------------------------------------------------KALKULATOR AMORTISASI OBLIGASI METODE BUNGA EFEKTIF OLEH BADAR WIRYAWAN------------------------------------------------------------------------

def kalkulasi_obligasi(Face_value=Nilai_Nominal, Nominal_interest=Bunga_Nominal, Effective_Interest=Bunga_Efektif, Payment=Pembayaran, Period=Tempo):

    #KOLOM 01

    daftar_banyaknya_pembayaran = []
    jumlah_bayar = Payment * Period

    Banyaknya_pembayaran = 0    
    for a in range(jumlah_bayar+1):
        Banyaknya_pembayaran = a
        daftar_banyaknya_pembayaran.append(Banyaknya_pembayaran)

    #KOLOM 02

    daftar_pembayaran_tunai = [0]
    pembayaran_tunai = Face_value * (Nominal_interest / Payment)
    
    for b in range(jumlah_bayar):
        daftar_pembayaran_tunai.append(pembayaran_tunai)

    #KOLOM 03, 04, dan 05

    daftar_beban_bunga = [0]
    daftar_pengurangan_amortisasi = [0]
    
    PV_Factor = 1 / ((1 + (Effective_Interest / Payment)) ** (jumlah_bayar))
    PV_Annuity_Factor = (1 - PV_Factor)/(Effective_Interest / Payment)

    Nilai_buku_awal = (Face_value * PV_Factor) + (Face_value * (Nominal_interest / Payment) * PV_Annuity_Factor)
        
    daftar_nilai_buku = [Nilai_buku_awal]

    if Nominal_interest > Effective_Interest:
        daftar_amortisasi = [Nilai_buku_awal - Face_value]

    elif Nominal_interest < Effective_Interest:
        daftar_amortisasi = [Face_value - Nilai_buku_awal]

    for c in range(0, (jumlah_bayar)):
        beban_bunga = daftar_nilai_buku[c] * (Effective_Interest / Payment)
        daftar_beban_bunga.append(beban_bunga)

        if Nominal_interest > Effective_Interest:
            pengurangan_amortisasi = daftar_pembayaran_tunai[c+1] - daftar_beban_bunga[c+1]
            daftar_pengurangan_amortisasi.append(pengurangan_amortisasi)

            amortisasi = daftar_amortisasi[c] - daftar_pengurangan_amortisasi[c+1]
            daftar_amortisasi.append(amortisasi)

            Nilai_buku = daftar_nilai_buku[c]-daftar_pengurangan_amortisasi[c+1]
            daftar_nilai_buku.append(Nilai_buku)
        
        elif Nominal_interest < Effective_Interest:
            pengurangan_amortisasi = daftar_beban_bunga[c+1] - daftar_pembayaran_tunai[c+1]
            daftar_pengurangan_amortisasi.append(pengurangan_amortisasi)

            amortisasi = daftar_amortisasi[c] - daftar_pengurangan_amortisasi[c+1]
            daftar_amortisasi.append(amortisasi)

            Nilai_buku = daftar_nilai_buku[c] + daftar_pengurangan_amortisasi[c+1]
            daftar_nilai_buku.append(Nilai_buku)
    
    tables = {"PEMBAYARAN KE-": daftar_banyaknya_pembayaran, "PEMBAYARAN TUNAI": daftar_pembayaran_tunai, "BEBAN BUNGA": daftar_beban_bunga, "PENGURANGAN AMORTISASI": daftar_pengurangan_amortisasi, "AMORTISASI": daftar_amortisasi, "NILAI BUKU": daftar_nilai_buku}
    data = pd.DataFrame(tables)

    Konfirmasi_cetak = input("Ingin mencetak hasil (Y/N)?: ")

    tanggal_sekarang = datetime.today()
    
    if Konfirmasi_cetak == "Y":
        data.to_csv(f"Kalkulasi_Obligasi_{tanggal_sekarang}.csv")
    
    elif Konfirmasi_cetak == "N":
        print(data)
        print(" ")
        Cetak_jurnal = input("Apakah Anda ingin melihat jurnal transaksinya (Y/N)?: ")
        print(" ")
        if Cetak_jurnal == "Y":  
            rupiah_nilai_nominal = locale.currency(Face_value, grouping=True) 
            rupiah_nilai_buku = locale.currency(daftar_nilai_buku[0], grouping=True)
            rupiah_amortisasi_awal = locale.currency(daftar_amortisasi[0], grouping=True)

            daftar_rupiah_pengurangan_amortisasi = []
            for d in range(0, (Payment * Period) + 1):      
                rupiah_amortisasi = locale.currency(daftar_pengurangan_amortisasi[d], grouping=True)
                daftar_rupiah_pengurangan_amortisasi.append(rupiah_amortisasi)
            
            daftar_rupiah_beban_bunga =[]
            for e in range(0, (Payment * Period) + 1):      
                rupiah_bunga = locale.currency(daftar_beban_bunga[e], grouping=True)
                daftar_rupiah_beban_bunga.append(rupiah_bunga)

            daftar_rupiah_kas = []
            for f in range(0, (Payment * Period) + 1):      
                rupiah_kas = locale.currency(daftar_pembayaran_tunai[f], grouping=True)
                daftar_rupiah_kas.append(rupiah_kas)

            if Nominal_interest > Effective_Interest:
                print("Kas" + " " * 16 + f"{rupiah_nilai_buku}")
                print(" " * 4 + "Utang Obligasi" + " " * 8 + f"{rupiah_nilai_nominal}")    
                print(" " * 4 + "Premi Obligasi" + " " * 8 + f"{rupiah_amortisasi_awal}")
                print("\033[3m" + "(Penerbitan obligasi)" + "\033[0m")
                print(" ")
            
            elif Nominal_interest < Effective_Interest:
                print("Kas" + " " * 16 + f"{rupiah_nilai_buku}")
                print("Diskon Obligasi" + " " * 4 + f"{rupiah_amortisasi_awal}")
                print(" " * 4 + "Utang Obligasi" + " " * 8 + f"{rupiah_nilai_nominal}")    
                print("\033[3m" + "(Penerbitan obligasi)" + "\033[0m")
                print(" ")

            for g in range(1, (Period * Payment) + 1):
                print("Utang Obligasi" + " " * 5 + f"{daftar_rupiah_pengurangan_amortisasi[g]}")
                print("Beban Bunga" + " " * 8 + f"{daftar_rupiah_beban_bunga[g]}")
                print(" " * 4 + "Kas" + " " * 19 +  f"{daftar_rupiah_kas[g]}")
                print("\033[3m" + f"(Pembayaran kupon obligasi ke-{g})" + "\033[0m")
                print(" ")    
            
        elif Cetak_jurnal == "N":
            print("Baiklah :)")

#---------------------------------------------------------KALKULATOR AMORTISASI OBLIGASI METODE BUNGA EFEKTIF OLEH BADAR WIRYAWAN------------------------------------------------------------------------

print(kalkulasi_obligasi())

#---------------------------------------------------------KALKULATOR AMORTISASI OBLIGASI METODE BUNGA EFEKTIF OLEH BADAR WIRYAWAN------------------------------------------------------------------------
