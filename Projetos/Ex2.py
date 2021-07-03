lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))

if (lado1+lado2) > lado3 and (lado1+lado3) > lado2 and (lado2+lado3) > lado1:
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Isósceles')
    elif lado1 == lado2 and lado2 == lado3:
        print('Equilátero')
    else: 
        print('Escaleno')
else: 
    print('Não é um triângulo!')