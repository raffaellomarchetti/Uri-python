c=int(input())
while c > 0:
    a, b = input().split()
    a=a.lower()
    b=b.lower()
    if a=='lagarto':
        if b=='spock' or b=='papel':
            print('rajesh')
        elif b=='tesoura' or b=='pedra':
            print('sheldon')
        else:
            print('empate')
    elif a=='papel':
        if b=='pedra' or b=='spock':
            print('rajesh')
        elif b=='tesoura' or b=='lagarto':
            print('sheldon')
        else:
            print('empate')
    elif a=='pedra':
        if b=='tesoura' or b=='spock':
            print('rajesh')
        elif b=='papel' or b=='lagarto':
            print('sheldon')
        else:
            print('empate')
    elif a=='spock':
        if b=='tesoura' or b=='pedra':
            print('rajesh')
        elif b=='papel' or b=='lagarto':
            print('sheldon')
        else:
            print('empate')
    elif a=='tesoura':
        if b=='papel' or b=='lagarto':
            print('rajesh')
        elif b=='spock' or b=='pedra':
            print('sheldon')
        else:
            print('empate')
    c=c-1