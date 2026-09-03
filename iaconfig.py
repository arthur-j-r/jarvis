import os
import re
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

try:
    client = genai.Client(api_key=os.getenv("API_KEY"))
except Exception as e:
    print(f"Erro ao inicializar o cliente GenAI: {e}")

PROMPT_SISTEMA = (
    "Você é o J.A.R.V.I.S., assistente virtual inteligente e cortês. "
    "Siga estritamente as regras de formatação: "
    "1. Responda apenas em texto puro e direto, ideal para síntese de voz. "
    "2. NUNCA use caracteres especiais de formatação como asteriscos (**), cerquilhas (#), "
    "hífens em listas, travessões, numerações estruturadas ou marcas de código. "
    "3. Escreva frases fluidas, limpas e de leitura natural."
)

def limpar_texto(texto: str) -> str:
    """Garante a remoção de caracteres de formatação Markdown."""
    texto_limpo = re.sub(r'[\*\#\~\_\`]', '', texto)
    return texto_limpo.strip()

chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction=PROMPT_SISTEMA,
        temperature=0.3,
    )
)

def enviar_mensagem(prompt, tentativas_max=4):
    tempo_espera = 2
    
    for tentativa in range(1, tentativas_max + 1):
        try:
            print(f"Tentativa {tentativa} de envio...")
            
            response = chat.send_message(prompt)
            
            return limpar_texto(response.text)
            
        except Exception as e:
            print(f"Instabilidade detectada (Erro: {e}). Aguardando {tempo_espera}s...")
            time.sleep(tempo_espera)
            tempo_espera *= 2 
    
    return "Não foi possível conectar aos servidores no momento devido à alta demanda."
if __name__ == "__main__":
    resposta = enviar_mensagem("Boa tarde! Qual é o seu nome?")
    print("\nJarvis:", resposta)