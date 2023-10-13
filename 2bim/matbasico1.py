'''
1)	Faça um programa para ler e imprimir 
uma matriz 2 × 4 de números inteiros.
'''
matriz = [[0] * 4 for i in range(2)]

for lin in range(2):
    for col in range(4):
        print("Digite um numero")
        matriz[lin][col] = int(input())

for lin in range(2):
    for col in range(4):
        print(matriz[lin][col],end="|")
    print()
