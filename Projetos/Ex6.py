lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

#imprimir o maior elemento
print(f'\n\nO maior elemento da lista é {max(lista)}')

#imprimir o menor elemento
print(f'O menor elemento da lista é {min(lista)}')

#imprimir os números pares
print('Os números pares são: ', end='')
for i in lista:
    if i % 2 == 0:
        print(i, end=', ')

#imprimir o número de ocorrências do primeiro elemento da lista
print(f'\nO número de ocorrências do primeiro elemento é {lista.count(12)}')

#imprimir a média dos elementos
print(f'A média dos elementos é {sum(lista)/len(lista):.2f}')

#imprimir a soma dos elementos de valor negativo
soma = 0
for i in lista:
    if(i < 0):
        soma += i
print(f'A soma dos elementos negativos é {soma}\n')
