'''
REPETIÇÃO5) Elaborar um programa que apresente
os valores de conversão de graus Celsius em 
Fahrenheit, de 10 em 10 graus, iniciando a 
contagem em 10 graus Celsius e finalizando em 
100 graus Celsius. O programa deverá apresentar 
os valores das duas temperaturas.
'''
'''
celsius = 10
while celsius <= 100:
    fah = (celsius * 1.8) + 32
    print("Celsius: ",celsius, " Fahrenheit: ", fah)
    celsius = celsius + 10
'''

for celsius in range(10,101,10):
    fah = (celsius * 1.8) + 32
    print("Celsius: ",celsius, " Fahrenheit: ", fah)


