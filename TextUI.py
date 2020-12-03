from DataManagement import *


def topten(programlista, x=0):  # denna funktion printar ut allt när vi vill se topp tio program

    if x == 0:
        kanallista = programlista
        kanallista.sort()
        kanallista = kanallista[::-1]  # vänder på listan, så att programmet med högst tittare är överst. Den sorteras tvärtom

        i = 0
        for p in range(10):  # tar ut sakerna som ska printas och printar bara det
            a = "{0}.".format(i+1)
            namn = kanallista[i].namn
            if len(kanallista[i].namn) > 25:
                namn = kanallista[i].namn[0:25]+"..."
            print("{0:<3s} {1:<30s} {2}".format(a, namn, kanallista[i].tittare))
            i += 1
    else:  # den här är om man vill se topp tio för en viss kanal
        i = 0
        kanallista = []
        for p in programlista:  # så vi sorterar upp programobjekten om de har samma kanal som man valde
            if programlista[i].kanal == x:
                kanallista.append(programlista[i])
            i += 1

        kanallista.sort()  # och fortsätter på samma sätt som om man inte hade valt kanal
        kanallista = kanallista[::-1]

        i = 0
        for p in range(10):
            a = "{0}.".format(i+1)
            namn = kanallista[i].namn
            if len(kanallista[i].namn) > 25:
                namn = kanallista[i].namn[0:25]+"..."
            print("{0:<3s} {1:<30s} {2}".format(a, namn, kanallista[i].tittare))
            i += 1
    return ""


def histogram(programlista, choice=1):  # det här är för att printa staplarna för kanalerna
    i = 0
    channel = []
    print("-----------------------Stapeldiagram över antal tittare, kanal {0}-----------------------".format(choice))
    for x in programlista:
        if programlista[i].kanal == choice:
            channel.append(programlista[i])
            print(programlista[i].histogram())  # objektfunktionen "histogram" ger tillbaka det som ska printas
        i += 1


def specprog(programlista, choice):  # hämtar en kanals tittare till antal och printar
    specchannel = []
    i = 0
    k = 1
    for p in range(len(programlista)):
        if programlista[i].kanal == choice:
            specchannel.append(programlista[p])
            print("{}.".format(k), programlista[p].namn)
            k += 1
        i += 1
    val3 = input("Vilket program vill du se tittarsiffror för? ")
    val3 = failsafe(val3, len(specchannel))
    print(specchannel[val3-1].namn, "hade", specchannel[val3-1].tittare, "tittare")


def failsafe(choice, val):  # gör så att användaren inte kan mata in konstiga saker
    while True:
        while True:
            try:
                choice = int(choice)
                i = 1
                a = 0
                for x in range(val):
                    if choice == i:
                        a = 1
                    i += 1
                if a == 1:
                    break
                else:
                    choice = input("Funkar inte, testa igen:")
            except(ValueError):
                choice = input("Funkar inte, testa igen: ")
        break
    return choice


def main():  # ger essentiellt bara ut menyn, allting annat är i funktioner.
    inputlist = inputlista("Kanal och tid")
    programlista = teveprogram("Kanal och program")
    tittare(programlista, inputlist)
    while True:
        print("Meny", "\n", "1. Se stapeldiagram för en viss kanal." ,"\n", "2. Lista över topp tio program.", "\n", "3. Lista över topp tio för en viss kanal.", "\n", "4. Tittare för en viss kanal.", "\n", "5. Avbryt")
        choice = input("Vad vill du göra? ")
        val1 = failsafe(choice, 5)
        if val1 == 1:
            val2 = input("Vilken kanal?")
            val2 = failsafe(val2, 5)
            still = histogram(programlista, val2)  # ge ut stapeldiagram för alla program i kanalen
        elif val1 == 2:
            #  val2 = input("För vilken kanal? (lämna tom om du vill se för alla) ")
            val2 = 0
            still = topten(programlista, val2)
        elif val1 == 3:
            val2 = input("Vilken kanal? ")
            val2 = failsafe(val2, 5)
            still = topten(programlista, val2)
        elif val1 == 4:
            val2 = input("Vilken kanal är programmet på? ")
            val2 = failsafe(val2, 5)
            still = specprog(programlista, val2)  # just nu: hur ska vi göra så att användaren får se tittarsiffror för ett specifikt program.
        elif val1 == 5:
            exit()  # stapeldiagram för en viss kanal, ta bort exit() i intro fkn
        input("Tryck enter för att återgå. ")
