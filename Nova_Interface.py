# Interface
# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import ttk
import logging

logging.basicConfig(filename="LogCont.log", format="%(message)s")

class FrameHK(Frame):
    def __init__(self, master):
        super().__init__()
        self['bg'] = 'light blue'
        self['bd'] = 5
        self['relief'] = SUNKEN
        self['padx'] = 10
        self['pady'] = 8
        self['height'] = 50
        

def ConcluirHKs():          # Função salvar.
    with open('Hotkey.txt','w') as f:
        f.write(HKp.get() +"\n"+ HKm.get() +"\n"+ HKz.get())
    
    # Desabilitar Frame inteira + Botão externo para Habilitar
    for child in FrameHKs.winfo_children():
        child.configure(state='disabled')       # Funcionando, Fazer o  mesmo pra ligar a edição
    AltButton.configure(state='normal')

def AltHKs():               # Função para alterar as Hks
    for child in FrameHKs.winfo_children():
        child.configure(state='normal')
    AltButton.configure(state='disabled')
    
    
## Janela
janela = Tk()
janela.title("")

with open('Hotkey.txt','r') as f:
        HKp2 = f.readline()
        HKm2 = f.readline()
        HKz2 = f.readline()
        HKp2 = HKp2[:-1]  #Limpando o '\n' das linhas em "Hotkey.txt"
        HKm2 = HKm2[:-1]

## Atribuindo as strings para as StringVars
HKp = StringVar()
HKp.set(HKp2)
HKm = StringVar()
HKm.set(HKm2)
HKz = StringVar()
HKz.set(HKz2)

## Frame HKs
FrameHKs = FrameHK(janela)
FrameHKs.grid(column=0, row=0, padx=5, pady=2)

TituloHKs = Label(FrameHKs, text="HOTKEYS GRAVADAS",
                  pady=5, font="Arial 15", bg="#52b6d1",
                  bd=1, relief="solid", padx=5, state='disabled').grid(row=0, column=1, columnspan=2) 

HKp_label = Label(FrameHKs, text="Cont+1 : ", bg="#52b6d1",
                  bd=1, relief="solid", padx=2, anchor='w', 
                  font="Arial 12")
HKp_label.grid(row=1, sticky="EW")          

HKp_entry = Entry(FrameHKs, textvariable=HKp, font="Arial 12", state='disabled')
HKp_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

HKm_label = Label(FrameHKs, text="Cont-1  : ", bg="#52b6d1",
                  bd=1, relief="solid", padx=2, anchor='w', 
                  font="Arial 12")
HKm_label.grid(row=2, sticky="EW")

HKm_entry = Entry(FrameHKs, textvariable=HKm, font="Arial 12", state='disabled')
HKm_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

HKz_label = Label(FrameHKs, text="Cont=0 : ", bg="#52b6d1",
                  bd=1, relief="solid", padx=2, anchor='w', 
                  font="Arial 12")
HKz_label.grid(row=3, sticky="EW")

HKz_entry = Entry(FrameHKs, textvariable=HKz, font="Arial 12", state='disabled')
HKz_entry.grid(column=1, row=3, columnspan=2, sticky="EW")

ConcluirButton = Button(FrameHKs, text="Concluir", command=ConcluirHKs, pady=2, bg="#52b6d1", state='disabled').grid(row=4, column=2, sticky=E, pady=3)

    # Acrescentar opção para alterar as HK desabilitando td a frame e a contagem.
    # # Colocar o .grid na mesma linha de declaraçao da variavel inpede o uso do metodo .configure
AltButton = Button(janela, text="Alterar", command=AltHKs, pady=2, bg="#52b6d1", state= NORMAL)
AltButton.grid(row=1, column=0, sticky=E, pady=1, padx=10)


## Frame Contador
FrameCont = FrameHK(janela)

    # Criar logging(import), usar format e filename, buscar o log como string e printar na area de log
    # Colocar o valor da contagem em baixo em destaque
    # Botao para ligar/desligar contagem e travar a alteração de HKs

FrameCont.grid(column=1, row=0, padx=10, pady=2)

## Geometry
TelaX = janela.winfo_screenwidth()
TelaY = janela.winfo_screenheight()
JanelaX = TelaX/3
JanelaY = TelaY/3
JanelaPosx = TelaX/2 - JanelaX/2
JanelaPosy = TelaY/2 -(JanelaY/2 + 80)
janela.geometry("%dx%d+%d+%d" % (JanelaX, JanelaY, JanelaPosx, JanelaPosy))

janela.mainloop()
