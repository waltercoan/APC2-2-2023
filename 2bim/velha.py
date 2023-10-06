velha = [[' '] * 3 for i in range(3)]
jogador = "X"
while True:
    for lin in range(3):
        for col in range(3):
            print(velha[lin][col],end="|")
        print("\n------")
    print("Jogador: ",jogador)
    print("Digite o num da linha")
    numlinha = int(input())
    print("Digite o num da coluna")
    numcoluna = int(input())
    velha[numlinha-1][numcoluna-1] = jogador
    if jogador == "X":
        jogador = "O"
    else: 
        jogador = "X"

#Validar sobreposição de jogadas
#Validar vencedor
#Validar empate