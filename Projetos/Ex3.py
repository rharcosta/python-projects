#Jogo da Velha
#Autor: Rubia Helena Archanjo 
#RA: 201910663

velha =""" 
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6
---+---+---  ---+---+---
   |   |      1 | 2 | 3
 """
posicoes = [None, (5,1), (5,5), (5,9), (3,1), (3,5), (3,9), (1,1), (1,5), (1,9)]
ganhar = [[1,2,3],[4,5,6],[7,8,9], #Linhas
          [7,4,1], [8,5,2], [9,6,3], #Colunas
          [7,5,3], [1,5,9]] #Diagonais

tabuleiro = []
for linha in velha.splitlines():
    tabuleiro.append(list(linha))

jogador = "X"
jogando = True
jogadas = 0 

while True:
    for i in tabuleiro: #Imprimindo tabuleiro
        print("".join(i))

    if not jogando:
        break

    if jogadas == 9: #Todas as posições ocupadas
        print("Ninguém ganhou! Deu velha!")
        break

    jogada = int(input("Digite a posição entre 1 e 9 (jogador %s): " %jogador))
    if jogada < 1 or jogada > 9:
        print("Essa posição é inválida!")
        continue

    if tabuleiro[posicoes[jogada][0]][posicoes[jogada][1]] != " ": #Verificação se a posição está livre
        print("Essa posição está ocupada!")
        continue

    #Marca a jogada do jogador
    tabuleiro[posicoes[jogada][0]][posicoes[jogada][1]] = jogador
    for j in ganhar: #verificação se ganhou
        for k in j: 
            if tabuleiro[posicoes[k][0]][posicoes[k][1]] != jogador:
                break 
        else:
            print("O jogador %s ganhou a partida! (%s): "%(jogador, j))
            jogando = False
            break
    jogadas +=1 #Contador
    jogador = "X" if jogador == "O" else "O" #Alterna o jogador
    
