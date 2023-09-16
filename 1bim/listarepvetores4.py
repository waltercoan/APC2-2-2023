'''
VETORES4 - Faça um programa que receba a temperatura 
média de cada mês do ano e armazene-as em um vetor. 
Calcule e mostre a maior e a menor temperatura do 
ano e em que mês elas ocorreram (mostrar o mês 
por extenso: 1- Janeiro, 2 – Fevereiro). 
Desconsidere empates.
'''
listameses = ['janeiro','fevereiro',
    'marco','abril','maio','junho',
    'julho','agosto','setembro',
    'outubro','novembro','dezembro']
listatemp = [0] * 12

for i in range(12):
    print("Digite a temp do mes", listameses[i])
    listatemp[i] = float(input())

omaior = 0
mesmaisquente = ''
omenor = 0
mesmaisfrio = ''
for i in range(12):
    #logica do maior
    if listatemp[i] > omaior:
        omaior = listatemp[i]
        mesmaisquente = listameses[i]
    #logica do menor
    if i == 0: #considerar o primeiro valor como o menor
        omenor = listatemp[i]
        mesmaisfrio = listameses[i]
    else:
        if listatemp[i] < omenor:
            omenor = listatemp[i]
            mesmaisfrio = listameses[i]
print("No mes ", mesmaisquente,
"houve a temp de ", omaior)

print("No mes ", mesmaisfrio,
"houve a temp de ", omenor)
