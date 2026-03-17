from random import randint, shuffle
def naloga (vprasanje, pravodg, napodg):
    print(vprasanje)
    odgovori = ["", "", "", ""]
    temp = randint(0, 3)
    odgovori[temp] = pravodg[0]
    shuffle(napodg)
    j = 0
    for i in range (len(odgovori)):
        if odgovori[i] == "":
            odgovori[i] = napodg[j]
            j += 1
        print(f"{i + 1}) {odgovori[i]}")
    vnos = 5
    while vnos > 3:
        vnos = int(input("napiši pravilen odgovor [1 - 4]")) - 1
    if odgovori[vnos] == pravodg[0]:
        print("bravo")
        print("   ")
        print("   ")
        print("   ")
        print("   ")
        return(1)
    else:
        print("napacno")
        print("pravilen odgovor je: " + pravodg[0])
        print("   ")
        print("   ")
        print("   ")
        print("   ")
        return(0)
tocke = 0
#naloga 1.1
nal1 = "Katera teorija prava kot osrednjo prvino prava izpostavlja vrednote in med njimi pravičnost?"
odg1 = ["naravopravne teorije"]
drugo1 = ["Pravni pozitivizem", "Sociološka teorija prava", "Realistična teorija prava"]
tocke = tocke + naloga (nal1, odg1, drugo1)
print("tvoje stevilo tock: ", tocke)

#naloga 1.2
nal1_2 = "Za katero teorijo prava je značilno, da subjektom, ki predpise uporabljajo (po uradni dolžnosti) in njihovi razlagi pomena predpisov (»law in action«) pripisuje večji pomen kot samim predpisom (»law in books«)?"
odg1_2 = ["Sociološke teorije"]
drugo1_2 = ["Naravnopravne torije", "Pravni pozitivezem", "Normativna teorija prava"]
tocke = tocke + naloga (nal1_2, odg1_2, drugo1_2)
print("tvoje stevilo tock: ", tocke)

#naloga 1.3
nal1_3 = "Na kratko opišite temeljne razlike med predmodernim in modernim oz. sodobnim pravom? "
odg1_3 = ["predmoderno pravo: zadrobljenost pravnih virov, pravno utrjena neenakost, prežetost z religijo, krute kazni za širok nabor kaznivih dejanj... Moderno pravo: splošnost, formalizem, racionalnost, abstraktnost, sistematičnost, načelo pravne države oz. vladavine prava, sekularnost"]
drugo1_3 = [
"Predmoderno pravo: splošnost pravnih pravil, racionalnost, abstraktnost in sistematičnost, ločitev prava od religije... Moderno pravo: zadrobljenost pravnih virov, močna povezanost z religijo, pravno utrjena neenakost in uporaba krutih telesnih kazni.", 
"Predmoderno pravo: temeljilo je na načelu pravne države, formalizmu in enakosti vseh pred zakonom... Moderno pravo: zaznamujejo ga običajno pravo, lokalna pravila, religiozne norme ter odsotnost sistematične zakonodaje.",
"Predmoderno pravo: racionalno kodificirano, abstraktno in sekularno, z razvitim sistemom človekovih pravic... Moderno pravo: osebno, nesistematično, odvisno od tradicije, verskih zapovedi in samovolje oblasti."
]
tocke = tocke + naloga (nal1_3, odg1_3, drugo1_3)
print("tvoje stevilo tock: ", tocke)

#nal 1.4
nal1_4 = "Katere specifične značilnosti lahko pripišemo zgodovinsko izoblikovanemu tipu prava, ki je značilen za moderno dobo?"
odg1_4 = ["Racionalnost, splošnost, abstraktnost, sistematičnost, formalizem."]
drugo1_4 = [
"Religioznost, običajnost, lokalna veljavnost, osebna oblast vladarja, nepisanost prava",
"Zadrobljenost pravnih virov, pravno utrjena neenakost, telesne kazni, povezanost z božjim pravom, odsotnost kodifikacije",
"Samovoljnost oblasti, prevlada tradicije nad zakonom, partikularnost pravil, vezanost na moralne in verske zapovedi, nesistematičnost"
]
tocke = tocke + naloga (nal1_4, odg1_4, drugo1_4)
print("tvoje stevilo tock: ", tocke)

#nal 2
nal2 = "V čem oz. na kakšen način se kaže sistematičnost kot značilnost modernega/sodobnega prava?"
odg2 = ["moderna pravo ima obliko hierarhicnega sistema pravnih pravil in pravnih aktov"]
drugo2 = ["moderna pravo nima oblike hierarhicnega sistema pravnih pravil in pravnih aktov", "V višini kazni", "V barvi uradnih listin"]
tocke = tocke + naloga(nal2, odg2, drugo2)
print("tvoje stevilo tock: ", tocke)

#nal 3
nal3 = "Kako bi na kratko opredelili pojem pravnega reda?"
odg3 = ["skupek dejansko obstojočih pravnih pravil, pravnih aktov in pravnih razmerij, ki se permanentno obnavlja oz. spreminja in razvija, imenujemo pravni red"]
drugo3 = ["Skupek političnih strank", "Seznam kazni", "Zbirka sodnih stavb"]
tocke = tocke + naloga(nal3, odg3, drugo3)
print("tvoje stevilo tock: ", tocke)

#nal 4
nal4 = "Kaj je pravni akt?"
odg4 = ["človekova zavestna dejanja/oblike v katerih nastajajo pravna pravila"]
drugo4 = ["Vsaka sodna razprava", "Politični govor", "Mnenje državljanov"]
tocke = tocke + naloga(nal4, odg4, drugo4)
print("tvoje stevilo tock: ", tocke)

#nal 5.1
nal5_1 = "Kateri pravni akti so splošni oblastni pravni akti?"
odg5_1 = ["zakoni, predisi, ustava, uredba..."]
drugo5_1 = ["Pogodbe", "Oporoke", "Računi"]
tocke = tocke + naloga(nal5_1, odg5_1, drugo5_1)
print("tvoje stevilo tock: ", tocke)

#nal 5.2
nal5_2 = "Kateri pravni akti so posamični oblastni pravni akti?"
odg5_2 = ["upravna odločba, upravni akti, sodni akti, pravni posli..."]
drugo5_2 = ["Zakoni", "Uredbe", "Statuti"]
tocke = tocke + naloga(nal5_2, odg5_2, drugo5_2)
print("tvoje stevilo tock: ", tocke)

#nal 5.3
nal5_3 = "Kateri pravni akti so splošni neoblastni pravni akti?"
odg5_3 = ["Statuti, kolektivne pogodbe..."]
drugo5_3 = ["Sodne odločbe", "Upravne odločbe", "Kazni"]
tocke = tocke + naloga(nal5_3, odg5_3, drugo5_3)
print("tvoje stevilo tock: ", tocke)

#nal 5.4
nal5_4 = "Kateri pravni akti so posamični neoblastni pravni akti?"
odg5_4 = ["Individualna pogodba, oporoka, odločba organizacije, odpoved delovnega razmerja..."]
drugo5_4 = ["Zakoni", "Uredbe", "Odloki"]
tocke = tocke + naloga(nal5_4, odg5_4, drugo5_4)
print("tvoje stevilo tock: ", tocke)

#nal 5.5
nal5_5 = "Za katere izmed omenjenih skupin pravnih aktov se uporablja izraz avtonomni predpisi?"
odg5_5 = ["Za splošne neoblastne pravne akte"]
drugo5_5 = ["Za kazenske zakone", "Za ustavo", "Za sodbe"]
tocke = tocke + naloga(nal5_5, odg5_5, drugo5_5)
print("tvoje stevilo tock: ", tocke)

#nal 6
nal6 = "Kaj ureja Kazenski zakonik RS?"
odg6 = ["Ureja kazniva dejanja in sankcije za le te opredeljuje kazniva dejanja"]
drugo6 = ["Prometna pravila", "Davčne obveznosti", "Šolski sistem"]
tocke = tocke + naloga(nal6, odg6, drugo6)
print("tvoje stevilo tock: ", tocke)

#nal 7
nal7 = "Kateri zakon ureja načine nastanka civilnopravne obveznosti in vrste pogodb?"
odg7 = ["Ovligacijski zakonik"]
drugo7 = ["Kazenski zakonik", "Ustava RS", "Zakon o volitvah"]
tocke = tocke + naloga(nal7, odg7, drugo7)
print("tvoje stevilo tock: ", tocke)

#nal 8
nal8 = "Kateri predpis ureja zakonodajni postopek?"
odg8 = ["Zakon o kazenskem postopku ZKP"]
drugo8 = ["Kazenski zakonik", "Občinski odlok", "Pravilnik o šolah"]
tocke = tocke + naloga(nal8, odg8, drugo8)
print("tvoje stevilo tock: ", tocke)

