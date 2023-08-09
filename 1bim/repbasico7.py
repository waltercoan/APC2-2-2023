'''
REPETIÇÃO7) Elaborar um programa que efetue a leitura 
sucessiva de valores numéricos e apresente no final o 
total do somatório, a média e o total de valores lidos. 
O programa deve fazer as leituras dos valores enquanto o 
usuário estiver fornecedor valores positivos. Ou seja, o 
programa deve parar quando o usuário fornecer um valor 
negativo.
'''

soma = 0
contador = 0
while True:
    print("Digite um numero")
    num = int(input())
    #aqui1
    if num < 0:
        break
    soma = soma + num
    contador = contador + 1
        
#fim do programa
print("A soma dos numeros e", soma)
if contador > 0:
    media = soma / contador
    print("A media e", media)