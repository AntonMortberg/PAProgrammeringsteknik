from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
from DataManagement import *
import matplotlib
import tkinter as tk
import numpy as np
matplotlib.use("TkAgg")


class Window(tk.Frame):

    def __init__(self, Master):
        super(Window, self).__init__(Master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):  # Här är alla widgetar förutom staplarna
        self.knapp_kanal = tk.Button(self, text="Tittare för en viss kanal", command=self.showval)
        self.knapp_kanal.pack()

        self.knapp_tiotopp = tk.Button(self, text="Tio i topp", command=self.plot)
        self.knapp_tiotopp.pack()

        self.knapp_avbryt = tk.Button(self, text="Avbryt", command=exit)
        self.knapp_avbryt.pack()

        self.kanal = tk.StringVar(self)
        self.kanal.set("Kanal 1")
        val_tuple = ("Kanal 1", "Kanal 2", "Kanal 3", "Kanal 4", "Kanal 5")
        self.val_knapp = tk.OptionMenu(self, self.kanal, *val_tuple, command=self.showstapel)

        self.canvastop = FigureCanvasTkAgg(topteng(), master=self)

    def showval(self):  # funktionerna nedan är för att aktivera/visa widgetarna ovan
        delete(self, self.canvastop.get_tk_widget())
        self.val_knapp.pack()

    def plot(self):
        delete(self)
        self.canvastop.draw()
        self.canvastop.get_tk_widget().pack()

    def showstapel(self, kanal):
        try:
            self.canvas.get_tk_widget().pack_forget()
        except:
            pass

        self.canvas = FigureCanvasTkAgg(stapel(kanal), master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()


def topteng():  # här skapas stapeldiagrammet för topp tio programmen
    indata_list = indata_lista("Kanal och tid")
    program_lista = teveprogram("Kanal och program")
    addtittare(program_lista, indata_list)

    kanal_lista = program_lista
    kanal_lista.sort()
    kanal_lista = kanal_lista[::-1]

    # gör figuren som staplarna ska vara i
    fig = Figure(figsize=(10, 5), dpi=100)

    # säger i princip vad x-axeln och y-axeln ska vara
    ynamn = []
    xtittare = []
    for x in kanal_lista[0:10]:
        ynamn.append(x.namn + "\n" + "(Kanal " + str(x.kanal) + ")")
        xtittare.append(x.tittare)

    # själva diagrammet med staplarna skapas här.
    plot_top = barplot(fig, w=0.2)  # hänvisar till en anna funktion för att minska kodupprepning
    rects = plot_top.barh(ynamn, xtittare)

    label_plot(rects, plot_top)  # skapar siffran som säger hur många tittare varje stapel har

    # för syns skull (diagrammet ser bättre ut och det blir tydligare staplar)
    plot_top.invert_yaxis()
    plot_top.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

    return fig


def stapel(kanal):  # skapar diagrammet för en kanal, ange kanalen.
    indata_list = indata_lista("Kanal och tid")
    program_lista = teveprogram("Kanal och program")
    addtittare(program_lista, indata_list)

    # hämtar ut programmen för kanalen man valde
    i = 0
    stapel_kanal = []
    indataVal = int(kanal[-1])
    for x in program_lista:
        if program_lista[i].kanal == indataVal:
            stapel_kanal.append(program_lista[i])
        i += 1

    # tar ut x och y axlarna
    ynamn = []
    xtittare = []
    for x in stapel_kanal:
        if len(x.namn) > 20:
            ynamn.append(x.namn[0:20] + "...")  # + "\n" + str(x.start) + str(x.stop))
        else:
            ynamn.append(x.namn)  # + "\n" + str(x.start) + "-" +  str(x.stop))
        xtittare.append(x.tittare)

    figch = Figure(figsize=(10, 10), dpi=100)
    x = 0
    while True:
        if indataVal == x:
            plot_ch = barplot(figch, indataVal=x)  # justerar diagramrutan mha en annan funktion
            break
        x += 1

    # Snyggar till diagrammet
    rects = plot_ch.barh(ynamn, xtittare, height=0.5)
    plot_ch.invert_yaxis()
    plot_ch.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
    plot_ch.set_xlabel("Tittare")
    plot_ch.set_title(kanal)

    label_plot(rects, plot_ch)  # skapar siffran som säger hur många tittare varje stapel har

    # sätter dit tiden på högersidan
    p = np.arange(len(ynamn))
    plot_time = plot_ch.twinx()
    plot_time.set_ylim(plot_ch.get_ylim())
    plot_time.set_yticks(p)
    plot_time.set_yticklabels(x.klass_histogram(2) for x in stapel_kanal)
    plot_time.set_ylabel("Sändes (tidpunkt)")

    return figch


# staplarnas ruta justeras
def barplot(fig, indataVal=0, w=0.19, ypos=0.1, xshrink=0.68, yshrink=0.8, xlen=18):
    if indataVal == 5:
        xtick = 2
    else:
        xtick = 10
    x = []
    for p in range(xlen):
        if p < 11:
            x.append(p*xtick)
        else:
            x.append(p*xtick+(p-xtick)*xtick)

    plot = fig.add_axes([w, ypos, xshrink, yshrink])
    plot.set_xticks(x)

    return plot


# skapar siffran som säger hur många tittare varje stapel har, ange staplarna och vilken plot
def label_plot(rects, plot):
    L = []
    for x in plot.get_xlim():
        L.append(int(x))
    L.sort()
    maxwidth = L[1]

    rect_labels = []
    for rect in rects:
        width = rect.get_width()
        if width < (maxwidth/12):
            xloc = 5
            clr = "black"
            align = "left"
        else:
            xloc = -5
            clr = "white"
            align = "right"
        yloc = rect.get_y() + rect.get_height() / 2
        label = plot.annotate(width, xy=(width,yloc), xytext=(xloc, 0), textcoords="offset points", horizontalalignment=align, verticalalignment="center", color=clr, weight="bold", clip_on=True)
        rect_labels.append(label)


def delete(master, name="all"):  # gömmer alla widgetar som man kan öppna om man inte specificerar vilken som ska gömmas.

    if name == "all":
        try:
            master.canvas.get_tk_widget().pack_forget()
        except:
            pass
        try:
            master.canvastop.get_tk_widget().pack_forget()
        except:
            pass
        try:
            master.val_knapp.pack_forget()
        except:
            pass

    else:
        try:
            name.pack_forget()
        except:
            pass


def maing():
    master = tk.Tk()
    master.title("Statistik över tittarsiffror")
    master.geometry("1200x800")
    Window(master)
    tk.mainloop()