#nal 9.1
nal9_1 = "Kaj ureja Zakon o prekrških?"
odg9_1 = ["Splošne pogoje za predpisovanje prekrškov in sankcij zanje, splošne pogoje za odgovornost za prekrške, za izrekanje in za izvršitev sankcij za prekrške ter organe in sodišča za odločanje o prekrških"]
drugo9_1 = ["Kazniva dejanja", "Volitve", "Mednarodne pogodbe"]
tocke = tocke + naloga(nal9_1, odg9_1, drugo9_1)
print("tvoje stevilo tock: ", tocke)

#nal 9.2
nal9_2 = "S katerimi predpisi se lahko določijo prekrški?"
odg9_2 = ["Z zakonom, uredbo vlade RS in odlokom samoupravne lokalne skupnosti"]
drugo9_2 = ["Samo z ustavo", "Samo s sodbami", "Samo z resolucijami"]
tocke = tocke + naloga(nal9_2, odg9_2, drugo9_2)
print("tvoje stevilo tock: ", tocke)

#nal 10
nal10 = "Kako se s tujko imenuje prevzem mednarodne pogodbe v notranji pravni red?"
odg10 = ["Ratifikacija"]
drugo10 = ["Interpelacija", "Amnestija", "Kvorum"]
tocke = tocke + naloga(nal10, odg10, drugo10)
print("tvoje stevilo tock: ", tocke)

#nal 11.1
nal11_1 = "Kako je zagotovljena participacija državljanov v sodni veji oblasti?"
odg11_1 = ["S sodniki porotniki kot predstavniki ljudstva"]
drugo11_1 = ["Z referendumom", "Z volitvami ministrov", "Z imenovanjem poslancev"]
tocke = tocke + naloga(nal11_1, odg11_1, drugo11_1)
print("tvoje stevilo tock: ", tocke)

#nal 11.2
nal11_2 = "Ali pravni sistem RS pozna poroto?"
odg11_2 = ["Da, Pozna sodnike porotnike"]
drugo11_2 = ["Pozna samo poroto", "Pozna le sodnike brez laikov", "Pozna izključno vojaško poroto"]
tocke = tocke + naloga(nal11_2, odg11_2, drugo11_2)
print("tvoje stevilo tock: ", tocke)

#nal 12.1
nal12_1 = "O katerih zadevah sodišča odločajo v pravdnem postopku?"
odg12_1 = ["O varstvu pravic civilnega prava, ki ga obvaduje načelo avtonomije strank"]
drugo12_1 = ["O kaznivih dejanjih", "O volitvah", "O zakonih"]
tocke = tocke + naloga(nal12_1, odg12_1, drugo12_1)
print("tvoje stevilo tock: ", tocke)

#nal 12.2
nal12_2 = "Navedite dve zadevi nepravdnega postopka."
odg12_2 = ["Odločitev o dediščini, izvedba razglasitve pogrešane osebe za mrtvo, razdelitev skupnega premoženja med zakoncema"]
drugo12_2 = ["Kaznovanje storilcev", "Volitve", "Zakonodajni postopek"]
tocke = tocke + naloga(nal12_2, odg12_2, drugo12_2)
print("tvoje stevilo tock: ", tocke)

#nal 12.3
nal12_3 = "Kako se imenuje postopek za odvzem poslovne sposobnosti?"
odg12_3 = ["nepravdni postopek"]
drugo12_3 = ["Kazenski postopek", "Upravni spor", "Volilni postopek"]
tocke = tocke + naloga(nal12_3, odg12_3, drugo12_3)
print("tvoje stevilo tock: ", tocke)

#nal 13
nal13 = "Katere vrste pravnih kršitev bi storil 21-letni uslužbenec, ki bi si protipravno prilastil računalnik, ki je last njegovega delodajalca?"
odg13 = ["kaznivo dejanje, disciplinski postopek, civilni delikt"]
drugo13 = ["Prometni prekršek", "Davčni prekršek", "Volilni prekršek"]
tocke = tocke + naloga(nal13, odg13, drugo13)
print("tvoje stevilo tock: ", tocke)

#nal 14
nal14 = "Katere vrste pravne odgovornosti bi moral prevzeti 21-letni uslužbenec, ki bi si protipravno prilastil računalnik, ki je last njegovega delodajalca?"
odg14 = ["(subjektivno) kazensko odgovornost, disciplinsko odgovornost in odškodninsko odgovornost"]
drugo14 = ["samo odškodninsko odgovornost", "samo disciplinsko odgovornost", "odškodninsko in kazensko odgovornost"]
tocke = tocke + naloga(nal14, odg14, drugo14)
print("tvoje stevilo tock: ", tocke)

#nal 15
nal15 = "Kazenski zakonik v prvem odstavku 115. člena določa, da se tisti, ki komu vzame življenje, kaznuje z zaporom od 5 do 15 let. Za katero vrsto pravnega pravila gre v tem primeru?"
odg15 = ["Splošno in abstraktno pravno pravilo"]
drugo15 = ["Moralno pravilo", "Tehnično pravilo", "Versko pravilo"]
tocke = tocke + naloga(nal15, odg15, drugo15)
print("tvoje stevilo tock: ", tocke)

#nal 16
nal16 = "Kateri pravni akt oz. predpis je v hierarhiji pravnih aktov v RS v rangu ustave?"
odg16 = ["Ustavni zakon"]
drugo16 = ["Zakon", "Uredba", "Odlok"]
tocke = tocke + naloga(nal16, odg16, drugo16)
print("tvoje stevilo tock: ", tocke)

#nal 17
nal17 = "Kateri pravni akt oz. predpis je v hierarhiji pravnih aktov v RS pod ustavo in nad zakoni?"
odg17 = ["Ratificiranje mednarodne pogodbe"]
drugo17 = ["Občinski odlok", "Sodba", "Pravilnik"]
tocke = tocke + naloga(nal17, odg17, drugo17)
print("tvoje stevilo tock: ", tocke)

#nal 18
nal18 = "Navedi dva primera pravnih aktov, ki sta avtonomna predpisa."
odg18 = ["Statuti, koletkivne pogodbe"]
drugo18 = ["Kazenski zakonik, koletkivne pogodbe", "Ustava, statuti", "Mednarodna pogodba, notarni dopis"]
tocke = tocke + naloga(nal18, odg18, drugo18)
print("tvoje stevilo tock: ", tocke)

#nal 19
nal19 = "Naštej vrste sankcij, ki jih v slovenskem pravnem redu sodišče lahko izreče storilcem kaznivih dejanj."
odg19 = ["Kazni, opozorilne sankcije, varnostni ukrepi, alternativne sankcije, vzgojni ukrepi za mladoletne storilce (KZ 1994)"]
drugo19 = ["Volitve, vzgojni ukrepi za mladoletne storilce (KZ 1994)", "Kazni, opozorilne sankcije, Nagrade", "Štipendije, opozorilne sankcije, varnostni ukrepi, Nagrade"]
tocke = tocke + naloga(nal19, odg19, drugo19)
print("tvoje stevilo tock: ", tocke)

#nal 20.1
nal20_1 = "Naštej vrste kazni, ki se v slovenskem pravnem redu lahko izrečejo odgovornim storilcem kaznivih dejanj."
odg20_1 = ["Zaporna kazen, denarna kazen, prepoved vožnje motornega vozila, izgon tujca iz države, prepoved opravljanja poklica, odvzem predmetov, hišni pripor"]
drugo20_1 = ["Šolski ukrepi", "Upravne takse", "Prometne table"]
tocke = tocke + naloga(nal20_1, odg20_1, drugo20_1)
print("tvoje stevilo tock: ", tocke)

#nal 20.2
nal20_2 = "Naštej vrste opozorilnih sankcij, ki se v slovenskem pravnem redu odgovornim storilcem kaznivih dejanj lahko izrečejo namesto kazni."
odg20_2 = ["Pogojna obsodba, pogojna obsodba z varstvenim nadzorstvom, sodni opomin"]
drugo20_2 = [
"Zaporna kazen, denarna kazen, delo v splošno korist",
"Varnostni ukrepi, hišni pripor, pripor",
"Kazni za prekrške, upravne globe, disciplinske sankcije"
]
tocke = tocke + naloga(nal20_2, odg20_2, drugo20_2)
print("tvoje stevilo tock: ", tocke)

