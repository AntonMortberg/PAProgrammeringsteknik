from ProgramClass import program


def inputlista(doc):  # det här skapar en lista, där varje index är en tv-apparat som innehåller tiderna som en apparat är inne och vilken kanal i den tidpunkten.
    kati = open(doc, "r")
    readkati = kati.read()
    inputlista = readkati.split("-------")
    k = list(inputlista[0])
    while True:
        if k[0] == "0" or k[0] == "1" or k[0] == "2":
            break
        else:
            del k[0]
            continue
    k = "".join(k)
    inputlista[0] = k
    kati.close()
    i = 0
    for x in range(len(inputlista)): # gör en list där varje index är en apparat och varje index i apparaten är tidpunkt och kanal
        inputlista[i] = inputlista[i].split("\n")
        if inputlista[i][0] == "":
            inputlista[i].pop(0)
        if inputlista[i][-1] == "":
            inputlista[i].pop(-1)
        k = 0
        for p in range(len(inputlista[i])):
            inputlista[i][k] = inputlista[i][k].replace(".", "")
            inputlista[i][k] = inputlista[i][k].split("/")
            k += 1
        i += 1

    return inputlista  # får ut en 3d lista med L[x] = apparat, L[x][x] = varje registrering och L[x][x][k] = k=1 är tidpunkt och k=2 är kanal


def teveprogram(doc):  # here we create a list with all the programs as objects
    kapr = open(doc, "r")
    readkapr = kapr.read()
    tevelista = readkapr.split("------------------------------------------------------------------")
    tevelista.pop(-1)

    i = 0
    for x in range(len(tevelista)):  # efter den här har vi en lista för varje kanal
        k = list(tevelista[i])
        while True:
            if k[0] == "0" or k[0] == "1" or k[0] == "2" or k[0] == "3" or k[0] == "4" or k[0] == "5":
                break
            else:
                del k[0]
                continue
        k = "".join(k)
        tevelista[i] = k
        i += 1

    i = 0
    for x in range(len(tevelista)):  # här är varje index en kanal, varje index för kanalerna är programmen där varje index i den listan är 1. start, 2. stop, 3. namn på programmet
        tevelista[i] = tevelista[i].split("\n")
        tevelista[i].pop(0)
        k = 0
        for p in range(len(tevelista[i])):
            tevelista[i][k] = tevelista[i][k].replace(".", "")
            tevelista[i][k] = tevelista[i][k].split(" ", 1)
            a = tevelista[i][k][-1]
            tevelista[i][k] = tevelista[i][k][0].split("-")
            tevelista[i][k].append(a)
            k += 1
        i += 1

    i = 0
    teve2 = []
    for x in range(len(tevelista)):
        j = 0
        tevelista[i].pop(-1)
        for p in range(len(tevelista[i])):
            program1 = program(tevelista[i][j][2], i+1, int(tevelista[i][j][0]), int(tevelista[i][j][1]))
            teve2.append(program1)
            j += 1
        i += 1
    return teve2

def tittare(tevelista, ilist):
    for i in range(len(ilist)):
        for p in range(len(ilist[i])):
            a = 0
            for k in range(len(tevelista)):
                if tevelista[k] == int(ilist[i][p][0]) and tevelista[k].kanal == int(ilist[i][p][1]):
                    tevelista[k].plusviewer()

    z = 0
#    for x in tevelista:
#        print(tevelista[z].info())
#        z += 1
    return tevelista
