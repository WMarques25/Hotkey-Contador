# Interface
# -*- coding: UTF-8 -*-

from tkinter import *

class FrameHK(Frame):
    def __init__(self, master):
        super().__init__()
        self['bg'] = 'light blue'
        self['bd'] = 5
        self['relief'] = SUNKEN
        self['padx'] = 30
        self['pady'] = 8
        self['height'] = 50


def ConcluirHKs():          # Função salvar.
    with open('Hotkey.txt','w') as f:
        f.write(HKp.get() +"\n"+ HKm.get() +"\n"+ HKz.get())


# Janela
janela = Tk()
janela.title("")

with open('Hotkey.txt','r') as f:
        HKp2 = f.readline()
        HKm2 = f.readline()
        HKz2 = f.readline()
        HKp2 = HKp2[:-1]  #Limpando o '\n' das linhas em "Hotkey.txt"
        HKm2 = HKm2[:-1]

# Atribuindo as strings para as StringVars
HKp = StringVar()
HKp.set(HKp2)
HKm = StringVar()
HKm.set(HKm2)
HKz = StringVar()
HKz.set(HKz2)
HKp3 = StringVar()
HKp3.set("AaAa") 

# Frame HKs
FrameHKs = FrameHK(janela)
TituloHKs = Label(FrameHKs, text="HOTKEYS GRAVADAS")    # modificar formatação usar 2 colunas
TituloHKs.grid(row=0, column=0)

HKp_label = Label(FrameHKs, text="Cont+1 : ").grid(row=1)          # Formatar as linhas
HKp_entry = Entry(FrameHKs, textvariable=HKp).grid(column=1, row=1)

HKm_label = Label(FrameHKs, text="Cont-1 : ").grid(row=2)
HKm_entry = Entry(FrameHKs, textvariable=HKm).grid(column=1, row=2)

HKz_label = Label(FrameHKs, text="Cont=0 : ").grid(row=3)
HKz_entry = Entry(FrameHKs, textvariable=HKz).grid(column=1, row=3)

ConcluirButton = Button(FrameHKs, text="ConcluirHKs", command=ConcluirHKs).grid(row=4, column=2)

# Acrescentar opção para alterar as HK desabilitando td a frame

FrameHKs.grid(column=0, row=0, padx=10, pady=2)

# Frame Contador
FrameCont = FrameHK(janela)
FrameCont.grid(column=1, row=0, padx=10, pady=2)

# Geometry
TelaX = janela.winfo_screenwidth()
TelaY = janela.winfo_screenheight()
JanelaX = TelaX/3
JanelaY = TelaY/3
JanelaPosx = TelaX/2 - JanelaX/2
JanelaPosy = TelaY/2 -(JanelaY/2 + 80)
janela.geometry("%dx%d+%d+%d" % (JanelaX, JanelaY, JanelaPosx, JanelaPosy))
