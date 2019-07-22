while True:
    try:
        n = int(input())
        match = 0
        for cont in range(n):
            especie = input()
            raca = input()
            nome = input().split()
            input()
            if len(nome)>1 and especie == 'cachorro':
                for i in nome:
                    if raca[0]==i[0]:
                        match = match+1
                        break
        print(match)
    except EOFError:
        break