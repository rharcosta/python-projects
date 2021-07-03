#Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos
#caracteres da segunda pelos da terceira.
string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')
string3 = input('Digite a terceira string: ')

if len(string2) == len(string3):
    resultado = ""
    for i in string1:
        posicao = string2.find(i)
        if posicao != -1:
            resultado += string3[posicao]
        else:
            resultado += i

    if resultado == "":
        print('Todos os caracteres foram removidos!')
    else:
        print(f'\nOs caracteres {string2} foram substituídos por {string3} em {string1}, gerando: {resultado}\n')
else:
    print('Erro! A segunda e a terceira string devem ter o mesmo tamanho!\n')

