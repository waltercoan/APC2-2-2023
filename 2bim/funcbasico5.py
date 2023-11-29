'''
5)	Foi realizada uma pesquisa de algumas características 
físicas de cinco habitantes de uma certa região. De cada 
habitante foram coletados os seguintes dados: 
sexo, cor dos olhos (A – Azuis ou C – Castanhos), 
cor dos cabelos (L – Louros, P – Pretos ou C – Castanhos) 
e idade.
a.	Faça uma função que leia esses dados em vetores. 
Determine, por meio de outra função, a média de idade 
das pessoas com olhos castanhos e cabelos pretos. 
Mostre esse resultado no programa principal.
b.	Faça uma função que determine e devolva ao 
programa principal a maior idade entre os habitantes.
c.	Faça uma função que determine e devolva ao programa 
principal a quantidade de indivíduos do sexo 
feminino cuja idade está entre 18 e 35 (inclusive) 
e que tenham olhos azuis e cabelos louros.
'''
pessoas = 5
listasexo = [' '] * pessoas
listacorolho = [' '] * pessoas
listacorcabelo = [' '] * pessoas
listaidade = [0] * pessoas

def entradas():
    for umapessoa in range(pessoas):
        print(f"Pessoa:{umapessoa+1}")
        listasexo[umapessoa] = input("Digite o sexo M/F")
        listacorolho[umapessoa] = input("Digite a cor do olho Azul/Verde/Cast/Preto")
        listacorcabelo[umapessoa] = input("Digite a cor do cabelo Loiro/Ruivo/Cast/Preto")
        listaidade[umapessoa] = int(input("Digite a idade"))

def mediaidade():
    #com olhos castanhos e cabelos pretos
    somaidades = 0 
    contapessoas = 0
    for umapessoa in range(pessoas):
        if listacorolho[umapessoa] == "c" and \
            listacorcabelo[umapessoa]  == "p":
            somaidades += listaidade[umapessoa]
            contapessoas += 1
    media = somaidades / contapessoas
    return media

def maioridade():
    return max(listaidade)


def contapessoas():
    contador = 0 
    for umapessoa in range(pessoas):
        if listasexo[umapessoa] == 'f' and \
            (listaidade[umapessoa] >= 18 and listaidade[umapessoa] <= 35) and \
            listacorolho[umapessoa] == 'a' and \
            listacorcabelo[umapessoa] == 'l':
            contador += 1
    return contador

if __name__ == "__main__":
    entradas()
    result = mediaidade()
    print("Media da idade das pessoas")
    print("com olho castanho e cabelo preto e: ", result)
    result = maioridade()
    print("Maior idade", result)
    result = contapessoas()
    print("Qtd de mulheres com idade entre 18 e 35")
    print("com cor de olho azul e cabelo loiro", result)
    
