listax = [0] * 10

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

