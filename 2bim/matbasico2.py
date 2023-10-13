'''
2)	Ler uma matriz A de duas dimensões 
com 7 linhas e 7 colunas. Ao final apresentar 
o total de elementos pares existentes 
dentro da matriz.
'''
import random
matriz = [[0] * 7 for _ in range(7)]

for lin in range(7):
    for col in range(7):
        matriz[lin][col] = random.randint(0,100)

soma = 0
for lin in range(7):
    for col in range(7):
        if matriz[lin][col] % 2 == 0:
            soma += matriz[lin][col]
print("A soma dos pares e", soma)