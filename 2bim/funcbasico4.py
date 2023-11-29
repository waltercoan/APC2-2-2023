'''
4)	Faça uma função que receba cinco 
valores inteiros, e retorne o maior 
valor. Faça uma segunda função que 
receba também cinco valores e retorne 
o menor deles.
'''
#VARARGS
def maior(*listanumeros):
    maior = 0
    for umnumero in listanumeros:
        if maior < umnumero:
            maior = umnumero
    return maior
def menor(*listanumeros):
    menor = 9999999
    for umnumero in listanumeros:
        if menor > umnumero:
            menor = umnumero
    return menor

res = maior(1,2,3,4,5)
print(res)
res = menor(1,2,3,4,5)
print(res)
