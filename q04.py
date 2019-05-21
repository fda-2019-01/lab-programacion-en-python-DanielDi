##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##

L = open('data.csv','r').readlines()
L = [line.split('\t') for line in L]
L = [line[2][5:7] for line in L]
a = sorted(set(L))
[print(f'{i},{L.count(i)}') for i in a]