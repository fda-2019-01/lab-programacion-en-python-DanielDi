import csv
##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
L = open('data.csv','r').readlines()
L = [line.split('\t') for line in L]
L1 = [line[4].split(',') for line in L]
A = []
for i in L1:
    A+=i
B = [i[0:3] for i in A]
Baux = sorted(set(B))
[print(f'{i},{B.count(i)}') for i in Baux]
#L2 = [line]
#L1 = sorted(set([i[4] for i in L]))