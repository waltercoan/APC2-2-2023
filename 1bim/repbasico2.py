'''
REPETIÇÃO2) Elabore um programa que 
apresente no final o somatório dos 
valores pares existentes 
na faixa de 1 até 500.
'''
soma = 0 #acumulador
for i in range(0,501): #bloco de repetição 1 a 500
    if i % 2 == 0: #se o resto div i por 2 for igual a ZERO
        print(i, end=' ') #Imprime o numero par
        soma = soma + i  #soma/acumula o numero PAR
print("A soma dos numeros pares de 1 a 500 e ", soma) #mostra a soma