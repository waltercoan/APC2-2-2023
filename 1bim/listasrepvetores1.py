'''
Faça um programa que carregue dois vetores 
de dez elementos numéricos cada um e 
mostre um vetor resultante da intercalação 
desses dois vetores.
'''
listaa = [0] * 10
listab = [0] * 10
listainter = [0] * 20

for i in range(10):
    print("Digite um numero (listaa)")
    listaa[i] = int(input())
for i in range(10):
    print("Digite um numero (listab)")
    listab[i] = int(input())

proxlivre = 0
for i in range(10):
    listainter[proxlivre] = listaa[i]
    proxlivre = proxlivre + 1
    listainter[proxlivre] = listab[i]
    proxlivre = proxlivre + 1

print(listainter)