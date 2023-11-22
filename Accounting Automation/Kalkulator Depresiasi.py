#Program ini memerlukan library Pandas, install dengan command "pip install pandas"




#---------------------------------------------------------KALKULATOR DEPRESIASI OLEH BADAR WIRYAWAN-----------------------------------------------------------

import pandas as pd

Nilai_aset = float(input("Masukkan nilai perolehan aset: "))
Nilai_residu = float(input("Masukkan nilai residu aset: "))
Masa_manfaat = int(input("Masukkan estimasi masa manfaat aset: "))
Metode_Depresiasi = input("Pilih Metode Depresiasi (Garis Lurus = 1, Jumlah Digit Tahun = 2, Penurunan Berganda = 3): ")

#---------------------------------------------------------KALKULATOR DEPRESIASI OLEH BADAR WIRYAWAN-----------------------------------------------------------

def depresiasi_garis_lurus(Acquisition_Cost = Nilai_aset, Residual_Cost = Nilai_residu, Useful_life = Masa_manfaat):

    #KOLOM 01

    daftar_tahun = []

    for a in range(Useful_life+1):
        daftar_tahun.append(a)

    #KOLOM 02

    daftar_beban_depresiasi = [0]

    beban_depresiasi = (Acquisition_Cost - Residual_Cost) / Useful_life

    for b in range(Useful_life):
        daftar_beban_depresiasi.append(beban_depresiasi)

    #KOLOM 03

    daftar_akumulasi_depresiasi = [0, daftar_beban_depresiasi[1]]

    for c in range (Useful_life-1):
        akumulasi_depresiasi = daftar_akumulasi_depresiasi[c+1] + daftar_beban_depresiasi[c+2]
        daftar_akumulasi_depresiasi.append(akumulasi_depresiasi)

    #KOLOM 04

    daftar_nilai_buku = [Acquisition_Cost]

    for d in range(Useful_life):
        nilai_buku_baru = daftar_nilai_buku[d] - daftar_beban_depresiasi[d+1]
        daftar_nilai_buku.append(nilai_buku_baru)

    tables = {"TAHUN": daftar_tahun,
              "BEBAN DEPRESIASI": daftar_beban_depresiasi,
              "AKUMULASI DEPRESIASI": daftar_akumulasi_depresiasi,
              "NILAI BUKU": daftar_nilai_buku}
    data = pd.DataFrame(tables)

    Konfirmasi_Cetak = input("Ingin Mencetak Hasil (Y/N)?: ")
    if Konfirmasi_Cetak == "Y":
        data.to_csv("Kalkulasi_Depresiasi_Garis_Lurus.csv")
    elif Konfirmasi_Cetak == "N":
        print(data)

        Konfirmasi_Cetak = input("Apakah Anda ingin mencetaknya kali ini (Y/N)?: ")

        if Konfirmasi_Cetak == "Y":
            data.to_csv("Kalkulasi_Depresiasi_Garis_Lurus.csv")
        elif Konfirmasi_Cetak == "N":
            print("Baiklah :)")

#---------------------------------------------------------KALKULATOR DEPRESIASI OLEH BADAR WIRYAWAN-----------------------------------------------------------

