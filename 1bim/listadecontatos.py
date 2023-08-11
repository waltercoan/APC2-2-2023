listanomes = []
listatelefones = []
opcao = 0

while opcao != 3:
    print("Lista Telefonica")
    print("1 - incluir numero")
    print("2 - listar numeros")
    print("3 - sair")
    print("Digite o numero da opcao")
    opcao = int(input())
    if opcao == 1:
        print("Incluir numero")
        nome = input("Digite seu nome")
        telefone = input("Digite seu telefone")
        listanomes.append(nome)
        listatelefones.append(telefone)
    
    if opcao == 2:
        print("Listar numeros")
        tamanho = len(listanomes)
        for i in range(tamanho):
            print(f"Nome: {listanomes[i]} - {listatelefones[i]}")