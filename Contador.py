# Contador
# -*- coding: UTF-8 -*-
from pynput import keyboard

def ContUp():
    
    file = open("Contador.txt","r")
    contx = file.readline() 
    file.close()
    file = open("Contador.txt","w")
    contx = int(contx)
    contx = 1 + contx
    contx = str(contx)    
    file.write(contx)
    file.close()
    print('Hotkey +!' + " " + contx)

def ContDown():
    
    file = open("Contador.txt","r")
    contx = file.readline() 
    file.close()
    file = open("Contador.txt","w")
    contx = int(contx)
    contx = contx -1
    contx = str(contx)    
    file.write(contx)
    file.close()
    print('Hotkey -!' + " " + contx)

def ContZero():
    file = open("Contador.txt","w")
    file.write('0')
    file.close()

Vhk = []
try:
    file = open("Contador.txt","x")
    file.write('0')
    file.close()

except:
    ContZero()
    
finally:
    HK = open("Hotkey.txt","r")
    HKl = HK.read()
    x = HKl.find("\n")
    HK.close()
    
    #with open('Hotkey.txt','r') as HK:
     #   Vhk.append(HK.readline())
      #  print(Vhk)

   # HKp = Vhk[0]
   # HKm = Vhk[1]
   # HKz = Vhk[2]

    HK = open("Hotkey.txt","r")
    HKp = HK.readline(x)
    limpador = HK.read(1) # Variavel para limpar o '\n' do "Hotkey.txt"
    HKm = HK.read()
    #limpador = HK.read(1)
    #HKz = HK.readline()
    HK.close()
    print("AS Hotkeys gravadas são:\n" + HKp + " para +\n" + HKm + " para -.\n")

    with keyboard.GlobalHotKeys({
        HKp: ContUp,
        HKm: ContDown}) as h:
        h.join()
