import random  # Biblioteca para gerar escolhas aleatórias
import time    # Biblioteca para pausar o programa (usada para animação)
import os      # Biblioteca para interagir com o sistema operacional (limpar console)

# Lista de frutas usadas nas roletas do caça-níquel
frutas = ['🍄', '🍌', '🍆', '🌶️', '🌽', '🍓', '🍑', '🍍']

# Função que limpa o console, compatível com Windows e Unix/Linux/Mac
def limparConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que gera o resultado final com 50% de chance de vitória
def gerarResultado50_50():
    ganhar = random.choice([True, False])  # Escolhe aleatoriamente entre ganhar ou não

    if ganhar:
        # Retorna três frutas iguais (vitória)
        fruta = random.choice(frutas)
        return [fruta, fruta, fruta]
    else:
        # Garante que o resultado não tenha três frutas iguais (derrota)
        while True:
            resultado = [random.choice(frutas) for _ in range(3)]
            if not (resultado[0] == resultado[1] == resultado[2]):
                return resultado

# Função que simula o giro das roletas e imprime o resultado final
def girar_moedas():
    print('🎰 Girando...')

    # Animação do giro das frutas (apenas visual)
    for _ in range(20):
        resultados = [random.choice(frutas) for _ in range(3)]
        print(f"| {resultados[0]} | {resultados[1]} | {resultados[2]} | ", end='\r')
        time.sleep(0.1)  # Pausa de 0.1 segundo entre as animações
    print()

    # Gera o resultado final com chance de vitória
    resultado_final = gerarResultado50_50()

    # Mostra o resultado final na tela
    print(f"| {resultado_final[0]} | {resultado_final[1]} | {resultado_final[2]} |")

    # Verifica se o jogador ganhou (3 frutas iguais)
    if resultado_final[0] == resultado_final[1] == resultado_final[2]:
        print("🎉 GANHOU, 3 FRUTAS IGUAIS!")
    else:
        print("🎲 Tente novamente, não ganhou desta vez.")

# Função principal do cassino: controla a interação com o jogador
def iniciar_cassino():
    limparConsole()
    print("🎰 Seja Bem-vindo ao Cassino 🎰")

    while True:
        # Solicita que o jogador escolha entre jogar ou sair
        entrada = input("\nDigite 1 para jogar ou 2 para sair: ").strip()
        
        if entrada == "1":
            limparConsole()
            girar_moedas()  # Inicia uma rodada
        elif entrada == "2":
            print("👋 Obrigado por jogar, volte sempre!")
            break  # Encerra o jogo
        else:
            print("Comando inválido, digite 1 para jogar e 2 para sair.")

# Ponto de entrada principal do programa
if __name__ == "__main__":
    iniciar_cassino()
