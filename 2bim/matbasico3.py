matriz =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

matriz = [[0] * 4 for i in range(4)]
cont = 1
for lin in range(4):
    for col in range(4):
        matriz[lin][col] = cont
        cont+=1
