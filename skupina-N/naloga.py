pomidori_vnos=int(input("vnesite količino pomidora: "))
zelje_vons=int(input("vnesite količino zelja!: "))
kiwi_vnos=int(input("vnesite količino kwija: "))

if(0<pomidori_vnos<5):
    print("cena je 3€ na kg: ",pomidori_vnos*3)
elif(5<pomidori_vnos<15):
    print("cena je 2.5€ na kg: ",pomidori_vnos*2.5)
elif(pomidori_vnos>15):
    print("cena je 1€ na kg",pomidori_vnos)
else:
    print("vnesli ste napacno kolicino")