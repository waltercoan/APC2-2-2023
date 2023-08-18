'''
4)	Faça um programa que receba dez números
e armazene em uma lista. Em seguida calcule 
a soma de todos os números percorrendo 
novamente a lista. Apresente a soma 
e em seguida a média baseada na soma 
e no número de números armazenados.
'''
lista = [0] * 10

for i in range(10):
    print("Digite um numero")
    lista[i] = int(input())

soma = 0
for i in range(10):
    soma = soma + lista[i]

media = soma / 10
print("A media e ", media)
