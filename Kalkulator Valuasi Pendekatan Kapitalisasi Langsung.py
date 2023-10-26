#-------------KALKULATOR VALUASI PENDEKATAN KAPITALISASI LANGSUNG OLEH BADAR WIRYAWAN---------------


import locale

#-------------KALKULATOR VALUASI PENDEKATAN KAPITALISASI LANGSUNG OLEH BADAR WIRYAWAN---------------

locale.setlocale(locale.LC_ALL, "id_ID")
Net_Income = float(input("Masukkan Pendapatan: "))
Capitalization_Rate = float(input("Masukkan Keuntungan yang Diharapkan: "))

#-------------KALKULATOR VALUASI PENDEKATAN KAPITALISASI LANGSUNG OLEH BADAR WIRYAWAN---------------

def pendapatan_kapitalisasi_langsung(Pendapatan=Net_Income, Tingkat_Keuntungan=Capitalization_Rate):
    return Pendapatan / Tingkat_Keuntungan

#-------------KALKULATOR VALUASI PENDEKATAN KAPITALISASI LANGSUNG OLEH BADAR WIRYAWAN---------------
  
Nominal_dalam_rupiah = locale.currency(pendapatan_kapitalisasi_langsung(), grouping=True)

#-------------KALKULATOR VALUASI PENDEKATAN KAPITALISASI LANGSUNG OLEH BADAR WIRYAWAN---------------

print(Nominal_dalam_rupiah)

#-------------KALKULATOR VALUASI PENDEKATAN KAPITALISASI LANGSUNG OLEH BADAR WIRYAWAN---------------

    
