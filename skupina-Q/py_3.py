#4.3

barve = [None] * 3

for i in range(3):
    barva = input(f"Vnesite {i + 1}. najljubšo barvo (če želite končati program pritisnite Enter): ")
    if barva == "":
        break
    barve[i] = barva

print("-- Vaše najljubše barve --")
for b in barve:
    if b is not None:
        print(b)