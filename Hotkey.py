# Hotkey
# -*- coding: UTF-8 -*-
from os import system
from pynput import keyboard
from Interface import jane


    
def altera():
        # Gravando Hotkey +
    HKs=("Digite a Hotkey que deseja gravar para aumentar a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
    Hotkey = input()
    HKs=("Hotkey gravada = ",Hotkey)
    HotkeyFile = open("Hotkey.txt", "w")
    HotkeyFile.write(Hotkey)

    # Gravando Hotkey -
    HKs=("\Digite a Hotkey que deseja gravar para reduzir a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
    Hotkey2 = input()
    HKs=("Hotkey gravada = ",Hotkey2)
    HotkeyFile.write("\n" + Hotkey2)

    # Gravando Hotkey 0
    HKs=("\Digite a Hotkey que deseja gravar para zerar a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
    Hotkey0 = input()
    HKs=("Hotkey gravada = ",Hotkey0)
    HotkeyFile.write("\n" + Hotkey0)
    HotkeyFile.close()

    # Loop para correção
    system('cls')
    HKs=("AS Hotkeys gravadas são:\n" + Hotkey + " para +\n" + Hotkey2 + " para -\n" + Hotkey0 + " para zerar.")

"""
try:
    open("Hotkey.txt", "x")

except:
    with open('Hotkey.txt','r') as f:
        HKp = f.readline()
        HKm = f.readline()
        HKz = f.readline()
    HKp = HKp[:-1]  #Limpando o '\n' das linhas em "Hotkey.txt"
    HKm = HKm[:-1]

    print("As Hotkeys gravadas são:\n" + HKp + " para +\n" + HKm + " para -\n" + HKz + " para zerar. \n")
    x = input("Deseja alterar as Hotkeys salvas? ('S' p/ SIM)\n\t")
    
else:
    x = 'S'

finally:
    while x.upper() == 'S':
        system('cls')
        
        # Gravando Hotkey +
        print("Digite a Hotkey que deseja gravar para aumentar a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
        Hotkey = input()
        print("Hotkey gravada = ",Hotkey)
        HotkeyFile = open("Hotkey.txt", "w")
        HotkeyFile.write(Hotkey)

        # Gravando Hotkey -
        print("\nDigite a Hotkey que deseja gravar para reduzir a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
        Hotkey2 = input()
        print("Hotkey gravada = ",Hotkey2)
        HotkeyFile.write("\n" + Hotkey2)

        # Gravando Hotkey 0
        print("\nDigite a Hotkey que deseja gravar para zerar a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
        Hotkey0 = input()
        print("Hotkey gravada = ",Hotkey0)
        HotkeyFile.write("\n" + Hotkey0)
        HotkeyFile.close()

        # Loop para correção
        system('cls')
        print("AS Hotkeys gravadas são:\n" + Hotkey + " para +\n" + Hotkey2 + " para -\n" + Hotkey0 + " para zerar.\n")
        x = input("Deseja alterar as Hotkeys salvas? ('S' p/ SIM)\n\t")
"""