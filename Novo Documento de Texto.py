from pynput import keyboard

def on_activate():
    #TODO Alterar para abrir e escrever +1 no txt 
    #TODO abrir txt, pegar numero, numero+1, criar novo txt com msm nome, escrever numero+1.
    print('Global hotkey activated!')

def for_canonical(f):
    return lambda k: f(l.canonical(k))
#TODO definir a variavel string puxando de outro txt c programa.
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<shift>++'), #TODO mudar conteudo para variavel string mudando por outro txt.
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()