def depresiasi_sum_of_year_digits(Acquisition_Cost = Nilai_aset, Residual_Cost = Nilai_residu, Useful_life = Masa_manfaat):

    #KOLOM 01

    daftar_tahun = []

    for a in range(Useful_life+1):
        daftar_tahun.append(a)

    #KOLOM 02

    daftar_basis_depresiasi = [0]

    for b in range(Useful_life):
        basis_depresiasi = ((Acquisition_Cost - Residual_Cost) / Useful_life) * Useful_life
        daftar_basis_depresiasi.append(basis_depresiasi)

    #KOLOM 03

    daftar_sisa_masa_manfaat = [0]

    for c in range(Useful_life):
        sisa_masa_manfaat = daftar_tahun[Useful_life - c]
        daftar_sisa_masa_manfaat.append(sisa_masa_manfaat) 

    #KOLOM 04

    daftar_faktor_depresiasi = [0]
    sum_of_digits = sum(daftar_sisa_masa_manfaat)

    for d in range(Useful_life):
        faktor_depresiasi = daftar_sisa_masa_manfaat[d + 1] / sum_of_digits
        daftar_faktor_depresiasi.append(faktor_depresiasi)

    #KOLOM 05

    daftar_beban_depresiasi = [0]

    for e in range(Useful_life):
        beban_depresiasi = daftar_basis_depresiasi[e + 1] * daftar_faktor_depresiasi[e + 1]
        daftar_beban_depresiasi.append(beban_depresiasi)

    #KOLOM 06

    daftar_akumulasi_depresiasi = [0]

    Dummy_akumulasi = 0
    for f in range(Useful_life):
        Dummy_akumulasi += daftar_beban_depresiasi[f+1]
        daftar_akumulasi_depresiasi.append(Dummy_akumulasi)

    #KOLOM 07

    daftar_nilai_buku = [Acquisition_Cost]

    for g in range(Useful_life):
        nilai_buku = daftar_nilai_buku[g]-daftar_beban_depresiasi[g+1]
        daftar_nilai_buku.append(nilai_buku)

    tables = {"TAHUN": daftar_tahun, 
              "BASIS DEPRESIASI": daftar_basis_depresiasi, 
              "SISA MASA MANFAAT": daftar_sisa_masa_manfaat,
              "FAKTOR DEPRESIASI": daftar_faktor_depresiasi, 
              "BEBAN DEPRESIASI": daftar_beban_depresiasi, 
              "AKUMULASI DEPRESIASI": daftar_akumulasi_depresiasi, 
              "NILAI BUKU": daftar_nilai_buku}
    data = pd.DataFrame(tables)

    Konfirmasi_Cetak = input("Ingin Mencetak Hasil (Y/N)?: ")
    if Konfirmasi_Cetak == "Y":
        data.to_csv("Kalkulasi_Depresiasi_Sum_Of_Year_Digits.csv")
    elif Konfirmasi_Cetak == "N":
        print(data)

        Konfirmasi_Cetak = input("Apakah Anda ingin mencetaknya kali ini (Y/N)?: ")

        if Konfirmasi_Cetak == "Y":
            data.to_csv("Kalkulasi_Depresiasi_Sum_Of_Year_Digits.csv")
        elif Konfirmasi_Cetak == "N":
            print("Baiklah :)")

#---------------------------------------------------------KALKULATOR DEPRESIASI OLEH BADAR WIRYAWAN-----------------------------------------------------------

