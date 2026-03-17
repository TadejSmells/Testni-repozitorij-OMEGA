besedilo = input("Vnesi besedilo: ")

if besedilo == "":
    print("")
elif len(besedilo) < 8:
    print("************")
else:
    dolzina = len(besedilo)
    if dolzina < 12:
        dolzina = 12
    print("+" * dolzina)

 

