'''
3)	Faça uma função que receba as 
três notas de um aluno como parâmetro 
e uma letra. Se a letra for A o 
procedimento calcula a média aritmética 
das notas do aluno, se for P o 
procedimento calcula a média ponderada 
com os pesos 5,3 e 2. A média calculada 
deve ser devolvida ao programa principal 
para, então, ser mostrada.
'''

def calcmedia(n1:int,n2:int,n3:int,tipo:str):
    media = 0
    if tipo == "A" or tipo == "a":
        media = (n1 + n2 + n3) / 3
    else:
        media = ((n1*5) + (n2*3) + (n3*2)) / 10
    return media

mf = calcmedia(2,10,5,'a')
print(f"Media Final: {mf}")