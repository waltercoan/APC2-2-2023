#criar a funcao
def somanumeros(num1:int, num2:int):
    result = num1 + num2
    print("entrou", result)
    return result

#chamar a funcao
print("Antes")
varguarda = somanumeros(3,4)
print("Depois",varguarda)