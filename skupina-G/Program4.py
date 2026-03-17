import random

def izpisi_rand():
    nakljucno_stevilo = random.randint(-1000,1000) # Generiranje rendom števila med -1000 in 1000
    print(f"Naključno število: {nakljucno_stevilo}") # Izpis


izpisi_rand()  # 1. klic funkcije
izpisi_rand()  # 2. klic funkcije
izpisi_rand()  # 3. klic funkcije
