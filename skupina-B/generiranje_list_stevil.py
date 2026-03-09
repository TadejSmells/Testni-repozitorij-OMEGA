from random import randint

def generate_random_numbers(n, lower, upper):
    random_numbers = []
    for _ in range(n):
        random_number = randint(lower, upper)
        random_numbers.append(random_number)
    return random_numbers


n = int(input("Vpiši število naključnih števil, ki jih želiš generirati: "))
lower = int(input("Vpiši spodno mejo števil: "))
upper = int(input("Vpiši zgornjo mejo števil: "))
random_numbers = generate_random_numbers(n, lower, upper)
print(random_numbers)