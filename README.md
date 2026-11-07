# Game.py

Jogo da Velha em Python, desenvolvido como projeto acadêmico para praticar lógica de programação, manipulação de listas e interação com o usuário no console.

## Descrição

Este projeto implementa um jogo de Jogo da Velha (Tic-Tac-Toe) em Python puro, sem uso de bibliotecas externas. O jogo inclui:

- menu principal com opções de jogar, regras e placar;
- validação de entradas do usuário;
- alternância entre os jogadores X e O;
- verificação de vitória e empate;
- contador acumulado de vitórias e empates;
- opção de reiniciar a partida ou voltar ao menu.

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python game.py
```

Ou, em algumas máquinas:

```bash
python3 game.py
```

## Como jogar

1. Escolha a opção `1` no menu para iniciar uma partida.
2. Informe a linha e a coluna onde deseja marcar.
3. As coordenadas válidas vão de `1` a `3`.
4. O primeiro jogador usa `X` e o segundo usa `O`.
5. O jogador que alinhar três casas em linha, coluna ou diagonal vence.

## Regras

- Cada jogada deve ocorrer em uma casa vazia.
- A linha e a coluna devem estar entre 1 e 3.
- Se todas as casas forem preenchidas sem um vencedor, o resultado é empate.

## Estrutura do projeto

- `game.py`: código principal do jogo.
- `README.md`: documentação do projeto.

## Status

Projeto finalizado como uma versão funcional de console, com foco em lógica e experiência de aprendizado.
