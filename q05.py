##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
L = open('data.csv','r').readlines()
L = [line.split('\t') for line in L]
A = [i[0] for i in L]
A = sorted(set(A))
dic = {}
for i in A:
    dic[i]=[]
for x in L:
    dic[x[0]].append(x[1])
[print(f'{i},{max(dic[i])},{min(dic[i])}') for i in dic]
