# -*- coding: utf-8 -*-
contador=0
lista=[]
while contador <=5:
    a=input()
    if '.' in a:
        lista.append(float(a))
    else:
        lista.append(int(a))
    contador+=1

positivo = 0
for item in lista:
    if item > 0:
        positivo+=1
print('%i valores positivos' % positivo)