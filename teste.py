import asyncio
import edge_tts
from playsound import playsound
import os

async def jarvis_falar(texto):
    voz = "pt-BR-AntonioNeural"
    arquivo_audio = "jarvis_fala.mp3"

    # +10% de velocidade e -2Hz no tom para um efeito mais sobrio e computacional
    communicate = edge_tts.Communicate(
        texto, 
        voz, 
        rate="+10%", 
        pitch="-2Hz"
    )
    
    await communicate.save(arquivo_audio)
    playsound(arquivo_audio)
    
    # Remove o arquivo temporario para nao acumular no projeto
    if os.path.exists(arquivo_audio):
        os.remove(arquivo_audio)

if __name__ == "__main__":
    asyncio.run(jarvis_falar("Sistemas online, senhor. Em que posso ajudar hoje?"))