#nal 20.3
nal20_3 = "Za katera kazniva dejanja in pod katerimi pogoji se lahko izreče pogojna obsodba (glej 58- čl. KZ-1)?"
odg20_3 = ["ce je sodisce storilcu dolocilo zacen zapora do 2 let ali denarno kazen, ce glede na osebnost storilca, njegovo prejsneje zivljenje (itd.) spozna, da je mogoce pricakovati, da ne bo vec ponovil kaznivega dejanja, in tudi za kazniva dejanja, za katera je predpisana kazen zapora najmanj 5 let, ce prizna krivdo o prvem izjavljanju o obtoženem aktu, v katerem je predlagan izrek pogojne obsodbe, ali prizna krivdo v sporazumu z drzavnim tozilcem"]
drugo20_3 = [
    "Za vsa kazniva dejanja ne glede na težo in brez kakršnihkoli pogojev",
    "Samo za kazniva dejanja zoper življenje in telo obvezno",
    "Le če storilec prestaja zaporno kazen daljšo od desetih let"
]
tocke = tocke + naloga(nal20_3, odg20_3, drugo20_3)
print("tvoje stevilo tock: ", tocke)

#nal 21
nal21 = "Naštej vrste sankcij, ki jih v slovenskem pravnem redu sodišče lahko izreče odgovornim storilcem prekrškov."
odg21 = ["globa, kazenske točke v CP, splošno koristno delo, izgon tujca iz države, odzvem predmetov, opomin..."]
drugo21 = ["Zapor do 20 let", "Smrtna kazen", "Dosmrtna ječa"]
tocke = tocke + naloga(nal21, odg21, drugo21)
print("tvoje stevilo tock: ", tocke)

#nal 22
nal22 = "Naštej vrste sankcij, ki jih v slovenskem pravnem redu sodišče lahko izreče storilcem disciplinskih prestopkov."
odg22 = ["opomin, ukor, denarna kazen, izključitev iz organizacije (za določen čas in/ali dokoncna izkljucitev), druge sankcije (npr prepoved pristopa k opravljanju izpita)"]
drugo22 = ["Zaplemba države", "Razglasitev vojne", "Razveljavitev ustave"]
tocke = tocke + naloga(nal22, odg22, drugo22)
print("tvoje stevilo tock: ", tocke)

#nal 23
nal23 = "Naštej vrste sankcij, ki jih v slovenskem pravnem redu sodišče lahko izreče odgovornim storilcem civilnih deliktov."
odg23 = ["restitucija, denarna odškodnina"]
drugo23 = ["Kazenski zapor", "Smrtna kazen", "Hišni pripor"]
tocke = tocke + naloga(nal23, odg23, drugo23)
print("tvoje stevilo tock: ", tocke)

#nal 24
nal24 = "Kateri državni organ v Republiki Sloveniji sprejema uredbe z zakonsko močjo?"
odg24 = ["Državni zbor in izjemoma predsednik"]
drugo24 = ["Predsednik republike", "Ustavno sodišče", "Državni svet"]
tocke = tocke + naloga(nal24, odg24, drugo24)
print("tvoje stevilo tock: ", tocke)

#nal 25
nal25 = "Kateri državni organ v Republiki Sloveniji sprejema spremembe ustave?"
odg25 = ["Državni zbor"]
drugo25 = ["Vlada", "Predsednik republike", "Ustavno sodišče"]
tocke = tocke + naloga(nal25, odg25, drugo25)
print("tvoje stevilo tock: ", tocke)

#nal 26
nal26 = "Ali drži trditev, da Kazenski zakonik v posebnem delu ureja izključno kazniva dejanja in sankcije zanje, medtem ko so prekrški kot blažja oblika kazenskih deliktov določeni s področnimi zakoni, vladnimi uredbami in občinskimi odloki?"
odg26 = ["Drži"]
drugo26 = ["Vedno drži", "Nikoli ne drži", "Velja samo za občine"]
tocke = tocke + naloga(nal26, odg26, drugo26)
print("tvoje stevilo tock: ", tocke)

#nal 27
nal27 = "Ali drži trditev, da Zakon o prekrških poleg prekrškov in sankcij za prekrške določa in sankcionira tudi nekatera manj huda kazniva dejanja?"
odg27 = ["Ne"]
drugo27 = ["Da, v celoti", "Da, v večini", "Da, samo za mladoletne"]
tocke = tocke + naloga(nal27, odg27, drugo27)
print("tvoje stevilo tock: ", tocke)

#nal 28
nal28 = "Katera dva velika pravna sistema oz. pravni tradiciji obstajata v zahodnem svetu?"
odg28 = ["Anglosaški in evropski pravni sistem"]
drugo28 = ["Fevdalni in socialistični", "Vojaški in civilni", "Cerklveni in državni"]
tocke = tocke + naloga(nal28, odg28, drugo28)
print("tvoje stevilo tock: ", tocke)

#nal 29.1
nal29_1 = "Na kratko pojasni, kako je v slovenskem pravnem redu urejen institut kazenske odgovornosti?"
odg29_1 = ["Voljno ravnanje človeka, bit inkriminacije, protipravnost, krivda"]
drugo29_1 = ["Po volilnem sistemu", "Po cerkvenem pravu", "Po občinskem statutu"]
tocke = tocke + naloga(nal29_1, odg29_1, drugo29_1)
print("tvoje stevilo tock: ", tocke)

#nal 29.2
nal29_2 = "Kdor stori dejanje v stanju neprištevnosti:"
odg29_2 = ["ni kriv,"]
drugo29_2 = ["Je vedno kaznovan", "Ni ravnal protipravno", "Se lahko mileje kaznuje"]
tocke = tocke + naloga(nal29_2, odg29_2, drugo29_2)
print("tvoje stevilo tock: ", tocke)

#nal 29.3
nal29_3 = "Kdor je dejanje storil v silobranu:"
odg29_3 = ["ni ravnal protipravno"]
drugo29_3 = ["Ni kriv", "Se kaznuje strožje", "Se kaznuje brez izjeme"]
tocke = tocke + naloga(nal29_3, odg29_3, drugo29_3)
print("tvoje stevilo tock: ", tocke)

#nal 29.4
nal29_4 = "Kako se z latinskim izrazom imenuje kazenskopravni institut, ki je namenjen uveljavljanju kazenske odgovornosti neprištevnih storilcev, ki so sami povzročili neprištevnost?"
odg29_4 = ["Actio libera in causa"]
drugo29_4 = ["Lex talionis", "Habeas corpus", "Stare decisis"]
tocke = tocke + naloga(nal29_4, odg29_4, drugo29_4)
print("tvoje stevilo tock: ", tocke)

#nal 30
nal30 = "Katera izraza se v slovenski pravni terminologiji praviloma uporabljata za stranki sodnega postopka, ki si nasprotujeta v civilnopravnem sporu?"
odg30 = ["Tožilec in toženec, tožnik in toženi"]
drugo30 = ["Tožilec in sodnik", "Obtoženec in priča", "Minister in poslanec"]
tocke = tocke + naloga(nal30, odg30, drugo30)
print("tvoje stevilo tock: ", tocke)

#nal 31
nal31 = "Naštej sestavine upravne odločbe."
odg31 = ["Uvod, izrek, obrazložitev, pravni pouk"]
drugo31 = ["Ime sodnika", "Kazenska sankcija", "Volilni izid"]
tocke = tocke + naloga(nal31, odg31, drugo31)
print("tvoje stevilo tock: ", tocke)

#nal 32
nal32 = "Pojasni za kaj gre pri diskrecijskem pravnem pravilu in kaj je diskrecijska pravica"
odg32 = ["Diskrecijsko pravno pravilo: to pravno pravilo dzavnim organom do prostega preudarka, ko odločajo o pravicah in obveznostih, drzavni organ je zavezan k spostovanju nacela zakontosti. Diskrecijska pravica: pravica, ki jo ime pristojni organ pri odločitvi, ali bo uporabil zakonsko možnost, ki je utrejena z diskrecijskim pravnim pravilom"]
drugo32 = ["Pravilo brez zakona", "Naključno odločanje", "Samovoljno kaznovanje"]
tocke = tocke + naloga(nal32, odg32, drugo32)
print("tvoje stevilo tock: ", tocke)

#nal 33
nal33 = "O čem in katero sodišče odloča v upravnem sporu?"
odg33 = ["upravno sodišče republike slovenije: -sodni nadzor nad zakonitostjo akter in delovanja upravnih organov države, odloča o zakonitosti posamičnih aktor in dejanj s katerimi se posega v ČPTS, če ni zagotovljeno drugo sodno varstvo, na 1. stopnji sodita US in Vrhovno sodišče, na 2.stopnji pa samo VS"]
drugo33 = ["O kaznivih dejanjih in kazensko sodišče", "O volitvah in ustavno sodišče", "O zakonih in parlament"]
tocke = tocke + naloga(nal33, odg33, drugo33)
print("tvoje stevilo tock: ", tocke)

#nal 34
nal34 = "Kako se imenuje pravni postopek, v katerem lahko upnik od dolžnika po sodni poti zahteva vračilo dolga?"
odg34 = ["Izvršilni pospek"]
drugo34 = ["Kazenski postopek", "Volilni postopek", "Upravni spor"]
tocke = tocke + naloga(nal34, odg34, drugo34)
print("tvoje stevilo tock: ", tocke)

