'''
VETORES6 - Faça um programa que simule um 
controle bancário. Para tanto, devem ser 
lidos os códigos de dez contas e os seus 
respectivos saldos. Os códigos devem ser 
armazenados em um vetor de números inteiros 
(não pode haver mais que uma conta com o 
mesmo código) e os saldos devem ser armazenados
em um vetor de números reais. O saldo deverá 
ser cadastrado na mesma posição do código. Por 
exemplo, se a conta 504 for armazenada na 
quinta posição do vetor de saldos. Depois de 
fazer a leitura dos valores, mostrar o seguinte menu na tela:

i.	Efetuar depósito
ii.	Efetuar saque
iii. Consultar o ativo bancário (ou seja, o somatório dos saldos de todos os clientes)
iv.	Finalizar o programa
Para efetuar depósito deve-se solicitar o código da conta e o valor a ser depositado. Se a conta não estiver cadastrada, mostrar a mensagem Conta não encontrada e voltar ao menu. Se a conta existir, atualizar o seu saldo.
Para efetuar saque deve-se solicitar o código da conta e o valor a ser sacado. Se a conta não estiver cadastrada, mostrar a mensagem Conta não encontrada e voltar ao menu. Se a conta existir, verificar se o seu saldo é suficiente para cobrir o saque. (Estamos supondo que a conta não pode ficar com o saldo negativo). Se o saldo for suficiente, realizar o saque e voltar ao menu. Caso contrário mostrar a mensagem Saldo insuficiente e voltar ao menu.
Para consultar o ativo bancário deve-se somar o saldo de todas as contas do banco. Depois de mostrar esse valor, voltar ao menu.
O programa só termina quando for digitada a opção 4 – Finalizar o programa.
'''

listacontas = [0] * 10
listasaldo = [0] * 10

for i in range(10):
    while True:
        print("Digite o numero da nova conta")
        novaconta = int(input())
        achei = False
        for j in range(10):
            if listacontas[j] == novaconta:
                achei = True
                break
        if achei == False:
            listacontas[i] = novaconta
            break
        else:
            print("Numero da conta repetido")
    print("Digite o saldo")
    listasaldo[i] = float(input())


#aqui voce vai programar as entradas
opcao = 0
while opcao != 4:
    print("Menu principal")
    print("1. Efetuar deposito")
    print("2. Efetuar saque")
    print("3. Consultar ativos")
    print("4. Sair")
    print("Digite a opcao")
    opcao = int(input())
    if opcao == 1:
        print("Deposito")
    if opcao == 2:
        print("SAQUE")
    if opcao == 3:
        print("Consulta")
    if opcao == 4:
        print("Até logo e obrigado pelos peixes")