def depresiasi_double_declining_balance(Acquisition_Cost = Nilai_aset, Residual_Cost = Nilai_residu, Useful_life = Masa_manfaat):

    #KOLOM 01

    daftar_tahun = []

    for a in range(Useful_life+1):
        daftar_tahun.append(a)

    #KOLOM 02

    daftar_faktor_declining = [0]

    for b in range(Useful_life): 
        faktor_declining = 2 * ((Acquisition_Cost - Residual_Cost) / Useful_life) / (((Acquisition_Cost - Residual_Cost) / Useful_life) * Useful_life)
        daftar_faktor_declining.append(faktor_declining)

    #KOLOM 03, 04, 05

    daftar_beban_depresiasi = [0]
    daftar_akumulasi_depresiasi = [0]
    daftar_nilai_buku = [Acquisition_Cost]
    
    for c in range(Useful_life):
        beban_depresiasi = daftar_nilai_buku[c] * daftar_faktor_declining[c+1]
        daftar_beban_depresiasi.append(beban_depresiasi)

        Dummy_akumulasi = daftar_akumulasi_depresiasi[c]
        Dummy_akumulasi += daftar_beban_depresiasi[c + 1]
        daftar_akumulasi_depresiasi.append(Dummy_akumulasi)

        Nilai_buku_baru = daftar_nilai_buku[c] - daftar_beban_depresiasi[c + 1]
        daftar_nilai_buku.append(Nilai_buku_baru)

    tables = {"TAHUN": daftar_tahun, 
              "FAKTOR DECLINING": daftar_faktor_declining, 
              "BEBAN DEPRESIASI": daftar_beban_depresiasi, 
              "AKUMULASI DEPRESIASI": daftar_akumulasi_depresiasi, 
              "NILAI BUKU": daftar_nilai_buku}
    data = pd.DataFrame(tables)

    check_for_excess = (data["NILAI BUKU"] < Residual_Cost).sum()

    if check_for_excess > 0:
        locate_excess_depreciation = data["NILAI BUKU"] < Residual_Cost
        data_clearing = data[~locate_excess_depreciation]

        tables_new = {"TAHUN": data_clearing["TAHUN"], 
                      "FAKTOR DECLINING": data_clearing["FAKTOR DECLINING"], 
                      "BEBAN DEPRESIASI": data_clearing["BEBAN DEPRESIASI"], 
                      "AKUMULASI DEPRESIASI": data_clearing["AKUMULASI DEPRESIASI"],
                      "NILAI BUKU": data_clearing["NILAI BUKU"]}
        data_new = pd.DataFrame(tables_new)

        to_add_tahun = data_new["TAHUN"].iloc[-1] + 1
        to_add_nilai_buku = Residual_Cost
        to_add_beban_depresiasi = data_new["NILAI BUKU"].iloc[-1] - Residual_Cost
        to_add_faktor_declining = [0]
        to_add_akumulasi_depresiasi = data_new["AKUMULASI DEPRESIASI"].iloc[-1] + data_new["BEBAN DEPRESIASI"].iloc[-1]

        tables_correction = {"TAHUN": to_add_tahun, 
                             "FAKTOR DECLINING": to_add_faktor_declining,
                             "BEBAN DEPRESIASI": to_add_beban_depresiasi,
                             "AKUMULASI DEPRESIASI": to_add_akumulasi_depresiasi,
                             "NILAI BUKU": to_add_nilai_buku}
        data_fix = pd.DataFrame(tables_correction)

        data_final = pd.concat([data_new, data_fix], ignore_index=True)
        data_final["FAKTOR DECLINING"].iloc[-1] = data_final["BEBAN DEPRESIASI"].iloc[-1] / data_final["NILAI BUKU"].iloc[-2]

        Konfirmasi_Cetak = input("Ingin Mencetak Hasil (Y/N)?: ")
        if Konfirmasi_Cetak == "Y":
            data_final.to_csv("Kalkulasi_Depresiasi_Double_Declining_Balance.csv")
        elif Konfirmasi_Cetak == "N":
            print(data_final)

            Konfirmasi_Cetak = input("Apakah Anda ingin mencetaknya kali ini (Y/N)?: ")

            if Konfirmasi_Cetak == "Y":
                data_final.to_csv("Kalkulasi_Depresiasi_Double_Declining_Balance.csv")
            elif Konfirmasi_Cetak == "N":
                print("Baiklah :)")
    
    else:
        Konfirmasi_Cetak = input("Ingin Mencetak Hasil (Y/N)?: ")
        if Konfirmasi_Cetak == "Y":
            data.to_csv("Kalkulasi_Depresiasi_Double_Declining_Balance.csv")
        elif Konfirmasi_Cetak == "N":
            print(data)

            Konfirmasi_Cetak = input("Apakah Anda ingin mencetaknya kali ini (Y/N)?: ")

            if Konfirmasi_Cetak == "Y":
                data.to_csv("Kalkulasi_Depresiasi_Double_Declining_Balance.csv")
            elif Konfirmasi_Cetak == "N":
                print("Baiklah :)")

#---------------------------------------------------------KALKULATOR DEPRESIASI OLEH BADAR WIRYAWAN-----------------------------------------------------------

if Metode_Depresiasi == "1":
    print(depresiasi_garis_lurus())
elif Metode_Depresiasi == "2":
    print(depresiasi_sum_of_year_digits())
elif Metode_Depresiasi == "3":
    print(depresiasi_double_declining_balance()) 
 
#---------------------------------------------------------KALKULATOR DEPRESIASI OLEH BADAR WIRYAWAN-----------------------------------------------------------
