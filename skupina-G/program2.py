import random
gesla = ["geslo1", "geslo2", "geslo3"]
while True:
    nakljucno_geslo = random.choice(gesla)
    vnos = input(f"Vnesite geslo '{nakljucno_geslo}': ")
    if vnos == nakljucno_geslo:
        print("Geslo ste vnesli pravilno! ")
        break
    else:
        print("Geslo ste vnesli napačno. ")