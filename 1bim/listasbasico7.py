'''
Faça um programa que receba dez 
números e armazene em uma lista. 
Em seguida copie todos os números 
da primeira lista para uma segunda 
lista, mas na ordem invertida da 
primeira lista.
'''
lista = [0] * 10
listainv = [0] * 10
for i in range(10):
    print("Digite um numero")
    lista[i] = int(input())

destino = 9
for origem in range(10):
    listainv[destino] = lista[origem]
    destino -= 1
print(listainv)


