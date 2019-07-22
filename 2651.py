while True:
    try:
        s = input().lower()
        if 'zelda' in s:
            print('Link Bolado')
        else:
            print('Link Tranquilo')
    except EOFError:
        break