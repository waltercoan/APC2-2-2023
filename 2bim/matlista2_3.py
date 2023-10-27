'''
3)	Faça um programa que receba o estoque atual de 
três produtos que estão armazenados em quatro 
armazéns e coloque esses dados em uma matriz 5x3. 
Sendo que a última linha da matriz contém o custo 
de cada produto, calcule e mostre:
a.	A quantidade de itens  armazenas em cada armazém
b.	Qual o armazém possui maior estoque do produto 2;
c.	Qual o armazém possui menor estoque
d.	Qual o custo total de cada produto
e.	Qual o custo total de cada armazém
'''
dados = [[0] * 3 for i in range(5)]
for linha_armazem in range(4):
    print("Armazem",linha_armazem+1)
    for col_produto in range(3):
        print("Produto",col_produto+1)
        print("Digite a quantidade")
        dados[linha_armazem][col_produto] = int(input())
for col_produto in range(3):
    print("Produto",col_produto+1)
    print("Digite o custo")
    dados[4][col_produto] = int(input())

#a.	A quantidade de itens  armazenas em cada armazém
for linha_armazem in range(4):
    total_armazem = 0
    for col_produto in range(3):
        total_armazem += dados[linha_armazem][col_produto]
    print("Total do armazem e ",total_armazem)

#b.	Qual o armazém possui maior estoque do produto 2;
omaior = 0
armazem_maior = 0
for linha_armazem in range(4):
    if dados[linha_armazem][1] > omaior:
        omaior = dados[linha_armazem][1]
        armazem_maior = linha_armazem
print("No armazem",armazem_maior,
    " ocorreu o maior valor de ",omaior)


#c.	Qual o armazém possui menor estoque
omenor = 0
armazem_menor = 0
for linha_armazem in range(4):
    total_armazem = 0
    for col_produto in range(3):
        total_armazem += dados[linha_armazem][col_produto]
    if linha_armazem == 0:
        omenor = total_armazem
        armazem_menor = linha_armazem
    else:
        if total_armazem < omenor:
            omenor = total_armazem
            armazem_menor = linha_armazem
print("O armazem ", armazem_menor,
      " possui a menor quantidade de produtos", omenor)

#d.	Qual o custo total de cada produto
for col_produto in range(3):
    somaqtd=0
    for linha_armazem in range(4):
        somaqtd += dados[linha_armazem][col_produto]
    custoprod = somaqtd * dados[4][col_produto]
    print("O custo total do produto ", col_produto+1,
         " é de ",custoprod)

#e.	Qual o custo total de cada armazém
for linha_armazem in range(4):
    custo_tot_armazem = 0
    for col_produto in range(3):
        custo_tot_armazem += dados[linha_armazem][col_produto] * \
                            dados[4][col_produto]
    print("O custo total do armazem", linha_armazem+1,
            " e de R$ ", custo_tot_armazem)
