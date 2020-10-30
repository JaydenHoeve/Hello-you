# Variabelen
Ja = ["Ja"]
Nee = ["Nee"]
Europa = ["Europa"]
Buurtland = ["Buurtland"]
Snel = ["Snellere"]
Veilig = ["Veilige"]
Egypte = ["Egypte"]
Door = ["Door"]
Overnachten = ["Overnachten"]

#-------hier worden de functions gedefined

def verhaal_1():
    keuze = input("Ga je op zoek naar je familie?   Ja / Nee ")


    if keuze == 'Ja':
        print("Je gaat opzoek naar je familie")
        verhaal_2()
        
    elif keuze == 'Nee':
        print("Je gaat niet opzoek naar je familie")
        verhaal_3()
        
    else:
        print("dit is geen geldige keuze antwoord met Ja of Nee")
        verhaal_1()

def verhaal_2():
    print("zoek familie")
    
    keuze = input("Je hebt je familie gevonden en je hebt met ze gepraat en besluit om te gaan vluvhten naar een land waar het veilig is ga je je familie mee vragen? Ja / Nee ")

    if keuze == 'Ja':
        print("Ja je neemt je familie mee naar een veilig land")
        verhaal_4()

    elif keuze == 'Nee':
        print("Je neemt je familie niet mee naar een ander land")
        verhaal_5()

    else:
        print("dit is geen geldige keuze antwoord met Ja of Nee")
        verhaal_2()
        

def verhaal_3():
    print("de familie ga ik niet zoeken, ik ga vluchten")

    keuze = input("Je besluit meteen te gaan vluvhten en niet naar je familie opzoek te gaan ga je eerst naar spullen zoeken om mee te nemen tijdens de reis zoals eten en drinken? Ja / nee ")

    if keuze == 'Ja':
        print("Je zoekt rond je huis of er nog iets is wat je mee kan nemen en gaat dan weg ")
        verhaal_6()

    elif keuze == 'Nee':
        print("Je wacht geen seconde en gaat meteen weg")
        verhaal_7()

    else:
        print("dit is geen geldige keuze antwoord met Ja of Nee")
        verhaal_3()
    


def verhaal_4():
    keuze = input("Je besluit je familie mee te nemen en samen te gaan vluchten waar ga je heen? Europa / Ergens naar het buurtland ")


    if keuze == 'Europa':
        print("Je besluit naar Europa te gaan met je familie")
        verhaal_8()

    elif keuze == 'Buurtland':
        print("Je besluit om ergens naar 1 van de buurt landen te gaan waar het veiliger is")
        verhaal_9()

    else:
        print("dit is geen geldige keuze antwoord met Europa of Ergens naar het buurtland")
        verhaal_4()


def verhaal_5():
    print("Je besluit je familie hier achter te laten en zelf te gaan vluvhten")
    keuze = input("Je hebt van je familie afschijd genomen en bent weg gegaan alleen zit je nu te denken waar je heen zou gaan? Europa / ergens naar het buurtland ")

    if keuze == 'Europa':
        print("Je besluit naar Europa te gaan")
        verhaal_10()

    elif keuze == 'Buurtland':
        print("Je besluit om ergens naar 1 van de buurt landen te gaan waar het veiliger is ")
        verhaal_11()

    else:
        print("dit is geen geldige keuze antwoord met Europa of Ergens naar het buurtland")
        verhaal_5()

def verhaal_6():
    print("Je hebt wat eten en wat drinken gevonden en gaat nu weg")
    keuze = input("Je hebt besloten dat je naar Europa gaat maar weet niet welke route? Neem je een snellere route maar wat wel gevaarlijker is / Neem je de langere route maar die veiliger is ")

    if keuze == 'Snellere':
        print("Je besluit de snele maar ook gevaarlijkere weg te nemen naar Europa")
        verhaal_12()

    elif keuze == 'Veilige':
        print("Je besluit om de veilige route te nemen maar er wel langer over te doen")
        verhaal_13()

    else:
        print("dit is geen geldige keuze antwoord met snelere weg of veilige weg")
        verhaal_6()

