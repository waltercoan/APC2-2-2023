'''
2)	Faça um programa que receba dez números 
e armazene em uma lista. Em seguida conte 
quantos números são impar e quantos são 
par. Apresente os contadores na tela.
'''
lista = [0] * 10
for i in range(10):
    print("Digite um numero")
    lista[i] = int(input())

contapar = 0
contaimpar = 0
for i in range(10):
    #print(lista[i])
    if lista[i] % 2 == 0:
        contapar = contapar + 1
    else:
        contaimpar = contaimpar + 1
print("Numero de pares", contapar)
print("Numero de impares", contaimpar)