'''
2)	Faça uma função que transforme 
e mostre segundos em horas, minutos 
e segundos. Todas as variáveis devem 
ser passadas como parâmetro, não 
havendo variáveis globais.
a.	1h = 3600s
b.	1m = 60s
'''

def conv(segundos:int):
    horas = int(segundos / 3600)
    sobraseg = segundos - (horas * 3600)
    minutos = int(sobraseg / 60)
    sobraseg = sobraseg - (minutos * 60)
    print(f"{horas}h:{minutos}m:{sobraseg}s")

conv(10000)