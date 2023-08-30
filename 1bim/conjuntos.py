listax = [0] * 10
listay = [0] * 10
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

