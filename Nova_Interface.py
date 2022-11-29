# Interface
# -*- coding: Windows_1252 -*-

from tkinter import *

class Frames(Frame):
    def __init__(self, master):
        super().__init__()
    # Definir formatação das frames

class linhaHKs(Label):
    def __init__(self, master):
        super().__init__()
    # Definir formatação das linhas de alteração das HKs

# Janela
janela = Tk()
janela.title("")

# Frame HKs
FrameHKs = Frame(janela, 
                 background="light blue",
                 borderwidth=5,
                 relief="sunken",
                 padx=30,
                 pady=8)
TituloHKs = Label(FrameHKs, text="HOTKEYS GRAVADAS")
TituloHKs.pack()
FrameHKs.grid(column=0, row=0, padx=10, pady=2)

# Frame Contador
FrameCont = Frames(janela)
FrameCont.grid(column=1, row=0,padx=10, pady=2)

# Geometry
TelaX = janela.winfo_screenwidth()
TelaY = janela.winfo_screenheight()
JanelaX = TelaX/3
JanelaY = TelaY/3
JanelaPosx = TelaX/2 - JanelaX/2
JanelaPosy = TelaY/2 -(JanelaY/2 + 80)
janela.geometry("%dx%d+%d+%d" % (JanelaX, JanelaY, JanelaPosx, JanelaPosy))
