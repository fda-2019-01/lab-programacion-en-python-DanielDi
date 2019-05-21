##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##

L = open('data.csv','rt').readlines()
L = [line.split('\t') for line in L]

let = [i[0] for i in L]
[print(f'{t},{let.count(t)}') for t in sorted(set(let))]