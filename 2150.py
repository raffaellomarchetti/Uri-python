from collections import Counter
while True:
    try:
        alien = list(input())
        frase = Counter(input())
        cont = 0
        for vogal in alien:
            cont=cont+frase[vogal]
        print(cont)
    except EOFError:
        break