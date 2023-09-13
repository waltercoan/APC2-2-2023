'''
Faça um programa que preencha um vetor 
com os nomes dos modelos de cinco carros 
(exemplo: fusca, gol). Carregue outro 
vetor com o consumo desses carros, isto 
é, quantos quilômetros cada um deles fez 
com um litro de combustivel. Calcule e 
mostre:
- o modelo de carro mais econômico
- quantos litros de combustível cada um 
dos carros cadastrados consome para 
percorrer uma distância de 1000 km.
'''

listacarros = [''] * 5
listaconsumo = [0] * 5

for i in range(5):
    print('Digite o nome do carro')
    listacarros[i] = input()
    print('Digite o consumo em km')
    listaconsumo[i] = int(input())

omaior = 0
qualomaior=0
for i in range(5):
    if listaconsumo[i] > omaior:
        omaior = listaconsumo[i]
        qualomaior = i
print("O carro", listacarros[qualomaior])
print("possui o menor consumo de", omaior)

for i in range(5):
    result = 1000 / listaconsumo[i]
    print("Carro",listacarros[i], "consome",result,"litros")
    