#nal 35
nal35 = "Kako se imenuje pravni postopek, v katerem stranka pridobi gradbeno dovoljenje, dovoljenje za prebivanje, pravico do azila ipd.?"
odg35 = ["Upravni postopek"]
drugo35 = ["Kazenski postopek", "Pravdni postopek", "Ustavni spor"]
tocke = tocke + naloga(nal35, odg35, drugo35)
print("tvoje stevilo tock: ", tocke)

#nal 36
nal36 = "Kako se imenuje pravni postopek, v katerem lahko sodišče odloči o odvzemu poslovne sposobnosti in razglasitvi pogrešane osebe za mrtvo?"
odg36 = ["Nepravdni postopek"]
drugo36 = ["Kazenski postopek", "Pravdni postopek", "Zakonodajni postopek"]
tocke = tocke + naloga(nal36, odg36, drugo36)
print("tvoje stevilo tock: ", tocke)

#nal 37
nal37 = "Kateri funkcionar lahko v RS pomilosti pravnomočno obsojene storilce kaznivih dejanj?"
odg37 = ["Predsednik republike"]
drugo37 = ["Predsednik vlade", "Ustavno sodišče", "Državni zbor"]
tocke = tocke + naloga(nal37, odg37, drugo37)
print("tvoje stevilo tock: ", tocke)

#nal 38
nal38 = "Ali drži trditev, da so v hierarhiji predpisov pravnem redu RS mednarodne pogodbe, ki jih ratificira Državni zbor, pod ustavo in nad zakoni?"
odg38 = ["Da"]
drugo38 = ["ne", "nikoli", "obcasno"]
tocke = tocke + naloga(nal38, odg38, drugo38)
print("tvoje stevilo tock: ", tocke)

#nal 39
nal39 = "Kako se imenuje pogodba iz leta 1992, s katero je bila ustanovljena EU?"
odg39 = ["Maastrichtska pogodba"]
drugo39 = ["Lizbonska pogodba", "Rimska pogodba", "Schengenski sporazum"]
tocke = tocke + naloga(nal39, odg39, drugo39)
print("tvoje stevilo tock: ", tocke)

#nal 40
nal40 = "Kako se imenuje ustanovna pogodba Evropske unije, ki je trenutno v veljavi?"
odg40 = ["Lizbonska pogodba"]
drugo40 = ["Maastrichtska pogodba", "Nicejska pogodba", "Pariška pogodba"]
tocke = tocke + naloga(nal40, odg40, drugo40)
print("tvoje stevilo tock: ", tocke)

#nal 41.1
nal41_1 = "Kateri dve instituciji EU sta zakonodajna organa?"
odg41_1 = ["Evropski parlament in svet europske unije"]
drugo41_1 = ["Evropska komisija in ECB", "Evropsko sodišče in Svet Evrope", "NATO in OZN"]
tocke = tocke + naloga(nal41_1, odg41_1, drugo41_1)
print("tvoje stevilo tock: ", tocke)

#nal 41.2
nal41_2 = "Katera institucija EU je izvršilni organ?"
odg41_2 = ["Evropska komisija"]
drugo41_2 = ["Evropski parlament", "Evropsko sodišče", "Svet Evrope"]
tocke = tocke + naloga(nal41_2, odg41_2, drugo41_2)
print("tvoje stevilo tock: ", tocke)

#nal 42
nal42 = "Katero obliko vladavine, politični sistem, sistem organizacije državne oblasti in obliko državne ureditve ima Slovenija?"
odg42 = ["oblika vladavine: republika - politicni sistem: demokracija - sistem organizacije drzavne oblasti: parlamentarni sistem - oblika dzavne ureditve: unitarna"]
drugo42 = ["oblika vladavine: monarhija - politicni sistem: demokracija - sistem organizacije drzavne oblasti: predsedniski sistem - oblika dzavne ureditve: unitarna", "oblika vladavine: avtokracija - politicni sistem: demokracija - sistem organizacije drzavne oblasti: parlamentarni sistem - oblika dzavne ureditve: Vojaško diktaturo", "Teokracijo"]
tocke = tocke + naloga(nal42, odg42, drugo42)
print("tvoje stevilo tock: ", tocke)

#nal 43.1
nal43_1 = "Katero obliko državne ureditve, sistem organizacije oblasti, politični sistem in obliko vladavine ima Hrvaška?"
odg43_1 = ["oblika vladavine: republika - politicni sistem: demokracija - sistem organizacije drzavne oblasti: parlamentarni sistem - oblika dzavne ureditve: unitarna"]
drugo43_1 = ["oblika vladavine: monarhija - politicni sistem: demokracija - sistem organizacije drzavne oblasti: predsedniski sistem - oblika dzavne ureditve: unitarna", "oblika vladavine: republika - politicni sistem: demokracija - sistem organizacije drzavne oblasti: predsedniski sistem - oblika dzavne ureditve: federacija", "Diktatura"]
tocke = tocke + naloga(nal43_1, odg43_1, drugo43_1)
print("tvoje stevilo tock: ", tocke)

#nal 43.2
nal43_2 = "Katero obliko državne ureditve, sistem organizacije oblasti, politični sistem in obliko vladavine ima ZDA?"
odg43_2 = ["oblika vladavine: republika - politicni sistem: demokracija - sistem organizacije drzavne oblasti: predsedniski sistem - oblika dzavne ureditve: federacija"]
drugo43_2 = ["Parlamentarna monarhija", "oblika vladavine: republika - politicni sistem: demokracija - sistem organizacije drzavne oblasti: parlamentarni sistem - oblika dzavne ureditve: unitarna", "oblika vladavine: avtokracija - politicni sistem: demokracija - sistem organizacije drzavne oblasti: parlamentarni sistem - oblika dzavne ureditve: Vojaško diktaturo"]
tocke = tocke + naloga(nal43_2, odg43_2, drugo43_2)
print("tvoje stevilo tock: ", tocke)

#nal 44
nal44 = "Katere bistvene značilnosti državo opredeljujejo kot republiko? "
odg44 = ["sef drzave je voljen organ, omejen madnat, pravno odgovoren, razlicen obseg pristojnosti parlamentarne, predsedniske, polpredsedniske republike"]
drugo44 = ["Dedna oblast, pravno odgovoren", "Absolutna monarhija", "Cerklvena oblast"]
tocke = tocke + naloga(nal44, odg44, drugo44)
print("tvoje stevilo tock: ", tocke)

#nal 45
nal45 = "V katerem členu Ustave RS je zapisano, da je Slovenija pravna država?"
odg45 = ["V 2. členu"]
drugo45 = ["V 1. členu", "V 50. členu", "V 120. členu"]
tocke = tocke + naloga(nal45, odg45, drugo45)
print("tvoje stevilo tock: ", tocke)

#nal 46
nal46 = "V katerem členu Ustave RS je zapisano, da je Slovenija socialna država?"
odg46 = ["V 2. členu"]
drugo46 = ["V 5. členu", "V 80. členu", "V 1. členu"]
tocke = tocke + naloga(nal46, odg46, drugo46)
print("tvoje stevilo tock: ", tocke)

#nal 47
nal47 = "Katere so bistvene značilnosti avtoritarne države?"
odg47 = ["Oblast je v rokah posameznika (lahko je voljen) ali skupine, ljudstvo ne more dejansko vplivati na oblast in ne more uveljevati odgovornosti, strog drzavni nadzor zasebne in gospodarske sfere, omejitev politicnih in osebnostnih pravic"]
drugo47 = [
"Polna politična svoboda posameznika, močna civilna družba in učinkovito varstvo človekovih pravic",
"Delitev oblasti na zakonodajno, izvršilno in sodno ter neodvisno sodstvo",
"Svobodne in poštene volitve ter odgovornost oblasti volivcem"
]
tocke = tocke + naloga(nal47, odg47, drugo47)
print("tvoje stevilo tock: ", tocke)

#nal 48
nal48 = "Kako se imenuje oblika (nad)državne ureditve, ki temelji na pogodbi, s katero države pogodbenice določijo nekatere skupne organe in nanje prenesejo določene pristojnosti, ne da bi pri tem izgubile svojo suverenost, za veljavnost odločitev skupnih organov pa je potrebno soglasje vseh članic povezave?"
odg48 = ["Konfederacija"]
drugo48 = ["Federacija", "Imperij", "Unitarna država"]
tocke = tocke + naloga(nal48, odg48, drugo48)
print("tvoje stevilo tock: ", tocke)

#nal 49
nal49 = "Kateri izraz se uporablja za politične stranke in poslance, ki v Državnem zboru tvorijo večino in kateri za politične stranke in poslance, ki so v manjšini?"
odg49 = ["Koalicija in opozicija"]
drugo49 = ["Sodniki in tožilci", "Volivci in kandidati", "Državljani in tujci"]
tocke = tocke + naloga(nal49, odg49, drugo49)
print("tvoje stevilo tock: ", tocke)

