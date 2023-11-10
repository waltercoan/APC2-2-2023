n1 = 0
n2 = 0 
n3 = 0 

def entradas():
    global n1,n2,n3
    n1 = int(input("Digite um valor"))
    n2 = int(input("Digite um valor"))
    n3 = int(input("Digite um valor"))


qqcoisa = entradas()
print(type(qqcoisa))
v1,v2,v3 = qqcoisa
print(v1)
print(v2)
print(v3)