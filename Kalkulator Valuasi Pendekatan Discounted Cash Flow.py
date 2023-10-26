#-------------------KALKULATOR VALUASI PENDEKATAN DISCOUNTED CASH FLOW OLEH BADAR WIRYAWAN------------------


import locale

#-------------------KALKULATOR VALUASI PENDEKATAN DISCOUNTED CASH FLOW OLEH BADAR WIRYAWAN------------------

locale.setlocale(locale.LC_ALL, "id_ID")
Net_Income = float(input("Masukkan Pendapatan: "))
Discount_Rate = float(input("Masukkan Tingkat Diskonto: "))
Periods = int(input("Masukkan Lamanya Tahun: "))

#-------------------KALKULATOR VALUASI PENDEKATAN DISCOUNTED CASH FLOW OLEH BADAR WIRYAWAN------------------

def pendekatan_discounted_cash_flow(Pendapatan=Net_Income, Tingkat_Diskonto=Discount_Rate, Periode=Periods):
    Nilai = 0
    for n in range(1, Periode + 1):
        Nilai += Pendapatan *  (1 / ((1 + Tingkat_Diskonto) ** n))
    return Nilai

#-------------------KALKULATOR VALUASI PENDEKATAN DISCOUNTED CASH FLOW OLEH BADAR WIRYAWAN------------------

Nominal_dalam_rupiah = locale.currency(pendekatan_discounted_cash_flow(), grouping=True)

#-------------------KALKULATOR VALUASI PENDEKATAN DISCOUNTED CASH FLOW OLEH BADAR WIRYAWAN------------------

print(Nominal_dalam_rupiah)

#-------------------KALKULATOR VALUASI PENDEKATAN DISCOUNTED CASH FLOW OLEH BADAR WIRYAWAN------------------

     
    
    
    