#nal 50.1
nal50_1 = "S kakšno osnovno večino Državni zbor sprejema zakone in druge odločitve iz svoje pristojnosti?"
odg50_1 = ["Z navadno relativno večino"]
drugo50_1 = ["Z dvotretjinsko večino vseh volivcev", "Z večino ministrov", "S soglasjem predsednika"]
tocke = tocke + naloga(nal50_1, odg50_1, drugo50_1)
print("tvoje stevilo tock: ", tocke)


#nal 50.2
nal50_2 = "Kako se poslovenjeno imenuje izraz kvorum?"
odg50_2 = ["Večina, sklepčnost (46 poslancev)"]
drugo50_2 = [
"Soglasje vseh poslancev",
"Udeležba na glasovanju",
"Parlamentarna večina"
]
tocke = tocke + naloga(nal50_2, odg50_2, drugo50_2)
print("tvoje stevilo tock: ", tocke)

#nal 51
nal51 = "S kakšno večino Državni zbor RS izvoli predsednika vlade in ministre?"
odg51 = ["Z večino vseh poslancev (absolutna večina - najmanj 46 glasov)"]
drugo51 = [
"Z relativno večino navzočih poslancev",
"Z dvotretjinsko večino vseh poslancev",
"Z navadno večino oddanih glasov"
]
tocke = tocke + naloga(nal51, odg51, drugo51)
print("tvoje stevilo tock: ", tocke)

#nal 52
nal52 = "Kako se s tujko imenuje akt Predsednika Republike, s katerim ta razglasi zakon?"
odg52 = ["Promulgacija"]
drugo52 = ["Ratifikacija", "Interpelacija", "Amnestija"]
tocke = tocke + naloga(nal52, odg52, drugo52)
print("tvoje stevilo tock: ", tocke)

#nal 53
nal53 = "Kaj je namen instituta parlamentarne preiskave?"
odg53 = ["Raziskati kršitve nedopustno ravnanje, zlorabo pooblastil... nosicev javnih funkcij in ugotoviti dejansko stanje za odločitev drzavnega zbora o politicni odgovornosti nosilcev javnih funkcij in pooblastil"]
drugo53 = [
    "Ugotoviti ustavno odgovornost nosilcev javnih funkcij in jim neposredno izreči sankcije",
    "Raziskati kazensko odgovornost posameznikov in odločiti o njihovi obsodbi",
    "Preveriti zakonitost sodnih odločb in posegati v delo sodišč"
]
tocke = tocke + naloga(nal53, odg53, drugo53)
print("tvoje stevilo tock: ", tocke)

#nal 54.1
nal54_1 = "Kaj praviloma sledi po končanem postopku interpelacije?"
odg54_1 = ["postopek razširjenega poslanskega vprasasanja zoper enega cloveka, ki naj bi ga ta zafrknil (obtozilni akt) za ministre -> nezaupnica razreši minister in predlaga novega ; nezaupnica zoper predsednika vlade je kontruktivna nezaupnica -> razresis obstojocega, tako da izvolis novega"]
drugo54_1 = [
    "postopek ugotavljanja kazenske odgovornosti ministra pred sodiščem in izrek sodbe o njegovi krivdi",
    "postopek razpustitve državnega zbora in avtomatična razpis novih volitev za celotno vlado",
    "postopek imenovanja nove vlade brez glasovanja o zaupnici ali nezaupnici"
]
tocke = tocke + naloga(nal54_1, odg54_1, drugo54_1)
print("tvoje stevilo tock: ", tocke)

#nal 54.2
nal54_2 = "Kaj pomeni izraz konstruktivna nezaupnica?"
odg54_2 = ["Nezaupnica zoper predsednika vlade"]
drugo54_2 = ["Neposredne volitve vlade", "Razpustitev parlamenta brez glasovanja", "Zamenjava predsednika republike"]
tocke = tocke + naloga(nal54_2, odg54_2, drugo54_2)
print("tvoje stevilo tock: ", tocke)

#nal 55
nal55 = "Kako se imenuje pravni akt oz. predpis, s katerim v ZDA dopolnjujejo oz. spreminjajo  ustavo?"
odg55 = ["Amandma(ustavni zakon)"]
drugo55 = ["Zvezni zakon", "Predsedniški odlok", "Vrhovna sodba"]
tocke = tocke + naloga(nal55, odg55, drugo55)
print("tvoje stevilo tock: ", tocke)

#nal 56
nal56 = "Kateri izraz se uporablja za sodbe najvišjih sodišč, ki imajo v pravnem redu ZDA status zakonov oziroma predpisov?"
odg56 = ["Precedensi"]
drugo56 = ["Uredbe", "Statuti", "Podzakonski akti"]
tocke = tocke + naloga(nal56, odg56, drugo56)
print("tvoje stevilo tock: ", tocke)

#nal 57.1
nal57_1 = "Koliko elektorskih glasov morata zbrati kandidata za predsednika in podpredsednika ZDA za izvolitev?"
odg57_1 = ["270"]
drugo57_1 = ["100", "200", "400"]
tocke = tocke + naloga(nal57_1, odg57_1, drugo57_1)
print("tvoje stevilo tock: ", tocke)

#nal 57.2
nal57_2 = "Koliko je skupno število elektorskih glasov na predsedniških volitvah v ZDA?"
odg57_2 = ["538"]
drugo57_2 = ["300", "470", "640"]
tocke = tocke + naloga(nal57_2, odg57_2, drugo57_2)
print("tvoje stevilo tock: ", tocke)

#nal 57.3
nal57_3 = "Kako se imenuje parlament v ZDA in kako se imenujeta njegova domova?"
odg57_3 = ["Congress in House of representatives ter senat"]
drugo57_3 = ["Parlament in vlada", "Zbor in senat", "Senat in kabinet"]
tocke = tocke + naloga(nal57_3, odg57_3, drugo57_3)
print("tvoje stevilo tock: ", tocke)

#nal 58
nal58 = "Katere organe bodo slovenski volivci na neposrednih demokratičnih volitvah volili v letu 2022?"
odg58 = ["Drzavni zbor, predsednik republike slovenije, lokalne organe (zupan in obcinski svet)"]
drugo58 = ["Ustavno sodišče", "Državni svet", "Vlado"]
tocke = tocke + naloga(nal58, odg58, drugo58)
print("tvoje stevilo tock: ", tocke)

#nal 59.1
nal59_1 = "Kdo je aktualni premier Velike Britanije?"
odg59_1 = ["Kier Starmer"]
drugo59_1 = ["Angela Merkel", "Emmanuel Macron", "Justin Trudeau"]
tocke = tocke + naloga(nal59_1, odg59_1, drugo59_1)
print("tvoje stevilo tock: ", tocke)

#nal 59.2
nal59_2 = "Katera politična stranka trenutno prevladuje v parlamentu Združenega kraljestva?"
odg59_2 = ["Labouristična stranka (Labour Party)"]
drugo59_2 = ["Zeleni", "Liberalni demokrati", "Socialdemokrati"]
tocke = tocke + naloga(nal59_2, odg59_2, drugo59_2)
print("tvoje stevilo tock: ", tocke)

#nal 60
nal60 = "Kateri organ in na čigav predlog v Republiki Sloveniji izvoli sodnike Ustavnega sodišča?"
odg60 = ["Državni zbor na predlog predsednika republike sloveniej"]
drugo60 = ["Vlada", "Predsednik republike sam", "Državni svet"]
tocke = tocke + naloga(nal60, odg60, drugo60)
print("tvoje stevilo tock: ", tocke)

#nal 61
nal61 = "S katerim institutom v Sloveniji zakonodajni organ uveljavlja pravno odgovornost vlade in ministrov zaradi kršitev ustave ali zakona pri opravljanju njihove funkcije? "
odg61 = ["Ustavna obtožba"]
drugo61 = ["Referendum", "Pomilostitev", "Volitve"]
tocke = tocke + naloga(nal61, odg61, drugo61)
print("tvoje stevilo tock: ", tocke)

#nal 62
nal62 = "Kateri subjekti lahko v Državni zbor vložijo predlog zakona?"
odg62 = ["Vlada, vsak poslanec, 5000 volilcev, državmo svet"]
drugo62 = ["Vlada, skupek 10 poslancov, 5000 volilcev, državmo svet", "Vlada, vsak poslanec, 3000 volilcev, državmo svet", "Državni svetniki"]
tocke = tocke + naloga(nal62, odg62, drugo62)
print("tvoje stevilo tock: ", tocke)

