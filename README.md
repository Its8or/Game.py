# Jogo da Velha

Projeto acadêmico desenvolvido em Python para praticar lógica de programação por meio de um jogo da velha para dois jogadores, executado no terminal.

## Requisitos

- Python 3
- Nenhuma biblioteca externa

## Como executar

No terminal, acesse a pasta do projeto e execute:

```bash
python game.py
```

Se necessário, use:

```bash
python3 game.py
```

## Como jogar

O menu principal oferece estas opções:

| Opção | Ação |
| --- | --- |
| `1` | Iniciar uma partida |
| `2` | Consultar as regras |
| `3` | Consultar o placar acumulado |
| `4` | Encerrar o programa |

O jogador `X` começa. Em cada turno, os jogadores informam uma linha e uma coluna entre `1` e `3`. Uma posição ocupada ou uma coordenada inválida não consome a vez. Ao terminar a partida, escolha `1` para jogar novamente ou `0` para retornar ao menu.

Vence quem completar uma linha, coluna ou diagonal com três marcas. Se o tabuleiro for preenchido sem um vencedor, a partida termina empatada.

## Conteúdos de programação aplicados

- **Tipos de dados e variáveis:** textos para as opções do menu, entradas e símbolos dos jogadores; números inteiros para coordenadas, contadores e placar; valores booleanos para controlar o estado da partida.
- **Operadores aritméticos, relacionais e lógicos:** conversão das coordenadas para índices, contagem das marcas, comparação de valores e validação de entradas com condições lógicas.
- **Estruturas de decisão (`if`, `elif`, `else`):** seleção das opções do menu, validação de jogadas e identificação de vitória, empate ou troca de jogador.
- **Estruturas de repetição (`while`, `for` e `range()`):** execução do menu e das partidas, repetição da leitura até uma entrada válida e percurso das casas para exibir e verificar o tabuleiro.
- **Matrizes e `for` aninhado:** o tabuleiro é representado por uma lista de listas; os percursos aninhados exibem e atualizam as casas e verificam linhas, colunas, diagonais e espaços vazios.

O placar mantém a quantidade de vitórias de `X`, vitórias de `O` e empates enquanto o programa estiver aberto. Ele não é salvo após o encerramento. Esta versão não calcula percentuais.

## Restrições do projeto

O programa utiliza os conteúdos básicos estudados: variáveis, operadores, decisões, repetições, matrizes e funções nativas como `print()`, `input()` e `int()`. Não utiliza funções definidas pelo aluno (`def` ou `lambda`), dicionários, tuplas, conjuntos, listas de uma dimensão como vetores independentes, métodos de lista ou texto, compreensão de listas, bibliotecas externas, tratamento de exceções (`try/except`), classes ou orientação a objetos.

## Colaboradores e responsabilidades

As responsabilidades abaixo foram identificadas a partir do histórico de commits do projeto:

- **Heitor Terto (Heitor Oliveira Terto):** iniciou a estrutura do jogo e implementou o tabuleiro em matriz, o menu, o placar acumulado, as regras, a validação de entradas e jogadas, além da lógica de vitória, empate e alternância de turnos. Também realizou correções e ajustes nessas funcionalidades.
- **Vinicius:** contribuiu com a implementação inicial da interação para as jogadas no tabuleiro e participou, como coautor, das alterações de validação de entradas e jogadas.

## Arquivos

- `game.py` — código-fonte do jogo.
- `README.md` — documentação do projeto.
