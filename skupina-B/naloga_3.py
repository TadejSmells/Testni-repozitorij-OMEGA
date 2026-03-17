from random import randint

a = int(input("Vnesi prvo število: "))
b = int(input("Vnesi drugo število: "))
c = int(input("Vnesi tretje število: "))

sortirana_stevila = [a, b ,c]
sortirana_stevila.sort()

nakljucno_stevilo = randint(sortirana_stevila[0], sortirana_stevila[2])

print("Debug: ", nakljucno_stevilo)
print("Razlika med številoma je: ", nakljucno_stevilo - sortirana_stevila[1])