'''
1)	Faça um programa que carregue uma matriz 3x5 
com números inteiros, calcule e mostre a 
quantidade de elementos entre 15 e 20.
'''
import random
#            Num Col           Num Linhas
matriz = [[0] * 5 for i in range(3)]

for lin in range(3):
    for col in range(5):
        matriz[lin][col] = random.randint(0,100)
print(matriz)

contador = 0
for lin in range(3):
    for col in range(5):
        if matriz[lin][col] >= 15 and matriz[lin][col] <= 20:
            contador += 1
print("O num de elementos entre 15 e 20 e ", contador)

