import numpy as np
#Ler duas listas e gerar uma terceira sem elementos repetidos
lista1 = []
lista2 = []
lista3 = []
print()
elementos = int(input('Quantos elementos você quer na listas? '))
for i in range (1, elementos + 1):
    valor = int(input('Digite o {} valor para ser inserido na primeira lista: '.format(i)))
    if valor == 0:
        break
    lista1.append(valor)
print('-' * 30)
for j in range (1, elementos + 1):
    valor = int(input('Digite o {} valor para ser inserido na segunda lista: '.format(j)))
    if valor == 0:
        break
    lista2.append(valor)
lista3 = np.unique(lista1 + lista2)
print('\nA soma das listas sem repetição é: {}\n'.format(lista3)) 