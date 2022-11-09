# Hotkey
# -*- coding: UTF-8 -*-
from pynput import keyboard

# Gravando Hotkey +
print("Digite a Hotkey que deseja gravar para aumentar a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
Hotkey = input()
print("Hotkey gravada = ",Hotkey)
HotkeyFile = open("Hotkey.txt", "w")
HotkeyFile.write(Hotkey)

# Gravando Hotkey -
print("Digite a Hotkey que deseja gravar para reduzir a contagem.\nUse o modelo : ' <ctrl>+<shift>+x '")
Hotkey2 = input()
print("Hotkey gravada = ",Hotkey2)
HotkeyFile.write("\n" + Hotkey2)
HotkeyFile.close()

