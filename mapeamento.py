import pyautogui
import time
import os

import sounddevice as sd



def get_mouse_position():
    time.sleep(5)
    print(pyautogui.position())
def teclas_teclado():
    print(pyautogui.KEYBOARD_KEYS)
def op3():
    # Set environment variable before importing sounddevice. Value is not important.
    os.environ["SD_ENABLE_ASIO"] = "1"
    print(sd.query_hostapis())

opcao = input()
if opcao == '1':
    time.sleep(15)
    get_mouse_position()
elif opcao == '2':
    teclas_teclado()
    pyautogui.press('win')
elif opcao == '3':
    op3()
else:
    print('Opção inválida')
