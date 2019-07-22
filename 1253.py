n = int(input())
while n > 0:
    cifrada = ''
    palavra = input()
    deslocamento = int(input())
    for letra in palavra:
        if ord(letra)-deslocamento >= 65:
            cifrada= cifrada + chr(ord(letra)-deslocamento)
        else:
            cifrada = cifrada + chr(91-(65-(ord(letra)-deslocamento)))
    n=n-1
    print(cifrada)