##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
L = open('data.csv','r').readlines()
L = [line.split('\t') for line in L]
dic = {t[0]:0 for t in L}

for t in L:
    dic[t[0]]+=int(t[1])

[print('{0},{1}'.format(x, y)) for x,y in sorted(dic.items())]