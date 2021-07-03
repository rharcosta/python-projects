#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado:#

km = float(input('Qual foi a quantidade de KM rodados? '))
dia = int(input('Qual foi a quantidade de dias que o carro ficou alugado? ')) 
valorkm = km*0.15
valordia = dia*60
total = valorkm + valordia
print('O preço que o cliente deverá pagar é R$ {:.3f} pelos KM rodados e R$ {} pelos dias alugados. Resultando em um total de R$ {}'.format(valorkm, valordia, total))