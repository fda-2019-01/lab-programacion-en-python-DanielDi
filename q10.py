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
with open('data.csv', 'r') as f:
    x = csv.reader(f,
                   delimiter='\t')

    ## se lee una linea a la vez
    print(x)
    L1 = sorted(set([i[4].split(',') for i in x]))
#    L2 = []
#    for i in x:
#        L2+=i[4]
#    A = [print(i,L2.count(i)) for i in L1]
