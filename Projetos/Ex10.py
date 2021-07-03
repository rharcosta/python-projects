import numpy as np
matriz = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11, 12]])
print()
print(matriz)
print()
opcao = int(input('Digite 1 para operações com as linhas e 2 para operações com as colunas da matriz: '))
if opcao == 1:
    linha = int(input('Digite qual linha deseja [1, 2 ou 3]: '))
    if linha == 1:
        desvio = media = matriz[0]
    elif linha == 2:
        desvio = media = matriz[1]
    elif linha == 3:
        desvio = media = matriz[2]
    else:
      print('Opção inválida!')  
    print(f'\nMédia aritmética da linha: {media.mean():.2f}\n')
    print(f'Desvio padrão da linha: {desvio.std():.2f}\n')
elif opcao == 2:
    coluna = int(input('Digite qual coluna deseja [1, 2, 3 ou 4]: '))
    if coluna == 1:
        desvio = media = matriz[:,0]
    elif coluna == 2:
        desvio = media = matriz[:,1]
    elif coluna == 3:
        desvio = media = matriz[:,2]
    elif coluna == 4:
        desvio = media = matriz[:,3]
    else:
      print('Opção inválida!')
    print(f'\nMédia aritmética da coluna: {media.mean():.2f}\n')
    print(f'Desvio padrão da coluna: {desvio.std():.2f}\n')
else: 
    print('Opção inexistente!')