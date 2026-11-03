# ====================
# GAME: Jogo da Velha (com Modificador de estatisticas)
# ====================

# TODO: 
# Leitura das jogadas com validação
# Verificação de vitória e empate
# Placar acumulado

# Variaveis para estatisticas
vitorias_x = 0
vitorias_o = 0
empates = 0

menu = ""

while menu != '4':
    print("\n=== JOGO DA VELHA ===")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Ver placar")
    print("4 - Sair")

    menu = input("Escolha uma opção: ")

    if menu == '1':
        novamente = '1'
        while novamente == '1':
            grid = [
                [".",".","."],
                [".",".","."],
                [".",".","."]
            ]

            jogador = 'X'
            terminou = False

            while not terminou:
                # print Tabuleiro 
                print("\n    1 2 3")
                for linha in range(3):
                    print(linha + 1, "|", end=" ")
                    for coluna in range(3):
                        print(grid[linha][coluna], end=" ")
                    print()

                print("Vez do jogador", jogador)

                    # Aceitar somente as opções válidas antes da conversão.
            
                while True:
                    entrada = input("Linha (1 a 3): ")


                    while entrada != "1" and entrada != "2" and entrada != "3":
                        print("Digite 1, 2 ou 3.")
                        entrada = input("Linha (1 a 3): ")


                    linha = int(entrada) - 1

                    entrada = input("Coluna (1 a 3): ")

                    while entrada != "1" and entrada != "2" and entrada != "3":
                        print("Digite 1, 2 ou 3.")
                        entrada = input("Coluna (1 a 3): ")

                    coluna = int(entrada) - 1

                    if grid[linha][coluna] != ".":
                        print("Posição ocupada, tente novamente.")
                        continue
                    break
                grid[linha][coluna] = jogador    
                if jogador == 'X':
                   jogador = 'O'
                else:
                    jogador = 'X'       

            # decisão para jogar novamente
            novamente = input('Jogo encerrado, gostaria de recomeçar (1 para sim, outro para não)? ')

    elif menu == '2':
        # Todo: Adicionar Regras (remova o pass apos construir lógica)
        pass

    elif menu == '3':
        print("\n=== PLACAR ACUMULADO ===")
        print("Vitórias de X:", vitorias_x)
        print("Vitórias de O:", vitorias_o)
        print("Empates:", empates)

    elif menu != '4':
        # Tratamento de entrada invalida
        print("Opção inválida. Digite 1, 2, 3 ou 4.")

print("Jogo encerrado. Até a próxima!")