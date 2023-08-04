'''
REPETIÇÃO6) Elaborar um programa que efetue
a leitura de 10 valores numéricos e apresente 
no final o total do somatório e a média do total.
'''
soma = 0
for i in range(10):
    n = int(input("Digite um numero"))
    soma = soma + n #Acumulador-totalizador
print("soma:", soma)
media = soma / 10
print("media", media)

