##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
L = open('data.csv','r').readlines()
L = [line.split('\t') for line in L]
R = [sum(h) for h in [[int(i[4]) for i in j] for j in [i[4].split(',') for i in L]]]
for i in range(0,40):
    print(f'{L[i][0]},{R[i]}')