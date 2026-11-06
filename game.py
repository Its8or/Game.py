# ====================
# GAME: Jogo da Velha (com Modificador de estatisticas)
# ====================

# TODO: 
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
                
                # Contar as marcas do jogador em cada linha e coluna.
                    venceu = False
                    for i in range(3):
                        iguais_linha = 0
                        iguais_coluna = 0
                        for j in range(3):
                            if grid[i][j] == jogador:
                                iguais_linha += 1
                            if grid[j][i] == jogador:
                                iguais_coluna += 1
                        if iguais_linha == 3 or iguais_coluna == 3:
                            venceu = True

                    # Percorrer as duas diagonais.
                    diagonal_principal = 0
                    diagonal_secundaria = 0
                    for i in range(3):
                        if grid[i][i] == jogador:
                            diagonal_principal += 1
                        if grid[i][2 - i] == jogador:
                            diagonal_secundaria += 1
                    if diagonal_principal == 3 or diagonal_secundaria == 3:
                        venceu = True

                    # Procurar casas vazias para identificar o empate.
                    vazias = 0
                    for i in range(3):
                        for j in range(3):
                            if grid[i][j] == ".":
                                vazias += 1

            # decisão para jogar novamente
            novamente = input('Jogo encerrado, gostaria de recomeçar (1 para sim, outro para não)? ')

    elif menu == '2':
        print("""\n==================================\n             REGRAS\n==================================\n1. Escolha a linha (1 a 3)\n2. Escolha a coluna (1 a 3)\n3. O outro jogador repete os passos 1 e 2.\n4. O jogador que colocar 3 casas juntas ganha.""")

    elif menu == '3':
        print("\n=== PLACAR ACUMULADO ===")
        print("Vitórias de X:", vitorias_x)
        print("Vitórias de O:", vitorias_o)
        print("Empates:", empates)

    elif menu != '4':
        # Tratamento de entrada invalida
        print("Opção inválida. Digite 1, 2, 3 ou 4.")

print("Jogo encerrado. Até a próxima!")
