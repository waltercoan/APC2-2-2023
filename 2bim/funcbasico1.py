'''
1)	Faça uma função que receba três números
 inteiros: a,b e c, onde a é maior que 1. 
 A função deve somar todos os inteiros 
 entre b e c que sejam divisíveis 
 por a (inclusive b e c) e retornar 
 o resultado para a função principal.
'''
def minhafuncao(a:int, b:int, c:int):
    soma = 0  
    for i in range(b,c+1):
        if i % a == 0:
            soma += i
    return soma

resultado = minhafuncao(2,0,100)
print(resultado)