#nal 63
nal63 = "Kateri volilni sistem je v Sloveniji trenutno v veljavi pri volitvah v Državni zbor in kateri pri volitvah predsednika republike?"
odg63 = ["Drzavni zbor: proporcialni volilni sistem - predsednik republike: vecinski volilni sistem"]
drugo63 = ["Večinski in absolutni", "Drzavni zbor: proporcialni volilni sistem - predsednik republike: absolutni volilni sistem", "Federalni in regionalni"]
tocke = tocke + naloga(nal63, odg63, drugo63)
print("tvoje stevilo tock: ", tocke)

#nal 64.1
nal64_1 = "Za kateri volilni sistem je značilna uporaba d'Hondtovega sistema razdelitve mandatov?"
odg64_1 = ["proporcionalni volilni sistem"]
drugo64_1 = ["Večinski sistem", "Dvokrožni sistem", "Preferenčni sistem"]
tocke = tocke + naloga(nal64_1, odg64_1, drugo64_1)
print("tvoje stevilo tock: ", tocke)

#nal 64.2
nal64_2 = "Za kateri volilni sistem je značilna uporaba Harejevega količnika pri razdelitvi mandatov?"
odg64_2 = ["Proporcionalni volilni sistem"]
drugo64_2 = ["Večinski sistem", "Dvokrožni sistem", "Relativni sistem"]
tocke = tocke + naloga(nal64_2, odg64_2, drugo64_2)
print("tvoje stevilo tock: ", tocke)

#nal 64.3
nal64_3 = "Za kateri volilni sistem so značilne plurinominalne volilne enote?"
odg64_3 = ["Proporcionalni volilni sistem"]
drugo64_3 = ["Enomandatne enote", "Predsedniške volitve", "Elektronske volitve"]
tocke = tocke + naloga(nal64_3, odg64_3, drugo64_3)
print("tvoje stevilo tock: ", tocke)

#nal 65
nal65 = "Kateri volilni sistem praviloma zagotavlja stabilno vlado oz. izvršilno vejo oblasti?"
odg65 = ["Večinski"]
drugo65 = ["Proporcionalni", "Preferenčni", "Mešani"]
tocke = tocke + naloga(nal65, odg65, drugo65)
print("tvoje stevilo tock: ", tocke)

#nal 66
nal66 = "Kateri volilni sistem omogoča, da se lahko s svojimi kandidati v parlament uvrstijo politične stranke s skrajnejšimi stališči?"
odg66 = ["Proporcionalni"]
drugo66 = ["Večinski", "Dvokrožni", "Enokrožni"]
tocke = tocke + naloga(nal66, odg66, drugo66)
print("tvoje stevilo tock: ", tocke)

#nal 67
nal67 = "Kako se imenujejo sodišča splošne pristojnosti, ki v sistemu sodstva v Republiki Sloveniji sodijo na prvi stopnji?"
odg67 = ["Orjana in okrožna sodišča"]
drugo67 = ["Ustavna sodišča", "Vrhovna sodišča", "Evropska sodišča"]
tocke = tocke + naloga(nal67, odg67, drugo67)
print("tvoje stevilo tock: ", tocke)

#nal 68
nal68 = "Katero sodišče je najvišje sodišče v Republiki Sloveniji?"
odg68 = ["Vrhovno sodišče"]
drugo68 = ["Okrožno sodišče", "Evropsko sodišče", "Upravno sodišče"]
tocke = tocke + naloga(nal68, odg68, drugo68)
print("tvoje stevilo tock: ", tocke)

#nal 69
nal69 = "Katere pristojnosti ima po Ustavi RS Državni svet RS?"
odg69 = ["Predlaga zakone, daje državnemu zboru mnenje o vseh zadevah in njihove pristojnosti, zahteva, da drzavni zbor pred razglasitvijo kakega zakona o njem se enkrat odloca (veto), zahteva preizskavo javnega pomena 93.clena"]
drugo69 = ["Imenuje vlado", "Sprejema ustavo", "Razpisuje volitve"]
tocke = tocke + naloga(nal69, odg69, drugo69)
print("tvoje stevilo tock: ", tocke)

#nal 70
nal70 = "Kdo v vladi Roberta Goloba trenutno opravlja funkcijo notranjega ministra?"
odg70 = ["Branko Zlobko (Bostjan Poklukar je odstopil)"]
drugo70 = ["Borut Pahor", "Janez Janša", "Anže Logar"]
tocke = tocke + naloga(nal70, odg70, drugo70)
print("tvoje stevilo tock: ", tocke)

#nal 71
nal71 = "Kdo trenutno opravlja funkcijo predsednika Državnega zbora?"
odg71 = ["Urška Klakočar Zupančič"]
drugo71 = ["Predsednik republike", "Predsednik vlade", "Notranji minister"]
tocke = tocke + naloga(nal71, odg71, drugo71)
print("tvoje stevilo tock: ", tocke)

#nal 72
nal72 = "Naštej instrumente, s katerimi Državni zbor izvaja svojo nadzorno funkcijo."
odg72 = ["Interpelacija, konstruktivna nezaupnica in obtozba predsednika vlade, ministra in predsednika pred ustavnim sodiscem"]
drugo72 = ["Kazenski postopki", "Sodni postopki", "Volilni nadzor"]
tocke = tocke + naloga(nal72, odg72, drugo72)
print("tvoje stevilo tock: ", tocke)

#nal 73
nal73 = "Naštej izjeme od načela splošnosti volilne pravice pri volitvah v Državni zbor."
odg73 = ["ni državljan RS, je mladoleten, če mu je bila odvzeta poslovna sposobnost, omejitev zaradi prestajanja kazni"]
drugo73 = [
    "če oseba nima stalnega prebivališča v Republiki Sloveniji, če ni zaposlena in če ne plačuje davkov",
    "če ni član politične stranke, če ne sodeluje v volilni kampanji, če ne izpolnjuje pogojev za kandidaturo",
    "če je mlajša od 25 let, če nima dokončane srednje šole, če ni vpisana v volilni imenik"
]
tocke = tocke + naloga(nal73, odg73, drugo73)
print("tvoje stevilo tock: ", tocke)

#nal 74
nal74 = "V čem se pri volitvah v Državni zbor kaže oziroma zagotavlja enakost volilne pravice?"
odg74 = ["glas vsakega volilca ima enako vrednost"]
drugo74 = ["Različna teža glasov", "Neenake volilne enote", "Glasujejo samo izbrani"]
tocke = tocke + naloga(nal74, odg74, drugo74)
print("tvoje stevilo tock: ", tocke)

#nal 75
nal75 = "V čem je razlika med aktivno in pasivno volilno pravico?"
odg75 = ["Aktivna volilna pravica: pravica voliti - pasivna volilna pravica: pravica biti voljen"]
drugo75 = ["Pomenita isto", "Aktivna volilna pravica: pravica voliti - pasivna volilna pravica: ne glasovati", "Aktivna pomeni biti izvoljen"]
tocke = tocke + naloga(nal75, odg75, drugo75)
print("tvoje stevilo tock: ", tocke)

#nal 76
nal76 = "Kateri organ odloča o vložitvi in kateri o utemeljenosti ustavne obtožbe najvišjih funkcionarjev izvršilne oblasti?"
odg76 = ["Drzavni zbor(vsaj 30 poslancev) Utemeljenost: ustavno sodisce"]
drugo76 = ["Vlada in predsednik republike", "Državni svet in vlada", "Ustavno sodišče in vlada"]
tocke = tocke + naloga(nal76, odg76, drugo76)
print("tvoje stevilo tock: ", tocke)

#nal 77
nal77 = "Pojasni razliko med ugotavljanjem politične in pravne odgovornosti funkcionarjev izvršilne oblasti."
odg77 = ["Politična odgovornost se ugotavlja v političnih organih in ima politične posledice (npr. nezaupnica, razrešitev), pravna odgovornost pa se ugotavlja v sodnih postopkih in ima pravne sankcije (kazenske, civilne, disciplinske)"]
drugo77 = [
    "Politična odgovornost se ugotavlja v sodnih postopkih in vodi do kazenskih sankcij, pravna odgovornost pa se ugotavlja v Državnem zboru in ima politične posledice",
    "Politična in pravna odgovornost se ugotavljata v istem postopku in vedno vodita do enakih sankcij",
    "Politična odgovornost pomeni kršitev kazenskega prava, pravna odgovornost pa izgubo politične funkcije brez sodnega postopka"
]
tocke = tocke + naloga(nal77, odg77, drugo77)
print("tvoje stevilo tock: ", tocke)

#nal 78
nal78 = "Na kratko opiši način oblikovanja vlade v Republiki Sloveniji."
odg78 = ["Predsednik republike predlaga kandidata za predsednika vlade, Državni zbor ga izvoli, nato predsednik vlade predlaga ministre, ki jih potrdi Državni zbor"]
drugo78 = [
    "Predsednik republike neposredno imenuje predsednika vlade in ministre brez potrditve Državnega zbora",
    "Državni zbor najprej izvoli ministre, nato pa skupaj izmed njih določi predsednika vlade",
    "Vlado oblikuje Ustavno sodišče na predlog političnih strank po opravljenih volitvah"
]
tocke = tocke + naloga(nal78, odg78, drugo78)
print("tvoje stevilo tock: ", tocke)

