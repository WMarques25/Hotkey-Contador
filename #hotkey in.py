# Hotkey in
# -*- coding: UTF-8 -*-
from pynput import keyboard

print("Digite a Hotkey que deseja gravar.\nUse o modelo : ' <ctrl>+<shift>+x '")


Hotkey = input()

print(Hotkey)
HotkeyFile = open("Hotkey.txt", "w")

HotkeyFile.write(Hotkey)

HotkeyFile.close()

