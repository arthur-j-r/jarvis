from jarvis import Jarvis
import playsound
usuario = input("Digite seu nome: ")

if __name__ == "__main__":
    while True:
        jarvis = Jarvis(usuario)
        jarvis.voz("Deseja ativar a integração com a IA? (1 para sim, 0 para não): ")
        modo_ia = input("Deseja ativar a integração com a IA? (1 para sim, 0 para não): ")
        if modo_ia == '1':
            jarvis.voz("Integração com a IA ativada.")
            jarvis.saudar_usuario()
            jarvis.voz("O que deseja saber, senhor?")
            fala = jarvis.usuario_falar()
            jarvis.jarvis_responder(fala)
        elif modo_ia == '0':
            jarvis.voz("Integração com a IA desativada.")
            jarvis.saudar_usuario()
            jarvis.voz("O que deseja, senhor?")
            fala = jarvis.usuario_falar().lower()
    
            if any(comando in fala for comando in ["programa","abrir programa", "abrir app","app","aplicativo"]):
                jarvis.voz("Qual programa deseja abrir?")
                programa = jarvis.usuario_falar().lower()
                jarvis.abrir_programa(programa)
        else:
            jarvis.voz("Opção inválida. A integração com a IA não será ativada.")
            break