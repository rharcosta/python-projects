#Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string
string = input('Digite uma string: ')
count = {}

for i in string:
    count[i] = count.get(i,0) + 1

for chave, valor in count.items():
    print(f'{chave}: {valor}x')
print()