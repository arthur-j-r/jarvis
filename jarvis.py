from autentication import chat_gpt_autentication
import pyautogui
import pyaudiowpatch
import sounddevice
import speech_recognition as sr
import requests
import time
import os
import sys
import subprocess
from PIL import Image
from openai import OpenAI


def chamar_chat_gpt(conteudo):
    client = OpenAI(api_key=chat_gpt_autentication)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente virtual chamado Jarvis."},
            {"role": "user", "content": conteudo}
        ]
    )
    return response.choices[0].message.content


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

    def usuario_falar(self):
        # Configurações do áudio
        sample_rate = 16000
        duration = 5  # Segundos que ele vai gravar

        print("Gravando... Fale agora!")
        # Grava diretamente pelo sounddevice
        audio_data = sounddevice.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sounddevice.wait()  # Aguarda terminar a gravação

        # Converte para o formato que o SpeechRecognition entende
        audio_bytes = audio_data.tobytes()
        audio_file = sr.AudioData(audio_bytes, sample_rate, 2)

        # Reconhecimento via Google
        rec = sr.Recognizer()
        try:
            texto = rec.recognize_google(audio_file, language="pt-BR")
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Não entendi o áudio.")
            return None
jarvis = Jarvis('Usuário')
jarvis.usuario_falar()

