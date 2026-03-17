import random

def izpisi_rand5():
    nakljucno_stevilo = random.randint(1, 10)# Generiramo naključno0 število med 1 in 10

    if 1 <= nakljucno_stevilo <= 5: # Pogoj če je med 1 in 5
        print(f"Naključno število je med 1 in 5: {nakljucno_stevilo}") # Izpis če je med 1 in 5
    elif 6 <= nakljucno_stevilo <= 10:  # Pogoj če je med 6 in 10
        print(f"Naključno število je med 6 in 10: {nakljucno_stevilo}") # Izpis če je med 6 in 10


izpisi_rand5()  # 1. klic funkcije
izpisi_rand5()  # 2. klic funkcije



