################
### Naloga 5 ###
################

# Napišite program, ki od uporabnika zahteva vnos gesla.
# S ponovnim vnosom gesla nato program preveri, ali si je uporabnik geslo zapomnil.
# Program naj izpiše samo rezultat preverjanja.

g1 = input("Vnesite geslo: ")
g2 = input("Vnesite geslo še enkrat: ")

if g1 == g2:
    print("Gesli se ujemata.")
else:
    print("Gesli se ne ujemata.")