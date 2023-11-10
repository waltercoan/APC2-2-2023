#entry point
#dunder method
#if __name__ == "__main__":
#    print("comando 1")
#    print("comando 2")
#    print("comando 3")

#def minhafuncao(repete:int, msg:str="comando"):
def minhafuncao(repete:int, msg:str="comando"):
    for i in range(repete):
        print(f"{msg} {i}")
    
def soma(num1:int, num2:int):
    return num1 + num2

print("Antes")
minhafuncao(3, 'qqcoisa')
print("Depois")
minhafuncao(msg="a para q da pra inverter", repete=5)
guardarresultado = soma(5,5)
print(guardarresultado)

n1 = int(input("Digite um numero"))
n2 = int(input("Digite outro numero"))
print(f"O resultado e : {soma(n1,n2)}")
