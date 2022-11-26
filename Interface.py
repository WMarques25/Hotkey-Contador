# Interface
# -*- coding: Windows_1252 -*-

from tkinter import *
#from tkinter import ttk
#from tkinter.ttk import *
#import Hotkey
#import Contador

def AltHK():
    #HKs_orientacao["text"] = ""
    Texto_HKin = Label(janela, text="aaAAA")
    Texto_HKin.grid(column=0, row=3, padx=0, pady=10)
    Xx = StringVar(janela, "<ctrl>+<shift>+x")
    
    Caixa_HK = Entry(janela, width=53, textvariable=Xx, state="disable")
    Caixa_HK["state"]= 'normal'
    Caixa_HK.grid(column=1, row=3, padx=10, pady=10)

    Bt = Button(janela, text="Próximo",
                command=lambda: AltHK1(Caixa_HK)).grid(row= 4, column=4)

    # Gravando Hotkey +
    HKs_orientacao["text"] =("Digite a Hotkey que deseja gravar para aumentar a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
    

def AltHK1(Caixa_HK):
    
    Hotkey = Caixa_HK.get()
    HKs_orientacao["text"]=("Hotkey gravada = ",Hotkey)
    label1 = Label(janela, text=Hotkey).grid(row=5, column=1)
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

# geometry

TelaX = janela.winfo_screenwidth()
TelaY = janela.winfo_screenheight()
JanelaX = TelaX/3
JanelaY = TelaY/3
JanelaPosx = TelaX/2 - JanelaX/2
JanelaPosy = TelaY/2 -(JanelaY/2 + 80)
janela.geometry("%dx%d+%d+%d" % (JanelaX, JanelaY, JanelaPosx, JanelaPosy))

#janela.resizable(width='false', height='false')
HKbut = Button(janela, text='Alterar Hotkeys', command=lambda: AltHK())
HKbut.pack()
HKbut.grid(column=1, row=4, padx=10, pady=10)

Xa = StringVar(janela, "Teste")
HKp = StringVar()
HKm = StringVar()
HKz = StringVar()

#Caixa_HK = Entry(janela, width= 40, textvariable=Xa)
#Caixa_HK.pack()
#Caixa_HK.grid(column=1, row=3, padx=10, pady=10)


with open('Hotkey.txt','r') as f:
        HKp.set(f.readline())
        HKm.set(f.readline())
        HKz.set(f.readline())
        #HKp = HKp[:-1]  #Limpando o '\n' das linhas em "Hotkey.txt"
        #HKm = HKm[:-1]

#HKs = StringVar(janela, "As Hotkeys gravadas são:\n" + "Cont+ :" + HKp + "\nCont-  :" + HKm + "\nCont0 :" + HKz )
#asd
HKs_orientacao = Label(janela,
                       borderwidth=5,
                       padx=30,
                       pady=30,
                       relief="solid",
                       background="light blue",
                       font="Arial 14",
                       state="disable",
                       textvariable=HKm)
HKs_orientacao.grid(column=1, row=2, padx=20, pady=2)
janela.mainloop()


# criar botao para alterar as HKs, liberando o state de disable para normal, cada linha para uma HK.
# separar HKs e contagem em frames = Frame(janela) relief SUNKEN
# HKs como StingVar, textvariable em Entrys 