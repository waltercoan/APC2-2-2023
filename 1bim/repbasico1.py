'''
REPETIÇÃO1) Faça um programa que 
apresente no final o somatório 
dos números de 1 até 100.
import time
while True: 
    print("Rodando")
    time.sleep(0.00001)
'''


#contador = 1 #variavel contador
#soma = 0
#while contador <= 100: #repete enquanto nao chega no 100
#    print(contador, end=" ") #imprimir o valor do contador
#    soma = soma + contador #acumulador
#    contador = contador + 1 #contador
#print("A soma e ", soma)
soma = 0
for i in range(1, 101):
    print(i, end=" ")
    soma = soma + i
print("A soma e ", soma)