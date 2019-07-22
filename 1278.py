n = int(input())
palavras = []
while n > 0:
    i = n
    for i in range(n):
        palavras.append(" ".join(input().split()))
    maior_tamanho = len(max(palavras,key=len))
    for palavra in palavras:
        if palavra == '':
            print(palavra)
        else:
            print(palavra.rjust(maior_tamanho, ' '))
    n=int(input())
    if n != 0:
        palavras=['']