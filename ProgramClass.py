

class Program:

    def __init__(self, namn, kanal, start, stopp, tittare=0):
        self.kanal = kanal  # int
        self.start = start  # int
        self.stopp = stopp    # int
        self.namn = namn    # str
        self.tittare = tittare  # int

    def __eq__(self, andra):  # om en viss tid är inom ramarna av programmets tid så kommer den att returna true.
        if self.start < andra < self.stopp:
            return True
        else:
            return False

    def __lt__(self, andra):
        return self.tittare < andra.tittare

    def __gt__(self, andra):
        return self.start > andra.start

    def adderaTittare(self):
        self.tittare += 1

    def klass_histogram(self, val):
        start = str(self.start)
        stopp = str(self.stopp)
        if len(start) == 4:
            start = start[0:2]+"."+start[2:4]
        elif len(start) == 3:
            start = start[0:1]+"."+start[1:3]
        if len(stopp) == 4:
            stopp = stopp[0:2]+"."+stopp[2:4]
        elif len(stopp) == 3:
            stopp = stopp[0:1]+"."+stopp[1:3]
        namn = self.namn
        if len(self.namn) > 30:
            namn = self.namn[0:28]+"..."
        viewers = int(round(self.tittare*0.9, 0))*"*"
        tittare = "("+str(self.tittare)+")"
        if val == 1:
            return "{0} {1:>5s} - {2:>5s} {3:<35s} {5:<5} |{4}".format(" ", start, stopp, namn, viewers, tittare)
        else:
            return "{0} {1:>5s} - {2:>5s}".format(" ", start, stopp)

    def info(self):
        return "Kanal:  {0}  Startar:   {1}    Slutar:  {2}     Tittare:    {4}    Namn: {3} ".format(self.kanal, self.start, self.stopp, self.namn, self.tittare)
