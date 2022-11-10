# Contador
# -*- coding: UTF-8 -*-
from pynput import keyboard

def ContUp():
    with open("Contador.txt",'r') as file:
        cont = file.readline()
        cont = int(cont)
        cont +=1
        cont = str(cont)
        with open("Contador.txt",'w') as file:
            file.write(cont)
        
    print('Hotkey +! ', cont)

def ContDown():
    with open("Contador.txt",'r') as file:
        cont = file.readline()
        cont = int(cont)
        cont -=1
        cont = str(cont)
        with open("Contador.txt",'w') as file:
            file.write(cont)

    print('Hotkey -! ', cont)

def ContZero():
    file = open("Contador.txt","w")
    file.write('0')
    file.close()
    print("\n-*- Contagem zerada! -*-\n")
            
try:
    file = open("Contador.txt","x")
    file.write('0')
    file.close()
    print("O contador está em: 0\n")

except:
    with open('Contador.txt','r') as f:
        cont = f.readline()
    print("O contador está em: ",cont,"\n  Deseja zerar o contador? ('S' p/ SIM)")
    x = input()
    if x.upper() == 'S':
        ContZero()
    else:
        print("")
    
finally: 
    with open('Hotkey.txt','r') as f:
        HKp = f.readline()
        HKm = f.readline()
        HKz = f.readline()
    HKp = HKp[:-1]  #Limpando o '\n' das linhas em "Hotkey.txt"
    HKm = HKm[:-1]

    print("AS Hotkeys gravadas são:\n" + HKp + " para +\n" + HKm + " para -\n" + HKz + " para zerar.\n\n")

    with keyboard.GlobalHotKeys({
        HKp: ContUp,
        HKm: ContDown,
        HKz: ContZero}) as h:
        h.join()
