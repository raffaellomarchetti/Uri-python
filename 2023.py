lista=[]
while True:
    try:
        name = input()
        lista.append(name)
    except EOFError:
        break
lista.sort(key=str.lower)
print(lista[-1])