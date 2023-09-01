listax = [0] * 10
listay = [0] * 10
'''
print("Conjunto X")
for i in range(10):
    achei = False
    while True:
        print("Digite um numero")
        aux = int(input())
        for j in range(10):
            if aux == listax[j]:
                print("Numero duplicado")
                achei = True
        if not achei:
            listax[i] = aux
            break

print("Conjunto Y")
for i in range(10):
    while True:
        achei = False
        print("Digite um numero")
        novonum = int(input())
        for j in range(10):
            if novonum == listay[j]:
                achei = True
                print("Numero duplicado")
                break
        if not achei:#if achei == False:
            listay[i] = novonum
            print("Numero cadastrado")
            break

#a.	a união de X com Y 
# (todos os elementos de X 
# e os elementos de Y que não estejam em X)
print("UNIÃO")
listauniao = [0] * 20

# (todos os elementos de X 
for i in range(10):
    listauniao[i] = listax[i]
# e os elementos de Y que não estejam em X)
proxlivre = 10
for i in range(10):
    # i = indexador da listaY
    achei = False
    for j in range(10):
        # j = indexador da listaX
        if listay[i] == listax[j]:
            achei = True
            break
    if not achei:
        listauniao[proxlivre] = listay[i]
        proxlivre += 1
print(listauniao)
'''
##b.	a diferença entre X e Y 
# (todos os elementos de X que não existam em Y)
listax = [1,2,3,4,5,6,7,8,9,10]
listay = [10,2,30,4,50,6,70,8,90,10]

listadif = [0] * 10

proxlivre = 0
for i in range(10): #i indexador do X
    print(listax[i])
    achei = False
    for j in range(10): #j indexador do Y
        print("\t", listay[j])
        if listax[i] == listay[j]:
            print("ACHEI")
            achei = True
            break
    if not achei:
        listadif[proxlivre] = listax[i]
        proxlivre += 1
print(listadif)

##c.a soma entre X e Y (soma de 
# cada elemento de X com o elemento de mesma posição em Y)
listasoma = [0] * 10
print("SOMA DOS CONJUNTOS")
for i in range(10):
    listasoma[i] = listax[i] + listay[i]
print(listasoma)

##d.	produto entre X e Y (multiplicação de 
# cada elemento de X com o elemento de mesma posição em Y)
listamulti = [0] * 10
print("MULTIPLICAÇÃO DOS CONJUNTOS")
for i in range(10):
    listamulti[i] = listax[i] * listay[i]
print(listamulti)

##e.a interseção entre X e Y (apenas 
# os elementos que aparecem nos dois vetores)
listainter = [0] * 10

proxlivre = 0
print("INTERSECAO")
for i in range(10): #indexador do X
    print(listax[i])
    for j in range(10): #indexador do Y
        print("\t", listay[j])
        if listax[i] == listay[j]:
            listainter[proxlivre] = listax[i]
            break
print(listainter)