#Pesquisa Binária
listanum = [100,18,200,13,17,2,7,42]
#Parte 1 - ORDENAR OS NUMEROS  - ALG DA BOLHA
for i in range(len(listanum)-1):
    for j in range(i+1,len(listanum)):
        if listanum[i] > listanum[j]:
            aux = listanum[i]
            listanum[i] = listanum[j]
            listanum[j] = aux
print(listanum)

#Parte 2 - Pesquisa Binária
procurado = int(input("Digite o numero procurado"))
ini = 0
fim = len(listanum)-1
while ini <= fim:
    meio = int((ini + fim) / 2)
    if procurado == listanum[meio]:
        print("Achei!!!")
        break
    else:
        if procurado > listanum[meio]:
            ini = meio + 1
        else:
            fim = meio - 1
if not ini <= fim:
    print("Nao achei!....")

