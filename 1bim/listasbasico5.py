'''
Faça um programa que receba dez 
números e armazene em uma lista. 
Em seguida percorra toda a lista 
e procure qual o MAIOR valor dentro 
da lista e qual o MENOR valor dentro 
da lista. No final apresente o 
MAIOR e o MENOR valor.
'''
omaior = 0
omenor = 0
lista = [0] * 10
for i in range(10):
    print("Digite um numero")
    lista[i] = int(input())

for i in range(10):
    if lista[i] > omaior:
        omaior = lista[i]
    #nunca mistar logica do maior e menor
    if i == 0: #estou na primeira volta do FOR
        omenor = lista[i]
    else: #para todos os outros numeros
        if lista[i] < omenor:
            omenor = lista[i]
print("O maior numero e", omaior)
print("O menor numero e", omenor)
