##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
L = open('data.csv','r').readlines()
L = [line.split('\t') for line in L]
A = []
for i in L:
    A += i[3].split(',')
A = sorted(set(A))
for i in A:
    a = 0
    for j in L:
        if(i in j[3]):
            a+=int(j[1])
    print(f'{i},{a}')