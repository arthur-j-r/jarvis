from autenticacaov15 import chat_gpt_autentication
import pyautogui
import pyttsx3
import sounddevice
import speech_recognition as sr
import requests
import time
import asyncio
import edge_tts
from playsound import playsound
import os
import sys
import subprocess
from PIL import Image
from openai import OpenAI
from iaconfig import enviar_mensagem


pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

class Jarvis:
    def __init__(self,username):
        self.me = 'Jarvis'
        self.username = username
        #self.integracao_gemini = enviar_mensagem
    def saudar_usuario(self):
        saudacao = f'Olá Senhor {self.username}, eu sou {self.me}, seu assistente virtual. Como posso ajudá-lo hoje?'
        print(saudacao)
        self.jarvis_responder(texto=saudacao)
    def abrir_programa(self,programa):
        try:
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.write(programa)
            pyautogui.press('enter')
            programa_aberto = f'Programa {programa} aberto com sucesso!'
            self.jarvis_responder(texto=programa_aberto)
            print(programa_aberto)
        except Exception as e:
            print(f'Erro ao abrir o programa {programa}: {e}')
    def fechar_programa(self,programa=None):
        try:
            pyautogui.hotkey('alt','f4')
            if programa is not None:
                programa_fechado = f'Programa {programa} fechado com sucesso!'
                self.jarvis_responder(texto=programa_fechado)
                print(programa_fechado)
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
            time.sleep(1)
            pesquisa_realizada = f'Pesquisa "{pesquisa}" realizada com sucesso!'
            self.jarvis_responder(texto=pesquisa_realizada)
            print(pesquisa_realizada)
        except Exception as e:
            print(f'Erro ao realizar a pesquisa {pesquisa}: {e}')
    def abrir_arquivo(self,caminho_arquivo):
        try:
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.write(caminho_arquivo)
            pyautogui.press('enter')
            arquivo_aberto = f'Arquivo {caminho_arquivo} aberto com sucesso!'
            self.jarvis_responder(texto=arquivo_aberto)
            print(arquivo_aberto)
        except Exception as e:
            print(f'Erro ao abrir o arquivo {caminho_arquivo}: {e}')
    def tirar_print(self,nome_arquivo):
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(nome_arquivo)
            captura = f'Print da tela salvo como {nome_arquivo}'
            self.jarvis_responder(texto=captura)
            print(captura)
        except Exception as e:
            print(f'Erro ao tirar print da tela: {e}')
    def desligar_computador(self):
        try:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.moveTo(x = 1127, y = 959, duration = 1)
            pyautogui.click()
            pyautogui.moveTo(x = 1089, y = 869, duration = 0.5)
            desligar = f'Desligando o computador...'
            self.jarvis_responder(texto=desligar)
            time.sleep(1)
            pyautogui.doubleClick()
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
    def jarvis_responder(self, texto):
        resposta = enviar_mensagem(texto)
        voz = "pt-BR-AntonioNeural"
        arquivo_audio = "jarvis_fala.mp3"
        communicate = edge_tts.Communicate(
            resposta, 
            voz, 
            rate="+10%", 
            pitch="-2Hz"
        )
        asyncio.run(communicate.save(arquivo_audio))
        playsound(arquivo_audio)
        if os.path.exists(arquivo_audio):
            os.remove(arquivo_audio)


## EX DE USO           
jarvis = Jarvis('Arthur')
jarvis.saudar_usuario()
jarvis.jarvis_responder(texto="Quem é Bruce Wayne?")



