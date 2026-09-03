from jarvis import Jarvis

usuario = input("Digite seu nome: ").capitalize()

if __name__ == "__main__":
    jarvis = Jarvis(usuario)
    
    while True:
        jarvis.voz("Deseja ativar a integração com a IA? (1 para sim, 0 para não): ")
        modo_ia = input("Deseja ativar a integração com a IA? (1 para sim, 0 para não): ")
        
        if modo_ia == '1':
            jarvis.voz("Integração com a IA ativada.")
            jarvis.saudar_usuario()
            jarvis.voz("O que deseja saber, senhor?")
            fala = jarvis.usuario_falar()
            if fala:
                jarvis.jarvis_responder(fala)
                
        elif modo_ia == '0':
            jarvis.voz("Integração com a IA desativada.")
            jarvis.saudar_usuario()
            jarvis.voz("Se desejar sair do modo sem integração com IA, diga 'sair'.")
            
            while True:
                fala = jarvis.usuario_falar()
                if not fala:
                    jarvis.voz("Não foi possível reconhecer sua fala. Por favor, tente novamente.")
                    continue

                fala = fala.lower()

                if any(comando in fala for comando in ["abrir", "iniciar", "rodar"]):
                    jarvis.voz("Qual programa deseja abrir?")
                    programa = jarvis.usuario_falar()
                    if programa:
                        jarvis.abrir_programa(programa)

                elif "fechar" in fala:
                    jarvis.voz("Qual programa deseja fechar?")
                    programa = jarvis.usuario_falar()
                    if programa:
                        jarvis.fechar_programa(programa)

                elif "sair" in fala:
                    jarvis.voz("Saindo do modo sem integração com IA.")
                    break

                elif any(comando in fala for comando in ["pesquisar", "buscar"]):
                    jarvis.voz("O que deseja pesquisar?")
                    pesquisa = jarvis.usuario_falar()
                    if pesquisa:
                        jarvis.pesquisar(pesquisa)

                elif any(comando in fala for comando in ["abrir arquivo", "abrir documento"]):
                    jarvis.voz("Qual arquivo deseja abrir? Forneça o caminho completo.")
                    caminho = jarvis.usuario_falar()
                    if caminho:
                        jarvis.abrir_arquivo(caminho)

                elif any(comando in fala for comando in ["print", "captura de tela"]):
                    jarvis.voz("Qual nome deseja dar ao arquivo?")
                    nome = jarvis.usuario_falar()
                    if nome:
                        jarvis.tirar_print(f"{nome}.png")

                elif any(comando in fala for comando in ["desligar computador", "desligar pc"]):
                    jarvis.desligar_computador()

                elif any(comando in fala for comando in ["dormir", "modo de espera"]):
                    jarvis.voz("Entrando em modo de espera.")
                    jarvis.dormir()

                else:
                    jarvis.voz("Comando não reconhecido. Por favor, tente novamente.")
        else:
            jarvis.voz("Opção inválida.")
            break