n = int(input())
lista = []
while n > 0:
    lista.append(input().split())
    n=n-1
for elemento in lista:
    msg = ''
    for palavras in elemento:
        msg=msg+palavras[0]
    print(msg)