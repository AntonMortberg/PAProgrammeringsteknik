from ProgramClass import program


def inputlista(doc):  # det här skapar en lista, där varje index är en tv-apparat som innehåller tiderna som en apparat är inne och vilken kanal i den tidpunkten.
    kannaltid = open(doc, "r")
    readkannaltid = kannaltid.read()
    inputlista = readkannaltid.split("-------")
    k = list(inputlista[0])

    while True:  # tar bort allt skräp innan siffrorna som jag vill ha.
        if k[0] == "0" or k[0] == "1" or k[0] == "2":
            break
        else:
            del k[0]
            continue
    k = "".join(k)
    inputlista[0] = k
    kannaltid.close()

    i = 0
    for x in range(len(inputlista)):  # gör en list där varje index är en apparat och varje index i apparaten är tidpunkt och kanal
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
    kannalprogram = open(doc, "r")
    readkannalprogram = kannalprogram.read()
    programlista = readkannalprogram.split("------------------------------------------------------------------")
    programlista.pop(-1)

    i = 0
    for x in range(len(programlista)):  # efter den här har vi en lista för varje kanal, vilket betyder att vi tar bort skräp i denna loop
        k = list(programlista[i])
        while True:
            if k[0] == "0" or k[0] == "1" or k[0] == "2" or k[0] == "3" or k[0] == "4" or k[0] == "5":
                break
            else:
                del k[0]
                continue
        k = "".join(k)
        programlista[i] = k
        i += 1

    i = 0
    for x in range(len(programlista)):  # här är varje index en kanal, varje index för kanalerna är programmen där varje index i den listan är 1. start, 2. stop, 3. namn på programmet
        programlista[i] = programlista[i].split("\n")
        programlista[i].pop(0)
        k = 0
        for p in range(len(programlista[i])):
            programlista[i][k] = programlista[i][k].replace(".", "")
            programlista[i][k] = programlista[i][k].split(" ", 1)
            a = programlista[i][k][-1]
            programlista[i][k] = programlista[i][k][0].split("-")
            programlista[i][k].append(a)
            k += 1
        i += 1

    i = 0
    teve2 = []
    for x in range(len(programlista)):  # här skapas programobjekten.
        j = 0
        programlista[i].pop(-1)
        for p in range(len(programlista[i])):
            program1 = program(programlista[i][j][2], i+1, int(programlista[i][j][0]), int(programlista[i][j][1]))
            teve2.append(program1)
            j += 1
        i += 1
    return teve2


def tittare(programlista, ilist):  # Varje programobjekt är utan tittare i början, så här plussar vi på tittare för varje log som är inom programmet start och stopp
    for i in range(len(ilist)):
        for p in range(len(ilist[i])):
            a = 0
            for k in range(len(programlista)):
                if programlista[k] == int(ilist[i][p][0]) and programlista[k].kanal == int(ilist[i][p][1]):
                    programlista[k].plusviewer()

    return programlista