def verhaal_7():
    keuze = input("Je heb geen seconde gewacht en wilt richting Europa gaan maar neem je de snele route of de veilige ")

    if keuze == 'Snellere':
        print("Je besluit de snele maar ook gevaarlijkere weg te nemen naar Europa")
        verhaal_14()

    elif keuze == 'Veilige':
        print("Je besluit om de veilige route te nemen maar er wel langer over te doen")
        verhaal_15()

    else:
        print("dit is geen geldige keuze antwoord met snelere weg of veilige weg")
        verhaal_7()

def verhaal_8():
    keuze = input("Je neemt je familie mee naar Europa neem je de snellere route of de veiligere route")

    if keuze == 'Snellere':
        print("Je besluit de snele maar ook gevaarlijkere weg te nemen naar Europa")
        verhaal_16()

    elif keuze == 'Veilige':
        print("Je besluit om de veilige route te nemen maar er wel langer over te doen")
        verhaal_17()

    else:
        print("dit is geen geldige keuze antwoord met snelere weg of veilige weg")
        verhaal_8()

def verhaal_9():
    keuze = input("Je gaat met je familie naar 1 van de buurt landen ga je naar Egypte / Saudi Arabië?")

    if keuze == 'Egypte':
        print("Je besluit de snele maar ook gevaarlijkere weg te nemen naar Europa")
        verhaal_18()

    elif keuze == 'Saudie Arabië':
        print("Je besluit om de veilige route te nemen maar er wel langer over te doen")
        verhaal_19()

    else:
        print("dit is geen geldige keuze antwoord met Egypte of Saudie Arabië")
        verhaal_9()

def verhaal_10():
    keuze = input("Je gaat met je familie naar Europa en gaat warschijnlijk naar Turkijë welke weg neem je? de snellere weg / de veilige weg")

    if keuze == 'snellere':
        print("Je besluit de snele maar ook gevaarlijkere weg te nemen naar Europa")
        verhaal_20()

    elif keuze == 'veilige':
        print("Je besluit om de veilige route te nemen maar er wel langer over te doen")
        verhaal_21()

    else:
        print("dit is geen geldige keuze antwoord met snelere weg of veilige weg")
        verhaal_10()

def verhaal_11():
    print("Je heb besloten naar Saudi Arabië te gaan en daar een paar jaar te blijven en te werken en uiteindelijk ga je terug naar je land met al het geld dat je hebt gemaakt en help je familie weer over eind te komen.")
    print("EINDE")


def verhaal_12():
    keuze = input("Je hebt besloten de snellere weg te nemen naar Europa en komt een stadje tegen ga je daar overnachten of ga je nog de hele nacht door")

    if keuze == 'Door':
        print("Je besluit de nacht door te gaan")
        verhaal_22()

    elif keuze == 'Overnachten':
        print("Je besluit om te gaan overnachten in het stadje wat je bent tegen bent gekomen")
        verhaal_23()

    else:
        print("dit is geen geldige keuze antwoord met door of overnachten")
        verhaal_12()

def verhaal_13():
    keuze = input("Je hebt voor de langere route gekozen en doet er uit eindelijk langer over om naar Europa te komen maar je komt en stadje tegen kies je ervoor om daar een slaap plek te regelen of ga je door")
    
    if keuze == 'Door':
        print("Je besluit de nacht door te gaan")
        verhaal_24()

    elif keuze == 'Overnachten':
        print("Je besluit om te gaan overnachten in het stadje wat je bent tegen bent gekomen")
        verhaal_25()

    else:
        print("dit is geen geldige keuze antwoord met door of overnachten")
        verhaal_13()

def verhaal_14():
    keuze = input("Je bent voor de snellere route gegaan en wilt zo snel mogelijk naar Turkijë en 

    

# ---------- hier start de main -------------
    
keuze = input("klik op enter om te starten")


print("Ik woon in een mooi wit huis met je gezin")
print("Op een dag ging ik naar mijn werk en toen was mijn huis weg")
verhaal_1()

