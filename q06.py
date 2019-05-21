##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
L = open('data.csv','r').readlines()
L = [line.split('\t') for line in L]
A = []
for i in L:
    A+=i[4].split(',')
dic = {}
for i in A:
    dic[i[0:3]]=[]
for x in A:
    dic[x[0:3]].append(x[4])
[print(f'{i},{max(dic[i])},{min(dic[i])}') for i in dic]
