while True:
    try:
        palavra = list(input())
        tam_str = len(" ".join(palavra))
        while palavra:
            print(" ".join(palavra).center(tam_str).rstrip())
            del(palavra[-1])
        print("")
    except EOFError:
        break