#3.8

visina = int(input("Vnesi višino piramide: "))

for i in range(1, visina + 1):
    prostor = visina - i
    znak = 2 * i - 1
    print(" " * prostor + "*" * znak)