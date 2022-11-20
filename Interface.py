# Interface
# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import Hotkey
import Contador

janela = Tk()
janela.title("")
#janela.resizable(width='false', height='false')
HKbut = Button(janela, text='HK', command=Hotkey)
HKbut.pack()
#asd
janela.mainloop()