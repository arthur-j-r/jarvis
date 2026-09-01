import speech_recognition as sr
import sounddevice as sd
import numpy as np

# Configurações do áudio
sample_rate = 16000
duration = 5  # Segundos que ele vai gravar

print("Gravando... Fale agora!")
# Grava diretamente pelo sounddevice
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
sd.wait()  # Aguarda terminar a gravação

# Converte para o formato que o SpeechRecognition entende
audio_bytes = audio_data.tobytes()
audio_file = sr.AudioData(audio_bytes, sample_rate, 2)

# Reconhecimento via Google
rec = sr.Recognizer()
try:
    texto = rec.recognize_google(audio_file, language="pt-BR")
    print(f"Você disse: {texto}")
except sr.UnknownValueError:
    print("Não entendi o áudio.")