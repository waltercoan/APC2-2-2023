'''
REPETIÇÃO4) Faça um programa que leia 
um número N que indica quantos valores 
inteiros e positivos devem ser lidos 
a seguir. Para cada número lido, mostre 
o valor lido e o fatorial desse valor.
'''

print("Digite o valor de N")
n = int(input())

#aquinao
for i in range(n):
    print("i", i)
    print("Digite o fatorial desejado")
    fat = int(input())
    result = 1
    for x in range(fat,0,-1):
        #print(x,end=" ")
        result = result * x
    print(fat,"!=",result)
#aqui2
