def je_prastevilo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Vnesi število: "))
prastevila = list(filter(je_prastevilo, range(2, n + 1)))
print("Praštevila:", prastevila)