#nal 79
nal79 = "Katere funkcije v pravnem sistemu RS opravlja vlada?"
odg79 = ["Predstavlja izbrsno oblast, izvaja zakone in druge predpise, ki jih sprejema DZ, izvaja predpise, ki so potrebni za razvoj drzave in za urejenost razmer na vseh podrocjih v pristojnosti drzave, najvisji organ drzave uprave"]
drugo79 = [
    "Predstavlja zakonodajno oblast, sprejema zakone in odloča o ustavnih spremembah",
    "Izvaja sodno oblast, odloča o sporih in izreka sodbe v imenu ljudstva",
    "Nadzira volitve, potrjuje mandate poslancev in razlaga ustavo"
]
tocke = tocke + naloga(nal79, odg79, drugo79)
print("tvoje stevilo tock: ", tocke)

#nal 80
nal80 = "V čem se kaže glavna razlika med parlamentarnim in predsedniškim sistemom oblasti?"
odg80 = ["V parlamentarnem sistemu vlado vodi premier, ki je odvisen od podpore parlamenta - v predsedniskem sistemu pa ima izvrsno oblast predsednik, ki je neodvisen od parlamenta"]
drugo80 = [
    "V parlamentarnem sistemu ima izvršno oblast predsednik republike, v predsedniškem sistemu pa vlado vodi premier, ki je odgovoren parlamentu",
    "V obeh sistemih ima izvršna oblast enako razmerje do parlamenta in ni razlik v odgovornosti vlade",
    "V parlamentarnem sistemu je predsednik države popolnoma neodvisen od parlamenta, v predsedniškem sistemu pa je izvršna oblast podrejena parlamentu"
]
tocke = tocke + naloga(nal80, odg80, drugo80)
print("tvoje stevilo tock: ", tocke)

#nal 81
nal81 = "Naštej pristojnosti, ki jih ima v pravnem sistemu RS predsednik republike."
odg81 = ["Predstavlja republiko slovenije, vrhovni poveljnik obrambnih sil, razpise volitve v DZ, razglasa zakone, imenuje nekatere drzavne funkcionarje, predstavlja in odpoklice veleposlanike in poslanike RS, izdaja listine o verifikaciji"]
drugo81 = [
    "Vodi vlado in usmerja delo ministrov, sprejema uredbe ter odgovarja Državnemu zboru",
    "Sprejema zakone, potrjuje državni proračun in odloča o zaupnici vladi",
    "Imenuje sodnike vseh sodišč samostojno, odloča o ustavnosti zakonov ter izreka sodne odločbe"
]
tocke = tocke + naloga(nal81, odg81, drugo81)
print("tvoje stevilo tock: ", tocke)

#nal 82
nal82 = "Naštej  pristojnosti, ki jih ima v pravnem sistemu RS Ustavno sodišče."
odg82 = ["presoja skladnosti obrambih in splosnih pravnih aktov z ustavo, oceni ustavnosti in zakonistosti predpisov, odlocanje o ustavnih pritozbah zaradi krsitev s posamicnimi akti, odlocanje v sporih glede pristojnosti, odlocanje o pravni odgovornosti PR, PV in ministrov"]
drugo82 = [
    "Sprejema zakone, potrjuje državni proračun in odloča o zaupnici vladi",
    "Odloča o kazenski odgovornosti posameznikov in izreka zaporne ter denarne kazni",
    "Vodi izvršilno oblast, izdaja uredbe in nadzira delo ministrstev"
]
tocke = tocke + naloga(nal82, odg82, drugo82)
print("tvoje stevilo tock: ", tocke)

#nal 83
nal83 = "O čem Ustavno sodišče odloča v ustavnem sporu?"
odg83 = ["Ustavni spor je postopek za oceno ustvarnosti predpisov"]
drugo83 = ["O kaznivih dejanjih", "O lokalnih volitvah", "O občinskih zakonih"]
tocke = tocke + naloga(nal83, odg83, drugo83)
print("tvoje stevilo tock: ", tocke)

#nal 84
nal84 = "Kako je v Ustavi RS urejena kazenska imuniteta poslancev?"
odg84 = ["poslanec drzavnega zbora ni kazensko odgovoren za mnenje ali glas, ki ga je izrekel na sejah drzavnega zbora ali njegovih delovnih teles. Poslanec ne sme biti priprt niti se zoper njega, ce se sklicuje ne imuniteto, ne sme zaceti kazenski postopek brez dovoljenja drzavnega zbora, razen ce je bil zaloten pri kaznivem dejanja, za katero je predpisana kazen zapora nad 5 let. DZ lahko prizna imuniteto tudi poslancu, ki se nanjo ni skliceral ali ki je bil zaloten pri kaznivem dejanju iz prejsnjega odstavka"]
drugo84 = [
    "Poslanec je kazensko neodgovoren za vsa svoja dejanja tudi izven sej Državnega zbora, kazenski postopek zoper njega pa se nikoli ne sme začeti brez dovoljenja Ustavnega sodišča",
    "Poslanec lahko vedno kazensko odgovarja brez kakršnegakoli dovoljenja Državnega zbora, tudi za mnenje in glasovanje na sejah Državnega zbora",
    "Kazenska imuniteta pomeni, da se poslancu med mandatom ne more izreči nobena kazenska sankcija, ne glede na vrsto kaznivega dejanja"
]
tocke = tocke + naloga(nal84, odg84, drugo84)
print("tvoje stevilo tock: ", tocke)

#nal 85
nal85 = "Predsednik republike, predsednik vlade in minister po Ustavi RS nimajo kazenske imunitete. Drži ali ne drži?"
odg85 = ["Drži (imoniteto lahko uživajo le poslanci DZ)"]
drugo85 = ["ne drži", "Drži samo za ministre", "Drži samo za predsednika republike"]
tocke = tocke + naloga(nal85, odg85, drugo85)
print("tvoje stevilo tock: ", tocke)

#nal 86
nal86 = "Kaj je značilno za manjšinsko parlamentarno preiskavo?"
odg86 = ["Izvede se na predlog ene tretjine poslancev ali DS"]
drugo86 = ["Je tajna", "Odloča ustavno sodišče", "Vodi jo vlada"]
tocke = tocke + naloga(nal86, odg86, drugo86)
print("tvoje stevilo tock: ", tocke)

#nal 87
nal87 = "V čem se razlikujeta imperativni in reprezentativni poslanski mandat?"
odg87 = ["Pri imperativnem mandatu je poslanec vezan na navodila volivcev in jih mora upoštevati, pri reprezentativnem mandatu pa poslanec odloča svobodno po svoji vesti in ni vezan na navodila volivcev."]
drugo87 = ["Ni razlike", "Imperativni je svoboden", "Reprezentativni je vezan"]
tocke = tocke + naloga(nal87, odg87, drugo87)
print("tvoje stevilo tock: ", tocke)

#nal 88
nal88 = "Katere vrste referendumov pozna pravni sistem Republike Slovenije?"
odg88 = ["Zakonodajni referendum, referendum o spremembi ustave, referendum o mednarodnih povezavah, posvetovalni referendum, lokalni referendum"]
drugo88 = ["Kazenski referendum", "Sodni referendum", "Upravni referendum"]
tocke = tocke + naloga(nal88, odg88, drugo88)
print("tvoje stevilo tock: ", tocke)

#nal 89
nal89 = "Pojasni razliko med potrditvenim, zavrnitvenim in razveljavitvenim zakonodajnim referendumom ter navedi, kateri tip je trenutno v veljavi v RS."
odg89 = ["Naknadni potrditveni: referendum o potrditvi zakona, drugega pravnega akta ali pravnega vprasanja, ki ga je sprejel zakonodajni ali drug organm pred njegovo uveljavitvijo - Razveljavitveni: referendum o razveljvaitvi celotnega zakoga - zavrnitveni: referendum o zavrnitvi zakona, drugega pravnega akta, ali drugega vprasanja, ki ga je sprejel zakonodajni ali drug organ pred njegovo uveljevitvijo ; naknadni zavrnitveni zakonodajni referendum"]
drugo89 = [
    "Naknadni potrditveni: referendum o potrditvi zakona, drugega pravnega akta ali pravnega vprasanja, ki ga je sprejel zakonodajni ali drug organm pred njegovo uveljavitvijo - Razveljavitveni: referendum o razveljvaitvi celotnega zakoga - zavrnitveni: referendum o zavrnitvi zakona, drugega pravnega akta, ali drugega vprasanja, ki ga je sprejel zakonodajni ali drug organ pred njegovo uveljevitvijo ; potrditveni referendum",
    "Naknadni potrditveni: referendum o potrditvi proračuna po njegovi uveljavitvi - Razveljavitveni: referendum o razveljavitvi vseh zakonov hkrati - Zavrnitveni: referendum o zavrnitvi vlade kot celote ; razveljavitveni referendum",
    "Naknadni potrditveni: referendum o potrditvi sodbe Ustavnega sodišča - Razveljavitveni: referendum o razveljavitvi kazenskega postopka - Zavrnitveni: referendum o zavrnitvi kazenske obsodbe ; sodni referendum"
]
tocke = tocke + naloga(nal89, odg89, drugo89)
print("tvoje stevilo tock: ", tocke)

