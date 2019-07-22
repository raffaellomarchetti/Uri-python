n = int(input())
while n > 0:
    palavra = input()
    metade = int(len(palavra)/2)
    final = int(len(palavra))
    primeira=''
    terceira=''
    #Primeiro e segundo processo
    for letra in reversed(palavra):
        if letra.isalpha():
            primeira = primeira + chr(ord(letra)+3)
        else:
            primeira = primeira + letra
    #Terceiro processo
    for i in range(final):
        if i < metade:
            terceira = terceira + primeira[i]
        else:
            terceira = terceira + chr(ord(primeira[i])-1)
    print(terceira)
    n=n-1