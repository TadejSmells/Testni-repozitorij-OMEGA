import random
import time
while True:
    stevilo = random.randint(0,9)
    print(stevilo)
    time.sleep(1)
    if stevilo == 0:
        o = input("Ali želite zaključiti izvajanje programa? (da/ne) ").lower()
        if o == "da":
            break