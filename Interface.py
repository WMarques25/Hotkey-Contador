# Interface
# -*- coding: Windows_1252 -*-

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import Hotkey
#import Contador

def AltHK():
    #HKs_orientacao["text"] = ""
    Texto_HKin = Label(janela, text="aaAAA")
    Texto_HKin.grid(column=0, row=3, padx=0, pady=10)
    Caixa_HK = Entry(janela, width=53, )
    Caixa_HK.grid(column=1, row=3, padx=10, pady=10)

    Bt = Button(janela, text="Próximo", command=AltHK1)

    # Gravando Hotkey +
    HKs_orientacao["text"] =("Digite a Hotkey que deseja gravar para aumentar a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
    

def AltHK1():
    
    Hotkey = Caixa_HK.get()
    HKs_orientacao["text"]=("Hotkey gravada = ",Hotkey)
    HotkeyFile = open("Hotkey.txt", "w")
    HotkeyFile.write(Hotkey)
    
    # Gravando Hotkey -
    HKs=("\Digite a Hotkey que deseja gravar para reduzir a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
    Hotkey2 = Caixa_HK.get()
    HKs=("Hotkey gravada = ",Hotkey2)
    HotkeyFile.write("\n" + Hotkey2)

    # Gravando Hotkey 0
    HKs=("\Digite a Hotkey que deseja gravar para zerar a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
    Hotkey0 = Caixa_HK.get()
    HKs=("Hotkey gravada = ",Hotkey0)
    HotkeyFile.write("\n" + Hotkey0)
    HotkeyFile.close()

    # Loop para correção
    
    HKs=("AS Hotkeys gravadas são:\n" + Hotkey + " para +\n" + Hotkey2 + " para -\n" + Hotkey0 + " para zerar.")



janela = Tk()
janela.title("")
#janela.resizable(width='false', height='false')
HKbut = Button(janela, text='Alterar Hotkeys', command=AltHK)
HKbut.grid(column=1, row=4, padx=10, pady=10)
Caixa_HK = Entry(janela, width=53 )
Caixa_HK.grid(column=1, row=3, padx=10, pady=10)

with open('Hotkey.txt','r') as f:
        HKp = f.readline()
        HKm = f.readline()
        HKz = f.readline()
        HKp = HKp[:-1]  #Limpando o '\n' das linhas em "Hotkey.txt"
        HKm = HKm[:-1]

HKs = ("As Hotkeys gravadas são:\n" + HKp + " para +\n" + HKm + " para -\n" + HKz + " para zerar.")
#asd
HKs_orientacao = Label(janela, text=HKs, relief="solid")
HKs_orientacao.grid(column=1, row=2, padx=20, pady=2)
janela.mainloop()