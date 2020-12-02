

class program:

    def __init__(self, namn, kanal, start, stop, tittare=0):
        self.kanal = kanal  # int
        self.start = start  # int
        self.stop = stop    # int
        self.namn = namn    # str
        self.tittare = tittare  # int

    def __eq__(self, other):  # om en viss tid är inom ramarna av programmets tid så kommer den att returna true.
        if self.start < other < self.stop:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.tittare < other.tittare

    def __gt__(self, other):
        return self.start > other.start

    def plusviewer(self):
        self.tittare += 1

    def histogram(self):
        start = str(self.start)
        stop = str(self.stop)
        if len(start) == 4:
            start = start[0:2]+"."+start[2:4]
        elif len(start) == 3:
            start = start[0:1]+"."+start[1:3]
        if len(stop) == 4:
            stop = stop[0:2]+"."+stop[2:4]
        elif len(stop) == 3:
            stop = stop[0:1]+"."+stop[1:3]
        namn = self.namn
        if len(self.namn) > 30:
            namn = self.namn[0:28]+"..."
        viewers = int(round(self.tittare*0.9, 0))*"*"
        tittare = "("+str(self.tittare)+")"
        return "{0} {1:>5s} - {2:>5s} {3:<35s} {5:<5} |{4}".format(" ", start, stop, namn, viewers, tittare)


    def info(self):
        return "Kanal:  {0}  Startar:   {1}    Slutar:  {2}     Tittare:    {4}    Namn: {3} ".format(self.kanal, self.start, self.stop, self.namn, self.tittare)
