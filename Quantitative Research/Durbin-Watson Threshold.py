#------------------------------------DURBIN WATSON THRESHOLD BY BADAR WIRYAWAN-------------------------------------

import pandas as pd

#------------------------------------DURBIN WATSON THRESHOLD BY BADAR WIRYAWAN-------------------------------------

#JUMLAH MAKSIMUM OBSERVASI = 2000
#JUMLAH MAKSIMUM VARIABEL INDEPENDEN = 20
#UNTUK OBSERVASI LEBIH DARI 200 s.d. 500, BULATKAN KE KELIPATAN 10 TERDEKAT. MISAL 223 --> 220, 277 --> 280
#UNTUK OBSERVASI LEBIH DARI 500 s.d. 2000, BULATKAN KE KELIPATAN 50 TERDEKAT. MISAL 535 --> 550, 715 --> 700

Observasi = int(input("Jumlah Observasi = "))
Variabel_Independen = int(input("Jumlah Variabel Independen = "))

#------------------------------------DURBIN WATSON THRESHOLD BY BADAR WIRYAWAN-------------------------------------

data = pd.read_csv("https://docs.google.com/spreadsheets/d/1PJQrU4Z5fn9sc5aubZPKvVwkeY7sy3o2/export?format=csv")

#SUMBER: https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://wernermurhadi.files.wordpress.com/2011/07/tabel-durbin-watson.pdf&ved=2ahUKEwjKttTXzL-JAxXFoGMGHQogGfQQFnoECCIQAQ&usg=AOvVaw0a_SHb1RD8hAK-MTEj9u2v

#------------------------------------DURBIN WATSON THRESHOLD BY BADAR WIRYAWAN-------------------------------------

locate = data[(data["T"] == Observasi) & (data["K"] == Variabel_Independen + 1)].index
locate.to_list()

dL = data["dL"].iloc[locate[0]]
dU = data["dU"].iloc[locate[0]]

#------------------------------------DURBIN WATSON THRESHOLD BY BADAR WIRYAWAN-------------------------------------

print("-----------------------------------------------")
print("DURBIN-WATSON THRESHOLD (0.95 Conf. Interval)")
print(f"Observasi = {Observasi}, Variabel Independen = {Variabel_Independen}")
print(" ")
print(f"Batas bawah (dL) = {dL}")
print("Batas atas (dU)" + " " * 2 + f"= {dU}")
print("4-dU" + " " * 13 + f"= {4-dU}")
print("-----------------------------------------------")

#------------------------------------DURBIN WATSON THRESHOLD BY BADAR WIRYAWAN-------------------------------------
