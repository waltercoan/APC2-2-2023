lista = [4,5,9,2,6]
print(lista)
#for inicia ZERO ate penultima casa
for i in range(len(lista)-1):
    print(lista[i])
    #for inicia 1 depois da primera
    #e vai ate a ultima casa
    for j in range(i+1,len(lista)):
        print('\t',lista[j])
        if lista[j] < lista[i]:
            print("Troca",lista[j],"por",lista[i])
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            #lista[i],lista[j] = lista[j],lista[i]
print(lista)