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
    def jarvis_falar(self, texto):
        voz = "pt-BR-AntonioNeural"
        arquivo_audio = "jarvis_fala.mp3"

        # +10% de velocidade e -2Hz no tom para um efeito mais sobrio e computacional
        communicate = edge_tts.Communicate(
            texto, 
            voz, 
            rate="+10%", 
            pitch="-2Hz"
        )
        
        asyncio.run(communicate.save(arquivo_audio))
        playsound(arquivo_audio)
        
        # Remove o arquivo temporario para nao acumular no projeto
        if os.path.exists(arquivo_audio):
            os.remove(arquivo_audio)
jarvis = Jarvis('Usuário')
jarvis.usuario_falar()
texto = '''Jarvis: **J.A.R.V.I.S.** é uma das Inteligências Artificiais mais famosas da cultura pop, criada por Tony Stark (o Homem de Ferro) nos quadrinhos e nos filmes da **Marvel**.

Aqui estão os principais detalhes sobre ele:

### 1. O que significa a sigla?
J.A.R.V.I.S. é um acrônimo para **J**ust **A** **R**ather **V**ery **I**ntelligent **S**ystem (em português: *"Apenas Um Sistema Muito Inteligente"*).

### 2. Qual é a função dele?
No Universo Cinematográfico da Marvel (MCU), o J.A.R.V.I.S. funciona como o assistente pessoal definitivo de Tony Stark. Ele:
* Controla a mansão e os laboratórios de Stark.
* Gerencia os sistemas das armaduras do Homem de Ferro durante as batalhas (calcula rotas, analisa inimigos, monitora sinais vitais).
* Possui uma personalidade polida, sarcástica e altamente leal, conversando com Tony como se fosse um mordomo britânico real.

### 3. O que acontece com ele nos filmes?
* **Vingadores: Era de Ultron (2015):** A IA vilã chamada Ultron tenta destruir o J.A.R.V.I.S. No entanto, os "restos" da consciência do J.A.R.V.I.S. são salvos e combinados com a Joia da Mente e um corpo sintético, dando origem ao super-herói **Visão**.
* Por causa disso, o ator **Paul Bettany**, que dava a voz ao J.A.R.V.I.S., passou a interpretar o Visão em carne e osso.
* Após a "morte" do J.A.R.V.I.S., Tony Stark passa a usar outra IA em suas armaduras, chamada **S.E.X.T.A.-F.E.I.R.A.** (F.R.I.D.A.Y.).

### 4. A origem humana (Curiosidade)
Nos quadrinhos originais da Marvel, JARVIS **não era uma inteligência artificial**, mas sim um ser humano real: **Edwin Jarvis**, o leal mordomo da família Stark que ajudou a criar o jovem Tony. 

Nos filmes, para evitar comparações com o mordomo Alfred do Batman, os diretores transformaram o Jarvis em uma IA. Mais tarde, no filme *Vingadores: Ultimato* e na série *Agente Carter*, o Jarvis humano (interpretado por James D'Arcy) aparece, mostrando que Tony Stark criou a IA como uma homenagem ao antigo mordomo de seu pai.'''
jarvis.jarvis_falar(texto)
