from DataManagement import *


def topten(tevelista, x=0):
    if x == 0:
        kanallista = tevelista
        kanallista.sort()
        kanallista = kanallista[::-1]
        i = 0
        for p in range(10):
            a = "{0}.".format(i+1)
            namn = kanallista[i].namn
            if len(kanallista[i].namn) > 25:
                namn = kanallista[i].namn[0:25]+"..."
            print("{0:<3s} {1:<30s} {2}".format(a, namn, kanallista[i].tittare))
            i += 1
    else:
        i = 0
        kanallista = []
        for p in tevelista:
            if tevelista[i].kanal == x:
                kanallista.append(tevelista[i])
            i += 1
        kanallista.sort()
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


def histogram(tevelista, choice=1):
    i = 0
    channel = []
    print("-----------------------Stapeldiagram över antal tittare, kanal {0}-----------------------".format(choice))
    for x in tevelista:
        if tevelista[i].kanal == choice:
            channel.append(tevelista[i])
            print(tevelista[i].histogram())
        i += 1


def specprog(tevelista, choice):  # här behöver man välja kanal och program, funderar på om man ska måsta skriva in själv namnet på programmet man vill kolla in, man kanske bara ska få se en lista med möjliga val. Vill göra så att man väljer av en lista i den grafiska versionen.
    #  x är kanalen som programmet är på, måste ha en input som väljer kanal
    specchannel = []
    i = 0
    k = 1
    for p in range(len(tevelista)):
        if tevelista[i].kanal == choice:
            specchannel.append(tevelista[p])
            print("{}.".format(k), tevelista[p].namn)
            k += 1
        i += 1
    val3 = input("Vilket program vill du se tittarsiffror för? ")
    val3 = failsafe(val3, len(specchannel))
    print(specchannel[val3-1].namn, "hade", specchannel[val3-1].tittare, "tittare")


def failsafe(choice, val):  # failsafe for the user
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

def main():
    ilist = inputlista("Kanal och tid")
    tevelista = teveprogram("Kanal och program")
    tittare(tevelista, ilist)
    while True:
        print("Menu", "\n", "1. Se stapeldiagram för en viss kanal." ,"\n", "2. Top ten list.", "\n", "3. Top ten list for a certain channel.", "\n", "4. Viewers for a certain program.", "\n", "5. Quit")
        choice = input("Vad vill du göra? ")
        val1 = failsafe(choice, 5)
        if val1 == 1:
            val2 = input("Vilken kanal?")
            val2 = failsafe(val2, 5)
            still = histogram(tevelista, val2)  # ge ut stapeldiagram för alla program i kanalen
        elif val1 == 2:
            #  val2 = input("För vilken kanal? (lämna tom om du vill se för alla) ")
            val2 = 0
            still = topten(tevelista, val2)
        elif val1 == 3:
            val2 = input("Vilken kanal? ")
            val2 = failsafe(val2, 5)
            still = topten(tevelista, val2)
        elif val1 == 4:
            val2 = input("Vilken kanal är programmet på? ")
            val2 = failsafe(val2, 5)
            still = specprog(tevelista, val2)  # just nu: hur ska vi göra så att användaren får se tittarsiffror för ett specifikt program.
        elif val1 == 5:
            exit()  # stapeldiagram för en viss kanal, ta bort exit() i intro fkn
        input("Tryck enter för att återgå. ")
