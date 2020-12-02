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

    def create_widgets(self):
        self.button1 = tk.Button(self, text="Viewers for a channel", command=self.showoption)
        self.button1.pack()

        self.button2 = tk.Button(self, text="Top ten programs", command=self.plot)
        self.button2.pack()

        self.button3 = tk.Button(self, text="Exit", command=exit)
        self.button3.pack()

        self.channel = tk.StringVar(self)
        self.channel.set("Channel 1")
        option_tuple = ("Channel 1", "Channel 2", "Channel 3", "Channel 4", "Channel 5")
        self.radiobutton = tk.OptionMenu(self, self.channel, *option_tuple, command=self.showstaple)

        self.canvastop = FigureCanvasTkAgg(topteng(), master=self)

    def showoption(self):
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


def topteng(x=0):
    ilist = inputlista("Kanal och tid")
    tevelista = teveprogram("Kanal och program")
    tittare(tevelista, ilist)

    kanallista = tevelista
    kanallista.sort()
    kanallista = kanallista[::-1]

    fig = Figure(figsize=(10, 5), dpi=100)

    ynames = []
    xviewers = []
    for x in kanallista[0:10]:
        ynames.append(x.namn + "\n" + "(Channel " + str(x.kanal) + ")")
        xviewers.append(x.tittare)

    plot_top = barplot(fig, w=0.2)
    rects = plot_top.barh(ynames, xviewers)

    L = []
    for x in plot_top.get_xlim():
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
        label = plot_top.annotate(width, xy=(width,yloc), xytext=(xloc, 0), textcoords="offset points", horizontalalignment=align, verticalalignment="center", color=clr, weight="bold", clip_on=True)
        rect_labels.append(label)

    plot_top.invert_yaxis()
    plot_top.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

    return fig


def staple(channel):
    ilist = inputlista("Kanal och tid")
    tevelista = teveprogram("Kanal och program")
    tittare(tevelista, ilist)

    i = 0
    staple_channel = []
    choice = int(channel[-1])
    for x in tevelista:
        if tevelista[i].kanal == choice:
            staple_channel.append(tevelista[i])
        i += 1

    ynames = []
    xviewers = []
    for x in staple_channel:
        if len(x.namn) > 20:
            ynames.append(x.namn[0:20] + "...")  # + "\n" + str(x.start) + str(x.stop))
        else:
            ynames.append(x.namn)  # + "\n" + str(x.start) + "-" +  str(x.stop))
        xviewers.append(x.tittare)

    figch = Figure(figsize=(10, 10), dpi=100)
    if choice == 1:
        plot_ch = barplot(figch)
    elif choice == 2:
        plot_ch = barplot(figch)
    elif choice == 3:
        plot_ch = barplot(figch)
    elif choice == 4:
        plot_ch = barplot(figch)
    else:
        plot_ch = barplot(figch, xtick=2)

    rects = plot_ch.barh(ynames, xviewers, height=0.5)
    plot_ch.invert_yaxis()
    plot_ch.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
    plot_ch.set_xlabel("Viewers")
    plot_ch.set_title(channel)

    L = []
    for x in plot_ch.get_xlim():
        L.append(int(x))
    L.sort()
    maxwidth = L[1]

    for rect in rects:

        width = rect.get_width()
        if width < (maxwidth/10):
            xloc = 5
            clr = "black"
            align = "left"
        else:
            xloc = -5
            clr = "white"
            align = "right"

        yloc = rect.get_y() + rect.get_height() / 2
        label = plot_ch.annotate(width, xy=(width,yloc), xytext=(xloc, 0), textcoords="offset points", horizontalalignment=align, verticalalignment="center", color=clr, weight="bold", clip_on=True)

    p = np.arange(len(ynames))
    plot_time = plot_ch.twinx()
    plot_time.set_ylim(plot_ch.get_ylim())
    plot_time.set_yticks(p)
    plot_time.set_yticklabels(str(x.start) + "-" + str(x.stop) for x in staple_channel)
    plot_time.set_ylabel("Time aired")

    return figch


def barplot(fig, w=0.19, ypos=0.1, xshrink=0.7, yshrink=0.8, xtick=10, xlen=18):

    x = []
    for p in range(xlen):
        if p < 11:
            x.append(p*xtick)
        else:
            x.append(p*xtick+(p-xtick)*xtick)

    plot = fig.add_axes([w, ypos, xshrink, yshrink])
    plot.set_xticks(x)

    return plot


def delete(master, name="all"):

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
    master.title("meny ett")
    master.geometry("1200x800")
    Window(master)
    tk.mainloop()
