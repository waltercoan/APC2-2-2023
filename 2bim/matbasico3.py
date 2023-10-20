'''
3)	Dada a seguinte matriz, calcule:
- A soma dos elementos de primeira coluna;
- O produto dos elementos da primeira linha;
- A soma de todos os elementos;
- O produto da diagonal principal.
'''

matriz =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

'''
soma = matriz[0][0] +  \
       matriz[1][0] + \
       matriz[2][0] + \
       matriz[3][0] 
'''
#- A soma dos elementos de primeira coluna;
soma = 0
for lin in range(4):
    soma += matriz[lin][0]
print("Soma da primeira coluna", soma)

#- O produto dos elementos da primeira linha;

prod = 1
for col in range(4):
    prod *= matriz[0][col]
print("A multiplicação da primeira linha e ", prod)

#- A soma de todos os elementos;
somatudo = 0
for lin in range(4):
    for col in range(4):
        somatudo += matriz[lin][col]
print("A soma de tudo e ", somatudo)

#- O produto da diagonal principal.
proddiag=1
for i in range(4):
    proddiag*= matriz[i][i]
print("Produto da diagonal principal", proddiag)