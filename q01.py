##
## Imprima la suma de la segunda columna.
##
L = open('data.csv','r').readlines()
L = [line.split('\t') for line in L]
a = 0
for i in L:
    a+=int(i[1])
print(a)