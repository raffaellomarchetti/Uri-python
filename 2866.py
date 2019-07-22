n = int(input())
while n > 0:
    resposta = ''
    palavra = input()
    for letra in palavra:
        if letra.islower():
            resposta = resposta + letra
    print(resposta[::-1])
    n=n-1