#nal 90
nal90 = "Kdo lahko v RS vloži zahtevo za razpis zakonodajnega referenduma?"
odg90 = ["najmanj 1/3 poslancev (30), državni svet in 10.000 volilcev"]
drugo90 = ["najmanj 1/3 poslancev (30), državni svet in 5.000 volilcev", "najmanj 1/3 poslancev (40), državni svet in 8000 volilcev", "Vsak državljan sam"]
tocke = tocke + naloga(nal90, odg90, drugo90)
print("tvoje stevilo tock: ", tocke)

#nal 91
nal91 = "Pod katerimi pogoji je po Ustavi RS zakon na referendumu zavrnjen?"
odg91 = ["Če proti glasuje večina volilcev, ki so veljavno glasovali, pod pogojem, da na volitvah glasuje najmanj petina vseh volilcev"]
drugo91 = ["Če glasuje večina poslancev proti", "Če predsednik republike zakon zavrne", "Če je udeležba nižja od 10 %"]
tocke = tocke + naloga(nal91, odg91, drugo91)
print("tvoje stevilo tock: ", tocke)

#nal 92
nal92 = "O katerih vprašanjih po Ustavi RS ni dopustno razpisati zakonodajnega referenduma?"
odg92 = ["O zakonih o nujnih ukrepih za zagotovitev obrambe drzave, varnosti ali odprave posledic naravnih nesrec, o zakonih o davkih, carinah in drugih obveznostih dajatvah ter o zakonu, ki se sprejema za izvrsevanje drzavenga proracuna, o zakonih o vatifikaciji mednarodnih pogodb, o zakonih, ki odpravljajo protiustavnost na podrocju clovekovih pravic in temeljnih svobodcin ali drugo protiustavnost"]
drugo92 = [
    "O zakonih o volitvah poslancev, o zakonih o imenovanju ministrov, o zakonih o notranji organizaciji vlade ter o zakonih o delovanju političnih strank",  
    "O zakonih o izobraževanju, o zakonih o zdravstvu, o zakonih o socialnem varstvu ter o zakonih o pokojninskem sistemu",
    "O zakonih o kazenskem postopku, o zakonih o sodnih odločbah, o zakonih o delovanju sodišč ter o zakonih o razlagi ustave"
]
tocke = tocke + naloga(nal92, odg92, drugo92)
print("tvoje stevilo tock: ", tocke)

#nal 93.1
nal93_1 = "Kdo lahko zahteva razpis referenduma o spremembi Ustave RS?"
odg93_1 = ["20 poslancev DZ, vlada, najmanj 30.000 volilcev"]
drugo93_1 = ["Predsednik vlade", "Ustavno sodišče", "Državni svet"]
tocke = tocke + naloga(nal93_1, odg93_1, drugo93_1)
print("tvoje stevilo tock: ", tocke)

#nal 93.2
nal93_2 = "Koliko ustavnorevizijskih referendumov je bilo do sedaj izvedenih v RS?"
odg93_2 = ["Trije"]
drugo93_2 = ["Pet", "Deset", "Noben"]
tocke = tocke + naloga(nal93_2, odg93_2, drugo93_2)
print("tvoje stevilo tock: ", tocke)

#nal 94.1
nal94_1 = "Kdaj je bila sprejeta in razglašena veljavna Ustava RS?"
odg94_1 = ["23. decembra 1991"]
drugo94_1 = ["12. januarja 1990", "7. maja 2000", "3. avgusta 1989"]
tocke = tocke + naloga(nal94_1, odg94_1, drugo94_1)
print("tvoje stevilo tock: ", tocke)

#nal 94.2
nal94_2 = "Kdaj je bila razglašena Temeljna ustavna listina o samostojnosti in neodvisnosti RS?"
odg94_2 = ["25. julija 1991"]
drugo94_2 = ["23. decembra 1991", "12. januarja 1990", "30. februarja 2001"]
tocke = tocke + naloga(nal94_2, odg94_2, drugo94_2)
print("tvoje stevilo tock: ", tocke)

#nal 95
nal95 = "Kaj je preambula?"
odg95 = ["Uvodni del pravnega predpisa (npr. ustave)"]
drugo95 = ["Kazenski del ustave", "Zadnje poglavje ustave", "Dodatek k zakonom"]
tocke = tocke + naloga(nal95, odg95, drugo95)
print("tvoje stevilo tock: ", tocke)

#nal 96
nal96 = "Kako je naslovljeno četrto poglavje Ustave RS?"
odg96 = ["Državna ureditev"]
drugo96 = ["Državni simboli", "Kazensko pravo", "Mednarodni odnosi"]
tocke = tocke + naloga(nal96, odg96, drugo96)
print("tvoje stevilo tock: ", tocke)

#nal 97
nal97 = "Kaj pomeni izraz materia constitutionis?"
odg97 = ["Tvorina ustave - pravna pravila o organizaciji drzavne oblasti + temelji (ustavne pravice)"]
drugo97 = ["Kazenske sankcije", "Upravni postopki", "Volilni sistem"]
tocke = tocke + naloga(nal97, odg97, drugo97)
print("tvoje stevilo tock: ", tocke)

#nal 98
nal98 = "Kdaj za ustavo lahko rečemo, da je toga ustava?"
odg98 = ["Strozji postopek, prepoved spreminjanja nekaterih odlocb, strozji postopek za nekatere dolocbe, ustavnorevizijski organ, ustavnorevizijski referendum"]
drugo98 = ["Če jo sprejme vlada", "Če velja le začasno", "Če jo lahko spreminja vsak zakon"]
tocke = tocke + naloga(nal98, odg98, drugo98)
print("tvoje stevilo tock: ", tocke)

#nal 99.1
nal99_1 = "Katera ustava velja za prvo moderno ustavo?"
odg99_1 = ["Ustava ZDA"]
drugo99_1 = ["Francoska ustava iz leta 1958", "Nemška ustava", "Rimsko pravo"]
tocke = tocke + naloga(nal99_1, odg99_1, drugo99_1)
print("tvoje stevilo tock: ", tocke)

#nal 99.2
nal99_2 = "Kdaj je bila sprejeta prva moderna ustava?"
odg99_2 = ["17. septembra 1787"]
drugo99_2 = ["2. januarja 1918", "1. januarja 1800", "17. septembra 1945"]
tocke = tocke + naloga(nal99_2, odg99_2, drugo99_2)
print("tvoje stevilo tock: ", tocke)

#nal 100.1
nal100_1 = "Kdo trenutno opravlja funkcijo predsednika oziroma predsednice Evropskega sveta?"
odg100_1 = ["António Costa"]
drugo100_1 = ["Ursula von der Leyen", "Roberta Metsola", "Emmanuel Macron"]
tocke = tocke + naloga(nal100_1, odg100_1, drugo100_1)
print("tvoje stevilo tock: ", tocke)

#nal 100.2
nal100_2 = "Kdo trenutno opravlja funkcijo predsednika oziroma predsednice Evropskega parlamenta?"
odg100_2 = ["Roberta Metsola"]
drugo100_2 = ["Charles Michel", "Ursula von der Leyen", "Olaf Scholz"]
tocke = tocke + naloga(nal100_2, odg100_2, drugo100_2)
print("tvoje stevilo tock: ", tocke)

#nal 100.3
nal100_3 = "Kdo trenutno opravlja funkcijo predsednika oziroma predsednice Evropske komisije?"
odg100_3 = ["Ursula von der Leyen"]
drugo100_3 = ["Roberta Metsola", "Charles Michel", "Mark Rutte"]
tocke = tocke + naloga(nal100_3, odg100_3, drugo100_3)
print("tvoje stevilo tock: ", tocke)

#nal 100.4
nal100_4 = "Kdo v aktualni sestavi Evropske komisije zaseda mesto komisarja iz Slovenije?"
odg100_4 = ["Marta Kos"]
drugo100_4 = ["Borut Pahor", "Janez Janša", "Tanja Fajon"]
tocke = tocke + naloga(nal100_4, odg100_4, drugo100_4)

procenti = (tocke / 131) * 100
print(f"izpit si koncal z {tocke}/131 tockami kar je {procenti} procentov")
