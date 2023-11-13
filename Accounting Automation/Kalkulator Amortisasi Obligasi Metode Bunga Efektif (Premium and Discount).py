#Program ini memerlukan library Pandas, install dengan "pip install pandas"
#Hanya dapat digunakan di obligasi premium atau diskon.



#---------------------------------------------------------KALKULATOR AMORTISASI OBLIGASI METODE BUNGA EFEKTIF OLEH BADAR WIRYAWAN------------------------------------------------------------------------

import pandas as pd

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
    daftar_amortisasi = [0]
    
    PV_Factor = 1 / ((1 + (Effective_Interest / Payment)) ** (jumlah_bayar))
    PV_Annuity_Factor = (1 - PV_Factor)/(Effective_Interest / Payment)

    Nilai_buku_awal = (Face_value * PV_Factor) + (Face_value * (Nominal_interest / Payment) * PV_Annuity_Factor)
        
    daftar_nilai_buku = [Nilai_buku_awal]

    for c in range(0, (jumlah_bayar)):
        beban_bunga = daftar_nilai_buku[c] * (Effective_Interest / Payment)
        daftar_beban_bunga.append(beban_bunga)

        if Nominal_interest > Effective_Interest:
            amortisasi = daftar_pembayaran_tunai[c+1] - daftar_beban_bunga[c+1]
            daftar_amortisasi.append(amortisasi)

            Nilai_buku = daftar_nilai_buku[c]-daftar_amortisasi[c+1]
            daftar_nilai_buku.append(Nilai_buku)
        
        elif Nominal_interest < Effective_Interest:
            amortisasi = daftar_beban_bunga[c+1] - daftar_pembayaran_tunai[c+1]
            daftar_amortisasi.append(amortisasi)

            Nilai_buku = daftar_nilai_buku[c] + daftar_amortisasi[c+1]
            daftar_nilai_buku.append(Nilai_buku)
    
    tables = {"PEMBAYARAN KE-": daftar_banyaknya_pembayaran, "PEMBAYARAN TUNAI": daftar_pembayaran_tunai, "BEBAN BUNGA": daftar_beban_bunga, "AMORTISASI": daftar_amortisasi, "NILAI BUKU": daftar_nilai_buku}
    data = pd.DataFrame(tables)

    Konfirmasi_cetak = input("Ingin mencetak hasil (Y/N)?: ")
    if Konfirmasi_cetak == "Y":
        data.to_csv("Kalkulasi_Obligasi.csv")
    
    elif Konfirmasi_cetak == "N":
        print(data)

#---------------------------------------------------------KALKULATOR AMORTISASI OBLIGASI METODE BUNGA EFEKTIF OLEH BADAR WIRYAWAN------------------------------------------------------------------------

print(kalkulasi_obligasi())

#---------------------------------------------------------KALKULATOR AMORTISASI OBLIGASI METODE BUNGA EFEKTIF OLEH BADAR WIRYAWAN------------------------------------------------------------------------
