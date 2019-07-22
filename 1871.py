soma = lambda a,b: int(a)+int(b)
while True:
    a,b = input().split()
    if a=='0' and b=='0':
        break
    else:
        print(str(soma(a,b)).replace('0', ''))