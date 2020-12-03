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
        self.button1 = tk.Button(self, text="Tittare för en viss kanal", command=self.showoption)
        self.button1.pack()

        self.button2 = tk.Button(self, text="Tio i topp", command=self.plot)
        self.button2.pack()

        self.button3 = tk.Button(self, text="Avbryt", command=exit)
        self.button3.pack()

        self.channel = tk.StringVar(self)
        self.channel.set("Kanal 1")
        option_tuple = ("Kanal 1", "Kanal 2", "Kanal 3", "Kanal 4", "Kanal 5")
        self.radiobutton = tk.OptionMenu(self, self.channel, *option_tuple, command=self.showstaple)

        self.canvastop = FigureCanvasTkAgg(topteng(), master=self)

    def showoption(self):  # funktionerna nedan är för att aktivera/visa widgetarna ovan
        delete(self, self.canvastop.get_tk_widget())
        self.radiobutton.pack()

    def plot(self):
        delete(self)
        self.canvastop.draw()
        self.canvastop.get_tk_widget().pack()

    def showstaple(self, channel):
        try:
            self.canvas.get_tk_widget().pack_forget()
        except:
            pass

        self.canvas = FigureCanvasTkAgg(staple(channel), master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()


def topteng(x=0):  # här skapas stapeldiagrammet för topp tio programmen
    inputlist = inputlista("Kanal och tid")
    programlista = teveprogram("Kanal och program")
    tittare(programlista, inputlist)

    kanallista = programlista
    kanallista.sort()
    kanallista = kanallista[::-1]

    # gör figuren som staplarna ska vara i
    fig = Figure(figsize=(10, 5), dpi=100)

    # säger i princip vad x-axeln och y-axeln ska vara
    ynames = []
    xviewers = []
    for x in kanallista[0:10]:
        ynames.append(x.namn + "\n" + "(Kanal " + str(x.kanal) + ")")
        xviewers.append(x.tittare)

    # själva diagrammet med staplarna skapas här.
    plot_top = barplot(fig, w=0.2)  # hänvisar till en anna funktion för att minska kodupprepning
    rects = plot_top.barh(ynames, xviewers)

    label_plot(rects, plot_top)  # skapar siffran som säger hur många tittare varje stapel har

    # för syns skull (diagrammet ser bättre ut och det blir tydligare staplar)
    plot_top.invert_yaxis()
    plot_top.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

    return fig


def staple(channel):  # diagrammet för enskilda kanalerna
    inputlist = inputlista("Kanal och tid")
    programlista = teveprogram("Kanal och program")
    tittare(programlista, inputlist)

    # hämtar ut programmen för kanalen man valde
    i = 0
    staple_channel = []
    choice = int(channel[-1])
    for x in programlista:
        if programlista[i].kanal == choice:
            staple_channel.append(programlista[i])
        i += 1

    # tar ut x och y axlarna
    ynames = []
    xviewers = []
    for x in staple_channel:
        if len(x.namn) > 20:
            ynames.append(x.namn[0:20] + "...")  # + "\n" + str(x.start) + str(x.stop))
        else:
            ynames.append(x.namn)  # + "\n" + str(x.start) + "-" +  str(x.stop))
        xviewers.append(x.tittare)

    figch = Figure(figsize=(10, 10), dpi=100)
    x = 0
    for x in range(6):
        if choice == x:
            plot_ch = barplot(figch, choice=x)  # justerar diagramrutan mha en annan funktion

    # Snyggar till diagrammet
    rects = plot_ch.barh(ynames, xviewers, height=0.5)
    plot_ch.invert_yaxis()
    plot_ch.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
    plot_ch.set_xlabel("Tittare")
    plot_ch.set_title(channel)

    label_plot(rects, plot_ch)  # skapar siffran som säger hur många tittare varje stapel har

    # sätter dit tiden på högersidan
    p = np.arange(len(ynames))
    plot_time = plot_ch.twinx()
    plot_time.set_ylim(plot_ch.get_ylim())
    plot_time.set_yticks(p)
    plot_time.set_yticklabels(str(x.start) + "-" + str(x.stop) for x in staple_channel)
    plot_time.set_ylabel("Sändes (tidpunkt)")

    return figch


def barplot(fig, choice=0, w=0.19, ypos=0.1, xshrink=0.7, yshrink=0.8, xlen=18):  # staplarnas ruta justeras
    if choice == 5:
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


# skapar siffran som säger hur många tittare varje stapel har
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


def delete(master, name="all"):  # ett sätt att inte få alla grafiska widgetar ovan på varandra

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
            master.radiobutton.pack_forget()
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
