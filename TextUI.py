from DataManagement import *


def topten(program_lista, x=0):  # denna funktion printar ut allt när vi vill se topp tio program

    if x == 0:
        kanal_lista = program_lista
        kanal_lista.sort()
        kanal_lista = kanal_lista[::-1]  # vänder på listan, så att programmet med högst tittare är överst. Den sorteras tvärtom

        i = 0
        for p in range(10):  # tar ut sakerna som ska printas och printar bara det
            a = "{0}.".format(i+1)
            namn = kanal_lista[i].namn
            if len(kanal_lista[i].namn) > 25:
                namn = kanal_lista[i].namn[0:25]+"..."
            print("{0:<3s} {1:<30s} {2}".format(a, namn, kanal_lista[i].tittare))
            i += 1
    else:  # den här är om man vill se topp tio för en viss kanal
        i = 0
        kanal_lista = []
        for p in program_lista:  # så vi sorterar upp programobjekten om de har samma kanal som man valde
            if program_lista[i].kanal == x:
                kanal_lista.append(program_lista[i])
            i += 1

        kanal_lista.sort()  # och fortsätter på samma sätt som om man inte hade valt kanal
        kanal_lista = kanal_lista[::-1]

        i = 0
        for p in range(10):
            a = "{0}.".format(i+1)
            namn = kanal_lista[i].namn
            if len(kanal_lista[i].namn) > 25:
                namn = kanal_lista[i].namn[0:25]+"..."
            print("{0:<3s} {1:<30s} {2}".format(a, namn, kanal_lista[i].tittare))
            i += 1
    return ""


def histogram(program_lista, indata_val=1):  # det här är för att printa staplarna för kanalerna
    i = 0
    kanal = []
    print("-----------------------Stapeldiagram över antal tittare, kanal {0}-----------------------".format(indata_val))
    for x in program_lista:
        if program_lista[i].kanal == indata_val:
            kanal.append(program_lista[i])
            print(program_lista[i].klass_histogram(1))  # objektfunktionen "histogram" ger tillbaka det som ska printas
        i += 1


def specprog(program_lista, indata_val):  # hämtar en kanals tittare till antal och printar
    spec_kanal = []
    i = 0
    k = 1
    for p in range(len(program_lista)):
        if program_lista[i].kanal == indata_val:
            spec_kanal.append(program_lista[p])
            print("{}.".format(k), program_lista[p].namn)
            k += 1
        i += 1
    val3 = input("Vilket program vill du se tittarsiffror för? ")
    val3 = feltesta(val3, len(spec_kanal))
    print(spec_kanal[val3-1].namn, "hade", spec_kanal[val3-1].tittare, "tittare")


def feltesta(indata_val, val):  # gör så att användaren inte kan mata in konstiga saker
    while True:
        while True:
            try:
                indata_val = int(indata_val)
                i = 1
                a = 0
                for x in range(val):
                    if indata_val == i:
                        a = 1
                    i += 1
                if a == 1:
                    break
                else:
                    indata_val = input("Funkar inte, testa igen:")
            except(ValueError):
                indata_val = input("Funkar inte, testa igen: ")
        break
    return indata_val


def main():  # ger essentiellt bara ut menyn, allting annat är i funktioner.
    indata_list = indata_lista("Kanal och tid")
    program_lista = teveprogram("Kanal och program")
    addtittare(program_lista, indata_list)
    while True:
        print("Meny", "\n", "1. Se stapeldiagram för en viss kanal." ,"\n", "2. Lista över topp tio program.", "\n", "3. Lista över topp tio för en viss kanal.", "\n", "4. Tittare för en viss kanal.", "\n", "5. Avbryt")
        indata_val = input("Vad vill du göra? ")
        val1 = feltesta(indata_val, 5)
        if val1 == 1:
            val2 = input("Vilken kanal?")
            val2 = feltesta(val2, 5)
            still = histogram(program_lista, val2)  # ge ut stapeldiagram för alla program i kanalen
        elif val1 == 2:
            #  val2 = input("För vilken kanal? (lämna tom om du vill se för alla) ")
            val2 = 0
            still = topten(program_lista, val2)
        elif val1 == 3:
            val2 = input("Vilken kanal? ")
            val2 = feltesta(val2, 5)
            still = topten(program_lista, val2)
        elif val1 == 4:
            val2 = input("Vilken kanal är programmet på? ")
            val2 = feltesta(val2, 5)
            still = specprog(program_lista, val2)  # just nu: hur ska vi göra så att användaren får se tittarsiffror för ett specifikt program.
        elif val1 == 5:
            exit()  # stapeldiagram för en viss kanal, ta bort exit() i intro fkn
        input("Tryck enter för att återgå. ")
