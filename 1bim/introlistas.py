#variaveis simples
nome = "zezinho"
#variaveis compostas (listas)
nomes = ["zezinho","mariazinha"]
#como acessar uma lista
print(nomes[0])
print(nomes[1])
#print(nomes[2]) ERRO
nomes[0] = "Huguinho"
print(nomes)

numeros = [0] * 10
cont = 0
while cont < 10:
    numeros[cont] = 10 * (cont+1)
    cont = cont + 1
print(numeros)

for i in range(10):
    numeros[i] = 10 * (i + 1)
print(numeros)

numeros = list(range(10,101,10))
print(numeros)
