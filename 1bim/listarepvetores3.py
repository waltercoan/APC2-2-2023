'''
VETORES3 - Faça um programa para corrigir provas de 
múltipla escolha com somatória. Cada prova tem dez 
questões e cada questão vale 1 ponto. O primeiro 
conjunto de dados a ser lido é o gabarito da prova. 
Os outros dados serão os números dos alunos e sua 
respectivas respostas. Existem 15 alunos matriculados. 
Calcule e mostre:
- Para cada aluno seu número e sua nota;
- A percentagem de aprovação, sabendo-se que a 
nota mínima é 6,0
'''

gaba = [0] * 10
print("Digite o GABARITO da prova")
for i in range(10):
    print("Questao",i+1,"digite a resposta")
    gaba[i] = int(input())

print("CORRECAO DAS PROVAS")
contaaprov = 0
for aluno in range(15):
    print("Aluno: ", aluno+1)
    matricula = int(input("Digite a matricula"))
    nota = 0
    for questao in range(10):
        print("Questao", questao+1,"digite a resposta")
        resp = int(input())
        if gaba[questao] == resp:
            nota += 1
    print("Nota", nota)
    if nota >= 6:
        contaaprov += 1
percaprov = (15 * 100) / contaaprov
print("O perc de aprovados e", percaprov)



