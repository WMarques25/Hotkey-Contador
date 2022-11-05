#Contador
# -*- coding: UTF-8 -*-
from pynput import keyboard

def on_activate():
    
    file = open("Contador.txt","r")
    contx = file.readline()
    #print(contx)
    file.close()
    file = open("Contador.txt","w")
    contx = int(contx)
    contx = 1 + contx
    contx = str(contx)
    #print(contx)
    file.write(contx)
    file.close()
    print('Global hotkey activated!' + " " + contx)

def for_canonical(f):
    return lambda k: f(l.canonical(k))

#with open("Hotkey.txt", "r") as text_file:
#    data = text_file.readlines()
#HKs = data[1] - para pegar a segunda linha.

try:
    file = open("Contador.txt","x")
    file.close()
    file2 = open("Contador.txt","w")
    file2.write('0')
    file2.close()
finally:
    HK = open("Hotkey.txt","r")
    HKs = HK.readline()
    HK.close()
    print("Hotkey gravada é: " + HKs)

    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse(HKs),
        on_activate)
    with keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as l:
        l.join()
