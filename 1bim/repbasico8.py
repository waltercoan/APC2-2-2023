'''
REPETIÇÃO8) Elaborar um programa que efetue a 
leitura de valores positivos inteiros até que 
um valor negativo seja informado. Ao final 
deve ser apresentados o maior e o menor 
número informado pelo usuário.
'''
omaior = 0
omenor = 0
contador = 0
while True:
    print("Digite um numero")
    num = int(input())
    if num < 0:
        break
    if num > omaior:
        omaior = num
    #NAO MISTURAR AS LOGICAS DO MAIOR E DO MENOR
    if contador == 0:
        omenor = num
    else:
        if num < omenor:
            omenor = num
    contador = contador + 1
print("O maior de todos e ", omaior)
print("O menor de todos e", omenor)