from ProgramClass import Program


def indata_lista(text_fil):  # det här skapar en lista, där varje index är en tv-apparat som innehåller tiderna som en apparat är inne och vilken kanal i den tidpunkten.
    kanal_TidText = open(text_fil, "r")
    readKanal_TidText = kanal_TidText.read()
    indata_lista = readKanal_TidText.split("-------")
    k = list(indata_lista[0])

    while True:  # tar bort allt skräp innan siffrorna som jag vill ha.
        if k[0] == "0" or k[0] == "1" or k[0] == "2":
            break
        else:
            del k[0]
            continue
    k = "".join(k)
    indata_lista[0] = k
    kanal_TidText.close()

    i = 0
    for x in range(len(indata_lista)):  # gör en list där varje index är en apparat och varje index i apparaten är tidpunkt och kanal
        indata_lista[i] = indata_lista[i].split("\n")
        if indata_lista[i][0] == "":
            indata_lista[i].pop(0)
        if indata_lista[i][-1] == "":
            indata_lista[i].pop(-1)
        k = 0
        for p in range(len(indata_lista[i])):
            indata_lista[i][k] = indata_lista[i][k].replace(".", "")
            indata_lista[i][k] = indata_lista[i][k].split("/")
            k += 1
        i += 1

    return indata_lista  # får ut en 3d lista med L[x] = apparat, L[x][x] = varje registrering och L[x][x][k] = k=1 är tidpunkt och k=2 är kanal


def teveprogram(text_fil):  # Här skapas en lista med programobjekt
    kanal_ProgramText = open(text_fil, "r")
    readKanal_ProgramText = kanal_ProgramText.read()
    program_lista = readKanal_ProgramText.split("------------------------------------------------------------------")
    program_lista.pop(-1)

    i = 0
    for x in range(len(program_lista)):  # efter den här har vi en lista för varje kanal, vilket betyder att vi tar bort skräp i denna loop
        k = list(program_lista[i])
        while True:
            if k[0] == "0" or k[0] == "1" or k[0] == "2" or k[0] == "3" or k[0] == "4" or k[0] == "5":
                break
            else:
                del k[0]
                continue
        k = "".join(k)
        program_lista[i] = k
        i += 1

    i = 0
    for x in range(len(program_lista)):  # här är varje index en kanal, varje index för kanalerna är programmen där varje index i den listan är 1. start, 2. stop, 3. namn på programmet
        program_lista[i] = program_lista[i].split("\n")
        program_lista[i].pop(0)
        k = 0
        for p in range(len(program_lista[i])):
            program_lista[i][k] = program_lista[i][k].replace(".", "")
            program_lista[i][k] = program_lista[i][k].split(" ", 1)
            a = program_lista[i][k][-1]
            program_lista[i][k] = program_lista[i][k][0].split("-")
            program_lista[i][k].append(a)
            k += 1
        i += 1

    i = 0
    finalPrg_lista = []
    for x in range(len(program_lista)):  # här skapas programobjekten.
        j = 0
        program_lista[i].pop(-1)
        for p in range(len(program_lista[i])):
            program1 = Program(program_lista[i][j][2], i+1, int(program_lista[i][j][0]), int(program_lista[i][j][1]))
            finalPrg_lista.append(program1)
            j += 1
        i += 1
    return finalPrg_lista


def addtittare(program_lista, indata_listan):  # Varje programobjekt är utan tittare i början, så här plussar vi på tittare för varje log som är inom programmet start och stopp
    for i in range(len(indata_listan)):
        for p in range(len(indata_listan[i])):
            a = 0
            for k in range(len(program_lista)):
                if program_lista[k] == int(indata_listan[i][p][0]) and program_lista[k].kanal == int(indata_listan[i][p][1]):
                    program_lista[k].adderaTittare()

    return program_lista
