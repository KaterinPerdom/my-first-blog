"""a=7
v=[1,5,9,7,1,9,4]
b = []
# Parameter v is an array of integers
# The function should return an integer
def min_max_subarray(v):
    minimo = min(v)
    maximo = max(v)
    for i in range(0,a-1):
        j = a
        while(i != j):
            
            j -= 1
    return 0
###
#n = int(input())
#v = list(map(int, input().split(' ')))
print(min_max_subarray(v))
"""
lista1 = [20,1,25,37,12]
lista2 = [43,10,31,15,30]

lista3 = []
"""
for i, w in enumerate(lista1):
    lista3.append(abs(lista1[i] - lista2[i]))
    a=min(lista3)
    print("Lista {},minimo {}".format(lista3,a))
"""
def matriz(lista1,lista2):
    lista3=[]
    for i in lista1:
        for j in lista2:
            lista3.append(abs(i-j))
    print(min(lista3))

matriz(lista1,lista2)