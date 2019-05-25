##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
L = open('data.csv','r').readlines()
L = [line.split('\t') for line in L]
col4 = [len(i[3].split(',')) for i in L]
col5 = [len(i[4].split(',')) for i in L]
for i in range(0,len(L)):
    print(f'{L[i][0]},{col4[i]},{col5[i]}')