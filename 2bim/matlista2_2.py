'''
2)	Faça um programa que receba as vendas 
semanais (de um mês) de cinco vendedores de 
uma loja e armazene essas vendas em uma
matriz. Calcule e mostre:
a.	O total de vendas do mês de cada vendedor
b.	O total de vendas de cada semana (todos os vendedores juntos)
c.	O total de vendas do mês

'''
vendas = [[0] * 4 for i in range(5)]
for vendedor in range(5):
    for semana in range(4):
        print("Vendedor ", (vendedor+1))
        print("Digite o valor da venda")
        vendas[vendedor][semana] = float(input())
#a.	O total de vendas do mês de cada vendedor
for linha_vendedor in range(5):
    somadovendedor = 0
    for col_semana in range(4):
        somadovendedor += vendas[linha_vendedor][col_semana]
    print("Total e ", somadovendedor)

#b.	O total de vendas de cada 
# semana (todos os vendedores juntos)
for col_semana in range(4):
    somasemana = 0
    for linha_vendedor in range(5):
        somasemana += vendas[linha_vendedor][col_semana]
    print("O total e ", somasemana)

#c.	O total de vendas do mês
total = 0
for linha_vendedor in range(5):
    for col_semana in range(4):
        total += vendas[linha_vendedor][col_semana]
print("Total geral", total)

