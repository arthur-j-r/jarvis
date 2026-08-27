import pyautogui
import sounddevice
import speech_recognition as sr
import time
import os
import sys
import subprocess
from PIL import Image

sounddevice.default.device = 'Microfone (Realtek(R) Audio)'

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

class Jarvis:
    def __init__(self,username):
        self.me = 'Jarvis'
        self.username = username
    def saudar_usuario(self):
        print(f'Olá {self.username}, eu sou {self.me}, seu assistente virtual.')
        print('Como posso ajudá-lo hoje?')
    def abrir_programa(self,programa):
        try:
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.write(programa)
            pyautogui.press('enter')
            print(f'Programa {programa} aberto com sucesso!')
        except Exception as e:
            print(f'Erro ao abrir o programa {programa}: {e}')
    def fechar_programa(self,programa=None):
        try:
            pyautogui.hotkey('alt','f4')
            if programa is not None:
                print(f'Programa {programa} fechado com sucesso!')
        except Exception as e:
            print(f'Erro ao fechar o programa {programa}: {e}')
    def pesquisar(self,pesquisa):
        try:
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.write('google chrome')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.moveTo(x = 621, y =510, duration = 1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.hotkey('ctrl','t')
            pyautogui.write(pesquisa)
            pyautogui.press('enter')
        except Exception as e:
            print(f'Erro ao realizar a pesquisa {pesquisa}: {e}')
    def abrir_arquivo(self,caminho_arquivo):
        try:
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.write(caminho_arquivo)
            pyautogui.press('enter')
            print(f'Arquivo {caminho_arquivo} aberto com sucesso!')
        except Exception as e:
            print(f'Erro ao abrir o arquivo {caminho_arquivo}: {e}')
    def tirar_print(self,nome_arquivo):
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(nome_arquivo)
            print(f'Print da tela salvo como {nome_arquivo}')
        except Exception as e:
            print(f'Erro ao tirar print da tela: {e}')
    def desligar_computador(self):
        try:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.moveTo(x = 1127, y = 959, duration = 1)
            pyautogui.click()
            pyautogui.moveTo(x = 1089, y = 869, duration = 0.5)
            time.sleep(0.5)
            pyautogui.doubleClick()
            print('Computador desligado com sucesso!')
        except Exception as e:
            print(f'Erro ao desligar o computador: {e}')

jarvis = Jarvis('Arthur')


