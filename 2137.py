while True:
    try:
        n = int(input())
        codigos = []*n
        for i in range(n):
            codigos.append(input())
        codigos.sort()
        for codigo in codigos:
            print(codigo)
    except EOFError:
        break